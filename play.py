# 1. камень, ножницы, бумага
import random

choices = ["камень", "ножницы", "бумага"]
computer = random.choice(choices)
player = input("Выберите: камень, ножницы или бумага? ").lower()

if player in choices:
    print(f"Компьютер выбрал: {computer}")
    if player == computer:
        print("Ничья!")
    elif (player == "камень" and computer == "ножницы") or \
         (player == "ножницы" and computer == "бумага") or \
         (player == "бумага" and computer == "камень"):
        print("Вы победили!")
    else:
        print("Компьютер победил!")
else:
    print("Ошибка ввода!")

# 2. виселица
import random

words = ["питон", "программа", "игра", "виселица"]
word = random.choice(words)
guessed = ["_"] * len(word)
attempts = 6

while attempts > 0 and "_" in guessed:
    print(" ".join(guessed))
    letter = input("Введите букву: ").lower()
    if letter in word:
        for i, char in enumerate(word):
            if char == letter:
                guessed[i] = letter
    else:
        attempts -= 1
        print(f"Ошибка! Осталось попыток: {attempts}")

if "_" not in guessed:
    print("Победа! Слово:", word)
else:
    print("Поражение! Слово было:", word)

# 3. змейка

import pygame
import time

pygame.init()
screen = pygame.display.set_mode((400, 300))
pygame.display.set_caption("Змейка")

snake = [(100, 100), (90, 100), (80, 100)]
direction = "RIGHT"

clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and direction != "DOWN":
                direction = "UP"
            elif event.key == pygame.K_DOWN and direction != "UP":
                direction = "DOWN"
            elif event.key == pygame.K_LEFT and direction != "RIGHT":
                direction = "LEFT"
            elif event.key == pygame.K_RIGHT and direction != "LEFT":
                direction = "RIGHT"

    # Движение змейки
    head = snake[0]
    if direction == "UP":
        new_head = (head[0], head[1] - 10)
    elif direction == "DOWN":
        new_head = (head[0], head[1] + 10)
    elif direction == "LEFT":
        new_head = (head[0] - 10, head[1])
    else:
        new_head = (head[0] + 10, head[1])
    snake.insert(0, new_head)
    snake.pop()

    # Отрисовка
    screen.fill((0, 0, 0))
    for segment in snake:
        pygame.draw.rect(screen, (0, 255, 0), (segment[0], segment[1], 10, 10))
    pygame.display.update()
    clock.tick(15)

# 4. угадай число

import random

number = random.randint(1, 100)
attempts = 0

while True:
    guess = int(input("Угадайте число от 1 до 100: "))
    attempts += 1
    if guess < number:
        print("Слишком мало!")
    elif guess > number:
        print("Слишком много!")
    else:
        print(f"Поздравляем! Вы угадали за {attempts} попыток.")
        break

  
