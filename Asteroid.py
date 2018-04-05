from Entity import*
from PyQt5.QtCore import*
from PyQt5.QtGui import*
from math import*

class Asteroid( Entity ):
    def __init__(self, game, position, velocity, radius = 20, edge_number = 5,
     angle = 0 ):
        super().__init__( position, velocity )
        self.game = game
        self.radius = radius
        self.edge_number = edge_number
        self.angle = angle
        self.pen = QPen( QColor( 255, 255, 0 ) )                      # set lineColor
        self.pen.setWidth(2)                                            # set lineWidth
        self.brush = QBrush( QColor( 255, 156, 0 ) )

    def update( self ):
        super().update()
        self.__hold_position_within_screen_bounds_()
        self.angle += 5
        self.angle %= 360

    def __hold_position_within_screen_bounds_( self ):
        if self.position.x + self.radius <= 0:
            self.position.x += self.game.field_width
        elif self.position.x - self.radius >= self.game.field_width:
            self.position.x -= self.game.field_width
        if self.position.y + self.radius <= 0:
            self.position.y += self.game.field_height
        elif self.position.y - self.radius >= self.game.field_height:
            self.position.y -= self.game.field_height

    def render( self, painter ):
        polygon = self.__create_polygon_( self.position, self.radius,
         self.edge_number, self.angle )
        painter.setPen(self.pen)
        painter.setBrush(self.brush)
        painter.drawPolygon( polygon )

    def __create_polygon_( self, position, radius, edge_number, angle):
        polygon = QPolygonF()
        if edge_number <= 2:
            edge_number = 3
        step = 360.0 / edge_number
        for i in range( edge_number ):
            alpha = angle + i * step
            x = position.x + radius * cos( radians( alpha ) )
            y = position.y + radius * sin( radians( alpha ) )
            polygon.append( QPointF( x, y ) )
        return polygon

"""
class MyWidget(QtWidgets.QWidget):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.pen = QtGui.QPen(QtGui.QColor(0,0,0))                      # set lineColor
        self.pen.setWidth(3)                                            # set lineWidth
        self.brush = QtGui.QBrush(QtGui.QColor(255,255,255,255))        # set fillColor
        self.polygon = self.createPoly(8,150,0)                         # polygon with n points, radius, angle of the first point

    def createPoly(self, n, r, s):
        polygon = QtGui.QPolygonF()
        w = 360/n                                                       # angle per step
        for i in range(n):                                              # add the points of polygon
            t = w*i + s
            x = r*math.cos(math.radians(t))
            y = r*math.sin(math.radians(t))
            polygon.append(QtCore.QPointF(self.width()/2 +x, self.height()/2 + y))

        return polygon

    def paintEvent(self, event):
        painter = QtGui.QPainter(self)
        painter.setPen(self.pen)
        painter.setBrush(self.brush)
        painter.drawPolygon(self.polygon)
"""
