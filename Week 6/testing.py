with open("census.txt") as file_in:
    print(f'file_in: {file_in}')
    
    for line in file_in:
        fields = line.split(",")


        print(f'line: {line}')
        print(f'fields: {fields}')
        print(f'fields[3]: {fields[3]}')