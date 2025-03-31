import dash
from dash import dcc, html
import plotly.express as px
import requests
import pandas as pd

# Инициализация Dash-приложения
app = dash.Dash(__name__)

@app.callback(
    dash.dependencies.Output('role-chart', 'figure'),
    [dash.dependencies.Input('interval-component', 'n_intervals')]
)
def update_role_chart(n):
    # Указание на API URL
    api_url = "https://legendary-carnival-gp75wwr5xx5cwv5j-8000.app.github.dev//api/users/"
    
    # Указываем заголовок для запроса, чтобы ожидать ответ в формате JSON
    headers = {"Accept": "application/json"}

    try:
        # Отправляем запрос с указанными заголовками
        response = requests.get(api_url, headers=headers, timeout=10)
        response.encoding = 'utf-8'

        # Логирование ответа для диагностики
        print(f"Response status code: {response.status_code}")
        print(f"Response headers: {response.headers}")

        # Проверяем, что ответ — JSON
        if "application/json" not in response.headers.get("Content-Type", ""):
            print("Ошибка: Ответ не в формате JSON")
            return px.bar(title="Ошибка: Сервер вернул неверный формат данных")

        data = response.json()
        print("Полученные данные:", data)

        # Проверяем, есть ли данные
        if not data:
            return px.bar(title="Ошибка: Нет данных от сервера")

        df = pd.DataFrame(data)

        # Проверяем наличие столбца 'role'
        if 'role' not in df.columns:
            return px.bar(title="Ошибка: В данных нет поля 'role'")

        # Подсчитываем количество пользователей по ролям
        role_counts = df['role'].value_counts().reset_index()
        role_counts.columns = ['Роль', 'Количество']

        if role_counts.empty:
            return px.bar(title="Нет данных для отображения")

        # Строим график
        fig = px.bar(role_counts, x='Роль', y='Количество', title='Распределение пользователей по ролям',
                     color='Роль', text_auto=True)

        return fig

    except requests.exceptions.RequestException as e:
        # Обрабатываем ошибки сетевого запроса
        print(f"Ошибка запроса: {e}")
        return px.bar(title="Ошибка соединения с сервером")
    except ValueError as e:
        # Обрабатываем ошибки при обработке JSON
        print(f"Ошибка JSON: {e}")
        return px.bar(title="Ошибка обработки данных")
    except Exception as e:
        # Обрабатываем все другие неожиданные ошибки
        print(f"Неожиданная ошибка: {e}")
        return px.bar(title="Неизвестная ошибка")

# Разметка приложения
app.layout = html.Div([
    dcc.Graph(id='role-chart'),
    dcc.Interval(
        id='interval-component',
        interval=60 * 1000,  # Интервал*
