This write-up is related to the Memory Fundamentals challenges.

4 : 32 bit CPU register stores the address of the next instruction to be executed
- EIP
5 : 64 bit CPU register stores the address of the next instruction to be executed
- RIP
13 : what environment variable can you set to avoid having to type "--profile=" and the OS version each time you run Volatility
- VOLATILITY_PROFILE
14 : what environment variable can you set to avoid having to type the path and name of the memory image each time you run Volatility
- VOLATILITY_LOCATION
19 : highest number that all Windows PIDs are divisible by
- 4 
20 : E in the EAX register stand for
- Extended
21 : how much RAM can a 16 bit system utilize
- 64 kb 
22 : How much RAM can a 32 bit system with a processor that supports Physical Address Extension utilize
- 64 GB 
23 : how much can actually be addressed by the latest AMD64 specification
- 256 TB
15 : when user mode applications call system level APIs, the address of the API in kernel memory is resolved using a table of pointers
- System Service Descriptor Table
16 : System Service Descriptor Table Shadow calls this AP
- win32k.sys
12 : the name of the user logged in Session 0
- python vol.py -f /data/sample005.bin --profile=Win2003SP0x86 consoles ( and then look for C:\Documents and Settings\<user>)
10 : hidden process has been unlinked from a linked list that the OS uses to track active processes. What is the name of this list
- PsActiveProcessHead (look at psxview for Volatility)
24 : KDBG "magic number" for Windows Server 2008
- 0x00000000000000004b4442473003 (found with https://github.com/libvmi/libvmi/blob/master/libvmi/os/windows/kdbg.c)

6 : What is the corresponding physical offset for this data
- Execute following commands
  - python vol.py -f /data/sample001.bin --profile=WinXPSP3x86 volshell
  - cc(pid=628)
  - proc().get_process_address_space().vtop(0x77a80000)
2 : subsystem of modern processors acts as a cache to the MMU in order to avoid costly translation operations in order to find physical addresses
- translation lookaside buffer
27 : How many null terminated strings of >=10 characters in little endian and big endian format are found in sample001.bin
- strings -el -10 sample001.bin | wc -l --> little endian, strings -eb -10 sample001.bin | wc -l --> big endian
