from MyFSM import Node, MyStateMachine
from re import compile


#s = "if(a>b)"
# s = "if(a>(b+c)]"
s = "aef"

# s = ";ab -> [ ] -> + -> [ ] -> cd -> [ ] -> * -> [ ] -> [e] -> [ ] -> = -> [ ] -> 357"
#s = ";ba"
#s = "ab+cd*eeeee  357"

nodes = {}


with open('input.txt', 'r') as in_schem:
    text = in_schem.read().splitlines()

print("READ FROM FILE ->")
print(text)
print("--------------------------------")

re_n = compile(r'(.)(\d+),(.)=(\w)(\w+)')

print("STATES:")

for node in text:
    try:
        print(node)
        res = re_n.match(node)
        state = int(res.group(2))
        c = res.group(3)
        #print(res.group(1))
        if(res.group(1) == 'q'):
            final = False
        else:
            final = True

        ref = int(res.group(5))

        if (nodes.__contains__(state)):
            nodes[state].addTransition(c, ref)
        else:
            nodes[state] = Node(state, final, [[c, ref]])

    except:
        print("INPUT FILE ERROR!!!")



print("--------------------------------")


MyStateMachine(nodes, 0).start(s)


