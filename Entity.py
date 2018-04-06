from Vector2D import*
from math import*
import copy

class Entity:
    def __init__( self, position, velocity ):
        self.position = position
        self.init_position = copy.deepcopy( position )
        self.velocity = velocity
        self.init_velocity = copy.deepcopy( velocity )
        self.alive = True

    def reset( self ):
        self.position = copy.deepcopy( self.init_position )
        self.velocity = copy.deepcopy( self.init_velocity )

    def distance_to( self, other ):
        return ( self.position - other.position ).magnitude()

    def is_alive( self ):
        return self.alive

    def update( self ):
        self.position += self.velocity

    def render( self, painter ):
        pass
