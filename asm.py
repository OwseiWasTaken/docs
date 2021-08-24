#! /usr/bin/python3.9
#imports
from util import *


#main
def Main(argv) -> int:
        argk = list(argv.keys())
        def     get(*indicators:object) -> list:
                nonlocal argv,argk
                other = []
                for indicator in indicators:
                        other = [*other, *argv[indicator]] if indicator in argk else other
        #               if indicator in argk:
        #                       other.append(argv[indicator])
                return other

        printl(COLOR.BrRed)
        


        FileIn = lst1(get("-i","-I","--input"))
        if not ss("nasm -f elf32 %s -o program.obj" % (FileIn)):
                if not ss("ld -m elf_i386 -o %s.run program.obj" % (FileIn[:-4])):
                        if not ss("rm program.obj"):
                                sout.write("%s%s compile sucessfuly as %s.run" % (color["green"],FileIn,FileIn[:-4]))
                        else:
                                sout.write("failed to remove .obj w/ \n")
                                sout.write("rm program.obj")
                else:
                        sout.write("failed to compile .obj w/ \n")
                        sout.write("ld -m elf_i386 -o %s.run program.obj" % (FileIn[:-4])) 
        else:
                sout.write("failed to create .obj w/ \n")
                sout.write("nasm -f elf32 -o program.obj %s" % (FileIn)) 

        sout.write('%s\n'%color["nc"])
        sout.flush()
        
        return 0






#start
if __name__ == '__main__':
        argv = ArgvAssing(argv[1:])
        start = tm()
        ExitCode = Main(argv)

        if '--debug' in argv.keys():
                if not ExitCode:printl("%scode successfully exited in " % color["green"])
                else:printl("%scode exited with error %d in " % (color["red"],ExitCode))
                print("%.3f seconds%s" % (round(tm()-start,5),color["nc"]))
exit(ExitCode)
