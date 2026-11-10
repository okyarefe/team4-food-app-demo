import { useEffect, useState } from 'react'
import { listCartItems } from '../api/cart'

type CartItem = { id: number; [key: string]: unknown }

export default function CartItemList() {
  const [items, setItems] = useState<CartItem[]>([])
  const [loading, setLoading] = useState(true)
  const [error, setError] = useState('')

  useEffect(() => {
    listCartItems()
      .then(setItems)
      .catch(err => setError(String(err)))
      .finally(() => setLoading(false))
  }, [])

  if (loading) return <p>Loading…</p>
  if (error) return <p className="error">{error}</p>
  if (items.length === 0) return <p>No cart items yet.</p>

  return (
    <ul className="cart-list">
      {items.map(item => (
        <li key={item.id}>{String(item.name ?? item.id)}</li>
      ))}
    </ul>
  )
}
