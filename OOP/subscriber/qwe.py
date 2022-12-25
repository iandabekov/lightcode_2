class Subscriber:
    def __init__(self, id, last_name, first_name, patronymic, address,
                 credit_card_number, debit, credit,
                 local_calls_time, long_distance_calls_time):
        self.id = id
        self.last_name = last_name
        self.first_name = first_name
        self.patronymic = patronymic
        self.address = address
        self.credit_card_number = credit_card_number
        self.debit = debit
        self.credit = credit
        self.local_calls_time = local_calls_time
        self.long_distance_calls_time = long_distance_calls_time

    def set_values(self, id, last_name, first_name, patronymic, address,
                   credit_card_number, debit, credit,
                   local_calls_time, long_distance_calls_time):
        self.id = id
        self.last_name = last_name
        self.first_name = first_name
        self.patronymic = patronymic
        self.address = address
        self.credit_card_number = credit_card_number
        self.debit = debit
        self.credit = credit
        self.local_calls_time = local_calls_time
        self.long_distance_calls_time = long_distance_calls_time

    def get_values(self):
        return (self.id, self.last_name, self.first_name,
                self.patronymic, self.address, self.credit_card_number,
                self.debit, self.credit, self.local_calls_time,
                self.long_distance_calls_time)

    def __str__(self):
        return f"Subscriber(id={self.id}, " \
               f"last_name='{self.last_name}', first_name='{self.first_name}', " \
               f"patronymic='{self.patronymic}', address='{self.address}', " \
               f"credit_card_number='{self.credit_card_number}', " \
               f"debit={self.debit}, credit={self.credit}, " \
               f"local_calls_time={self.local_calls_time}, " \
               f"long_distance_calls_time={self.long_distance_calls_time})"


subscribers = []
# Создание объектов класса Subscriber и добавление их в массив
subscriber1 = Subscriber(1, "Ivanov", "Ivan", "Ivanovich", "Moscow", "1234 5678 9012 3456", 100, 50, 10, 20)
subscribers.append(subscriber1)
subscriber2 = Subscriber(2, "Petrov", "Petr", "Petrovich", "St. Petersburg", "1234 5678 9012 3457", 200, 100, 20, 30)
subscribers.append(subscriber2)
subscriber3 = Subscriber(3, "Sidorov", "Sidor", "Sidorovich", "Novosibirsk", "1234 5678 9012 3458", 300, 150, 30, 0)
subscribers.append(subscriber3)

# Вывод сведений относительно абонентов, у которых время городских переговоров превышает заданное
threshold = 15
print()
print('Вывод сведений относительно абонентов, у которых время городских переговоров превышает заданное')
for subscriber in subscribers:
    if subscriber.local_calls_time > threshold:
        print(subscriber)
print()

# Вывод сведений относительно абонентов, которые пользовались междугородной связью
print('Вывод сведений относительно абонентов, которые пользовались междугородной связью')
for subscriber in subscribers:
    if subscriber.long_distance_calls_time > 0:
        print(subscriber)
print()

# Список абонентов в алфавитном порядке
subscribers.sort(key=lambda subscriber: subscriber.last_name)
print('Список абонентов в алфавитном порядке')
for subscriber in subscribers:
    print(subscriber)
print()
