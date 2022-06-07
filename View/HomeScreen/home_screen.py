from View.base_screen import BaseScreenView
from View.HomeScreen.components.ContentNavigationDrawer.content_navigation_drawer import ContentNavigationDrawer

class HomeScreenView(BaseScreenView):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def model_is_changed(self):
        print("HomeScreenView")
