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
        self.file_system = File_System(kernel=self) #initialize File_System with kernel address as parameter
        self.load_services()
        self.running = True
        if (self.running):
            print( f'\nMonolithic Kernel loaded' )
            self.main()

    def load_services(self):
        print( f'Loading Kernel Services...')
        self.file_system.load_service()
    
    def main(self):
        print(f'Whatever comparisons we want run')



#
#   Base class for services
#
class Kernel_Service:
    def __init__(self, service_name, kernel):
        self.service_name = service_name #requires all kernel services to provide name and kernel object address
        self.kernel = kernel

    def load_service(self): #inherited by all child classes
        print(f'  Loading {self.service_name}...')

#
#   File System class
#
class File_System(Kernel_Service):
    def __init__(self, kernel):
        super().__init__("file_System", kernel) #instantiates parent class (must include service name), inherits load_service function
        self.file_dict = {} #dictionary to simulate file management

    def read_file(self, file_name):
        print(f'File_System: Reading from "{file_name}"...') #print file read message
        return self.file.get(file_name, "File not found") #.get method returns value of file_name key or "file not found" default
    
    def write_file(self, file_name, file_content):
        print(f'File_System: Writing to "{file_name}"...') #print file write message
        self.file[file_name] = file_content #add file_name (key) and file_content (value) pair to file dictionary
        return True



