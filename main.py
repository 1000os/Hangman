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
