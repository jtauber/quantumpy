from random import random


class Psi:
    def __init__(self, n_qubits):
        """
        set up a quantum system with the given number of qubits
        initialized to the "zero" qubit.
        """
        self.n_qubits = n_qubits
        # in this classical simulation, we use 2^n_qubits complex numbers
        self.amplitudes = [0] * (1 << n_qubits)
        self.amplitudes[0] = 1
    
    def collapse(self):
        """
        collapse the system (i.e. measure it) and return a tuple
        of the bits.
        """
        weights = [abs(amp) ** 2 for amp in self.amplitudes]
        choice = random() * sum(weights)
        for i, w in enumerate(weights):
            choice -= w
            if choice < 0:
                self.amplitudes = [0] * (1 << self.n_qubits)
                self.amplitudes[i] = 1
                return tuple((i >> bit) % 2 for bit in range(self.n_qubits))
