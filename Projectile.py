from Entity import*
from PyQt5.QtCore import*
from PyQt5.QtGui import*
from math import*

class Projectile( Entity ):
    def __init__( self, game, position, velocity, angle ):
        super().__init__( position, velocity )
        self.game = game
        self.angle = angle
        self.width = 1
        self.height = 15
        self.COLOR = QColor( 255, 0, 0 )

    def update( self ):
        super().update()
        if ( self.position.x <= 0 or self.position.x > self.game.field_width or self.position.y <= 0 or self.position.y > self.game.field_height ):
            print("Removing projectile")
            self.alive = False
            print("self.alive = ", self.is_alive() )

    def render( self, painter ):
        painter.save()
        painter.translate( self.position.x + self.width / 2, self.position.y + self.height / 2 )
        painter.rotate( self.angle )
        painter.setBrush( self.COLOR )
        painter.fillRect( QRectF( -self.width / 2, self.height / 2, self.width,
         self.height ), self.COLOR )
        painter.restore()
