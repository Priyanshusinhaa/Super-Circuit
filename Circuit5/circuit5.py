from qiskit import *
import qiskit


class Circuit5:
    def __init__(self, qubits, layers, thetaList, crxList) -> None:
        self.qubits = qubits
        self.layers = layers
        self.crxList = crxList
        self.qc = QuantumCircuit(qubits)
        for l in range(self.layers):
            for q in range(self.qubits):
                
