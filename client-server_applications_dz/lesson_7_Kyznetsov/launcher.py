import subprocess



PROCESS = []

while True:
    ACTION = input(
            'Выберите действие: '
            'q - выход, '
            's - запустить сервер и клиенты, '
            'x - закрыть все окна\n>>> '
    )

    
    if ACTION == 'q':
        break

    elif ACTION == 's':
        PROCESS.append(
            subprocess.Popen(
                'python server.py',
                shell = True
            )
        )
        
        PROCESS.append(
            subprocess.Popen(
                'python client.py -m send',
                shell=True
                # creationflags = subprocess.CREATE_NEW_CONSOLE
                # Конструкция корректна только для windows
            )
        )
        
        PROCESS.append(
            subprocess.Popen(
                'python client.py -m listen',
                shell=True
                # creationflags = subprocess.CREATE_NEW_CONSOLE
            )
        )
    
    elif ACTION == 'x':
        while PROCESS:
            PROCESS.pop().kill()
