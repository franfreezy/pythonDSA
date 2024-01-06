#Write a Python program to create a person class. 
#Include attributes like name, country and date of birth. Implement a method to determine the person's age.

print('A program that computes the age of a person')
currentYear=2024
name = input( 'Enter your name then press Enter on the keyboard: ')
country = input(' which country do you live in : ')
date =int(input( ' enter your date of birth in the DD/MM/YYYY without symbols:'))

class Person():
    def __init__(self,name,country,date,currentYear):
        self.name = name
        self.country = country
        self.date = date
        self.currentYear = currentYear

    def age(self):
        
        self.dob = str(date)
        n = len(self.dob)
        k = -4
        YearOfBirth = []
       

        for i in range (4):
            values = self.dob[k]
            YearOfBirth.append(values)
            
            k=k+1
        
        year = str(0)
        for i in range(4):
            year =year+ str(YearOfBirth[i]) 
        age=self.currentYear-(int(year))
        return age
# instantiate an object
person = Person(name,country,date,currentYear)
Age = person.age()

print(name + ' from ' + country + ' is ' + str(Age) + ' years old ' )