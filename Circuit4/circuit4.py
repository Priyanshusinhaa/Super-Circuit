from qiskit import *

theta = [i for i in range(100)]
crxList = [i for i in range(80)]

class Circuit4:
    def __init__(self, qubits, layers, thetaList, crxList) -> None:
        self.qubits = qubits
        self.layers = layers
        self.thetaList = thetaList
        self.crxList = iter(crxList)
        self.qc = QuantumCircuit(self.qubits)
        for l in range(self.layers):
            for q in range(self.qubits):
                self.qc.rx(self.thetaList[2*l + self.qubits*q*2], q)
                self.qc.rz(self.thetaList[2*l+1 + self.qubits*q*2], q)
            ent = self.qubits-1
            self.qc.barrier()
            while ent > 0:
                self.qc.crx(next(self.crxList), ent, ent-1)
                ent = ent -1
            self.qc.barrier()
    def draw(self):
        print(self.qc)
    
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
    Circuit4(7,3, theta, crxList).draw()
    pass

if __name__ == '__main__':
    main()
