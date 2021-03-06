from subprocess import call
from os import remove

class __nasm__:

    def __init__(self):
        pass

    def __call__(self, code):
        f = '.inasm_tmp.asm'
        open(f, 'w').write(code)
        call(['nasm', f])
        try:
            open(f[:-4], 'r').close()
        except:
            return
        call(['ndisasm', f[:-4]])
        try:
            remove(f)
            remove(f[:-4])
        except:
            pass
