import pygame
import random

# Initialize pygame
pygame.init()

# Screen dimensions
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Catch the Falling Object")

# Colors
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)

# Player properties
player_width = 100
player_height = 20
player_x = screen_width // 2 - player_width // 2
player_y = screen_height - player_height - 10
player_speed = 10

# Object properties
object_width = 30
object_height = 30
object_x = random.randint(0, screen_width - object_width)
object_y = -object_height
object_speed = 5

# Score
score = 0
font = pygame.font.Font(None, 36)

# Game loop flag
running = True

# Main game loop
while running:
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # Player movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_x > 0:
        player_x -= player_speed
    if keys[pygame.K_RIGHT] and player_x < screen_width - player_width:
        player_x += player_speed

    # Object movement
    object_y += object_speed

    # Check if object is caught
    if (player_y < object_y + object_height and
            player_x < object_x + object_width and
            player_x + player_width > object_x):
        score += 1
        object_x = random.randint(0, screen_width - object_width)
        object_y = -object_height

    # Check if object hits the ground
    if object_y > screen_height:
        object_x = random.randint(0, screen_width - object_width)
        object_y = -object_height
    
    # Clear screen
    screen.fill(white)

    # Draw player
    pygame.draw.rect(screen, black, (player_x, player_y, player_width, player_height))

    # Draw falling object
    pygame.draw.rect(screen, red, (object_x, object_y, object_width, object_height))

    # Display score
    score_text = font.render(f"Score: {score}", True, black)
    screen.blit(score_text, (10, 10))

    # Refresh the screen
    pygame.display.flip()

    # Frame rate
    pygame.time.Clock().tick(30)

# Quit pygame
pygame.quit()