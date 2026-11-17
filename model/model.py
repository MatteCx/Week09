from database.dao import Dao

class Model:
    def __init__(self):
        self._solutions = []

    def get_stats(self, serate):
        return Dao.readStats(serate)

    def best_serie(self, serate):
        self._solutions = []
        films = Dao.films(serate)
        self.recursion([], films, 0, serate)
        self._solutions.sort(key=lambda serie: self.grater_overall(serie))
        return self._solutions[-1]

    def recursion(self, ps, films, indice_serate, tot_serate):
        generi = [film.genere for film in ps]
        if indice_serate == tot_serate:
            if not(len(set(generi)) < 3) and not(generi.count("Comedy") < 2):
                self._solutions.append(list(ps))
            return
        for film in films[indice_serate]:
            if (ps == [] or ps[-1].genere != film.genere) and (generi.count(film.genere) < 2):
                ps.append(film)
                self.recursion(ps, films, indice_serate + 1, tot_serate)
                ps.pop()

    def grater_overall(self, serie):
        total = 0
        for film in serie: total += film.media
        return total
