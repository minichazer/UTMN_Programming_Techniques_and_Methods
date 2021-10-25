'''

класс, 2 метода (запись и чтение из файла) 

массив байт в метод, имя к файлу, мод записи (аргумент) 

чтение и запись через системные вызовы (kernel32.dll; create file, read file, )






1 000 000 строк - f.write и f.read питона и собственный статический класс и вызов напрямую из kernel32.dll

'''

from ctypes import *
from ctypes import wintypes as w
import time
from datetime import datetime



def CreateFile(file_name='',data=''):
    file_handler = _CreateFileA(file_name,GENERIC_ALL,0,None,OPEN_ALWAYS,FILE_ATTRIBUTE_NORMAL,None)
    written = w.DWORD()
    try:
        _WriteFile(file_handler,data,len(data),byref(written),None)
    finally:
        _CloseHandle(file_handler)

def ReadAFile(file_name=''):
    file_handler = _CreateFileA(file_name,GENERIC_ALL,0,None,OPEN_ALWAYS,FILE_ATTRIBUTE_NORMAL,None)
    data = create_string_buffer(4096)
    read = w.DWORD()
    try:
        _ReadFile(file_handler,byref(data),1024,byref(read),None)
    finally:
        _CloseHandle(file_handler)
    # print(data.value)

def validate_handle(result,func,args):
    if result == INVALID_HANDLE_VALUE:
        raise WindowsError(get_last_error())
    return result

def validate_bool(result,func,args):
    if not result:
        raise WindowsError(get_last_error())


INVALID_HANDLE_VALUE = w.HANDLE(-1).value
GENERIC_ALL = 0x10000000
OPEN_ALWAYS = 4
FILE_ATTRIBUTE_NORMAL = 0x80


_k32 = WinDLL('kernel32',use_last_error=True)
_CreateFileA = _k32.CreateFileA
_WriteFile = _k32.WriteFile
_ReadFile = _k32.ReadFile
_CloseHandle = _k32.CloseHandle


""" _CreateFileA.argtypes = w.LPCSTR,w.DWORD,w.DWORD,c_void_p,w.DWORD,w.DWORD,w.HANDLE
_CreateFileA.restype = w.HANDLE
_CreateFileA.errcheck = validate_handle
_WriteFile.argtypes = w.HANDLE,c_void_p,w.DWORD,POINTER(w.DWORD),c_void_p
_WriteFile.restype = w.BOOL
_WriteFile.errcheck = validate_bool
_ReadFile.argtypes = w.HANDLE,w.LPVOID,w.DWORD,POINTER(w.DWORD),c_void_p
_ReadFile.restype = w.BOOL
_ReadFile.errcheck = validate_bool
_CloseHandle.argtypes = w.HANDLE,
_CloseHandle.restype = w.BOOL
_CloseHandle.errcheck = validate_bool """













n = 1000


print("Времени прошло:")
start_1w = time.process_time()
for i in range(n):
  with open('strings.txt', 'w') as f:
    f.write(str(i))
print(f'Запись в файл: {time.process_time() - start_1w}')

start_1r = time.process_time()
for i in range(n):
  f = open('strings.txt').readlines()
print(f'Чтение файла: {time.process_time() - start_1r}')


start_2w = time.process_time()
for i in range(n):
  CreateFile('strings2.txt', str(i))
print(f'Запись в файл (ctypes): {time.process_time() - start_2w}')

start_2r = time.process_time()
for i in range(n):
  ReadAFile('strings2.txt')
print(f'Чтение файла (ctypes): {time.process_time() - start_2r}')






















"""
def ReadFile(handle, desired_bytes):
  # Calls kernel32.ReadFile().
  c_read = wintypes.DWORD()
  buff = wintypes.create_string_buffer(desired_bytes+1)
  windll.kernel32.ReadFile(
      handle, buff, desired_bytes, wintypes.byref(c_read), None)
  # NULL terminate it.
  buff[c_read.value] = '\x00'
  return wintypes.GetLastError(), buff.value





def shared_open(path):
  #Opens a file with full sharing mode and without inheritance.
 
 # The file is open for both read and write.
 
  #See https://bugs.python.org/issue15244 for inspiration.
  
  path = unicode(path)
  handle = ctypes.windll.kernel32.CreateFileW(
      path,
      GENERIC_READ|GENERIC_WRITE,
      FILE_SHARE_READ|FILE_SHARE_WRITE|FILE_SHARE_DELETE,
      None,
      OPEN_ALWAYS,
      FILE_ATTRIBUTE_NORMAL,
      None)
  ctr_handle = msvcrt.open_osfhandle(handle, os.O_BINARY | os.O_NOINHERIT)
  return os.fdopen(ctr_handle, 'r+b')




"""