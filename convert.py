import PySimpleGUI as sg

layout = [
    [sg.Text('Numeric Converter')],
    [sg.Input(key = '-INPUT_FIELD-'), sg.Spin(['binary to decimal','decimal to binary'],key = '-CONVERSION_SELECTOR-')],
    [sg.Button('Convert', key="-CONVERT_BUTTON-"), sg.Text(' [ Value Field ]', key='-VALUE_FIELD-')]
]

window = sg.Window('Converter Application', layout)

def binToDec(val):
    converted_value = 0
    error_message = '[ something doesn\'t seem right with your input ]'
    # increment power 
    counter = 0
    # splits string input into a list by character
    checker = [val for val in val]
    condition = True
    # if input is blank return error
    if val == '':
        return error_message
    # checks if each element in checker is 0 or 1
    for x in checker:
        if x != '0' and x != '1':
            condition = False

    # if input is only 1's and 0's we convert from binary to decimal   
    if condition == True:
        val = int(val)
        while val != 0:
            digit = val % 10
            converted_value = converted_value + (digit * pow(2,counter))
            counter += 1
            val = val//10
    
    # if there is something wrong with input, we throw an error message
    else:
        converted_value = error_message

    # returns converted value or error message
    return converted_value

def decToBin(val):
    converted_value = ''
    error_message = '[ something doesn\'t seem right with your input ]'

    # return error message if inputed value is empty
    if val == '':
        return error_message
    
    # if input value is only numbers, we can continue with code
    if val.isnumeric():
        val = int(val)
        while val != 0:
            digit = val % 2
            converted_value = str(digit) + converted_value
            val = val // 2
    else:
        return error_message
    
    return converted_value


while True:
    event, values = window.read()

    if event == sg.WIN_CLOSED:
        break

    if event == '-CONVERT_BUTTON-':
        # val holds value in the input field
        val = values['-INPUT_FIELD-']
        if values['-CONVERSION_SELECTOR-'] == 'binary to decimal':
            # call our binary to decimal method
            converted_value = binToDec(val)
        elif values['-CONVERSION_SELECTOR-'] == 'decimal to binary':
            converted_value = decToBin(val)

        window['-VALUE_FIELD-'].update(converted_value)

window.close()