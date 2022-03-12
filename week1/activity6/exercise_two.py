class Name(object):
    def __init__(self, first_name, surname, title, *other_names) -> None:
        super().__init__()
        self.first_name = first_name
        self.surname = surname
        self.title = title
        self.other_names = other_names

    def formal_name(self):
        return f'{self.title} {self.first_name[:1]}. {self.get_initials(self.other_names)} {self.surname}'

    @staticmethod
    def get_initials(other_names):
        return ' '.join(map(lambda n: n[:1] + ".", other_names))


class Person(object):
    def __init__(self, name) -> None:
        super().__init__()
        self.name = name

    def say_hello(self):
        print(self.name.formal_name())


class Student(Person):
    def __init__(self, name) -> None:
        super().__init__(name)


class DistanceStudent(Student):
    def __init__(self, name, current_module) -> None:
        super().__init__(name)
        self.current_module = current_module

    def report_current_study_module(self):
        print(f'{self.name.formal_name()} is currently studying the {self.current_module} module.')


greenhold = Name('James', 'Greenhold', 'Mr', 'Samuel')
DistanceStudent(greenhold, 'Advanced Programming').report_current_study_module()
