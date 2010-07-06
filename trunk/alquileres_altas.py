#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import wx
import MySQLdb

# Genero una ventana
class Ventana (wx.App):
    def OnInit(self):
        
        self.db = MySQLdb.connect('localhost', 'yanina', 'yanina', 'yanina', charset='UTF8')
        
        # Panel donde se apolla los widgets
        self.ventana = wx.Frame (parent = None, title = 'Alquileres', size = (500,300), pos = (300,200))
        panel = wx.Panel (self.ventana, -1)
        
        # Id_peliculas: Ingreso
        pelicula = wx.StaticText (panel, -1, u'Pelicula', pos = (20,25))
        self.ingreso_pelicula = wx.TextCtrl (panel, -1, u'', size = (390,30),  pos = (100,20))
        
        # Id_socio: Ingreso
        socio = wx.StaticText (panel, -1, u'Socio', pos = (20,65))
        self.ingreso_socio = wx.TextCtrl (panel, -1, u'', size = (390,30),  pos = (100,60))
        
        
        # Fecha de retiro: Ingreso
        fecha_retiro= wx.StaticText (panel, -1, u'Retiro', pos = (20,105))
        self.ingreso_fecha_retiro = wx.DatePickerCtrl(panel, size = (390,30),  pos = (100,100))
        
        # Fecha Devolución: Ingreso
        fecha_devolucion = wx.StaticText (panel, -1, u'Devolución', pos = (20,145))
        self.ingreso_fecha_devolucion = wx.DatePickerCtrl(panel, size = (390,30),  pos = (100,140))
        
        # Aceptar/Cancelar: Botones
        b_aceptar = wx.Button (panel, -1, u'Aceptar', size = (-1,-1), pos = (290,260))
        b_cancelar = wx.Button (panel, -1, u'Cancelar', size = (-1,-1), pos = (390,260))
        self.Bind(wx.EVT_BUTTON, self.OnAceptarBoton, b_aceptar)
        self.Bind(wx.EVT_BUTTON, self.OnCancelarBoton, b_cancelar)
        
        self.ventana.Show()
        return True
    
    # Aceptar: guardar los datos en db [tabla_socios] y mostrar un mensaje con los datos ingresados.
    def OnAceptarBoton(self, event):
        
        pelicula = self.ingreso_pelicula.GetValue()
        socio = self.ingreso_socio.GetValue()
        fr = self.ingreso_fecha_retiro.GetValue()
        fr = str (fr)
        fd = self.ingreso_fecha_devolucion.GetValue()
        fd = str (fd)
        
        c = self.db.cursor()
        c.execute('''INSERT INTO tabla_alquileres (pelicula, socio, fr,
        fd) VALUES (%s, %s, %s, %s)''' , (pelicula, socio, fr, fd))
        c.close()
                     
        # Borrar: Volver a ventana en blanco.
        pelicula = self.ingreso_pelicula.SetValue('')
        socio = self.ingreso_socio.SetValue('')
        fecha_retiro = self.ingreso_fecha_retiro.SetValue('')
        fecha_devolucion = self.ingreso_fecha_devolucion.SetValue('')
        
    # Cancelar: se cierra la ventana        
    def OnCancelarBoton(self, event):
        self.ventana.Destroy()
            
        
programa = Ventana()
programa.MainLoop() 


        

