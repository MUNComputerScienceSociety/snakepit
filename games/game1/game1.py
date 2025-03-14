"""
Game 1: Red Clicker
A simple clicker game with a red background.
"""

import pygame

BACKGROUND_COLOR = (255, 100, 100)
BUTTON_COLOR = (200, 200, 200)
BUTTON_HOVER_COLOR = (220, 220, 220)
BUTTON_TEXT_COLOR = (0, 0, 0)
BUTTON_RECT = pygame.Rect(300, 300, 200, 100)
CLICK_VALUE = 1


def game_init(screen, assets=None):
    """Initialize the red clicker game."""
    font = pygame.font.SysFont(None, 36)

    return {"font": font, "button_rect": BUTTON_RECT, "button_hover": False}


def game_update(screen, state, events, dt, score):
    """Update and render the red clicker game."""
    font = state["font"]
    button_rect = state["button_rect"]
    button_hover = state["button_hover"]
    score_change = 0

    for event in events:
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if button_rect.collidepoint(event.pos):
                score_change = CLICK_VALUE

    mouse_pos = pygame.mouse.get_pos()
    button_hover = button_rect.collidepoint(mouse_pos)

    screen.fill(BACKGROUND_COLOR)

    pygame.draw.rect(
        screen, BUTTON_HOVER_COLOR if button_hover else BUTTON_COLOR, button_rect
    )
    pygame.draw.rect(screen, (0, 0, 0), button_rect, 2)

    text = font.render("Click Me", True, BUTTON_TEXT_COLOR)
    text_rect = text.get_rect(center=button_rect.center)
    screen.blit(text, text_rect)

    score_text = font.render(f"Score: {score}", True, (255, 255, 255))
    screen.blit(score_text, (20, 20))

    game_name = font.render("Red Clicker", True, (255, 255, 255))
    screen.blit(game_name, (screen.get_width() - game_name.get_width() - 20, 20))

    state["button_hover"] = button_hover

    # Explicitly create a tuple with two elements
    return_value = (state, score_change)
    return return_value


def game_shutdown(state):
    """Clean up the red clicker game."""
    pass
