from pygame.locals import *
import configuration.settings as s
from actors.Player import Player
from actors.Meteor import Meteor
import pygame
import sys
from configuration.settings import ran

s.Update()
pygame.font.init() 
pygame.init()
vec = s.VEC
my_font = s.MY_FONT
FramePerSec = pygame.time.Clock()
displaysurface = s.DisplaySurface
Clock = pygame.time.Clock()
Meteors = pygame.sprite.Group()
Bullets = pygame.sprite.Group()
all_sprites = pygame.sprite.Group()

def _GameOver():
    for e in all_sprites:
        e.kill()
    for e in Bullets:
        e.kill()
    for e in Meteors:
        e.kill()
    end = s.BIG_FONT.render('Game Over', False, s.WHITE)
    displaysurface.blit(end, (178,211))
    pygame.display.update()
    pygame.time.wait(5000)
    pygame.quit()
    sys.exit()

def main():
    P1 = Player()
    all_sprites.add(P1)
    P1.GetTriangle(s.WIDTH/2,s.HEIGHT/2,25)
    Time = 0
    Last = 0
    NextM = 2000
    Score = 0
    GameOver = False
    while True:
        if not GameOver:
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
            if(Time - Last > NextM):
                NextM = max(NextM - 50,500)
                Last = Time
                vx = ran.randint(0,10) - 5
                vy = ran.randint(0,10) - 5
                Vel = vec(vx,vy)
                x = ran.randint(0,s.WIDTH)
                y = -100
                if ran.randint(1,2) == 1: y = s.HEIGHT + 100 
                m = Meteor(vec(x,y),Vel,100)
                Meteors.add(m)
            displaysurface.fill((0,0,0))
            for entity in Meteors:
                entity.Update()
            for entity in Bullets:
                entity.Update()
            for entity in Meteors:
                if P1.Collide(entity.Center,entity.Radius): 
                    _GameOver()
            for entity in Meteors:
                for e in Bullets:
                    if entity.CollideB(e):
                        Score += 1
                        new = entity.Explode(e.Vel)
                        if len(new) > 0:
                            Meteors.add(new[0])
                            Meteors.add(new[1])
                        entity.kill()
                        e.kill()
            b = P1.Update(FramePerSec.get_time())
            if b is not None:
                Bullets.add(b)
        end = s.BIG_FONT.render('Game Over', False, s.WHITE)
        mouse_pos = my_font.render(str(pygame.mouse.get_pos()), False, s.WHITE)
        text_surface = my_font.render(str(Score), False, s.WHITE)
        displaysurface.blit(text_surface, (0,0))
        pygame.display.update()
        Time += FramePerSec.get_time()
        FramePerSec.tick(s.FPS)

if __name__ == "__main__":
    main()