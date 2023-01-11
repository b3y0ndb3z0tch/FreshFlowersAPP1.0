from kivy.properties import StringProperty, BooleanProperty, ObjectProperty, NumericProperty
from kivymd.uix.button import MDRaisedButton, MDFillRoundFlatButton, MDRoundFlatButton, MDRectangleFlatIconButton, \
    MDRectangleFlatButton
from kivymd.uix.card import MDCard, MDCardSwipe, MDSeparator
from kivy.uix.screenmanager import ScreenManager, NoTransition
from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.core.window import Window
from kivymd.uix.screen import MDScreen
from kivymd.uix.textfield import MDTextField
import recieve_homepage.recieve_button_functions

Window.size = (300, 500)

navigation_helper = """
<ShareFlowerCard>
    padding: 4 
    size_hint: None, None
    MDRelativeLayout:
        MDFillRoundFlatButton:
            pos_hint: {"center_x": .5, "center_y": .5}
            size_hint: 1,.5
            text: "Share"
            on_press:
                app.share_flowers(root)
<RecieveFlowerCard>
    padding: 4 
    size_hint: None, None
    MDRelativeLayout:
        MDFillRoundFlatButton:
            pos_hint: {"center_x": .5, "center_y": .5}
            size_hint: 1,.5
            text: "Recieve"
            on_press: 
                app.recieve_flowers()

#START OF APP
MDScreen:
    MDNavigationLayout:
        ScreenManager:
            id: screen_manager
            MDScreen:
                name: "HomeScreen"
                MDBoxLayout:
                    orientation: 'vertical'
                    id: home_screen
                    adaptive_size: True
                    spacing: "56dp"
                    pos_hint: {"center_x": .5, "center_y": .5}
                    ShareFlowerCard:
                        line_color:(0.2, 0.2, 0.2, 0)
                        md_bg_color:self.theme_cls.primary_light
                        shadow_softness:2
                        shadow_offset:(0, 1)
                        on_press:print("This was pressed")
                    RecieveFlowerCard:
                        line_color:(0.2, 0.2, 0.2, 0)
                        md_bg_color:self.theme_cls.primary_light
                        shadow_softness:2
                        shadow_offset:(0, 1)
                        on_press:print("This was pressed")
            MDScreen:
                name: "shareflowers_page"
                MDBoxLayout:
                    orientation: 'vertical'
                    md_bg_color: app.theme_cls.primary_color
                    MDTopAppBar:
                        title: "Posie Pusher"
                        use_overflow: True
                        md_bg_color: app.theme_cls.accent_color
                        specific_text_color: app.theme_cls.accent_color
                        halign: "center"
                        elevation: 4
                        pos_hint: {"top": 1}
                        left_action_items: [['menu', lambda x: nav_drawer.set_state('open'), "Menu"]]
                        right_action_items: [['menu-down-outline', lambda x: nav_drawer2.set_state('open')]]
                    MDBoxLayout:
                        orientation: 'vertical'
                        spacing: 10
                        MDAnchorLayout:
                            #size_hint: (1,3)
                            #adaptive_height: True
                            anchor_x: 'center'
                            padding: [20, 5, 5, 35]
                            md_bg_color: 1,1,1,.3
                            MDScrollView:
                                scroll_timeout: 100
                                do_x_scroll: True
                                MDList:
                                    id: shareflowers_MDSCROLLVIEW
                                    spacing: 15
                        MDAnchorLayout:
                            id: shareflowers_MDANCHORLAYOUT
                            padding: [0,0,10,0]
                            size_hint: (1, .1)
                            anchor_x: 'center'
                            anchor_y: 'bottom'                    
"""


class shareflowers_page_textfield(MDTextField):
    id = StringProperty()
    size_hint_x: .5
    pos_hint: {"center_x": .5}

class ShareFlowerCard(MDCard):
    pass


class RecieveFlowerCard(MDCard):
    pass


class ScreenManager(ScreenManager):
    pass


class CreateEventScreen(MDScreen):
    pass


class shareflowers_page(MDScreen):
    pass


sm = ScreenManager(transition=NoTransition())
sm.add_widget(CreateEventScreen(name="HomeScreen"))
sm.add_widget(CreateEventScreen(name="NotificationScreen"))
sm.add_widget(CreateEventScreen(name="CreateEventScreen"))
sm.add_widget(shareflowers_page(name="shareflowers_page"))


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
    share_flowers_information = {"Email": False, "Phone": False, "Guest Count": False, "Event Zip": False,
                                 "Event Location": False, "Event Color Theme": False}

    def shareflowers_page_submitbutton_function(self, root):
        print("hello")

    def share_flowers(self, root):
        print("share_flowers from 'HOME SCREEN' / 'home_screen'")
        self.root.ids.screen_manager.current = 'shareflowers_page'
        for key, value in self.share_flowers_information.items():
            print(key, value)
            text_field = shareflowers_page_textfield(hint_text=str(key), id=str(key))
            self.root.ids.shareflowers_MDSCROLLVIEW.add_widget(text_field)
        self.root.ids.shareflowers_MDSCROLLVIEW.add_widget(MDSeparator(color=(0, 0, 0, 1), size_hint=(.8, None)))
        # self.root.ids.shareflowers_MDSCROLLVIEW.add_widget(MDAnchorLayout(id="shareflowers_MDANCHORLAYOUT", padding=[0,0,10,0], size_hint = (1,1), anchor_y='bottom'))
        submit_button = MDFillRoundFlatButton(text="Submit",
                                              on_press=recieve_homepage.recieve_button_functions.shareflowers_page_submitbutton_function(
                                                  self.root))
        # self.shareflowers_page_submitbutton_function)
        self.root.ids.shareflowers_MDANCHORLAYOUT.add_widget(submit_button)
        # , on_press=recieve_homepage.recieve_button_functions.shareflowers_page_submitbutton_function(self, root)))
        # , on_press=recieve_homepage.recieve_button_functions.shareflowers_page_submitbutton_function(self)))

    def shareflowers_page_submit(self):
        print("Time to run through the textfield / delete the textfields")

    def recieve_flowers(self):
        print("Recieve Flowers")

    def build(self):
        screen = Builder.load_string(navigation_helper)
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Green"
        return screen


DemoApp().run()