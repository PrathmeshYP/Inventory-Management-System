# theme.py

DARK = {
    "bg": "#0f172a",
    "card": "#1e293b",
    "text": "#f8fafc",
    "primary": "#38bdf8",
    "success": "#22c55e",
    "danger": "#ef4444"
}

LIGHT = {
    "bg": "#f1f5f9",
    "card": "#ffffff",
    "text": "#0f172a",
    "primary": "#0284c7",
    "success": "#16a34a",
    "danger": "#dc2626"
}

current_theme = DARK

def toggle_theme():
    global current_theme
    current_theme = LIGHT if current_theme == DARK else DARK
