import flet as ft


class Controller:
    def __init__(self, view, model):
        self.storeSelezionato = None
        self._view = view
        self._model = model

    def fillDD(self):
        stores = self._model.getStore()
        for store in stores:
            self._view._ddStore.options.append(ft.dropdown.Option(key = store.store_name, data = store, on_click=self.choiceStore))
        self._view.update_page()

    def handleCreaGrafo(self, e):
        giorniMax = self._view._txtIntK.value
        if self._view._txtIntK is None:
            self._view.txt_result.controls.clear()
            self._view.txt_result.controls.append(ft.Text("Devi inserire un valore di K!", color="red"))
            return
        try:
            giorniMax = int(giorniMax)
        except ValueError:
            self._view.txt_result.controls.clear()
            self._view.txt_result.controls.append(ft.Text("Devi inserire un valore numerico di K!", color="red"))
            return
        self._view.txt_result.controls.clear()
        self._model.buildGraph(self.storeSelezionato.store_id, giorniMax)
        nodi, archi = self._model.getGraphDetails()
        self._view.txt_result.controls.append(ft.Text(f"Grafo creato correttamente:"))
        self._view.txt_result.controls.append(ft.Text(f"Numero di nodi: {nodi}"))
        self._view.txt_result.controls.append(ft.Text(f"Numero di archi: {archi}"))
        self._view.update_page()


    def handleCerca(self, e):
        pass

    def handleRicorsione(self, e):
        pass

    def choiceStore(self, e):
        self.storeSelezionato = e.control.data