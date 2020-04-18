from Question_Base import QuestionBase
from Question_Base import BChar


# Main class for describing a menu
class Menu(QuestionBase)  :
            

    _PossibleAnwsers = []
    _SelectedIdx = -1

    def isValidChoice(self) :
        available_range  = range(0, len(self._PossibleAnwsers)-1)
        return self._SelectedIdx in available_range 

    # get the selected idx , in the range of possible answers
    def getChoiceIdx(self)    :
        return self._SelectedIdx

    # get the answer at selected idx
    def getChoiceAnswer(self) :
        try :
            return self._PossibleAnwsers[self.getChoiceIdx()]
        except IndexError  :
            return "IndexError :No Valid Answer selected"

    # get the text to display for answer idx
    def _getAnswerText(self, idx)   :
        return self._PossibleAnwsers[idx].getstr()
            
    # Set the anwsers 
    def setAvailableAnswers(self, listAnswers)  :
        if isinstance(listAnswers,list)   :
            self._PossibleAnwsers = listAnswers
  
    # make text look selected
    def _selectedText(self, text)   :
        from textwrap   import wrap
        from curses     import A_STANDOUT
        from math       import floor
        from math       import ceil
        if self._Screen is not None:
            for t in QuestionBase.textwrapper(text, self._MenuSize - 2)    :
                extraspace = (self._MenuSize - len(t)) /2
                self._Screen.addstr(BChar.V + ' ' * floor(extraspace))
                self._Screen.addstr(t, A_STANDOUT)
                self._Screen.addstr( ' ' * ceil(extraspace) + BChar.V + '\n')
     

    # format text to build the window :
    def format(self)  :
        self._borderline(top = True)
        self._addlinecentered(self.getTitleStr())
        self._addemptyLine()
        # the possible answers :
        for idx, anws in enumerate(self._PossibleAnwsers):
            anws = str(idx) + " - " + str(anws)
            if self._SelectedIdx == idx :
                self._selectedText(anws)
            else                        :
                self._addlinecentered(anws)
        # finish the window
        self._addemptyLine()
        self._addemptyLine()
        self._addlinecentered("select using up and down and press enter")
        self._borderline(top = False)



    # this is the important function
    def handleUserInput(self, char)  :
        from curses import KEY_UP
        from curses import KEY_DOWN
        range_possible = range(0, len(self._PossibleAnwsers) )
         # let's get the screen update until the user press enter
        if char == KEY_UP:
            if self._SelectedIdx - 1 in range_possible :
                self._SelectedIdx -= 1
        elif char == KEY_DOWN:
            if self._SelectedIdx + 1 in range_possible :
                self._SelectedIdx += 1
        else  :
            raise QuestionBase.InconclusiveInput()
    

    def _onEnter(self)  :
        if not self.isValidChoice():
            raise IndexError
        


    def cleanup(self) :
        QuestionBase.cleanup(self)
        

