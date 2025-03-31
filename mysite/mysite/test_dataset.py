from playwright.sync_api import sync_playwright

# URL с dataset
dataset_url = 'https://legendary-carnival-gp75wwr5xx5cwv5j-8000.app.github.dev/dataset/'

def run_playwright():
    with sync_playwright() as p:
        # Запуск браузера
        browser = p.chromium.launch(headless=True)  # Включить headless режим
        page = browser.new_page()

        # Открываем страницу с dataset
        page.goto(dataset_url)

        # Делаем какие-то действия с dataset, например, проверяем, что он загружен
        print("Доступ к dataset успешно получен")

        # Закрываем браузер
        browser.close()

if __name__ == '__main__':
    run_playwright()