![supercircuit](https://github.com/Priyanshusinhaa/Super-Circuit/blob/master/Images/supercircuit.svg)


_______________________________________________________________________________________________________________________________________________________________________

### Introduction
_______________________________________________________________________________________________________________________________________________________________________

The Super Circuit is a versatile parameterized circuit that can be applied to any size of data without being restricted to a fixed number of qubits, layers, or both. By passing a 'number of qubit', 'number of layer', and 'list of theta' as parameters, you can construct a circuit for any number of qubits. Each circuit is built independently, making it a convenient core component for Quantum Algorithms such as Quantum Machine Learning, VQE, QAOA, etc. Built on Python using Qiskit, you can simply take a class of circuit and use it in your project or software. To use the Super Circuit, follow the steps outlined below.

_______________________________________________________________________________________________________________________________________________________________________

### Uses
_______________________________________________________________________________________________________________________________________________________________________

1. Install Qiskit by running the command "pip install qiskit" in your terminal or command prompt.

2. Choose a circuit from the Qiskit library. For example, you may select Circuit 3.

3. Go to the repository for Circuit 3 and download circuit3.py.

4. Use the class methods to call the circuit as needed for your project or software.

Note: It is recommended to install Qiskit in a virtual environment to develop your project independently. To use Qiskit in your project or software, refer to the provided examples and documentation to understand how to call and use the various functions and methods.

______________________________________________________________________________________________________________________________________________________

### Examples
_______________________________________________________________________________________________________________________________________________________________________

 for example you could call the class by following code:
            
            > Circuit7(qubit, layer, thetaList).draw()
            
            where,
                qubit = number of qubit
                layer = number of repetition of circuit along x-axis
                thetaList = List of theta for tunable gates

 For creating a circuit for 128 qubits,

                to "draw" in terminal use .draw(),
                    > Circuit7(128, 1, thetaList).draw()
                
                to get "circuit" use .getCircuit(),
                    > Circuit7(128, 1, thetaList).getCircuit()

                to get "statevector" use .statevector(),
                    > Circuit7(128, 1, thetaList).statevector()
                
                to get "counts" use .counts(), 
                    > Circuit7(128, 1, thetaList).counts()

 feel free to add more function as per your need
 
_______________________________________________________________________________________________________________________________________________________________________

### Images of Super Circuit

_______________________________________________________________________________________________________________________________________________________________________

#### 1. Super Circuit 1

+ Circuit1(6, 6, thetaList).draw() ![Circuit1](https://github.com/Priyanshusinhaa/Super-Circuit/blob/master/Images/circuit1.png)
+ Single layer for Circuit1: 

![Layer1](https://github.com/Priyanshusinhaa/Super-Circuit/blob/master/Images/circuit1SingleLayer.png)

_______________________________________________________________________________________________________________________________________________________________________

#### 2. Super Circuit 2
+ Circuit3(6, 4, thetaList).draw() ![Circuit2](https://github.com/Priyanshusinhaa/Super-Circuit/blob/master/Images/circuit2.png)
+ Single layer for Circuit2: 

![Layer1](https://github.com/Priyanshusinhaa/Super-Circuit/blob/master/Images/circuit2SingleLayer.png)

_______________________________________________________________________________________________________________________________________________________________________

#### 3. Super Circuit 3
+ Circuit3(6, 5, thetaList).draw() ![Circuit3](https://github.com/Priyanshusinhaa/Super-Circuit/blob/master/Images/circuit3.png)
+ Single layer for Circuit3: 

![Layer1](https://github.com/Priyanshusinhaa/Super-Circuit/blob/master/Images/circuit3SingleLayer.png)

_______________________________________________________________________________________________________________________________________________________________________

#### 4. Super Circuit 4
+ Circuit4(6, 5, thetaList, crxList).draw() ![Circuit1](https://github.com/Priyanshusinhaa/Super-Circuit/blob/master/Images/circuit4.png)
+ Single layer for Circuit4: 

![Layer1](https://github.com/Priyanshusinhaa/Super-Circuit/blob/master/Images/circuit4SingleLayer.png)

_______________________________________________________________________________________________________________________________________________________________________

#### 5. Super Circuit 5
+ Circuit5(6, 5, thetaList).draw() ![Circuit5](https://github.com/Priyanshusinhaa/Super-Circuit/blob/master/Images/circuit5.png)
+ There are three layer in the below image. First layer is (RY, RZ), second and third layer are (CX, RY, RZ)

![Layer1](https://github.com/Priyanshusinhaa/Super-Circuit/blob/master/Images/circuit5SingleLayer.png)

_______________________________________________________________________________________________________________________________________________________________________


#### 6. Super Circuit 6
+ Circuit6(6, 5, thetaList).draw() ![Circuit6](https://github.com/Priyanshusinhaa/Super-Circuit/blob/master/Images/circuit6.png)
+ There are three layer in the below image. First layer is (RY, RZ), second and third layer are (SWAP, RY, RZ)

![Layer1](https://github.com/Priyanshusinhaa/Super-Circuit/blob/master/Images/circuit6SingleLayer.png)

_______________________________________________________________________________________________________________________________________________________________________

#### 7. Super Circuit 7
+ Circuit7(6, 5, thetaList).draw() ![Circuit7](https://github.com/Priyanshusinhaa/Super-Circuit/blob/master/Images/circuit7.png)
+ There are three layer in the below image. First layer is (RY, RZ), second and third layer are (SWAP, RY, RZ)

![Layer1](https://github.com/Priyanshusinhaa/Super-Circuit/blob/master/Images/circuit7SingleLayer.png)

_______________________________________________________________________________________________________________________________________________________________________

#### 8. Super Circuit 8
+ Circuit8(6, 5, thetaList).draw() ![Circuit8](https://github.com/Priyanshusinhaa/Super-Circuit/blob/master/Images/circuit8.png)
+ There are three layer in the below image. First layer is (RY, RZ), second and third layer are (CX, RY, RZ)

![Layer1](https://github.com/Priyanshusinhaa/Super-Circuit/blob/master/Images/circuit8SingleLayer.png)

_______________________________________________________________________________________________________________________________________________________________________

#### 9. Super Circuit 9
+ Circuit9(6, 5, thetaList, crzList).draw() ![Circuit8](https://github.com/Priyanshusinhaa/Super-Circuit/blob/master/Images/circuit9.png)
+ There are three layer in the below image. First layer is (RY, RZ), second and third layer are (CRX, RY, RZ)
+ It takes one additional parameter that's a list of CRX. It is denoted as crxList in the code.

![Layer1](https://github.com/Priyanshusinhaa/Super-Circuit/blob/master/Images/circuit9SingleLayer.png)

_______________________________________________________________________________________________________________________________________________________________________

#### 10. Super Circuit 10
+ Circuit10(6, 5, thetaList, crzList).draw() ![Circuit8](https://github.com/Priyanshusinhaa/Super-Circuit/blob/master/Images/circuit10.png)
+ There are three layer in the below image. First layer is (RY, RZ), second and third layer are (CRZ, RY, RZ)
+ It takes one additional parameter that's a list of CRZ. It is denoted as crzList in the code.

![Layer1](https://github.com/Priyanshusinhaa/Super-Circuit/blob/master/Images/circuit10SingleLayer.png)

_______________________________________________________________________________________________________________________________________________________________________


