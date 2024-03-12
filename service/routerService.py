from models.routing import Routing
from loader.RouterFactory import RouterFactory
from loader.IRouter import IRouter


class RouterService:
    def __init__(self):
        self.__routing = Routing()
        self.__routerFactory = RouterFactory()
        self.__iRouter: IRouter = None

    def setRoute(self):
        print("Set Path")
        path = input("Enter Path:")
        controller = input("Enter Controller function: ")
        self.__iRouter = self.__routerFactory.getRouter(path)

        try:
            self.__iRouter.setRoute(path, controller, self.__routing)
        except Exception:
            print("Invalid Input")

    def getRoute(self):
        print("Get Path")
        path = input("Enter Path:")
        self.__iRouter = self.__routerFactory.getRouter(path)
        result = None
        try:
            result = self.__iRouter.getRoute(path, self.__routing)
        except Exception:
            print("Invalid Input")

        return result
