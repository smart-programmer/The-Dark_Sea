import pygame
import random

WIDTH = 1080
HEIGHT = 675

game_display = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("the dark sea")
clock = pygame.time.Clock()


green = (0, 255, 0)
blue = (0, 0, 255)
red = (255, 0, 0)
white = (250, 255, 255)
black = (0, 0, 0)
fuchsia = (255,0,255)
aqua =     (0,255,255)
purple = (138, 43, 226)
lightning = (230, 230, 255)
rc = (random.randrange(0, 255),random.randrange(0, 255), random.randrange(0, 255))


x = (WIDTH * 0.45)
y =508
y_m = 350
x_m = 10
x_m_change = 0
x_change = 0
y_m_change = 0
y_change = 0
right_mon = x_m + 240
down_mon = y_m + 240
right_ch = x + 98
down_ch = y + 98
mon_shot_change = 0
mon_bullets = 0 
mon_shot_x_l = 0
mon_shot_x_r = 0
right_of_right_shot = mon_shot_x_r + 74
hit = [x_m + 506, x_m + 506 -6, x_m + 506 + 6]
ch_sord_x_r = 0
ch_sord_x_l = 0
right_of_right_sord = 0
ch_sord_change = 0
ch_bullets = 0
play_press_sound = 0

first_ground_x = 100
right_first_ground_x = first_ground_x + 305
second_ground_x = 670
right_second_ground_x = second_ground_x + 305
third_ground_x = second_ground_x - first_ground_x-200

left_b_ground_y = 490
right_b_ground_y = 489
left_and_right_u_ground_y = 100
right_u_ground_x = 900
left_u_ground_x = -100
left_b_ground_x = -100
right_left_b_ground_x = left_b_ground_x + 305
right_b_ground_x = 900

first_and_second_ground_y = 290
third_ground_y = 180


pick_poster = 0
pick_tutorial = 0
sord_direction = 1
shot_direction = 1
bool = False
bool_t = None
bool_up = False
bool_end = None
move = True
jamie_wins = False
Ruler_wins = False


hit_sound = pygame.mixer.Sound("hit.aiff")
press_sound = pygame.mixer.Sound("press_button_sound.wav")
hit_ruler_sound = pygame.mixer.Sound("hit_ruler.wav")
hit_jamie_sound = pygame.mixer.Sound("hit_jamie.wav")

charecter = pygame.image.load("g4 (2).png")       
ground1 = pygame.image.load("homsi's_floor.png")
space_ship_rect = charecter.get_rect() 
monster = pygame.image.load("ghost3.png")
poster = pygame.image.load("begin2.jpeg")
back_round = pygame.image.load("back.jpeg")
creature_pos = monster.get_rect()
shot_pic = pygame.image.load("left_shot.png")
poster_without = pygame.image.load("poster_without.jpeg")
Tutorial_press = pygame.image.load("Tutorial_press.jpeg")
Tutorial = pygame.image.load("Tutorial.jpeg")
right_orange_sord = pygame.image.load("right_orange_sord.png")
right_green_sord = pygame.image.load("right_green_sord.png")
right_master_sord = pygame.image.load("right_master_sord.png")
right_red_sord = pygame.image.load("right_red_sord.png")
left_orange_sord = pygame.image.load("left_orange_sord.png")
left_green_sord = pygame.image.load("left_green_sord.png")
left_master_sord = pygame.image.load("left_master_sord.png")
left_red_sord = pygame.image.load("left_red_sord.png")
icon = pygame.image.load("icon.jpg")
ruler_wins_display = pygame.image.load("ruler_wins.jpeg")
jamie_wins_display = pygame.image.load("janie_wins.jpeg")

