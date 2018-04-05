from PyQt5.QtCore import*
from Ship import*
from Asteroid import*
from Star import*
from Projectile import*
from KeyState import*
from math import*
import random

class Game:
    def __init__( self, window_width, window_height ):
        self.NUM_STARS = 300
        self.field_width = window_width
        self.field_height = window_height
        self.entities = []
        self.start_ship_pos = Vector2D( self.field_width / 2, self.field_height / 2 )
        self.ship = Ship( self, self.start_ship_pos )
        self.__create_asteroids_()
        self.__create_stars_()
        self.level = 5

    def reset( self ):
        self.level = 1

    def __create_asteroids_( self ):
        for i in range( 5 ):
            self.__add_asteroid_()

    def __create_stars_( self ):
        for i in range( self.NUM_STARS ):
            x = random.choice( range( self.field_width ) )
            y = random.choice( range( self.field_height ) )
            position = Vector2D( x, y )
            rand_angle = random.choice( range( 360 ) )
            velocity = Vector2D( 0.25 * cos( rand_angle ), 0.25 * sin( rand_angle ) )
            star = Star( self, position, velocity )
            self.entities.append( star )

    def __add_asteroid_( self ):
        while True:
            x = random.choice( range( self.field_width ) )
            y = random.choice( range( self.field_height ) )
            position = Vector2D( x, y )
            rand_angle = random.choice( range( 360 ) )
            velocity = Vector2D( 5 * cos( rand_angle ), 5 * sin( rand_angle ) )
            radius = random.choice( range( 10, 40) )
            edge_number = random.choice( range( 5, 10) )
            asteroid = Asteroid( self, Vector2D( x, y ), velocity, radius,
             edge_number )
            if self.ship.distance_to( asteroid) >= 100.0:
                self.entities.append( asteroid )
                break

    def user_input_phase( self, key_state ):
        self.ship.handleUserInput( key_state )

    def update_phase( self ):
        self.ship.update()
        self.entities = [ e for e in self.entities if e.is_alive() ]
        print(" entities.size = ", len( self.entities ))
        for e in self.entities:
            e.update()

    def render_phase( self, painter ):
        self.render_background( painter )
        for e in self.entities:
            e.render( painter )
        self.ship.render( painter )

    def render_background( self, painter ):
        painter.fillRect( 0, 0, self.field_width, self.field_height, Qt.black)
