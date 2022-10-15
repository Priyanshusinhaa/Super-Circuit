from qiskit import *
import qiskit

theta = [i for i in range(100)]
rcxList = [i for i in range(80)]

class Circuit5:
    def __init__(self, qubits, thetaList, crzList) -> None:
        self.qubits = qubits
        self.thetaList = thetaList
        self.crzList = iter(crzList)
        self.qc = QuantumCircuit(qubits)
        self.qc2 = QuantumCircuit(qubits)
        a = 0
        for q in range(self.qubits):
            self.qc.rx(self.thetaList[a], q)
            self.qc.rz(self.thetaList[a+1], q)
            self.qc2.rx(self.thetaList[a+2], q)
            self.qc2.rz(self.thetaList[a+3], q)
            a += 4
        self.qc.barrier()

        for i in range(4):
            ent = self.qubits-1
            if i == 0 :
                while ent > 0:
                    self.qc.crz(next(self.crzList), ent, ent-1)
                    ent = ent -1  
                self.qc.barrier()
            if i == 1:
                while ent > 0:
                    if ent != self.qubits-1:
                        self.qc.crz(next(self.crzList), ent, ent-1)
                    else:
                        self.qc.crz(next(self.crzList), ent-1, ent)
                    ent = ent -1  
                self.qc.barrier()
            if i == 2:
                while ent > 0:
                    if ent != 1:
                        self.qc.crz(next(self.crzList), ent-1, ent)
                    else:
                        self.qc.crz(next(self.crzList), ent, ent-1)
                    ent = ent -1  
                self.qc.barrier()
            if i == 3:
                while ent > 0:
                    self.qc.crz(next(self.crzList), 0, ent)
                    ent = ent -1  
                self.qc.barrier()
        self.qc3 = self.qc + self.qc2

    def draw(self):
        print(self.qc3)

    def getCircuit(self):
        return self.qc
    
    def statevector(self):
        simu_sv = BasicAer.get_backend('statevector_simulator')
        sv = execute(self.qc, simu_sv).result().get_statevector()
        if type == 'print':
            print(sv)
        return sv
    
    def counts(self, type = None):
        simu_sv = BasicAer.get_backend('statevector_simulator')
        counts = execute(self.qc, simu_sv).result().get_counts()
        if type == 'print':
            print(counts)
        return counts

def main():
    Circuit6(9, theta, theta).draw()

    pass

if __name__ == '__main__':
    main()


