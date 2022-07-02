import math, random, time
import pygame as pg


hand_width = 20

mass_coeff = 100
angular_mass_coeff = 100
friction = 1000000

class Hand:
    def __init__(self, canvas, length, angle, color):
        self.canvas = canvas
        self.length = length
        self.angle = angle
        self.color = color

        center = (canvas.get_width()/2,canvas.get_height()/2)
        self.center = center

        # angular velocity
        self.v = 0

        # angular acceleration
        self.a = 0
       
        
        # mass and angular mass based on length
        self.mass = mass_coeff * self.length
        self.I = angular_mass_coeff * self.length


    def update(self):

        # Calculate gravity on arm
        g = self.mass * 9.81
        fp = g * math.cos(math.radians(self.angle))

        # Calculate torque
        t = (self.length / 2) * fp

        # Apply friction based on rotation direction
        if self.v > 0:
            t -= friction * (self.mass * 0.0001)
        elif self.v < 0:
            t += friction * (self.mass * 0.0001)


        # Calculate angular acceration from gravity
        self.a = t * self.I
        self.v += self.a * 0.000001
        self.angle += self.v * 0.000001

        self._render()

        
    def _render(self):
        x = self.center[0] + math.cos(math.radians(self.angle)) * self.length
        y = self.center[1] + math.sin(math.radians(self.angle)) * self.length
        pg.draw.line(self.canvas, self.color, self.center, (x,y), hand_width)


class Agent:
    def __init__(self, canvas, color_seed):
        self.canvas = canvas


        # randomly color agents
        random.seed(color_seed)
        self.color = (random.randint(150, 255), random.randint(150, 255), random.randint(150, 255))

        # randomly place agents
        random.seed(color_seed * time.time()) # to avoid deterministic
        self.x = random.randint(0,canvas.get_width())
        self.y = random.randint(0,canvas.get_height())

        # size, angle, motion
        self.radius = 10
        self.angle = 0
        self.v = 0

        self.f = 10


    def update(self):

        self.v += 0.01
        self.angle += 1

        self.x += self.v * math.cos(math.radians(self.angle))
        self.y += self.v * math.sin(math.radians(self.angle))


        # Prevent leaving the canvas
        max_x = self.canvas.get_width()
        if self.x > max_x:
            self.x = max_x
        if self.x < 0:
            self.x = 0
        max_y = self.canvas.get_height()
        if self.y > max_y:
            self.y = max_y
        if self.y < 0:
            self.y = 0

        self._render()

        
    def _render(self):
        pg.draw.circle(self.canvas, self.color, (self.x, self.y), self.radius)
