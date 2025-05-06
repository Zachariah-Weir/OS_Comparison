from comparisons import *


"""
This file contains:
- the implementation of the Monolithic and Microkernel OSes.
- the implementatin of our OS comparisons.
- this file will be visualized using a GUI.
"""


def main():

    while True:
        # main menu
        print( f'=====================================', '\n' )
        print( f'Monolithic vs Microkernel'.center(20), '\n' )
        print( f'0) Quit' )
        print( f'1) Boot Comparison' )
        print( f'2) IPC Comparison' )
        print( f'3) System Call Comparison' )
        print( f'4) Fault Isolation Comparison' , '\n')
        print( f'=====================================', '\n' )

        # get user choice
        choice = int( input(f'Enter menu option: ') )

        # Quit
        if choice == 0:
            break

        # Boot
        elif choice == 1:
            # Mono
            result, monolithic_elapsed_time_Boot = Mono_Boot()
            print(f'\nMonolithic Elapsed Time: {monolithic_elapsed_time_Boot:.6f}\n')
            _Monolithic, _User_Application_Mono = result
            
            # Micro
            result, micro_elapsed_time_Boot = Micro_Boot()
            print(f'\nMicrokernel Elapsed Time: {micro_elapsed_time_Boot:.6f}\n')
            _Microkernel, _File_System, _User_Application_Micro, _Disk = result

        # IPC
        elif choice == 2:
            # Micro
            micro_elapsed_time_IPC = Micro_IPC_Comparison( _Microkernel, _File_System, _User_Application_Micro, _Disk )
            print(f'\nMicrokernel Elapsed Time: {micro_elapsed_time_IPC:.6f}\n')

        # Sys Call
        elif choice == 3: 
            # Mono
            monolithic_elapsed_time_SysCall = Mono_SysCall_Comparison(_Monolithic, _User_Application_Mono)
            print(f'\nMonolithic Elapsed Time: {monolithic_elapsed_time_SysCall:.6f}\n')

            # Micro
            micro_elapsed_time_SysCall = Micro_SysCall_Comparison( _Microkernel, _File_System, _User_Application_Micro, _Disk )
            print(f'\nMicrokernel Elapsed Time: {micro_elapsed_time_SysCall:.6f}\n')

        # Fault Isolation
        elif choice == 4:
            # Mono
            monolithic_elapsed_time_fault = Mono_Fault_Isolation_Comparison(_Monolithic, _User_Application_Mono)
            print(f'\nMonolithic Elapsed Time: {monolithic_elapsed_time_fault:.6f}\n')

            # Micro
            micro_elapsed_time_fault = Micro_Fault_Isolation_Comparison( _Microkernel, _File_System, _User_Application_Micro, _Disk )
            print(f'\nMicrokernel Elapsed Time: {micro_elapsed_time_fault:.6f}\n')





if __name__ == "__main__":
    main()