import { useState } from 'react'

export default function UserForm() {
  const [form, setForm] = useState<Record<string, string>>({})

  function update(field: string, value: string) {
    setForm(prev => ({ ...prev, [field]: value }))
  }

  return (
    <form className="auth-form">
      <label>
        Email
        <input type="text" value={form.email ?? ''} onChange={e => update('email', e.target.value)} />
      </label>
    </form>
  )
}
