from enum import Enum

class Keys( Enum ):
    KEY_MOVE_FORWARD = 1
    KEY_MOVE_BACKWARD = 2
    KEY_ROTATE_CLOCKWISE = 3
    KEY_ROTATE_COUNTERCLOCKWISE = 4
    KEY_FIRE = 5

class KeyState:
    def __init_( self ):
        self.__keys = {}

    def get( self, key ):
        return self.__keys[key]

    def set( self, key ):
        self.__keys[key] = True

    def reset( self, key ):
        self.__keys[key] = False
