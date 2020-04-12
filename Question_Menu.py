

# Main class for describing a menu
class Menu(object)  :

    
    _Question   = 'DefaultQuestion'

    _PossibleAnwsers = ["default anwser 1","default anwser 2" ]

    _MenuSize = 40

    # make text look selected
    def _selected(self, text)   :
        return '\x1b[0;30;47m' + text + '\x1b[0m'

    # format text to build the window :
    def _format(self, selected = -1)  :
        from textwrap import wrap
        text = "+" + "-" * self._MenuSize + "+" + '\n'
        for quest in wrap(self._Question, self._MenuSize - 2)    :
             text += "|" + quest.center(self._MenuSize,' ') + "|"  +'\n'
        text += "|" + str("|").rjust(self._MenuSize + 1) + '\n'
        # the possible answers :
        for idx, anws in enumerate(self._PossibleAnwsers):
            anws = str(idx) + " - " + anws
            for t in wrap(anws, self._MenuSize - 2)    :
                if selected in range(0, len(self._PossibleAnwsers) -1)  :
                    text += "|" + self._selected(t).center(self._MenuSize,' ') + "|"  +'\n'
                else                                                    :
                    text += "|" + t.center(self._MenuSize,' ') + "|"  +'\n'
        # finish the window
        text += "|" + str("|").rjust(self._MenuSize + 1) + '\n'
        text += "|" + "select using up and down and press enter" + "|"  +'\n'
        text += "+" + "-" * self._MenuSize + "+" + '\n'
        return text

    @staticmethod
    def _Getch():
        import sys,tty,termios    
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(sys.stdin.fileno())
            ch = sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        return ch

    def ask(self)  :
        from curses import initscr
        from time import sleep

        screen = initscr()
        screen.clear()
        screen.addstr(0, 0, self._format())
        screen.keypad(True)
        screen.refresh()
        while(1):
            k= Menu._Getch()
            if k=='\x1b[A':
                    print("up")
            elif k=='\x1b[B':
                    print("down")
            elif k=='\x1b[C':
                    print("right")
            elif k=='\x1b[D':
                    print("left")
            else:
                    print(k + " is not an arrow key!")

    def __init__(self):
        super().__init__()
