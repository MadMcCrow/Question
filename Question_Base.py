


# Base class for all Question Menu type objects
class QuestionBase(object)  :

    # Exception for when editing the Question when it has already been sent to the user
    class AlreadyStarted(Exception):
        pass

    # Base title of the Question
    _QuestionTitle   = 'DefaultQuestion'

    # Method to get title
    def getTitleStr(self)   :
        return self._QuestionTitle

    # whether this Menu as started prompting the user
    _started = False

    # reference to the curse screen
    _Screen = None

    # size of the menu (width)
    _MenuSize = 40

    # useful method to find if user pressed enter
    @staticmethod
    def _characterIsEnter(char) :
        from curses import KEY_ENTER
        return (char == KEY_ENTER or char == 10 or char == 13)

    # draws the top/Bottom border line 
    def _borderline(self)       :
        from math       import floor
        from math       import ceil
        if self._Screen is not None:
            extraspace = (self._MenuSize) /2
            self._Screen.addstr("+" + '-' * floor(extraspace))
            self._Screen.addstr( '-' * ceil(extraspace) + "+" + '\n')

    # draws an empty line (just the border line on each sides)
    def _addemptyLine(self) :
        from textwrap   import wrap
        from math       import floor
        from math       import ceil
        if self._Screen is not None:
            extraspace = (self._MenuSize) /2
            self._Screen.addstr("|" + ' ' * floor(extraspace))
            self._Screen.addstr( ' ' * ceil(extraspace) + "|" + '\n')


    # draws text line (with the border line on each sides)
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

    # how to display on screen
    def _format(self)  :
        raise NotImplementedError()

    # how to behave on user input (except enter it's reserved)
    def _handleUserInput(self)  :
        raise NotImplementedError()
        # should always return the value of the input 
        # return -1

    # how to interpret user pressing Enter/NewLine 
    def _onEnter(self)              :
         raise NotImplementedError()

    def _checkEnter(self, character) :
        if QuestionBase._characterIsEnter(character)    :
            # self._onEnter() // we  could also put it here 
            return True
        else    :
            return False


    def ask(self)  :
        #let's begin
        self.startup()
        self._SelectedIdx = -1
        while True:
            char = self._handleUserInput()
            if self._checkEnter(char)    :
                self._onEnter()
                break
        self.cleanup()

    # initial setup
    # initialize curses
    def startup(self)   :
        from curses import initscr
        from curses import noecho
        if self._Screen is None :
            self._Screen = initscr()
            noecho()
        self._started = True

    # post ask cleanup
    # ask curses to move back to default
    def cleanup(self)   :
        if self._Screen is not None :
            import curses
            self._Screen.clear()
            curses.nocbreak()
            curses.echo()
            curses.endwin()
        self._started = False

    #create object with title 
    def __init__(self, Question)  :
        super.__init__()
        self._QuestionTitle = Question


