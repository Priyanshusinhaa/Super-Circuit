import qiskit
from qiskit import *

theta = [i for i in range(32)]


class Circuit8:

    def __init__(self, qubits, layer, thetaList) -> None:
        self.qubits = qubits
        self.layer = layer -1
        self.theta = thetaList
        
        nbgates_0_last = self.countOdd(self.layer + 1)*2
        nbtheta = (nbgates_0_last*2) + (self.qubits-2)*((self.layer+1)*2)
        
        if (len(self.theta) > nbtheta):
            print('Given theta list is Greater than Required gates')
        elif (len(self.theta) == nbtheta):
            pass
        else:
            print("Number of Elements in theta list provided isn't equal to Gates required in Ansatz. Please check thetaList")
            raise
        
        if (self.qubits < 4) or (self.qubits%2 != 0):
            print('Qubit must be greater than 4 and qubit must be even')
            raise
        
        if ((self.layer + 1) <= 2) or ((self.layer+1)%2 != 1):
            print('Layer should always be greater than 2 and layer must be odd number')
        
        if type(self.qubits) != type(int):
            self.qubits = int(self.qubits)
        else:
            print("Please Check You're Entering Right DataType in place of 'Qubits' parameter")
            raise
    def countOdd(self, num):
        count = 0
        for i in range(0, num + 1):
            if i%2 == 1:
                count += 1
            else:
                pass
        return count

    def addAllAtIndex(self, mylist, index):
        a = mylist
        num = 0
        for i in range(0, index):
            num += a[i]
        return num
    
    def draw(self):

        qc = QuantumCircuit(self.qubits)
        
        nbgates_0_last = self.countOdd(self.layer + 1)*2
        nbgates_all = (self.layer+1)*2
        
        nbgates_at_each_layer = []
        for i in range(0, self.qubits):
            if i == 0 or i == self.qubits - 1:
                nbgates_at_each_layer.append(nbgates_0_last)
            else:
                nbgates_at_each_layer.append(nbgates_all)
        
        for i in range(0, self.layer + 1):
            if i%2 == 0: # apply first layer with entanglement
                j = 0
                ent = 0
                while j < self.qubits:
                    if j == 0:
                        qc.ry(self.theta[i], j)
                        qc.rz(self.theta[i+1], j)
                    elif j == self.qubits - 1:
                        qc.ry(self.theta[self.addAllAtIndex(nbgates_at_each_layer, j) + i], j)
                        qc.rz(self.theta[self.addAllAtIndex(nbgates_at_each_layer, j) + i + 1], j)
                    else: 
                        qc.ry(self.theta[self.addAllAtIndex(nbgates_at_each_layer, j) + i*2], j)
                        qc.rz(self.theta[self.addAllAtIndex(nbgates_at_each_layer, j) + i *2+ 1], j)   
                    j += 1
                if i != self.layer:
                    while ent < self.qubits:
                        qc.swap(ent, ent+1)
                        ent += 2
            else: 
                j = 0
                ent = 1
                while j < self.qubits:
                    if j == 0:
                        qc.i(j)
                        qc.i(j)            
                    elif j == self.qubits-1:
                        qc.i(j)
                        qc.i(j)            
                    else:
                        qc.ry(self.theta[self.addAllAtIndex(nbgates_at_each_layer, j) + i*2], j)
                        qc.rz(self.theta[self.addAllAtIndex(nbgates_at_each_layer, j) + i*2 + 1], j)
                    j += 1
                qc.i(0)
                while ent < self.qubits -1:
                    qc.swap(ent, ent+1)
                    ent += 2
                qc.i(self.qubits-1)
        print(qc)
        
Circuit8(4, 5, theta).draw()