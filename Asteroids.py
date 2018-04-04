from PyQt5.QtWidgets import QMainWindow, QFrame, QDesktopWidget, QApplication
from PyQt5.QtCore import*
from PyQt5.QtGui import*
import sys, random
from KeyState import*
from Game import*

TITLE_OF_PROGRAM = "TePyQtAsteroids"
WINDOW_WIDTH = 600
WINDOW_HEIGHT = 600
TIMER_DELAY = 100

class MainWindow( QMainWindow ):
    def __init__( self ):
        super().__init__()
        self.init_UI()

    def init_UI( self ):
        self.key_state = KeyState()
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
        self.game = Game( WINDOW_WIDTH, WINDOW_HEIGHT )
        self.timer = QBasicTimer()
        self.timer.start( TIMER_DELAY, self )

    def keyPressEvent( self, event ):
        key = event.key()
        if key == Qt.Key_Left:
            self.parent().key_state.set( Keys.KEY_ROTATE_COUNTERCLOCKWISE )
        elif key == Qt.Key_Right:
            self.parent().key_state.set( Keys.KEY_ROTATE_CLOCKWISE )
        elif key == Qt.Key_Up:
            self.parent().key_state.set( Keys.KEY_MOVE_FORWARD )
        elif key == Qt.Key_Down:
            self.parent().key_state.set( Keys.KEY_MOVE_BACKWARD )
        elif key == Qt.Key_F:
            self.parent().key_state.set( Keys.KEY_FIRE )

    def keyReleaseEvent( self, event ):
        key = event.key()
        if key == Qt.Key_Left:
            self.parent().key_state.reset( Keys.KEY_ROTATE_COUNTERCLOCKWISE )
        elif key == Qt.Key_Right:
            self.parent().key_state.reset( Keys.KEY_ROTATE_CLOCKWISE )
        elif key == Qt.Key_Up:
            self.parent().key_state.reset( Keys.KEY_MOVE_FORWARD )
        elif key == Qt.Key_Down:
            self.parent().key_state.reset( Keys.KEY_MOVE_BACKWARD )
        elif key == Qt.Key_F:
            self.parent().key_state.reset( Keys.KEY_FIRE )

    def paintEvent( self, event ):
        painter = QPainter( self )
        self.game.render_phase( painter )

    def timerEvent( self, event ):
        if event.timerId() == self.timer.timerId():
            self.game.user_input_phase( self.parent().key_state )
            self.game.update()
            self.update()

if __name__ == '__main__':
    app = QApplication([])
    window = MainWindow()
    sys.exit(app.exec_())
