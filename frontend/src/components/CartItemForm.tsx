import { useState, type FormEvent } from 'react'
import { createCartItem } from '../api/cart'

export default function CartItemForm() {
  const [form, setForm] = useState<Record<string, string>>({})
  const [message, setMessage] = useState('')

  function update(field: string, value: string) {
    setForm(prev => ({ ...prev, [field]: value }))
  }

  async function submit(event: FormEvent) {
    event.preventDefault()
    if (!form.menu_item_id) {
      setMessage('Menu item id is required')
      return
    }
    await createCartItem(form)
    setMessage('Saved!')
    setForm({})
  }

  return (
    <form className="cart-form" onSubmit={submit}>
      <label>
        Menu item id
        <input type="number" value={form.menu_item_id ?? ''} onChange={e => update('menu_item_id', e.target.value)} />
      </label>
      <label>
        Quantity
        <input type="number" value={form.quantity ?? ''} onChange={e => update('quantity', e.target.value)} />
      </label>
      <button type="submit">Save</button>
      {message && <p>{message}</p>}
    </form>
  )
}
