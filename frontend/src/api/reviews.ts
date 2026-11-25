const BASE = '/api/reviews'

export async function listReviews() {
  const res = await fetch(BASE)
  if (!res.ok) throw new Error('Failed to load reviews')
  return res.json()
}
