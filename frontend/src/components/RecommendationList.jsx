export default function RecommendationList({ result }) {
  if (!result) {
    return null
  }

  return (
    <section>
      <h2>Recommendations for {result.destination}</h2>
      <ul>
        {result.recommendations.map((recommendation) => (
          <li key={recommendation.title}>
            <h3>{recommendation.title}</h3>
            <p>{recommendation.description}</p>
          </li>
        ))}
      </ul>
    </section>
  )
}
