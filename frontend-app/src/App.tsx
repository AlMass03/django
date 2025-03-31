import ContainerList from "./components/UserList/ContainerList"
import RentalList from "./components/UserList/RentalsList"
import UsersList from "./components/UserList/UsersList"

function App() {

  return (
    <>
  <h1>Учетные данные СибТранс</h1>
    <ContainerList />
    <UsersList />
    <RentalList />
    </>
  )
}

export default App