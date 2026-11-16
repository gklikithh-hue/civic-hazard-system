from typing import Any, Dict

def generate_complaint_report(
    hazard_name: str,
    description: str,
    location_name: str,
    latitude: float | None,
    longitude: float | None,
    severity: Dict[str, Any]
) -> Dict[str, Any]:
    title = hazard_name.replace("_", " ").title()
    summary = (
        f"Detected a {title} hazard near {location_name or 'reported location'}. "
        f"The system estimates the risk level as {severity['risk_level']}."
    )

    return {
        "title": f"Urgent civic hazard: {title}",
        "summary": summary,
        "risk_level": severity["risk_level"],
        "score": severity["score"],
        "location_name": location_name or "Not given",
        "coordinates": {
            "latitude": latitude,
            "longitude": longitude
        },
        "message": (
            f"Citizen report: {description or 'No description provided'}. "
            f"Potential impact: {severity['human_impact']}"
        )
    }
