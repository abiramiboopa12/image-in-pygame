import pygame
pygame.init()

screen_whith, screen_hight = (500, 500)
screen = pygame.display.set_mode((screen_whith, screen_hight))
pygame.display.set_caption("Adding image and background image")

background_image = pygame.transform.scale(pygame.image.load("image1.png").convert(), (screen_whith, screen_hight))
image1 = pygame.transform.scale(pygame.image.load("image1.png").convert_alpha(), (500, 500))
text = pygame.font.Font(None, 36).render("Hello world", True, pygame.Color("White"))
text_rect = text.get_rect(center=(screen_whith / 2, screen_hight / 2))

def game_loop():
    clock = pygame.time.Clock()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        screen.blit(background_image, (0, 0))
        screen.blit(image1, (0, 0))
        screen.blit(text, text_rect)
        pygame.display.flip()
        clock.tick(30)
    pygame.quit()

# Call the game loop to start the game
game_loop()