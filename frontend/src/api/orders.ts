const BASE = '/api/orders'

export async function listOrders() {
  const res = await fetch(BASE)
  if (!res.ok) throw new Error('Failed to load orders')
  return res.json()
}

export async function getOrder(id: number) {
  const res = await fetch(`${BASE}/${id}`)
  if (!res.ok) throw new Error('Not found')
  return res.json()
}
