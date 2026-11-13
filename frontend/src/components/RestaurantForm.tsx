import { useState } from 'react'

export default function RestaurantForm() {
  const [form, setForm] = useState<Record<string, string>>({})

  function update(field: string, value: string) {
    setForm(prev => ({ ...prev, [field]: value }))
  }

  return (
    <form className="restaurants-form">
      <label>
        Name
        <input type="text" value={form.name ?? ''} onChange={e => update('name', e.target.value)} />
      </label>
      <label>
        Address
        <input type="text" value={form.address ?? ''} onChange={e => update('address', e.target.value)} />
      </label>
      <label>
        Opens at
        <input type="text" value={form.opens_at ?? ''} onChange={e => update('opens_at', e.target.value)} />
      </label>
    </form>
  )
}
