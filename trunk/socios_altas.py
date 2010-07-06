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
        self.ventana = wx.Frame (parent = None, title = 'Ingreso de Socios', size = (500,400), pos = (300,200))
        panel = wx.Panel (self.ventana, -1)
        
        # Apellido: Ingreso
        t_apellido = wx.StaticText (panel, -1, u'Apellido', pos = (20,25))
        self.ingreso_apellido = wx.TextCtrl (panel, -1, u'', size = (390,30),  pos = (100,20))
        
        # Nombre: Ingreso
        t_nombre = wx.StaticText (panel, -1, u'Nombre', pos = (20,65))
        self.ingreso_nombre = wx.TextCtrl (panel, -1, u'', size = (390,30),  pos = (100,60))
        
        
        # DNI: Ingreso
        t_dni = wx.StaticText (panel, -1, u'DNI', pos = (20,105))
        self.ingreso_dni = wx.TextCtrl (panel, -1, u'', size = (390,30),  pos = (100,100))
        
        # Tel: Ingreso
        t_tel = wx.StaticText (panel, -1, u'Tel', pos = (20,145))
        self.ingreso_tel = wx.TextCtrl (panel, -1, u'', size = (390,30),  pos = (100,140))
        
        # Dirección: Ingreso
        t_calle = wx.StaticText (panel, -1, u'Calle', pos = (20,185))
        self.ingreso_calle = wx.TextCtrl (panel, -1, u'', size = (220,30),  pos = (100,180))
        
        t_numero = wx.StaticText (panel, -1, u'Num', pos = (340,185))
        self.ingreso_numero = wx.TextCtrl (panel, -1, u'', size = (110,30),  pos = (380,180))
        
        # Depto: Ingreso
        t_piso = wx.StaticText (panel, -1, u'Piso', pos = (20,225))
        self.ingreso_piso = wx.TextCtrl (panel, -1, u'', size = (80,30),  pos = (100,220))
        
        t_depto = wx.StaticText (panel, -1, u'Depto', pos = (190,225))
        self.ingreso_depto = wx.TextCtrl (panel, -1, u'', size = (80,30),  pos = (240,220))
        
        t_cp = wx.StaticText (panel, -1, u'CP', pos = (340,225))
        self.ingreso_cp = wx.TextCtrl (panel, -1, u'', size = (110,30),  pos = (380,220))
        
        # Localidad: Ingreso
        t_localidad = wx.StaticText (panel, -1, u'Localidad', pos = (20,265))
        self.ingreso_localidad = wx.TextCtrl (panel, -1, u'', size = (390,30),  pos = (100,260)) 
        
        # Correo: Ingreso
        t_correo = wx.StaticText (panel, -1, u'Correo', pos = (20,305))
        self.ingreso_correo = wx.TextCtrl (panel, -1, u'', size = (390,30),  pos = (100,300))       
        
        # Aceptar/Cancelar: Botones
        b_aceptar = wx.Button (panel, -1, u'Aceptar', size = (-1,-1), pos = (290,360))
        b_cancelar = wx.Button (panel, -1, u'Cancelar', size = (-1,-1), pos = (390,360))
        self.Bind(wx.EVT_BUTTON, self.OnAceptarBoton, b_aceptar)
        self.Bind(wx.EVT_BUTTON, self.OnCancelarBoton, b_cancelar)
        
        self.ventana.Show()
        return True
    
    # Aceptar: guardar los datos en db [tabla_socios] y mostrar un mensaje con los datos ingresados.
    def OnAceptarBoton(self, event):
        
        apellido = self.ingreso_apellido.GetValue()
        nombre = self.ingreso_nombre.GetValue()
        dni = self.ingreso_dni.GetValue()
        dni = str (dni)
        tel = self.ingreso_tel.GetValue()
        tel = str (tel)
        calle = self.ingreso_calle.GetValue()
        numero = self.ingreso_numero.GetValue()
        numero = str (numero)
        piso = self.ingreso_piso.GetValue()
        piso = str (piso)
        depto = self.ingreso_depto.GetValue()
        depto = str (depto)
        cp = self.ingreso_cp.GetValue()
        cp = str (cp)
        localidad = self.ingreso_localidad.GetValue()
        correo = self.ingreso_correo.GetValue()
        correo = str (correo)
        
        pass
        c = self.db.cursor()
        c.execute('''INSERT INTO tabla_socios (Apellido, Nombre, Dni, 
        Tel, Calle, Num, Piso, dep, Cp, localidad, correo) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)''' , (apellido, nombre, dni, tel, calle, numero, piso, depto, cp, localidad, correo))
        c.close()
        
       
        # Borrar: Volver a ventana en blanco.
        apellido = self.ingreso_apellido.SetValue('')
        nombre = self.ingreso_nombre.SetValue('')
        dni = self.ingreso_dni.SetValue('')
        tel = self.ingreso_tel.SetValue('')
        calle = self.ingreso_calle.SetValue('')
        numero = self.ingreso_numero.SetValue('')
        piso = self.ingreso_piso.SetValue('')
        depto = self.ingreso_depto.SetValue('')
        cp = self.ingreso_cp.SetValue('')
        localidad = self.ingreso_localidad.SetValue('')
        correo = self.ingreso_correo.SetValue('')
        
    # Cancelar: se cierra la ventana        
    def OnCancelarBoton(self, event):
        self.ventana.Destroy()
            
        
programa = Ventana()
programa.MainLoop() 


        

