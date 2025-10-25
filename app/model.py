# model.py
from pysentimiento import create_analyzer

# Carga única para performance (se descarga la 1ª vez)
analyzer = create_analyzer(task="sentiment", lang="es")

def analiza(text: str) -> dict:
    """Retorna {'output': 'POS|NEG|NEU', 'probas': {...}}"""
    r = analyzer.predict(text)
    return {"output": r.output, "probas": r.probas}
