# ***** Paquetes *****
import random as rd
import pygame as pg
import string
import sys
from pygame.locals import *


# ***** Colores *****
Ancho = 500
Alto = 400

negro = (0,0,0)
blanco = (255,255,255)
rojo = (255,0,0)
verde = (0,255,0)
morado = (255,0,255)
azul = (0,0,255)

rango = 10

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

def Comparar(Antes,Ahora):
	bolean = False
	Antes = [int(Antes[i]) for i in range(len(Antes))]
	if Antes[0] == Ahora.year and Antes[1] == Ahora.month and Antes[2] == Ahora.day:
		if Antes[3] == Ahora.hour:
			if Ahora.minute-Antes[4] <=15:
				bolean = True
		elif Ahora.hour - Antes[3] == 1:
			if Ahora.minute + 60 - Antes[4] <=15:
				bolean = True
		elif Antes[3] - Ahora.hour == 23:
			if Ahora.minute + 60 - Antes[4] <=15:
				bolean = True
	return bolean
	
def Agregar(L_ulti,L_nuev,bolean_error):
	L_ulti[0:7] = L_nuev[0:7]
	L_ulti[7] = str(int(L_ulti[7])+1)
	if bolean_error:
		L_ulti[8] = str(int(L_ulti[8])+1)
	L_ulti = ' '.join(L_ulti)
	return L_ulti


def Conver(Hora):
	H = int(Hora[0])
	M = int(Hora[1])
	S = int(Hora[2])
	MS = int(Hora[3])
	Valor = H*3600000 + M*60000 + S*1000 + MS
	return Valor

def Guardar_registro(linea,time,bolean_error):
	lineas = []
	try:
		f = open('.Resultados.txt','r')
		lineas = f.read()
		#print lineas
		lineas = lineas.split('\n')
		ultimo = lineas[-1].split(' ')
		if Comparar(ultimo,time):
			lineas[-1] = Agregar(ultimo,linea,bolean_error)
		else:
			linea = ' '.join(linea)
			lineas.append(linea)
		lineas = '\n'.join(lineas)
		f.close()
		g = open('.Resultados.txt','w')
		g.write(lineas)
		g.close()
	except IOError:
		f = open('.Resultados.txt','w')
		linea = ' '.join(linea)
		f.write(linea)
		f.close()

# ***** Bucle Principal *****
def main():
	pg.init()
	Ventana = pg.display.set_mode((Ancho,Alto))
	pg.display.set_caption("Vamos a sumar!!")

	Pregunta = "Respuesta"
	pg.font.init()
	current_string = []
	display_box(Ventana,Pregunta + ":" + string.join(current_string, ""))

	cant = 0
	errores = 0
	x = rd.randint(0,rango)
	y = rd.randint(0,rango)

	Draco = pg.image.load("Dracolaura.png").convert_alpha()
	Draco = pg.transform.scale(Draco,(120,300))
	Frank = pg.image.load("Frankie.png").convert_alpha()
	Frank = pg.transform.scale(Frank,(95,245))

	while True:
		Ventana.fill(blanco)
		Ventana.blit(Draco,(0,0))
		Ventana.blit(Frank,(Ventana.get_width()-100,55))
		display_box(Ventana, Pregunta + ": " + string.join(current_string,""))
		fontobject0 = pg.font.Font(None,60)
		fontobject1 = pg.font.Font(None,24)
		Ventana.blit(fontobject0.render("%i+%i"%(x,y),1,negro),
				((Ventana.get_width()/2)-40,(Ventana.get_height()/2)-70))
		Ventana.blit(fontobject1.render("Presionar ENTER para dar tu respuesta",1,negro),
				((Ventana.get_width()/2)-140,(Ventana.get_height()/2)+30))
		Ventana.blit(fontobject1.render("Aciertos: %i"%(cant - errores),1,negro),
				(Ventana.get_width() / 2-30,Ventana.get_height()-30))


		for evento in pg.event.get():
			if evento.type == QUIT:
				pg.quit()
				sys.exit()
			elif evento.type == KEYDOWN:
				inkey = evento.key
				if inkey == K_BACKSPACE:
					current_string = current_string[0:-1]
				elif inkey == K_RETURN or inkey == K_KP_ENTER:
					resp = string.join(current_string,"")
					try:
						resp = int(resp)
						bolean_error = False
						if resp == x + y:
							Ventana.blit(fontobject1.render("CORRECTO!!!",1,morado),
								((Ventana.get_width()/2)-50,(Ventana.get_height()/2)+70))
							pg.display.update()
						else:
							Ventana.blit(fontobject1.render("Eres muy mensu! la respuesta es: %i"%(x+y),1,rojo),
								((Ventana.get_width()/2)-120,(Ventana.get_height()/2)+70))
							pg.display.update()
							errores += 1
							bolean_error = True
						pg.time.wait(2000)
						x = rd.randint(0,rango)
						y = rd.randint(0,rango)
						cant += 1
						current_string = []
						
						# ***** Guardado en el fichero *****
						#probar si se puede abrir archvos ocultos						
						time = dt.datetime.now()
						linea = [str(time.year), str(time.month), str(time.day), 
									str(time.hour), str(time.minute), str(time.second),
									str(time.microsecond), str(cant), str(errores)]
						Guardar_registro(linea,time,bolean_error)
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
