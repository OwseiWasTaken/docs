#! /usr/bin/python3.9
#imports
from util import *


#main
def Main(argv) -> int:
        clear()
        argk = list(argv.keys())
        def get(*indicators:object, default = [], MakeBool = False) -> list:
                nonlocal argv,argk
                other = []

                for indicator in SingleList(indicators):
                        other = [*other, *argv.get(indicator,default)]

                if MakeBool and other:
                        return bool(eval(other[0]))
                return other

        colors = [col for col in color.keys() if "bk " in col]
        colors.remove("bk nc")
        HideCursor()
        x,y = GetTerminalSize()
        y+=11
        wait = 1
        try:
            num = float(get('-n')[0])
        except KeyError:
            pass
        line = " "*x
        while True:
# formating: '{name}' : '\003[{mode};{ColorCode}m'
# modes: 0:normal 1:bold? 2:dark 3:italics 4:underline 5:blinking 7:bkground 8:hidden
#'dark grey' : '\033[0;90m',


                #draw colors
                cn = ritem(colors)
                bc = cn
                tc = bc.replace("bk ","")
                bc = color[bc]
                if tc in ["grey","gray"]:
                    tc = "light grey"
                
                tc = color[tc]
                tc = SetColorMode(tc,'2')
                #ic = tc.find('[')+1
                #tc = list(tc)
                #tc[ic] = '2'
                #tc = ''.join(tc)
                

                printl(bc)
                for i in r(y):
                        printl(line)

                ##print(tc + pos(y//2-5,x/2-8) + "FELIZ ANIVERSÁRIO")
                #print(tc + pos(y//2-4,x/2-3) + "MIRELA")

                sleep(num)

        return 0





#start
if __name__ == '__main__':
        argv = ArgvAssing(argv[1:])
        start = tm()
        ExitCode = Main(argv)

        if '--debug' in argv.keys():
                if not ExitCode:printl("%scode successfully exited in " % color["green"])
                else:printl("%scode exited with error %d in " % (color["red"],ExitCode))
                print("%.3f seconds%s" % (tm()-start,color["nc"]))
        exit(ExitCode)
