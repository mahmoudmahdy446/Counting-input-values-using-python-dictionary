counts=dict()

def startprog():
    names=list()
    x=input('Enter Name :')
    if x=='done':
        quit('all done')
    else:
        names.append(x)
        for name in names:
            counts[name]=counts.get(name,0)+1
            print(counts)
        startprog()
        
startprog()
