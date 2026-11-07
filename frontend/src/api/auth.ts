const BASE = '/api/auth'

export async function listUsers() {
  const res = await fetch(BASE)
  if (!res.ok) throw new Error('Failed to load users')
  return res.json()
}

export async function getUser(id: number) {
  const res = await fetch(`${BASE}/${id}`)
  if (!res.ok) throw new Error('Not found')
  return res.json()
}
