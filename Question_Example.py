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

    class OpenPromptA(Action):
        def do(self):
            PromptA()

    class OpenPromptB(Action):
        def do(self):
            prompt = PromptB()
            print("of course path was :" + prompt.gatherString())

    def __init__(self):
        super().__init__("Example Question")

        AnswerA = Menu.Answer(MainQuestion.OpenPromptA("Write French litterature"))
        AnswerB = Menu.Answer(MainQuestion.OpenPromptB("Check sys is working fine"))
        self.addPossibleAnwser(AnswerA)
        self.addPossibleAnwser(AnswerB)
        self.ask()

# Actual demo 
MainMenu = MainQuestion()

print("that's all folks !")

