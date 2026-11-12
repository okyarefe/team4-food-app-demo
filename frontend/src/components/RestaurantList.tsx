import { useEffect, useState } from 'react'
import { listRestaurants } from '../api/restaurants'

type Restaurant = { id: number; [key: string]: unknown }

export default function RestaurantList() {
  const [items, setItems] = useState<Restaurant[]>([])
  const [loading, setLoading] = useState(true)
  const [error, setError] = useState('')

  useEffect(() => {
    listRestaurants()
      .then(setItems)
      .catch(err => setError(String(err)))
      .finally(() => setLoading(false))
  }, [])

  if (loading) return <p>Loading…</p>
  if (error) return <p className="error">{error}</p>
  if (items.length === 0) return <p>No restaurants yet.</p>

  return (
    <ul className="restaurants-list">
      {items.map(item => (
        <li key={item.id}>{String(item.name ?? item.id)}</li>
      ))}
    </ul>
  )
}
