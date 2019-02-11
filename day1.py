import collections
from random import choice

CPA = collections.namedtuple('CPA', ['section','module'])

class FrenchDeck:
    modules = [str(n) for n in range(1,10)]
    sections = 'FAR AUD BEC REG'.split()


    def __init__(self):
        self._cpas = [CPA(section, module) for section in self.sections
                                            for module in self.modules]

    def __len__(self):
        return len(self._cpas)

    def __getitem__(self,position):
        return self._cpas[position]


progress = FrenchDeck()

print(choice(progress))
