import pygame
import random

ANCHO = 800
ALTO = 600
NEGRO = [0, 0, 0]
ROJO = [255, 0, 0]
VERDE = [0, 255, 0]
AMARILLO = [255, 255, 0]
BLANCO = [255, 255, 255]


class Jugador(pygame.sprite.Sprite):
    def __init__(self, pos):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([50, 50])
        self.image.fill(BLANCO)
        self.rect = self.image.get_rect()
        self.rect.x = pos[0]
        self.rect.y = (ALTO - self.rect.height) - 10
        self.velx = 0
        # self.vely=0

    def RetPos(self):
        x = self.rect.x
        y = self.rect.y - 20
        return [x, y]

    def update(self):
        self.rect.x += self.velx
        # self.rect.y+=self.vely


class Rival(pygame.sprite.Sprite):
    def __init__(self, pos):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([50, 50])
        self.image.fill(VERDE)
        self.rect = self.image.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]
        self.velx = 0
        self.vely = 0

    def update(self):
        # self.rect.x+=self.velx
        # self.rect.y+=self.vely
        pass


class Bala(pygame.sprite.Sprite):
    def __init__(self, pos):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([20, 30])
        self.image.fill(BLANCO)
        self.rect = self.image.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]
        self.vely = 0

    def update(self):
        self.rect.y += self.vely


if __name__ == '__main__':
    pygame.init()
    # Definicion de variables
    ventana = pygame.display.set_mode([ANCHO, ALTO])
    jugadores = pygame.sprite.Group()
    rivales = pygame.sprite.Group()
    balas = pygame.sprite.Group()

    j = Jugador([300, 200])
    jugadores.add(j)

    n = 10
    for i in range(n):
        x = random.randrange(ANCHO)
        y = random.randrange((ALTO - 150))
        vx = random.randrange(10)
        r = Rival([x, y])
        r.velx = vx
        rivales.add(r)

    reloj = pygame.time.Clock()
    fin = False
    while not fin:
        # Gestion eventos
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                fin = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    j.velx = 5
                    j.vely = 0
                if event.key == pygame.K_LEFT:
                    j.velx = -5
                    j.vely = 0
                if event.key == pygame.K_UP:
                    j.vely = -5
                    j.velx = 0
                if event.key == pygame.K_DOWN:
                    j.vely = 5
                    j.velx = 0
            if event.type == pygame.MOUSEBUTTONDOWN:
                p = j.RetPos()
                b = Bala(p)
                b.vely = -10
                balas.add(b)
            if event.type == pygame.KEYUP:
                j.vely = 0
                j.velx = 0
        # Control
        if j.rect.x > ANCHO:
            j.rect.x = 0 - j.rect.width
        # Colision

        # Limpieza de memoria
        for b in balas:
            if b.rect.y < -50:
                balas.remove(b)
        # Refresco
        jugadores.update()
        rivales.update()
        balas.update()
        ventana.fill(NEGRO)
        jugadores.draw(ventana)
        rivales.draw(ventana)
        balas.draw(ventana)
        pygame.display.flip()
        reloj.tick(40)