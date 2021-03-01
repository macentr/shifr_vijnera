import PySimpleGUI as sg  
import cod     

#для эстетики 
sg.theme('DarkAmber') 

#вызов статичного окна
layout = [[sg.Text('Впишите слово')],      
          [sg.Input(key='-IN-')],
          [sg.Text('Впишите ключ')],
          [sg.Input(key='-IN1-')],
          [sg.Text('Шифр')],
          [sg.Output( key='-OUTPUT-')],  
          [sg.Button('Шифровать'), sg.Exit()]]      

window = sg.Window('Шифратор', layout)      

while True:                             # The Event Loop
    event, values = window.read() 
    word1 = values['-IN-']
    word = str(word1).lower()
    key1 = values['-IN1-']
    key = str(key1).lower()
    key_encoded = cod.encode_val(key)
    value_encoded = cod.encode_val(word) 
    shifre = cod.full_encode(value_encoded, key_encoded)
    print (''.join(cod.decode_val(shifre)))
    

    if event == sg.WIN_CLOSED or event == 'Выход':
        break      

window.close()