from typing import List

RECOMMENDATIONS = {
    "pothole": [
        "Avoid the damaged road section and warn others nearby.",
        "Report to local municipal authorities with location details.",
        "If the pothole is on a busy road, reduce speed and use a safer route."
    ],
    "open_manhole": [
        "Do not walk or drive near the open drain area.",
        "Mark the location with visible warning signs if possible.",
        "Notify civic authorities immediately for repair."
    ],
    "exposed_wire": [
        "Keep clear of the area and do not touch the wire.",
        "Call the electricity department or emergency services.",
        "Warn nearby people if the wire is in a public area."
    ],
    "waterlogging": [
        "Avoid the flooded area to reduce risk of skidding or vehicle damage.",
        "Do not allow children or elderly to walk through deep water.",
        "Report drainage blockage or poor road drainage."
    ],
    "garbage_blocked_drain": [
        "Avoid stagnant water near the drain.",
        "Report the blocked drainage to municipal waste or drainage teams.",
        "Reduce standing water exposure to prevent mosquito breeding."
    ],
    "damaged_streetlight": [
        "Avoid poorly lit areas, especially after dark.",
        "Report the issue to the local authorities for repair.",
        "Use a flashlight or safer route if necessary."
    ],
    "broken_footpath": [
        "Use caution and walk around the damaged section.",
        "Warn pedestrians, especially elders and children.",
        "Request repair to prevent trip accidents."
    ],
    "garbage_dump": [
        "Avoid the area if there are sharp objects or contaminated waste.",
        "Report the dumping to municipal waste services.",
        "Keep distance from unattended waste piles."
    ]
}

def generate_recommendations(hazard_name: str, context: str = "busy_road") -> List[str]:
    return RECOMMENDATIONS.get(hazard_name, [
        "Avoid the unsafe area.",
        "Notify the relevant civic authority.",
        "Request immediate inspection in the reported location."
    ])
