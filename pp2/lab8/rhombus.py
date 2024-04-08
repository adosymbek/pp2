import pygame

def main():
    pygame.init()
    
    #Creating colors
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    RED = (255, 0, 0)
    GREEN = (0, 255, 0)
    BLUE = (0, 0, 255)
    
    #Other Variables for use in the program
    WINDOW_WIDTH = 500
    WINDOW_HEIGHT = 500
    
    #Create a white screen
    screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    new_surf = pygame.Surface((WINDOW_WIDTH, WINDOW_HEIGHT))
    screen.fill(BLACK)
    clock = pygame.time.Clock()
    

    prev= None
    cur = None


    mouse_down = False
    while True:
        
        pressed = pygame.key.get_pressed()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_down = True
                prev = pygame.mouse.get_pos()
               
                
            if event.type == pygame.MOUSEMOTION:
                if mouse_down:
                    cur = pygame.mouse.get_pos()

            if event.type == pygame.MOUSEBUTTONUP: 
                mouse_down = False
                new_surf.blit(screen, (0,0))
                cur = None

        if mouse_down and prev!= None and cur!= None:
            screen.blit(new_surf, (0,0))
            point3 = [prev[0]- (cur[0]-prev[0]) , cur[1]]
            point4 = [prev[0], cur[1] + (cur[1] - prev[1])]
            pygame.draw.polygon(screen, (255,255,255), (prev,cur, point4 ,point3), 1)
        
        
        pygame.display.flip()
        
        clock.tick(60)


main()