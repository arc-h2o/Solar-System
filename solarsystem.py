import pygame
import math
from random import randint

pygame.init()

FONT = pygame.font.SysFont("comicsans", 12)
screen = pygame.display.set_mode((1700, 950))
pygame.display.set_caption("Solar System")

class Planet:
    def __init__(self, radius, distance, color, increaseAngle, name):
        self.radius = radius
        self.distance = distance
        self.color = color
        self.increaseAngle = increaseAngle
        self.name = name
        self.angle = 0
    
    def movePlanet(self):      
        self.angle = self.angle + self.increaseAngle

    def draw(self, surface):
        x = 850 + int(math.cos(math.radians(self.angle)) * self.distance)
        y = 475 + int(math.sin(math.radians(self.angle)) * self.distance)
        pygame.draw.circle(surface, self.color, (x, y), self.radius)
        if self.name == "Saturn":
            pygame.draw.line(surface, (153, 150, 155), (x - 1.2 * self.radius, y - 1.2 * self.radius), (x + 1.2 * self.radius, y + 1.2 * self.radius), 3)
        name = FONT.render(self.name, 1, (255, 255, 255))
        screen.blit(name, (x + name.get_width() / 2, y + name.get_height() / 2))

def draw_orbit(surface, planet): 
    pygame.draw.circle(surface, planet.color, (850, 475), planet.distance, 1)

def main():
    sun = Planet(40, 0, (255, 255, 0), 0, "Sun")
    planets = [
        Planet(10, 100, (128, 128, 128), 0.047, "Mercury"), 
        Planet(12, 150, (255, 255, 255), 0.035, "Venus"),    
        Planet(14, 200, (0, 0, 255), 0.029, "Earth"),      
        Planet(12, 250, (198, 123, 92), 0.024, "Mars"),    
        Planet(22, 300, (167, 156, 134), 0.013, "Jupiter"),  
        Planet(18, 350, (123, 120, 105), 0.010, "Saturn"),    
        Planet(16, 400, (213, 251, 252), 0.007, "Uranus"),    
        Planet(16, 450, (96, 129, 255), 0.006, "Neptune")    
    ]
    stars = [((randint(180, 200), randint(180, 200), randint(180, 200)), (randint(1, 1700), randint(1, 950)), randint(1, 2)) for _ in range(250)]
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        screen.fill((0, 0, 0))
        for star in stars:
            pygame.draw.circle(screen, star[0], star[1], star[2])
        sun.draw(screen)
        for planet in planets:
            draw_orbit(screen, planet)
            planet.movePlanet()
            planet.draw(screen)   
        pygame.display.flip()
    pygame.quit()

if __name__ == "__main__":
    main()