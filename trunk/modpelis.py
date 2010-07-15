#!/usr/bin/env python
# -*- coding: utf-8 -*-
# generated by wxGlade 0.6.3 on Tue Jun 29 13:36:13 2010

import wx
import MySQLdb

# begin wxGlade: extracode
# end wxGlade



class MyFrame1(wx.Frame):
    def __init__(self, *args, **kwds):
        # begin wxGlade: MyFrame1.__init__
        kwds["style"] = wx.DEFAULT_FRAME_STYLE
        wx.Frame.__init__(self, *args, **kwds)
        self.db = MySQLdb.connect('localhost', 'yanina', 'yanina', 'yanina', charset='UTF8')
        self.panel_1 = wx.Panel(self, -1)
        self.frase = wx.StaticText(self.panel_1, -1, "Ingrese el nombre de la pelicula a modificar")
        self.peliculas = wx.StaticText(self.panel_1, -1, "pelicula:")
        self.texto_peliculas = wx.TextCtrl(self.panel_1, -1, "")
        self.static_line_1 = wx.StaticLine(self.panel_1, -1)
        self.static_line_2 = wx.StaticLine(self.panel_1, -1)
        self.boton_aceptar = wx.Button(self.panel_1, wx.ID_SAVE, "")
        self.boton_cancelar = wx.Button(self.panel_1, wx.ID_EXIT, "")

        self.__set_properties()
        self.__do_layout()

        self.Bind(wx.EVT_BUTTON, self.OnAceptar, self.boton_aceptar)
        self.Bind(wx.EVT_BUTTON, self.OnCancelar, self.boton_cancelar)
        # end wxGlade

    def __set_properties(self):
        # begin wxGlade: MyFrame1.__set_properties
        self.SetTitle("Modificación")
        self.frase.SetFont(wx.Font(10, wx.MODERN, wx.NORMAL, wx.NORMAL, 1, ""))
        self.SetFocus()
        # end wxGlade

    def __do_layout(self):
        # begin wxGlade: MyFrame1.__do_layout
        sizer_2 = wx.BoxSizer(wx.VERTICAL)
        sizer_3 = wx.BoxSizer(wx.VERTICAL)
        sizer_4 = wx.BoxSizer(wx.HORIZONTAL)
        grid_sizer_1 = wx.FlexGridSizer(2, 2, 0, 0)
        sizer_3.Add(self.frase, 0, wx.ALL, 10)
        grid_sizer_1.Add(self.peliculas, 0, wx.ALL, 10)
        grid_sizer_1.Add(self.texto_peliculas, 0, wx.BOTTOM|wx.EXPAND, 10)
        grid_sizer_1.Add(self.static_line_1, 0, wx.EXPAND, 0)
        grid_sizer_1.Add(self.static_line_2, 0, wx.EXPAND, 0)
        grid_sizer_1.AddGrowableCol(1)
        sizer_3.Add(grid_sizer_1, 0, wx.EXPAND, 0)
        sizer_4.Add(self.boton_aceptar, 0, wx.ALL, 10)
        sizer_4.Add(self.boton_cancelar, 0, wx.ALL, 10)
        sizer_3.Add(sizer_4, 0, wx.ALIGN_RIGHT, 0)
        self.panel_1.SetSizer(sizer_3)
        sizer_2.Add(self.panel_1, 1, wx.EXPAND, 0)
        self.SetSizer(sizer_2)
        sizer_2.Fit(self)
        self.Layout()
        # end wxGlade

    def OnAceptar(self, event): # wxGlade: MyFrame1.<event_handler>
        
        
        pelicula = self.texto_peliculas.GetValue()
        self.texto_peliculas.SetValue('')
        c = self.db.cursor()
        c.execute('''SELECT ID_peliculas, titulo, genero FROM peliculas WHERE titulo = %s''', (pelicula))
        q = c.fetchall()
        c.close()
        print q
        lista = []
        for elemento in q:
            lista.append(str(elemento[0]) + ' - ' + elemento[1] + ' - ' + elemento[2])
        print lista
        dlg = wx.SingleChoiceDialog(None, 'Las peliculas que cumplen su criterio de busqueda son:', 'Modificacion', lista, wx.CHOICEDLG_STYLE)

        if dlg.ShowModal() == wx.ID_OK:
            print 'You selected: %s\n' % dlg.GetStringSelection()

        dlg.Destroy()
        
        import peliculas
        ventana = peliculas.MyFrame(self, -1, u"Modificación de Peliculas")
        ventana.CenterOnScreen()
        ventana.Show()

    def OnCancelar(self, event): # wxGlade: MyFrame1.<event_handler>
        self.Close()

# end of class MyFrame1


if __name__ == "__main__":
    app = wx.PySimpleApp(0)
    wx.InitAllImageHandlers()
    frame1 = MyFrame1(None, -1, "")
    app.SetTopWindow(frame1)
    frame1.Show()
    app.MainLoop()