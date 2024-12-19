import numpy as np

# Quantum State Initialization
def initialize_qubit_state():
    """Initialize a simple qubit in |0> state."""
    return np.array([1, 0], dtype=complex)

# Quantum State Evolution
def evolve_qubit_state(qubit, operator):
    """
    Evolve a qubit state using a specified operator (gate).

    Parameters:
        qubit (numpy.array): The initial quantum state.
        operator (numpy.array): The quantum gate or operator.

    Returns:
        numpy.array: The evolved quantum state.
    """
    if operator.shape != (len(qubit), len(qubit)):
        raise ValueError("Operator dimensions must match qubit state dimensions.")
    return operator @ qubit

# Multi-Dimensional State Mapping
def map_state_to_dimension(qubit_state, dimensions=3):
    """
    Map a qubit state to higher dimensions for visualization or computation.

    Parameters:
        qubit_state (numpy.array): Quantum state vector.
        dimensions (int): Number of dimensions (2D, 3D, 4D).

    Returns:
        numpy.array: State mapped to specified dimensions.
    """
    if dimensions < len(qubit_state):
        raise ValueError("Cannot map to dimensions smaller than the qubit state.")
    return np.pad(qubit_state, (0, dimensions - len(qubit_state)), 'constant')

# Main Execution
if __name__ == "__main__":
    # Initialize qubit in |0> state
    qubit = initialize_qubit_state()
    print(f"Initial Qubit State: {qubit}")

    # Apply Quantum Gate (X Gate)
    GATES = {
        "X": np.array([[0, 1], [1, 0]]),
        "H": np.array([[1, 1], [1, -1]]) / np.sqrt(2),
    }
    X_GATE = GATES["X"]
    evolved_qubit = evolve_qubit_state(qubit, X_GATE)
    print(f"Evolved Qubit State: {evolved_qubit}")

    # Map State to Higher Dimensions
    mapped_state = map_state_to_dimension(evolved_qubit, dimensions=4)
    print(f"Mapped State to 4D: {mapped_state}")
