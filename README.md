# OS_Comparison

Comparison of Monolithic and Microkernel Operating Systems

## File Structure

- **main.py** contains the implementation of our OSes and comparisons.
- **comparisons.py** contains the comparison functions that will be used in the main.
- **MicroKernel_Implementation.py** contains the implementation of the MicroKernel class and its functions.
- **Monolithic_Implementation.py** contains the implementation of the Monolithic class and its functions.

## Comparisons Impementations

### 1) IPC Performance

#### What to Measure

- The time it takes the Microkernel to pass a message between modules.
- How much overhead is added for message relays in Microkernels.

#### Takeaway

- Microkernels can be slower even for simple operations due to communication costs.

#### How

- Start the user application and make a request to access a file.
- Monolithic will directly communicate with the file system (doesn't require IPC).
- Microkernel messages will look like: application -> kernel -> filesystem -> kernel -> application.
- Measure each IPC time and return the sum for each OS (add sleep timer for IPC).

#### Alternate How

- This scenario will be user application to user application.
- This will make it so that both OSes will use IPC between applications.
- Mono will directly IPC between the applications.
- Micro will: application -> kernel -> application.

#### Services Needed

- user_application()		# fake user application to make requests to kernel
  - request_file()
- filesystem()			# fake filesystem
  - read_file()
- IPC( A, B )			# message from A to B
- user_application_2()	# if alternate how is used

### 2) System Call Performance

#### What to Measure

- The time it takes for an app to complete an operation that needs the kernel (via system call).
- How much overhead is added for system calls in microKernels.
- System Call overhead will consist of additional IPC required for Microkernel. In Monolithic, no IPC, just internal function calls.

#### Takeaway

- Unlike in a Monolithic OS, system call doesn't go directly to the kernel function. Microkernel OS has to go through multiple modules.

#### How

- Same scenario as IPC, but include write file as well. This will simulate an additional system call to emphasize overhead created for two system calls rather than one.
- Return the total times for system calls and IPC.
- For Mono, total time will just be the system calls and function calls. Make sure function call times are less than IPC times.

#### Services Needed

- user_application()	# fake application
  - request_file()
- filesystem()		# fake filesystem
  - read_file()
- IPC( A, B )		# only for MicroKernel

### 3) Code Complexity and Size

#### What to Measure

- The size of the kernel and user layer in both OSes.
- How many modules inside the kernel and user layers in both OSes.

#### Takeaway

- Microkernels are more modular.

#### How

- Screenshots of code and some metrics should be sufficient.

#### Services Needed

- No additional services needed.

### 4) Fault Isolation

#### What to Measure

- Crash severity when a service crashes (eg. Device Driver).
- How long it takes to recover.
- How much of the system is affected.

#### Takeaway

- Microkernels have better crash stability and recovery.
- Recovery depends on the extent of the crash, but if the whole Monolithic OS crashes, it would take longer to recover than just the Microkernel service that crashed.

#### How

- filesystem tries readfile(), but raise an exception due to file missing.
- for Mono, set a flag to signify the kernel is dead (OS crashed), crashing the OS.
  - then restart the OS, will take more time for Mono to recover due to more services being re-loaded.
- for Micro, crash the filesystem service, then restart the service. OS stays stable.
