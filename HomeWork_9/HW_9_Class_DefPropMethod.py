class Student:
    name = None
    spec = None
    grades = []

    def setPropr(self, n, s, g):
        self.name = n
        self.spec = s
        for i in range(len(g)):
            if 0 <= g[i] <= 10:
                self.grades = g
            else:
                print("Ooops, wrong value")

    def sayHi(self):
        print(f'Hi! my name is {self.name}. I learn {self.spec}\n'
              f'My grades is:')
        for i in range(len(self.grades)):
            print(f'>> {self.grades[i]:10f}')

    def calcAvgGrade(self):
        s = 0
        for i in range(len(self.grades)):
            s += self.grades[i]
        print(f'Average grade of {self.name} is {s / len(self.grades):2f}')


s1 = Student()
s2 = Student()

s1.setPropr('Ion', 'MIT', [10.0, 9.65, 8, 6.58, 7.5])
s2.setPropr('Maria', 'Philology', [7, 8.5, 9.6, 8.3])

s1.sayHi()
s1.calcAvgGrade()

print("*" * 40)

s2.sayHi()
s2.calcAvgGrade()
