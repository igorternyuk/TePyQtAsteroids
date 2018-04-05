from math import*

class Vector2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def scale( self, scale ):
        self.x *= scale
        self.y *= scale
        return self

    def magnitude( self ):
        return sqrt( pow( self.x, 2 ) + pow( self.y, 2 ))

    def __abs__( self ):
        return self.magnitude()

    def __add__( self, other ):
        return Vector2D( self.x + other.x, self.y + other.y )

    def __sub__( self, other ):
        return Vector2D( self.x - other.x, self.y - other.y )

    def __iadd__( self, other ):
        self.x += other.x
        self.y += other.y
        return self

    def __isub__( self, other ):
        self.x -= other.x
        self.y -= other.y
        return self

    def __mul__( self, other ):
        return self.x * other.x + self.y * other.y

    def __eq__( self, other ):
        return self.x == other.x and self.y == other.y

    def __ne__( self, other ):
        return self.x != other.x and self.y != other.y

    def __str__( self ):
        return "(%8.3e, %8.3e)" % ( self.x, self.y )
