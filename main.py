from comparisons import *


"""
This file contains:
- the implementation of the Monolithic and Microkernel OSes.
- the implementatin of our OS comparisons.
- this file will be visualized using a GUI.
"""


def main():

    _Monolithic, _User_Application_Mono = Start_Monolithic()
    _Microkernel, _File_System, _User_Application_Micro = Start_Microkernel()

    Monolithic_Tests(_Monolithic, _User_Application_Mono)
    Micro_Tests(_Monolithic, _User_Application_Mono)
    
    IPC_Comparison(_Microkernel, _File_System, _User_Application_Micro, _Monolithic, _User_Application_Mono)
    SysCall_Comparison(_Microkernel, _File_System, _User_Application_Micro, _Monolithic, _User_Application_Mono)
    Fault_Isolation_Comparison(_Microkernel, _File_System, _User_Application_Micro, _Monolithic, _User_Application_Mono)

    # comment


if __name__ == "__main__":
    main()