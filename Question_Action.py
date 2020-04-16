
# Main class for describing a menu
class Action(object)  :

    _Name = "DefaultAction"
    
    def __init__(self, text)  :
        object.__init__(self)
        self._Name = text

    def do(self)   :
        raise NotImplementedError()

    def getstr(self)   :
        return self._Name



