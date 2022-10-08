from qiskit import *
import qiskit

class Circuit1:
    def __init__(self, qubits, layers, thetaList) -> None:
        self.qubits = qubits
        self.layers = layers
        self.thetaList = thetaList

    def draw(self):
        qc = QuantumCircuit(self.qubits)
        for l in range(self.layers):
            for qb in range(self.qubits):
                qc.rx(thetaList[i + self.qubits])
                qc.ry()

