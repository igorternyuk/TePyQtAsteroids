from Vector2D import*
from math import*

class Entity:
    def __init__( self, position, velocity ):
        self.position = position
        self.velocity = velocity
        self.alive = True

    def distance_to( self, other ):
        return ( self.position - other.position ).magnitude()

    def is_alive( self ):
        return self.alive

    def update( self ):
        self.position += self.velocity

    def render( self, painter ):
        pass
