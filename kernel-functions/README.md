# kernel-functions

We learn about kernel functions and their parallel to quantum computing here.

They are applied in Kernel methods. SVM is a popular example of a kernel method.

Kernel methods are instance based learners, learning a weight $w_i$ for a corresponding training sample $(\bold{x}_i, y_i)$. For unseen data, we apply a "similarity function" $k$, which is a kernel.

A "kernel" is a weighting function for a weighted sum/integral. The function $K : X \times X \rarr \mathbb{R}$ is a kernel if there exists a function $\Phi$ such that for any two data points $x,z$, we have $K(x,z)=\Phi(x) \cdot \Phi(z)$ ($X$ denotes the feature space). Here $\Phi$ is an implicit mapping of data points to a higher dimensional space.

### Example

A kernel over $X=\mathbb{R}^n$ for example is $K(x,z)=(x\cdot z)^2$.

Then for $X=\mathbb{R}^2$, $K(x, z) = \Phi(x) \cdot \Phi(z)$ for $\Phi(x)=(x_1^2, x_2^2, \sqrt{2}x_1x_2)$. Why? Well $(x \cdot z)^2=(x_1z_1 + x_2z_2)^2 = x_1^2z_1^2 + 2x_1z_1x_2z_2 + x_2^2z_2^2$. On the other hand, $\Phi(x) \cdot \Phi(z) = x_1z_1 + x_2z_2 + 2x_1z_1x_2z_2$. Thus the existence and form of this mapping $\Phi(x)$ satisfies $K$ to be a kernel for the space $X=\mathbb{R}^2$.

The kernel is useful because it can in many cases replace the traditional dot product $x\cdot z$ with $K(x, z)$, and the algorithms then behave as if the data was in a higher dimensional space given by $\Phi(x)$. Additionally, computing $K$ can be more efficient than computing the dot product.

A *kernalizable* algorithm is one that interacts with its data only via the traditional dot product.

### More Examples

1. The linear kernel $K(x, z)= x\cdot z$.
2. The polynomial kernel $K(x, z)=(x \cdot z)^d$, or $K(x, z)=(1+x\cdot z)^d$
3. Gaussian kernel $K(x, z)=e^{-||x-z||^2/(2\sigma^2)}$.
4. Laplace kernel $K(x,z)=e^{-||x-z||/(2\sigma^2)}$

## Optimal Margin Classification

Within a set of data, find the hyperplane that maximizes the minimum distance between any training sample and the hyperplane.

The distance between the training sample and the hyperplane is given by 

$$
\gamma^(i) = \frac{y^{(i)}(w^Tx^{(i)}+b)}{||w||}
$$

and the classifier maximizes $\gamma = \min_i \gamma^(i)$.

## Kernel Trick

1. Write the whole algorithm in terms of $\langle x, z\rangle$.
2. Let there be some mapping from $x \rarr \Phi(x)$. 

For example let $x$ contain one feature. Then you could map $x$ to $\Phi(x)=(x, x^2, x^3, x^4)$, turning a 1-D input to a higher dimensional sample.

3. Find a way to compute $K(x, z) = \Phi(x) \cdot \Phi(z)$ efficiently

### Example

Let $x = (x_1, x_2, x_3)$, and $\Phi(x)=(x_1x_1,x_1x_2,x_1x_3,x_2x_1,x_2x_2,x_2x_3,x_3x_1,x_3x_2,x_3x_3)$. $x\in\mathbb{R}^n$ and $x\in\mathbb{R}^{n^2}$. Similarly $\Phi(z)=(z_1z_1,z_1z_2,z_1z_3,z_2z_1,z_2z_2,z_2z_3,z_3z_1,z_3z_2,z_3z_3)$. With $n^2$ elements, we need $O(n^2)$ time to compute $\Phi(x)$ or $\Phi(x) \cdot \Phi(z)$ explicitly. We want to find a better way to compute $K$. 

Claim: $K$ can be computed as $(x^Tz)^2$. This would be $O(n)$ time since $x, z\in\mathbb{R}^n$ and not $\mathbb{R}^{n^2}$. 

$$
\begin{align}
(x^Tz)^2 &= (\sum_{i=1}^n x_iz_i)(\sum_{j=1}^nx_jz_j) \\
&= \sum_{i=1}^n\sum_{j=1}^n x_iz_i\ x_jz_j \\
&= \sum_{i=1}^n\sum_{j=1}^n(x_ix_j)(z_iz_j)
\end{align}
$$

This last quantity is equal to $\Phi(x) \cdot \Phi(z)$.
## References

1. [Kernel method](https://en.wikipedia.org/wiki/Kernel_method)
2. [Kernels Methods in Machine Learning](https://web2.qatar.cmu.edu/~gdicaro/10315-Fall19/additional/balcan-notes-on-kernel-methods.pdf) - M. Balcan, CMU
3. [Lecture 7 - Kernels | Stanford CS229](https://www.youtube.com/watch?v=8NYoQiRANpg) - Andrew Ng (Autumn 2018)