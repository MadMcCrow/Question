from Question_Base import QuestionBase
from Question_Base import BChar

# Main class for describing a prompt for text
class Prompt(QuestionBase)  :

    # reference to the curses textpad for input
    _Textpad = None

    # Obtained string from user
    _UserString = str()

    # how much can we print
    _InputSize = QuestionBase._MenuSize -2


    # Where are we in the input text
    _CursorPosition = 0
    
    # unwanted characters as anwser :
    _ExcludedCharacters = ['^j']


    def gatherString(self)  :
        return self._UserString

    # make text look selected
    def _addInputText(self)   :
        from curses     import A_BLINK
        from curses     import A_UNDERLINE
        from math       import floor
        from math       import ceil
        if self._Screen is not None:
                text = self._UserString
                begin = max(self._CursorPosition - self._InputSize, 0)
                end = begin + self._InputSize
                substring = text[begin:end]
                rel_cursor_position =  self._CursorPosition - begin
                extraspace =(self._MenuSize - min(self._InputSize, self._MenuSize -2) )/ 2
                self._Screen.addstr(BChar.V + ' ' * floor(extraspace))
                for idx in range(0, self._InputSize)    :
                    try:
                        self._Screen.addstr(substring[idx],(A_BLINK if idx == rel_cursor_position else A_UNDERLINE))
                    except IndexError:
                        self._Screen.addstr(" ", A_BLINK if idx == rel_cursor_position else A_UNDERLINE)
                        pass                    
                self._Screen.addstr( ' ' * ceil(extraspace) + BChar.V + '\n')
 
    # add a list of characters to the unwanted characters
    def addExcludedChars(self, chars = list())   :
        try:
            for c in chars  :
                if c not in self._ExcludedCharacters    :
                    self._ExcludedCharacters.append(c)
        except ValueError:
            pass

    # how to display on screen
    def _format(self)  :
            self._borderline(top = True)
            self._addlinecentered(self.getTitleStr())
            self._addemptyLine()
            self._addInputText()
            self._addemptyLine()
            self._addemptyLine()
            self._addlinecentered("Enter text: (hit enter to send)")
            self._borderline(top = False)


    # how to behave on user input (except enter it's reserved)
    def _handleUserInput(self, char)  :
            from curses import KEY_LEFT
            from curses import KEY_RIGHT
            from curses import KEY_BACKSPACE
            from curses import KEY_DC
            from curses import ascii
            range_possible = range(0, len(self._UserString) + 1 )
            if char == KEY_LEFT:
                if self._CursorPosition - 1 in range_possible :
                    self._CursorPosition -= 1
            elif char == KEY_RIGHT:
                if self._CursorPosition + 1 in range_possible :
                    self._CursorPosition += 1
            elif char == KEY_BACKSPACE:
                if self._CursorPosition - 1 in range_possible :
                    self._UserString = self._UserString[:self._CursorPosition - 1] + self._UserString[self._CursorPosition:] 
                    self._CursorPosition -= 1
            elif char == KEY_DC:
                if self._CursorPosition + 1 in range_possible :
                    self._UserString = self._UserString[:self._CursorPosition ] + self._UserString[self._CursorPosition+1:] 
            elif ascii.isprint(char)    and chr(char) not in self._ExcludedCharacters:
                self._UserString = self._UserString[:self._CursorPosition] + chr(char) + self._UserString[self._CursorPosition:] 
                self._CursorPosition += 1
            else :
                raise QuestionBase.InconclusiveInput()
        
    # how to interpret user pressing Enter/NewLine 
    def _onEnter(self)  :
        try:
            print(gatherString())
        except (RuntimeError, TypeError, NameError):
            print("ERROR")
            pass


    def __init__(self, Question)  :
        QuestionBase.__init__(self,Question)
        self._InputSize = self._MenuSize -2
        self._CursorPosition = len(self._UserString)

    