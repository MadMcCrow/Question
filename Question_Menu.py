

# Main class for describing a menu
class Menu(object)  :


    _Question   = 'DefaultQuestion'

    _PossibleAnwsers = ["default anwser 1","default anwser 2" ]

    _MenuSize = 40

    def _format(self)  :
        from textwrap import wrap
        text = "+" + "-" * self._MenuSize + "+" + '\n'
        for quest in wrap(self._Question, self._MenuSize - 2)    :
             text += "|" + quest.center(self._MenuSize,' ') + "|"  +'\n'
        text += "|" + str("|").rjust(self._MenuSize + 1) + '\n'
        for idx, anws in enumerate(self._PossibleAnwsers):
            anws = str(idx) + " - " + anws
            for t in wrap(anws, self._MenuSize - 2)    :
                text += "|" + t.center(self._MenuSize,' ') + "|"  +'\n'
        text += "|" + str("|").rjust(self._MenuSize + 1) + '\n'
        text += "|" + "enter a number : ".center(self._MenuSize,' ') + "|"  +'\n'
        text += "+" + "-" * self._MenuSize + "+" + '\n'
        return text


    def _ask(self)  :
        userinput = -1
        while userinput is not in range(0, len(self._PossibleAnwsers) -1)
        userinput = print(self._format())



    def __init__(self):
        super().__init__()
