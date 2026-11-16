import copy
from database.dao import Dao

class Model:
    def __init__(self):
        self._solutions = []

    def serie_valida(self, ps):
        result = True
        generi = [film.genere for film in ps]
        generi_set = set(generi)
        if len(generi_set) < 3 : result = False
        if generi.count("Comedy") < 2: result = False
        return result

    def get_stats(self, serate):
        return Dao.readStats(serate)

    def best_serie(self, serate):
        self._solutions = []
        films = Dao.films(serate)
        self.recursion([], films, [n+1 for n in range(serate)])
        self._solutions.sort(key=lambda serie: self.grater_overall(serie))
        return self._solutions[-1]

    def recursion(self, ps, films, n):
        generi = [film.genere for film in ps]
        generi_set = set(generi)
        if len(n) == 0:
            if not(len(generi_set) < 3) and not(generi.count("Comedy") < 2):
                self._solutions.append(copy.deepcopy(ps))
            return
        D = copy.deepcopy(n)
        for s in D:
            for film in films[s-1]:
                if (ps == [] or ps[-1].genere != film.genere) and (generi.count(film.genere) < 2):
                    ps.append(copy.deepcopy(film))
                    n.remove(s)
                    self.recursion(ps, films, n)
                    ps.pop()
                    n.append(s)
                    n.sort()
            return

    def grater_overall(self, serie):
        total = 0
        for film in serie: total += film.media
        return total
