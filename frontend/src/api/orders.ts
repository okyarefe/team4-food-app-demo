const BASE = '/api/orders'

export async function listOrders() {
  const res = await fetch(BASE)
  if (!res.ok) throw new Error('Failed to load orders')
  return res.json()
}
