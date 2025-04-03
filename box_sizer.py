import wx


def is_default_size(widget):
    if not hasattr(widget, 'GetMinSize'):
        return False
    min_size = widget.GetMinSize()
    return min_size == (-1, -1)


def is_expand_widget(widget):
    return isinstance(widget, wx.StaticLine) | isinstance(widget, wx.StaticBoxSizer)


class SimpleSizer(wx.BoxSizer):
    def __init__(self, orient=wx.VERTICAL, content_default_size=(60, -1), padding=3):
        super().__init__(orient)
        self.row_type = wx.HORIZONTAL if orient == wx.VERTICAL else wx.VERTICAL
        self.content_default_size = content_default_size
        self.padding = padding
        self.align = wx.ALIGN_BOTTOM if self.row_type == wx.HORIZONTAL else wx.ALIGN_LEFT

    def add_1d(self, widgets):
        row_sizer = wx.BoxSizer(self.row_type)
        for widget in widgets:
            if is_default_size(widget):
                widget.SetMinSize(self.content_default_size)
            row_sizer.Add(widget, 1 if is_expand_widget(widget) else 0, self.align | wx.ALL, self.padding)
        self.Add(row_sizer, 0, wx.ALL | wx.EXPAND, self.padding)

    def add_2d(self, widgets_list):
        for widgets in widgets_list:
            self.add_1d(widgets)


class SimpleStaticSizer(wx.StaticBoxSizer):
    def __init__(self, panel, static_box_label, orient=wx.VERTICAL, content_default_size=(60, -1), padding=3):
        static_box = wx.StaticBox(panel, label=static_box_label)
        super().__init__(static_box, orient)
        self.static_box = static_box
        self.row_type = wx.HORIZONTAL if orient == wx.VERTICAL else wx.VERTICAL
        self.content_default_size = content_default_size
        self.padding = padding
        self.align = wx.ALIGN_BOTTOM if self.row_type == wx.HORIZONTAL else wx.ALIGN_LEFT

    def add_1d(self, widgets):
        row_sizer = wx.BoxSizer(self.row_type)
        for widget in widgets:
            if is_default_size(widget):
                widget.SetMinSize(self.content_default_size)
            row_sizer.Add(widget, 1 if is_expand_widget(widget) else 0, self.align | wx.ALL, self.padding)
        self.Add(row_sizer, 0, wx.ALL | wx.EXPAND, self.padding)

    def add_2d(self, widgets_list):
        for widgets in widgets_list:
            self.add_1d(widgets)
