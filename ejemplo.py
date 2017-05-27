#!/usr/bin/python
#-*- coding: latin-1 -*-
import wx


app = wx.App(False)
frame = wx.Frame(None, title = "titulo", size = (300, 300))
nb = wx.Notebook(frame)

panel1 = wx.Panel(nb)
texto = wx.StaticText(panel1, label = "text de prueba", pos = (12, 23))
boton = wx.Button(panel1, label = "soy un boton xdxd", pos = ( 30, 23))




nb.AddPage(panel1(nb), "panel 1")

frame.Show()
app.MainLoop()
