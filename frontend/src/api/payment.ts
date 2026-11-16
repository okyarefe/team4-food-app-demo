const BASE = '/api/payment'

export async function createPayment(data: Record<string, unknown>) {
  const res = await fetch(BASE, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify(data),
  })
  if (!res.ok) throw new Error('Could not save')
  return res.json()
}

export async function listPayments() {
  const res = await fetch(BASE)
  if (!res.ok) throw new Error('Failed to load payments')
  return res.json()
}
