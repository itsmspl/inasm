from subprocess import call
from os import remove

class __ndisasm__:

    def __init__(self):
        pass

    def __call__(self, code):
        f = '.inasm_tmp'
        b = bytearray()
        for i in range(len(code)//2):
            b += bytearray([int(
                code[i*2:(i+1)*2], 16)])
        open(f, 'wb').write(b)
        call(['ndisasm', f])
        remove(f)
