import wx


class SimpleApp(wx.App):
    HIGH_DPI = False

    def __init__(self, title="SimpleApp"):
        super().__init__()

        self.frame = wx.Frame(None, title=title)
        self.panel = wx.Panel(self.frame)

    def run(self):
        if self.HIGH_DPI:
            ScaleWindowDPI(self.frame)
        self.panel.SetSize(self.panel.GetBestSize())
        self.frame.Fit()
        self.frame.Show()
        self.MainLoop()

    def bind_button(self, button_name, call):
        self.Bind(wx.EVT_BUTTON, call, id=self.frame.FindWindowByName(button_name).GetId())

    def activate_high_dpi(self):
        import ctypes

        try:
            # 1 = 系统级 DPI 感知（推荐）
            ctypes.windll.shcore.SetProcessDpiAwareness(1)
        except:
            # 回退到旧版 API（Win7/8）
            ctypes.windll.user32.SetProcessDPIAware()

        self.HIGH_DPI = True


def ScaleWindowDPI(window):
    """递归缩放窗口及其所有子控件的尺寸和位置"""
    if not isinstance(window, wx.Window):
        return

    # 缩放窗口自身尺寸
    if window.GetSize() != wx.DefaultSize:
        window.SetSize(window.FromDIP(window.GetSize()))

    # 缩放窗口位置（如果是顶级窗口）
    if isinstance(window, wx.TopLevelWindow) and window.GetPosition() != wx.DefaultPosition:
        window.SetPosition(window.FromDIP(window.GetPosition()))

    # 字体DPI适配（核心新增部分）
    if window.GetFont().IsOk():
        font = window.GetFont()
        dpi_ratio = wx.Window.GetDPIScaleFactor(wx.Window())
        window.SetFont(font.Scaled(1.0 / dpi_ratio))

    # 递归处理所有子控件
    for child in window.GetChildren():
        ScaleWindowDPI(child)
