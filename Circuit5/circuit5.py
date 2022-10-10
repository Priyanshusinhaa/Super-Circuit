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
            self.qc.barrier()

            for i in range(4):
                ent = self.qubits-1
                if i == 0 :
                    while ent > 0:
                        self.qc.crx(next(self.crxList), ent, ent-1)
                        ent = ent -1  
                    self.qc.barrier()
                if i == 1:
                    while ent > 0:
                        if ent != self.qubits-1:
                            self.qc.crx(next(self.crxList), ent, ent-1)
                        else:
                            self.qc.crx(next(self.crxList), ent-1, ent)
                        ent = ent -1  
                    self.qc.barrier()
                if i == 2:
                    while ent > 0:
                        if ent != 1:
                            self.qc.crx(next(self.crxList), ent-1, ent)
                        else:
                            self.qc.crx(next(self.crxList), ent, ent-1)
                        ent = ent -1  
                    self.qc.barrier()
                if i == 3:
                    while ent > 0:
                        self.qc.crx(next(self.crxList), 0, ent)
                        ent = ent -1  
                    self.qc.barrier()

            
    def draw(self):
        print(self.qc)


Circuit5(6,1, theta, theta).draw()


