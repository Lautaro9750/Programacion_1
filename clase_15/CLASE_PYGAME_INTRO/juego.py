import pygame

pygame.init()
#Acá fuera van constantes para después meter un código más lindo.
#La creación de la pantalla principal, adentro va el funcionamiento en sí.
ancho_ventana = 500
alto_ventana = 500

color_blanco = (123, 200, 246)
color_verde = (0,255,0)
color_x = (230,12,200)
color_rojo = (255,0,0)


ventana_ppal = pygame.display.set_mode((ancho_ventana,alto_ventana)) #ventana principal del juego(ancho y alto) y tamaño de la misma
pygame.display.set_caption("Test game")
print((type(ventana_ppal))) #<class 'pygame.Surface'>
posicion_circulo = [300, 300]#Tuve que cambiar de paréntesis a lista

#TIMER
timer_segundo = pygame.USEREVENT
pygame.time.set_timer(timer_segundo,100)#1 vez por segundo se va a ejecutar, ejemplo que haya un tiempo, o que se mueva algo cada cierto tiempo, por ejemplo.

#Leer una imagen.
imagen_xd = pygame.image.load("C:/Users/Lautaro/Desktop/Capturas/Asi-lucian-las-versiones-adolescentes-de-Misato-y-Kaji-en-Neon-Genesis-Evangelion-1.jpg")
imagen_xd = pygame.transform.scale(imagen_xd,(150,150))
rect_misato = pygame.Rect(0,0,150,150)

#Crear un texto
fuente = pygame.font.SysFont("Arial",30)
texto = fuente.render("HOLA MISATO",True,color_rojo)

flag_run = True
while flag_run:

    lista_eventos = pygame.event.get()#Cosas que suceden.
    for evento in lista_eventos:
        if evento.type == pygame.quit:
            flag_run = False
        if evento.type == pygame.MOUSEBUTTONDOWN:
            print(evento.pos)#Evento tiene la coordenadas y pos ayuda por x e y.
            posicion_circulo = list(evento.pos)#Hacemos que el circulo se ponga en el centro del click. Dependiendo donde use el flip o las otras variables, puedo pasar el circulo por detrás como adelante. Se castea porque me devuelve una tupla.
        if evento.type == pygame.USEREVENT: #Se  if evento.type == timer_segundo si hay uno solo, si no,  se pone if evento.type == pygame.USEREVENT
            if evento.type == timer_segundo:
                if(posicion_circulo[0] < ancho_ventana + 80):
                    posicion_circulo[0] = posicion_circulo[0] + 10 #Se mueve el circulo para la derecha cada cieto tiempo. Está lógica me sirve para que se vaya moviendo el paisaje de  fondo.
                else: 
                    posicion_circulo[0] = -80
        if evento.type == pygame.KEYDOWN: #Eventos hasta cuando apreto la tecla, suelto y vuelvo a apretar.
            if evento.key == pygame.K_SPACE:
                posicion_circulo[1] = posicion_circulo[1] + 10

    lista_teclas = pygame.key.get_pressed() #Me devuelve las teclas presionadas.
    if lista_teclas[pygame.K_LEFT]:
        posicion_circulo[1] = posicion_circulo[1] + 1


    ventana_ppal.fill(color_verde) #Dar color a la  ventana.0
    pygame.draw.rect(ventana_ppal,color_blanco,(30,60,100,200))
    pygame.draw.circle(ventana_ppal,color_x,posicion_circulo,80)
    ventana_ppal.blit(imagen_xd,(rect_misato))
    ventana_ppal.blit(texto,(300,300))




    pygame.display.flip() #Se ven los cambios ejecutados, con este código.

pygame.quit() #Cierra a nivel programa de forma prolija. El programa cierra cuando sale del While.