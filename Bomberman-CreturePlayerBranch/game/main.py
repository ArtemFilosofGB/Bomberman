import pygame

from npc import Npc
from tile import TileType
from player import Player
from key_input import readKeyboard
from background import Background
from map import Map


class GameLoop:
    def __init__(self):
        pygame.init()

        screen_width = 1200
        screen_height = 800
        self.screen = pygame.display.set_mode((screen_width, screen_height))
        pygame.display.set_caption("Bomberman")

        self.background = Background(screen_width, screen_height)

        self.map = Map(self.screen)
        self.map.create_map()

        self.clock = pygame.time.Clock()

        self.running = False

        self.player1 = Player(148, 90, pygame.image.load("../assets/Player/player_bomberman.png"), 1)
        self.player2 = Player(1000, 665, pygame.image.load("../assets/Player/player_bomberman.png"),1)
        self.npc1 = Npc(500, 500, pygame.image.load("../assets/Player/apple_npc.png"))
    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

    def update(self):

        self.player1.check_collision_tile(self.map.tiles_map)
        self.player2.check_collision_tile(self.map.tiles_map)

        self.player1.check_collision_npc(self.npc1)
        self.player2.check_collision_npc(self.npc1)

        if self.player1.is_collided_with(self.npc1):
            print("p1 collision npc")
        if self.player2.is_collided_with(self.npc1):
            print("p2 collision npc")
        if self.player1.is_collided_with(self.player2):
            print("p1 collision p2")
        if self.player2.is_collided_with(self.player1):
            print("p2 collision p1")
        #todo npc list




        #test revers collision
        if self.npc1.check_collision(self.player1):
            #todo animation for npc bite
            pass
            #print("npc bite player1")
        pygame.display.update()

    def draw(self):
        self.background.draw(self.screen)
        self.map.draw(self.screen)


    def run(self):
        self.running = True

        while self.running:
            self.handle_events()
            self.draw()

            #draw players
            self.player1.draw(self.screen)
            self.player2.draw(self.screen)
            self.npc1.draw(self.screen)

            #check timer to blow up bombs
            self.player1.blow_up_bomb()
            self.player2.blow_up_bomb()

            #draw bombs
            #todo: extract to method
            for bomb in self.player1.bombs_list:
                bomb.draw(self.screen)
            for bomb in self.player2.bombs_list:
                bomb.draw(self.screen)
            for exp in self.player1.explosion_list:
                exp.draw(self.screen)
            for exp in self.player2.explosion_list:
                exp.draw(self.screen)

            #read keyboard
            readKeyboard(self.player1,1)
            readKeyboard(self.player2,2)
            timer = pygame.time.get_ticks() # in milliseconds
            print(timer)
            self.update()
            self.clock.tick(30)

        pygame.quit()


if __name__ == "__main__":
    game = GameLoop()
    game.run()  # main loop
