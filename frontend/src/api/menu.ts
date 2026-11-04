const BASE = '/api/menu'

export async function listMenuItems() {
  const res = await fetch(BASE)
  if (!res.ok) throw new Error('Failed to load menu items')
  return res.json()
}
