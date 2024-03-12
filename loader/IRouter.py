from abc import ABC, abstractmethod
from models.routing import Routing


class IRouter(ABC):

    @abstractmethod
    def getRoute(self, path, routeTable: Routing):
        pass

    @abstractmethod
    def setRoute(self, path, controller, routeTable: Routing):
        pass
