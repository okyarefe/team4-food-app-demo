const BASE = '/api/cart'

export async function listCartItems() {
  const res = await fetch(BASE)
  if (!res.ok) throw new Error('Failed to load cart items')
  return res.json()
}
