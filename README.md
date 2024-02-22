# BomberMan
![game.jpg](game.jpg)
## Список объектов
* Creature
  * x,y
  * speed
  * skin
  * Rect
  * life = 3

* Player (Creature)
  * bomb_count

* Block
  * x
  * y
  * Rect
  * Type (GRASS, BORDER, DESTRUCTIBLE = 0, 1, 2)

* Map 
  * map_width = 21 
  * map_height = 15 
  * tiles_map list[Block]

* keyboardInput
  * def keyEvent()

* Menu
  * start -> main loop
  * settings
  * exit

* Bomb
  * x,y
  * Rect
  * power
  * timer
 
* NPC
  * movement

![scheme.jpg](scheme.jpg)

        # Проверка когда клавиша нажимается
        elif event.type == py.KEYDOWN:
            if event.key == py.K_LEFT:
                #x -= 10
                fl_left = True
            elif event.key == py.K_RIGHT:
                #x += 10
                fl_right = True
            elif event.key == py.K_UP:
                #y -= 10
                fl_up = True
            elif event.key == py.K_DOWN:
                #y += 10
                fl_down = True
        # Проверка когда клавиша отпускается
        elif event.type == py.KEYUP:
            if event.key == py.K_LEFT:
                fl_left = False
            elif event.key == py.K_RIGHT:
                fl_right = False
            elif event.key == py.K_UP:
                fl_up = False
            elif event.key == py.K_DOWN:
                fl_down = False