import networkx as nx
from database.DAO import DAO

class Model:

    def __init__(self):
        self._graph = nx.Graph()
        self._idMapOrdini ={}

    @staticmethod
    def getStore():
        return DAO.getStore()

    def buildGraph(self, store, giorniMax):
        nodi = DAO.getOrdini(store)
        for nodo in nodi:
            self._idMapOrdini[nodo.order_id] = nodo
        self._graph.add_nodes_from(nodi)
        archi = DAO.getArchi(giorniMax, store, self._idMapOrdini)
        for arco in archi:
            self._graph.add_edge(self._idMapOrdini[arco["ordine1"]], self._idMapOrdini[arco["ordine2"]], weight = arco["pesotot"])

    def getGraphDetails(self):
        return self._graph.number_of_nodes(), self._graph.number_of_edges()