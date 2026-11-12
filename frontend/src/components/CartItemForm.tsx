import { useState } from 'react'

export default function CartItemForm() {
  const [form, setForm] = useState<Record<string, string>>({})

  function update(field: string, value: string) {
    setForm(prev => ({ ...prev, [field]: value }))
  }

  return (
    <form className="cart-form">
      <label>
        Menu item id
        <input type="number" value={form.menu_item_id ?? ''} onChange={e => update('menu_item_id', e.target.value)} />
      </label>
      <label>
        Quantity
        <input type="number" value={form.quantity ?? ''} onChange={e => update('quantity', e.target.value)} />
      </label>
    </form>
  )
}
