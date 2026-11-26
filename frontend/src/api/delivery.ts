const BASE = '/api/delivery'

export async function listDeliveries() {
  const res = await fetch(BASE)
  if (!res.ok) throw new Error('Failed to load deliveries')
  return res.json()
}

export async function getDelivery(id: number) {
  const res = await fetch(`${BASE}/${id}`)
  if (!res.ok) throw new Error('Not found')
  return res.json()
}

export async function createDelivery(data: Record<string, unknown>) {
  const res = await fetch(BASE, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify(data),
  })
  if (!res.ok) throw new Error('Could not save')
  return res.json()
}

export async function updateDelivery(id: number, data: Record<string, unknown>) {
  const res = await fetch(`${BASE}/${id}`, {
    method: 'PATCH',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify(data),
  })
  if (!res.ok) throw new Error('Could not update')
  return res.json()
}
