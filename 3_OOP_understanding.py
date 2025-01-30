'''
Specifically for the Advanced Python Programming Course
Author: Arta Khosravi
Last Update: Jan. 2025
'''
'''
Object Oriented Programming:
Mix different related items

In defining objects, I have i) variables, and ii) methods.

I) Variables are: 1) "Class" variable (constant), and 2) Object variable.
In OOP, I define Classes which includes different variables, which is
a mere definition. For example by defining a class called "person()",
Arta will be an object of this class when I write Arta = person(). 

II) Methods include functions, such as showing the grade, etc.
'''
# Example 1:
#Making classes for uni
class Person:
    #defining the constant variables.
    count = 0 #initially, zero people are present. 
    #count is the class' variable.
    #defining a method, called __init__.
    def __init__(self,name,age): #the initial starting method
    #in python, when I'm working with the functions inside a class,-
    #-I will always use "self"
    #Self will point out the very specific variable referring to it.
        self.name = name #variable 1 of init
        self.age = age #variable 2 of init
        Person.count += 1
    def get_name(self): #method 2
        print('Their name is %s.' %self.name)
    def get_age(self):
        print('Their age is %s.' %self.age)
    def get_info(self):
        print('Their name is %s, and their age is %i.' %(self.name,self.age))
    def birthday(self):
        self.age += 1
        print('Happy birthday %s!' % self.name)
    def return_count(self): #this one doesnt need self
        return (Person.count)
Arta = Person('Arta',25)
Arta.get_name() # I made an object, as a category of the Person class.
Arta.get_info() #gives age as 25
Arta.birthday()
Arta.get_age() #gives age as 26!
manooch = Person('manoochehr',12)
manooch.get_info()
#Arta and manooch are both 2 objects of this class.
print('At this moment I have %i people.' %Arta.return_count())

''''''''''''''''''''''''''''''''''''''''''''''''
# Example 2:
class Computer:
    count = 0
    def __init__(self, ram, hard, cpu):
        Computer.count += 1 #because it's a class variable
        self.ram = ram
        self.hard = hard
        self.cpu = cpu
    def value(self):
        return self.ram + self.hard + self.cpu
     #imaginary formula haha
    def __del__(self): #destructive method
        Computer.count -= 1
class Laptop(Computer): #Laptops inherit from Computer.
    # pass #at first
    #now, to define a function specifically
    #my init is the same as computer because it's inherited.
    def value(self):
        return self.cpu + self.hard + self.ram + self.size #refer to bottom page

pc_home = Computer(ram=12,hard=2,cpu=4) #output: 18
pc_work = Computer(ram=8,hard=4,cpu=4) #output: 16
print(pc_home.value(),pc_work.value())
del pc_work
laptop_home = Laptop(ram=16,hard=2,cpu=4) #output if pass: 22
#output if def value: 35
laptop_home.size = 13 #I'm randomly defining a size of 13' for this laptop,
#without defining it in the laptop class beforehand.
print(laptop_home.value())

''''''''''''''''''''''''''''''''''''''''''''''''
# Example 3:
'''
IOT : Internet of Things
'''
#We have a few devices connected through IPs, such as TVs.
# and they have thermometers with a readable number. 
# I want to control them through class and OOP.

class Device: #they're all devices. so we should first define a device class.
    count = 0 
    def __init__(self, ip, mac, name):
        self. ip = ip
        self.mac = mac 
        self.name = name 
        Device.count +=1
        # init the device
        #this is a complete random example
        result = int(input('Enter a number (>10): '))
        if result > 10:
            self.status = 'Active'
        else:
            self.status = 'Unknown'
class TV(Device):
    def turn_on(self):
        #connect to self.ip and turn on
        pass
    def turn_off(self):
        #connect to self.ip and turn off
        pass
class Thermometer(Device):
    def get_degree(self):
        # connect to self.ip and read degree and return results
        # return result
        pass

class SmartTV(TV):
    def turn_on(self): #overloading the turn_on function
        #this version of turn_on will be called instead of the TV.
        #turn on the smart tv from self.ip
        pass

Arta_tv = TV(10,2,'TV')
