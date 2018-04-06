from PyQt5.QtCore import QRect
from PyQt5.QtGui import QPixmap
from math import*
from Entity import*
from Vector2D import*
from Game import*
from KeyState import*
from Projectile import*

class Ship( Entity ):
    def __init__( self, game, position, velocity = Vector2D( 0, 0) ):
        super().__init__( position, velocity )
        self.image = QPixmap("spaceship.png")
        w = self.image.width()
        h = self.image.height()
        self.circum_radius = max( w / 2, h / 2 )
        self.angle = 0
        self.VELOCITY = 20
        self.ANGLE_STEP = 5
        self.lives = 3
        self.game = game

    def reset( self ):
        super().reset()
        self.angle = 0
        self.lives = 3

    def hit( self ):
        self.lives -= 1

    def is_alive( self ):
        return self.lives > 0

    def distance_to( self, entity ):
        cx = self.position.x + self.circum_radius
        cy = self.position.y + self.circum_radius
        center = Vector2D( cx, cy )
        return abs( center - entity.position )

    def handleUserInput( self, key_state ):
        if key_state[ Keys.KEY_FIRE ]:
            self.fire()
        #Rotation
        if key_state[ Keys.KEY_ROTATE_CLOCKWISE ]:
            self.angle += self.ANGLE_STEP
            self.angle %= 360
        elif key_state[ Keys.KEY_ROTATE_COUNTERCLOCKWISE ]:
            self.angle -= self.ANGLE_STEP
            self.angle %= 360
        #Translation
        if key_state[ Keys.KEY_MOVE_FORWARD ]:
            self.velocity.x = self.VELOCITY * sin( radians( self.angle ) )
            self.velocity.y = -self.VELOCITY * cos( radians( self.angle ) )
        elif key_state[ Keys.KEY_MOVE_BACKWARD ]:
            self.velocity.x = -self.VELOCITY * sin( radians( self.angle ) )
            self.velocity.y = self.VELOCITY * cos( radians( self.angle ) )
        elif key_state[ Keys.KEY_MOVE_TO_THE_LEFT ]:
            self.velocity.x = -self.VELOCITY * cos( radians( self.angle ) )
            self.velocity.y = -self.VELOCITY * sin( radians( self.angle ) )
        elif key_state[ Keys.KEY_MOVE_TO_THE_RIGHT ]:
            self.velocity.x = self.VELOCITY * cos( radians( self.angle ) )
            self.velocity.y = self.VELOCITY * sin( radians( self.angle ) )
        else:
            self.velocity.x = 0
            self.velocity.y = 0

    def fire( self ):
        angle_rad = radians( self.angle )
        x = self.position.x  + self.image.width() / 2 + 60 * sin( angle_rad )
        y = self.position.y  + self.image.height() / 2  - 60 * cos( angle_rad )
        vx = 20 * sin( angle_rad )
        vy = -20 * cos( angle_rad )
        position = Vector2D( x, y )
        velocity = Vector2D( vx, vy )
        self.game.entities.append( Projectile( self.game, position, velocity, self.angle ) )

    def update( self ):
        next_pos = self.position + self.velocity
        is_out_of_field_bounds = ( next_pos.x + self.circum_radius <= 0 or
         next_pos.x + self.circum_radius >= self.game.field_width or
          next_pos.y + self.circum_radius <= 0 or
          next_pos.y + self.circum_radius >= self.game.field_height )
        if not is_out_of_field_bounds:
            super().update()

    def render( self, painter ):
        painter.save()
        dx = self.position.x + self.image.width() / 2
        dy = self.position.y + self.image.height() / 2
        painter.translate( dx, dy )
        painter.rotate( self.angle )
        w = self.image.width()
        h = self.image.height()
        painter.drawPixmap( QRect(-w / 4, -h / 4, w / 2, h / 2 ), self.image )
        painter.restore()
