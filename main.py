from service.routerService import RouterService


if __name__ == "__main__":
    routerService: RouterService = RouterService()
    routerService.setRoute()
    print(routerService.getRoute())



