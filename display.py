import pygame
import sys

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

pygame.init()
screen_size = (800, 600)
screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption("Binary Tree Visualization")

class Node:
    def __init__(self, key, x, y):
        self.key = key
        self.left = None
        self.right = None
        self.x = x
        self.y = y

def draw_tree(node, x, y, level_width):
    if node:
        pygame.draw.circle(screen, BLACK, (x, y), 20)
        font = pygame.font.Font(None, 36)
        text = font.render(str(node.key), True, WHITE)
        screen.blit(text, (x - 10, y - 10))

        if node.left:
            pygame.draw.line(screen, BLACK, (x, y + 20), (x - level_width, y + 100), 2)
            draw_tree(node.left, x - level_width, y + 100, level_width / 2)

        if node.right:
            pygame.draw.line(screen, BLACK, (x, y + 20), (x + level_width, y + 100), 2)
            draw_tree(node.right, x + level_width, y + 100, level_width / 2)

def run_game(arr):
    clock = pygame.time.Clock()
    running = True

    level_order_traversal =arr
    root_node = build_tree(level_order_traversal)

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill(WHITE)
        draw_tree(root_node, screen_size[0] // 2, 50, 200)

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()
    sys.exit()

def build_tree(level_order):
    if not level_order:
        return None

    root = Node(level_order[0], screen_size[0] // 2, 50)
    queue = [root]
    i = 1

    while i < len(level_order):
        current_node = queue.pop(0)

        if i < len(level_order) and level_order[i] is not None:
            current_node.left = Node(level_order[i], 0, 0) 
            queue.append(current_node.left)
        i += 1
        if i < len(level_order) and level_order[i] is not None:
            current_node.right = Node(level_order[i], 0, 0) 
            queue.append(current_node.right)
        i += 1

    update_coordinates(root, screen_size[0] // 2, 50, 200)

    return root

def update_coordinates(node, x, y, level_width):
    if node:
        node.x = x
        node.y = y

        if node.left:
            update_coordinates(node.left, x - level_width, y + 100, level_width / 2)

        if node.right:
            update_coordinates(node.right, x + level_width, y + 100, level_width / 2)

run_game( [1, 2, 3, 4, None, 5, 6, None, None, None, None, 7])
