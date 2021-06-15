# 1)staticmethods ve dundermethodslari research edin-------------------------------------------



# class Isciler():
#     isci_siyahisi = []

#     def __init__(self, ad, soyad, maas, departament):
#         self.ad          = ad
#         self.soyad       = soyad
#         self.maas        = maas
#         self.departament = departament
#         self.melumatlari_saxla() 

#     def melumatlari_saxla(self):
#         self.isci_siyahisi.append(self.ad)
#         self.isci_siyahisi.append(self.soyad)
#         self.isci_siyahisi.append(self.maas)
#         self.isci_siyahisi.append(self.departament)
#     @classmethod
#     def melumatlari_goster(cls):
#         print(cls.isci_siyahisi) 

#     @staticmethod
#     def bonus_faizi():
#         return 0.12           

# isci_1 = Isciler("Eli", "Veliyev", "700", "Muhasib")

# isci_1.melumatlari_goster()
# Isciler.melumatlari_goster()

# from datetime import date
   
# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
       
#     # a class method to create a Person object by birth year.
#     @classmethod
#     def fromBirthYear(cls, name, year):
#         return cls(name, date.today().year - year)
       
#     # a static method to check if a Person is adult or not.
#     @staticmethod
#     def isAdult(age):
#         return age > 18
   
# person1 = Person('mayank', 21)
# person2 = Person.fromBirthYear('mayank', 1996)
   
# print (person1.age)
# print (person2.age)
   
# # print the result
# print (Person.isAdult(22))


# class Person:

#     def __init__(self, name):
#         self.name = name 

#     def about_me(self):
#         print("I am {}".format(self.name))    
#     @staticmethod
#     def speak(msg):
#         print(msg)

# p = Person("Nik")
# p.about_me() 

# p.speak("hello")
# Person.speak("asxdasd")

#2)inheritance ve polimorfizmi tetbiq etmek ucun iki dene class yaradin, attribut ve metodlari inheritance numune getirin.-------------------------

# class Rehber():
     
    
#     def __init__(self,ad,soyad,maas):
#         self.ad = ad
#         self.soyad = soyad 
#         self.maas = maas 
        
        

#     def info(self):
#         print(f" {self.ad}  {self.soyad} {self.maas} ") 
        
        

# class Isci(Rehber):
#     def __init__(self,ad,soyad,maas,):
#         super().__init__(ad,soyad,maas)
        
#     def info(self):
#         print(f" {self.ad}  {self.soyad}  {self.maas} maas alir") 
        
    
# isci1 = Isci("Eli","Mireliyev",4000)  
# isci1.info()
# rehber1 = Rehber("Samir", "Hesenov", 7000)
# rehber1.info()

#3)super() function haqqinda research edin ve bildiklerinizi yazin----------------------------------------------------------


# Super funksiyasi alt sinifi yaradarken ust sinifdeki __init__ metodu icindeki butun kodlari  alib burada istifade etmek ucun lazim olur.Misal ile izah Edek

class Emekdaslar():
    def _init__(self, ad, vezife, maas):
        self.ad = ad
        self.vezife = vezife
        self.maas = 0

    def maas_hesabla():
        print("Maas hesablanir")

class Muhasibler(Emekdaslar):
    def __init__(self, ad, vezife, maas):
        super().__init__(ad, vezife)
        self.maas = 100        

isci1 = Muhasibler()
isci1(print(f" {self.ad}  {self.soyad}  {self.maas} maas alir") )