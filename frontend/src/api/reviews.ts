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

export async function createReview(data: Record<string, unknown>) {
  const res = await fetch(BASE, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify(data),
  })
  if (!res.ok) throw new Error('Could not save')
  return res.json()
}

export async function updateReview(id: number, data: Record<string, unknown>) {
  const res = await fetch(`${BASE}/${id}`, {
    method: 'PATCH',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify(data),
  })
  if (!res.ok) throw new Error('Could not update')
  return res.json()
}
