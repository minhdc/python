'''
Created on Jan 23, 2018

@author: extre_000
'''
import my_debugger

debugger = my_debugger.debugger()

pid = input("enter the PID of the process to attach to...")

debugger.attach(int(pid))

list = debugger.enumerate_thread()
print("list = ",list)
#grab & show value of some register
for thread in list:
    thread_context = debugger.get_thread_context(thread)
    print("[*] dumping register for thread ID 0x%08x"%thread)
    print("[**] EIP : 0x%08x "%thread_context.Eip)
    print("[**] ESP : 0x%08x "%thread_context.Esp)
    print("[**] EBP : 0x%08x "%thread_context.Ebp)
    
    print("[**] EAX : 0x%08x "%thread_context.Eax)
    print("[**] EBX : 0x%08x "%thread_context.Ebx)
    print("[**] ECX : 0x%08x "%thread_context.Ecx)
    print("[**] EDX : 0x%08x "%thread_context.Edx)
    print("[*] END DUMPP")

debugger.detach()

#
#path_to_file = "C:\Windows\System32\calc.exe"
#debugger.load(path_to_file)