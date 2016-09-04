class Token():
    def __init__(self,color):
        self._color=color

    @property
    def color(self):
        return self._color

    @color.setter
    def color(self,v):
        self._color=v