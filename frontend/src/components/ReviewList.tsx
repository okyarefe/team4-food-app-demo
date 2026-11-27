import { useEffect, useState } from 'react'
import { listReviews } from '../api/reviews'

export default function ReviewList() {
  const [items, setItems] = useState<any[]>([])
  const [loading, setLoading] = useState(true)

  useEffect(() => {
    listReviews()
      .then(setItems)
      .finally(() => setLoading(false))
  }, [])

  if (loading) return <p>Loading…</p>

  return (
    <ul className="reviews-list">
      {items.map(item => (
        <li key={item.id}>{String(item.name ?? item.id)}</li>
      ))}
    </ul>
  )
}
