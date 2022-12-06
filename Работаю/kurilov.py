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
def traffic() :
    for idx in range(len(documents)):
        values = list(documents[idx].values())
        all_numbers.append(values[1])
def determine(doc_number: str) :
    if doc_number in all_numbers:
        for idx in range(len(documents)):
            values = list(documents[idx].values())
            if doc_number in values:
                return print("Владелец документа: ", values[2])
    else:
        return print('Документ не найден в базе')
while True:
    command = input("Введите команду: ")
    if command == "p":
        doc_number = input("Введите номер документа: ")
        all_numbers = []
        traffic()
        determine(doc_number)







