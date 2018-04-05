from PyQt5.QtCore import*
#from Vector2D import*
from Ship import*
from Asteroid import*
from Star import*
from Projectile import*
from KeyState import*
from math import*
import random

class Game:
    def __init__( self, window_width, window_height ):
        self.field_width = window_width
        self.field_height = window_height
        self.start_ship_pos = Vector2D( self.field_width / 2, self.field_height / 2 )
        self.ship = Ship( self, self.start_ship_pos )
        self.__create_asteroids_()
        self.level = 5

    def reset( self ):
        self.level = 1

    def __create_asteroids_( self ):
        self.asteroids = []
        for i in range( 5 ):
            self.__add_asteroid_()

    def __add_asteroid_( self ):
        while True:
            x = random.choice( range( self.field_width ) )
            y = random.choice( range( self.field_height ) )
            position = Vector2D( x, y )
            rand_angle = random.choice( range( 360 ) )
            velocity = Vector2D( 5 * cos( rand_angle ), 5 * sin( rand_angle ) )
            asteroid = Asteroid( self, Vector2D( x, y ), velocity )
            print("self.ship.position = ", self.ship.position)
            print("asteroid.position = ", asteroid.position)
            dist = abs( self.ship.position - asteroid.position )
            if dist >= 100.0:
                self.asteroids.append( asteroid )
                break

    def user_input_phase( self, key_state ):
        self.ship.handleUserInput( key_state )

    def update_phase( self ):
        self.ship.update()
        for a in self.asteroids:
            a.update()

    def render_phase( self, painter ):
        self.render_background( painter )
        self.ship.render( painter )
        for a in self.asteroids:
            a.render( painter )

    def render_background( self, painter ):
        painter.fillRect( 0, 0, self.field_width, self.field_height, Qt.black)
