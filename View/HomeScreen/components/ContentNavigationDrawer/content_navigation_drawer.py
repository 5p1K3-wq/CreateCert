from kivymd.theming import ThemableBehavior
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.list import MDList, OneLineIconListItem
from kivy.properties import StringProperty, ListProperty


class ItemDrawer(OneLineIconListItem):
    icon = StringProperty()
    text_color = ListProperty((0, 0, 0, 1))


class ContentNavigationDrawer(MDBoxLayout):
    pass


class DrawerList(ThemableBehavior, MDList):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        icons_item = {
            "account-cowboy-hat": "About author",
            "github": "Source code",
            "share-variant": "Share app",
            "shield-sun": "Dark/Light",
        }
        for icon_name in icons_item.keys():
            self.add_widget(
                ItemDrawer(icon=icon_name, text=icons_item[icon_name])
            )
            #self.root.ids.content_drawer.ids.md_list.add_widget(
            #    ItemDrawer(icon=icon_name, text=icons_item[icon_name])
            #)

    def set_color_item(self, instance_item):
        for item in self.children:
            if item.text_color == self.theme_cls.primary_color:
                item.text_color = self.theme_cls.text_color
                break
        instance_item.text_color = self.theme_cls.primary_color
