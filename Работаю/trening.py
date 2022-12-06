documents = [
 {'type': 'passport', 'number': '2207 876234', 'name': 'Василий Гупкин'},
 {'type': 'invoice', 'number': '11-2', 'name': 'Геннадий Покемонов'},
 {'type': 'insurance', 'number': '10006', 'name': 'Аристарх Павлов'}
]
directories = {
 '1': ['2207 876234', '11-2'],
 '2': ['10006'],
 '3': []
}
f = input()
all_numbers = []
def traffic() :
    all_numbers = []
    for idx in range(len(documents)):
        values = list(documents[idx].values())
        all_numbers.append(values[1])
if type(f)