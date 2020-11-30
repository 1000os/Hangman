import pygame
import random

#setting up the screen------------------------------------------------------------------------------------------------------
pygame.init()
WIDTH, HEIGHT = 800,500
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Hangman")
#making classes-------------------------------------------------------------------------------------------------------------
class word():
    def __init__(self, word):
        self.string = word
        self.word_len = len(self.string)
        self.letters = []
        
        for index, letter in enumerate(self.string):
            self.letters.append(self.string[index])
        print(self.letters)
    def draw(self):
        
        for index in range(len(self.letters)):
            if self.letters[index] == self.letters[index].upper():
                if index == 0:
                    ShowText(self.letters[index],(255,255,255),index*30+350,220)
                else:
                    ShowText(self.letters[index].lower(),(255,255,255),index*30+350,220)
            else:
                line_start = (index*30+350,250)
                line_end = (line_start[0]+20,250)
                pygame.draw.line(screen,(255,255,255), line_start, line_end, 1)
                
class VirtualKeyboard():
    def __init__(self):
        self.keys = ["Q","W","E","R","T","Y","U","I","O","P",
                        "A","S","D","F","G","H","J","K","L",
                         "Z","X","C","V","B","N","M","-"]

        
#making functions------------------------------------------------------------------------------------------------------
def MouseInRect(x,y,w,h):
    if pygame.mouse.get_pos()[0] > x and pygame.mouse.get_pos()[0] < x+w\
       and pygame.mouse.get_pos()[1] > y and pygame.mouse.get_pos()[1] < y+h:
        return True
    else:
        return False

def ShowText(text, colour,x,y):
    screen_text = FONT.render(text, True, colour)
    screen.blit(screen_text,[x,y])

def KeyboardInput():

    value_returned = False
    
    for letter in range(10):
        if MouseInRect((75*letter)+50,300,35,35):
            return vk.keys[letter]
            value_returned = True

    for letter in range(9):
        if MouseInRect((75*letter)+100,350,35,35):
            return vk.keys[letter+10]
            value_returned = True
            
    for letter in range(8):
        if MouseInRect((75*letter)+150,400,35,35):
            return vk.keys[letter+19]
            value_returned = True
            
    if not value_returned:
        return False
