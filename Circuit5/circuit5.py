from qiskit import *
import qiskit

theta = [i for i in range(100)]
rcxList = [i for i in range(80)]

class Circuit5:
    def __init__(self, qubits, layers, thetaList, crxList) -> None:
        self.qubits = qubits
        self.layers = layers
        self.thetaList = thetaList
        self.crxList = iter(crxList)
        self.qc = QuantumCircuit(qubits)
        for l in range(self.layers):
            for q in range(self.qubits):
                self.qc.rx(self.thetaList[2*l + self.qubits*q*2], q)
                self.qc.rz(self.thetaList[2*l+1 + self.qubits*q*2], q)
            ent = self.qubits-1
            for i in range(4):
                ent = self.qubits-1
                if i == 0 or i ==3:
                    while ent > 0:
                        self.qc.crx(next(self.crxList), ent, ent-1)
                        ent = ent -1  
                # if i == 1 or i ==2:
                #     while ent > 0:
                #         self.qc.crx(next(self.rcxList), ent, ent-1)
                #         ent = ent -1  
    def draw(self):
        print(self.qc)


Circuit5(4,4, theta, theta).draw()


