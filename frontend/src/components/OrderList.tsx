import { useEffect, useState } from 'react'
import { listOrders } from '../api/orders'

export default function OrderList() {
  const [items, setItems] = useState<any[]>([])

  useEffect(() => {
    listOrders()
      .then(setItems)
  }, [])

  return (
    <ul className="orders-list">
      {items.map(item => (
        <li key={item.id}>{String(item.name ?? item.id)}</li>
      ))}
    </ul>
  )
}
