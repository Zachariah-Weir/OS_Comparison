from comparisons import *


"""
This file contains:
- the implementation of the Monolithic and Microkernel OSes.
- the implementatin of our OS comparisons.
- this file will be visualized using a GUI.
"""


def main():

    _Monolithic, _User_Application_Mono = Start_Monolithic()
    Monolithic_Tests(_Monolithic, _User_Application_Mono)

    _Microkernel, _File_System, _User_Application_Micro = Start_Microkernel()
    Micro_Tests(_Microkernel, _File_System, _User_Application_Micro)

    # comment


if __name__ == "__main__":
    main()