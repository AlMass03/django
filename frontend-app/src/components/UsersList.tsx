import {useUsers} from '../../hooks/useUserList'
import dayjs from "dayjs";

const UsersList = () => {
  const {users, loading, error} = useUsers();

  if(loading) return <p>Загрузка...</p>
  if(error) return <p>Ошибка...</p>

  return (
    <div>
      <h2>Список пользователей</h2>
      <ul>
        {users.map((user) => (
          <li key={user.user_id}>
            <strong>Имя: </strong>{user.name || "не указан"} <br />
            <strong>Почта: </strong>{user.email || "не указан"} <br />
            <strong>Роль: </strong>{user.role || "не указан"} <br />
            <strong>Создан:</strong> {dayjs(user.created_at).format("YYYY-MM-DD")}
          </li>
        ))}
      </ul>
    </div>
  )
}

export default UsersList;