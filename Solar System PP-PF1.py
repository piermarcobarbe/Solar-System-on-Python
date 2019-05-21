#!/usr/local/bin/python

__author__ = 'Andrea Vicari'

import turtle

planets_inf = {'Mercury':[88, 57.9, 2440], 'Venus':[224, 108.2, 6100], 'Earth':[365, 149.6, 6378], 'Mars':[687, 227.9, 3380], 'Jupiter':[4328, 778.3, 71350], 'Saturn':[10752, 1429, 60400], 'Uranus':[30663, 2875, 23800], 'Neptune':[60152, 4496, 22200]}


#Background
screen = turtle.Screen()
turtle.setworldcoordinates(-30000, -30000, 30000, 30000)
screen.title("Solar System")
turtle.bgpic('planet_textures/universe.gif')
screen.setup (width=1500, height=1000, startx=0, starty=0)


#Import images in the register of the shapes
turtle.register_shape('planet_textures/sole.gif')
turtle.register_shape('planet_textures/mercurio.gif')
turtle.register_shape('planet_textures/venere.gif')
turtle.register_shape('planet_textures/terra.gif')
turtle.register_shape('planet_textures/marte.gif')
turtle.register_shape('planet_textures/giove.gif')
turtle.register_shape('planet_textures/saturno.gif')
turtle.register_shape('planet_textures/urano.gif')
turtle.register_shape('planet_textures/nettuno.gif')



#Create one different turtle for each Planet
sun = turtle.Turtle()
mercury = turtle.Turtle()
venus = turtle.Turtle()
earth = turtle.Turtle()
mars = turtle.Turtle()
jupiter = turtle.Turtle()
saturn = turtle.Turtle()
uranus = turtle.Turtle()
neptune = turtle.Turtle()
asteroids = turtle.Turtle()


#Legenda
legenda = turtle.Turtle()
legenda1 = turtle.Turtle()
legenda2 = turtle.Turtle()
legenda3 = turtle.Turtle()
legenda4 = turtle.Turtle()
legenda5 = turtle.Turtle()
start_write = turtle.Turtle()
start_write1 = turtle.Turtle()
end_write = turtle.Turtle



#Informations about planets
information = turtle.Turtle()
information1 = turtle.Turtle()
information2 = turtle.Turtle()
information3 = turtle.Turtle()


#definition starting title
def start():
    start_write.pu()
    start_write1.pu()
    start_write.goto(-6500, 0)
    start_write1.goto(-10000, 2000)
    start_write.hideturtle()
    start_write1.hideturtle()
    start_write.color('white')
    start_write1.color('white')
    start_write.write('Press RETURN to start the simulation.', font=(80))
    start_write1.write('WELCOME TO THE SOLAR SYSTEM SIMULATION!', font=(100))
    screen.mainloop()


def hide_start():
    start_write.reset()
    start_write1.reset()

    
#definitions of the written parts
def legen():
    legenda.pu()
    legenda1.pu()
    legenda2.pu()
    legenda3.pu()
    legenda4.pu()
    legenda5.pu()
    legenda.goto(-57000, 32000)
    legenda1.goto(-60500, 29500)
    legenda2.goto(-60500, 28000)
    legenda3.goto(-60500, 26500)
    legenda4.goto(-60500, 25000)
    legenda5.goto(-60500, 23500)
    legenda.hideturtle()
    legenda1.hideturtle()
    legenda2.hideturtle()
    legenda3.hideturtle()
    legenda4.hideturtle()
    legenda5.hideturtle()
    legenda.color('white')
    legenda1.color('white')
    legenda2.color('white')
    legenda3.color('white')
    legenda4.color('white')
    legenda5.color('white')
    legenda.write('SOLAR SYSTEM ANIMATION', font=(30))
    legenda1.write('- Press UP ARROW for the fast animation.', font=(20))
    legenda2.write('- Press DOWN ARROW for the slow animation.', font=(20))
    legenda3.write('- Press RIGHT ARROW for orbits only.', font=(20))
    legenda4.write('- Press R to restart.', font=(20))
    legenda5.write('- Click on the planets to read information about them.', font=(20))
   
def hide_legen():
    legenda.reset()
    legenda1.reset()
    legenda2.reset()
    legenda3.reset()
    legenda4.reset()
    legenda5.reset()

#definition of the sun
def d_sun():
    sun.shape('planet_textures/sole.gif')
    sun.goto(0,0)

#general definition of the planet and the asteroids
def planet(name_planet, shape, color, angle, distance, size):
    name_planet.shape(shape)
    name_planet.color(color)
    name_planet.turtlesize(size)
    name_planet.penup()
    name_planet.left(angle)
    name_planet.forward(distance)
    name_planet.pendown()
    name_planet.left(90)


def aster():
    screen.tracer(0)
    asteroids.shape('circle')
    asteroids.color('grey')
    asteroids.turtlesize(0.0001)
    asteroids.penup()
    asteroids.forward(20909)
    asteroids.left(90)
    for i in range(25):
        asteroids.circle(20909, 27.085)
        asteroids.dot()
    asteroids.left(90)
    asteroids.forward(2000)
    asteroids.right(90)
    for i in range(25):
        asteroids.circle(19553.5, 18.085, 2)
        asteroids.dot()
    asteroids.left(90)
    asteroids.forward(2000)
    asteroids.right(90)
    for i in range(25):
        asteroids.circle(18553.5, 11.085, 1)
        asteroids.dot()

#definition for receiving information about planets
#where to put the information box
def position_inf():
    information.reset()
    information1.reset()
    information2.reset()
    information3.reset()
    information.pu()
    information1.pu()
    information2.pu()
    information3.pu()
    screen.tracer(0)
    information.goto(-60500, -19500)
    information1.goto(-60500, -21000)
    information2.goto(-60500, -22500)
    information3.goto(-60500, -24000)
    information.hideturtle()
    information1.hideturtle()
    information2.hideturtle()
    information3.hideturtle()
    information.color('white')
    information1.color('white')
    information2.color('white')
    information3.color('white')
    screen.update()

    
#information about Planets
def inf_planets(x, y):
    position_inf()
    coordinat = (x, y)

    if (-6000, 0) < coordinat < (6000, 0):
        key = 'Sun'
        name = 'This is the Sun:'
        old = 'It is 5 billion year old.'
        temperature =' It reahces ~6000 degrees on the surface, 15 million degrees at the center.'
        radius = '1.4 million Kilometers of radius.'
        information.write(name, font = 60)
        information1.write(old, font = 30)
        information2.write(temperature, font = 30)
        information3.write(radius, font = 30)
        
    
    if (8500, 0) < coordinat < (10000, 0):
        key = 'Mercury'
        
    if (10800, 0) < coordinat < (12500, 0):
        key = 'Venus'
        
    if (13000, 0) < coordinat < (15500, 0):
        key = 'Earth'
        
    if (15800, 0) < coordinat < (17300, 0):
        key = 'Mars'
        
    if (22000, 0) < coordinat < (27000, 0):
        key = 'Jupiter'
        
    if (30000, 0) < coordinat < (38000, 0):
        key = 'Saturn'

    if (40000, 0) < coordinat < (46000, 0):
        key = 'Uranus'
        
    if (50000, 0) < coordinat < (56000, 0):
        key = 'Neptune'
        
    name = 'This Planet is ' + key +':'
    days = str(planets_inf[key][0]) + ' days to complete one orbit.'
    distance = str(planets_inf[key][1]) + ' millions Kilometers from the Sun.'
    radius = str(planets_inf[key][2]) + ' Kilometers of radius.'
    information.write(name, font = 60)
    information1.write(days, font = 30)
    information2.write(distance, font = 30)
    information3.write(radius, font = 30)       

#put the Sun, the planets and the ateroids in position
def main():
    hide_start()
    d_sun()
    screen.tracer(2)
    planet  (mercury,  'planet_textures/mercurio.gif',      'brown',      0,   9058,     0.1)
    planet  (venus,    'planet_textures/venere.gif',        'orange',     0,   11309,    0.31)
    planet  (earth,    'planet_textures/terra.gif',         'blue',       0,   13650,    0.39)
    planet  (mars,     'planet_textures/marte.gif',         'green',      0,   16028,    0.277)
    planet  (jupiter,  'planet_textures/giove.gif',         'purple',     0,   24790,    2.84)
    planet  (saturn,   'planet_textures/saturno.gif',       'pink',       0,   34300,    2.095)
    planet  (uranus,   'planet_textures/urano.gif',         'grey',       0,   42750,    1.495)
    planet  (neptune,  'planet_textures/nettuno.gif',       'red',        0,   52000,    1.341)
    aster()
    legen()
    screen.update()

#reset the screen
def reset():
    screen.reset()
    start()
    



##different definitions for making the planets move around the Sun (every definition changes tracer in order to modify the speed)
    
#1 Results of the equation from the real values
def move_planets_superspeed():
    screen.tracer(2000)
    hide_legen()
    for x in range(679):
       mercury.circle(9058, 450)
       venus.circle(11309, 143.40)
       earth.circle(13650, 88)
       mars.circle(16028, 46.75)
       jupiter.circle(24790, 7.42)
       saturn.circle(34300, 2.99)
       uranus.circle(42750, 1.04)
       neptune.circle(52000, 0.53)
       screen.update()
    
#2
def move_planets_orbitsonly():
    screen.tracer(0)
    hide_legen()
    for x in range(360):
       mercury.circle(9058, 2)
       venus.circle(11309, 2)
       earth.circle(13650, 2)
       mars.circle(16028, 2)
       jupiter.circle(24790, 2)
       saturn.circle(34300, 2)
       uranus.circle(42750, 2)
       neptune.circle(52000, 2)
       
#3 Values chosen in order to see the planets move at the same speed
def move_planets_slowly():
    screen.tracer(128)
    hide_legen()
    for x in range(360):
       mercury.circle(9058, 8)
       venus.circle(11309, 7)
       earth.circle(13650, 6)
       mars.circle(16028, 5)
       jupiter.circle(24790, 4)
       saturn.circle(34300, 3)
       uranus.circle(42750, 2)
       neptune.circle(52000, 1)
       screen.update()
    
#4 slowly rappresentation of the superspeed definition
def move_planets_debug():
    screen.tracer(20)
    hide_legen()
    for x in range(680):
       mercury.circle(9058, 450)
       venus.circle(11309, 143.40)
       earth.circle(13650, 88)
       mars.circle(16028, 46.75)
       jupiter.circle(24790, 7.42)
       saturn.circle(34300, 2.99)
       uranus.circle(42750, 1.04)
       neptune.circle(52000, 0.53)
       screen.update()

    

######################################user's choiches#############################


#keys inputs
screen.onkey(move_planets_superspeed, "Up")
screen.onkey(move_planets_orbitsonly, "Right")
screen.onkey(move_planets_slowly, "Down")
screen.onkey(main, "Return")
screen.onkey(move_planets_debug, "d")
screen.onkey(reset, "r")
screen.onkey(reset, "R")
screen.onkey(move_planets_debug, "D")
screen.onclick(inf_planets)

screen.listen()

start()

