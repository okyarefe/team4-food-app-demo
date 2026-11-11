import { useEffect, useState } from 'react'
import { listRestaurants } from '../api/restaurants'

export default function RestaurantList() {
  const [items, setItems] = useState<any[]>([])
  const [loading, setLoading] = useState(true)

  useEffect(() => {
    listRestaurants()
      .then(setItems)
      .finally(() => setLoading(false))
  }, [])

  if (loading) return <p>Loading…</p>

  return (
    <ul className="restaurants-list">
      {items.map(item => (
        <li key={item.id}>{String(item.name ?? item.id)}</li>
      ))}
    </ul>
  )
}
