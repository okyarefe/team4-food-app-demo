const BASE = '/api/reviews'

export async function listReviews() {
  const res = await fetch(BASE)
  if (!res.ok) throw new Error('Failed to load reviews')
  return res.json()
}

export async function getReview(id: number) {
  const res = await fetch(`${BASE}/${id}`)
  if (!res.ok) throw new Error('Not found')
  return res.json()
}
