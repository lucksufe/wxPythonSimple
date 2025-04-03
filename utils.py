import wx
import json


def binary_ico(frame, binary_ico_data):
    icon = wx.Icon()
    icon.CopyFromBitmap(wx.Bitmap.NewFromPNGData(binary_ico_data, len(binary_ico_data)))
    frame.SetIcon(icon)


def get_event_value(event, name):
    return event.GetEventObject().GetParent().FindWindowByName(name).GetValue()


def get_event_dict(event):
    return get_ui_dict(event.GetEventObject().GetParent())


def dump_event_dict(event, file_name):
    kv = get_ui_dict(event.GetEventObject().GetParent())
    with open(file_name, "w") as f:
        json.dump(kv, f)
    return kv


def get_ui_dict(panel):
    widgets = panel.GetChildren()
    kv = {}
    for widget in widgets:
        if hasattr(widget, 'GetValue') and hasattr(widget, 'GetName'):
            kv[widget.GetName()] = widget.GetValue()
    return kv


def dump_ui_data(panel, file_name):
    with open(file_name, "w") as f:
        json.dump(get_ui_dict(panel), f)


def load_ui_data(panel, kv):
    widgets = panel.GetChildren()
    for widget in widgets:
        if hasattr(widget, 'GetValue') and hasattr(widget, 'GetName') and widget.GetName() in kv and hasattr(widget, 'SetValue'):
            widget.SetValue(kv[widget.GetName()])


def load_ui_data_from_file(panel, file_name):
    with open(file_name, "r") as f:
        kv = json.load(f)
        load_ui_data(panel, kv)
