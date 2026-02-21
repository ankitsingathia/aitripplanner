import { useState } from 'react'

import { fetchRecommendations } from './api/recommendations'
import RecommendationList from './components/RecommendationList'
import TripForm from './components/TripForm'

export default function App() {
  const [result, setResult] = useState(null)
  const [loading, setLoading] = useState(false)
  const [error, setError] = useState('')

  async function handleSubmit(payload) {
    try {
      setLoading(true)
      setError('')
      const data = await fetchRecommendations(payload)
      setResult(data)
    } catch (submitError) {
      setError(submitError.message)
    } finally {
      setLoading(false)
    }
  }

  return (
    <main>
      <h1>AI Travel Recommendation System</h1>
      <TripForm onSubmit={handleSubmit} loading={loading} />
      {error && <p>{error}</p>}
      <RecommendationList result={result} />
    </main>
  )
}
