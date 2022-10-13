from qiskit import *
import qiskit

theta = [i for i in range(50)]

class Circuit2:
    def __init__(self, qubits, layers, thetaList) -> None:
        self.qubits = qubits
        self.layers = layers
        self.thetaList = thetaList
        self.qc = QuantumCircuit(self.qubits)
        for l in range(self.layers):
            for q in range(self.qubits):
                self.qc.rx(self.thetaList[2*l + self.qubits*q*2], q)
                self.qc.rz(self.thetaList[2*l+1 + self.qubits*q*2], q)
            ent = self.qubits-1
            while ent > 0:
                self.qc.cx(ent, ent-1)
                ent = ent -1

    def draw(self):
        # print(self.qc)
        self.qc.draw('mpl')
    
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


# Circuit2(6, 6, theta).draw()