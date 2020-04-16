

class BChar()   :
    H     = chr(int("2550",16))
    V     = chr(int("2551",16))
    TL    = chr(int("2554",16))
    TR    = chr(int("2557",16))
    BL    = chr(int("255a",16))
    BR    = chr(int("255d",16))

# Base class for all Question Menu type objects
class QuestionBase(object)  :

    # Exception for when editing the Question when it has already been sent to the user
    class AlreadyStarted(Exception):
        pass

    # Exception for when you have an input that does not make sens in the context.
    # allows you to continue to next input avoiding this input being processed
    class InconclusiveInput(Exception):
        pass
  
    # Exception for when the user validate it's choice
    class OnValidateInput(Exception):
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
    _MenuSize = 50

    # useful method to find if user pressed enter
    @staticmethod
    def _characterIsEnter(char) :
        from curses import KEY_ENTER
        return (char == KEY_ENTER or char == 10 or char == 13)

    # draws the top/Bottom border line 
    def _borderline(self, top = True)       :
        from math       import floor
        from math       import ceil
        if self._Screen is not None:
            L = (BChar.TL if top else BChar.BL) 
            R = (BChar.TR if top else BChar.BR)
            extraspace = (self._MenuSize) /2
            self._Screen.addstr( L + BChar.H * floor(extraspace))
            self._Screen.addstr( BChar.H * floor(extraspace) + R  + '\n')

    # draws an empty line (just the border line on each sides)
    def _addemptyLine(self) :
        from textwrap   import wrap
        from math       import floor
        from math       import ceil
        if self._Screen is not None:
            extraspace = (self._MenuSize) /2
            self._Screen.addstr( BChar.V + ' ' * floor(extraspace))
            self._Screen.addstr( ' ' * ceil(extraspace) +  BChar.V + '\n')

    # draws text line (with the border line on each sides)
    def _addlinecentered(self,text):
        from textwrap   import wrap
        from math       import floor
        from math       import ceil
        if self._Screen is not None:
            for t in wrap(text, self._MenuSize - 2)    :
                extraspace = (self._MenuSize - len(t)) /2
                self._Screen.addstr(BChar.V + ' ' * floor(extraspace))
                self._Screen.addstr(t)
                self._Screen.addstr( ' ' * ceil(extraspace) + BChar.V + '\n')

    # how to display on screen
    def _format(self)  :
        raise NotImplementedError()

    # how to behave on user input.
    def _handleUserInput(self, char)  :
        raise NotImplementedError()

    # how to interpret user pressing Enter/NewLine 
    def _onEnter(self)              :
         raise NotImplementedError()

    # try to get user input
    def _tryInput(self) :
        character = None
        from curses import ungetch
        try: 
            while True:  
                self._Screen.keypad(True)  
                self._Screen.clear()
                self._format()
                self._Screen.refresh()
                character = self._Screen.getch()
                self._handleUserInput(character)      
                if QuestionBase._characterIsEnter(character):
                    raise QuestionBase.OnValidateInput()
            
        except KeyboardInterrupt:
            self.cleanup()
            raise
        except ValueError:
            self.cleanup()
            raise
        except TypeError:
            self.cleanup()
            raise

        except QuestionBase.InconclusiveInput:
            #it's ok the user can be stubborn sometimes
            character = None
            pass

        except NotImplementedError:
            pass
        
        except QuestionBase.OnValidateInput: 
            self._onEnter()
    




    def ask(self)  :
        #let's begin
        self.startup()
        self._tryInput()
        self.cleanup()

    # initial setup
    # initialize curses
    def startup(self)   :
        from curses import initscr
        from curses import noecho
        if self._Screen is None :
            self._Screen = initscr()
            self._Screen.keypad(True)
            noecho()
        self._started = True

    # post ask cleanup
    # ask curses to move back to default
    def cleanup(self)   :
        if self._Screen is not None :
            import curses
            self._Screen.clear()
            self._Screen = None 
            curses.echo()
            curses.endwin()
            
        self._started = False

    #create object with title 
    def __init__(self, Question)  :
        ''' somehow  super didn't worked ...'''
        object.__init__(self)
        self._QuestionTitle = Question


