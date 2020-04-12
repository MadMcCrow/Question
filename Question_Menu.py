

# Main class for describing a menu
class Menu(object)  :

    _Screen = None
    
    _Question   = 'DefaultQuestion'

    _PossibleAnwsers = ["default anwser 1","default anwser 2" ]

    _MenuSize = 40

    _SelectedIdx = -1


    def addlinecentered(self,text):
        from textwrap import wrap
        if self._Screen is not None:
            for t in wrap(text, self._MenuSize - 2)    :
                self._Screen.addstr("|" + ' ' *int((self._MenuSize - len(text)) /2))
                self._Screen.addstr(t)
                self._Screen.addstr( ' ' * int((self._MenuSize - len(text)) /2) + "|" + '\n')

    # make text look selected
    def _selectedText(self, text)   :
        import curses
        self._Screen.addstr("|" + ' ' * int((self._MenuSize - len(text)) /2))
        self._Screen.addstr(0, 0,text, curses.A_STANDOUT)
        self._Screen.addstr( ' ' * int((self._MenuSize - len(text)) /2) + "|" + '\n')


    # format text to build the window :
    def _format(self)  :
        
        text = "+" + "-" * (self._MenuSize -2 )+ "+" + '\n'
        self.addlinecentered(self._Question)
        self.addlinecentered(" ")
        # the possible answers :
        for idx, anws in enumerate(self._PossibleAnwsers):
            anws = str(idx) + " - " + anws
            if self._SelectedIdx == idx :
                self._selectedText(anws)
            else                        :
                self.addlinecentered(anws)
        # finish the window
        self.addlinecentered(" ")
        self.addlinecentered("select using up and down and press enter")

    def ask(self)  :
        import curses
        from time import sleep

        screen = curses.initscr()
        # let's get the screen update until the user press enter
        while True:
            screen.clear()
            self._format()
            screen.keypad(True)
            screen.refresh()
            while True:   
                k= screen.getch()
                if k== curses.KEY_UP:
                        if self._SelectedIdx - 1 in  range(0, len(self._PossibleAnwsers) -1) :
                            self._SelectedIdx -= 1
                            break
                elif k== curses.KEY_DOWN:
                        if self._SelectedIdx + 1 in  range(0, len(self._PossibleAnwsers) -1) :
                            self._SelectedIdx += 1
                            break

    def __init__(self):
        super().__init__()
        from curses import initscr
        self._Screen = initscr()
