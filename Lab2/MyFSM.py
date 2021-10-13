
from itertools import chain
from FSMtoGraph import Matter
from transitions.extensions import GraphMachine

def f4(seq):
   # order preserving
   noDupes = []
   [noDupes.append(i) for i in seq if not noDupes.count(i)]
   return noDupes

class Node:
    def __init__(self, num, terminate, trans):
        self.state_num = num
        self.transitions = trans
        self.terminate = terminate

    def addTransition(self, c, ref):
        self.transitions.append([c, ref])

    def __str__(self):
        if(self.terminate):
            return str(self.state_num) +  "#" + str(self.transitions) + " * "
        else:
            return str(self.state_num) +  "#" + str(self.transitions)



class MyStateMachine:
    def __init__(self, nodes, start_state):
        self.state = start_state
        self.nodes = nodes
        self.terminate = nodes[0].terminate

    def get_state(self, c):
        for t in self.nodes[self.state].transitions:
            if(t[0] == c):
                return t[1]
        return -1


    def getRemovedNodeTrans(self, c, trans):
        new_trans = []
        nodes = []
        for t in trans:
            if(t[0]==c):
                nodes.append(t[1])
        #print(nodes)
        for node in nodes:
            new_trans.append(self.nodes[node].transitions)
        new_trans = list(chain.from_iterable(new_trans))
        print(self.nodes[node]);

        new_state = int("".join(str(x) for x in nodes))
        self.addNode(new_state, new_trans, False)

        self.checkNodes(nodes, new_state)
        self.removeDuplicates()
        return nodes

    def addNode(self, state, transitions, terminate):
        self.nodes[state] = Node(state, terminate, transitions)

    def removeNodes(self, nodes):
        if(nodes != type(None)):
            for node in nodes:
                del self.nodes[node]

    def removeDuplicates(self):
        for node in self.nodes:
            self.nodes[node].transitions = f4(self.nodes[node].transitions)

    def checkNodes(self, check_list, new_state):
        for node in self.nodes:
            for i, t in enumerate(self.nodes[node].transitions):
                for s in check_list:
                    if(t[1]==s):
                        self.nodes[node].transitions[i][1]=new_state


    def check_nfa_cast_to_dfa(self):
        k=0
        f=False
        for node in self.nodes:
            for i_1, t_1 in enumerate(self.nodes[node].transitions):
                for i_2, t_2 in enumerate(self.nodes[node].transitions):
                    if(t_1[0]==t_2[0]):
                        k+=1
                    if (k > 1):
                        return self.getRemovedNodeTrans(t_1[0], self.nodes[node].transitions)
                k = 0
        #self.printNodes()

    def printNodes(self):
        print("==========================")
        for n in self.nodes:
            print(self.nodes[n])
        print("==========================")

    def getStates(self):
        states = []
        for node in self.nodes:
            states.append(str(node))
        return states

    def getTransitions(self):
        transitions = []
        for node in self.nodes:
            for t in self.nodes[node].transitions:
                transitions.append([str(t[0]),str(node),str(t[1])])
        return transitions

    def plotGraph(self, img_name):
        model = Matter()

        machine = GraphMachine(model=model,
                               states=self.getStates(),
                               transitions=self.getTransitions(),
                               initial='0',
                               show_auto_transitions=False,  # default value is False
                               title="Lab2",
                               show_state_attributes=True,
                               show_conditions=True)
        model.show_graph(img_name)

    def start(self, string):
        self.plotGraph('before')
        self.printNodes()
        while True:
            rn = self.check_nfa_cast_to_dfa()
            if(rn):
                self.removeNodes(rn)
            else:
                break
        self.printNodes()

        for c in string:
            state = self.get_state(c)
            if(state!=-1):
                print(str(self.state) + " -> " + str(state) + "  char: " + c)
                self.state = state
                self.terminate = self.nodes[state].terminate
            else:
                print("Bad Input String!")
        if(self.terminate == True and len(string)>0):
            print("Success!")
            self.plotGraph('after')
        else:
            print("ERROR! Stop in non-final state or an empty string.")
        #
        # return self.getStates(), self.getTransitions()

