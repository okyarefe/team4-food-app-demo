const BASE = '/api/restaurants'

export async function listRestaurants() {
  const res = await fetch(BASE)
  if (!res.ok) throw new Error('Failed to load restaurants')
  return res.json()
}
