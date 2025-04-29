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
        print( f'\nBooting Monolithic Kernel' )
        time.sleep(0.01) # 10ms kernel boot
        self.file_system = File_System(kernel=self) # initialize File_System with kernel address as parameter
        self.application_manager = Application_Manager(kernel=self) # initialize Application_Manager
        self.load_services()
        self.running = True
        if (self.running):
            print( f'Monolithic Kernel booted' )

    def load_services(self):
        print( f'   Loading Kernel Services...')
        time.sleep(0.005) # 5ms service manager startup
        self.file_system.load_service()
        self.application_manager.load_service()

    def system_call_handler(self, operation, *args):
        
        try:
            print(f"Monolithic Kernel: Received system call for \"{operation}\"")
            time.sleep(0.0002) # 0.2ms dispatch
            # no IPC required as all functions are called directly from kernel
            if operation == "read":
                return self.file_system.read_file(*args)
            elif operation == "write":
                return self.file_system.write_file(*args)
            else:
                raise ValueError(f'Monolithic Kernel: Invalid system call \"{operation}\"') # throws error if invalid system call
        except ValueError as error:
            print(error)
            print(f"Monolithic Kernel: Rebooting Kernel")
            time.sleep(0.005) # 5ms kernel teardown
            self.__init__()
            
    
    def create_application(self, application_name):
        return self.application_manager.create_application(application_name)
    
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
        print(f'   Loading {self.service_name}...')
        time.sleep(0.004) # 4ms service boot

#
#   File System class
#
class File_System(Kernel_Service):
    def __init__(self, kernel):
        super().__init__("file_system", kernel) # instantiates parent class (must include service name), inherits load_service function
        self.file_dict = {} # dictionary to simulate file management

    def read_file(self, file_name):
        print(f'File_System: Reading from "{file_name}"') # print file read message
        print(f'   Disk loading file into memory...\n'); time.sleep( .002 ) # wait for disk loading 2ms
        print(f'File_System: "{file_name}" read from successfully')
        return self.file_dict.get(file_name, "File not found") # .get method returns value of file_name key or "file not found" default
    
    def write_file(self, file_name, file_content):
        print(f'File_System: Writing to "{file_name}"') # print file write message
        print(f'   Disk writing to file...\n'); time.sleep( .0025 ) # wait for disk writing 2.5ms
        self.file_dict[file_name] = file_content # add file_name (key) and file_content (value) pair to file dictionary
        print(f'File_System: "{file_name}" writen to successfully')
        return True
    
#
#   Application Manager class
#
class Application_Manager(Kernel_Service):
    def __init__(self, kernel):
        super().__init__("application_manager", kernel)
        self.application_table = {} #dictionary to simulate application table

    def create_application(self, application_name):
        time.sleep(0.005) # 5ms application creation
        print(f'Application Manager: Creating user application "{application_name}"...')
        current_application = Monolithic_User_Application(self.kernel, application_name)
        self.application_table[application_name] = current_application
        return current_application

    def get_application(self, app_name):
        return self.application_table.get(app_name)


#
#   User Application class
#
class Monolithic_User_Application:
    def __init__(self, kernel, application_name):
        self.kernel = kernel
        self.application_name = application_name
    
    def system_call(self, operation, *args):
        if (operation == "read"):
            print(f'\nUser Application: Requesting File Read...')
        elif (operation == "write"):
            print(f'\nUser Application: Requesting File Write...')

        self.kernel.system_call_handler(operation, *args)



