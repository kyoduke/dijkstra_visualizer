# Visualizador do Algoritmo de Dijkstra para uma Mina de Carvão (Grid 2D) usando pygame

import pygame
from queue import PriorityQueue
import sys
from utils.colors import *
from utils.node import Node
from utils.button import Button

WIDTH = 600
BUTTON_HEIGHT = 40
WIN = pygame.display.set_mode((WIDTH, WIDTH + BUTTON_HEIGHT))
pygame.display.set_caption("Visualização do Algoritmo de Dijkstra (Mina de Carvão)")
pygame.init()

def reconstruct_path(came_from, current, draw):
    while current in came_from:
        current = came_from[current]
        if not current.is_start():
            current.make_path()
        draw()

def dijkstra(draw, grid, start, end):
    count = 0
    open_set = PriorityQueue()
    open_set.put((0, count, start))
    distances = {node: float("inf") for row in grid for node in row}
    distances[start] = 0
    came_from = {}

    open_set_hash = {start}

    while not open_set.empty():
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        current = open_set.get()[2]
        open_set_hash.remove(current)

        if current == end:
            reconstruct_path(came_from, end, draw)
            end.make_end()
            start.make_start()
            return True

        for neighbor in current.neighbors:
            temp_dist = distances[current] + 1  # All edges have weight 1
            if temp_dist < distances[neighbor]:
                came_from[neighbor] = current
                distances[neighbor] = temp_dist
                if neighbor not in open_set_hash:
                    count += 1
                    open_set.put((distances[neighbor], count, neighbor))
                    open_set_hash.add(neighbor)
                    neighbor.make_open()

        draw()

        if current != start:
            current.make_closed()

    return False

def make_grid(rows, width):
    grid = []
    gap = width // rows
    for i in range(rows):
        grid.append([])
        for j in range(rows):
            node = Node(i, j, gap, rows)
            grid[i].append(node)
    return grid

def draw_grid(win, rows, width):
    gap = width // rows
    for i in range(rows):
        pygame.draw.line(win, GREY, (0, i * gap), (width, i * gap))
        for j in range(rows):
            pygame.draw.line(win, GREY, (j * gap, 0), (j * gap, width))

def draw(win, grid, rows, width, buttons):
    win.fill(WHITE)

    for row in grid:
        for node in row:
            node.draw(win)

    draw_grid(win, rows, width)

    # Draw buttons
    for button in buttons:
        button.draw(win)

    pygame.display.update()

def get_clicked_pos(pos, rows, width):
    gap = width // rows
    y, x = pos
    row = y // gap
    col = x // gap
    return row, col

def clear_path(grid):
    for row in grid:
        for node in row:
            if node.is_path() or node.is_closed() or node.is_open():
                node.reset()

def draw_welcome_screen(win):
    win.fill(WHITE)

    # Title
    font_title = pygame.font.SysFont('arial', 30, bold=True)
    title_text = font_title.render("Visualizador do Algoritmo de Dijkstra", True, BLACK)
    win.blit(title_text, (WIDTH//2 - title_text.get_width()//2, 50))

    # Subtitle
    font_subtitle = pygame.font.SysFont('arial', 22)
    subtitle_text = font_subtitle.render("Simulação de Busca de Caminho em Mina de Carvão", True, DARK_GREY)
    win.blit(subtitle_text, (WIDTH//2 - subtitle_text.get_width()//2, 90))

    # Instructions
    font_instructions = pygame.font.SysFont('arial', 15)
    instructions = [
        "Este visualizador demonstra o algoritmo de Dijkstra para busca de caminhos.",
        "Instruções:",
        "• Primeiro clique: Coloca o ponto de início (laranja)",
        "• Segundo clique: Coloca o ponto de destino (turquesa)",
        "• Arrastar mouse: Cria barreiras (preto)",
        "• Clique direito: Apaga elementos",
        "",
        "Após definir os pontos de início e fim, clique em 'Iniciar Algoritmo'",
        "para visualizar como o algoritmo de Dijkstra encontra o menor caminho."
    ]

    y_pos = 140
    for line in instructions:
        text = font_instructions.render(line, True, BLACK)
        win.blit(text, (WIDTH//2 - text.get_width()//2, y_pos))
        y_pos += 25

    # Color Legend
    y_pos += 5
    legend_title = font_instructions.render("Legenda de Cores:", True, BLACK)
    win.blit(legend_title, (WIDTH//2 - legend_title.get_width()//2, y_pos))
    y_pos += 25

    # Reorganized legend to avoid text overlap
    legend_items = [
        (ORANGE, "Ponto de Início"),
        (TURQUOISE, "Ponto de Destino"),
        (BLACK, "Barreira"),
        (GREEN, "Fronteira"),
        (RED, "Visitado"),
        (YELLOW, "Caminho")
    ]

    left_x = WIDTH//2 - 180
    right_x = WIDTH//2 + 20

    # First row
    pygame.draw.rect(win, legend_items[0][0], (left_x, y_pos, 20, 20))
    label_text = font_instructions.render(legend_items[0][1], True, BLACK)
    win.blit(label_text, (left_x + 30, y_pos))

    pygame.draw.rect(win, legend_items[1][0], (right_x, y_pos, 20, 20))
    label_text = font_instructions.render(legend_items[1][1], True, BLACK)
    win.blit(label_text, (right_x + 30, y_pos))

    y_pos += 25

    # Second row
    pygame.draw.rect(win, legend_items[2][0], (left_x, y_pos, 20, 20))
    label_text = font_instructions.render(legend_items[2][1], True, BLACK)
    win.blit(label_text, (left_x + 30, y_pos))

    pygame.draw.rect(win, legend_items[3][0], (right_x, y_pos, 20, 20))
    label_text = font_instructions.render(legend_items[3][1], True, BLACK)
    win.blit(label_text, (right_x + 30, y_pos))

    y_pos += 25

    # Third row
    pygame.draw.rect(win, legend_items[4][0], (left_x, y_pos, 20, 20))
    label_text = font_instructions.render(legend_items[4][1], True, BLACK)
    win.blit(label_text, (left_x + 30, y_pos))

    pygame.draw.rect(win, legend_items[5][0], (right_x, y_pos, 20, 20))
    label_text = font_instructions.render(legend_items[5][1], True, BLACK)
    win.blit(label_text, (right_x + 30, y_pos))

    y_pos += 40

    # Create start button
    start_app_button = Button(WIDTH//2 - 100, y_pos, 200, 50, "Iniciar Aplicação", LIGHT_BLUE, GREEN, BLACK)
    start_app_button.draw(win)

    pygame.display.update()
    return start_app_button

def main(win, width):
    ROWS = 30
    grid = make_grid(ROWS, width)

    start = None
    end = None

    run = True
    started = False
    show_welcome = True

    # Create buttons for the main application
    button_width = (width - 40) // 3

    start_button = Button(10, width + 5, button_width, 30, "Iniciar Algoritmo", LIGHT_GREY, GREEN)
    clear_button = Button(20 + button_width, width + 5, button_width, 30, "Limpar Caminho", LIGHT_GREY, YELLOW)
    reset_button = Button(30 + 2 * button_width, width + 5, button_width, 30, "Reiniciar Tudo", LIGHT_GREY, RED)

    buttons = [start_button, clear_button, reset_button]

    # Welcome screen button
    start_app_button = None

    while run:
        mouse_pos = pygame.mouse.get_pos()

        # Show welcome screen or main application
        if show_welcome:
            if start_app_button is None:
                start_app_button = draw_welcome_screen(win)
            else:
                start_app_button.check_hover(mouse_pos)
                start_app_button.draw(win)
                pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    if start_app_button.is_clicked(mouse_pos, True):
                        show_welcome = False
                        # Reset the display for the main application
                        win.fill(WHITE)
        else:
            # Main application
            # Update button hover states
            for button in buttons:
                button.check_hover(mouse_pos)

            draw(win, grid, ROWS, width, buttons)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                    pygame.quit()
                    sys.exit()

                # Track mouse button state
                left_mouse_pressed = pygame.mouse.get_pressed()[0]  # LEFT
                right_mouse_pressed = pygame.mouse.get_pressed()[2]  # RIGHT

                # Handle button clicks and drawing on grid
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:  # Left click
                    # Check if buttons were clicked
                    if start_button.is_clicked(mouse_pos, True) and not started and start and end:
                        for row in grid:
                            for node in row:
                                node.update_neighbors(grid)
                        started = True
                        dijkstra(lambda: draw(win, grid, ROWS, width, buttons), grid, start, end)
                        started = False

                    elif clear_button.is_clicked(mouse_pos, True) and not started:
                        clear_path(grid)

                    elif reset_button.is_clicked(mouse_pos, True) and not started:
                        start = None
                        end = None
                        grid = make_grid(ROWS, width)

                # Handle grid interactions (both click and drag)
                if left_mouse_pressed and not started and mouse_pos[1] < width:  # Only if in the grid area
                    row, col = get_clicked_pos(mouse_pos, ROWS, width)
                    if 0 <= row < ROWS and 0 <= col < ROWS:
                        node = grid[row][col]
                        if not start and node != end:
                            start = node
                            start.make_start()
                        elif not end and node != start:
                            end = node
                            end.make_end()
                        elif node != end and node != start:
                            node.make_barrier()

                # Handle right-click (erase)
                if right_mouse_pressed and not started and mouse_pos[1] < width:  # RIGHT
                    row, col = get_clicked_pos(mouse_pos, ROWS, width)
                    if 0 <= row < ROWS and 0 <= col < ROWS:
                        node = grid[row][col]
                        node.reset()
                        if node == start:
                            start = None
                        elif node == end:
                            end = None

                # Keep keyboard shortcuts for convenience
                if event.type == pygame.KEYDOWN and not started:
                    if event.key == pygame.K_SPACE and start and end:
                        for row in grid:
                            for node in row:
                                node.update_neighbors(grid)
                        started = True
                        dijkstra(lambda: draw(win, grid, ROWS, width, buttons), grid, start, end)
                        started = False

                    if event.key == pygame.K_c:
                        start = None
                        end = None
                        grid = make_grid(ROWS, width)

                    # Add key to return to welcome screen
                    if event.key == pygame.K_ESCAPE:
                        show_welcome = True
                        start_app_button = None

    pygame.quit()

if __name__ == "__main__":
    main(WIN, WIDTH)
