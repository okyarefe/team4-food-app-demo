import { useState, type FormEvent } from 'react'
import { createRestaurant } from '../api/restaurants'

export default function RestaurantForm() {
  const [form, setForm] = useState<Record<string, string>>({})
  const [message, setMessage] = useState('')

  function update(field: string, value: string) {
    setForm(prev => ({ ...prev, [field]: value }))
  }

  async function submit(event: FormEvent) {
    event.preventDefault()
    if (!form.name) {
      setMessage('Name is required')
      return
    }
    await createRestaurant(form)
    setMessage('Saved!')
    setForm({})
  }

  return (
    <form className="restaurants-form" onSubmit={submit}>
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
      <label>
        Closes at
        <input type="text" value={form.closes_at ?? ''} onChange={e => update('closes_at', e.target.value)} />
      </label>
      <button type="submit">Save</button>
      {message && <p>{message}</p>}
    </form>
  )
}
