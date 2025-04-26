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
        self.kernel_services = []
        self.user_services = []
        self.running = True

    # register kernel services to give access to kernel
    def register_kernel_service( self, service ):
        self.kernel_services.append( service )
        service.kernel = self

    # register user services to give access to kernel
    def register_user_service( self, service ):
        self.user_services.append( service )
        service.kernel = self

    # IPC service
    def IPC( self, sender, receiver, message ):
        print( f'IPC: {sender} -> {receiver}: "{message}"' )

    # Start OS
    def start_Micro( self ):
        print( f'\nLoading Microkernel...' )

        print( f'   Loading Kernel Services...')
        for service in self.kernel_services:
            service.load_service()
            
        print( f'   Loading User Services...' )
        for service in self.user_services:
            service.load_service()


#
#   Service class
#
class Service:

    # constructor
    def __init__( self, service_name ):
        self.service_name = service_name
        self.kernel = None

    def load_service( self ):
        print( f'       Loading {self.service_name}...' )


#   Kernel Service class
class Kernel_Service( Service ):
    pass


#   User Service class
class User_Service( Service ):
    pass


#
#   File System class
#
class File_System( Kernel_Service ):

    # read file
    def read_file( self ):
        self.kernel.IPC( self.service_name, "Kernel", "Reading File..." )


#
#   User Application class
#
class User_Application( Service ):
    pass