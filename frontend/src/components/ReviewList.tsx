import { useEffect, useState } from 'react'
import { listReviews } from '../api/reviews'

export default function ReviewList() {
  const [items, setItems] = useState<any[]>([])

  useEffect(() => {
    listReviews()
      .then(setItems)
  }, [])

  return (
    <ul className="reviews-list">
      {items.map(item => (
        <li key={item.id}>{String(item.name ?? item.id)}</li>
      ))}
    </ul>
  )
}
