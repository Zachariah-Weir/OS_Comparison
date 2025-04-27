import time

"""
This file contains the implementation of the Microkernel class and its functions.
"""


#
#   Monolithic class
#
class Monolithic:

    # constructor
    def __init__( self ):
        print( f'\nLoading Monolithic Kernel...' )
        self.file_system = File_System(kernel=self)
        self.load_services()
        self.running = True

    def load_services(self):
        print( f'   Loading Kernel Services...')
        self.file_system.load_service()
        self



#
#   Base class for services
#
class Kernel_Service:
    def __init__(self, service_name, kernel):
        self.service_name = service_name
        self.kernel = kernel

    def load_service(self):
        print(f'  Loading {self.service_name}...')


#
#   File System class
#
class File_System(Kernel_Service):
    def __init__(self, kernel):
        super().__init__("file_System", kernel) #instantiates parent class (must include service name), inherits load_service function
        self.file_dict = {} #dictionary to simulate file management

    def read_file(self, file_name):
        print(f'File_System: Reading from "{file_name}"...')
        return self.file.get(file_name, "File not found")
    
    def write_file(self, file_name, file_content):
        print(f'File_System: Writing to "{file_name}"...')
        self.file[file_name] = file_content
        return True



