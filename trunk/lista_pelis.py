#!/usr/bin/env python
# -*- coding: utf-8 -*-
# generated by wxGlade 0.6.3 on Fri Jul  9 22:35:44 2010
import wx
import sys
import MySQLdb
# begin wxGlade: extracode
# end wxGlade



class Ventana(wx.Frame):
    def __init__(self, *args, **kwds):
        # begin wxGlade: Ventana.__init__
        kwds["style"] = wx.DEFAULT_FRAME_STYLE
        wx.Frame.__init__(self, *args, **kwds)
        self.panel_ventana = wx.Panel(self, -1)
        self.db = MySQLdb.connect('localhost', 'yanina', 'yanina', 'yanina', charset='UTF8')
        self.peli_lista = wx.ListCtrl(self.panel_ventana, -1, style=wx.LC_REPORT|wx.SUNKEN_BORDER)
        self.b_cerrar = wx.Button(self.panel_ventana, wx.ID_CLOSE, "")

        self.__set_properties()
        self.__do_layout()

        self.Bind(wx.EVT_BUTTON, self.OnCerrarBoton, self.b_cerrar)
        # end wxGlade

    def __set_properties(self):
        # begin wxGlade: Ventana.__set_properties
        self.SetTitle("Lista Peliculas")
        self.SetSize((350, 450))
        self.peli_lista.SetMinSize((640, 400))
        self.panel_ventana.SetMinSize((650, 495))
        # end wxGlade
    #agrego columnas
        columnas = [u'id_Peli', u'Titulo', u'Genero']
        for col, text in enumerate(columnas):
            self.peli_lista.InsertColumn(col, text)
        self.peli_lista.SetColumnWidth(0, 60)
        self.peli_lista.SetColumnWidth(1, 150)
        self.peli_lista.SetColumnWidth(2, 100)
        

        c = self.db.cursor()
        a = c.execute('''SELECT id_peliculas, titulo, genero FROM tabla_peliculas''')
        q = c.fetchall()

        for lista in q:
            index = self.peli_lista.InsertStringItem(sys.maxint, str(lista[0]))
            for colu, text in enumerate (lista[1:]):
                self.peli_lista.SetStringItem(index, colu+1, str(text))
        c.close()
    
    
    def __do_layout(self):
        # begin wxGlade: Ventana.__do_layout
        sizer_1 = wx.BoxSizer(wx.VERTICAL)
        grid_sizer_1 = wx.GridSizer(2, 1, 0, 0)
        grid_sizer_1.Add(self.peli_lista, 1, wx.EXPAND, 0)
        grid_sizer_1.Add(self.b_cerrar, 0, wx.TOP|wx.ALIGN_LEFT, 160)
        self.panel_ventana.SetSizer(grid_sizer_1)
        sizer_1.Add(self.panel_ventana, 1, wx.EXPAND, 0)
        self.SetSizer(sizer_1)
        self.Layout()
        self.Centre()
        # end wxGlade

    def OnCerrarBoton(self, event):
        # wxGlade: Ventana.<event_handler>
        self.Close()

# end of class Ventana


class MyApp(wx.App):
    def OnInit(self):
        wx.InitAllImageHandlers()
        listado = Ventana(None, -1, "")
        self.SetTopWindow(listado)
        listado.Show()
        return 1

# end of class MyApp

if __name__ == "__main__":
    app = MyApp(0)
    app.MainLoop()