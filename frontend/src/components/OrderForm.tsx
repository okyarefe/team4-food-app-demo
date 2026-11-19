import { useState, type FormEvent } from 'react'
import { createOrder } from '../api/orders'

export default function OrderForm() {
  const [form, setForm] = useState<Record<string, string>>({})
  const [message, setMessage] = useState('')

  function update(field: string, value: string) {
    setForm(prev => ({ ...prev, [field]: value }))
  }

  async function submit(event: FormEvent) {
    event.preventDefault()
    if (!form.user_id) {
      setMessage('User id is required')
      return
    }
    await createOrder(form)
    setMessage('Saved!')
    setForm({})
  }

  return (
    <form className="orders-form" onSubmit={submit}>
      <label>
        User id
        <input type="number" value={form.user_id ?? ''} onChange={e => update('user_id', e.target.value)} />
      </label>
      <label>
        Status
        <input type="text" value={form.status ?? ''} onChange={e => update('status', e.target.value)} />
      </label>
      <label>
        Total
        <input type="number" value={form.total ?? ''} onChange={e => update('total', e.target.value)} />
      </label>
      <button type="submit">Save</button>
      {message && <p>{message}</p>}
    </form>
  )
}
