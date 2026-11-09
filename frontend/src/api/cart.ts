const BASE = '/api/cart'

export async function listCartItems() {
  const res = await fetch(BASE)
  if (!res.ok) throw new Error('Failed to load cart items')
  return res.json()
}

export async function getCartItem(id: number) {
  const res = await fetch(`${BASE}/${id}`)
  if (!res.ok) throw new Error('Not found')
  return res.json()
}

export async function createCartItem(data: Record<string, unknown>) {
  const res = await fetch(BASE, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify(data),
  })
  if (!res.ok) throw new Error('Could not save')
  return res.json()
}
