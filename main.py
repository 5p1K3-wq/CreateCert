"""
The entry point to the application.

The application uses the MVC template. Adhering to the principles of clean
architecture means ensuring that your application is easy to test, maintain,
and modernize.

You can read more about this template at the links below:

https://github.com/HeaTTheatR/LoginAppMVC
https://en.wikipedia.org/wiki/Model–view–controller
"""
import os
from typing import NoReturn

from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager

from kivymd.app import MDApp

from View.screens import screens


class CreateCert(MDApp):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.path_to_view = self.directory + '/View'
        self.load_all_kv_files()
        self.manager_screens = ScreenManager()

    def build(self) -> ScreenManager:
        self.generate_application_screens()
        return self.manager_screens

    def load_all_kv_files(self) -> NoReturn:
        for d, dirs, files in os.walk(self.path_to_view):
            for f in files:
                if (
                        os.path.splitext(f)[1] == ".kv"
                        and f != "style.kv"
                        and "Updates" not in d
                        and "__MACOS" not in d
                ):
                    path_to_kv_file = os.path.join(d, f)
                    with open(path_to_kv_file, encoding="utf-8") as kv_file:
                        Builder.load_string(kv_file.read())

    def generate_application_screens(self) -> NoReturn:
        """
        Creating and adding screens to the screen manager.
        You should not change this cycle unnecessarily. He is self-sufficient.

        If you need to add any screen, open the `View.screens.py` module and
        see how new screens are added according to the given application
        architecture.
        """

        for i, name_screen in enumerate(screens.keys()):
            model = screens[name_screen]["model"]()
            controller = screens[name_screen]["controller"](model)
            view = controller.get_view()
            view.manager_screens = self.manager_screens
            view.name = name_screen
            self.manager_screens.add_widget(view)


if __name__ == "__main__":
    CreateCert().run()
