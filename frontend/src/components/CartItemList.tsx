import { useEffect, useState } from 'react'
import { listCartItems } from '../api/cart'

export default function CartItemList() {
  const [items, setItems] = useState<any[]>([])
  const [loading, setLoading] = useState(true)

  useEffect(() => {
    listCartItems()
      .then(setItems)
      .finally(() => setLoading(false))
  }, [])

  if (loading) return <p>Loading…</p>

  return (
    <ul className="cart-list">
      {items.map(item => (
        <li key={item.id}>{String(item.name ?? item.id)}</li>
      ))}
    </ul>
  )
}
