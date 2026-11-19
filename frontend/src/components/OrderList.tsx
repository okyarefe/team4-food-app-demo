import { useEffect, useState } from 'react'
import { listOrders } from '../api/orders'

type Order = { id: number; [key: string]: unknown }

export default function OrderList() {
  const [items, setItems] = useState<Order[]>([])
  const [loading, setLoading] = useState(true)
  const [error, setError] = useState('')

  useEffect(() => {
    listOrders()
      .then(setItems)
      .catch(err => setError(String(err)))
      .finally(() => setLoading(false))
  }, [])

  if (loading) return <p>Loading…</p>
  if (error) return <p className="error">{error}</p>
  if (items.length === 0) return <p>No orders yet.</p>

  return (
    <ul className="orders-list card">
      {items.map(item => (
        <li key={item.id}>{String(item.name ?? item.id)}</li>
      ))}
    </ul>
  )
}
