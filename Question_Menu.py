

# Main class for describing a menu
class Menu(object)  :

    class Answer(object)    :
        
        _Text = "DEFAULT ANSWER TEXT"

        _Action = None

        def __init__(self, text, action = None):
            super().__init__()
            self._Text   = text
            self._Action = action

        def getstr(self)    :
            return self._Text

        def __str__(self)   :
            return self.getstr()

        def DoAction(self)    :
            try:
                self._Action.Do()
            # ignore error based on bad actions : we're not supposed to know your action is meant to not work
            except (RuntimeError, TypeError, NameError):
                return False
            # if we could call Do it's ok
            finally :
                return True
            



    _Screen = None
    
    _Question   = 'DefaultQuestion'

    _PossibleAnwsers = [Answer("default anwser 1"),Answer("default anwser 2") ]

    _MenuSize = 40

    _SelectedIdx = -1

    @staticmethod
    def _characterIsEnter(char) :
        from curses import KEY_ENTER
        return (char == KEY_ENTER or char == 10 or char == 13)

    def _getAnswerText(self, idx)   :
        return self._PossibleAnwsers[idx].getstr()

    def _execAnswerAction(self, idx)   :
        return self._PossibleAnwsers[idx].DoAction()


    def _borderline(self)       :
        from math       import floor
        from math       import ceil
        if self._Screen is not None:
            extraspace = (self._MenuSize) /2
            self._Screen.addstr("+" + '-' * floor(extraspace))
            self._Screen.addstr( '-' * ceil(extraspace) + "+" + '\n')

    def _addemptyLine(self) :
        from textwrap   import wrap
        from math       import floor
        from math       import ceil
        if self._Screen is not None:
            extraspace = (self._MenuSize) /2
            self._Screen.addstr("|" + ' ' * floor(extraspace))
            self._Screen.addstr( ' ' * ceil(extraspace) + "|" + '\n')


    # add line centered
    def _addlinecentered(self,text):
        from textwrap   import wrap
        from math       import floor
        from math       import ceil
        if self._Screen is not None:
            for t in wrap(text, self._MenuSize - 2)    :
                extraspace = (self._MenuSize - len(t)) /2
                self._Screen.addstr("|" + ' ' * floor(extraspace))
                self._Screen.addstr(t)
                self._Screen.addstr( ' ' * ceil(extraspace) + "|" + '\n')

    # make text look selected
    def _selectedText(self, text)   :
        from textwrap   import wrap
        from curses     import A_STANDOUT
        from math       import floor
        from math       import ceil
        if self._Screen is not None:
            for t in wrap(text, self._MenuSize - 2)    :
                extraspace = (self._MenuSize - len(t)) /2
                self._Screen.addstr("|" + ' ' * floor(extraspace))
                self._Screen.addstr(t, A_STANDOUT)
                self._Screen.addstr( ' ' * ceil(extraspace) + "|" + '\n')


    # format text to build the window :
    def _format(self)  :
        
        self._borderline()
        self._addlinecentered(self._Question)
        self._addemptyLine()
        # the possible answers :
        for idx, anws in enumerate(self._PossibleAnwsers):
            anws = str(idx) + " - " + anws.getstr()
            if self._SelectedIdx == idx :
                self._selectedText(anws)
            else                        :
                self._addlinecentered(anws)
        # finish the window
        self._addemptyLine()
        self._addemptyLine()
        self._addlinecentered("select using up and down and press enter")
        self._borderline()

    def ask(self)  :
        #let's begin
        self.Startup()


        import curses
        from time import sleep
        self._SelectedIdx = -1
        range_possible = range(0, len(self._PossibleAnwsers) )

        k = 0
        # let's get the screen update until the user press enter
        while not (self._characterIsEnter(k) and self._SelectedIdx in range_possible) :  
            self._Screen.clear()
            self._format()
            self._Screen.keypad(True)
            self._Screen.refresh() 
            k= self._Screen.getch()
            if k == curses.KEY_UP:
                if self._SelectedIdx - 1 in range_possible :
                    self._SelectedIdx -= 1
                    continue
            elif k == curses.KEY_DOWN:
                if self._SelectedIdx + 1 in range_possible :
                    self._SelectedIdx += 1
                    continue     
        
        # handle enter action
        try:
           _execAnswerAction(_SelectedIdx)
        except (RuntimeError, TypeError, NameError):
            print("ERROR")
            pass
        finally:
            self._Screen.keypad(False)
        

        # Cleanup after we've asked
        self.Cleanup()
            

        



    def __init__(self):
        super().__init__()



    def Startup(self)   :
        from curses import initscr
        from curses import noecho
        if self._Screen is None :
            self._Screen = initscr()
            noecho()

    def Cleanup(self)   :
        if self._Screen is not None :
            import curses
            self._Screen.clear()
            curses.nocbreak()
            curses.echo()
            curses.endwin()

