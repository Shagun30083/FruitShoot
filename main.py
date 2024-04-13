import pygame
import random
import math
import asyncio

async def main():

    # Initialize the pygame
    pygame.init()

    # Create the screen
    screen = pygame.display.set_mode((800, 600))

    # Background
    background = pygame.image.load("background.jpg")

    # Caption and Icon
    pygame.display.set_caption('Shoot Fruits')
    icon = pygame.image.load('Icon.png')
    pygame.display.set_icon(icon)

    # Gun
    gunImg = pygame.image.load('gun.png')
    gunX = 650
    gunY = 268
    gunY_change = 0

    # Mango
    mangoImg = pygame.image.load('mango.png')
    mangoX = random.randint(40, 500)
    mangoY = random.randint(-500, -32)
    mangoX_change = 0
    mangoY_change = 2.5

    # Apple
    appleImg = pygame.image.load('apple.png')
    appleX = random.randint(40, 500)
    appleY = random.randint(-500, -32)
    appleX_change = 0
    appleY_change = 2.5

    # Banana
    bananaImg = pygame.image.load('banana.png')
    bananaX = random.randint(40, 500)
    bananaY = random.randint(-500, -32)
    bananaX_change = 0
    bananaY_change = 2.5

    # Strawberry
    strawberryImg = pygame.image.load('strawberry.png')
    strawberryX = random.randint(40, 500)
    strawberryY = random.randint(-500, -32)
    strawberryX_change = 0
    strawberryY_change = 2.5

    # Apricot
    apricotImg = pygame.image.load('apricot.png')
    apricotX = random.randint(40, 500)
    apricotY = random.randint(-500, -32)
    apricotX_change = 0
    apricotY_change = 2.5

    # Pomegranate
    pomegranateImg = pygame.image.load('pomegranate.png')
    pomegranateX = random.randint(40, 500)
    pomegranateY = random.randint(-500, -32)
    pomegranateX_change = 0
    pomegranateY_change = 2.5

    # Bullet

    # Ready - You can't see the bullet on the screen
    # Fire - the bullet is currently moving

    bulletImg = pygame.image.load('bullet.png')
    bulletX = 650
    bulletY = gunY
    bulletX_change = 20
    bulletY_change = 0
    bullet_state = 'ready'


    # Score
    score_value = 0
    font = pygame.font.SysFont('Berlin Sans FB', 40)

    # Display position of Score
    textX = 630
    textY = 15

    # Lives
    lifeImg = pygame.image.load('life.png')
    lifeX = 10
    lifeY = []
    for a in range(20, 580, 40):
        lifeY.append(a)
    lifeReduce = 0

    # Game Over
    font_Game_Over = pygame.font.SysFont('Arial', 80, bold=1)

    # For Instructing the user
    font_Instruction = pygame.font.SysFont('Arial', 13)


    def gun(x, y):
        screen.blit(gunImg, (x, y))


    def mango(x, y):
        screen.blit(mangoImg, (x, y))


    def apple(x, y):
        screen.blit(appleImg, (x, y))


    def banana(x, y):
        screen.blit(bananaImg, (x, y))


    def strawberry(x, y):
        screen.blit(strawberryImg, (x, y))


    def apricot(x, y):
        screen.blit(apricotImg, (x, y))


    def pomegranate(x, y):
        screen.blit(pomegranateImg, (x, y))


    def isCollision(fruitX, fruitY, bulletX, bulletY):
        distance = math.sqrt((math.pow(bulletX - fruitX, 2)) + (math.pow(bulletY - fruitY, 2)))
        if distance <= 27:
            return True
        else:
            return False


    def show_score(x, y):
        score = font.render('Score : ' + str(score_value), True, (255, 255, 255))

        screen.blit(score, (x, y))


    def life(a):
        for i in range(a):
            screen.blit(lifeImg, (lifeX, lifeY[i]))


    def game_over_text():
        over_text = font_Game_Over.render('GAME OVER', True, (0,0,0))
        screen.blit(background, (0, 0))
        screen.blit(over_text, (150, 250))



    # Game Loop
    running = True
    while running:

        # ScreenColor
        screen.fill((0, 0, 0))

        # Background Image
        screen.blit(background, (0, 0))
        
        Instruction_Text = font_Instruction.render('Press SPACE button to fire the bullet & use UP and DOWN keys for gun movement', True, (255,255,255))
        screen.blit(Instruction_Text, (70, 25))

        if lifeReduce == 14:
            game_over_text()
            show_score(20, 20)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

        else:
                
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False


                # if keystroke is pressed check whether its up or down
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        gunY_change = -5
                    if event.key == pygame.K_DOWN:
                        gunY_change = 5
                    if event.key == pygame.K_SPACE:
                        if bullet_state == 'ready':
                            # Get the current x cordinate of the gun
                            bulletY = gunY
                            bullet_state = 'fire'
                            screen.blit(bulletImg, (bulletX, bulletY + 29))

                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                        gunY_change = 0

            gunY += gunY_change

            # Checking for boundaries of gun so that it does not go out of the boundaries.
            if gunY <= 40:
                gunY = 40
            elif gunY >= 536:
                gunY = 536

            # Mango Movement
            mangoY += mangoY_change
            num_of_lives = len(lifeY)
            if mangoY >= 600:
                mangoY = random.randint(-500, -32)
                mangoX = random.randint(40, 500)
                mangoY_change = random.randrange(2, 5)

                # Change in lives
                lifeReduce += 1
                if lifeReduce <= 14:
                    del lifeY[-1]
                num_of_lives = len(lifeY)

            # Apple Movement
            appleY += appleY_change

            if appleY >= 600:
                appleY = random.randint(-500, -32)
                appleX = random.randint(40, 500)
                appleY_change = random.randrange(2, 5)

            # Banana Movement
            bananaY += bananaY_change

            if bananaY >= 600:
                bananaY = random.randint(-500, -32)
                bananaX = random.randint(40, 500)
                bananaY_change = random.randrange(2, 5)

            # Strawberry Movement
            strawberryY += strawberryY_change

            if strawberryY >= 600:
                strawberryY = random.randint(-500, -32)
                strawberryX = random.randint(40, 500)
                strawberryY_change = random.randrange(2, 5)

            # Apricot Movement
            apricotY += apricotY_change

            if apricotY >= 600:
                apricotY = random.randint(-500, -32)
                apricotX = random.randint(40, 500)
                apricotY_change = random.randrange(2, 5)

            # Pomegranate Movement
            pomegranateY += pomegranateY_change

            if pomegranateY >= 600:
                pomegranateY = random.randint(-500, -32)
                pomegranateX = random.randint(40, 500)
                pomegranateY_change = random.randrange(2, 5)

            # Bullet Movement
            if bulletX <= 40:
                bulletX = 650
                bullet_state = 'ready'

            if bullet_state == 'fire':
                bullet_state = 'fire'
                screen.blit(bulletImg, (bulletX, bulletY + 29))
                bulletX -= bulletX_change

            # Collision of mango
            collision = isCollision(mangoX, mangoY, bulletX, bulletY)
            if collision:
                bulletX = 650
                bullet_state = 'ready'
                score_value += 1
                mangoX = random.randint(40, 500)
                mangoY = random.randint(-500, -32)
                mangoY_change = random.randrange(2, 5)

            # Collision of apple
            collision = isCollision(appleX, appleY, bulletX, bulletY)
            if collision:
                bulletX = 650
                bullet_state = 'ready'
                score_value += 1
                appleX = random.randint(40, 500)
                appleY = random.randint(-500, -32)
                appleY_change = random.randrange(2, 5)

            # Collision of banana
            collision = isCollision(bananaX, bananaY, bulletX, bulletY)
            if collision:
                bulletX = 650
                bullet_state = 'ready'
                score_value += 1
                bananaX = random.randint(40, 500)
                bananaY = random.randint(-500, -32)
                bananaY_change = random.randrange(2, 5)

            # Collision of strawberry
            collision = isCollision(strawberryX, strawberryY, bulletX, bulletY)
            if collision:
                bulletX = 650
                bullet_state = 'ready'
                score_value += 1
                strawberryX = random.randint(40, 500)
                strawberryY = random.randint(-500, -32)
                strawberryY_change = random.randrange(2, 5)

            # Collision of apricot
            collision = isCollision(apricotX, apricotY, bulletX, bulletY)
            if collision:
                bulletX = 650
                bullet_state = 'ready'
                score_value += 1
                apricotX = random.randint(40, 500)
                apricotY = random.randint(-500, -32)
                apricotY_change = random.randrange(2, 5)

            # Collision of pomegranate
            collision = isCollision(pomegranateX, pomegranateY, bulletX, bulletY)
            if collision:
                bulletX = 650
                bullet_state = 'ready'
                score_value += 1
                pomegranateX = random.randint(40, 500)
                pomegranateY = random.randint(-500, -32)
                pomegranateY_change = random.randrange(2, 5)

            gun(gunX, gunY)

            mango(mangoX, mangoY)

            apple(appleX, appleY)

            banana(bananaX, bananaY)

            strawberry(strawberryX, strawberryY)

            apricot(apricotX, apricotY)

            pomegranate(pomegranateX, pomegranateY)

            show_score(textX, textY)

            life(num_of_lives)

        # if lifeReduce == 14:
        #     game_over_text()
        #     show_score(20, 20)

        pygame.display.update()
        await asyncio.sleep(0)

asyncio.run(main())
