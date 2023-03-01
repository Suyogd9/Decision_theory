import sys

class Decision_tree:
    Ch_dict = {}
    lot_dict = {}
    op_dict = {}
    inc = 0
    node_no = 0

    #Inner class so that node exists if its a decision tree hiding the node details
    class Node():
        def __init__(self, name, N_type, parent, number):
            self.name = name
            self.type = N_type
            self.parent = parent
            self.number = number

    #Reading input file into choice, lottery and outcome dictionary
    def read_file(self, input_file):
        with open(input_file) as pblm:
            text = pblm.readlines()
        for i in range(len(text)):
            temp_val = []
            temp_lot = []
            if text[i][0:6] == 'CHOICE':
                splt = text[i].split(":")[1].strip('\n')
                for j in range(i+1, len(text)):
                    if "ENDCHOICE" in text[j]:
                        break
                    else:
                        val = text[j].strip('\n').split(":")
                        val1 = val[1].lstrip().split(" ")
                        temp_val.append(val1)
                        self.Ch_dict[splt[1:]] = temp_val
            if text[i][0:7] == 'LOTTERY':
                splt_lot = text[i].split(":")[1].strip('\n')
                for j in range(i+1, len(text)):
                    if "ENDLOTTERY" in text[j]:
                        break
                    else:
                        vlot = text[j].strip('\n').split(":")
                        vlot1 = vlot[1].lstrip().split(" ")
                        temp_lot.append(vlot1)
                        self.lot_dict[splt_lot[1:]] = temp_lot
            if text[i][0:7] == 'OUTCOME':
                splt_OC = text[i].split(":")[1].strip().split(" ")
                self.op_dict[splt_OC[0]] = splt_OC[1]
        self.graph_build('Start', None)                  # Function call to build a graph
        print('---------------------------------------')
        self.exp_values('Start')                         # Function call to calculate expected values

    #Building graph using recursion
    def graph_build(self, src, parent):
        if src in self.Ch_dict.keys():
            self.inc += 1
            ch_temp = self.Ch_dict[src]
            obj_node = self.Node(src, 'decision', parent, self.inc)
            print("Adding Node " + str(self.inc) + " " +
                  obj_node.type + " " + src + " " + str(obj_node.parent))
            for ch in ch_temp:
                obj_node.parent = src
                self.graph_build(ch[1], obj_node.parent)
        if src in self.lot_dict.keys():
            self.inc += 1
            lot_temp = self.lot_dict[src]
            obj_node = self.Node(src, 'Lottery', parent, self.inc)
            print("Adding Node " + str(self.inc) + " " +
                  obj_node.type + " " + src + " " + str(obj_node.parent))
            for lt in lot_temp:
                obj_node.parent = src
                self.graph_build(lt[2], obj_node.parent)
        if src in self.op_dict.keys():
            self.inc += 1
            obj_node = self.Node(src, 'Outcome', parent, self.inc)
            print("Adding Node " + str(self.inc) + " " +
                  obj_node.type + " " + src + " " + str(obj_node.parent))

    #Calculating expected values
    def exp_values(self,exp_var):
        if exp_var in self.Ch_dict.keys():
            nv={}
            self.node_no += 1
            obj_ch = self.Node(exp_var,"Decision",None,self.node_no)
            for ch in self.Ch_dict[exp_var]:
                nv[ch[0]] = self.exp_values(ch[1])
            x = max(nv.values())                                    #Taking maximum of two values at decision node
            keys = [k for k, v in nv.items() if v == x]
            final_decision = keys[0]
            print("Decision Node:"+" "+str(obj_ch.number)+","+obj_ch.name+" "+str(final_decision)+" "+str(nv[final_decision]) )
            return nv[final_decision]
        if exp_var in self.lot_dict.keys():
            sum = 0
            self.node_no += 1
            obj_lot = self.Node(exp_var,"Lottery",None,self.node_no)
            for lot in self.lot_dict[exp_var]:
                sum += float(lot[1]) * float(self.exp_values(lot[2]))   #Calulating expected values
            print("Expected Value Node:" +" "+ str(obj_lot.number)+","+obj_lot.name+" "+str(sum))
            return sum
        if exp_var in self.op_dict.keys():
            self.node_no += 1
            obj_op = self.Node(exp_var,"Outcome",None,self.node_no)
            op_value = float(self.op_dict[exp_var])
            print("Outcome :" + str(self.node_no) + " " + obj_op.name + " " + str(op_value))
            return op_value

dt = Decision_tree()
input_file = str(sys.argv[1])
dt.read_file(input_file)
