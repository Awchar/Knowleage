import Knowleage

print('Welcome to Learn')

while True:
    command  = int(input('1.Show Data\n2.Test Yourself\n3.Insert Data\nInput: '))
    if command == 1:
        while True:
            sub_command = int(input('\n1.Biology Name\n2.Chemistry\n3.General Knowleage\n4.All\nYour Input: '))
            if sub_command == 1:
                Knowleage.Biology.Bionomial_Nomenclature.Show()
            elif sub_command == 2:
                Knowleage.Chemistry.Periodic_Table.Show()
            elif sub_command ==3:
                Knowleage.General_Knowleage.Show()
            elif sub_command == 4:
                Knowleage.Show_All_Data()
            elif sub_command == 0:
                break
            else:
                print('INVALID INPUT\n')
    elif command == 2:
        while True:
            sub_command = int(input('\n1.Biology Name\n2.Chemistry\n3.General knowleage\n4.Physics\nYour Input: '))
            if sub_command == 1:
                Knowleage.Biology.Bionomial_Nomenclature.Test()
            elif sub_command == 2:
                Knowleage.Chemistry.Periodic_Table.Test()
            elif sub_command == 3:
                Knowleage.General_Knowleage.Test()
            elif sub_command == 4:
                pass
            elif sub_command == 0:
                break
            else:
                print('INVALID INPUT\n')

    elif command == 3:
        while True:
            sub_command = int(input('\n1.Biology Name\n2.Chemistry\n3.General Knowleage\n4.Physics\nYour Input: '))
            if sub_command == 1:
                Knowleage.Biology.Bionomial_Nomenclature.Add()
            elif sub_command == 2:
                Knowleage.Chemistry.Periodic_Table.Add()
            elif sub_command == 3:
                Knowleage.General_Knowleage.Add()
            elif sub_command == 4:
                pass
            elif sub_command == 0:
                break
            else:
                ('INVALID INPUT\n')

    elif command == 0:
        break
    else:
        print('INVALID INPUT\n')