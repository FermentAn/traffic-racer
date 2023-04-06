import pygame

pygame.init()

window_width = 840
window_height = 650
window = pygame.display.set_mode((window_width, window_height))

background_image = pygame.image.load("background.png").convert()
background_rect = background_image.get_rect()
car = pygame.image.load('car.png')
car1 = pygame.image.load('car1.jpeg')

car2 = pygame.image.load('car2.png')
car3 =pygame.image.load('car3.png')

car_rect = car.get_rect(center=[400,400])
car_speed = 5
car_rect.x = 400
car_rect.y = 400

car.set_colorkey([20,20,20])
car1.set_colorkey([27,27,27])
car2.
car3.
clock = pygame.time.Clock()

# Начальное положение фонового изображения
background_y = 0

# Скорость прокрутки заднего фона игры
scroll_speed = 5

while True:
    window.fill(pygame.Color("black"))
    window.blit(background_image, [0,0])
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
    
    # Обновляем координату начального положения фонового изображения
    background_y += scroll_speed

    # Показываем часть фонового изображения на экране
    window.blit(background_image, (0, background_y - window_height))
    window.blit(background_image, (0, background_y))
    

    # Сбросить положение фонового изображение, если оно исчезнет с экрана
    if background_y >= window_height:
        background_y = 0
    
    window.blit(car1,[325,0])
    window.blit(car,car_rect)
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        car_rect.x -= car_speed
        if car_rect.x<170:
            car_rect.x = 170
    if keys[pygame.K_RIGHT]:
        car_rect.x += car_speed
        if car_rect.x>670-car_rect.width:
            car_rect.x= 670 - car_rect.width
    if keys[pygame.K_UP]:
        car_rect.y -=car_speed
        if car_rect.y < 0:
            car_rect.y= 0
    if keys[pygame.K_DOWN]:   
        car_rect.y +=car_speed
        if car_rect.y > 650 - car_rect.height:
            car_rect.y= 650 - car_rect.height

    # update the display
    pygame.display.update()

    # control the frame rate
    clock.tick(60)