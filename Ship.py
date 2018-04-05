from PyQt5.QtCore import QRect
from PyQt5.QtGui import QPixmap
from math import*
from Entity import*
from Vector2D import*
from Game import*
from KeyState import*

class Ship( Entity ):
    def __init__( self, game, position, velocity = Vector2D( 0, 0) ):
        super().__init__( position, velocity )
        self.game = game
        self.image = QPixmap("spaceship.png")
        self.angle = 0

    def handleUserInput( self, key_state ):
        #Rotation
        if key_state[ Keys.KEY_ROTATE_CLOCKWISE ]:
            self.angle += 2
            self.angle %= 360
            print( self.angle )
        elif key_state[ Keys.KEY_ROTATE_COUNTERCLOCKWISE ]:
            self.angle -= 2
            self.angle %= 360
            print( self.angle )

        if key_state[ Keys.KEY_MOVE_FORWARD ]:
            self.velocity.x = 20 * sin( radians( self.angle ) )
            self.velocity.y = -20 * cos( radians( self.angle ) )
            print( self.angle )
        elif key_state[ Keys.KEY_MOVE_BACKWARD ]:
            self.velocity.x = -20 * sin( radians( self.angle ) )
            self.velocity.y = 20 * cos( radians( self.angle ) )
            print( self.angle )
        else:
            self.velocity.x = 0
            self.velocity.y = 0

    def update( self ):
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
