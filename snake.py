import pygame
import random

pygame.init()

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 155, 0)

DISPLAY_WIDTH = 480
DISPLAY_HEIGHT = 272
BLOCK_SIZE = 10
FPS = 15

game_display = pygame.display.set_mode((DISPLAY_WIDTH, DISPLAY_HEIGHT))
pygame.display.set_caption('Slither')
clock = pygame.time.Clock()

font = pygame.font.SysFont(None, 25)

def draw_snake(snake_list):
    """Draws the snake on the screen."""
    for segment in snake_list:
        pygame.draw.rect(game_display, GREEN, [segment[0], segment[1], BLOCK_SIZE, BLOCK_SIZE])

def draw_text(text, color, y_offset=0):
    """Draws text on the screen."""
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect(center=(DISPLAY_WIDTH / 2, DISPLAY_HEIGHT / 2 + y_offset))
    game_display.blit(text_surface, text_rect)

def generate_apple():
    """Generates a random position for the apple."""
    return (
        random.randrange(0, DISPLAY_WIDTH - BLOCK_SIZE, BLOCK_SIZE),
        random.randrange(0, DISPLAY_HEIGHT - BLOCK_SIZE, BLOCK_SIZE)
    )

def game_loop():
    """Main game loop."""
    game_exit = False
    game_over = False

    lead_x = DISPLAY_WIDTH / 2
    lead_y = DISPLAY_HEIGHT / 2
    lead_x_change = 0
    lead_y_change = 0

    snake_list = []
    snake_length = 1
    apple_x, apple_y = generate_apple()

    while not game_exit:
        while game_over:
            game_display.fill(WHITE)
            draw_text('Game over! Press C to play again or Q to quit', RED)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_exit = True
                    game_over = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_exit = True
                        game_over = False
                    if event.key == pygame.K_c:
                        game_loop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_exit = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and lead_x_change == 0:
                    lead_x_change = -BLOCK_SIZE
                    lead_y_change = 0
                elif event.key == pygame.K_RIGHT and lead_x_change == 0:
                    lead_x_change = BLOCK_SIZE
                    lead_y_change = 0
                elif event.key == pygame.K_UP and lead_y_change == 0:
                    lead_y_change = -BLOCK_SIZE
                    lead_x_change = 0
                elif event.key == pygame.K_DOWN and lead_y_change == 0:
                    lead_y_change = BLOCK_SIZE
                    lead_x_change = 0

        if lead_x >= DISPLAY_WIDTH or lead_x < 0 or lead_y >= DISPLAY_HEIGHT or lead_y < 0:
            game_over = True

        lead_x += lead_x_change
        lead_y += lead_y_change

        game_display.fill(WHITE)
        pygame.draw.rect(game_display, RED, [apple_x, apple_y, BLOCK_SIZE, BLOCK_SIZE])

        snake_head = [lead_x, lead_y]
        snake_list.append(snake_head)
        if len(snake_list) > snake_length:
            del snake_list[0]

        if snake_head in snake_list[:-1]:
            game_over = True

        draw_snake(snake_list)
        pygame.display.update()

        if (
            lead_x < apple_x + BLOCK_SIZE and
            lead_x > apple_x - BLOCK_SIZE and
            lead_y < apple_y + BLOCK_SIZE and
            lead_y > apple_y - BLOCK_SIZE
        ):
            apple_x, apple_y = generate_apple()
            snake_length += 1

        clock.tick(FPS)

    pygame.quit()
    quit()

game_loop()