# Quantum-Parameterize-Super-Circuits

###### Quantum Parameterize Super Circuit is a circuit used to tune the parameters of gates. So that, we could get desired values. If you have created the parameterize circuit previously you have come across many difficulties such as, Aligning the gates serially with multi qubit gates(cx, crx, cry, crz, swap and etc.) and Theta List (list of radian that you want to pass in circuit), If you've design circuit for specific number of Qubits. for example: let suppose, you have design a circuit for 8 Qubits that contains some tunable gates(rx, ry, rz and etc.) and follow some random pattern. Its difficult to expand the number Qubits from initial design but its easy with super circuit. All you need to pass the qubit number and It will create a circuit for you.

###### You could use Super Circuit in serveral Quantum Algorithm including QML, VQE, QAOA and etc. I'll add encoder and label extracter for QML later

###### for example

            Circuit7(qubit, layer, thetaList).draw()
            where,
                Qubit = number of qubit
                Layer = number of repetition of circuit along x-axis
                thetaList = List of theta for tunable gates

###### if project requirement is for 128 qubits you just need to pass like,

                for "draw" in terminal,
                    > circuit7(128, 1, thetaList).draw()

                for getting "statevector",
                    > circuit7(128, 1, thetaList).statevector()
                
                for getting "counts", 
                    > circuit7(128, 1, thetaList).counts()

###### feel free to add more function as per your need
