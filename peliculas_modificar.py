#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import wx
import MySQLdb

class Ventana (wx.App):
    def OnInit(self):
        
        self.db = MySQLdb.connect('localhost', 'yanina', 'yanina', 'yanina', charset='UTF8')
        
        # Panel donde se apolla los widgets
        self.ventana = wx.Frame (parent = None, title = 'Modificar Películas', size = (500,200), pos = (300,200))
        panel = wx.Panel (self.ventana, -1)
        
        # titulo: Ingreso
        titulo = wx.StaticText (panel, -1, u'T. Pelicula', pos = (20,25))
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
        # Selccionar título e id de la tabla_peliculas en db.
        titulo_buscar = self.ingreso_titulo.GetValue()

        # Selccionar título e id de la tabla_peliculas en db.
        c = self.db.cursor()
        c.execute('''SELECT id_peliculas, titulo FROM tabla_peliculas WHERE titulo = %s''', (titulo_buscar))
        q = c.fetchall()
        c.close()
        
                
        # Generar una lista donde se guardan los elementos solicitados anteriormente
        lista = []
        for elemento in q:
            lista.append(str (elemento[0]) + ' - ' + (elemento[1]))
                
        # Ventana donde se muestran los datos pedidos.
        dlg = wx.SingleChoiceDialog(None, 'Elija el Id a modificar', 'Modificar', lista, wx.CHOICEDLG_STYLE)
        if dlg.ShowModal() == wx.ID_OK:
            modificar = dlg.GetStringSelection()
            # separar la cadena
            registro = modificar.split('-')
            id_peli = str(registro[0])
                #Traigo los datos de la peli seleccionada
            c = self.db.cursor()
            c.execute('''SELECT titulo, genero, director, actor, anio FROM tabla_peliculas WHERE id_peliculas = %s''', (id_peli))
            q = c.fetchone()
            c.close()
            
  
        
            #importo ventana            
            import peliculas_altas
            ventana = peliculas_altas.Ventana(etiqueta, None, -1, '')
            ventana.CenterOnScreen()
            ventana.show(True)
       
                    
                
        
    # Cancelar: se cierra la ventana        
    def OnCancelarBoton(self, event):
        self.ventana.Destroy()
            
        
programa = Ventana()
programa.MainLoop() 


        

