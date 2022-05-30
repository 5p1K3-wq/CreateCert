# The screens dictionary contains the objects of the models and controllers
# of the screens of the application.

from Controller.home_screen import HomeScreenController
from Model.home_screen import HomeScreenModel

screens = {
    "home screen": {
        "model": HomeScreenModel,
        "controller": HomeScreenController,
    },
}
