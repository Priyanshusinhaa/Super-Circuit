# Super-Circuit

###### Super Circuit is a type of parameterize circuit which is independent of qubits, layers or both. It is used to tune the parameters of circuit to get the desire value.
If you have created the parameterize circuit previously you have come across many difficulties such as, Aligning the gates serially with multi qubit gates(cx, crx, cry, crz, swap and etc.) and List of radians (list of radian that you want to pass in circuit), If you've design circuit for specific number of Qubits. for example: let suppose, you have design a circuit for 8 Qubits that contains some tunable gates(rx, ry, rz and etc.) and follow some random pattern. Its difficult to expand the number Qubits from initial design but its easy with super circuit. All you need to pass the qubit number and It will create a circuit for you.

###### Super Circuit can be used in serveral Quantum Algorithm including QML, VQE, QAOA and etc. I'll add encoder and label extracter for QML later

###### for example

            Circuit7(qubit, layer, thetaList).draw()
            where,
                qubit = number of qubit
                layer = number of repetition of circuit along x-axis
                thetaList = List of theta for tunable gates

###### For creating a circuit for 128 qubits.

                to "draw" in terminal use .draw(),
                    > Circuit7(128, 1, thetaList).draw()
                
                to get "circuit" use .getCircuit(),
                    > Circuit7(128, 1, thetaList).getCircuit()

                to get "statevector" use .statevector(),
                    > Circuit7(128, 1, thetaList).statevector()
                
                to get "counts" use .counts(), 
                    > Circuit7(128, 1, thetaList).counts()

###### feel free to add more function as per your need

###### Here are some Super Circuit from library:

###### Super Circuit 1
![Circuit1](https://github.com/Priyanshusinhaa/Parameterize-Super-Circuits/blob/master/Images/circuit1.png)

Single Layer for Super Circuit 1
![Layer1](https://github.com/Priyanshusinhaa/Super-Circuit/blob/master/Images/circuit1SingleLayer.png)

###### Super Circuit 2
![Circuit2](https://github.com/Priyanshusinhaa/Parameterize-Super-Circuits/blob/master/Images/circuit2.png)

Single Layer for Super Circuit 2
![Layer2](https://github.com/Priyanshusinhaa/Super-Circuit/blob/master/Images/circuit2SingleLayer.png)

###### Super Circuit 3
![Circuit3](https://github.com/Priyanshusinhaa/Parameterize-Super-Circuits/blob/master/Images/circuit3.png)

Single Layer for Super Circuit 3
![Layer3](https://github.com/Priyanshusinhaa/Super-Circuit/blob/master/Images/circuit3SingleLayer.png)


###### Super Circuit 4
![Circuit4](https://github.com/Priyanshusinhaa/Parameterize-Super-Circuits/blob/master/Images/circuit4.png)

Single Layer for Super Circuit 4
![Layer4](https://github.com/Priyanshusinhaa/Super-Circuit/blob/master/Images/circuit4SingleLayer.png)



