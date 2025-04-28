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
        print( f'\nMicrokernel Elapsed Time: {microkernel_elapsed_time}\n' )

        # Monolithic

        # Results
        print( f'Microkernel vs Monolithic Simulation Results:' )
        print( f'   Microkernel elapsed IPC time: {microkernel_elapsed_time - 0.0025}s' )   # subtracting SysCall time to isolate IPC time
        print( f'   Monolithic elapsed IPC time: ' )
        print( f'   Elapsed time difference:' )


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