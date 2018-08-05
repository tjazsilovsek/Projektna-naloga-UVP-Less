BELA, CRNA = 'bela', 'crna'

class Figura:

    def __init__(self, x, y, barva):
        self.x = x
        self.y = y
        self.barva = barva

    def __str__(self):
        return '{0} figura na polju ({1}, {2})'.format(self.barva, self.x, self.y)

ZACETNAPOLJABELI = {(0, 0), (1, 0), (0, 1), (1, 1)}
ZACETNAPOLJACRNI = {(5, 5), (5, 4), (4, 5), (4, 4)}

class Plosca:

    def __init__(self, visina=6, sirina=6):
        self.visina = visina
        self.sirina = sirina
        self.poteze = 3
        self.plosca = [[' '] * self.visina for _ in range(self.sirina)]
        self.igralec = '0'
        self.izbrana_figura = None
        self.belefigure = []
        self.crnefigure = []
        for vrstica, stolpec in ZACETNAPOLJABELI:
            self.plosca[stolpec][vrstica] = '0'
            self.belefigure.append((vrstica, stolpec))
        for vrstica, stolpec in ZACETNAPOLJACRNI:
            self.plosca[stolpec][vrstica] = 'X'
            self.crnefigure.append((vrstica, stolpec))



    def __repr__(self):
        return 'Plosca(visina={}, sirina={}, belefigure={}, crnefigure={})'.format(
            self.visina, self.sirina, self.belefigure, self.crnefigure
        )

    def __str__(self):

        niz = ''
        rob = '+' + self.sirina * '-' + '+\n'
        for i ,vrstica in enumerate(self.plosca, 1):
            niz += '|' + ''.join(vrstica) + '|' + str(i) + '\n'
        return rob + niz + rob + ' 123456'

    def je_prosto(self, x, y):
        return self.plosca[y][x] == ' '

    def izberi_figuro(self, x, y):
        if self.izbrana_figura is None and self.igralec == self.plosca[y][x]:
            self.izbrana_figura = (x, y)

    def prestavi_figuro(self, x, y):
        if self.izbrana_figura:
            x1, y1 = self.izbrana_figura
            if self.igralec == self.plosca[y1][x1]:
                if 0 <= x < self.sirina and 0 <= y < self.visina and self.je_prosto(x, y):
                    if (abs(x1 - x) == 1 and y == y1) or (abs(y1 - y) == 1 and x1 == x) or (abs(x1 - x) == 2 and y == y1 and not self.je_prosto(min(x, x1) + 1, y)) or\
                    (abs(y1 - y) == 2 and x1 == x and not self.je_prosto(x, min(y, y1) + 1)):
                        self.plosca[y1][x1] = ' '
                        self.plosca[y][x] = self.igralec
                        self.poteze -= 1
                        self.izbrana_figura = None
                        if self.igralec == '0':
                            self.belefigure.remove((x1, y1))
                            self.belefigure.append((x, y))
                        else:
                            self.crnefigure.remove((x1, y1))
                            self.crnefigure.append((x, y))

                        if self.poteze == 0:
                            self.poteze = 3
                            if self.igralec == 'X':
                                self.igralec = '0'
                            else:
                                self.igralec = 'X'




    def zmaga(self):
        if ZACETNAPOLJACRNI == set(self.belefigure):
            return True
        elif ZACETNAPOLJABELI == set(self.crnefigure):
            return True
        else:
            return False

plosca = Plosca()
