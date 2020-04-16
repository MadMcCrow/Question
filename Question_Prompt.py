from Question_Base import QuestionBase

# Main class for describing a prompt for text
class Prompt(QuestionBase)  :

    # reference to the curses textpad for input
    _Textpad = None

    # Obtained string from user
    _UserString = str()

    # unwanted characters as anwser :
    _ExcludedCharacters = ['^j']


    def gatherString(self)  :
        return self._UserString

    # add a list of characters to the unwanted characters
    def AddExcludedChars(self, chars = list())   :
        try:
            for c in chars  :
                if c not in self._ExcludedCharacters    :
                    self._ExcludedCharacters.append(c)
        except ValueError:
            pass

    # how to display on screen
    def _format(self)  :
            from curses import textpad
            self._borderline()
            self._addlinecentered(self.getTitleStr())
            self._addemptyLine()
            # will add the text box there
            textpad.rectangle(self._Screen, 3, 2, 3+1, self._MenuSize -(2 + 2))
            # finish the window
            self._addemptyLine()
            self._addemptyLine()
            self._addlinecentered("Enter text: (hit Ctrl-G to send)")
            self._borderline()


    # how to behave on user input (except enter it's reserved)
    def _handleUserInput(self)  :
        return -1
    # how to interpret user pressing Enter/NewLine 
    def _onEnter(self)              :
        return -1


    def ask(self)  :
        #let's begin
        self.startup()
        self._SelectedIdx = -1
        self._Textpad.edit()
        self._UserString = self._Textpad.gather()
        self.cleanup()
    