import { useEffect, useState } from 'react'
import { listDeliveries } from '../api/delivery'

export default function DeliveryList() {
  const [items, setItems] = useState<any[]>([])

  useEffect(() => {
    listDeliveries()
      .then(setItems)
  }, [])

  return (
    <ul className="delivery-list">
      {items.map(item => (
        <li key={item.id}>{String(item.name ?? item.id)}</li>
      ))}
    </ul>
  )
}
