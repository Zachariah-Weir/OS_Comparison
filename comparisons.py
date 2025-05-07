from MicroKernel_Implementation import *
from Monolithic_Implementation import *
from matplotlib import pyplot as plt


"""
This fiile contains all the performance comparison simulations done for this project.
Time efficiency decorator included to be applied as a timer where needed.
"""



#
#   Time Efficiency Decorators
#

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
#   Start OSes
#
@Time_Efficiency_Result_Decorator
def Micro_Boot():
    # Microkernel  
    print(
    f'\n---------------------------------------------------------------------------\n\n\
    Microkernel Boot Comparison:\n\n\
    - Scenario: Booting up Microkernel OS.\n\
    - Measuring: Boot Overhead due to IPC.\
    \n\n---------------------------------------------------------------------------\n' )
    _Microkernel = Microkernel()                                # create Microkernel object
    _File_System = File_System( "File System" )                 # create service objects
    _User_Application = User_Application( "User Application")
    _Disk = Disk( "Disk" )  
    _Microkernel.register_core_service( _File_System )        # register services to Microkernel
    _Microkernel.register_core_service( _Disk )
    _Microkernel.register_user_service( _User_Application )          
    _Microkernel.start_Micro()                                  # start the Microkernel
    print()

    return _Microkernel, _File_System, _User_Application, _Disk


@Time_Efficiency_Result_Decorator
def Mono_Boot():
    print(
    f'\n---------------------------------------------------------------------------\n\
    Monolithic Boot Comparison:\n\n\
    - Scenario: Booting up Monolithic Kernel.\n\
    - Measuring: Boot speed (no necessity for IPC).\
    \n---------------------------------------------------------------------------\n' )

    _Monolithic = Monolithic() # create Monolithic object
    # no necessity to load services individually
    _User_Application = _Monolithic.system_call_handler("create_application", "user_application1")

    return _Monolithic, _User_Application



#
#   IPC comparisons
#
@Time_Efficiency_Decorator
def Micro_IPC_Comparison( Microkernel, File_System, User_Application, Disk ):
    print(
    f'\n---------------------------------------------------------------------------\n\n\
    Microkernel IPC Comparison:\n\n\
    - Scenario: User application requests to read a file.\n\
    - Measuring: Overhead due to IPC.\
    \n\n---------------------------------------------------------------------------\n' )
    # User App SysCalls and IPCs to Kernel
    User_Application.kernel.SysCall( User_Application.service_name, "Requesting to read file..." )
    # Kernel IPCs to file system
    Microkernel.IPC(IPC_Message( "Kernel", File_System.service_name, "Requesting to read file..." ))
    # File System IPCs to Kernel
    File_System.kernel.IPC(IPC_Message( File_System.service_name, "Kernel", "Requesting to read file..." ))
    # Kernel IPCs to Disk
    Microkernel.IPC(IPC_Message( "Kernel", Disk.service_name, "Requesting to read file..." ))
    # Disk reads
    Disk.read_file()
    # Disk IPCs to Kernel
    Disk.kernel.IPC(IPC_Message( Disk.service_name, "Kernel", "File loaded into memory..." ))
    # Kernel IPCs to File System
    Microkernel.IPC( IPC_Message( "Kernel", File_System.service_name, "File loaded into memory..." ) )
    # File System IPCs to Kernel
    File_System.kernel.IPC(IPC_Message( File_System.service_name, "Kernel", "File loaded into memory..." ))
    # Kernel IPCs to User App
    Microkernel.IPC(IPC_Message( "Kernel", User_Application.service_name, "File loaded into memory..." ))



#
#   System Call comparisons
#
@Time_Efficiency_Decorator
def Micro_SysCall_Comparison( Microkernel, File_System, User_Application, Disk ) :
    print(
    f'\n---------------------------------------------------------------------------\n\n\
    Microkernel SysCall Comparison:\n\n\
    - Scenario: User application requests to read and write to a file.\n\
    - Measuring: SysCall Overhead due to IPC.\
    \n\n---------------------------------------------------------------------------\n' )

    # { Read }
    # User App SysCalls and IPCs to Kernel
    User_Application.kernel.SysCall( User_Application.service_name, "Requesting to read file..." )
    # Kernel IPCs to file system
    Microkernel.IPC(IPC_Message( "Kernel", File_System.service_name, "Requesting to read file..." ))
    # File System IPCs to Kernel
    File_System.kernel.IPC(IPC_Message( File_System.service_name, "Kernel", "Requesting to read file..." ))
    # Kernel IPCs to Disk
    Microkernel.IPC(IPC_Message( "Kernel", Disk.service_name, "Requesting to read file..." ))
    # Disk reads
    Disk.read_file()
    # Disk IPCs to Kernel
    Disk.kernel.IPC(IPC_Message( Disk.service_name, "Kernel", "File loaded into memory..." ))
    # Kernel IPCs to File System
    Microkernel.IPC(IPC_Message( "Kernel", File_System.service_name, "File loaded into memory..." ))
    # File System IPCs to Kernel
    File_System.kernel.IPC(IPC_Message( File_System.service_name, "Kernel", "File loaded into memory..." ))
    # Kernel IPCs to User App
    Microkernel.IPC(IPC_Message( "Kernel", User_Application.service_name, "File loaded into memory..." ))
    print()

    # { Write }
    # User App SysCalls and IPCs to Kernel
    User_Application.kernel.SysCall( User_Application.service_name, "Requesting to write file..." )
    # Kernel IPCs to file system
    Microkernel.IPC(IPC_Message( "Kernel", File_System.service_name, "Requesting to write file..." ))
    # File System IPCs to Kernel
    File_System.kernel.IPC(IPC_Message( File_System.service_name, "Kernel", "Requesting to write file..." ))
    # Kernel IPCs to Disk
    Microkernel.IPC(IPC_Message( "Kernel", Disk.service_name, "Requesting to write file..." ))
    # Disk writes
    Disk.write_file()
    # Disk IPCs to Kernel
    Disk.kernel.IPC(IPC_Message( Disk.service_name, "Kernel", "File succesfully written..." ))
    # Kernel IPCs to File System
    Microkernel.IPC(IPC_Message( "Kernel", File_System.service_name, "File succesfully written..." ))
    # File System IPCs to Kernel
    File_System.kernel.IPC(IPC_Message( File_System.service_name, "Kernel", "File succesfully written..." ))
    # Kernel IPCs to User App
    Microkernel.IPC(IPC_Message( "Kernel", User_Application.service_name, "File succesfully written..." ))


@Time_Efficiency_Decorator
def Mono_SysCall_Comparison( Kernel, User_Application ):
    print(
    f'\n---------------------------------------------------------------------------\n\
    Monolithic System Call Comparison:\n\n\
    - Scenario: User application requests to read and write to a file.\n\
    - Measuring: Speed of system call (no IPC required).\
    \n---------------------------------------------------------------------------\n' )

    User_Application.system_call("write", "text.txt", "sample text")
    User_Application.system_call("read", "text.txt")




#
#   Fault Isolation comparisons
#
@Time_Efficiency_Decorator
def Micro_Fault_Isolation_Comparison( _Microkernel, _File_System, _User_Application, _Disk ):
    print(
    f'\n---------------------------------------------------------------------------\n\n\
    Microkernel Fault Isolation Comparison:\n\n\
    - Scenario: User application attempts to read a file, but File System crashes.\n\
    - Measuring: Time it takes to reboot the service(s).\
    \n\n---------------------------------------------------------------------------\n' )

    # request file read
    _User_Application.kernel.SysCall( _User_Application.service_name, "Requesting to read file..." )
    _Microkernel.IPC(IPC_Message( "Kernel", _File_System.service_name, "Requesting to read file..." ))
    _File_System.kernel.IPC(IPC_Message( _File_System.service_name, _Disk.service_name, "Requesting to read file..." ))
    
    # Disk crashes
    print( f'ERROR: Disk crashed.' )
    del _Disk
    print( f'   [System] Rebooting Disk...' )
    
    # reboot file system
    _Disk = Disk( "Disk" )
    _Microkernel.register_core_service( _Disk )
    _Disk.kernel.IPC(IPC_Message( _Disk.service_name, "Kernel", "Disk successfuly rebooted!" ))



@Time_Efficiency_Decorator
def Mono_Fault_Isolation_Comparison(Kernel, User_Application):
    print(
    f'\n---------------------------------------------------------------------------\n\
    Monolithic Fault Isolation Comparison:\n\n\
    - Scenario: User application attempts to read a file, but File System crashes.\n\
    - Measuring: Speed of reboot (entire kernel requires reboot).\
    \n---------------------------------------------------------------------------\n' )
    
    User_Application.system_call("read_fault", "text.txt")



#
#   Combined Comparison Tests
#
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

    _Microkernel, _File_System, _User_Application_Micro, _Disk = result
    
    # IPC
    micro_elapsed_time_IPC = Micro_IPC_Comparison( _Microkernel, _File_System, _User_Application_Micro, _Disk )
    print(f'\nMicrokernel Elapsed Time: {micro_elapsed_time_IPC:.6f}\n')

    # System Call
    micro_elapsed_time_SysCall = Micro_SysCall_Comparison( _Microkernel, _File_System, _User_Application_Micro, _Disk )
    print(f'\nMicrokernel Elapsed Time: {micro_elapsed_time_SysCall:.6f}\n')

    # Fault Isolation
    micro_elapsed_time_fault = Micro_Fault_Isolation_Comparison( _Microkernel, _File_System, _User_Application_Micro, _Disk )
    print(f'\nMicrokernel Elapsed Time: {micro_elapsed_time_fault:.6f}\n')

    return micro_elapsed_time_IPC, micro_elapsed_time_SysCall, micro_elapsed_time_fault

    

#
#   Plot a Bar Graph
#
def plot_bar_graph( title, ylabel, xlabel, values, xlabels ):
    # if number of values doesn't match number of labels on x-axis, throw error
    if len( values ) != len( xlabels ):
        raise ValueError( "Length of values and xlabels must be the same." )

    # generate x-axis positions for each value
    x = list( range(len(values)) )

    # set figure size and bar info
    plt.figure( figsize=(8, 6) )
    bars = plt.bar( x, values, color='skyblue' )

    # Title and axis labels
    plt.title( title )
    plt.ylabel( ylabel )
    plt.xlabel( xlabel )

    # Custom x-axis labels
    plt.xticks( x, xlabels, rotation=45 )

    # Add value labels on top of each bar
    for bar in bars:
        height = bar.get_height()
        plt.text(
            bar.get_x() + bar.get_width() / 2,
            height,
            f'{height:.4f}',
            ha='center',
            va='bottom'
        )

    plt.show()