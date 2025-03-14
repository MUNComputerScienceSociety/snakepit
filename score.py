"""Score module for games."""


def init_score():
    """Initialize score to 0."""
    return 0


def update_score(current_score, change):
    """Update score by adding change, never below 0."""
    return max(0, current_score + change)


def format_score(score):
    """Format score for display."""
    return f"Score: {score}"
