import json

from kivy.properties import StringProperty, BooleanProperty, ObjectProperty, NumericProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.scrollview import ScrollView
from kivy.utils import get_color_from_hex
from kivymd.material_resources import dp
from kivymd.uix.behaviors import RoundedRectangularElevationBehavior
from kivymd.uix.button import MDRaisedButton, MDFillRoundFlatButton, MDRoundFlatButton, MDRectangleFlatIconButton, \
    MDRectangleFlatButton
from kivymd.uix.card import MDCard, MDCardSwipe, MDSeparator
from kivy.uix.screenmanager import ScreenManager, NoTransition
from kivy.uix.widget import Widget
from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.core.window import Window
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.expansionpanel import MDExpansionPanelThreeLine
from kivymd.uix.floatlayout import MDFloatLayout
from kivymd.uix.label import MDLabel
from kivymd.uix.list import IconLeftWidget, OneLineAvatarIconListItem, IRightBodyTouch, ILeftBodyTouch, \
    ThreeLineAvatarIconListItem, TwoLineAvatarIconListItem, TwoLineListItem
from kivymd.uix.menu import MDDropdownMenu
from kivymd.uix.navigationdrawer import MDNavigationLayout
from kivymd.uix.screen import MDScreen
from kivymd.uix.tab import MDTabsBase
from kivymd.uix.textfield import MDTextField
from kivy.properties import partial
from kivymd.uix.list import OneLineListItem

Window.size = (300, 500)


navigation_helper = """

#START OF APP
MDScreen:
    MDNavigationLayout:
        ScreenManager:
            id: screen_manager
            MDScreen:
                name: "HomeScreen"
                BoxLayout:
                    orientation: 'vertical'
                    MDTopAppBar:
                        title: "Posie Pusher"
                        use_overflow: True
                        md_bg_color: app.theme_cls.accent_color
                        specific_text_color: app.theme_cls.accent_color
                        halign: "center"
                        elevation: 4
                        pos_hint: {"top": 1}
                        left_action_items: [['menu', lambda x: nav_drawer.set_state('open'), "Menu"]]
                        right_action_items: [['menu', lambda x: nav_drawer2.set_state('open')]]
                    BoxLayout:
                        orientation: 'vertical'
                        id: home_screen
"""


class ScreenManager(ScreenManager):
    pass

class CreateEventScreen(MDScreen):
    pass

sm = ScreenManager(transition=NoTransition())
sm.add_widget(CreateEventScreen(name="HomeScreen"))
sm.add_widget(CreateEventScreen(name="NotificationScreen"))
sm.add_widget(CreateEventScreen(name="CreateEventScreen"))
# sm.add_widget(CreatePlayerScreen(name="CreatePlayerScreen"))
# sm.add_widget(CreatePlayerScreen(name="CurrentEventsPage"))
# sm.add_widget(CreatePlayerScreen(name="CompletedEventsPage"))
# sm.add_widget(CreatePlayerScreen(name="SpecificEventPage"))
# sm.add_widget(CreatePlayerScreen(name="SearchPlayerScreen"))
# sm.add_widget(CreatePlayerScreen(name="SpecificFoundPlayerScreen"))
# sm.add_widget(CreatePlayerScreen(name="InviteRegularsScreen"))
# sm.add_widget(CreatePlayerScreen(name="OrganizeEventScreen"))
# sm.add_widget(CreatePlayerScreen(name="AssignDark"))
# sm.add_widget(CreatePlayerScreen(name="AssignLight"))
# sm.add_widget(CreatePlayerScreen(name="SearchInviteIndividualPlayer"))
# sm.add_widget(CreatePlayerScreen(name="FoundEventPlayerScreen"))
# sm.add_widget(CreatePlayerScreen(name="FoundEventInvitePlayerScreen"))
# sm.add_widget(CreatePlayerScreen(name="InviteIndividualsScreen"))
# sm.add_widget(CreatePlayerScreen(name="CreatePlayerScreen"))
# sm.add_widget(CreatePlayerScreen(name="DisplayTeams"))
# sm.add_widget(CreatePlayerScreen(name="CreateQuickEventScreen"))
# sm.add_widget(CreatePlayerScreen(name="EditQuickEventScreen"))
# sm.add_widget(CreatePlayerScreen(name="PaymentPage"))
# sm.add_widget(CreatePlayerScreen(name="ReviewPage"))
# sm.add_widget(CreatePlayerScreen(name="InviteAllPLayersScreen"))

class DemoApp(MDApp):
    def __int__(self, **kwargs):
        super(DemoApp, self).__init__(**kwargs)
    print("This will run when app is started")


    def build(self):
        screen = Builder.load_string(navigation_helper)
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Green"
        return screen

DemoApp().run()