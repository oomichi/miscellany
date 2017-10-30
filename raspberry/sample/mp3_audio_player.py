import pygame.mixer
import time

pygame.mixer.init()
pygame.mixer.music.load("closer.mp3")
mtime = pygame.mixer.music.get_pos()
print("%s" % mtime)
pygame.mixer.music.play(1)


time.sleep(10)
pygame.mixer.music.fadeout(100)
