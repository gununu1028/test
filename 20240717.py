class StudentCard:
  def __init__(self, id, name):
    self.id = id
    self.name = name
  def print_info(self):
    print('学籍番号:', self.id)
    print('氏名:', self.name)

class IStudentCard(StudentCard):
  def __init__(self, id, name, nationality):
    self.nationality = nationality
    super().__init__(id, name)
  def print_info(self):
    print(f'国籍: {self.nationality}')
    print(f'学籍番号: {self.id}')
    print(f'氏名: {self.name}')

class Person:
    def __init__(self, lastname, firstname):
        self.lastname = lastname
        self.firstname = firstname
 
    def show(self):
        print(f'私は{self.lastname}{self.firstname}です！')
 
class BusinessPerson(Person):
    def work(self):
        print(f'{self.lastname}{self.firstname}は働いています！’)

a = BusinessPerson(‘山形’, ‘太郎’)
a.show()
a.work()
