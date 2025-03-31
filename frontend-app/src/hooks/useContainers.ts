import { useState, useEffect } from "react";
import { fetchContainers } from "../api";
import { Container } from "../types";

export const useContainers = () => {
  const [containers, setContainers] = useState<Container[]>([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    const loadContainers = async () => {
      try {
        const data = await fetchContainers();
        setContainers(data);
      } catch (err) {
        console.error(err)
        setError("Ошибка при загрузке контейнеров");
      } finally {
        setLoading(false);
      }
    };

    loadContainers();
  }, []);

  return { containers, loading, error };
};