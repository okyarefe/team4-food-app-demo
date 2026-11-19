import { useState } from 'react'

export default function OrderForm() {
  const [form, setForm] = useState<Record<string, string>>({})

  function update(field: string, value: string) {
    setForm(prev => ({ ...prev, [field]: value }))
  }

  return (
    <form className="orders-form">
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
    </form>
  )
}
