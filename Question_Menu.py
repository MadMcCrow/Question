from Question_Base import QuestionBase

# Main class for describing a menu
class Menu(QuestionBase)  :

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
            


    _PossibleAnwsers = list()

    _SelectedIdx = -1

    def _getAnswerText(self, idx)   :
        return self._PossibleAnwsers[idx].getstr()

    def _execAnswerAction(self, idx)   :
        return self._PossibleAnwsers[idx].DoAction()

    def addPossibleAnwser(self,  text, action)   :
        if self._started is True :
            raise Menu.AlreadyStarted("the Menu is already on screen adding on the fly is not supported") 
        else    :
            try :
                self._PossibleAnwsers.append(Menu.Answer(text, action))
            except (RuntimeError, TypeError, NameError):
                self._PossibleAnwsers.append(Menu.Answer("Error ", None))
          

    # format text to build the window :
    def _format(self)  :
        
        self._borderline()
        self._addlinecentered(self.getTitleStr())
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



    def _handleUserInput(self)  :
        from curses import KEY_UP
        from curses import KEY_DOWN
        range_possible = range(0, len(self._PossibleAnwsers) )
         # let's get the screen update until the user press enter
        self._Screen.clear()
        self._format()
        self._Screen.keypad(True)
        self._Screen.refresh() 
        k = self._Screen.getch()
        if k == KEY_UP:
            if self._SelectedIdx - 1 in range_possible :
                self._SelectedIdx -= 1
        elif k == KEY_DOWN:
            if self._SelectedIdx + 1 in range_possible :
                self._SelectedIdx += 1
        return k

    def _onEnter(self)  :
        try:
           _execAnswerAction(_SelectedIdx)
        except (RuntimeError, TypeError, NameError):
            print("ERROR")
            pass
        finally:
            self._Screen.keypad(False)  
