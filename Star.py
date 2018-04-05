from Entity import*
from PyQt5.QtCore import*
from PyQt5.QtGui import*

class Star( Entity ):
    def __init__( self, game, position, velocity ):
        super().__init__( position, velocity )
        self.game = game
        self.color = QColor( 255, 233, 127, 100 )
        self.pen = QPen( self.color )                      # set lineColor
        self.pen.setWidth(2)                                            # set lineWidth
        self.brush = QBrush( QColor( self.color ) )
        self.RADIUS = 0.5

    def update( self ):
        super().update()
        self.__keep_star_within_field_bounds_()

    def __keep_star_within_field_bounds_( self ):
        if self.position.x + self.RADIUS <= 0:
            self.position.x += self.game.field_width
        elif self.position.x - self.RADIUS >= self.game.field_width:
            self.position.x -= self.game.field_width
        if self.position.y + self.RADIUS <= 0:
            self.position.y += self.game.field_height
        elif self.position.y - self.RADIUS >= self.game.field_height:
            self.position.y -= self.game.field_height

    def render( self, painter ):
        painter.setPen(self.pen)
        painter.setBrush( self.brush )
        painter.drawEllipse( QPointF( self.position.x, self.position.y ),
         self.RADIUS, self.RADIUS )
