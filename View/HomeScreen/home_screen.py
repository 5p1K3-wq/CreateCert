from View.base_screen import BaseScreenView
from View.HomeScreen.components.Tab.tab_home_screen import TabHomeScreen

class HomeScreenView(BaseScreenView):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def model_is_changed(self):
        print("HomeScreenView")