# Super Circuit

##### Super Circuit is a type of parameterize circuit which is independent of qubits, layers or both. It is used to tune the parameters of circuit to get the desire value. It is build on python using Qiskit. So, to install qiskit use,

> pip install qiskit

##### Although, I recommand you to install it in virtual environment. It will help you to develop your project independently.


##### Super Circuit can be used in serveral Quantum Algorithm including QML, VQE, QAOA and etc. I'll add encoder and label extracter for QML later

##### for example you could call the class by following code:
            
            > Circuit7(qubit, layer, thetaList).draw()
            
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
+ Circuit1(6, 6, thetaList).draw() ![Circuit1](https://github.com/Priyanshusinhaa/SuperCircuit/blob/master/Images/circuit1.png)
+ Single layer for Circuit1: 

![Layer1](https://github.com/Priyanshusinhaa/SuperCircuit/blob/master/Images/circuit1SingleLayer.png)

##### 2. Super Circuit 2
+ Circuit3(6, 4, thetaList).draw() ![Circuit2](https://github.com/Priyanshusinhaa/SuperCircuit/blob/master/Images/circuit2.png)
+ Single layer for Circuit2: 

![Layer1](https://github.com/Priyanshusinhaa/SuperCircuit/blob/master/Images/circuit2SingleLayer.png)

##### 3. Super Circuit 3
+ Circuit3(6, 5, thetaList).draw() ![Circuit3](https://github.com/Priyanshusinhaa/SuperCircuit/blob/master/Images/circuit3.png)
+ Single layer for Circuit3: 

![Layer1](https://github.com/Priyanshusinhaa/SuperCircuit/blob/master/Images/circuit3SingleLayer.png)

##### 4. Super Circuit 4
+ Circuit4(6, 5, thetaList).draw() ![Circuit1](https://github.com/Priyanshusinhaa/SuperCircuit/blob/master/Images/circuit4.png)
+ Single layer for Circuit4: 

![Layer1](https://github.com/Priyanshusinhaa/SuperCircuit/blob/master/Images/circuit4SingleLayer.png)


##### 5. Super Circuit 5
+ Circuit5(6, 5, thetaList).draw() ![Circuit5](https://github.com/Priyanshusinhaa/SuperCircuit/blob/master/Images/circuit5.png)
+ There are three layer in the below image. First layer is (RY, RZ), second and third layer are (CX, RY, RZ)

![Layer1](https://github.com/Priyanshusinhaa/SuperCircuit/blob/master/Images/circuit5SingleLayer.png)


##### 6. Super Circuit 6
+ Circuit6(6, 5, thetaList).draw() ![Circuit6](https://github.com/Priyanshusinhaa/SuperCircuit/blob/master/Images/circuit6.png)
+ There are three layer in the below image. First layer is (RY, RZ), second and third layer are (SWAP, RY, RZ)

![Layer1](https://github.com/Priyanshusinhaa/SuperCircuit/blob/master/Images/circuit6SingleLayer.png)


##### 7. Super Circuit 7
+ Circuit7(6, 5, thetaList).draw() ![Circuit7](https://github.com/Priyanshusinhaa/SuperCircuit/blob/master/Images/circuit7.png)
+ There are three layer in the below image. First layer is (RY, RZ), second and third layer are (SWAP, RY, RZ)

![Layer1](https://github.com/Priyanshusinhaa/SuperCircuit/blob/master/Images/circuit7SingleLayer.png)


##### 8. Super Circuit 8
+ Circuit8(6, 5, thetaList).draw() ![Circuit8](https://github.com/Priyanshusinhaa/SuperCircuit/blob/master/Images/circuit8.png)
+ There are three layer in the below image. First layer is (RY, RZ), second and third layer are (CX, RY, RZ)

![Layer1](https://github.com/Priyanshusinhaa/SuperCircuit/blob/master/Images/circuit8SingleLayer.png)


##### 9. Super Circuit 9
+ Circuit9(6, 5, thetaList, crzList).draw() ![Circuit8](https://github.com/Priyanshusinhaa/SuperCircuit/blob/master/Images/circuit9.png)
+ There are three layer in the below image. First layer is (RY, RZ), second and third layer are (CRX, RY, RZ)
+ It takes one additional parameter that's a list of CRX. It is denoted as crxList in the code.

![Layer1](https://github.com/Priyanshusinhaa/SuperCircuit/blob/master/Images/circuit9SingleLayer.png)


##### 10. Super Circuit 10
+ Circuit10(6, 5, thetaList, crzList).draw() ![Circuit8](https://github.com/Priyanshusinhaa/SuperCircuit/blob/master/Images/circuit10.png)
+ There are three layer in the below image. First layer is (RY, RZ), second and third layer are (CRZ, RY, RZ)
+ It takes one additional parameter that's a list of CRZ. It is denoted as crzList in the code.

![Layer1](https://github.com/Priyanshusinhaa/SuperCircuit/blob/master/Images/circuit10SingleLayer.png)



