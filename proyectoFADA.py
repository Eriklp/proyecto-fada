#!/usr/bin/python
#-*- coding: utf-8 -*-
import wx
import time

np = 0
numeroProcedimientos = 0
ListProc = []
def HorasAminutos(hora, minutos):
    resultado = (hora * 60) + minutos
    return resultado
def cruzan(proc1, proc2):
    minHIproc1 = HorasAminutos(proc1[1].tm_hour, proc1[1].tm_min)
    minHFproc1 = HorasAminutos(proc1[2].tm_hour, proc1[2].tm_min)
    minHIproc2 = HorasAminutos(proc2[1].tm_hour, proc2[1].tm_min)
    minHFproc2 = HorasAminutos(proc2[2].tm_hour, proc2[2].tm_min)
    var = False
    if minHFproc1 > minHIproc2:
        var = True
    elif minHIproc2 < minHFproc1:
        var = True
    else:
        var = False
    return var
class panelProcedimientos(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent)
        self.quote = wx.StaticText(self, label="integrantes: \n Erik López - 1430406 \n Camilo Jose Cruz - 1428907 \n Robert Quiceno -...", pos=(10, 10))

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
        self.Bind(wx.EVT_BUTTON, self.ClickAnadir, self.buttonAgg)

        self.buttonInge = wx.Button(self, label = 'Solucion Ingenua o Exhaustiva', pos = (45, 260))
        self.Bind(wx.EVT_BUTTON, self.ClickIngenuo, self.buttonInge)
        self.buttonInge.Disable()
        self.buttonVor = wx.Button(self, label = 'Solucion Voraz', pos = (95, 290))
        self.Bind(wx.EVT_BUTTON, self.CLickVoraz, self.buttonVor)
        self.buttonVor.Disable()
        self.buttonDim = wx.Button(self, label = 'Solucion Dinámica', pos = (85, 320))
        self.Bind(wx.EVT_BUTTON, self.ClickDinamico, self.buttonDim)
        self.buttonDim.Disable()

        #parte de abrir archivos ¬¬
        self.buttonArchivo = wx.Button(self, label = 'archivo', pos = (8, 132))
        self.Bind(wx.EVT_BUTTON, self.ClickArchivo, self.buttonArchivo)
        #fin de parte de abrir archivo ¬¬
    def ClickArchivo(self, event):
        archivo = open("procedimientos.txt", "r")
        linea1 = archivo.readline()
        global numeroProcedimientos
        numeroProcedimientos = int(linea1)
        lineas = archivo.readlines()
        global ListProc
        for i  in range(0, len(lineas), 1):
            lin = lineas[i].split(' ')
            ListProc.append(lin)
        for i in range(numeroProcedimientos):
            ListProc[i][2] = ListProc[i][2].replace('\n', '')
        for i in range(numeroProcedimientos):
            for j in range(1, 3):
                ListProc[i][j] = time.strptime(ListProc[i][j], "%H:%M")
        self.buttonInge.Enable()
        self.buttonVor.Enable()
        self.buttonDim.Enable()
        self.buttonAgg.Disable()
        self.buttonOk.Disable()
        self.numProc.SetValue(str(numeroProcedimientos))
        self.numProc.SetEditable(False)
        self.numProc.Disable()
    def CLickOk(self,event):
        global numeroProcedimientos
        numeroProcedimientos = int(self.numProc.GetValue())
        global ListProc
        ListProc = [range(3) for i in range(numeroProcedimientos)]
        self.logger.SetValue("numero de procedimientos: " + str(numeroProcedimientos) + '\n')
        self.lblproc.SetLabel('Procedimiento: 0')
        self.numProc.SetEditable(False)
    def ClickAnadir(self, event):
        global numeroProcedimientos
        global np
        if np < numeroProcedimientos:
            nombre_tem = self.nomProc.GetValue()
            horain_tem = time.strptime(self.horaini.GetValue(), "%H:%M")
            horafin_tem = time.strptime(self.horafin.GetValue(), "%H:%M")
            ListProc[np][0] = str(nombre_tem)
            ListProc[np][1] = horain_tem
            ListProc[np][2] = horafin_tem
            self.logger.SetValue('Se añadio el procedimiento: ' + ListProc[np][0] + '\nhora inicio: ' + str(ListProc[np][1].tm_hour) +':'+str(ListProc[np][1].tm_min) + '\nhora fin : ' + str(ListProc[np][2].tm_hour) + ':' + str(ListProc[np][1].tm_min) +'\n' )
            infoProc = '[nombre_proc] \t [hora_ini] \t [hora_fin] \n'
            for i in range(np + 1):
                for j in range(3):
                    if j == 0:
                        infoProc += str(ListProc[i][j]) +'                      \t'
                    else:
                        infoProc += str(ListProc[i][j].tm_hour) + ':' + str(ListProc[i][j].tm_min) +'             \t'

                infoProc += '\n'
            self.logger.AppendText(infoProc)
            self.nomProc.SetValue('')
            self.horaini.SetValue('')
            self.horafin.SetValue('')
            np += 1
            if np != numeroProcedimientos:
                self.lblproc.SetLabel('Procedimiento: ' + str(np))
            elif np == numeroProcedimientos:
                msj = wx.MessageDialog(self, 'ya lleno todos los procedimientos!', 'Proyecto', style = wx.OK)
                msj.ShowModal()
                self.lblproc.SetLabel('Procedimientos: ' + str(numeroProcedimientos))
                self.nomProc.SetEditable(False)
                self.horaini.SetEditable(False)
                self.horafin.SetEditable(False)
                self.buttonAgg.Disable()
                self.buttonOk.Disable()
                self.buttonInge.Enable()
                self.buttonVor.Enable()
                self.buttonDim.Enable()
    def ClickIngenuo(self, event):
        self.logger.SetValue('solucion ingenua: \n')
        infoProc = '[nombre_proc] \t [hora_ini] \t [hora_fin] \n'
        for i in range(numeroProcedimientos):
            for j in range(3):
                if j == 0:
                    infoProc += str(ListProc[i][j]) +'                      \t'
                else:
                    infoProc += str(ListProc[i][j].tm_hour) + ':' + str(ListProc[i][j].tm_min) +'             \t'
            infoProc += '\n'
        self.logger.AppendText(infoProc)
        listaDePesos = []
        for i in range(numeroProcedimientos):
            peso = HorasAminutos(ListProc[i][2].tm_hour, ListProc[i][2].tm_min) - HorasAminutos(ListProc[i][1].tm_hour, ListProc[i][1].tm_min)
            listaDePesos.append(peso)
        print(listaDePesos)
        ProcedimientosARealizar = []
        sum = 0
        maxx = 0
        while sum < 1440:
            if sum == 0:
                maxx = max(listaDePesos)
                ind = listaDePesos.index(maxx)
                ProcedimientosARealizar.append(ListProc[ind])
                ListProc.remove(ListProc[ind])
                listaDePesos.remove(maxx)
                sum = sum + maxx
            else:
                print(str(sum) + "else")
                maxx = max(listaDePesos)
                ind = listaDePesos.index(maxx)
                if not cruzan(ListProc[ind], ProcedimientosARealizar[len(ProcedimientosARealizar) - 1]):
                    print(str(sum) + "if not")
                    ProcedimientosARealizar.append(ListProc[ind])
                    ListProc.remove(ListProc[ind])
                    listaDePesos.remove(maxx)
                    sum = sum + maxx
                listaDePesos.remove(maxx)

            #print(HorasAminutos(ProcedimientosARealizar[i][1].tm_hour, ProcedimientosARealizar[i][1].tm_min))
        info = '[nombre_proc] \t [hora_ini] \t [hora_fin] \n'
        for i in range(len(ProcedimientosARealizar)):
            for j in range(3):
                if j == 0:
                    info += str(ProcedimientosARealizar[i][j]) +'                      \t'
                else:
                    info += str(ProcedimientosARealizar[i][j].tm_hour) + ':' + str(ProcedimientosARealizar[i][j].tm_min) +'             \t'
            info += '\n'
        self.logger.AppendText(info)
    def CLickVoraz(self, event):
        self.logger.SetValue('Hola, aqui va la solucion voraz del problema')
    def ClickDinamico(self,event):
        self.logger.SetValue('Hola, aqui va la solucion dinamica del problema')

class panelLibros(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent)

        self.logger = wx.TextCtrl(self, pos=(260,20), size=(450,400), style=wx.TE_MULTILINE | wx.TE_READONLY)

        self.buttonCargar =wx.Button(self, label="Cargar Archivo", pos=(20, 20), size = (120, 30))
        self.Bind(wx.EVT_BUTTON, self.ClickCargar, self.buttonCargar)

	self.buttonInge = wx.Button(self, label = 'Solucion Ingenua o Exhaustiva', pos = (45, 260))
        self.Bind(wx.EVT_BUTTON, self.ClickIngenuo, self.buttonInge)
        self.buttonInge.Disable()
        self.buttonVor = wx.Button(self, label = 'Solucion Voraz', pos = (95, 300))
        self.Bind(wx.EVT_BUTTON, self.CLickVoraz, self.buttonVor)
        self.buttonVor.Disable()
        self.buttonDim = wx.Button(self, label = 'Solucion Dinámica', pos = (85, 340))
        self.Bind(wx.EVT_BUTTON, self.ClickDinamico, self.buttonDim)
        self.buttonDim.Disable()


    def ClickIngenuo(self,event):
	self.logger.SetValue('Se mostrara la solucion ingenua del problema')
    def CLickVoraz(self,event):
	self.logger.SetValue('Se mostrara la solucion voraz del problema')
    def ClickDinamico(self,event):
	self.logger.SetValue('Se mostrara la solucion dinamica del problema')


    def ClickCargar(self,event):
	self.logger.SetValue('Se mostrara la informacion del archivo')
	self.buttonInge.Enable()
	self.buttonVor.Enable()
	self.buttonDim.Enable()




app = wx.App(False)
# Creamos el frame padre
frame = wx.Frame(None, title="Proyecto de FADA", size=(780,520))
# Creamos el contenedor de pestañas
nb = wx.Notebook(frame)
# Añadimos los paneles con Addpage
nb.AddPage(panelLibros(nb), "Copia de libros")
nb.AddPage(panelProcedimientos(nb), "Sala operaciones")

frame.Show()
app.MainLoop()
