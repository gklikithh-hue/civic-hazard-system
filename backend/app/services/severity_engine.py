from typing import Any, Dict

BASE_SEVERITY = {
    "pothole": 78,
    "open_manhole": 92,
    "exposed_wire": 96,
    "waterlogging": 72,
    "garbage_blocked_drain": 68,
    "damaged_streetlight": 64,
    "broken_footpath": 74,
    "garbage_dump": 58
}

CONTEXT_MULTIPLIER = {
    "busy_road": 1.18,
    "school_zone": 1.22,
    "market_area": 1.12,
    "residential": 0.95,
    "construction_zone": 1.08,
    "footpath": 1.10,
    "unknown": 1.0
}

def compute_risk_level(score: float) -> str:
    if score >= 90:
        return "critical"
    if score >= 75:
        return "high"
    if score >= 50:
        return "medium"
    return "low"

def evaluate_hazard(hazard_name: str, context: str = "busy_road", area_type: str = "urban") -> Dict[str, Any]:
    base = BASE_SEVERITY.get(hazard_name, 60)
    context_weight = CONTEXT_MULTIPLIER.get(context, 1.0)
    area_factor = 1.05 if area_type.lower() in ["urban", "commercial"] else 1.0

    score = base * context_weight * area_factor
    score = max(10, min(99, round(score, 1)))

    human_impact_map = {
        "pothole": "Can cause vehicle damage, accidents, and falls for riders and pedestrians.",
        "open_manhole": "May lead to severe injury if someone steps into it or if a vehicle hits it.",
        "exposed_wire": "May cause electrocution or fire hazard near pedestrians and vehicles.",
        "waterlogging": "Creates slippery roads, reduces visibility, and may cause skidding.",
        "garbage_blocked_drain": "Can cause flooding, stagnation, and mosquito breeding risk.",
        "damaged_streetlight": "Reduces visibility and raises risk of accidents at night.",
        "broken_footpath": "Increases trip and fall risk for pedestrians, especially children and elders.",
        "garbage_dump": "May cause hygiene issues, blocked paths, and public health concerns."
    }

    return {
        "hazard": hazard_name,
        "score": score,
        "risk_level": compute_risk_level(score),
        "human_impact": human_impact_map.get(hazard_name, "May affect public safety and require quick action.")
    }
