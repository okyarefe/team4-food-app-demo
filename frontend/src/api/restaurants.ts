const BASE = '/api/restaurants'

export async function listRestaurants() {
  const res = await fetch(BASE)
  if (!res.ok) throw new Error('Failed to load restaurants')
  return res.json()
}

export async function getRestaurant(id: number) {
  const res = await fetch(`${BASE}/${id}`)
  if (!res.ok) throw new Error('Not found')
  return res.json()
}

export async function createRestaurant(data: Record<string, unknown>) {
  const res = await fetch(BASE, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify(data),
  })
  if (!res.ok) throw new Error('Could not save')
  return res.json()
}
