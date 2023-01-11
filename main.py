from kivy.clock import Clock

import json

from kivy.properties import StringProperty, BooleanProperty, ObjectProperty, NumericProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.scrollview import ScrollView
from kivy.utils import get_color_from_hex
from kivymd.material_resources import dp
from kivymd.uix.anchorlayout import MDAnchorLayout
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
import recieve_homepage.recieve_button_functions
import util.shareflowers_page
import util.email_handle
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
                app.recieve_flowers(root)
<Email_Card>
    padding: 4
    #pos_hint: {"center_x":.5, "center_y": .5}
    size_hint: 1, 1
    MDBoxLayout:
        orientation: 'vertical'
        MDTextField:
            id: email_text_field
            hint_text: "Enter Valid Email"
            #pos_hint: {"center_x":.5,"center_y":.5}
            #size_hint: (.5, None)

#START OF APP
MDScreen:
    MDNavigationLayout:
        ScreenManager:
            id: screen_manager
            # MDScreen:
            #     name: "SetInitialScreen"
            #     MDBoxLayout:
            #         orientation: 'vertical'
            #         id: SetInitialScreen
            MDScreen:
                name: "EmailScreen"
                MDBoxLayout:
                    orientation: 'vertical'
                    spacing: '50dp'
                    id: email_screen
                    Image:
                        source: 'images/Logo.jpg'
                        size_hint: .8, .75
                        pos_hint: {"center_x":.5, "center_y":.5}
                    Email_Card:
                        size_hint: .8,.75
                        pos_hint: {"center_x":.5, "center_y":.5}
                        line_color:(0.2, 0.2, 0.2, 0)
                        md_bg_color:self.theme_cls.primary_light
                        shadow_softness:2
                        shadow_offset:(0, 1)
                        on_press:print("This was pressed")
                    MDFillRoundFlatButton:
                        pos_hint: {"center_x": .5, "center_y": .2}
                        size_hint: .5,.25
                        text: "Start"
                        on_press:
                            app.verify_email(root)
            MDScreen:
                name: "HomeScreen"
                # MDBoxLayout:
                #     orientation: 'vertical'
                    # MDTopAppBar:
                    #     title: "Posie Pusher"
                    #     use_overflow: True
                    #     md_bg_color: app.theme_cls.accent_color
                    #     specific_text_color: app.theme_cls.accent_color
                    #     halign: "center"
                    #     elevation: 4
                    #     pos_hint: {"top": 1}
                    #     left_action_items: [['menu', lambda x: nav_drawer.set_state('open'), "Menu"]]
                    #     right_action_items: [['menu-down-outline', lambda x: nav_drawer2.set_state('open')]]
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
                #recieve_homepage.recieve_button_functions.recieve_homepage(self)
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
                        left_action_items: [['menu', lambda x: top_app_left.set_state('open'), "Menu"]]
                        right_action_items: [['menu-down-outline', lambda x: app.open_top_app_right_navigation()]]
                    MDBoxLayout:
                        orientation: 'vertical'
                        #md_bg_color: 0,0,0,.1
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
                            #md_bg_color: 1,1,1,.3
                            size_hint: (1, .1)
                            #adaptive_height: True
                            anchor_x: 'center'
                            anchor_y: 'bottom'     
                            
        MDNavigationDrawer:
            id: top_app_left
            radius: (0, 16, 16, 0)
            ContentNavigationDrawer:
                orientation: 'vertical'
                spacing: '8dp'
                padding: '8dp'
                Image:
                    source: 'images/Logo.jpg'
                ScrollView:
                    MDList:
                        id: top_app_left_md_list
                        spacing: '8dp'
                        padding: '8dp'        
        
        MDNavigationDrawer:
            id: top_app_right
            radius: (16, 0, 0, 16)
            anchor: 'right'
            ContentNavigationDrawer:
                orientation: 'vertical'
                spacing: '8dp'
                padding: '8dp'
                Image:
                    source: 'images/Logo.jpg'
                MDLabel:
                    id: label1
                    text: app.account_info_email
                ScrollView:
                    MDList:
                        id: top_app_right_md_list
                        spacing: '8dp'
                        padding: '8dp'
                           
"""
class ContentNavigationDrawer(MDBoxLayout):
    #account_email = StringProperty()
    pass
class shareflowers_page_textfield(MDTextField):
    id = StringProperty()
    size_hint_x: .5
    pos_hint: {"center_x":.5}

class ShareFlowerCard(MDCard):
    pass
class RecieveFlowerCard(MDCard):
    pass
class Email_Card(MDCard):
    pass
class ScreenManager(ScreenManager):
    pass

class CreateEventScreen(MDScreen):
    pass

class DecideScreen(MDScreen):
    print("This is going to be run")
    # with open("json/account_info.json") as account_info:
    #     account_info = json.load(account_info)
    #     print(account_info)
    #     if account_info["Email"] == False & account_info["Verified"] == False:
    #         print("ENTER EMAIL")
    #         ScreenManager.current = "EmailScreen"
    #     if account_info["Email"] == True & account_info["Verified"] == False:
    #         print("NEED TO VERIFY EMAIL")
    #         ScreenManager.current = "HomeScreen"
    #     if account_info["Email"] == True & account_info["Verified"] == True:
    #         print("Need to go to the share page")

class SetInitialScreen(MDScreen):
    print("SetInitialScreen")
    def on_pre_enter(self):
        print("Got the on_pre_enter")
        Clock.schedule_once(self.setinitialscreen())
    def setinitialscreen(self):
        print("on_enter")
        with open("json/account_info.json") as account_info:
            account_info = json.load(account_info)
            print(account_info)
            if account_info["Email"] == False & account_info["Verified"] == False:
                print("ENTER EMAIL")
                self.ScreenManager.current = "EmailScreen"
            if account_info["Email"] == True & account_info["Verified"] == False:
                print("NEED TO VERIFY EMAIL")
                self.ScreenManager.current = "HomeScreen"
            if account_info["Email"] == True & account_info["Verified"] == True:
                print("Need to go to the share page")
class shareflowers_page(MDScreen):
    pass


sm = ScreenManager(transition=NoTransition())
sm.add_widget(DecideScreen(name="SetInitialScreen"))
sm.add_widget(CreateEventScreen(name="EmailScreen"))
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
    #Need to check if email verified through .json file
    # with open("json/account_info.json") as account_info:
    #     account_info = json.load(account_info)
    #     print(account_info)
    #     if account_info["Email"] == False & account_info["Verified"] == False:
    #         print("ENTER EMAIL")
    #         ScreenManager.current = "EmailScreen"
    #     if account_info["Email"] == True & account_info["Verified"] == False:
    #         print("NEED TO VERIFY EMAIL")
    #         ScreenManager.current = "HomeScreen"
    #     if account_info["Email"] == True & account_info["Verified"] == True:
    #         print("Need to go to the share page")
    #email_entered = True
    account_info_email = StringProperty()
    #share_flowers_information_to_kv = ObjectProperty()
    share_flowers_information = {"Email":False, "Phone":False, "Guest Count":False, "Event Zip": False, "Event Location": False, "Event Color Theme": False}
    # if email_entered == False:
    #     print("Make the screen EmailScreen")

    def open_top_app_right_navigation(self):
        #print(self.root.ids.screen_manager.current)
        print("Opening top_app_right navigation from " + self.root.ids.screen_manager.current)
        self.change_top_app_right_navigation_state()


    def share_flowers(self,app):
        print("'shareflowers_page' from 'HomeScreen' / button in boxlayout id: home_screen")
        self.root.ids.screen_manager.current = 'shareflowers_page'
        #print(self.root.ids.screen_manager.ids.HomeScreen)
        util.shareflowers_page.shareflowers_page_add_shareflowers_page_textfield(self,self.share_flowers_information,shareflowers_page_textfield)
        # for key, value in self.share_flowers_information.items():
        #     print(key, value)
        #     text_field = shareflowers_page_textfield(hint_text=str(key), id=str(key))
        #     self.root.ids.shareflowers_MDSCROLLVIEW.add_widget(text_field)
        submit_button = MDFillRoundFlatButton(text="Submit", on_press = self.gather_textfields)
        self.root.ids.shareflowers_MDANCHORLAYOUT.add_widget(submit_button)


    def change_top_app_right_navigation_state(self):
        print("FUNCTION: change_top_app_right_navigation_state - Need to change top_app_right navigation state")
        print(self.root.ids.top_app_right.state)
        if self.root.ids.top_app_right.state == "close":
            self.root.ids.top_app_right.set_state('open')
        else:
            self.root.ids.top_app_right.set_state('close')


    def gather_textfields(self,root):
        print("FUNCTION: gather_textfields from " + self.root.ids.screen_manager.current)
        for child in self.root.ids.shareflowers_MDSCROLLVIEW.children[:]:
            print(child.text)
            print(child.id)
            if child.text:
                self.share_flowers_information[child.id] = child.text
            # else:
            #     self.share_flowers_information[child.id] = False
            #print(self.share_flowers_information[child.id])
        print(self.share_flowers_information)
        #self.share_flowers_information_to_kv = self.share_flowers_information
        #print(self.share_flowers_information_to_kv)
        #print(self.root.ids.top_app_right.children.text)
        self.account_info_email = self.share_flowers_information["Email"]


    def shareflowers_page_submit(self):
        print("Time to run through the textfield / delete the textfields")
    def recieve_flowers(self):
        print("Recieve Flowers")
    def verify_email(self,app):
        print("verify_email FUNCTION pressed from " + self.root.ids.screen_manager.current)
        util.email_handle.email_alert("adamwilliams86@yahoo.com", "This is a test email from posies", "Body of the email to be decided")

    def build(self):
        screen = Builder.load_string(navigation_helper)
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Green"
        return screen


DemoApp().run()