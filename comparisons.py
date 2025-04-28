from MicroKernel_Implementation import *
from Monolithic_Implementation import *


"""
This fiile contains all the performance comparison simulations done for this project.
Time efficiency decorator included to be applied as a timer where needed.
"""


# Time Efficiency Decorator
def Time_Efficiency_Decorator( func ):
    def wrapper( *args, **kwargs):
        # get start time
        start_time = time.time()
        # run the function being decorated
        func( *args, **kwargs )
        # get end time
        end_time = time.time()
        # get elapsed time
        elapsed_time = end_time - start_time
        return elapsed_time
    return wrapper


#
#   Start Microkernel
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
#   Start Monolithic
#
def Start_Monolithic():

    _Monolithic = Monolithic() # create Monolithic object
    # no necessity to load services individually

    return _Monolithic



#
#   IPC comparisons
#
@Time_Efficiency_Decorator
def Micro_IPC_Comparison( Microkernel, File_System, User_Application ):
    print( f'Microkernel Simulation:\n- User application requests to read file.\n- Only IPC time being measured.\n' )
    User_Application.kernel.SysCall( User_Application.service_name, "Kernel", "Requesting File Read via File System...")
    Microkernel.IPC( "Kernel", File_System.service_name, "Requesting to Read File..." )
    print( f'IPC: {File_System.service_name} -> Disk: "Requesting File Read"' ); time.sleep( .001 )
    print( f'\nDisk loading file into memory...\n' ); time.sleep( .002 )
    File_System.kernel.IPC( File_System.service_name, "Kernel", "File loaded into main memory..." )
    Microkernel.IPC( "Kernel", User_Application.service_name, "File loaded into main memory..." )

    
def Mono_IPC_Comparison():
    print( f'Monolithic Simulation:\n- User application requests to read file.\n- Only IPC time being measured.\n' )


#
#   System Call comparisons
#
@Time_Efficiency_Decorator
def Micro_SysCall_Comparison( Microkernel, File_System, User_Application):
    print( f'Microkernel Simulation:\n- User application requests to read and write file.\n- Only IPC and SysCall times being measured.\n' )
    # read file
    User_Application.kernel.SysCall( User_Application.service_name, "Kernel", "Requesting File Read via File System...")
    Microkernel.IPC( "Kernel", File_System.service_name, "Requesting to Read File..." )
    File_System.kernel.IPC( File_System.service_name, "Disk", "Requesting File Read..." )
    print( f'\nDisk loading file into memory...\n' ); time.sleep( .002 )    # 2ms file read
    File_System.kernel.IPC( File_System.service_name, "Kernel", "File loaded into main memory..." )
    Microkernel.IPC( "Kernel", User_Application.service_name, "File loaded into main memory..." )
    # write file
    print()
    User_Application.kernel.SysCall( User_Application.service_name, "Kernel", "Requesting File Write via File system..." )
    Microkernel.IPC( "Kernel", File_System.service_name, "Requesting File Write...")
    File_System.kernel.IPC( File_System.service_name, "Disk", "Requesting File Write..." )
    print( f'\nDisk writing to file...\n' ); time.sleep( .002 )    # 2ms file read
    File_System.kernel.IPC( File_System.service_name, "Kernel", "File Write completed...")
    Microkernel.IPC( "Kernel", User_Application.service_name, "File Write completed...")


def Mono_SysCall_Comparison( Kernel):
    print( f'Monolithic Simulation:\n- User application requests to read and write file.\n- SysCall times being measured.\n' )
    User_app = Kernel.create_application("User_App1")
    User_app.system_call("write", "text.txt", "sample text")
    User_app.system_call("read", "text.txt")



#
#   Fault Isolation comparisons
#
@Time_Efficiency_Decorator
def Micro_Fault_Isolation_Comparison( Microkernel, _File_System, User_Application ):
    print( f'Microkernel Simulation:\n- User application requests to read file, but it fails.\n- Only service restart times being measured.\n' )
    # attempt to read a file, but crash the file system
    User_Application.kernel.SysCall( User_Application.service_name, "Kernel", "Requesting File Read via File System...")
    Microkernel.IPC( "Kernel", _File_System.service_name, "Requesting to Read File..." )
    del _File_System; print( f'ERROR: File System Error - Service Unavailable. Restarting the service...' )
    # restart the file system
    _File_System = File_System( "File System" )
    Microkernel.register_kernel_service( _File_System ); print( f'Registering File System service...' ); time.sleep(0.01)   # 10ms service restart
    _File_System.kernel.IPC( _File_System.service_name, "Kernel", "File System service successfully restarted..." )


def Mono_Fault_Isolation_Comparison():
    pass
