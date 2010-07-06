#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import wx
import MySQLdb

class Ventana (wx.App):
    def OnInit(self):
        
        self.db = MySQLdb.connect('localhost', 'yanina', 'yanina', 'yanina', charset='UTF8')
        
        # Panel donde se apolla los widgets
        self.ventana = wx.Frame (parent = None, title = 'Listado de Películas', size = (500,400), pos = (300,200))
        panel = wx.Panel (self.ventana, -1)
        
        # titulo: Ingreso
        t_titulo = wx.StaticText (panel, -1, u'Título', pos = (20,25))
        self.ingreso_titulo = wx.TextCtrl (panel, -1, u'', size = (390,30),  pos = (100,20))
        
        # Genero: Desplegable
        t_genero = wx.StaticText (panel, -1, u'Género', pos = (20,65))
        ingreso_genero = ['Drama', 'Acción', 'Comedia', 'Terror', 'Suspenso', 'Ciencia Ficción', 'Bélica', 'Catástrofe', 'Infantil', 'Fantasía', 'Serie', 'Documental']
        self.d_genero = wx.ComboBox (panel, -1, u'', (100,60) , (390,30), ingreso_genero, wx.CB_DROPDOWN|wx.CB_READONLY)
        
        
        # Director: Ingreso
        t_director = wx.StaticText (panel, -1, u'Director', pos = (20,105))
        self.ingreso_director = wx.TextCtrl (panel, -1, u'', size = (390,30),  pos = (100,100))
        
        # Actuaciones: Ingreso
        t_actor = wx.StaticText (panel, -1, u'Actores', pos = (20,145))
        self.ingreso_actor = wx.TextCtrl (panel, -1, u'', size = (390,30),  pos = (100,140))
        
        # Año: Ingreso
        t_anio = wx.StaticText (panel, -1, u'Año', pos = (20,185))
        self.ingreso_anio = wx.TextCtrl (panel, -1, u'', size = (390,30),  pos = (100,180))
        
        # Aceptar/Cancelar: Botones
        b_aceptar = wx.Button (panel, -1, u'Aceptar', size = (-1,-1), pos = (290,360))
        b_cancelar = wx.Button (panel, -1, u'Cancelar', size = (-1,-1), pos = (390,360))
        self.Bind(wx.EVT_BUTTON, self.OnAceptarBoton, b_aceptar)
        self.Bind(wx.EVT_BUTTON, self.OnCancelarBoton, b_cancelar)
        
        self.ventana.Show()
        return True
    
    # Aceptar: guardar los datos en db [tabla_peliculas] y mostrar un mensaje con los datos ingresados.
    def OnAceptarBoton(self, event):
        
        titulo = self.ingreso_titulo.GetValue()
        genero = self.d_genero.GetValue()
        director = self.ingreso_director.GetValue()
        actor = self.ingreso_actor.GetValue()
        anio = self.ingreso_anio.GetValue()
                
        c = self.db.cursor()
        c.execute('''INSERT INTO tabla_peliculas (titulo, genero, director, 
        actor, anio) VALUES (%s, %s, %s, %s, %s)''' , (titulo, genero, director, 
        actor, anio))
        c.close()
        
              
        # Borrar: Volver a ventana en blanco.
        titulo = self.ingreso_titulo.SetValue('')
        genero = self.d_genero.SetValue('')
        director = self.ingreso_director.SetValue('')
        actor = self.ingreso_actor.SetValue('')
        anio = self.ingreso_anio.SetValue('')
        
        
    # Cancelar: se cierra la ventana        
    def OnCancelarBoton(self, event):
        self.ventana.Destroy()
            
        
programa = Ventana()
programa.MainLoop() 


        

