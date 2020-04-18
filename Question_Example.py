from Question_Prompt    import Prompt
from Question_Menu      import Menu

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

    def __init__(self):
        super().__init__("Example Question")
        answerA = "Write French litterature"
        answerB = "Check sys is working fine" 
        self.setAvailableAnswers([answerA,answerB])
        self.ask()


    def postAskAction(self) :
        if self.getChoiceIdx() == 0  :
            prompt = PromptA()
            finalText =str("\nyou wrote a possible sentence from Perec : " + prompt.gatherString() + "\n")
        elif self.getChoiceIdx() == 1    :
            prompt = PromptB()
            finalText =str("\nof course path was : " + prompt.gatherString() + "\n")
        print(finalText)

# Actual demo 
MainMenu = MainQuestion()
print(MainQuestion.finalText)
print("that's all folks !")

