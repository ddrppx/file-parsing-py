import os

path = input('Insira o caminho do arquivo: ')

file_status = os.path.isfile(path)

if(file_status):
        # Arrays for storing data
    contents = []
        # Opening the filed  
    with open(path) as f:
        contents = f.readlines()

    count = 0
    output = []
        # Going through file contents
    for content in contents:
        count += 1
            # Splitting values for another array loop
        splitted = content.split()
        for index in splitted:
                # searching for arrows in array string
            search = index.find('->')
                # >= because it returns position of, -1 for "false"
            if (search >= 0):
                output = index
                print(f'{count}: {output}')
else:
    print(f'File not found.\nCheck the inserted path: {path}')
