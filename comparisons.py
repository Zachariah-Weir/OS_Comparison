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
    _File_System = File_System()                                # create service objects
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
    _User_Application = _Monolithic.create_application("User Application")

    return _Monolithic, _User_Application



#
#   IPC comparisons
#
@Time_Efficiency_Decorator
def Micro_IPC_Comparison( Microkernel, File_System, User_Application ):
    print( f'\nMicrokernel Simulation:\n- User application requests to read file.\n- Only IPC time is measured.\n' )
    Microkernel.IPC(IPC_Message("sender1", "file_system", "sample_operation"))

    
@Time_Efficiency_Decorator
def Mono_IPC_Comparison(Kernel, User_Application):
    print(f'\nMonolithic Simulation:\n- For IPC comparison\n- User application requests to read file.\n- Only system call time being measured (no IPC necessary).\n')

    User_Application.system_call("read", "text.txt")



#
#   System Call comparisons
#
@Time_Efficiency_Decorator
def Micro_SysCall_Comparison( Microkernel, File_System, User_Application):
    print( f'Microkernel Simulation:\n- User application requests to read and write file.\n- Only IPC and SysCall times being measured.\n' )
    
    User_Application.system_call("write", "text.txt", "sample text")
    User_Application.system_call("read", "text.txt")

@Time_Efficiency_Decorator
def Mono_SysCall_Comparison(Kernel, User_Application):
    print( f'Monolithic Simulation:\n- For system call comparison\n- User application requests to read and write file.\n- SysCall times being measured.\n' )

    User_Application.system_call("write", "text.txt", "sample text")
    User_Application.system_call("read", "text.txt")



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

@Time_Efficiency_Decorator
def Mono_Fault_Isolation_Comparison(Kernel, User_Application):
    print( f'Microkernel Simulation:\n- For fault isolation comparison\n- User application requests to read file, but it fails.\n- Kernel reboot time is measured.\n' )

    User_Application.system_call("read_fault", "text.txt")

#
# IPC comparisons: simulate a file read
#
def IPC_Comparison(_Microkernel, _File_System, _User_Application_Micro, _Monolithic, _User_Application_Mono):
    # Microkernel
    microkernel_elapsed_time = Micro_IPC_Comparison(_Microkernel, _File_System, _User_Application_Micro)
    print(f'\nMicrokernel Elapsed Time: {microkernel_elapsed_time:.6f}\n')

    # Monolithic
    monolithic_elapsed_time = Mono_IPC_Comparison(_Monolithic, _User_Application_Mono)
    print(f'Monolithic Elapsed Time: {monolithic_elapsed_time:.6f}\n')

    # Results
    print(f'Microkernel vs Monolithic Simulation Results:')
    print(f'   Microkernel elapsed SysCall + IPC time: {microkernel_elapsed_time:.6f}')   # subtracting SysCall time to isolate IPC time
    print(f'   Monolithic elapsed SysCall time: {monolithic_elapsed_time:.6f}') # can't substract system call because that is only component
    print(f'   Elapsed time difference: {microkernel_elapsed_time - monolithic_elapsed_time:.6f}')


#
# System Call comparisons: simulate a file read and write
#
def SysCall_Comparison(_Microkernel, _File_System, _User_Application_Micro, _Monolithic, _User_Application_Mono):
    # Microkernel
    microkernel_elapsed_time = Micro_SysCall_Comparison(_Microkernel, _File_System, _User_Application_Micro)
    print(f'\nMicrokernel Elapsed Time: {microkernel_elapsed_time:.6f}\n')

    # Monolithic
    monolithic_elapsed_time = Mono_SysCall_Comparison(_Monolithic, _User_Application_Mono)
    print(f'Monolithic Elapsed Time: {monolithic_elapsed_time:.6f}\n')

    # Results
    print(f'Microkernel vs Monolithic Simulation Results:')
    print(f'   Microkernel elapsed SysCall + IPC time: {microkernel_elapsed_time:.6f}')   # subtracting SysCall time to isolate IPC time
    print(f'   Monolithic elapsed SysCall time: {monolithic_elapsed_time:.6f}') # can't substract system call because that is only component
    print(f'   Elapsed time difference: {microkernel_elapsed_time - monolithic_elapsed_time:.6f}')


#
# Fault Isolation comparisons: simulate a file read failure
#
def Fault_Isolation_Comparison(_Microkernel, _File_System, _User_Application_Micro, _Monolithic, _User_Application_Mono):
    # Microkernel
    microkernel_elapsed_time = Micro_Fault_Isolation_Comparison(_Microkernel, _File_System, _User_Application_Micro)
    print(f'\nMicrokernel Elapsed Time: {microkernel_elapsed_time:.6f}\n')

    # Monolithic
    monolithic_elapsed_time = Mono_Fault_Isolation_Comparison(_Monolithic, _User_Application_Mono)
    print(f'Monolithic Elapsed Time: {monolithic_elapsed_time:.6f}\n')

    # Results
    print(f'Microkernel vs Monolithic Simulation Results:')
    print(f'   Microkernel elapsed SysCall + IPC time: {microkernel_elapsed_time:.6f}')   # subtracting SysCall time to isolate IPC time
    print(f'   Monolithic elapsed SysCall time: {monolithic_elapsed_time:.6f}') # can't substract system call because that is only component
    print(f'   Elapsed time difference: {microkernel_elapsed_time - monolithic_elapsed_time:.6f}')


def Monolithic_Tests(_Monolithic, _User_Application_Mono):
    
    # IPC
    monolithic_elapsed_time_IPC = Mono_IPC_Comparison(_Monolithic, _User_Application_Mono)
    print(f'\nMonolithic Elapsed Time: {monolithic_elapsed_time_IPC:.6f}\n')

    # System Call
    monolithic_elapsed_time_SysCall = Mono_SysCall_Comparison(_Monolithic, _User_Application_Mono)
    print(f'\nMonolithic Elapsed Time: {monolithic_elapsed_time_SysCall:.6f}\n')

    # Fault Isolation
    monolithic_elapsed_time_fault = Mono_Fault_Isolation_Comparison(_Monolithic, _User_Application_Mono)
    print(f'\nMonolithic Elapsed Time: {monolithic_elapsed_time_fault:.6f}\n')

    return monolithic_elapsed_time_IPC, monolithic_elapsed_time_SysCall, monolithic_elapsed_time_fault

def Micro_Tests(_Microkernel, _File_System, _User_Application_Micro):
    
    # IPC
    micro_elapsed_time_IPC = Micro_IPC_Comparison(_Microkernel, _File_System, _User_Application_Micro)
    print(f'\nMicrokernel Elapsed Time: {micro_elapsed_time_IPC:.6f}\n')

    # System Call
    micro_elapsed_time_SysCall = Micro_SysCall_Comparison(_Microkernel, _File_System, _User_Application_Micro)
    print(f'\nMicrokernel Elapsed Time: {micro_elapsed_time_SysCall:.6f}\n')

    # Fault Isolation
    micro_elapsed_time_fault = Micro_Fault_Isolation_Comparison(_Microkernel, _File_System, _User_Application_Micro)
    print(f'\nMicrokernel Elapsed Time: {micro_elapsed_time_fault:.6f}\n')

    return micro_elapsed_time_IPC, micro_elapsed_time_SysCall, micro_elapsed_time_fault

    