from PyQt5.QtWidgets import QMainWindow, QFrame, QDesktopWidget, QApplication
from PyQt5.QtCore import*
from PyQt5.QtGui import*
import sys, random

TITLE_OF_PROGRAM = "TePyQtAsteroids"
WINDOW_WIDTH = 600
WINDOW_HEIGHT = 600
TIMER_DELAY = 100

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
        self.timer = QBasicTimer()
        #self.timer.start( TIMER_DELAY, self )

    def keyPressEvent( self, event ):
        pass

    def keyReleaseEvent( self, event ):
        pass

    def paintEvent( self, event ):
        painter = QPainter( self )
        painter.fillRect( 10, 10, 100, 100, Qt.green )

    def timerEvent( self, event ):
        pass

if __name__ == '__main__':
    app = QApplication([])
    window = MainWindow()
    sys.exit(app.exec_())
