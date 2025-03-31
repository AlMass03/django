import {fetchRentals} from "../api"
import {useState, useEffect} from "react"
import {Rental} from '../types'

export const useRentals = () => {
const [rentals, setRentals] = useState<Rental[]>([])
const [loading, setLoading] = useState<boolean>(true)
const [error, setError] = useState<string | null>(null) 

useEffect(() => {
    const loadRentals = async () => {
        try {
            const data = await fetchRentals()
            setRentals(data)
        } catch (error) {
            setError("Ошибка при запуске аренды")
        }finally{
            setLoading(false)
        }
    }
    loadRentals()
},[])

    return { rentals, loading, error }
}