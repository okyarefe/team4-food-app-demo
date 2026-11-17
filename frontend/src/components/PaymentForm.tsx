import { useState } from 'react'

export default function PaymentForm() {
  const [form, setForm] = useState<Record<string, string>>({})

  function update(field: string, value: string) {
    setForm(prev => ({ ...prev, [field]: value }))
  }

  return (
    <form className="payment-form">
      <label>
        Order id
        <input type="number" value={form.order_id ?? ''} onChange={e => update('order_id', e.target.value)} />
      </label>
      <label>
        Amount
        <input type="number" value={form.amount ?? ''} onChange={e => update('amount', e.target.value)} />
      </label>
    </form>
  )
}
