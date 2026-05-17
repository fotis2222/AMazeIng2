import threading
import time

import pygame

pygame.init()
screen = pygame.display.set_mode((1280, 720))
running = True
start = time.time()
start2 = time.time()
x = 10
y = 10
level = 1
speed = 1
end_time = 0
end_time2 = 0
w14_width = 500

BLACK = (0, 0, 0)


def resize_part():
    global w14_width
    while True:
        for i in range(400):
            w14_width += 1
            time.sleep(0.01)
        time.sleep(1)
        for i in range(400):
            w14_width -= 1
            time.sleep(0.01)
        time.sleep(1)


def draw_borders():
    top_b = pygame.draw.rect(screen, BLACK, pygame.Rect(0, 0, 1280, 10))
    bot_b = pygame.draw.rect(screen, BLACK, pygame.Rect(0, 710, 1280, 10))
    l_b = pygame.draw.rect(screen, BLACK, pygame.Rect(0, 0, 10, 720))
    r_b = pygame.draw.rect(screen, BLACK, pygame.Rect(1270, 0, 10, 710))
    border1 = pygame.draw.rect(screen, BLACK, pygame.Rect(455, 10, 90, 470))
    border2 = pygame.draw.rect(screen, BLACK, pygame.Rect(150, 150, 222, 222))
    border3 = pygame.draw.rect(screen, BLACK, pygame.Rect(75, 0, 10, w14_width))
    border4 = pygame.draw.rect(screen, BLACK, pygame.Rect(76, 479, 200, 10))
    border5 = pygame.draw.rect(screen, BLACK, pygame.Rect(372, 372, 10, 500))
    border6 = pygame.draw.rect(screen, BLACK, pygame.Rect(657, 75, 34, 700))
    border7 = pygame.draw.rect(screen, BLACK, pygame.Rect(657, 100, 100, 50))
    border8 = pygame.draw.rect(screen, BLACK, pygame.Rect(750, 200, 600, 50))
    border9 = pygame.draw.rect(screen, BLACK, pygame.Rect(657, 400, 555, 200))
    return [
        top_b,
        bot_b,
        l_b,
        r_b,
        border1,
        border2,
        border3,
        border4,
        border5,
        border6,
        border7,
        border8,
        border9,
    ]


def draw_edge_borders():
    top_b = pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(0, 0, 1280, 10))
    bot_b = pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(0, 710, 1280, 10))
    l_b = pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(0, 0, 10, 720))
    r_b = pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(1270, 0, 10, 710))
    return [top_b, bot_b, l_b, r_b]


def move(pressed, x, y):
    if pressed[pygame.K_w] or pressed[pygame.K_UP]:
        y -= 1
    if pressed[pygame.K_a] or pressed[pygame.K_LEFT]:
        x -= 1
    if pressed[pygame.K_s] or pressed[pygame.K_DOWN]:
        y += 1
    if pressed[pygame.K_d] or pressed[pygame.K_RIGHT]:
        x += 1
    return x, y


def move_inverted(pressed, x, y):
    if pressed[pygame.K_w] or pressed[pygame.K_UP]:
        y += 1
    if pressed[pygame.K_a] or pressed[pygame.K_LEFT]:
        x += 1
    if pressed[pygame.K_s] or pressed[pygame.K_DOWN]:
        y -= 1
    if pressed[pygame.K_d] or pressed[pygame.K_RIGHT]:
        x -= 1
    return x, y


resize_thread = threading.Thread(target=resize_part)
resize_thread.daemon = True
resize_thread.start()


def level2():
    global x, y, start2, end_time2, level
    pressed = pygame.key.get_pressed()
    x, y = move(pressed, x, y)
    screen.fill((255, 255, 0))
    p = pygame.draw.rect(screen, (255, 0, 0), pygame.Rect(x, y, 10, 10))
    borders = draw_borders()
    finishline = pygame.draw.rect(screen, (255, 128, 0), pygame.Rect(700, 650, 50, 50))
    for i in borders:
        if p.colliderect(i):
            x = 10
            y = 10
    if p.colliderect(finishline):
        level = 3
        x = 10
        y = 10
        end2 = time.time()
        end_time2 = round(end2 - start2, 2)
        print(end_time2)
        start2 = end2
    font = pygame.font.SysFont("tahoma", 20, True, True)
    text = font.render("Time: " + str(end_time), True, [255, 0, 0])
    screen.blit(text, (950, 100))


def level1():
    global x, y, end_time, start, level
    pressed = pygame.key.get_pressed()
    x, y = move(pressed, x, y)
    screen.fill((255, 0, 0))
    p = pygame.draw.rect(screen, (255, 255, 0), pygame.Rect(x, y, 50, 50))
    borders = draw_borders()
    finishline = pygame.draw.rect(screen, (255, 128, 0), pygame.Rect(700, 650, 50, 50))
    for i in borders:
        if p.colliderect(i):
            x, y = move_inverted(pressed, x, y)

    if p.colliderect(finishline):
        level = 2
        x = 10
        y = 10
        end = time.time()
        end_time = round(end - start, 2)
        print(end_time)
        start = end
    font = pygame.font.SysFont("tahoma", 20, True, True)
    text = font.render("Time: " + str(end_time), True, [255, 255, 0])
    screen.blit(text, (950, 100))


def level3():
    global y, x
    pressed = pygame.key.get_pressed()
    x, y = move(pressed, x, y)
    screen.fill((255, 128, 0))
    p = pygame.draw.rect(screen, (255, 150, 0), pygame.Rect(x, y, 100, 100))
    borders = draw_edge_borders()
    font = pygame.font.SysFont("tahoma", 50, True, True)
    text = font.render(str("Congratulations! You won!"), True, [255, 255, 0])
    screen.blit(text, (500, 300))
    font2 = pygame.font.SysFont("tahoma", 10, True, True)
    text2 = font2.render(str("Orrrr did you?!?!?!?!?"), True, [255, 0, 0])
    screen.blit(text2, (500, 700))
    text3 = font.render("Total timer:" + str(end_time + end_time2), True, [255, 0, 0])
    screen.blit(text3, (800, 200))
    for i in borders:
        if p.colliderect(i):
            x, y = move_inverted(pressed, x, y)


def main():
    global running
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        if level == 1:
            level1()
        if level == 2:
            level2()
        if level == 3:
            level3()

        pygame.display.flip()


if __name__ == "__main__":
    main()
