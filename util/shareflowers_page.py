def shareflowers_page_add_shareflowers_page_textfield(self, share_flowers_information, shareflowers_page_textfield):
    print("calling FUNC shareflowers_page_add_shareflowers_page_textfield from shareflowers_page using dict: self.share_flowers_information to add: shareflowers_page_textfield into the shareflowers_MDSCROLLVIEW")
    for key, value in self.share_flowers_information.items():
        print(key, value)
        text_field = shareflowers_page_textfield(hint_text=str(key), id=str(key))
        self.root.ids.shareflowers_MDSCROLLVIEW.add_widget(text_field)

def shareflowers_page_widget_SUBMIT_button(self):
    print("calling FUNC shareflowers_page_widget_SUBMIT_button from shareflowers_page using id: shareflowers_MDSCROLLVIEW to gather children textfield")