# nonlinear-activations

30 July 2025

Notes on Section 6.1.4 of Supervised Machine Learning with Quantum Computers of M. Schuld, F. Petruccione.

#

In some research about practical implementations of VQCs for classification, there is mention of how the quantum VQC approach suffers from a lack of expressibility due to the linearity of a quantum circuit. Because of this, some of the research is about combining quantum-enhanced layers with non-linear classical layers, in an attempt to "get the best of both worlds" in terms of expressibility. This disadvantage takes form when the data is complex and not linearly separable (convex hulls bounding each class of data are disjoint).

## How to introduce nonlinearity

We look at nonlinearity from the angle of a subset of activation functions like ReLU. A non-linear function $\varphi$ maps an input $v$ to $\varphi(v)$.

### Amplitude Encoding

Applying an activation function to a layer means implementing the map $\ket{\psi_v} \rarr \ket{\psi_{\varphi(v)}}$ for some $v$ and activation function $\varphi$. This operation cannot be performed via a standard unitary transformation. However, we have the non-unitary tool of measurement to our disposal. Ultimately the trick here is to store $v$ in basis encoding and use the "conditional rotation" trick to prepare

$$
\ket{\psi}\ket{0}\ket{v} \rarr \ket{\psi}(\varphi(v)\ket{0}+\sqrt{1-\varphi(v)^2}\ket{1})\ket{v}
$$

and use "branch selection" to get a state proportional to $\varphi(v)\ket{\psi}\ket{v}$. Since we would rely on basis encoding anyway, amplitude encoding doesn't seem to be the right avenue for this.

### Basis Encoding

In basis encoding we benefit from the fact that any classical algorithm can be performed deterministically on a quantum computer, including $\varphi$. 

Let a scalar $v$ be reprsented by

$$
v=b_sb_{\tau_l-1} \dots b_1b_0\ .\ b_{-1}b_{-2} \dots b_{-\tau_r}
$$

where $\tau_l$ and $\tau_r$ are the numbers of bits left and right of the dot (integer and fractional bits). Thus $v$ is represented using $(1+\tau_l+\tau_r)$ bits. The bit $b_s$ is the sign bit, where if $b_s$ is set $v$ is negative.


#### Step function

Define the step function

$$
\varphi(v) = \begin{cases}0 & \text{if}\ v ≥ 0 \\ 1 & \text{else}\end{cases}
$$

Note the textbook states the first case as $v ≤ 0$, which must be a typo based on what is next written.

The sign qubit of $v$ is used as the map, where $\ket{v} \rarr \ket{b_s}$.

#### ReLU function
Define ReLU:

$$
\varphi(v) = \begin{cases}0 & \text{if}\ v≥0 \\ v & \text{else}\end{cases}
$$

Here we again condition on the sign qubit but instead copy all of $\ket{v}$ based on $\ket{b_s}$ and $\ket{b_k}$ for $k=\tau_l-1, \dots,0,\dots,-\tau_r$.

#### Sigmoid

The sigmoid function

$$
\varphi(v;\delta)=\frac{1}{1+e^{-\delta v}}
$$

is tricky because of the exponentiation and the division. Instead we look at approximation methods, which includes reducing the precision, and computing a look up table containing the input bitstrings and the output bitstrings. As precision increases the size grows exponentially, however. Using methods like Quine-McClusky, one can reduce the size of the look up table by solving essentially a "summarization" problem of finding the minimum sufficient condition for a set of outputs.


## References

1. Supervised Machine Learning with Quantum Computers - M. Schuld, F. Petruccione.
2. [Linear separability](https://en.wikipedia.org/wiki/Linear_separability)





