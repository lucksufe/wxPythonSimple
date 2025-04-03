import wx


class SimpleApp(wx.App):
    def __init__(self, title="SimpleApp"):
        super().__init__()
        self.frame = wx.Frame(None, title=title)
        self.panel = wx.Panel(self.frame)

    def run(self):
        self.panel.SetSize(self.panel.GetBestSize())
        self.frame.Fit()
        self.frame.Show()
        self.MainLoop()

    def bind_button(self, button_name, call):
        self.Bind(wx.EVT_BUTTON, call, id=self.frame.FindWindowByName(button_name).GetId())
