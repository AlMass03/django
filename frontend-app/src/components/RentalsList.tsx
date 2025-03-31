import dayjs from 'dayjs';
import { useRentals } from '../../hooks/useRentals';

const RentalList = () => {
    const {rentals, loading, error} = useRentals();
    
    if(loading) return <p>Загрузка...</p>
    if(error) return <p>Ошибка...</p>

    return (
        <div>
<h2>Список Аренд</h2>
<ul>
{rentals.map((rental) => (
          <li key={rental.rental_id}>
            <strong>Начало аренды: </strong>{dayjs(rental.start_date).format("YYYY-MM-DD HH:mm:ss") || "не указан"} <br />
            <strong>Конец аренды: </strong>{dayjs(rental.end_date).format("YYYY-MM-DD HH:mm:ss") || "не указан"} <br />
            <strong>Статус:</strong> {rental.status} <br />
            <strong>Суточная ставка: </strong>{rental.daily_rate || "не указан"} <br />
            <strong>Статус:</strong> {dayjs(rental.created_at).format("YYYY-MM-DD")}
          </li>
        ))}
</ul>
        </div>

    )
}
export default RentalList;