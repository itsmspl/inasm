from help import __help__

if __name__ == '__main__':

    mode = 'asm'

    while 1:
        
        try:
            i = input('%s> ' % mode).strip()
        except:
            exit()

        if i == '.help':
            print(__help__)

        elif i.startswith('.mode'):
            nm = i[5:].strip()
            if nm == '':
                mode = 'disasm' if mode == 'asm' else 'asm'
            elif nm == 'asm':
                mode = 'asm'
            elif nm == 'disasm':
                mode = 'disasm'
            else:
                print('error: unknown mode\n')
        
        else:
            if mode == 'asm':
                pass
            elif mode == 'disasm':
                pass
