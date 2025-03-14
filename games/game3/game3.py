"""
Game 3: Green Clicker
A simple clicker game with a green background.
"""

import pygame

import random

BACKGROUND_COLOR = (100, 255, 100)
BUTTON_COLOR = (200, 200, 200)
BUTTON_HOVER_COLOR = (220, 220, 220)
BUTTON_TEXT_COLOR = (0, 0, 0)
BASE_CLICK_VALUE = 1
MAX_BONUS = 4


def game_init(screen, assets=None):
    font = pygame.font.SysFont(None, 36)

    button_x = random.randint(100, screen.get_width() - 300)
    button_y = random.randint(100, screen.get_height() - 200)
    button_rect = pygame.Rect(button_x, button_y, 200, 100)

    return {
        "font": font,
        "button_rect": button_rect,
        "button_hover": False,
        "move_timer": 0,
        "current_bonus": 1,
    }


def game_update(screen, state, events, dt, score):
    font = state["font"]
    button_rect = state["button_rect"]
    button_hover = state["button_hover"]
    move_timer = state["move_timer"]
    current_bonus = state["current_bonus"]
    score_change = 0

    for event in events:
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if button_rect.collidepoint(event.pos):
                score_change = BASE_CLICK_VALUE * current_bonus
                button_rect.x = random.randint(100, screen.get_width() - 300)
                button_rect.y = random.randint(100, screen.get_height() - 200)
                current_bonus = min(current_bonus + 1, MAX_BONUS)

    move_timer += dt
    if move_timer > 3.0:
        move_timer = 0
        current_bonus = 1

    mouse_pos = pygame.mouse.get_pos()
    button_hover = button_rect.collidepoint(mouse_pos)

    screen.fill(BACKGROUND_COLOR)

    pygame.draw.rect(
        screen, BUTTON_HOVER_COLOR if button_hover else BUTTON_COLOR, button_rect
    )
    pygame.draw.rect(screen, (0, 0, 0), button_rect, 2)

    text = font.render(f"Click Me (x{current_bonus})", True, BUTTON_TEXT_COLOR)
    text_rect = text.get_rect(center=button_rect.center)
    screen.blit(text, text_rect)

    score_text = font.render(f"Score: {score}", True, (0, 100, 0))
    screen.blit(score_text, (20, 20))

    game_name = font.render("Green Clicker", True, (0, 100, 0))
    screen.blit(game_name, (screen.get_width() - game_name.get_width() - 20, 20))

    timer_width = 200 * (1 - (move_timer / 3.0))
    pygame.draw.rect(screen, (50, 150, 50), (20, 60, 200, 20), 2)
    if timer_width > 0:
        pygame.draw.rect(screen, (50, 150, 50), (20, 60, timer_width, 20))

    state["button_hover"] = button_hover
    state["button_rect"] = button_rect
    state["move_timer"] = move_timer
    state["current_bonus"] = current_bonus

    return state, score_change


def game_shutdown(state):
    pass
