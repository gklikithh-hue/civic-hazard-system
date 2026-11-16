import { useState } from 'react'

const API_URL = 'http://localhost:8000/api/analyze'

function App() {
  const [file, setFile] = useState(null)
  const [form, setForm] = useState({
    description: '',
    location_name: '',
    context: 'busy_road',
    area_type: 'urban'
  })
  const [result, setResult] = useState(null)
  const [loading, setLoading] = useState(false)

  const handleChange = (e) => {
    setForm({ ...form, [e.target.name]: e.target.value })
  }

  const handleSubmit = async (e) => {
    e.preventDefault()

    if (!file) {
      alert('Please upload an image.')
      return
    }

    const formData = new FormData()
    formData.append('file', file)
    formData.append('description', form.description)
    formData.append('location_name', form.location_name)
    formData.append('context', form.context)
    formData.append('area_type', form.area_type)

    try {
      setLoading(true)
      const response = await fetch(API_URL, {
        method: 'POST',
        body: formData
      })
      const data = await response.json()
      setResult(data)
    } catch (error) {
      console.error(error)
      alert('Request failed.')
    } finally {
      setLoading(false)
    }
  }

  return (
    <div className="app-shell">
      <header className="hero">
        <h1>AI Civic Hazard Detection</h1>
        <p>Citizen safety assistant for civic hazard reporting</p>
      </header>

      <main className="layout">
        <section className="panel">
          <h2>Report a Hazard</h2>
          <form onSubmit={handleSubmit} className="report-form">
            <label>
              Upload image
              <input
                type="file"
                accept="image/*"
                onChange={(e) => setFile(e.target.files[0])}
              />
            </label>

            <label>
              Location name
              <input
                type="text"
                name="location_name"
                value={form.location_name}
                onChange={handleChange}
                placeholder="e.g., Main Road, Near School Gate"
              />
            </label>

            <label>
              Hazard description
              <textarea
                name="description"
                value={form.description}
                onChange={handleChange}
                rows="4"
                placeholder="Describe the problem"
              />
            </label>

            <label>
              Context
              <select name="context" value={form.context} onChange={handleChange}>
                <option value="busy_road">Busy Road</option>
                <option value="school_zone">School Zone</option>
                <option value="market_area">Market Area</option>
                <option value="residential">Residential</option>
                <option value="footpath">Footpath</option>
                <option value="construction_zone">Construction Zone</option>
              </select>
            </label>

            <label>
              Area type
              <select name="area_type" value={form.area_type} onChange={handleChange}>
                <option value="urban">Urban</option>
                <option value="rural">Rural</option>
                <option value="commercial">Commercial</option>
              </select>
            </label>

            <button type="submit" disabled={loading}>
              {loading ? 'Analyzing...' : 'Analyze Hazard'}
            </button>
          </form>
        </section>

        <section className="panel output-panel">
          <h2>Safety Analysis</h2>

          {!result && <p className="placeholder">Submit a photo to see the hazard assessment.</p>}

          {result && (
            <>
              <div className="badge">
                <span>Detected hazard:</span>
                <strong>{result.hazard_detected.replace('_', ' ')}</strong>
              </div>

              <div className="score-card">
                <span>Risk level</span>
                <strong>{result.severity.risk_level}</strong>
                <small>Score: {result.severity.score}/100</small>
              </div>

              <div className="impact-box">
                <h3>Human impact</h3>
                <p>{result.severity.human_impact}</p>
              </div>

              <div className="recommendation-box">
                <h3>Safety recommendations</h3>
                <ul>
                  {result.recommendations.map((item, index) => (
                    <li key={index}>{item}</li>
                  ))}
                </ul>
              </div>

              <div className="report-box">
                <h3>Generated civic report</h3>
                <p><strong>{result.report.title}</strong></p>
                <p>{result.report.summary}</p>
                <p>Location: {result.report.location_name}</p>
                <p>Priority: {result.report.risk_level}</p>
              </div>
            </>
          )}
        </section>
      </main>
    </div>
  )
}

export default App
