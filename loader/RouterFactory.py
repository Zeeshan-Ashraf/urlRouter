from models.advRouter import AdvRouter
from models.simpleRouter import SimpleRouter


class RouterFactory:
    def getRouter(self, path: str):
        if '*' in path:
            return AdvRouter()
        else:
            return SimpleRouter()
