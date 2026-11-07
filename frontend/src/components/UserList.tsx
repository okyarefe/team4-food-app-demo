import { useEffect, useState } from 'react'
import { listUsers } from '../api/auth'

export default function UserList() {
  const [items, setItems] = useState<any[]>([])

  useEffect(() => {
    listUsers()
      .then(setItems)
  }, [])

  return (
    <ul className="auth-list">
      {items.map(item => (
        <li key={item.id}>{String(item.name ?? item.id)}</li>
      ))}
    </ul>
  )
}
