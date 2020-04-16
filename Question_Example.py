from Question_Prompt    import Prompt
from Question_Menu      import Menu


#demo class for a question prompt
class MainPrompt(Prompt)    :

    def __init__(self):
       
        super().__init__()
        self.ask()

#demo class for a question menu
class MainQuestion(Menu)    :

    def __init__(self):
        self._PossibleAnwsers = [Menu.Answer("default anwser 1"),Menu.Answer("default anwser 2") ]
        super().__init__()
        self.ask()


# Actual demo 
MainMenu = MainQuestion()
MainPrompt = MainPrompt()
print("that's all folks !")

