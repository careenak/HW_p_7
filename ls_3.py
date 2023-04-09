class Worker:

    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": wage, "bonus": bonus}


class Position(Worker):

    def __init__(self,  name, surname, position, wage, bonus):
        super().__init__(name, surname, position, wage, bonus)

    def get_full_name(self):
        return f'ФИО: {self.surname} {self.name}'

    def get_total_income(self):
        return sum(self._income.values())


if __name__ == '__main__':
    me = Position('Karina', 'Lyakhova', 'DevOps engineer', 3500, 1000)
    me2 = Position('Karina', 'Lyakhova', 'Top DevOps engineer', 35000, 10000)
    print(me.get_full_name())
    print(f'Total income: {me.get_total_income()}')
    print(me._income)
    print(me2.get_full_name())
    print(f'Total income: {me2.get_total_income()}')
    print(me2.position)