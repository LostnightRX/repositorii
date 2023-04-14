import PySimpleGUI as sg

sg.theme('LightBlue2')  # Set the theme

s=['1','2','3']
a=[
'''
for y in range():
    print('')''',
'''
for x in range():
    print('')''',
'''
for z in range():
    print('')'''
]
# Define the layout
layout = [[sg.Combo(s, default_value=s[0], s=(15,22), enable_events=True, readonly=True, k='-COMBO-', key='Combo'),
          sg.Output(s=(40,10), key='outputt')],
          [sg.Button('вывод', font=('Consolas', 12), button_color=('white', '#4CAF50'), key='process'),
           sg.Button('сбежать', font=('Consolas', 12), button_color=('white', '#4CAF50'), key='exit')]]

# Create the window
window = sg.Window('это говно сделано мной(аноним) v1.0', layout)

# Event loop
while True:
    event, values = window.read()

    # Exit the app when the window is closed
    if event == sg.WINDOW_CLOSED:
        break

    # Process the input and update the output when the button is clicked
    if event == 'process':
        choice=a[int(values['Combo'])-1]
        #print(choice)
        #window['outputt'].update('')
        window['outputt'].update(choice)
    if event == 'exit':
        break

# Close the window
window.close()
