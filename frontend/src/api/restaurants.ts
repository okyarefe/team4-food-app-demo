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
