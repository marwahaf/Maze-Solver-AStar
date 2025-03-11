import pygame

# Define constants
GRID_COLOR = [60, 150, 50]


def setting_environment(screen, w, h, shape):
    """
    Set the environment for the maze game.

    Args:
        screen: The Pygame screen object.
        w: The width of the screen.
        h: The height of the screen.
        shape: The shape of the maze.

    Returns:
        start_x: The x-coordinate of the starting point of the maze.
        start_y: The y-coordinate of the starting point of the maze.
        pas_h: The horizontal grid size.
        pas_v: The vertical grid size.
    """
    grid_size = max(min(w, h) - 40, 0)
    pas_h = grid_size // shape[1]
    pas_v = grid_size // shape[0]

    # Centered origine
    start_x = (w - shape[1] * pas_h) // 2
    start_y = (h - shape[0] * pas_v) // 2

    for i in range(shape[1] + 1):
        start_pos_h = [start_x + i * pas_h, start_y]
        end_pos_h = [start_x + i * pas_h, start_y + pas_v * shape[0]]
        pygame.draw.line(screen, GRID_COLOR, start_pos_h, end_pos_h, 2)

    for i in range(shape[0] + 1):
        start_pos_v = [start_x, start_y + i * pas_v]
        end_pos_v = [start_x + pas_h * shape[1], start_y + i * pas_v]
        pygame.draw.line(screen, GRID_COLOR, start_pos_v, end_pos_v, 2)

    return start_x, start_y, pas_h, pas_v


def game_play(screen, src, dest, maze, start_x, start_y, pas_h, pas_v, right_path):
    """
    Visualize the gameplay by drawing the source, destination, grid, and path on the screen.

    Args:
        screen: The Pygame screen object.
        src: The coordinates of the source cell.
        dest: The coordinates of the destination cell.
        maze: The 2D array representing the maze.
        start_x: The x-coordinate of the starting point of the maze.
        start_y: The y-coordinate of the starting point of the maze.
        pas_h: The horizontal grid size.
        pas_v: The vertical grid size.
        right_path: The path to the destination cell.
    """

    # Draw the grid (1 for unblocked, 0 for blocked)
    for i in range(len(maze)):
        for j in range(len(maze[0])):
            if maze[i][j] == 0:
                pygame.draw.rect(
                    screen,
                    "Grey",
                    (start_x + j * pas_h, start_y + i * pas_v, pas_h, pas_v),
                )

    # Draw the source and destination

    # Draw source as Red - Source is (row, col) but we need (x, y) for drawing
    pygame.draw.rect(
        screen,
        "Red",
        (start_x + src[1] * pas_h, start_y + src[0] * pas_v, pas_h, pas_v),
    )

    # Draw destination as Blue
    pygame.draw.rect(
        screen,
        "Blue",
        (start_x + dest[1] * pas_h, start_y + dest[0] * pas_v, pas_h, pas_v),
    )

    # Draw the right path
    if right_path:
        for i in range(len(right_path) - 1):
            (row, col) = right_path[i]
            (future_row, future_col) = right_path[i + 1]

            x1 = start_x + col * pas_h + pas_h // 2
            y1 = start_y + row * pas_v + pas_v // 2

            x2 = start_x + future_col * pas_h + pas_h // 2
            y2 = start_y + future_row * pas_v + pas_v // 2

            pygame.draw.line(screen, "Green", (x1, y1), (x2, y2), 3)  # Thinner line


def main(maze, src, dest, right_path, shape):
    """
    Main loop for pygame.

    Args:
        maze: The 2D array representing the maze.
        src: The coordinates of the source cell.
        dest: The coordinates of the destination cell.
        right_path: The path to the destination cell.
        shape: The shape of the maze.
    """
    pygame.init()
    screen = pygame.display.set_mode((1280, 720))
    clock = pygame.time.Clock()
    running = True

    # Game setup
    w, h = screen.get_width(), screen.get_height()

    while running:
        # poll for events
        # pygame.QUIT event means the user clicked X to close your window
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # fill the screen with a color to wipe away anything from last frame
        screen.fill("black")

        # Game played
        start_x, start_y, pas_h, pas_v = setting_environment(screen, w, h, shape)
        game_play(screen, src, dest, maze, start_x, start_y, pas_h, pas_v, right_path)

        # flip() the display to put your work on screen
        pygame.display.flip()
        clock.tick(60)  # limits FPS to 60

    pygame.quit()
