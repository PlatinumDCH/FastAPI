class SetNames:
    def __init__(self, names:list):
        self.names = []
        self.results = dict()
        self.add(names)

    def __call__(self, surname):
        # пытаемся получить список полных имен по данной фамилии
        result = self.results.get(surname)


        if surname not in self.results:
            self.results[surname] = [f'{name} {surname}' for name in self.names]
        return self.results[surname]

    def add(self, input_names: list):
        for name in input_names:
            if not isinstance(name, str):
                raise TypeError(
                    'Name mast be string'
                )
        self.results.clear()
        self.names.extend(input_names)

names = SetNames(['Dima','Tim','Bim'])
names('Cheban')
names('Tolian')
print(names.results)
