import random
import sqlite3


conn = sqlite3.connect('Data/Knowleage.db')
c = conn.cursor()
c.execute('CREATE TABLE IF NOT EXISTS Bionomial_Nomenclature(Kingdom TXT,Phylum TXT, Sub_Phylum TXT, Class TXT, Sub_Class TXT, Order_ TXT, Sub_Order TXT, Family TXT, Sub_Family TXT, Genus TXT, Sub_Genus TXT, Species TXt)')
c.execute('CREATE TABLE IF NOT EXISTS Periodic_Table(Atomic_Number INT,Name TXT,Symbol TXT,Melting_Point FLOAT,Boiling_Point FLOAT,Discovery INT,Density FLOAT)')
c.execute('CREATE TABLE IF NOT EXISTS General_Knowleage(Question TXT, Answer TXT)')
conn.commit()


class Math:
    def __init__(self):
        pass
    class Triangle:
        def __init__(self,height,base,):
            self.height = height
            self.base = base


    class Square:
        def __init__(self,side):
            self.side = side
        
        
        def Area(self):
            return self.side*self.side


    def Percentage(T=None,O=None,P=None):
        '''Given output with input 
        T is Total,O is Obtain and P is Percentage
        if Total and Obtain Given output Percentage and so on'''
        if P == None:
            return O*100/T
        elif T == None:
            return O*100/P
        elif O == None:
            return T*P/100



    def Calculation_Test():
        correct = 0
        number = 10
        for i in range(number):
            a = random.randrange(30)
            b = random.randrange(10)
            ans = int(input(f'{a} X {b}: '))
            c = a * b
            if ans == c:
                print('Your Ans Right.')
                correct += 1
            else:
                print(c)
        print(f'\nYour Right Ans: {correct}\n')
        print(f"Your Ans Percentage: {Math.Percentage(T=number,O=correct)} %")



class Biology:
    def __init__(self):
        pass
    class Bionomial_Nomenclature:
        def __init__(self):
            pass


        def Add():
            """Adding New Nomenclature"""
            kingdom = input('Kingdom: ')
            phylum = input('Phylum: ')
            sub_phylum = input('Sub Phylum: ')
            classs = input('Class: ')
            sub_class  = input('Sub Class: ')
            order = input('Order: ')
            sub_order  = input('Sub Order: ')
            family = input('Family: ')
            sub_family = input('Sub Family: ')
            genus = input('Genus: ')
            sub_genus = input('Sub Genus: ')
            species = input('Species: ')
            c.execute('INSERT INTO Bionomial_Nomenclature(Kingdom, Phylum, Sub_Phylum, Order_, Sub_Order, Class, Sub_Class, Family, Sub_Family, Genus, Sub_Genus, Species) VALUES(?,?,?,?,?,?,?,?,?,?,?,?)',(kingdom,phylum,sub_phylum,order,sub_order,classs,sub_class,family,sub_family,genus,sub_genus,species))
            conn.commit()
            print(f'Adding {species} Entry Successfull.')

        def Show():
            datas = c.execute('SELECT * FROM Bionomial_Nomenclature')
            for data in datas:
                print(data)


        def Test():
            pass





class General_Knowleage:
    def __init__(self):
        pass


    def Add():
        question = input('Question: ')
        answer = input('Answer: ')
        c.execute('INSERT INTO General_Knowleage(Question,Answer) VALUES (?,?)',(question,answer))
        conn.commit()


    def Show():
        datas = c.execute('SELECT * FROM General_Knowleage')
        for data in datas:
            print(data)




class Chemistry:
    class Periodic_Table:
        def __init__(self):
            pass
        def Add():
            element = input('Element Name: ')
            element_symbol = input('Element Symbol: ')
            element_atom_number = input('Element Atomic Number: ')
            element_melting_point = input('Element Melting Point: ')
            element_boiling_point = input('Element Boiling Point: ')
            element_discovery = input('Element Discovry: ')
            element_densitry = input('Element Density: ')
            c.execute('INSERT INTO Periodic_Table(Atomic_Number, Name, Symbol, Melting_Point, Boiling_Point, Discovery, Density) VALUES (?,?,?,?,?,?,?)',(element_atom_number, element,element_symbol, element_melting_point, element_boiling_point, element_discovery, element_densitry))
            conn.commit()
            
        def Show():
            datas = c.execute('SELECT * FROM Periodic_Table')
            for data in datas:
                print(data)







class Physics:
    def __init__(self):
        pass
    pass



def Show_All_Data():
    """It to Show All Database Table What we have in each class"""
    Biology.Bionomial_Nomenclature.Show()
    Chemistry.Periodic_Table.Show()
    General_Knowleage.Show()


def __main__():
    General_Knowleage()
    Physics()
    Chemistry()
    Biology()
    Math()
