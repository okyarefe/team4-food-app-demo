import { useEffect, useState } from 'react'
import { listMenuItems } from '../api/menu'

export default function MenuItemList() {
  const [items, setItems] = useState<any[]>([])

  useEffect(() => {
    listMenuItems()
      .then(setItems)
  }, [])

  return (
    <ul className="menu-list">
      {items.map(item => (
        <li key={item.id}>{String(item.name ?? item.id)}</li>
      ))}
    </ul>
  )
}
