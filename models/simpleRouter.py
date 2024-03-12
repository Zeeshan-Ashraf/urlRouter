from loader.IRouter import IRouter
from models.routing import Routing


class SimpleRouter(IRouter):
    def getRoute(self, path, routeTable: Routing):
        return routeTable.getRouteTable()[path]

    def setRoute(self, path, controller, routing: Routing):
        routing.getRouteTable()[path] = controller
