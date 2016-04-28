# ***** Paquetes *****
import random as rd
import pygame as pg
import string
import sys
from pygame.locals import *


# ***** Colores *****
negro = (0,0,0)
blanco = (255,255,255)
rojo = (255,0,0)
verde = (0,255,0)
morado = (255,0,255)
azul = (0,0,255)

# ***** Metodos *****
def display_box(screen, message):
	fontobject = pg.font.Font(None,18)
	pg.draw.rect(screen, negro,
		((screen.get_width() / 2) - 100,
		(screen.get_height() / 2) - 10,
		200,20), 0)
	pg.draw.rect(screen, negro,
		((screen.get_width() / 2) - 102,
		(screen.get_height() / 2) - 12,
		204,24), 1)
	if len(message) != 0:
		screen.blit(fontobject.render(message,1,blanco),
			((screen.get_width()/2)-100,(screen.get_height()/2)-10))


#def Texto(screen,message,x1,):

# ***** MAIN *****
def main():
	pg.init()
	Ventana = pg.display.set_mode((400,300))
	pg.display.set_caption("Vemos a sumar!!")

	Pregunta = "Respuesta"
	pg.font.init()
	current_string = []
	display_box(Ventana,Pregunta + ":" + string.join(current_string, ""))

	cant = 0
	errores = 0
	rango = 10
	x = rd.randint(0,rango)
	y = rd.randint(0,rango)

	while True:
		Ventana.fill(blanco)
		display_box(Ventana, Pregunta + ": " + string.join(current_string,""))
		fontobject0 = pg.font.Font(None,36)
		fontobject1 = pg.font.Font(None,24)
		Ventana.blit(fontobject0.render("%i+%i"%(x,y),1,negro),
				((Ventana.get_width()/2)-70,(Ventana.get_height()/2)-40))
		Ventana.blit(fontobject1.render("Presionar Enter para dar tu respuesta",1,negro),
				((Ventana.get_width()/2)-140,(Ventana.get_height()/2)+30))
		Ventana.blit(fontobject1.render("Aciertos: %i"%(cant - errores),1,negro),
				(30,Ventana.get_height()-30))
		for evento in pg.event.get():
			if evento.type == QUIT:
				pg.quit()
				sys.exit()
			elif evento.type == KEYDOWN:
				inkey = evento.key
				print inkey
				if inkey == K_BACKSPACE:
					current_string = current_string[0:-1]
				elif inkey == K_RETURN or inkey == K_KP_ENTER:
					resp = string.join(current_string,"")
					try:
						resp = int(resp)
						if resp == x + y:
							print "Muy bien eres muy inteligente"
						else:
							print "Eres muy mensu! la respuesta es %i"%(x+y)
							errores += 1
						
						x = rd.randint(0,rango)
						y = rd.randint(0,rango)
						cant += 1
						current_string = []
					except ValueError:
						current_string = []
				elif inkey <= 127 or (inkey>=256 and inkey<=265):
					if inkey <= 127:
						current_string.append(chr(inkey))
					else:
						inkey = inkey%208
						current_string.append(chr(inkey))
				display_box(Ventana, Pregunta + ": " + string.join(current_string,""))
		pg.display.update()

if __name__ == '__main__':
	main()
