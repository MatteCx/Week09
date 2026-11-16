from database.DB_connect import DBConnect
from model.film import Film

class Dao:
    @staticmethod
    def get_all_film():
        """Query di esempio, non utilizzata dalle funzionalità dell'esercizio."""
        cnx = DBConnect.get_connection()
        try:
            cursor = cnx.cursor(dictionary=True)
            try:
                cursor.execute('''SELECT id, titolo, genere, serata,
                                         numero_voti, somma_voti
                                  FROM film ORDER BY id''')

                result = []
                for r in cursor:
                    film = Film(r['id'], r['titolo'], r['genere'], r['serata'], r['numero_voti'], float(r['somma_voti']))
                    result.append(film)
                return result

            finally:
                cursor.close()
        finally:
            cnx.close()

    @staticmethod
    def readStats(serate):
            cnx = DBConnect.get_connection()
            try:
                cursor = cnx.cursor(dictionary=True)
                try:
                    query = '''SELECT genere, avg(somma_voti/numero_voti) as average, count(distinct id) as nFilms
                                FROM film
                                WHERE serata <= %s
                                GROUP BY genere
                                order by average'''
                    cursor.execute(query, (serate, ))
                    result = [f"{r['genere']}  |  {r['nFilms']}  |  {round(r['average'], 2)}" for r in cursor.fetchall()]
                    return result
                finally:
                    cursor.close()
            finally:
                cnx.close()

    @staticmethod
    def films(serate):
        cnx = DBConnect.get_connection()
        try:
            cursor = cnx.cursor(dictionary=True)
            try:
                result = []
                for s in range(serate):
                    query = '''SELECT id, titolo, genere, serata,somma_voti,numero_voti,  (somma_voti/numero_voti) as average
                                    FROM film
                                    WHERE serata = %s
                                    order by average desc '''
                    cursor.execute(query, (s+1,))
                    lista_di_oggetti = []
                    for f in cursor.fetchall():
                        film = Film(id=f['id'], titolo=f['titolo'], genere=f['genere'], serata=f['serata'], numero_voti=f['numero_voti'], somma_voti=f['somma_voti'])
                        lista_di_oggetti.append(film)
                    result.append(lista_di_oggetti)
                return result
            finally:
                cursor.close()
        finally:
            cnx.close()
