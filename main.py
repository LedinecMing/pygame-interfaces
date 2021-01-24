
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
	def __init__(self, locate):
		self.locate=locate
	def setLoc(self,name):
		self.locate=name
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
objects=[]
class Interface():
	# Basic class for all types
	def __init__(self, start_coords:list=[0, 0], end_coords:list=[root.get_width(), root.get_height()], id=None, _class=None, *, content=[Text(size=50)], locate="main"):
		self.size=max([contet.get_size() for contet in content])
		self.rect=[start_coords, end_coords]
		self.contents=content
		self.locate=locate
		objects.append(self)
	def draw(self):
		for content in self.contents:
			root.blit(content,self.rect[0])
class Button(Interface):
	def __init__(self, start_coords:list=[0, 0], end_coords:list=[root.get_width(), root.get_height()], id=None, _class=None, *, content=[Text(size=50)],onClick="",locate="main"):
		self.size=max([contet.get_size() for contet in content])
		self.rect=[start_coords, end_coords]
		self.contents=content
		self.eventable=1
		self.click=onClick
		self.locate=locate
		objects.append(self)
	def event(self,event):
		if event.type==MOUSEBUTTONUP:
			if event.pos[1]<self.rect[1][1]+1 and event.pos[1]>self.rect[0][1]-1 and event.pos[0]<self.rect[1][0]+1 and event.pos[0]>self.rect[0][0]-1:
				exec(self.click)

Button(onClick="window.setLoc('main_2')", locate="main")
window=Window('main')
def main():
	root.fill((0,0,0))
	for i in objects:
		if i.eventable:
			for event in pygame.event.get():
				i.event(event)
	for i in [i for i in objects if i.locate==window.locate]:
		i.draw()
		
	pygame.display.update()
while 1:
	main()
	