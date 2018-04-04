from math import*

class Vector2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def add( self, dx, dy ):
        self.x += dx
        self.y += dy

    def addOther( self, other ):
        self.x += other.x
        self.y += other.y

    def multiply( self, scale ):
        self.x *= scale
        self.y *= scale

    def magnitude( self ):
        return sqrt( pow( self.x, 2 ) + pow( self.y, 2 ))

    def __str__( self ):
        return "(%8.3e, %8.3e)" % ( self.x, self.y )

vec = Vector2D( 3, 4 )
print( vec )
vec.add( 3, 4 )
print( vec )
print( vec.magnitude() )
vec2 = Vector2D( -3, -4 )
vec.addOther( vec2 )
print( vec )
