# single-qubit-pc-training

29 July 2025.

This subproject demonstrates the use of gradient descent to train a single-qubit variational (parametrized) circuit into a circuit capable of turning any state $\ket{\psi}$ into $\ket{1}$.

We define the cost function $C(\theta)$ as the expectation value of the Pauli Z operator applied to the state $\ket{\psi}$ after a rotation of $R_Y(\theta)$. That is,

$$C(\theta) = \langle{(R_Y(\theta)\ket{\psi})}|Z|{(R_Y(\theta)\ket{\psi})}\rangle$$

Then we take its derivative $C'(\theta)$:

$$
C'(\theta) = -2|\alpha|^2\sin \theta/2 \cos\theta/2 -\alpha^\ast\beta(\cos^2\theta/2-\sin^2\theta/2)+2|\beta|^2\sin\theta/2\cos\theta/2
$$

in terms of the state $\ket{\psi}=\alpha\ket{0}+\beta\ket{1}$, $\alpha,\beta\in\mathbb{C}$. We define an update rule $\theta_{\text{new}}=\theta_{\text{old}}-\eta 
C'(\theta_\text{old})$, and iterate many times.

See `main.ipynb` for the mathematical and computational details.

## References

1. [Fidelity of quantum states](https://en.wikipedia.org/wiki/Fidelity_of_quantum_states)
2. [Expectation value (quantum mechanics)](https://en.wikipedia.org/wiki/Expectation_value_(quantum_mechanics))
