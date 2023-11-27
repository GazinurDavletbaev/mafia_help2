from kivy.lang import Builder
from kivy.properties import ObjectProperty

from kivymd.app import MDApp
from kivymd.uix.scrollview import MDScrollView

KV = '''
<ContentNavigationDrawer>

    MDList: # list popup on the left

        OneLineListItem:    # button in popup list
            text: "Новая игра"
            on_press:
                root.nav_drawer.set_state("close")
                root.screen_manager.current = "scr 1"
        OneLineListItem:
            text: "Игровой день"
            on_press:
                root.nav_drawer.set_state("close")
                root.screen_manager.current = "scr 2"
        OneLineListItem:
            text: "Рейтинг"
            on_press:
                root.nav_drawer.set_state("close")
                root.screen_manager.current = "scr 3"
        OneLineListItem:
            text: "Настройки"
            on_press:
                root.nav_drawer.set_state("close")
                root.screen_manager.current = "scr 4"
                


MDScreen:

    MDTopAppBar:
        pos_hint: {"top": 1}
        elevation: 4
        title: "MAFIA_HELP"
        left_action_items: [["menu", lambda x: nav_drawer.set_state("open")]]

    MDNavigationLayout: 

        MDScreenManager:
            id: screen_manager

            MDScreen:
                name: "scr 1"

                MDLabel:
                    text: "Screen 1"
                    halign: "center"

            MDScreen:
                name: "scr 2"

                MDLabel:
                    text: "loh"
                    image: "image/mafia_help.jpg"
                    halign: "center"
            MDScreen:
                name: "scr 3"

                MDLabel:
                    text: "loh2"
                    halign: "center"
            MDScreen:
                name: "scr 4"

                MDLabel:
                    text: "loh3"
                    halign: "center"

        MDNavigationDrawer:
            id: nav_drawer
            radius: (0, 16, 16, 0)
            MDNavigationDrawerMenu:

                MDNavigationDrawerHeader:
                    source: "image/mafia_help.jpg"
                    spacing: "4dp"
                    padding: "12dp", 0, 0, "56dp"

            ContentNavigationDrawer:
                screen_manager: screen_manager
                nav_drawer: nav_drawer
'''


class ContentNavigationDrawer(MDScrollView):
    screen_manager = ObjectProperty()
    nav_drawer = ObjectProperty()


class Example(MDApp):
    def build(self):
        self.theme_cls.primary_palette = "Orange"
        self.theme_cls.theme_style = "Dark"
        return Builder.load_string(KV)


Example().run()