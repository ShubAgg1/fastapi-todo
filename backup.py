class Student:
    def __init__(self, name, rating):
        self.name = name
        self.rating = rating

    def is_expert(self):
        return self.rating >= 1600
    

s1 = Student("Aryan", 1400)
s2 = Student("Rahul", 1600)

print(s1.name)
print(s2.rating)

print(s1.is_expert())
print(s2.is_expert())