import pygame
import random
import sys

# Initialize pygame
pygame.init()

BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
WHITE = (255, 255, 255)
font = pygame.font.SysFont(None, 35)

paused = False
score = 0
snake_dir = (0, 0)
snake = [(480, 360), (460, 360), (440, 360), (420, 360), (400, 360)]
food = (random.randint(0, (960 - 20) // 20) * 20,
        random.randint(0, (720 - 20) // 20) * 20)

screen = pygame.display.set_mode((960, 720))
screen.fill(BLACK)  # Fill screen with black

def draw_snake(snake):
    for block in snake:
        print(block)
        pygame.draw.rect(screen, GREEN, (*block, 20, 20))

def draw_food(position):
    pygame.draw.rect(screen, RED, (*position, 20, 20))

def show_score():
    score_text = font.render(f"Score: {score}", True, WHITE)
    screen.blit(score_text, [10, 10])

def game_over():
    text = font.render("GAME OVER! Press R to restart, Q to quit or C to continue", True, WHITE)
    screen.blit(text, [160, 360])
    pygame.display.flip()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q or event.key == pygame.K_ESCAPE:
                    sys.exit()
                if event.key == pygame.K_r:
                    main(True)
                if event.key == pygame.K_c:
                    main(False)

def reset_game():
    global snake, snake_dir, paused, food, score
    snake_dir = (0, 0)
    snake = [(480, 360), (460, 360), (440, 360), (420, 360), (400, 360)]
    food = (random.randint(0, (960 - 20) // 20) * 20,
            random.randint(0, (720 - 20) // 20) * 20)
    score = 0

def continue_game():
    global snake_dir, food
    snake_dir = (0, 0)
    food = (random.randint(0, (960 - 20) // 20) * 20,
            random.randint(0, (720 - 20) // 20) * 20)

def main(flag):
    global snake, snake_dir, paused, food, score
    clock = pygame.time.Clock()
    if flag:
        reset_game()
    else:
        continue_game()

    while True:
        screen.fill(BLACK)
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    paused = not paused
                if not paused:
                    if event.key == pygame.K_UP and snake_dir != (0, 20):
                        snake_dir = (0, -20)
                    if event.key == pygame.K_DOWN and snake_dir != (0, -20):
                        snake_dir = (0, 20)
                    if event.key == pygame.K_LEFT and snake_dir != (20, 0):
                        snake_dir = (-20, 0)
                    if event.key == pygame.K_RIGHT and snake_dir != (-20, 0):
                        snake_dir = (20, 0)

        if not paused:
            head = (snake[0][0] + snake_dir[0], snake[0][1] + snake_dir[1])

            if  snake_dir != (0, 0) and (head[0] < 0 or head[0] >= 960 or
                head[1] < 0 or head[1] >= 720 or
                head in snake[1:]):
                game_over()

            snake.insert(0, head)

            if head == food:
                score += 10
                food = (random.randint(0, (960 - 20) // 20) * 20,
                        random.randint(0, (720 - 20) // 20) * 20)
            else:
                snake.pop()

        draw_snake(snake)
        draw_food(food)
        show_score()
        pygame.display.update()
        clock.tick(10)


if __name__ == "__main__":
    main(True)
