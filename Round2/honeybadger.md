This write up is for the second set of challenges for Honey Badger

2-1 was to find the profile of the image
- vol.py -f /data/hunter.vmem imageinfo , then first result Win7SP1x86 matched

2-2 find the suspicious remote port
- vol.py -f /data/hunter.vmem --profile=Win7SP1x86_23418 netscan , there is a connection that is SYN_SENT

2-3 find the suspicious remote IP
- vol.py -f /data/hunter.vmem --profile=Win7SP1x86_23418 netscan , there is a connection that is SYN_SENT

2-4 find the PID that initiated this connection
- vol.py -f /data/hunter.vmem --profile=Win7SP1x86_23418 netscan , there is a connection that is SYN_SENT

2-5 start time for this suspicious process
- vol.py -f /data/hunter.vmem --profile=Win7SP1x86_23418 pslist, then look at PID 1572
2-6 PPID of the suspicious process from Honey Badger 2-5
- look at PPID for PID 1572
2-7 full path for the suspicious process from Honey Badger 2-6
- vol.py -f /data/hunter.vmem --profile=Win7SP1x86_23418 filescan | grep oiwwsi.exe
