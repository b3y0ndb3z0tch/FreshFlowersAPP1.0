import os

from faker import Faker

from kivy.clock import Clock
from kivy.lang import Builder
from kivy.properties import StringProperty

from kivymd.app import MDApp
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.segmentedbutton import MDSegmentedButton, MDSegmentedButtonItem
from kivymd.utils import asynckivy

KV = '''
<UserCard>
    adaptive_height: True
    md_bg_color: "#343930"
    radius: 16

    TwoLineAvatarListItem:
        id: item
        divider: None
        _no_ripple_effect: True
        text: root.name
        secondary_text: root.path_to_file
        theme_text_color: "Custom"
        text_color: "#8A8D79"
        secondary_theme_text_color: self.theme_text_color
        secondary_text_color: self.text_color
        on_size:
            self.ids._left_container.size = (item.height, item.height)
            self.ids._left_container.x = dp(6)
            self._txt_right_pad = item.height + dp(12)

        ImageLeftWidget:
            source: root.album
            radius: root.radius


MDScreen:
    md_bg_color: "#151514"

    MDBoxLayout:
        orientation: "vertical"
        padding: "12dp"
        spacing: "12dp"

        MDLabel:
            adaptive_height: True
            text: "Your downloads"
            font_style: "H5"
            theme_text_color: "Custom"
            text_color: "#8A8D79"

        MDSegmentedButton:
            size_hint_x: 1
            selected_color: "#303A29"
            line_color: "#343930"
            on_marked: app.on_marked(*args)

            MDSegmentedButtonItem:
                text: "Songs"
                active: True

            MDSegmentedButtonItem:
                text: "Albums"

            MDSegmentedButtonItem:
                text: "Podcasts"

        RecycleView:
            id: card_list
            viewclass: "UserCard"
            bar_width: 0

            RecycleBoxLayout:
                orientation: 'vertical'
                spacing: "16dp"
                padding: "16dp"
                default_size: None, dp(72)
                default_size_hint: 1, None
                size_hint_y: None
                height: self.minimum_height
'''


class UserCard(MDBoxLayout):
    name = StringProperty()
    path_to_file = StringProperty()
    album = StringProperty()


class Example(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Dark"
        return Builder.load_string(KV)

    def on_marked(
        self,
        segment_button: MDSegmentedButton,
        segment_item: MDSegmentedButtonItem,
        marked: bool,
    ) -> None:
        self.generate_card()

    def generate_card(self):
        async def generate_card():
            for i in range(10):
                await asynckivy.sleep(0)
                self.root.ids.card_list.data.append(
                    {
                        "name": fake.name(),
                        "path_to_file": f"{os.path.splitext(fake.file_path())[0]}.mp3",
                        "album": fake.image_url(),
                    }
                )

        fake = Faker()
        self.root.ids.card_list.data = []
        Clock.schedule_once(lambda x: asynckivy.start(generate_card()))


Example().run()