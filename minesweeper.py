import pygame
import os
from random import randrange


class Settings(object):
    width = 16 * 4 * 9
    height = 16 * 4 * 9
    fps = 60
    title = "Minesweeper"
    file_path = os.path.dirname(os.path.abspath(__file__))
    images_path = os.path.join(file_path, "images")
    gameover = False
    start = True
    click = False
    hold = False
    hover = False
    flag = False

    @staticmethod
    def get_dim():
        return Settings.width, Settings.height


class Empty_Tile(pygame.sprite.Sprite):
    def __init__(self, pygame, x, y):
        super().__init__()
        self.image = pygame.image.load(os.path.join(Settings.images_path, "empty_tile.png")).convert_alpha()
        self.image = pygame.transform.scale(self.image, (64, 64))
        self.rect = self.image.get_rect()
        self.rect.left = x
        self.rect.top = y


class Tile(pygame.sprite.Sprite):
    def __init__(self, pygame, x, y):
        super().__init__()
        self.image = pygame.image.load(os.path.join(Settings.images_path, "tile.png")).convert_alpha()
        self.image = pygame.transform.scale(self.image, (64, 64))
        self.rect = self.image.get_rect()
        self.rect.left = x
        self.rect.top = y
        self.fade = 255
        self.die = False

    def update(self):
        if Settings.flag == False and Settings.click == True and pygame.mouse.get_pos()[0] >= self.rect.left and pygame.mouse.get_pos()[0] <= self.rect.right and pygame.mouse.get_pos()[1] >= self.rect.top and pygame.mouse.get_pos()[1] <= self.rect.bottom:
            self.die = True
            #print("klick")
        if self.die == True:
            #print(self.fade)
            self.image.set_alpha(self.fade)
            self.fade -= 60
            if self.fade <= 0:
                self.kill()
                #print("kill")


class Mine(pygame.sprite.Sprite):
    def __init__(self, pygame, x, y):
        super().__init__()
        self.image = pygame.image.load(os.path.join(Settings.images_path, "mine.png")).convert_alpha()
        self.image = pygame.transform.scale(self.image, (64, 64))
        self.rect = self.image.get_rect()
        self.rect.left = x
        self.rect.top = y

    def update(self):
        if Settings.click == True and pygame.mouse.get_pos()[0] >= self.rect.left and pygame.mouse.get_pos()[0] <= self.rect.right and pygame.mouse.get_pos()[1] >= self.rect.top and pygame.mouse.get_pos()[1] <= self.rect.bottom:
            Settings.gameover = True
            self.image = pygame.image.load(os.path.join(Settings.images_path, "red_mine.png")).convert_alpha()
            self.image = pygame.transform.scale(self.image, (64, 64))


class Flag(pygame.sprite.Sprite):
    def __init__(self, pygame, x, y):
        super().__init__()
        self.image = pygame.image.load(os.path.join(Settings.images_path, "flag.png")).convert_alpha()
        self.image = pygame.transform.scale(self.image, (64, 64))
        self.rect = self.image.get_rect()
        self.rect.left = x
        self.rect.top = y

    def update(self):
        if pygame.mouse.get_pos()[0] >= self.rect.left and pygame.mouse.get_pos()[0] <= self.rect.right and pygame.mouse.get_pos()[1] >= self.rect.top and pygame.mouse.get_pos()[1] <= self.rect.bottom:
            self.kill()
            #print("Flagge killed")


class Number(pygame.sprite.Sprite):
    def __init__(self, pygame, x, y):
        super().__init__()
        self.image = pygame.image.load(os.path.join(Settings.images_path, "1.png")).convert_alpha()
        self.image = pygame.transform.scale(self.image, (64, 64))
        self.rect = self.image.get_rect()
        self.rect.left = x
        self.rect.top = y
        self.number = 1

    def update(self):
        if self.number == 2:
            self.image = pygame.image.load(os.path.join(Settings.images_path, "2.png")).convert_alpha()
            self.image = pygame.transform.scale(self.image, (64, 64))

        if self.number == 3:
            self.image = pygame.image.load(os.path.join(Settings.images_path, "3.png")).convert_alpha()
            self.image = pygame.transform.scale(self.image, (64, 64))

        if self.number == 4:
            self.image = pygame.image.load(os.path.join(Settings.images_path, "4.png")).convert_alpha()
            self.image = pygame.transform.scale(self.image, (64, 64))

        if self.number == 5:
            self.image = pygame.image.load(os.path.join(Settings.images_path, "5.png")).convert_alpha()
            self.image = pygame.transform.scale(self.image, (64, 64))

        if self.number == 6:
            self.image = pygame.image.load(os.path.join(Settings.images_path, "6.png")).convert_alpha()
            self.image = pygame.transform.scale(self.image, (64, 64))

        if self.number == 7:
            self.image = pygame.image.load(os.path.join(Settings.images_path, "7.png")).convert_alpha()
            self.image = pygame.transform.scale(self.image, (64, 64))

        if self.number == 8:
            self.image = pygame.image.load(os.path.join(Settings.images_path, "8.png")).convert_alpha()
            self.image = pygame.transform.scale(self.image, (64, 64))


class Mouse(pygame.sprite.Sprite):
    def __init__(self, pygame):
        super().__init__()
        self.image = pygame.image.load(os.path.join(Settings.images_path, "tile.png")).convert_alpha()
        self.image = pygame.transform.scale(self.image, (1, 1))
        self.rect = self.image.get_rect()

    def update(self):
        self.rect.left = pygame.mouse.get_pos()[0]
        self.rect.top = pygame.mouse.get_pos()[1]


class Collision_detection(pygame.sprite.Sprite):
    def __init__(self, pygame, x, y):
        super().__init__()
        self.image = pygame.image.load(os.path.join(Settings.images_path, "tile.png")).convert_alpha()
        self.image = pygame.transform.scale(self.image, (64, 64))
        self.rect = self.image.get_rect()
        self.rect.left = x
        self.rect.top = y
        self.moved = False

    def update(self):
        if self.moved == False and Settings.click == True and pygame.mouse.get_pos()[0] >= self.rect.left and pygame.mouse.get_pos()[0] <= self.rect.right and pygame.mouse.get_pos()[1] >= self.rect.top and pygame.mouse.get_pos()[1] <= self.rect.bottom:
            self.image = pygame.image.load(os.path.join(Settings.images_path, "tile.png")).convert_alpha()
            self.image = pygame.transform.scale(self.image, (66, 66))
            self.rect.left -= 1
            self.rect.top -= 1
            self.rect.width += 2
            self.rect.height += 2
            self.moved = True


class Killer(pygame.sprite.Sprite):
    def __init__(self, pygame, x, y):
        super().__init__()
        self.image = pygame.image.load(os.path.join(Settings.images_path, "tile.png")).convert_alpha()
        self.image = pygame.transform.scale(self.image, (66, 66))
        self.rect = self.image.get_rect()
        self.rect.left = x
        self.rect.top = y


class Game(object):
    def __init__(self):
        self.screen = pygame.display.set_mode(Settings.get_dim())
        pygame.display.set_caption(Settings.title)

        self.clock = pygame.time.Clock()
        self.done = False
        self.spawn = True
        self.input = False
        self.name = ""
        self.newhighscore = False
        self.mouse = Mouse(pygame)

        self.ground = pygame.sprite.Group()
        self.mines = pygame.sprite.Group()
        self.toptiles = pygame.sprite.Group()
        self.numbers = pygame.sprite.Group()
        self.flags = pygame.sprite.Group()
        self.collisions = pygame.sprite.Group()
        self.killers = pygame.sprite.Group()

        pygame.font.init()
        self.font = pygame.font.SysFont("", 30)
        self.font2 = pygame.font.SysFont("", 75)
        self.gameovertext = self.font2.render("GAMEOVER", False, (150, 0, 0))
        self.wintext = self.font2.render("YOU WON", False, (0, 255, 0))
        self.againtext = self.font.render("RIGHT CLICK TO PLAY AGAIN", False, (0, 0, 0))


    def run(self):
        while not self.done:
            self.clock.tick(Settings.fps)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.done = True

                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.done = True
                    elif event.key == pygame.K_q:
                        self.done = True

                # Flagge beim Rechtsklick plazieren und löschen
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 3 and pygame.sprite.spritecollide(self.mouse, self.toptiles, False) and Settings.flag == False:
                        self.flag = Flag(pygame, pygame.mouse.get_pos()[0]//64 * 64, pygame.mouse.get_pos()[1]//64 * 64)
                        self.flags.add(self.flag)
                        #print("Flagge plaziert", len(self.flags))
                    elif event.button == 3 and Settings.flag == True:
                        self.flags.update()

                    elif event.button == 1 and pygame.sprite.spritecollide(self.mouse, self.collisions, False):
                        self.killer = Killer(pygame, pygame.mouse.get_pos()[0]//64 * 64 - 1, pygame.mouse.get_pos()[1]//64 * 64 - 1)
                        self.killers.add(self.killer)


            if Settings.start == True:
                Settings.start = False
                for x in range(0, 576, 64):
                    #print(x)
                    for y in range(0, 576, 64):
                        self.empty_tile = Empty_Tile(pygame, x, y)
                        self.ground.add(self.empty_tile)

                for m in range(0, 10):
                    #print(m)
                    spawn = True
                    while spawn == True:
                        #print(m)
                        self.minex = randrange(0, 576, 64)
                        self.miney = randrange(0, 576, 64)
                        self.mine = Mine(pygame, self.minex, self.miney)
                        self.mines.add(self.mine)
                        if m != 0:
                            for mine in self.mines:
                                for mine2 in self.mines:
                                    if mine != mine2:
                                        if pygame.sprite.collide_rect(mine, mine2):
                                            mine.kill()
                                            #print("Kollision")
                                            spawn = True
                                            break
                                        else:
                                            spawn = False
                                else:
                                    continue
                                break
                        else:
                            spawn = False
                        #print(spawn)
                    
                    #print("Minex:", self.minex, "Miney:",self.miney)
                    for a in range(self.minex - 64, self.minex + 65, 64):
                        for b in range(self.miney - 64, self.miney + 65, 64):
                            if not a < 0 and not b < 0:
                                self.number = Number(pygame, a, b)
                                self.numbers.add(self.number)
                                #print(a, b)

                #print("Bomben:", len(self.mines))

                for number in self.numbers:
                    for number2 in self.numbers:
                        if number != number2:
                            if pygame.sprite.collide_rect(number, number2):
                                number.number += 1

                for x in range(0, 576, 64):
                    for y in range(0, 576, 64):
                        self.tile = Tile(pygame, x, y)
                        self.toptiles.add(self.tile)

                for x in range(0, 576, 64):
                    for y in range(0, 576, 64):
                        self.collision = Collision_detection(pygame, x, y)
                        self.collisions.add(self.collision)

                for collision in self.collisions:
                    for number in self.numbers:
                        if pygame.sprite.collide_rect(collision, number):
                            collision.kill()

                for collision in self.collisions:
                    for mine in self.mines:
                        if pygame.sprite.collide_rect(collision, mine):
                            collision.kill()

            # Kollision
            if pygame.mouse.get_pressed()[0] == True and Settings.click == False and Settings.hold == False:
                Settings.click = True
                Settings.hold = True
            elif pygame.mouse.get_pressed()[0] == True and Settings.click == True:
                Settings.click = False
                Settings.hold = True
            elif pygame.mouse.get_pressed()[0] == False and Settings.hold == True:
                Settings.hold = False
                Settings.click = False

            if pygame.sprite.spritecollide(self.mouse, self.flags, False):
                Settings.flag = True
                #print("Flagge")
            else:
                Settings.flag = False
                #print("keine Flagge")

            for collision in self.collisions:
                for collision2 in self.collisions:
                    if collision != collision2:
                        if pygame.sprite.collide_rect(collision, collision2) and collision.moved == False:
                            collision.image = pygame.image.load(os.path.join(Settings.images_path, "tile.png")).convert_alpha()
                            collision.image = pygame.transform.scale(collision.image, (66, 66))
                            collision.rect.left -= 1
                            collision.rect.top -= 1
                            collision.rect.width += 2
                            collision.rect.height += 2
                            collision.moved = True
                            self.killer = Killer(pygame, collision.rect.left, collision.rect.top)
                            self.killers.add(self.killer)

            for killer in self.killers:
                for tile in self.toptiles:
                    if pygame.sprite.collide_rect(killer, tile):
                        tile.die = True


            # Zeichungen und Updates
            self.ground.draw(self.screen)
            self.numbers.draw(self.screen)
            self.mines.draw(self.screen)
            self.mines.update()
            self.toptiles.draw(self.screen)
            self.toptiles.update()
            self.numbers.update()
            self.flags.draw(self.screen)
            self.mouse.update()
            self.collisions.update()

            # Gewinnbedingung
            if len(self.toptiles) <= 10 or Settings.gameover == True:
                self.toptiles.empty()
                self.screen.blit(self.againtext, self.againtext.get_rect(center=(Settings.width//2, Settings.height//2)))

                if Settings.gameover == True:
                    self.screen.blit(self.gameovertext, self.gameovertext.get_rect(center=(Settings.width//2, Settings.height//2 - 50)))
                else:
                    self.screen.blit(self.wintext, self.wintext.get_rect(center=(Settings.width//2, Settings.height//2 - 50)))

                if pygame.mouse.get_pressed()[2]:
                    Settings.start = True
                    Settings.gameover = False
                    self.ground.empty()
                    self.mines.empty()
                    self.numbers.empty()
                    self.flags.empty()
                    self.collisions.empty()
                    self.killers.empty()


            pygame.display.flip()


if __name__ == '__main__':
    pygame.init()
    game = Game()
    game.run()
    pygame.quit()
