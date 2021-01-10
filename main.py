
############################
import pygame as pygame    #
from pygame.locals import *#
pygame.init()              #
import time                #
import random              #
############################
def get_font(path:str,size:str):
	try:
		return pygame.font.Font(path,size)
	except:		
		return pygame.font.SysFont(path, size)
class Window():
	0
def Image(path:str):
	return pygame.image.load(path)
class Font():
	def size(path:str,text:str):
		return get_font(path).size(text)
	def __call__(self, path, size):
		# If you use Text() you will call this method
		get_font(path, size)
def Text(font="sans", size:int=12, text:str="Hello world!",color=(255,0,0)):
		# If path, then importing
		return get_font(font,size).render(text,1,color)
				
root=pygame.display.set_mode((700,500))
class Interface():
	# Basic class for all types
	def __init__(self, start_coords:list=[0, 0], end_coords:list=[root.get_width(), root.get_height()], id=None, _class=None, *, content=[Text(size=50)]):
		self.size=max([contet.get_size() for contet in content])
		self.rect=[start_coords, end_coords]
		self.contents=content
	def draw(self):
		for content in self.contents:
			root.blit(content,self.rect[0])
class Button(Interface):
	def __init__(self, start_coords:list=[0, 0], end_coords:list=[root.get_width(), root.get_height()], id=None, _class=None, *, content=[Text(size=50)],onClick=""):
		self.size=max([contet.get_size() for contet in content])
		self.rect=[start_coords, end_coords]
		self.contents=content
		self.click=onClick

objects=[Interface(content=[Text(size=100)])]

while 1:
	for i in objects:
		i.draw()
	pygame.display.update()
	root.fill((0,0,0))
