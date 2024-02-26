import pygame

from npc import Npc
from bomb import Bomb
from tile import TileType, Tile
from сreature import Creature
from explosions import Explosions


class Player(Creature):
    def __init__(self, x: int, y: int, image: pygame.Surface, bomb_count: int):
        super().__init__(x,y,image)
        self.bomb_count = bomb_count
        self.bombs_drop_time = [0,0,0]
        self.bombs_list = []
        self.explosion_list = []


    def draw(self, screen):
        screen.blit(self.image, self.rect)

    def is_collided_with(self, creature: Creature):
        if self.rect.colliderect(creature.rect):
            return True
        return False

    def check_collision_npc(self, npc: Npc):
        if self.rect.colliderect(npc.rect):
            print("npc collision")
            self.damage(1)
            print(self.life)
            if self.life > 0:
                #todo: spawn places for players
                self.rect.x = self.spawn_x
                self.rect.y = self.spawn_y
            else:
                self.death()

    def check_collision_tile(self, tile_map: list[list[Tile]]):
        for line in tile_map:
            for tile in line:
                if tile.type == TileType.BORDER:
                    pass
                    #print("Collision border")
                if tile.type == TileType.GRASS:
                    pass
                    #print("Collision grass")
                if tile.type == TileType.DESTRUCTIBLE:
                    pass
                    #print("Collision destructible")

    def can_move(self, dx, dy):
        self.check_collision_tile(self.map.tiles_map)

    def drop_bomb(self):
        if self.bomb_count >0 and pygame.time.get_ticks() - self.bombs_drop_time[self.bomb_count+1]>1000:
            self.bombs_drop_time[self.bomb_count] = pygame.time.get_ticks()
            self.bombs_list.append(Bomb(self.rect.x, self.rect.y, pygame.image.load("../assets/Bomb/Bomb32.png")))
            self.bomb_count -= 1
        #todo: add sound
        #todo: add animation
        #todo: add timer: timeout to next drop
        print("Bomb count: ",self.bomb_count)


    def blow_up_bomb(self):
        for bomb in self.bombs_list:
            if bomb.drop_time + 3000 < pygame.time.get_ticks():
                for i in range(bomb.power):
                    self.explosion_list.append(Explosions(bomb.x+i*48, bomb.y, pygame.image.load("../assets/explosion/explosion64.png")))
                #todo: transform animation of explosion
                pygame.time.delay(1000)
                self.bombs_list.remove(bomb)
                print ("Removr bomb")
                self.bomb_count += 1


    def action(self):
        for bomb in self.bombs_list:
            bomb.oblow_up()

    def death(self):
        self.speed = 0
        self.image = pygame.image.load("../assets/Player/death32.png")
        pass

    def gameover(self):
        #todo: end game score, time, go to main menu
        pass



