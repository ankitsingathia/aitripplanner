import { useState } from 'react'

export default function TripForm({ onSubmit, loading }) {
  const [destination, setDestination] = useState('')
  const [interests, setInterests] = useState('')

  function handleSubmit(event) {
    event.preventDefault()
    onSubmit({
      destination,
      interests: interests
        .split(',')
        .map((interest) => interest.trim())
        .filter(Boolean),
    })
  }

  return (
    <form onSubmit={handleSubmit}>
      <label>
        Destination
        <input
          value={destination}
          onChange={(event) => setDestination(event.target.value)}
          placeholder="e.g. Tokyo"
          required
        />
      </label>

      <label>
        Interests (comma separated)
        <input
          value={interests}
          onChange={(event) => setInterests(event.target.value)}
          placeholder="food, museums, hiking"
        />
      </label>

      <button type="submit" disabled={loading}>
        {loading ? 'Generating...' : 'Get recommendations'}
      </button>
    </form>
  )
}
