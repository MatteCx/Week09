from UI.view import View
from model.model import Model
import flet as ft

class Controller:
    def __init__(self, view, model: Model):
        self._view = view
        self._model = model

    def handle_statistiche(self, e):
        serate = self._view.dd_serate.value
        elenco = self._model.get_stats(int(serate))
        self._view.risultati.controls = [ft.Text(el, size = 16) for el in elenco]
        self._view.page.update()

    def handle_programma(self, e):
        serate = self._view.dd_serate.value
        serie_ottimale = self._model.best_serie(int(serate))
        self._view.risultati.controls = [ft.Text(el, size=16) for el in serie_ottimale]
        self._view.page.update()
