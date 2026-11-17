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

export async function createOrder(data: Record<string, unknown>) {
  const res = await fetch(BASE, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify(data),
  })
  if (!res.ok) throw new Error('Could not save')
  return res.json()
}

export async function updateOrder(id: number, data: Record<string, unknown>) {
  const res = await fetch(`${BASE}/${id}`, {
    method: 'PATCH',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify(data),
  })
  if (!res.ok) throw new Error('Could not update')
  return res.json()
}

export async function deleteOrder(id: number) {
  const res = await fetch(`${BASE}/${id}`, { method: 'DELETE' })
  return res.ok
}
