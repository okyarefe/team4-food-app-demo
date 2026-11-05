const BASE = '/api/menu'

export async function listMenuItems() {
  const res = await fetch(BASE)
  if (!res.ok) throw new Error('Failed to load menu items')
  return res.json()
}

export async function getMenuItem(id: number) {
  const res = await fetch(`${BASE}/${id}`)
  if (!res.ok) throw new Error('Not found')
  return res.json()
}
