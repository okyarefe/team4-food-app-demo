import { useEffect, useState } from 'react'
import { listUsers } from '../api/auth'

type User = { id: number; [key: string]: unknown }

export default function UserList() {
  const [items, setItems] = useState<User[]>([])
  const [loading, setLoading] = useState(true)
  const [error, setError] = useState('')

  useEffect(() => {
    listUsers()
      .then(setItems)
      .catch(err => setError(String(err)))
      .finally(() => setLoading(false))
  }, [])

  if (loading) return <p>Loading…</p>
  if (error) return <p className="error">{error}</p>
  if (items.length === 0) return <p>No users yet.</p>

  return (
    <ul className="auth-list">
      {items.map(item => (
        <li key={item.id}>{String(item.name ?? item.id)}</li>
      ))}
    </ul>
  )
}
