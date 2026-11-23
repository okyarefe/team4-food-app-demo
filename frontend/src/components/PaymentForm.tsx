import { useState, type FormEvent } from 'react'
import { createPayment } from '../api/payment'

export default function PaymentForm() {
  const [form, setForm] = useState<Record<string, string>>({})
  const [message, setMessage] = useState('')

  function update(field: string, value: string) {
    setForm(prev => ({ ...prev, [field]: value }))
  }

  async function submit(event: FormEvent) {
    event.preventDefault()
    console.log('submitting payment', form)
    if (!form.order_id) {
      setMessage('Order id is required')
      return
    }
    await createPayment(form)
    setMessage('Saved!')
    setForm({})
  }

  return (
    <form className="payment-form" onSubmit={submit}>
      <label>
        Order id
        <input type="number" value={form.order_id ?? ''} onChange={e => update('order_id', e.target.value)} />
      </label>
      <label>
        Amount
        <input type="number" value={form.amount ?? ''} onChange={e => update('amount', e.target.value)} />
      </label>
      <button type="submit">Save</button>
      {message && <p>{message}</p>}
    </form>
  )
}
