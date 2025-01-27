from ctypes import * 
from my_debugger_defines import * 
 
import sys 
import time 
kernel32 = windll.kernel32 
 
class debugger(): 
 
    def __init__(self): 
        self.h_process = None
        self.pid = None
        self.debugger_active = False 
                 
                 
    def load(self,path_to_exe): 
         
        # dwCreation flag determines how to create the process 
        # set creation_flags = CREATE_NEW_CONSOLE if you want 
        # to see the calculator GUI 
        creation_flags = DEBUG_PROCESS 
     
        # instantiate the structs 
        startupinfo        = STARTUPINFO() 
        process_information = PROCESS_INFORMATION() 
         
        # The following two options allow the started process 
        # to be shown as a separate window. This also illustrates 
        # how different settings in the STARTUPINFO struct can affect 
        # the debuggee. 
        startupinfo.dwFlags    = 0x1 
        startupinfo.wShowWindow = 0x0 
         
        # We then initialize the cb variable in the STARTUPINFO struct
        # which is just the size of the struct itself 
        startupinfo.cb = sizeof(startupinfo) 
         
        if kernel32.CreateProcessA(path_to_exe, 
                                          None, 
                                          None, 
                                          None, 
                                          None, 
                                creation_flags, 
                                          None, 
                                          None, 
                            byref(startupinfo), 
                     byref(process_information)): 
            print("[*] We have successfully launched the process!") 
            print("[*] The Process ID I have is: %d" % process_information.dwProcessId) 
            self.h_process = self.open_process(process_information.dwProcessId)
        else:     
            print("[*] Error with error code %d." % kernel32.GetLastError()) 
    def open_process(self, pid):
        h_process = kernel32.OpenProcess(PROCESS_ALL_ACCESS, pid, False)
        return h_process
    def open_thread(self, pid):
        h_thread = kernel32.OpenThread(THREAD_QUERY_INFORMATION, False, pid)
        return h_thread
    def attach(self, pid):
        self.h_process = self.open_process(pid)
        # Мы пытаемся прикрепиться к процессу 
        # если он проваливаемся мы отключаем вызов
        if kernel32.DebugActiveProcess(pid):
            self.debugger_active = True
            self.pid = int(pid)
        else:
            print("[*] Unable to attach to the process")
    def detach(self):
        if kernel32.DebugActiveProcessStop(self.pid):
            print("[*] finished debugging. Exiting...")
            return True
        else:
            print("There was an error")
            return False