import time


"""
This file contains the implementation of the Microkernel class and its functions.
"""


#
#   Microkernel class
#
class Microkernel:

    # constructor
    def __init__(self):
        print(f'\nBooting Microkernel')
        time.sleep(0.01) # 10ms kernel boot
        self.kernel_services = []
        self.user_services = []
        self.running = True

        self.service_dict = {
            "read": "file_system",
            "write": "file_system",
            "read_fault": "file_system"
        }

    # register kernel services to give access to kernel
    def register_kernel_service(self, service):
        self.kernel_services.append(service)
        service.kernel = self

    # register user services to give access to kernel
    def register_user_service(self, service):
        self.user_services.append(service)
        service.kernel = self

    # IPC service
    def IPC(self, message):
        time.sleep(.001)    # set IPC time to 1ms
        for service in self.kernel_services + self.user_services:
            if service.service_name == message.receiver:
                print(f'IPC: {message.sender} -> {message.receiver}: \"{message.operation}\"')
                # try:
                #     service.receive_IPC(message)
                # except ValueError as error:
                #     print(error)
                #     print(f'Microkernel: Rebooting {message.receiver}')
                #     self.crash_recovery(message.receiver)
                    


    def SysCall(self, sender, operation, *args):
        time.sleep(.0002) # set SysCall time to .2ms

        print(f'Microkernel: System call for \"{operation}\" received')
        receiver = self.service_dict.get(operation)

        # if receiver:
        #     self.IPC(IPC_Message(sender, receiver, operation, args))
        # else:
        #     raise ValueError(f'Microkernel: Invalid system call \"{operation}\"') # throws error if invalid system call
        # In real microkernels, some system calls may be handeled by the kernel rather than IPC
    
    def crash_recovery(self, service_name):
        time.sleep(0.002) # 2ms service teardown
        for service in self.kernel_services:
            if service.service_name == service_name:
                self.kernel_services.remove(service)
                new_system = File_System()
                self.register_kernel_service(new_system)
                new_system.load_service()

        for service in self.user_services:
            if service.service_name == service_name:
                self.user_services.remove(service)
                new_system = File_System()
                self.register_user_service(new_system)
                new_system.load_service()




    # Start OS
    def start_Micro(self):
        print( f'   Loading Microkernel...' )

        time.sleep(0.005) # 5ms service manager startup
        print( f'   Starting System Service manager...' )
        print( f'       Loading Core Services...' )
        
        for service in self.kernel_services:
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
    def __init__(self, service_name):
        self.service_name = service_name
        self.kernel = None
        time.sleep(0.004) # 4ms service boot

    def load_service(self):
        print(f'                Loading {self.service_name}...')
        time.sleep(0.004) # 4ms service boot
    
    # def receive_IPC(self, message):
    #     print(f"{self.service_name} received IPC: operation='{message.operation}', args={message.args}")


#   Kernel Service class
class Kernel_Service(Service):
    pass


#   User Service class
class User_Service(Service):
    pass


#
#   File System class
#
class File_System(Service):
    # def __init__(self):
    #     super().__init__("file_system")
    #     self.file_dict = {}

    def read_file(self, file_name):
        print(f'File_System: Reading from "{file_name}"')
        print(f'   Disk loading file into memory...')
        time.sleep(0.002)
        print(f'File_System: "{file_name}" read successfully')
        return self.file_dict.get(file_name, "File not found") # in real microkernel, would be sent as IPC message

    def write_file(self, file_name, file_content):
        print(f'File_System: Writing to "{file_name}"')
        print(f'   Disk writing to file...')
        time.sleep(0.0025)
        self.file_dict[file_name] = file_content
        print(f'File_System: "{file_name}" written to successfully')
        return True # in real microkernel, would be sent as IPC message

    def receive_IPC(self, message):
        print(f"File_System: IPC for \"{message.operation}\" received")

        if message.operation == "read":
            file_name = message.args[0]  # unpack first argument
            return self.read_file(file_name)
        elif message.operation == "write":
            file_name = message.args[0]   # first argument
            file_content = message.args[1]  # second argument
            return self.write_file(file_name, file_content)
        elif message.operation =="read_fault":
            raise ValueError(f'Monolithic Kernel: Invalid system call \"{message.operation}\"') # throws error if invalid system call


#
#   User Application class
#
class User_Application(Service):
    def system_call(self, operation, *args):
        if (operation == "read"):
            print(f'\nUser Application: Requesting File Read...')
        elif (operation == "write"):
            print(f'\nUser Application: Requesting File Write...')

        self.kernel.SysCall(self.service_name, operation, *args)

#
#   Message class (used for IPC)
#
class IPC_Message:
    def __init__(self, sender, receiver, operation, args=None):
        self.sender = sender
        self.receiver = receiver
        self.operation = operation
        self.args = args or []
