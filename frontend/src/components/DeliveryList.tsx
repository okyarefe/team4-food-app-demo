import { useEffect, useState } from 'react'
import { listDeliveries } from '../api/delivery'

type Delivery = { id: number; [key: string]: unknown }

export default function DeliveryList() {
  const [items, setItems] = useState<Delivery[]>([])
  const [loading, setLoading] = useState(true)
  const [error, setError] = useState('')

  useEffect(() => {
    listDeliveries()
      .then(setItems)
      .catch(err => setError(String(err)))
      .finally(() => setLoading(false))
  }, [])

  if (loading) return <p>Loading…</p>
  if (error) return <p className="error">{error}</p>
  if (items.length === 0) return <p>No deliveries yet.</p>

  return (
    <ul className="delivery-list">
      {items.map(item => (
        <li key={item.id}>{String(item.name ?? item.id)}</li>
      ))}
    </ul>
  )
}
