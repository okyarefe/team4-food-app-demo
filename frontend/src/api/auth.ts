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

export async function createUser(data: Record<string, unknown>) {
  const res = await fetch(BASE, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify(data),
  })
  if (!res.ok) throw new Error('Could not save')
  return res.json()
}

export async function updateUser(id: number, data: Record<string, unknown>) {
  const res = await fetch(`${BASE}/${id}`, {
    method: 'PATCH',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify(data),
  })
  if (!res.ok) throw new Error('Could not update')
  return res.json()
}
