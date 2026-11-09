import { useState, type FormEvent } from 'react'
import { createUser } from '../api/auth'

export default function UserForm() {
  const [form, setForm] = useState<Record<string, string>>({})
  const [message, setMessage] = useState('')

  function update(field: string, value: string) {
    setForm(prev => ({ ...prev, [field]: value }))
  }

  async function submit(event: FormEvent) {
    event.preventDefault()
    if (!form.email) {
      setMessage('Email is required')
      return
    }
    await createUser(form)
    setMessage('Saved!')
    setForm({})
  }

  return (
    <form className="auth-form" onSubmit={submit}>
      <label>
        Email
        <input type="text" value={form.email ?? ''} onChange={e => update('email', e.target.value)} />
      </label>
      <label>
        Name
        <input type="text" value={form.name ?? ''} onChange={e => update('name', e.target.value)} />
      </label>
      <button type="submit">Save</button>
      {message && <p>{message}</p>}
    </form>
  )
}
