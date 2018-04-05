from Vector2D import*
from math import*

class Entity:
    def __init__( self, position, velocity ):
        self.position = position
        print("Entity pos = ", (self.position) )
        self.velocity = velocity

    def distance_to( self, other ):
        return ( self.position - other.position ).magnitude()

    def update( self ):
        self.position += self.velocity

    def render( self, painter ):
        pass
