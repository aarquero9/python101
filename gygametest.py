import pygame
import sys

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1080, 720))
clock = pygame.time.Clock()
running = True
dt = 0

player_radius = 10
player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)
score = 0
game_over = False
win = False

# Define your maze structure
maze = [
    "######################",
    "##o  ####x####o    o##",
    "#### #### ##### ### ##",
    "####o####o#####  o# ##",
    "#o     ## ######### ##",
    "###### ##   o  #### ##",
    "### o  #######      ##",
    "### ########## #######",
    "### ######  o  #######",
    "###o        ##########",
    "########## ###########",
    "########## ###########",
    "          P           ",
]

# Hide the mouse cursor
pygame.mouse.set_visible(False)

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                running = False
            elif event.key == pygame.K_r:  # Restart the game
            # Reset game variables
                player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)
                score = 0
                game_over = False
                win = False
                # Reset maze to its initial state
                maze = [
                    "######################",
                    "##o  ####x####o    o##",
                    "#### #### ##### ### ##",
                    "####o####o#####  o# ##",
                    "#o     ## ######### ##",
                    "###### ##   o  #### ##",
                    "### o  #######      ##",
                    "### ########## #######",
                    "### ######  o  #######",
                    "###o        ##########",
                    "########## ###########",
                    "########## ###########",
                    "          P           ",
                ]

    if not game_over and not win:
        # fill the screen with a color to wipe away anything from last frame
        screen.fill((0, 255, 255))  # Background color

        # Get the mouse position
        mouse_x, mouse_y = pygame.mouse.get_pos()

        # Update the player position to follow the mouse
        player_pos.x = mouse_x
        player_pos.y = mouse_y

        # Check for collision with maze walls and 'x'
        for y, row in enumerate(maze):
            for x, cell in enumerate(row):
                if cell == "#":
                    wall_rect = pygame.Rect(x * 50, y * 50, 50, 50)
                    if wall_rect.colliderect(
                        pygame.Rect(
                            player_pos.x - player_radius,
                            player_pos.y - player_radius,
                            player_radius * 2,
                            player_radius * 2,
                        )
                    ):
                        game_over = True  # Set game over if player hits a wall
                elif cell == "x":
                    x_rect = pygame.Rect(x * 50, y * 50, 50, 50)
                    if x_rect.colliderect(
                        pygame.Rect(
                            player_pos.x - player_radius,
                            player_pos.y - player_radius,
                            player_radius * 2,
                            player_radius * 2,
                        )
                    ):
                        win = True  # Set win if player touches 'x'
                        score += 10  # Increment score

                elif cell == "o":
                    coin_rect = pygame.Rect(x * 50 + 5, y * 50 + 5, 40, 40)
                    pygame.draw.circle(screen, (255, 255, 0), (x * 50 + 25, y * 50 + 25), 20)
                    if coin_rect.colliderect(
                        pygame.Rect(
                            player_pos.x - player_radius,
                            player_pos.y - player_radius,
                            player_radius * 2,
                            player_radius * 2,
                        )
                    ):
                        score += 1
                        maze[y] = maze[y][:x] + " " + maze[y][x + 1:]

        pygame.draw.circle(screen, (0, 244, 100), player_pos, player_radius)  # Player circle

        # Draw the maze
        for y, row in enumerate(maze):
            for x, cell in enumerate(row):
                if cell == "#":
                    pygame.draw.rect(screen, (255, 0, 0), pygame.Rect(x * 50, y * 50, 50, 50))
                if cell == "o":
                    pygame.draw.circle(screen, (255, 255, 0), (x * 50 + 25, y * 50 + 25), 20)

        # Draw score
        font = pygame.font.Font(None, 36)
        text = font.render(f'Score: {score}', True, (0, 0, 0))
        screen.blit(text, (10, 10))

    # Show game over screen
    if game_over:
        screen.fill((0, 0, 0))  # Black screen for game over
        font = pygame.font.Font(None, 64)
        text = font.render("Game Over", True, (255, 0, 0))
        screen.blit(text, (400, 300))
        text = font.render(f'Score: {score}', True, (255, 255, 255))
        screen.blit(text, (420, 400))

    # Show win screen
    if win:
        screen.fill((0, 0, 0))  # Black screen for win
        font = pygame.font.Font(None, 64)
        text = font.render("You Win!", True, (0, 255, 0))
        screen.blit(text, (420, 300))
        text = font.render(f'Score: {score}', True, (255, 255, 255))
        screen.blit(text, (420, 400))

    # flip() the display to put your work on screen
    pygame.display.flip()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(60) / 1000

pygame.quit()
sys.exit()  # Terminate the program after pygame quits
