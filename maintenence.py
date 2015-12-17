t_d = []
lineNum = 0
paths = []
nodes = {}
unimod = []
file = open('qq1.txt', 'r')

def makeDictStr(file):
    '''
        file: file object from which is the input to the program
        returns: a map of parents to their children
    '''
    for i, line in enumerate(file):
        line = line.rstrip().strip("';.")
        line = line.split()
        try:
            if line[0] in nodes:
                nodes[line[0]].append(line[1])
            else:
                nodes[line[0]] = []
                nodes[line[0]].append(line[1])
        except:
            t_d.append(line[0])
            continue
    
    # t_d[0] -> transaction to look at
    # t_d[1] -> defective module
    return nodes, t_d[0], t_d[1]


def findPath(nodes, key, defMod, lev, path=''):
    '''
        nodes: the map containing parent children pairs
        key:   the defective module name
        lev:   the level in the recursive call, used in tracking path
               directory structure.
        path:  path from root to defective module, is appended to pathlist
               after each successful find.
    '''
    if key in nodes and path.count(key) <= 1:
            path += key
            for ch in nodes[key]:
                # print(ch)!k
                if ch == defMod:
                    path += ch
                    paths.append(path)
                    path = path[:lev]
                else:
                    findPath(nodes, ch, defMod, lev+1, path)

def fmtPrint(ch, sp):
    '''
        ch: children of the upper parent module
        sp: spaces specified for correct print formatting
    '''
    for i in range (0,sp*2):
        print(" ", end=" ")
    print(ch)                

printed = []
def explode(nodes, trn, lev):
    '''
        nodes: the tree type structure
        trn:   the defective module
        lev:   level of the recursive call
    '''
    lev += 1
    if trn in nodes:
        for ch in nodes[trn]:
            if ch in printed:
                ch = ch + "*"
            fmtPrint(ch, lev)
            printed.append(ch)
            explode(nodes, ch, lev)
    else:
        pass

def uMod(list):
    for i, val in enumerate(list):
        unimod.append(val)
        try:
            uMod(nodes[val])
        except:
            continue
    return unimod
    
if __name__ == '__main__':
    nodes, trn, defMod = makeDictStr(file)
    
    print("Data structure: \n", nodes)
    findPath(nodes, trn, defMod, 1)  
    print("\n\n")
    
    print("Unique paths: \n",paths)
    print("\n\n")
    
    print("Explosion: \n")
    print(trn)
    explode(nodes, trn, 0)
    print("\n\n")
    
    umod = uMod(nodes[trn])
    umod.append(trn)
    print("Unique modules: \n", set(umod))
    print("No. of unique modules: \n", len(set(umod)))
    