data = {'1': 'S001',
        '2': 'S002',
        '3': 'S001',
        '4': 'S005',
        '5': 'S005',
        '6': 'S009',
        '7': 'S007'}

print(set([value for key,value in data.items()]))