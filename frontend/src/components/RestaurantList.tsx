import { useEffect, useState } from 'react'
import { listRestaurants } from '../api/restaurants'

export default function RestaurantList() {
  const [items, setItems] = useState<any[]>([])

  useEffect(() => {
    listRestaurants()
      .then(setItems)
  }, [])

  return (
    <ul className="restaurants-list">
      {items.map(item => (
        <li key={item.id}>{String(item.name ?? item.id)}</li>
      ))}
    </ul>
  )
}
