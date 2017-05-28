#!/usr/bin/python
#-*- coding: latin-1 -*-
import wx

ListProc = [3 * 1]
class panelProcedimientos(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent)
        self.quote = wx.StaticText(self, label="integrantes: \n Erik López - 1430406 \n Camilo Jose Cruz - ... \n Robert Quiceno -...", pos=(10, 10))

        self.logger = wx.TextCtrl(self, pos=(300,20), size=(400,350), style=wx.TE_MULTILINE | wx.TE_READONLY)

        self.buttonOk =wx.Button(self, label="OK", pos=(240, 100), size = (50, 30))
        self.Bind(wx.EVT_BUTTON, self.CLickOk, self.buttonOk)

        self.lblnum = wx.StaticText(self, label="Numero de procedimientos :", pos=(10,100))
        self.numProc = wx.TextCtrl(self, value="", pos=(195, 100), size=(40,-1))

        self.lblproc = wx.StaticText(self, label="Procedimiento # :", pos=(95, 140))

        self.lblnomproc = wx.StaticText(self, label = 'nombre: ', pos = (10, 160))
        self.nomProc = wx.TextCtrl(self, value = '', pos = (10, 180), size = (120, -1))
        self.lblhoraini = wx.StaticText(self, label = 'Hora inicio: ', pos = (135, 160))
        self.horaini = wx.TextCtrl(self, value = '', pos = (135, 180), size = (75, -1))
        self.lblhorafin = wx.StaticText(self, label = 'Hora fin: ', pos = (220, 160))
        self.horafin = wx.TextCtrl(self, value = '', pos = (220, 180), size = (75, -1))

        self.buttonAgg = wx.Button(self, label = 'añadir', pos = (110, 210), size = (75, -1))

        self.burronInge = wx.Button(self, label = 'Solucion Ingenua o Exhaustiva', pos = (45, 260))
        self.burronInge = wx.Button(self, label = 'Solucion Voraz', pos = (95, 290))
        self.burronInge = wx.Button(self, label = 'Solucion dinámica', pos = (85, 320))

    def CLickOk(self,event):
        numeroProcedimientos = int(self.numProc.GetValue())
        ListProc = [range(3) for i in range(numeroProcedimientos)]
        self.logger.SetValue("numero de procedimientos: " + str(numeroProcedimientos) + '\n')
        infoProc = '[nomre_proc] \t [hora_ini] \t [hora_fin] \n'
        for i in range(numeroProcedimientos):
            for j in range(3):
                #ListProc[i][j] = i*j
                infoProc += str(ListProc[i][j]) +'\t'
            infoProc += '\n'
        self.logger.AppendText(infoProc)
        self.lblproc.SetLabel('Procedimiento 0: ')

    def EvtText(self, event):
        self.logger.AppendText('Evento de texto: ' + event.GetString() + '\n')

class panelLibros(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent)
        self.control = wx.TextCtrl(self, style=wx.TE_MULTILINE)

        # Creamos un sizer para ocupar todo el tamaño
        self.sizer = wx.BoxSizer(wx.HORIZONTAL)
        self.sizer.Add(self.control,1, wx.EXPAND)
        self.SetSizer(self.sizer)


app = wx.App(False)
# Creamos el frame padre
frame = wx.Frame(None, title="Proyecto de FADA", size=(710,440))
# Creamos el contenedor de pestañas
nb = wx.Notebook(frame)
# Añadimos los paneles con Addpage
nb.AddPage(panelProcedimientos(nb), "Sala operaciones")
nb.AddPage(panelLibros(nb), "Copia de libros")
frame.Show()
app.MainLoop()
