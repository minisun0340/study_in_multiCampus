# wxtest2

import wx;
import weather;
from ch143 import * ;
from ch143 import itemdb

app = wx.App();
frame = wx.Frame(None, 0 , 'Test');

p1 = wx.Panel(frame);
bt1 = wx.Button(p1,label='Button1');
bt2 = wx.Button(p1,label='Button2');
bt3 = wx.Button(p1,label='Button3');
ps = wx.BoxSizer(wx.HORIZONTAL);
ps.Add(bt1);
ps.Add(bt2);
ps.Add(bt3);
p1.SetSizer(ps);

p2 = wx.Panel(frame);
names = ['abc','eds','fse','gfsd'];
list = wx.ListBox(p2,choices= names);
list.SetSize(wx.Size(300,200));

box = wx.BoxSizer(wx.VERTICAL);
frame.SetSizer(box);
box.Add(p1,border=10,flag=wx.DOWN);
box.Add(p2,border=10,flag=wx.UP);


def clickbt1(event):
    list.Clear();
    items = weather.getdata();
    list.AppendItems(items);
def clickbt2(event):
    list.Clear();
    items = itemdb.selectui();
    list.AppendItems(items);
def clickbt3(event):
    list.Clear();
    items = ['999', '000', '111', '222'];
    list.AppendItems(items);
bt1.Bind(wx.EVT_BUTTON, clickbt1);
bt2.Bind(wx.EVT_BUTTON, clickbt2);
bt3.Bind(wx.EVT_BUTTON, clickbt3);

frame.Show(True);
app.MainLoop();
