import pygame
pygame.init()
from variables import *
import random
from classes import *
import time


#if right_mon > x  and x > x_m and (y + 98 > y_m or down_mon > y and y_m > down_ch):
#elif x_m < right_ch and right_mon > right_ch and (y + 98 > y_m or down_mon > y and y_m > down_ch):


def draw_rain(rain_list):
    for rain_dict in rain_list:
        for drop_id in rain_dict:
            drop = rain_dict[drop_id]
            pygame.draw.line(game_display, drop.color, [drop.x1, drop.y1],[drop.x2, drop.y2], drop.size)
            drop.move()
    
    
def thunder():
    random_y = random.randint(0, HEIGHT)
    random_x = random.randint(0, WIDTH)
    pick = random.randrange(1, 1000)
    if pick < 2:
        game_display.fill(white)
        
def pick_drawed_poster():
    global pick_poster
    pick_poster += 1
    if pick_poster > 15: # was 20
        game_display.blit(poster, (260, 100))
    else:
        game_display.blit(poster_without, (260, 100))
    if pick_poster > 30:
        pick_poster = 0

def pick_drawed_tutorial():
    global pick_tutorial
    pick_tutorial += 1
    if pick_tutorial > 15: # was 20
        game_display.blit(Tutorial_press, (0, 0))
    else:
        game_display.blit(Tutorial, (0, 0))
    if pick_tutorial > 70:
        pick_tutorial = 0
        
def pick_left_ch_sord():
    left_sords_list = [left_green_sord, left_orange_sord, left_master_sord, left_red_sord]
    picked_left_ch_sord = random.choice(left_sords_list)
    return picked_left_ch_sord

def pick_right_ch_sord():
    right_sords_list = [right_orange_sord, right_green_sord, right_master_sord, right_red_sord]
    picked_right_ch_sord = random.choice(right_sords_list)
    return picked_right_ch_sord



def main():
    pygame.display.set_icon(icon)
#     pygame.mixer.music.play(-1)
    next_ground = False
    on_ground = True
    on_ground_mon = True
    rain = dict(enumerate([Bsg(blue) for i in range(1000)]))
    ruler_kills = 0
    jamie_kills = 0
    score_list = []
    global sord_direction
    global play_press_sound
    global mon_shot_x_r
    global right_of_right_shot
    global mon_shot_x_l
    global bool
    global bool_t
    global bool_up
    global bool_end
    global move
    global wins_loose
    global Ruler_wins
    global right_mon
    global mon_shot_change
    global monster
    global charecter
    global x_m_change
    global y_m_change
    global x_change
    global x
    global y
    global x_m
    global y_m
    global y_change
    global right_ch
    global down_ch
    global down_mon
    global right_mon
    global bullets
    global ch_sord_change
    global ch_sord_x_r
    global ch_sord_x_l
    global shot_direction
    global jamie_wins
    global Ruler_wins
#     global
#     global
    
 # '''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''' # 
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    charecter = pygame.image.load("g4 (2)_flip.png")
                    sord_direction = -1
                    x_change = -16
                elif event.key == pygame.K_RIGHT:
                    charecter = pygame.image.load("g4 (2).png")
                    sord_direction = 1
                    x_change = 16
                elif event.key == pygame.K_UP and y == 508:
                    y_change = -30
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT:
                    x_change = 0
                elif event.key == pygame.K_LEFT:
                    x_change = 0
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    monster = pygame.image.load("ghost3.png")
                    shot_direction = 1
                    x_m_change = -15
                elif event.key == pygame.K_d:
                    monster = pygame.image.load("ghost3_flip.png")
                    shot_direction = -1
                    x_m_change = 15
                elif event.key == pygame.K_w and y_m == 350:
                    y_m_change = -30
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_a:
                    x_m_change = 0
                elif event.key == pygame.K_d:
                    x_m_change = 0

 # '''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''' # 
#             if event.type == pygame.KEYDOWN:
#                 bool_t = True
            if event.type == pygame.KEYUP:
                bool_up = True
                if play_press_sound < 2:
                    pygame.mixer.Sound.play(press_sound)
                    play_press_sound += 1
        if bool_up == True:
            if event.type == pygame.KEYDOWN:
                    bool = True
            if bool == True:
#                 pygame.mixer.music.stop()
                game_display.blit(back_round, (0, 0))
                draw_rain([rain])
                thunder()
                game_display.blit(ground1, (first_ground_x, first_and_second_ground_y))
                game_display.blit(ground1, (third_ground_x, first_and_second_ground_y))
                game_display.blit(ground1, (second_ground_x, first_and_second_ground_y))
                game_display.blit(ground1, (right_b_ground_x, right_b_ground_y))
                game_display.blit(ground1, (left_b_ground_x, left_b_ground_y))
                game_display.blit(ground1, (left_u_ground_x, left_and_right_u_ground_y))
                game_display.blit(ground1, (right_u_ground_x, left_and_right_u_ground_y))
                
#                 game_display.blit(ground1, (third_ground_x, third_ground_y))
                game_display.blit(monster, (x_m, y_m))
                game_display.blit(ground1, (0, 629))
                game_display.blit(ground1, (200, 629))
                game_display.blit(ground1, (475, 629))
                game_display.blit(ground1, (780, 629))
                game_display.blit(charecter, (x, y))
                game_display.blit(monster, (x_m, y_m))
                x += x_change
                y += y_change
                right_mon = x_m + 240
                right_ch = x + 98
                down_ch = y + 98
                space_ship_rect.x += x_change
                if right_mon > WIDTH+50:
                    x_m = WIDTH-247
                elif x_m < -47:
                    x_m = -47
                x_m += x_m_change
                y_m += y_m_change
#                 if y_m > 350:
#                     y_m = 350
#                 elif y_m < 0 :
#                     y_m = 0
# '''''''''''''''''''''''''''''''''''''''''''''''''''''''''left_ground_box''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''' #
                if down_mon < first_and_second_ground_y and first_ground_x <  right_mon and x_m < right_second_ground_x-140:
                    y_m_change = 0
                    on_ground_mon = True
                if down_mon < left_b_ground_y and y_m > left_b_ground_y-280 and right_mon-100 < right_left_b_ground_x:
                    y_m_change = 0
                    on_ground_mon = True
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_w:
                            y_m_change = -30
                if down_mon < right_b_ground_y and y_m > right_b_ground_y-300 and right_mon-100 > right_b_ground_x:
                    y_m_change = 0 
                    on_ground_mon = False
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_w:
                            y_m_change = -30
                if down_mon < right_b_ground_y and y_m > right_b_ground_y-300 and right_mon-100 < right_b_ground_x and not on_ground_mon:
                    y_m_change = 15
                if down_mon < first_and_second_ground_y and first_ground_x > right_mon-100 or down_mon < first_and_second_ground_y and  x_m > right_second_ground_x-140 and on_ground_mon:
                    y_m_change = 15
                if down_mon < left_b_ground_y and y_m > left_b_ground_y-280 and right_mon-100 > right_left_b_ground_x and on_ground_mon:
                    y_m_change = 15
                
#                 if down_mon < left_b_ground_y and down_mon > left_b_ground_y-5 and right_mon < right_left_b_ground_x:
#                     y_m_change = 0
                        
#                 if right_first_ground_x+95< right_mon and down_mon < first_and_second_ground_y or x_m +145 < first_ground_x and down_mon < first_and_second_ground_y:
#                     y_m_change = 15
#                 if first_ground_x < right_mon and down_mon < first_and_second_ground_y or x > right_second_ground_x:
#                     y_m_change = 15
                if y_m < 0:
                    y_m = 0
                    y_m_change = 40

                if y_m > 350:
                    on_ground_mon = True
                    y_m = 350
                if y > 508:
                    on_ground = True
                    y = 508 
                        
                if down_ch < left_b_ground_y and down_ch > left_b_ground_y-5 and right_ch < right_left_b_ground_x:
                    y_change = 0
                    on_ground = False
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_UP:
                            y_change = -30
                if down_ch < right_b_ground_y and down_ch > right_b_ground_y-5 and x > right_b_ground_x:
                    y_change = 0
                    on_ground = True
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_UP:
                            y_change = -30
                if down_ch < right_b_ground_y:
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_UP:
                            y_change = -30
                if down_ch < right_b_ground_y and down_ch > right_b_ground_y-5 and right_ch < right_b_ground_x and on_ground:
                    y_change = 15
                if down_ch < left_b_ground_y and down_ch > left_b_ground_y-5 and right_ch > right_left_b_ground_x and not on_ground:
                    y_change = 15

                if down_ch < first_and_second_ground_y and x+64 > first_ground_x or down_ch < first_and_second_ground_y and x < right_second_ground_x:
                    y_change = 0
                    on_ground = False
#                 if event.type == pygame.KEYDOWN:
#                     if event.key == pygame.K_UP:
#                         y_change = -30
                if x+64 < first_ground_x and down_ch < first_and_second_ground_y or x > right_second_ground_x and down_ch < first_and_second_ground_y:
                    y_change = 15
#                 if right_first_ground_x+60< right_ch and down_ch < first_and_second_ground_y and next_ground == False or x+64 < first_ground_x and down_ch < first_and_second_ground_y:
#                     y_change = 15
#                 if next_ground and down_ch < first_and_second_ground_y and x > right_second_ground_x or next_ground and down_ch < first_and_second_ground_y and right_ch < second_ground_x:
#                     next_ground = True
#                
# '''''''''''''''''''''''''''''''''''''''''''''''''''''''''right_ground_box''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''' #     

# '''''''''''''''''''''''''''''''''''''''''''''''''''''''''high_ground_box''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''' # 

# ''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''' #                   
                if right_ch > WIDTH:
                    x = WIDTH-100
                elif x < 0:
                    x = 0
#                 if y_m_change == -40:
#                     if y_m < 100:
#                         y_m = 100
#                         y_m_change = 40

                if y < 10:
                    y = 10
                    y_change = 15
#                 if y > 508:
#                     y = 508
#                 if y < 0 :
#                         y = 0
                down_mon = y_m + 235
# '''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''' #                        
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_e and shot_direction == 1:
                        shot_pic = pygame.image.load("left_shot.png")
                        x_shot_pic = mon_shot_x_l
                        mon_shot_x_l = right_mon/1.2
                        mon_shot_y = y_m + 140
                        mon_shot_change = -20
                    elif event.key == pygame.K_e and shot_direction == -1:
                        shot_pic = pygame.image.load("right_shot.png")
                        x_shot_pic = mon_shot_x_r
                        mon_shot_x_r = x_m + 20
                        right_of_right_shot = mon_shot_x_r + 74
                        mon_shot_y = y_m + 140
                        mon_shot_change = 20
    #             if bullets < 400:
                if mon_shot_change == -20 or mon_shot_change == 20:
#                     bullets += 1
                    x_shot_pic += mon_shot_change
                    mon_shot_x_l += mon_shot_change
                    mon_shot_x_r += mon_shot_change
                    down_ch = y + 98
                    game_display.blit(shot_pic, (x_shot_pic, mon_shot_y))
# '''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''' #  

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RSHIFT and sord_direction == -1:
                        sord_pic = pick_left_ch_sord()#pygame.image.load("left_orange_sord.png")
                        x_shot_pic_ch = ch_sord_x_l
                        ch_sord_x_l = right_ch/1.2
                        ch_sord_y = y
                        ch_sord_change = -20
                    elif event.key == pygame.K_RSHIFT and sord_direction == 1:
                        sord_pic = pick_right_ch_sord()
                        x_shot_pic_ch = ch_sord_x_r
                        ch_sord_x_r = x + 20
                        right_of_right_sord = ch_sord_x_l + 148
                        ch_sord_y = y
                        ch_sord_change = 20
    #             if bullets < 400:
                if ch_sord_change == -20 or ch_sord_change == 20:
#                     bullets += 1
                    x_shot_pic_ch += ch_sord_change
                    ch_sord_x_l += ch_sord_change
                    ch_sord_x_r += ch_sord_change
                    down_mon = y_m + 235
                    game_display.blit(sord_pic, (x_shot_pic_ch, ch_sord_y))    

# '''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''' #          
                if mon_shot_change == -20:
                    if mon_shot_x_l < right_ch and x < mon_shot_x_l and mon_shot_y < down_ch and mon_shot_y > y-25: # mon_shot_y > y
                        pygame.mixer.Sound.play(hit_jamie_sound)
                        Ruler_wins = True
                        score_list.append(ruler_kills)
                        jamie_wins = False
                        bool_end = True
                        
                elif mon_shot_change == 20:
                    if mon_shot_x_r - x > 50 and mon_shot_x_r < right_ch and mon_shot_y < down_ch and mon_shot_y > y-25:#right_of_right_shot > x
                        pygame.mixer.Sound.play(hit_jamie_sound)
                        Ruler_wins = True
                        jamie_wins = False
                        bool_end = True
# '''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''' #
                if ch_sord_change == -20:
                    if ch_sord_x_l < right_mon and x_m < ch_sord_x_l and ch_sord_y < down_mon and ch_sord_y > y_m-25: # mon_shot_y > y
                        pygame.mixer.Sound.play(hit_ruler_sound)
                        jamie_wins = True
                        jamie_kills += 1
                        Ruler_wins = False
                        bool_end = True
                        
                elif ch_sord_change == 20:
                    if ch_sord_x_r - x_m > 50 and ch_sord_x_r < right_mon and ch_sord_y < down_mon and ch_sord_y > y_m-25:#right_of_right_shot > x
                        pygame.mixer.Sound.play(hit_ruler_sound)
                        jamie_wins = True
                        jamie_kills += 1
                        Ruler_wins = False
                        bool_end = True
# '''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''' #
                if bool_end == True and jamie_wins:
                    basicfont = pygame.font.SysFont(None, 48)
                    score = basicfont.render(str(jamie_kills), True, (255, 0, 0), (0, 0, 0))
                    score_r = basicfont.render(str(ruler_kills), True, (255, 0, 0), (0, 0, 0))
                    x_m = -1000
                    game_display.blit(jamie_wins_display, (0, 0))
                    game_display.blit(score, (855, 550))
                    game_display.blit(score_r, (215, 550))
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_SPACE:
                            pygame.quit()
                            quit()
                        elif event.key == pygame.K_p:
                            bool_end = False
                            x_m = -1000
                elif bool_end == True and Ruler_wins:
                    basicfont = pygame.font.SysFont(None, 48)
                    score = basicfont.render(str(jamie_kills), True, (255, 0, 0), (0, 0, 0))
                    score_r = basicfont.render(str(ruler_kills), True, (255, 0, 0), (0, 0, 0))
                    x_m = -1000
                    game_display.blit(ruler_wins_display, (0, 0))
                    game_display.blit(score, (855, 550))
                    game_display.blit(score_r, (215, 550))
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_SPACE:
                            ruler_kills += 1
                            pygame.quit()
                            quit()
                        elif event.key == pygame.K_p:
                            ruler_kills += 1
                            bool_end = False
                            x_m = -1000
            else:
                pick_drawed_tutorial()
        else: 
            pick_drawed_poster()
            
        pygame.display.update()
        clock.tick(60)

if __name__ == '__main__':
    main()
