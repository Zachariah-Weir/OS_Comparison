import time


"""
This file contains the implementation of the Microkernel class and its functions.
"""


#
#   Microkernel class
#
class Microkernel:

    # constructor
    def __init__( self ):
        time.sleep( 0.01 ) # 10ms kernel boot
        self.core_services = []
        self.user_services = []
        self.running = True


    # register kernel services to give access to kernel
    def register_core_service( self, service ):
        self.core_services.append( service )
        service.kernel = self


    # register user services to give access to kernel
    def register_user_service( self, service ):
        self.user_services.append( service )
        service.kernel = self


    # IPC service
    def IPC( self, message ):
        time.sleep( .001 )    # set IPC time to 1ms
        print( f'IPC: {message.sender} -> {message.receiver}: \"{message.operation}\"' )            


    def SysCall( self, sender, operation ):
        time.sleep( .0002 ) # set SysCall time to .2ms
        print( f'SysCall: {sender} -> Kernel: \"{operation}\"' )


    # Start OS
    def start_Micro( self ):
        print( f'   Loading Microkernel...' )

        time.sleep( 0.005 ) # 5ms service manager startup
        print( f'   Starting System Service manager...' )
        print( f'       Loading Core Services...' )
        
        for service in self.core_services:
            print( f'           ', end='' )
            self.IPC(IPC_Message( "System Service Manager", service.service_name, f'Initialize {service.service_name} service...' ))
            service.load_service()

        print( f'       Loading User Services...' )
        
        for service in self.user_services:
            print( f'           ', end='' )
            self.IPC(IPC_Message( "System Service Manager", service.service_name, f'Initialize {service.service_name} service...' ))
            service.load_service()

        if ( self.running ):
            print( f'Microkernel booted' )


#
#   Service class
#
class Service:

    # constructor
    def __init__( self, service_name ):
        self.service_name = service_name
        self.kernel = None
        time.sleep( 0.004 ) # 4ms service boot

    def load_service( self ):
        print(f'                Loading {self.service_name}...')
        time.sleep( 0.004 ) # 4ms service boot
    


#   Kernel Service class
class Core_Service( Service ):
    pass


#   User Service class
class User_Service( Service ):
    pass


#
#   File System class
#
class File_System( Service ):
    # no functionality other than IPC
    pass
    

#
#   Disk class
#
class Disk( Core_Service ):

    def read_file( self ):
        print(f'   Disk loading file into memory...')
        time.sleep(0.002)

    def write_file( self ):
        print(f'   Disk writing to file...')
        time.sleep(0.0025)
    

#
#   User Application class
#
class User_Application( Service ):
    # no functionality other than IPC
    pass




#
#   Message class (used for IPC)
#
class IPC_Message:
    def __init__( self, sender, receiver, operation ):
        self.sender = sender
        self.receiver = receiver
        self.operation = operation
