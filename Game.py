from Ship import*
from Asteroid import*
from Star import*
from Projectile import*
from KeyState import*

class Game:
    def __init__( self, window_width, window_height ):
        self.window_width = window_width
        self.window_height = window_height
        self.ship = Ship( self, Vector2D( self.window_width / 2, self.window_height / 2 ) )

    def reset( self ):
        pass

    def user_input_phase( self, key_state ):
        self.ship.handleUserInput( key_state )

    def update_phase( self ):
        self.ship.update()

    def render_phase( self, painter ):
        self.ship.render( painter )
