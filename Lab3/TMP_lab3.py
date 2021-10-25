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
