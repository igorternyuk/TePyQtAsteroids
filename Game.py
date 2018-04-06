from PyQt5.QtCore import*
from Ship import*
from Asteroid import*
from Star import*
from Projectile import*
from KeyState import*
from enum import Enum
from math import*
import random

class GameState( Enum ):
    PLAYING = 0
    PAUSED = 1
    GAME_OVER = 2

class Game:
    def __init__( self, window_width, window_height ):
        self.NUM_STARS = 300
        self.SMALL_FONT = QFont( "Arial", 25 )
        self.LARGE_FONT = QFont( "Arial", 80 )
        self.score = 0
        self.level = 1
        self.field_width = window_width
        self.field_height = window_height
        self.state = GameState.PLAYING
        self.entities = []
        self.start_ship_pos = Vector2D( self.field_width / 2, self.field_height / 2 )
        self.ship = Ship( self, self.start_ship_pos )
        self.__create_asteroids_()
        self.__create_stars_()

    def reset( self ):
        self.score = 0
        self.level = 1
        self.state = GameState.PLAYING
        self.ship.reset()
        self.entities = []
        self.__create_asteroids_()
        self.__create_stars_()

    def __create_asteroids_( self ):
        for i in range( self.level + 5 ):
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
        if self.state == GameState.PLAYING:
            self.ship.handleUserInput( key_state )

    def __get_asteroids_( self ):
        return [ e for e in self.entities if type(e) is Asteroid ]

    def __get_projectiles_( self ):
        return [ e for e in self.entities if type(e) is Projectile ]

    def __check_collisions_( self ):
        projectiles = self.__get_projectiles_()
        asteroids = self.__get_asteroids_()
        print("-------------------------------")
        for a in asteroids:
            dist = self.ship.distance_to( a )
            #print("dist = ", dist )
            #print("a.radius = ", a.radius )
            #print("self.ship.circum_radius = ", self.ship.circum_radius)
            #print("self.ship.circum_radius + a.radius = ", self.ship.circum_radius + a.radius )
            if dist <= self.ship.circum_radius:
                #print("ship collision dist = ", dist )
                self.ship.hit()
                #print("lives remains ", self.ship.lives )
                if not self.ship.is_alive():
                    self.state = GameState.GAME_OVER
                    return
                a.alive = False
                break
        for p in projectiles:
            for a in asteroids:
                if a.distance_to(p) < a.radius:
                    if a.radius > 25:
                        a.radius /= 1.3
                    else:
                        a.alive = False
                    p.alive = False
                    self.score += 1
                    break
        if len( asteroids ) == 0:
            self.level += 1
            self.__create_asteroids_()

    def update_phase( self ):
        if self.state == GameState.PLAYING:
            self.ship.update()
            self.entities = [ e for e in self.entities if e.is_alive() ]
            for e in self.entities:
                e.update()
            self.__check_collisions_()

    def render_phase( self, painter ):
        self.render_background( painter )
        for e in self.entities:
            e.render( painter )
        self.ship.render( painter )
        self.render_game_info( painter )
        if self.state == GameState.GAME_OVER:
            self.render_game_over( painter )

    def render_background( self, painter ):
        painter.fillRect( 0, 0, self.field_width, self.field_height, Qt.black)

    def render_game_info( self, painter ):
        text = "(Level:%d Score:%d Lives:%d)" % ( self.level, self.score,
         self.ship.lives )
        painter.setFont( self.SMALL_FONT )
        painter.setPen( QPen( Qt.green, 20) )
        painter.drawText( QRectF( 0, 0, self.field_width, 100 ),
         Qt.AlignLeft | Qt.AlignCenter, text )

    def render_game_over( self, painter ):
        painter.setFont( self.LARGE_FONT )
        painter.setPen( QPen( Qt.red, 20) )
        painter.drawText( QRectF( 0, 0, self.field_width, self.field_height ),
         Qt.AlignCenter | Qt.AlignCenter, "GAME OVER!!!" )
