from MicroKernel_Implementation import *
from Monolithic_Implementation import *


#
#   Start OSes
#
def Start_Microkernel():
    # Microkernel  
    _Microkernel = Microkernel()                                # create Microkernel object
    _File_System = File_System( "File System" )                 # create service objects
    _User_Application = User_Application( "User Application")  
    _Microkernel.register_kernel_service( _File_System )        # register services to Microkernel
    _Microkernel.register_user_service( _User_Application )          
    _Microkernel.start_Micro()                                  # start the Microkernel
    print()

    return _Microkernel, _File_System, _User_Application


#
#   IPC comparisons
#
def Micro_IPC_Comparison():
    print()

def Mono_IPC_Comparison():
    print()


#
#   System Call comparisons
#
def Micro_SysCall_Comparison():
    print()

def Mono_IPC_Comparison():
    print()