from qiskit import *
import qiskit

theta = [i for i in range(50)]
class Circuit1:
    def __init__(self, qubits, layers, thetaList, measure = False) -> None:
        self.qubits = qubits
        self.layers = layers
        self.thetaList = thetaList
        self.qc = QuantumCircuit(self.qubits)
        for l in range(self.layers):
            for q in range(0, self.qubits):
                self.qc.rx(self.thetaList[2*l + q*self.layers*2], q)
                self.qc.rz(self.thetaList[2*l+1 + q*self.layers*2], q)
        if measure == True:
            self.qc.measure_all()
    def draw(self):
        print(self.qc)
        
    def statevector(self, type = None):
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


Circuit1(4, 4, theta).draw()

                
