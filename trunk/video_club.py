#!/usr/bin/env python
# -*- coding: utf-8 -*-
# generated by wxGlade 0.6.3 on Thu Jun 24 13:54:36 2010

import wx
import os
import MySQLdb
# begin wxGlade: extracode
# end wxGlade



class MyFrame (wx.Frame):
    def __init__(self, *args, **kwds):
        # begin wxGlade: MyFrame.__init__
        kwds["style"] = wx.DEFAULT_FRAME_STYLE
        wx.Frame.__init__(self, *args, **kwds)
        self.panel_1 = wx.Panel(self, -1)
        self.frame_1_statusbar = self.CreateStatusBar(1, 0)
        
        # Menu Bar
        self.menu = wx.MenuBar()
        self.altas  = wx.Menu()
        self.peliculas_altas = wx.MenuItem(self.altas , wx.NewId(), "Peliculas", "Ingreso de peliculas", wx.ITEM_NORMAL)
        self.altas .AppendItem(self.peliculas_altas)
        self.socios_altas = wx.MenuItem(self.altas , wx.NewId(), "Socios ", "Ingreso de socios", wx.ITEM_NORMAL)
        self.altas .AppendItem(self.socios_altas)
        self.alquileres_altas  = wx.MenuItem(self.altas , wx.NewId(), "Alquiler", "Ingresar alquileres", wx.ITEM_NORMAL)
        self.altas .AppendItem(self.alquileres_altas )
        self.menu.Append(self.altas , "&Altas")
        self.bajas = wx.Menu()
        self.peliculas_bajas = wx.MenuItem(self.bajas, wx.NewId(), "Peliculas ", "Eliminar peliculas", wx.ITEM_NORMAL)
        self.bajas.AppendItem(self.peliculas_bajas)
        self.socios_bajas = wx.MenuItem(self.bajas, wx.NewId(), "Socios ", "Eliminar socios", wx.ITEM_NORMAL)
        self.bajas.AppendItem(self.socios_bajas)
        self.alquiler_bajas = wx.MenuItem(self.bajas, wx.NewId(), "Alquiler", "Eliminar alquileres", wx.ITEM_NORMAL)
        self.bajas.AppendItem(self.alquiler_bajas)
        self.menu.Append(self.bajas, "&Bajas ")
        self.modificar = wx.Menu()
        self.peliculas_modificar = wx.MenuItem(self.modificar, wx.NewId(), "Peliculas", "Editar Peliculas", wx.ITEM_NORMAL)
        self.modificar.AppendItem(self.peliculas_modificar)
        self.socios_modificar = wx.MenuItem(self.modificar, wx.NewId(), "Socios", "Editar socios", wx.ITEM_NORMAL)
        self.modificar.AppendItem(self.socios_modificar)
        self.alquiler_modificar = wx.MenuItem(self.modificar, wx.NewId(), "Alquiler", "Editar alquileres", wx.ITEM_NORMAL)
        self.modificar.AppendItem(self.alquiler_modificar)
        self.menu.Append(self.modificar, "&Modificar")
        self.lista = wx.Menu()
        self.peliculas_lista = wx.MenuItem(self.lista, wx.NewId(), "Peliculas ", "Mostrar lista de peliculas", wx.ITEM_NORMAL)
        self.lista.AppendItem(self.peliculas_lista)
        self.socios_lista = wx.MenuItem(self.lista, wx.NewId(), "Socios", "Mostrar lista de socios", wx.ITEM_NORMAL)
        self.lista.AppendItem(self.socios_lista)
        self.alquileres_lista = wx.MenuItem(self.lista, wx.NewId(), "Alquileres ", "Mostar lista de alquileres", wx.ITEM_NORMAL)
        self.lista.AppendItem(self.alquileres_lista)
        self.menu.Append(self.lista, "&Lista")
        self.SetMenuBar(self.menu)
        # Menu Bar end
        
        #Para crear la funcion del boton y lugo la def
        self.Bind(wx.EVT_MENU, self.OnAltasPeliculas, self.peliculas_altas)
        self.Bind(wx.EVT_MENU, self.OnAltasSocios, self.socios_altas)
        self.Bind(wx.EVT_MENU, self.OnAltasAlquileres, self.alquileres_altas)
        self.Bind(wx.EVT_MENU, self.OnModificarPeliculas, self.peliculas_modificar)
        self.Bind(wx.EVT_MENU, self.OnModificarSocios, self.socios_modificar)
        
        self.__set_properties()
        self.__do_layout()
        # end wxGlade

    def __set_properties(self):
        # begin wxGlade: MyFrame.__set_properties
        self.SetTitle("frame_1")
        self.frame_1_statusbar.SetStatusWidths([-1])
        # statusbar fields
        frame_1_statusbar_fields = ["frame_1_statusbar"]
        for i in range(len(frame_1_statusbar_fields)):
            self.frame_1_statusbar.SetStatusText(frame_1_statusbar_fields[i], i)
        # end wxGlade

    def __do_layout(self):
        # begin wxGlade: MyFrame.__do_layout
        sizer_1 = wx.BoxSizer(wx.VERTICAL)
        sizer_1.Add(self.panel_1, 1, wx.EXPAND, 0)
        self.SetSizer(sizer_1)
        sizer_1.Fit(self)
        self.Layout()
        
    def OnAltasPeliculas(self,evt):
        import peliculas_altas
        ventana = stats.MyFrame(self, -1, u'',
        style = wx.DEFAULT_FRAME_STYLE)
        ventana.centerOnScreen()
        ventana.show(True)
    
    def OnAltasSocios(self,evt):
        import socios_altas
        ventana = stats.MyFrame(self, -1, u'',
        style = wx.DEFAULT_FRAME_STYLE)
        ventana.centerOnScreen()
        ventana.show(True)
    
    def OnAltasAlquileres(self,evt):
        import alquileres_altas
        ventana = alquileres_altas.Ventana(self, -1, u'')
        ventana.centerOnScreen()
        ventana.Show(True)
        
    def OnModificarPeliculas(self,evt):
        import peliculas_modificar
        ventana = stats.MyFrame(self, -1, u'',
        style = wx.DEFAULT_FRAME_STYLE)
        ventana.centerOnScreen()
        ventana.show(True)
        
    def OnModificarSocios(self,evt):
        import socios_modificar
        ventana = stats.MyFrame(self, -1, u'',
        style = wx.DEFAULT_FRAME_STYLE)
        ventana.centerOnScreen()
        ventana.show(True)
        # end wxGlade

# end of class MyFrame


if __name__ == "__main__":
    app = wx.PySimpleApp(0)
    wx.InitAllImageHandlers()
    ventana = MyFrame (None, -1, "")
    app.SetTopWindow(ventana)
    ventana.Show()
    app.MainLoop()
