import pygame
import random
from variables import *


# class rain  (pygame_draw)
class Bsg:

    def __init__(self, color):
        self.x1 = random.randrange(-WIDTH, WIDTH)
        self.y1 = -random.randrange(50, 3000)
        self.size = 1
        self.color = color
        self.x2 = self.x1 +10
        self.y2 = self.y1 + 40

    def move(self):
        
       # self.move_y = random.randrange(-3,4)
       
        #self.y1 += 100
        #self.y1 += 10
      #  self.y2 += 10
      #   self.x1 += 10
      #  self.x2 -= 10
#      a = self.x1
#      b = self.x2
     self.y1 += random.randrange(1, 20)
     self.y2 = self.y1 + 30
     self.x1 += 5
     self.x2 += 5
    
    
     if self.y1 > HEIGHT:
         self.y1 = -random.randrange(50, 1000)
         self.y2 = self.y1 + random.randrange(30, 60)
         
     if self.x2 > WIDTH:
         self.y1 = -random.randrange(50, 1000)
         self.y2 = self.y1 + random.randrange(30, 60)
         self.x1 = random.randrange(-WIDTH, WIDTH)
         self.x2 = self.x1 + 10




# class Blob    (pygame_draw)
class Blob:

    def __init__(self, color):
        self.x = random.randrange(0, WIDTH)
        self.y = random.randrange(0, HEIGHT)
        self.size = random.randrange(4,20)
        self.color = color

    def move(self):
        self.move_x = random.randrange(-3,4)
       # self.move_y = random.randrange(-3,4)
       
        self.y += 2
        self.x += 2
        
       

        if self.x < 0: self.x = 0
        elif self.x > WIDTH: self.x = -200
        
        if self.y < 0: self.y = 0
        elif self.y > 650: self.y = -200
        
        
        
        
# class sun  (pygame_draw)              
class BlobSun:

    def __init__(self, color):
        self.x = 100
        self.y = 100
        self.size = 100
        self.color = color

    def move(self):
        self.move_x = random.randrange(-3,4)
       # self.move_y = random.randrange(-3,4)
       
        self.y += 2
        self.x += 2
        
       

        if self.x < 0: self.x = 0
        elif self.x > WIDTH: self.x = -200
        
        if self.y < 0: self.y = 0
        elif self.y > 650: self.y = -200


#class line_floor  (pygame_draw)
class BsgGr:

    def __init__(self, color):
        self.x1 = 800
        self.y1 = 550
        self.size = 100
        self.color = color
        self.x2 = 0
        self.y2 = 550

    def move(self):
        
       # self.move_y = random.randrange(-3,4)
       
        #self.y1 += 100
        #self.y1 += 10
      #  self.y2 += 10
      #   self.x1 += 10
      #  self.x2 -= 10
      pass
   
   
   
# class Shot:
#     
#     def __init__(self, image, y):
#         self.shot_pic = pygame.image.load(image)
#         self.y = y
#         
# #     def move_shot(self, key_right, key_left, mon_shot):
# #         if key_right == pygame.K_d:
# #             self.x += 5
# #         if key_left == pygame.K_e:
# #             self.x -= mon_shot
                    
#     def draw_shot(self, x, key_right, key_left, mon_shot):
#         game_display.blit(self.shot_pic, (x, self.y))
#         
#         def move_shot():
#             global x
#             if key_right == pygame.K_d:
#                 self.x += 5
#             if key_left == pygame.K_e:
#                 x -= mon_shot
#         move_shot()
#         

