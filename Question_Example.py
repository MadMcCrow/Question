from Question_Prompt    import Prompt
from Question_Menu      import Menu
from Question_Action    import Action



#demo class for a question prompt
class PromptA(Prompt)    :

    def __init__(self):
        super().__init__("La disparition")
        self.addExcludedChars(['e'])
        self.ask()


class PromptB(Prompt)    :

    def __init__(self):
        from os import getcwd
        super().__init__("is it current path ?", str(getcwd()))
        self.ask()

#demo class for a question menu
class MainQuestion(Menu)    :

    finalText = str()

    # you can define actions or use postAskAction to define what to do after selection is made
    class OpenPromptA(Action):
        def do(self):
            PromptA()

    class OpenPromptB(Action):
        def do(self):
            prompt = PromptB()
            MainQuestion.finalText =str("\nof course path was :" + prompt.gatherString() + "\n")

    def __init__(self):
        super().__init__("Example Question")

        AnswerA = Menu.Answer(MainQuestion.OpenPromptA("Write French litterature"))
        AnswerB = Menu.Answer(MainQuestion.OpenPromptB("Check sys is working fine"))
        self.addPossibleAnwser(AnswerA)
        self.addPossibleAnwser(AnswerB)
        self.ask()

    # this another way of implementing the actions
    '''
    def postAskAction(self) :
        if getSelectedIdx() == 0    :
            prompt = PromptB()
            finalText =str("\nof course path was : " + prompt.gatherString() + "\n")
        elif getSelectedIdx() == 1  :
            prompt = PromptA()
            finalText =str("\nyou wrote a possible sentence from Perec : " + prompt.gatherString() + "\n")
        
    '''

# Actual demo 
MainMenu = MainQuestion()
print(MainQuestion.finalText)
print("that's all folks !")

