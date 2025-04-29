from comparisons import *


"""
This file contains:
- the implementation of the Monolithic and Microkernel OSes.
- the implementatin of our OS comparisons.
- this file will be visualized using a GUI.
"""


def main():

    #
    # IPC comparisons: simulate a file read
    #
    def IPC_comparison():
        # load MICROKERNEL and services
        _Microkernel, _File_System, _User_Application = Start_Microkernel()
        # run MICROKERNEL IPC simulation
        microkernel_elapsed_time = Micro_IPC_Comparison( _Microkernel, _File_System, _User_Application )
        print(f'\nMicrokernel Elapsed Time: {microkernel_elapsed_time:.6f}\n')

        # Monolithic
        _Monolithic = Start_Monolithic()
        monolithic_elapsed_time = Mono_IPC_Comparison(_Monolithic)
        print(f'Monolithic Elapsed Time: {monolithic_elapsed_time:.6f}\n')

        # Results
        print(f'Microkernel vs Monolithic Simulation Results:')
        print(f'   Microkernel elapsed SysCall + IPC time: {microkernel_elapsed_time}')   # subtracting SysCall time to isolate IPC time
        print(f'   Monolithic elapsed SysCall time: {monolithic_elapsed_time}') # can't substract system call because that is only component
        print(f'   Elapsed time difference: {microkernel_elapsed_time - monolithic_elapsed_time}')


    #
    # System Call comparisons: simulate a file read and write
    #
    def SysCall_Comparison():
        # load MICROKERNEL and services
        _Microkernel, _File_System, _User_Application = Start_Microkernel()
        # run MICROKERNEL SysCall simulation
        microkernel_elapsed_time = Micro_SysCall_Comparison( _Microkernel, _File_System, _User_Application )
        print( f'\nMicrokernel Elapsed Time: {microkernel_elapsed_time}\n' )

        # monolithic

        # results


    #
    # Fault Isolation comparisons: simulate a file read failure
    #
    def Fault_Isolation_Comparison():
        # load MICROKERNEL and services
        _Microkernel, _File_System, _User_Application = Start_Microkernel()
        # run MICROKERNEL SysCall simulation
        microkernel_elapsed_time = Micro_Fault_Isolation_Comparison( _Microkernel, _File_System, _User_Application )
        print( f'\nMicrokernel Elapsed Time: {microkernel_elapsed_time - .0005 - .001*2}' )


    Fault_Isolation_Comparison()


if __name__ == "__main__":
    main()