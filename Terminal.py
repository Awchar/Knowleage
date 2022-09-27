from asyncio.proactor_events import _ProactorBaseWritePipeTransport
import Knowleage

print('Welcome to Learn')

while True:
    command  = int(input('1.Show Data\n2.Test Yourself\n3.Insert Data\nInput: '))
    if command == 1:
        while True:
            sub_command = input('\n1.Biology\n2.Chemistry\n3.General Knowleage\n4.All\nYour Input: ')
            if sub_command == 1:
                Knowleage.Biology.Binominal_Nomenclature.Show()
            elif sub_command == 2:
                Knowleage.Chemistry.Periodic_Table.Show()
            elif sub_command ==3:
                Knowleage.General_Knowleage.Show()
            elif sub_command == 4:
                Knowleage.Show_All_Data()
            elif sub_command in ['quit','exit','q']:
                break
            else:
                print('INVALID INPUT\n')

    elif command == 2:
        pass
    elif command in ['quit','exit','q']:
        break
    else:
        print('INVALID INPUT\n')