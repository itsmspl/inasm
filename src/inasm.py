from help import __help__
from asm import __nasm__
from disasm import __ndisasm__

if __name__ == '__main__':

    mode = 'asm'
    asm = __nasm__()
    disasm = __ndisasm__()

    while 1:
        
        try:
            i = input('\n%s> ' % mode).strip()
        except:
            exit('^C')

        if i == '.help':
            print(__help__)

        elif i.startswith('.mode'):
            nm = i[5:].strip()
            if nm == '':
                mode = 'disasm' if mode == 'asm' else 'asm'
            elif nm == 'a':
                mode = 'asm'
            elif nm == 'd':
                mode = 'disasm'
            else:
                print('error: unknown mode')
        
        else:

            if mode == 'asm':
                asm(i)

            elif mode == 'disasm':
                disasm(i)
