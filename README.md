# Super-Circuit

##### Super Circuit is a type of parameterize circuit which is independent of qubits, layers or both. It is used to tune the parameters of circuit to get the desire value. It is build on python using Qiskit. So, to install qiskit use,

> pip install qiskit

##### Although, I recommand you to install it in virtual environment. It will help you to develop your project independently.


##### Super Circuit can be used in serveral Quantum Algorithm including QML, VQE, QAOA and etc. I'll add encoder and label extracter for QML later

##### for example

            Circuit7(qubit, layer, thetaList).draw()
            where,
                qubit = number of qubit
                layer = number of repetition of circuit along x-axis
                thetaList = List of theta for tunable gates

##### For creating a circuit for 128 qubits.

                to "draw" in terminal use .draw(),
                    > Circuit7(128, 1, thetaList).draw()
                
                to get "circuit" use .getCircuit(),
                    > Circuit7(128, 1, thetaList).getCircuit()

                to get "statevector" use .statevector(),
                    > Circuit7(128, 1, thetaList).statevector()
                
                to get "counts" use .counts(), 
                    > Circuit7(128, 1, thetaList).counts()

##### feel free to add more function as per your need

##### Here are some Super Circuit from library:

##### 1. Super Circuit 1
+ Circuit1(6, 6, thetaList).draw() ![Circuit1](https://github.com/Priyanshusinhaa/Parameterize-Super-Circuits/blob/master/Images/circuit1.png)
+ Single layer for Circuit1: 

![Layer1](https://github.com/Priyanshusinhaa/Super-Circuit/blob/master/Images/circuit1SingleLayer.png)

##### 2. Super Circuit 2
+ Circuit3(6, 6, thetaList).draw() ![Circuit2](https://github.com/Priyanshusinhaa/Parameterize-Super-Circuits/blob/master/Images/circuit2.png)
+ Single layer for Circuit1: 

![Layer1](https://github.com/Priyanshusinhaa/Super-Circuit/blob/master/Images/circuit2SingleLayer.png)

##### Super Circuit 3
+ Circuit3(6, 5, thetaList).draw() ![Circuit3](https://github.com/Priyanshusinhaa/Parameterize-Super-Circuits/blob/master/Images/circuit3.png)
+ Single layer for Circuit1: 

![Layer1](https://github.com/Priyanshusinhaa/Super-Circuit/blob/master/Images/circuit3SingleLayer.png)

##### Super Circuit 4
+ Circuit4(6, 5, thetaList).draw() ![Circuit1](https://github.com/Priyanshusinhaa/Parameterize-Super-Circuits/blob/master/Images/circuit4.png)
+ Single layer for Circuit4: 

![Layer1](https://github.com/Priyanshusinhaa/Super-Circuit/blob/master/Images/circuit4SingleLayer.png)


