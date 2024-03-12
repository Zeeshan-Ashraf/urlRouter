from loader.IRouter import IRouter
from models.routing import Routing
from utility.getRegex import getRegex
import re


class AdvRouter(IRouter):
    def getRoute(self, path, routing: Routing):
        regexFormula = getRegex(path)
        result = []

        for key, value in routing.getRouteTable().items():
            if re.search(regexFormula, key):
                result.append(value)

        return result

    def setRoute(self, path, controller, routing: Routing):
        routing.getRouteTable()[path] = controller
