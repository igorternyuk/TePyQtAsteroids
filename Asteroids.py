from PyQt5.QtWidgets import QMainWindow, QFrame, QDesktopWidget, QApplication
from PyQt5.QtCore import*
from PyQt5.QtGui import*
import sys, random
from KeyState import*
from Game import*

TITLE_OF_PROGRAM = "TePyQtAsteroids"
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 700
TIMER_DELAY = 34

class MainWindow( QMainWindow ):
    def __init__( self ):
        super().__init__()
        self.init_UI()

    def init_UI( self ):
        self.canvas = Canvas( self )
        self.setCentralWidget( self.canvas )
        self.setWindowTitle( TITLE_OF_PROGRAM )
        self.setFixedSize( WINDOW_WIDTH, WINDOW_HEIGHT )
        self.move_to_the_screen_center()
        self.show()

    def move_to_the_screen_center( self ):
        screenRect = QDesktopWidget().screenGeometry()
        windowRect = self.geometry()
        dx = ( screenRect.width() - windowRect.width() ) / 2
        dy = ( screenRect.height() - windowRect.height() ) / 2
        self.move( dx, dy )

class Canvas( QFrame ):
    def __init__( self, parent = None ):
        super().__init__( parent )
        self.setFocusPolicy( Qt.StrongFocus )
        self.key_state = {}
        self.reset_keys()
        self.game = Game( WINDOW_WIDTH, WINDOW_HEIGHT )
        self.timer = QBasicTimer()
        self.timer.start( TIMER_DELAY, self )

    def reset_keys( self ):
        self.key_state[ Keys.KEY_MOVE_FORWARD ] = False
        self.key_state[ Keys.KEY_MOVE_BACKWARD ] = False
        self.key_state[ Keys.KEY_MOVE_TO_THE_LEFT ] = False
        self.key_state[ Keys.KEY_MOVE_TO_THE_RIGHT ] = False
        self.key_state[ Keys.KEY_ROTATE_CLOCKWISE ] = False
        self.key_state[ Keys.KEY_ROTATE_COUNTERCLOCKWISE ] = False
        self.key_state[ Keys.KEY_FIRE ] = False

    def keyPressEvent( self, event ):
        key = event.key()
        if key == Qt.Key_A or key == Qt.Key_Left:
            self.key_state[ Keys.KEY_MOVE_TO_THE_LEFT ] = True
        elif key == Qt.Key_D or key == Qt.Key_Right:
            self.key_state[ Keys.KEY_MOVE_TO_THE_RIGHT ] = True
        elif key == Qt.Key_W:
            self.key_state[ Keys.KEY_MOVE_FORWARD ] = True
        elif key == Qt.Key_S:
            self.key_state[ Keys.KEY_MOVE_BACKWARD ] = True
        elif key == Qt.Key_Up:
            self.key_state[ Keys.KEY_ROTATE_COUNTERCLOCKWISE ] = True
        elif key == Qt.Key_Down:
            self.key_state[ Keys.KEY_ROTATE_CLOCKWISE ] = True
        elif key == Qt.Key_F:
            self.key_state[ Keys.KEY_FIRE ] = True

    def keyReleaseEvent( self, event ):
        key = event.key()
        if key == Qt.Key_N:
            self.game.reset()
        elif key == Qt.Key_Space:
            if self.timer.isActive():
                self.timer.stop()
            else:
                self.timer.start( TIMER_DELAY, self )
        if key == Qt.Key_A or key == Qt.Key_Left:
            self.key_state[ Keys.KEY_MOVE_TO_THE_LEFT ] = False
        elif key == Qt.Key_D or key == Qt.Key_Right:
            self.key_state[ Keys.KEY_MOVE_TO_THE_RIGHT ] = False
        elif key == Qt.Key_W:
            self.key_state[ Keys.KEY_MOVE_FORWARD ] = False
        elif key == Qt.Key_S:
            self.key_state[ Keys.KEY_MOVE_BACKWARD ] = False
        elif key == Qt.Key_Up:
            self.key_state[ Keys.KEY_ROTATE_COUNTERCLOCKWISE ] = False
        elif key == Qt.Key_Down:
            self.key_state[ Keys.KEY_ROTATE_CLOCKWISE ] = False
        elif key == Qt.Key_F:
            self.key_state[ Keys.KEY_FIRE ] = False

    def paintEvent( self, event ):
        painter = QPainter( self )
        self.game.render_phase( painter )

    def timerEvent( self, event ):
        if event.timerId() == self.timer.timerId():
            self.game.user_input_phase( self.key_state )
            self.game.update_phase()
            self.update()

if __name__ == '__main__':
    app = QApplication([])
    window = MainWindow()
    sys.exit(app.exec_())
