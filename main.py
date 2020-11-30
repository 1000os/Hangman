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
    
    
    
def DrawKeyboard():    
    for x in range(10):
        pygame.draw.ellipse(screen,(255,255,255),[(75*x)+50,300,35,35])
    for x in range(9):
        pygame.draw.ellipse(screen,(255,255,255),[(75*x)+100,350,35,35])
    for x in range(8):
        pygame.draw.ellipse(screen,(255,255,255),[(75*x)+150,400,35,35])
    
    for x in range(10):
        ShowText(vk.keys[x],(0,0,0),(75*x)+55,295)
    for x in range(9): 
        ShowText(vk.keys[x+10],(0,0,0),(75*x)+105,345)
    for x in range(8):
        ShowText(vk.keys[x+19],(0,0,0),(75*x)+155,395)

def DrawEverything():
    screen.fill((50,50,50))
    DrawKeyboard()
    w.draw()
    if attempts <= 6:
        screen.blit(images[hangman_status],(50,50))
    ShowText("Attempts left: " + str(len(images)-attempts),(255,255,255),650,30)

#loading the images----------------------------------------------------------------------------------------------------------------------------------------------------------------
images = []
for i in range(7):
    image = pygame.image.load("hangman"+str(i)+".png")
    images.append(image)

#game variables------------------------------------------------------------------------------------------------------------------------------------------------------------
hangman_status = 0
f = open('WordList.txt','r')
content = f.read()
f.close()
print(type(content))
WORD_LIST = content.split(",")
word_string = random.choice(WORD_LIST)
print(word_string)
FONT = pygame.font.Font("Pacifico.ttf",20)
w = word(word_string)
vk = VirtualKeyboard()
gs = 1
global attempts
attempts = 0
