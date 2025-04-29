from MicroKernel_Implementation import *
from Monolithic_Implementation import *


"""
This fiile contains all the performance comparison simulations done for this project.
Time efficiency decorator included to be applied as a timer where needed.
"""


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

def Time_Efficiency_Result_Decorator(func):
    def wrapper(*args, **kwargs):
        # Get start time
        start_time = time.time()

        # Run the function and store the result
        result = func(*args, **kwargs)

        # Get end time
        end_time = time.time()

        # Calculate elapsed time
        elapsed_time = end_time - start_time

        # Return both the result and the elapsed time
        return result, elapsed_time

    return wrapper


#
#   Start Microkernel
#
@Time_Efficiency_Result_Decorator
def Micro_Boot():
    # Microkernel  
    print( f'Microkernel Simulation:\n- For boot speed comparison\n- Microkernel is booted including one user application\n')
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
@Time_Efficiency_Result_Decorator
def Mono_Boot():
    print( f'Monolithic Simulation:\n- For boot speed comparison\n- Monolithic Kernel is booted including one user application\n')

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

    User_Application.system_call("read_fault", "text.txt")


@Time_Efficiency_Decorator
def Mono_Fault_Isolation_Comparison(Kernel, User_Application):
    print( f'Microkernel Simulation:\n- For fault isolation comparison\n- User application requests to read file, but it fails.\n- Kernel reboot time is measured.\n' )

    User_Application.system_call("read_fault", "text.txt")

def Monolithic_Tests():

    # Kernel Boot
    result, monolithic_elapsed_time_Boot = Mono_Boot()
    print(f'\nMonolithic Elapsed Time: {monolithic_elapsed_time_Boot:.6f}\n')

    _Monolithic, _User_Application_Mono = result[0], result[1]
    
    # System Call
    monolithic_elapsed_time_SysCall = Mono_SysCall_Comparison(_Monolithic, _User_Application_Mono)
    print(f'\nMonolithic Elapsed Time: {monolithic_elapsed_time_SysCall:.6f}\n')

    # Fault Isolation
    monolithic_elapsed_time_fault = Mono_Fault_Isolation_Comparison(_Monolithic, _User_Application_Mono)
    print(f'\nMonolithic Elapsed Time: {monolithic_elapsed_time_fault:.6f}\n')

    return monolithic_elapsed_time_SysCall, monolithic_elapsed_time_fault

def Micro_Tests():

    # Kernel Boot
    result, micro_elapsed_time_Boot = Micro_Boot()
    print(f'\nMicrokernel Elapsed Time: {micro_elapsed_time_Boot:.6f}\n')

    _Microkernel, _File_System, _User_Application_Micro = result[0], result[1], result[2]
    
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

    