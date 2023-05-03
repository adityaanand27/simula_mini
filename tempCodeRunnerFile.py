import pygame
import random

# Initialize pygame
pygame.init()

# Set up the window
WIDTH = 1000
HEIGHT = 580
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Traffic Simulation")

# Load images
road = pygame.image.load("simu/road.png")
grass = pygame.transform.scale(pygame.image.load("simu/grass.png"), (int(WIDTH/7), int(HEIGHT/8)))
car = pygame.image.load("simu/car.png")

# Set up variables
cars = []
spawn_rate = 0.005  # probability of a car spawning in each frame
spawn_interval = 2000  # spawn a new car every 2000ms (2 seconds)
last_spawn_time = pygame.time.get_ticks()
car_speed = 5  # pixels per frame
car_count = 0

# Spawn a new car randomly on the left side of the road
def car_spawn():
    global cars, last_spawn_time
    now = pygame.time.get_ticks()
    if now - last_spawn_time > spawn_interval:
        last_spawn_time = now
        if random.random() < spawn_rate:
            car_y = random.randint(0, HEIGHT - car.get_height())
            cars.append({
                'rect': car.get_rect(center=(0, car_y)),
                'speed': car_speed
            })

# Move the cars to the right and remove them if they go off screen
def car_move():
    global cars, car_count
    for car in cars:
        car['rect'].move_ip(car['speed'], 0)
        if car['rect'].right > WIDTH:
            cars.remove(car)
            car_count += 1

# Draw the road, grass, cars, and car count
def draw():
    screen.blit(road, (0, 70))
    for i in range(7):
        screen.blit(grass, (i*int(WIDTH/7), 0))
        screen.blit(grass, (i*int(WIDTH/7), HEIGHT-grass.get_height()))
    for car in cars:
        screen.blit(pygame.transform.flip(car['image'], True, False), car['rect'])
    font = pygame.font.SysFont(None, 30)
    text = font.render("Cars passed: " + str(car_count), True, (255, 255, 255))
    screen.blit(text, (WIDTH - text.get_width() - 10, 10))

# Run the simulation
clock = pygame.time.Clock()
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Spawn and move cars
    car_spawn()
    car_move()

    # Draw everything
    screen.fill((0, 0, 0))
    draw()
    pygame.display.flip()

    # Wait for next frame
    clock.tick(60)

# Quit pygame
pygame.quit()
