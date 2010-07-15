#!/usr/bin/env python
# -*- coding: utf-8 -*-
# generated by wxGlade 0.6.3 on Thu Jul  8 14:35:04 2010

import os
import wx
import MySQLdb

# begin wxGlade: extracode
# end wxGlade



class Ventana(wx.Frame):
    def __init__(self, *args, **kwds):
        self.db = MySQLdb.connect('localhost', 'yanina', 'yanina', 'yanina', charset='UTF8')
        # begin wxGlade: Ventana.__init__
        kwds["style"] = wx.DEFAULT_FRAME_STYLE
        wx.Frame.__init__(self, *args, **kwds)
        self.panel_1 = wx.Panel(self, -1)
        
        #Titulo:Ingreso
        self.apellido = wx.StaticText(self.panel_1, -1, "Apellido:")
        self.apellido_ingreso = wx.TextCtrl(self.panel_1, -1, "")
        
        #Botones:
        self.boton_aceptar = wx.Button(self.panel_1, -1, "Aceptar")
        self.boton_cancelar = wx.Button(self.panel_1, -1, "Cancelar")
        self.Bind(wx.EVT_BUTTON, self.OnAceptarBoton, self.boton_aceptar)
        self.Bind(wx.EVT_BUTTON, self.OnCancelarBoton, self.boton_cancelar)

        self.__set_properties()
        self.__do_layout()
        # end wxGlade

    def __set_properties(self):
        # begin wxGlade: Ventana.__set_properties
        self.SetTitle("Modificar Socios")
        # end wxGlade

    def __do_layout(self):
        # begin wxGlade: Ventana.__do_layout
        sizer_1 = wx.BoxSizer(wx.VERTICAL)
        grid_sizer_1 = wx.GridSizer(2, 2, 0, 0)
        grid_sizer_1.Add(self.apellido, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 0)
        grid_sizer_1.Add(self.apellido_ingreso, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 0)
        grid_sizer_1.Add(self.boton_aceptar, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 0)
        grid_sizer_1.Add(self.boton_cancelar, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 0)
        self.panel_1.SetSizer(grid_sizer_1)
        sizer_1.Add(self.panel_1, 1, wx.EXPAND, 0)
        self.SetSizer(sizer_1)
        sizer_1.Fit(self)
        self.Layout()
        # end wxGlade
    def OnAceptarBoton(self, event):
        # Selccionar título e id de la tabla_peliculas en db.
        apellido_buscar = self.apellido_ingreso.GetValue()

        # Selccionar título e id de la tabla_peliculas en db.
        c = self.db.cursor()
        c.execute('''SELECT id_socios, apellido FROM tabla_socios WHERE apellido = %s''', (apellido_buscar))
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
            id_socios = str(registro[0])
                #Traigo los datos de la peli seleccionada
            c = self.db.cursor()
            c.execute('''SELECT apellido, nombre, dni, tel, calle, num, piso, dep, Cp, localidad, correo
            FROM tabla_socios WHERE id_socios = %s''', (id_socios))
            q = c.fetchone()
            c.close()
            
  
        
            #importo ventana            
            import socios_altas_hacia
            ventana = socios_altas_hacia.Ventana(id_socios, None, -1, '')
            ventana.CenterOnScreen()
            ventana.Show(True)
            
            
            
    def OnCancelarBoton(self, event):
        self.Close()
# end of class Ventana


if __name__ == "__main__":
    app = wx.PySimpleApp(0)
    wx.InitAllImageHandlers()
    ventana = Ventana(None, -1, "")
    app.SetTopWindow(ventana)
    ventana.Show()
    app.MainLoop()
