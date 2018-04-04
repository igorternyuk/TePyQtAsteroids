class Entity:
    def __init__( self, position, velocity ):
        self.position = position
        self.velocity = velocity

    def update( self ):
        self.position.addWidget( self.velocity )

    def render( self, painter ):
        pass
