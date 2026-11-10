import { useEffect, useState } from 'react'
import { listCartItems } from '../api/cart'

export default function CartItemList() {
  const [items, setItems] = useState<any[]>([])

  useEffect(() => {
    listCartItems()
      .then(setItems)
  }, [])

  return (
    <ul className="cart-list">
      {items.map(item => (
        <li key={item.id}>{String(item.name ?? item.id)}</li>
      ))}
    </ul>
  )
}
