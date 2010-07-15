#!/usr/bin/env python
# -*- coding: utf-8 -*-
# generated by wxGlade 0.6.3 on Tue Jul  6 15:15:34 2010


import os
import wx
import MySQLdb
# begin wxGlade: extracode
# end wxGlade



class Ventana(wx.Frame):
    def __init__(self, id_peli, *args, **kwds):
        # begin wxGlade: Ventana.__init__
        kwds["style"] = wx.DEFAULT_FRAME_STYLE
        wx.Frame.__init__(self, *args, **kwds)
        self.db = MySQLdb.connect('localhost', 'yanina', 'yanina', 'yanina', charset='UTF8')
        
        self.id_peli = id_peli
        c = self.db.cursor()
        c.execute('''SELECT * FROM tabla_peliculas WHERE id_peliculas = %s''', (self.id_peli))
        q = c.fetchone()
        c.close() 
        
        #Titulo:Ingreso
        self.titulo = wx.StaticText(self, -1, "Titulo:")
        self.titulo_ingreso = wx.TextCtrl(self, -1,q[1] )
        
        #Genero:Ingreso
        self.genero = wx.StaticText(self, -1, "Genero:")
        self.genero_ingreso = wx.TextCtrl(self, -1, q[2])
        
        #Director:ingreso
        self.director = wx.StaticText(self, -1, "Director:")
        self.director_ingreso = wx.TextCtrl(self, -1, q[3])
        
        #Actor:Ingreso
        self.actor = wx.StaticText(self, -1, "Actor:")
        self.actor_ingreso = wx.TextCtrl(self, -1, q[4])
        
        #Año:Ingreso
        self.anio = wx.StaticText(self, -1, u"Año:")
        self.anio_ingreso = wx.TextCtrl(self, -1, q[5])
        
        #Botones
        self.boton_aceptar = wx.Button(self, -1, "Aceptar")
        self.boton_cancelar = wx.Button(self, -1, "Cancelar")
        self.Bind(wx.EVT_BUTTON, self.OnAceptarBoton, self.boton_aceptar)
        self.Bind(wx.EVT_BUTTON, self.OnCancelarBoton, self.boton_cancelar)
        self.__set_properties()
        self.__do_layout()
        # end wxGlade

    def __set_properties(self):
        # begin wxGlade: Ventana.__set_properties
        self.SetTitle("Peliculas")
        # end wxGlade

    def __do_layout(self):
        # begin wxGlade: Ventana.__do_layout
        grid_sizer_4 = wx.GridSizer(6, 2, 0, 0)
        grid_sizer_4.Add(self.titulo, 0, wx.ALIGN_CENTER_HORIZONTAL, 0)
        grid_sizer_4.Add(self.titulo_ingreso, 0, wx.ALIGN_CENTER_HORIZONTAL, 0)
        grid_sizer_4.Add(self.genero, 0, wx.ALIGN_CENTER_HORIZONTAL, 0)
        grid_sizer_4.Add(self.genero_ingreso, 0, wx.ALIGN_CENTER_HORIZONTAL, 0)
        grid_sizer_4.Add(self.director, 0, wx.ALIGN_CENTER_HORIZONTAL, 0)
        grid_sizer_4.Add(self.director_ingreso, 0, wx.ALIGN_CENTER_HORIZONTAL, 0)
        grid_sizer_4.Add(self.actor, 0, wx.ALIGN_CENTER_HORIZONTAL, 0)
        grid_sizer_4.Add(self.actor_ingreso, 0, wx.ALIGN_CENTER_HORIZONTAL, 0)
        grid_sizer_4.Add(self.anio, 0, wx.ALIGN_CENTER_HORIZONTAL, 0)
        grid_sizer_4.Add(self.anio_ingreso, 0, wx.ALIGN_CENTER_HORIZONTAL, 0)
        grid_sizer_4.Add(self.boton_aceptar, 0, wx.ALIGN_CENTER_HORIZONTAL, 0)
        grid_sizer_4.Add(self.boton_cancelar, 0, wx.ALIGN_CENTER_HORIZONTAL, 0)
        self.SetSizer(grid_sizer_4)
        grid_sizer_4.Fit(self)
        self.Layout()
        # end wxGlade
        
    def OnAceptarBoton(self,event):
        titulo = self.titulo_ingreso.GetValue()
        genero = self.genero_ingreso.GetValue()
        director = self.director_ingreso.GetValue()
        actor = self.actor_ingreso.GetValue()
        anio = self.anio_ingreso.GetValue()
        
        c = self.db.cursor()
        c.execute('''UPDATE tabla_peliculas SET titulo = %s, genero = %s, director = %s, actor = %s, anio = %s
        WHERE id_peliculas = %s''', (titulo, genero, director, actor, anio, self.id_peli))
        c.close()
        
        # Mensaje: Devolver un mensaje con los datos ingresados
        wx.MessageBox (u'\nTítulo: %s \nGénero: %s \nDirector: %s \nActor: %s \nAño: %s' %(titulo, genero, director, actor, anio), u'Datos Ingresados', wx.OK | wx.ICON_INFORMATION, None)
        
     # Cancelar: se cierra la ventana  
    def OnCancelarBoton(self, event):
        self.Close()
            
# end of class Ventana
if __name__ == "__main__":
    app = wx.PySimpleApp(0)
    wx.InitAllImageHandlers()
    ventana = Ventana (None, -1, "")
    app.SetTopWindow(ventana)
    ventana.Show()
    app.MainLoop()
