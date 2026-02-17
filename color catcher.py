import pygame
import random
import sys

# Initialize pygame
pygame.init()

# Screen setup
WIDTH, HEIGHT = 600, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Color Catcher - Unique BSc IT Project")

clock = pygame.time.Clock()

# Colors
COLOR_LIST = {
    "red": (255, 0, 0),
    "blue": (0, 0, 255),
    "green": (0, 255, 0),
    "yellow": (255, 255, 0)
}

color_names = list(COLOR_LIST.keys())

# Paddle
paddle_width = 120
paddle_height = 20
paddle_x = WIDTH // 2 - paddle_width // 2
paddle_y = HEIGHT - 50
paddle_color_name = "red"
paddle_speed = 30

# Ball
ball_radius = 15
ball_x = random.randint(50, WIDTH - 50)
ball_y = 50
ball_color_name = random.choice(color_names)
ball_speed = 3

# Score
score = 0
font = pygame.font.SysFont("Arial", 28)
game_over = False

def reset_ball():
    global ball_x, ball_y, ball_color_name
    ball_x = random.randint(50, WIDTH - 50)
    ball_y = 50
    ball_color_name = random.choice(color_names)

# Game loop
running = True
while running:
    clock.tick(60)
    screen.fill((0, 0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT and paddle_x > 0:
                paddle_x -= paddle_speed
            if event.key == pygame.K_RIGHT and paddle_x < WIDTH - paddle_width:
                paddle_x += paddle_speed
            if event.key == pygame.K_SPACE:
                paddle_color_name = random.choice(color_names)

    if not game_over:
        # Move ball
        ball_y += ball_speed

        # Ball hits bottom
        if ball_y > HEIGHT:
            reset_ball()

        # Collision detection
        if (paddle_y < ball_y + ball_radius < paddle_y + paddle_height and
            paddle_x < ball_x < paddle_x + paddle_width):

            if ball_color_name == paddle_color_name:
                score += 1
                ball_speed += 0.2  # increase difficulty
                reset_ball()
            else:
                game_over = True

    # Draw paddle
    pygame.draw.rect(screen, COLOR_LIST[paddle_color_name],
                     (paddle_x, paddle_y, paddle_width, paddle_height))

    # Draw ball
    pygame.draw.circle(screen, COLOR_LIST[ball_color_name],
                       (ball_x, ball_y), ball_radius)

    # Draw score
    score_text = font.render(f"Score: {score}", True, (255, 255, 255))
    screen.blit(score_text, (WIDTH // 2 - score_text.get_width() // 2, 10))

    # Game Over
    if game_over:
        game_over_text = font.render("GAME OVER", True, (255, 255, 255))
        screen.blit(game_over_text,
                    (WIDTH // 2 - game_over_text.get_width() // 2,
                     HEIGHT // 2 - 20))

    pygame.display.update()

pygame.quit()
sys.exit()

