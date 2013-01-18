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
