import PySimpleGUI as sg


sg.theme('BlueMono')
layout = [ [sg.Text("¿Cual es tu Nombre?")],
            [sg.Input()],
            [sg.Button('OK')]]

windows = sg.Window('Ventana de prueba', layout)

event, values = windows.read()

print('Hola', values[0], "usando entorno grafico")

windows.close()
