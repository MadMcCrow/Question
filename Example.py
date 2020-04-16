from Question_Menu import Menu

class Main(Menu)    :

    def __init__(self):
        self._PossibleAnwsers = [Menu.Answer("default anwser 1"),Menu.Answer("default anwser 2") ]
        super().__init__()
        self.ask()


MainMenu = Main()


