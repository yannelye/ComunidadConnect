import re

# Phrasebook: English → simple Spanish
PHRASEBOOK = {
    "evacuate": "evacuar",
    "shelter": "refugio",
    "evacuation": "evacuación",
    "police": "la policía",
    "do not": "no",
    "don't": "no",
    "call 911": "llame al 911",
    "medical attention": "atención médica",
    "immigration": "inmigración",
    "legal assistance": "asistencia legal",
    "food bank": "banco de alimentos",
    "appointment": "cita",
    "free": "gratuito"
}

def translate_to_spanish_simplified(text):
    """
    Translates text to a simple, accessible Spanish using the PHRASEBOOK.
    Returns a single string with a prepended message.
    """
    text = text.strip()
    low = text.lower()
    # Replace phrases from PHRASEBOOK
    for en, es in PHRASEBOOK.items():
        low = re.sub(r"\b" + re.escape(en) + r"\b", es, low)
    
    # Capitalize sentences
    sentences = re.split(r"[.!?]+", low)
    simple = []
    for s in sentences:
        s = s.strip()
        if not s:
            continue
        s = s.capitalize()
        simple.append(s)
    
    joined = ". ".join(simple)
    if joined and not joined.endswith("."):
        joined += "."
    
    return "Mensaje en español (versión accesible): " + joined

def extract_key_actions(text):
    """
    Extracts up to 6 key actionable phrases from the input text.
    Looks for common verbs or phrases related to actions.
    """
    sentences = re.split(r"[.!?]+", text)
    actions = []
    for s in sentences:
        s = s.strip()
        if not s:
            continue
        # Look for action keywords
        if re.search(r"\b(call|go to|evacuate|go|stay|gather|leave|seek|ask for|apply|bring)\b", s.lower()):
            actions.append(s.strip())
    
    # Remove duplicates, limit to 6
    seen = []
    for a in actions:
        if a not in seen:
            seen.append(a)
    return seen[:6]
