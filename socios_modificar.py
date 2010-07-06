#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import wx
import MySQLdb

class Ventana (wx.App):
    def OnInit(self):
        
        self.db = MySQLdb.connect('localhost', 'martin', 'martin', 'martin', charset='UTF8')
        
        # Panel donde se apolla los widgets
        self.ventana = wx.Frame (parent = None, title = 'Modificar socios', size = (500,200), pos = (300,200))
        panel = wx.Panel (self.ventana, -1)
        
        # titulo: Ingreso
        titulo = wx.StaticText (panel, -1, u'N. socio', pos = (20,25))
        self.ingreso_titulo = wx.TextCtrl (panel, -1, u'', size = (390,30),  pos = (100,20))
        
        # Aceptar/Cancelar: Botones
        b_aceptar = wx.Button (panel, -1, u'Aceptar', size = (-1,-1), pos = (290,160))
        b_cancelar = wx.Button (panel, -1, u'Cancelar', size = (-1,-1), pos = (390,160))
        self.Bind(wx.EVT_BUTTON, self.OnAceptarBoton, b_aceptar)
        self.Bind(wx.EVT_BUTTON, self.OnCancelarBoton, b_cancelar)
        
        self.ventana.Show()
        return True
    
    # Aceptar: guardar los datos en db [tabla_peliculas] y mostrar un mensaje con los datos ingresados.
    def OnAceptarBoton(self, event):
        c = self.db.cursor()
        c.execute('''UPDATE socios SET 
        titulo = %s''',(titulo, self.ingreso_titulo))
        c.close()
        
    #Cancelar: se cierra la ventana        
    def OnCancelarBoton(self, event):
        self.ventana.Destroy()
            
        
programa = Ventana()
programa.MainLoop() 

