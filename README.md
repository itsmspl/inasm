# Interactive shell of NASM.

```asm
$ python3 inasm.py

asm> mov eax, 0x12345678  
00000000  66B878563412      mov eax,0x12345678

asm> xor ecx, edx
00000000  6631D1            xor ecx,edx

asm> .mode d

disasm> 66B8785634126631D1
00000000  66B878563412      mov eax,0x12345678
00000006  6631D1            xor ecx,edx
```
