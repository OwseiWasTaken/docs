#! /usr/bin/python3.9
#imports
from util import r,ss,sleep,tm,argv,rint,pos,ClearLine

#main
def main(argv):
    cells = []
    class cell:
        def __init__(self,x,y,alive=True):
            self.x = x
            self.y = y
            self.alive = alive
            cells.append(self)
        def next_gen(self,alive):
            self.nxt_alive = alive

        def next(self):
            self.alive = self.nxt_alive

        def __repr__(self):
            if self.alive:
                return '■'
            else:
                return '□'
        def __call__(self):
            return self.alive

    X,Y = 60,60
    mp = [[x for x in r(X)] for x in r(Y)]
    for x in r(mp):
        for y in r(mp[x]):
            # starting cell selection
            mp[x][y] = cell(x,y,rint(0,1))
            # if f'{x},{y}' in argv:
            # else:
                # mp[x][y] = cell(x,y,0)

    def neighbors(cell):
        nonlocal mp
        j=0
        tps=[
        ['+1' ,'+1']
        ,[''	  ,'+1']
        ,['-1' ,'+1']
        ,['+1' ,'']
        ,['-1' ,'']
        ,['+1' ,'-1']
        ,[''	  ,'-1']
        ,['-1' ,'-1']
        ]
        for i in tps:
            try:
                j+=eval(f'mp[cell.x{i[0]}][cell.y{i[1]}]()')
            except IndexError:pass
        return j

    try:
        ss('clear')
        while True:
            ClearLine(y+3)
            print(pos(1,1))

            #[print(f'{i+1}:\t{str(mp[i])[1:-2]}\t:{i+1}') for i in r(mp)]
            [print("%s:\t%s\b\t:%s" % (i+1,str(mp[i])[1:-2],i+1)) for i in r(mp)]
            if 'sbs' in argv:
                if input() == 'c':ss("clear")
            else:
                sleep(ms=300)
            for cli in mp:
                for cl in cli:
                    # rules
                    ney=neighbors(cl)
                    if 2 > ney or ney > 3:
                        cl.next_gen(False)
                    elif ney == 3:
                        cl.next_gen(True)
                    else:
                        cl.next_gen(cl())

            # todo: for x \n for y if neighbors = [x-1,y+1....]

            [cl.next() for cl in cells]
            # ss('clear')


    except KeyboardInterrupt:pass
    return 0

#start
if __name__ == '__main__':
    nc = '\033[0m'
    start = tm()

    name = argv.pop(0)
    debug = '--debug' in argv
    if debug:
        argv.remove('--debug')

    exit_code = main(argv)

    if debug:
        if exit_code:
            printf(f'{color("red")}code exited with error {exit_code} in {round(tm()-start,5)} seconds{nc}')
        else:
            printf(f'{color("green")}code successfully exited in {round(tm()-start,5)} second{nc}')
    exit(exit_code)
