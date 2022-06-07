from View.HomeScreen.home_screen import HomeScreenView


class HomeScreenController:
    def __init__(self, model):
        self.model = model
        self.view = HomeScreenView(controller=self, model=self.model)

    def get_view(self) -> HomeScreenView:
        return self.view
