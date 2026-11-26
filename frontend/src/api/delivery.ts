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
