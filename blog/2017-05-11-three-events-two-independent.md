Title: How much can we simplify the joint probability $P(A, B, C)$ if two events are independent?

*Published: 2017-05-11.*

To answer this question, consider two different ways of decomposing joint probabilities:

\begin{align}
P(A, B, C) & = P(A, B | C) P(C),    \\
P(A, B, C) & = P(A | B, C) P(B, C).
\end{align}

Both equations allow to simplify further given two types of independence assumptions:

1. Conditional independence holds if $P(A, B | C) =  P(B | C) P(A | C)$. If $B$ and $A$ are conditionally independent given $C$, one can simplify eq. (1):
$$ P(A, B, C) = P(B | C) P(A | C) P(C).$$
2. Independence holds if $P(B, C) = P(B) P(C)$. If $B$ and $C$ are independent, one can simplify eq. (2):
$$ P(A, B, C) =  P(A | B, C) P(B) P(C).$$

The simplified eq. (1) now only involves terms with two events at most. 
Can we also achieve this for eq. (2) by further decomposing the first term $P(A | B, C)$? The answer is no. Let us look at an example.

### Example 1

Let

* $B \in \\{0, 1\\}$: result of coin toss
* $C \in \\{0, 1\\}$: result of another coin toss
* $A \in \\{0, 1, 2\\}$: sum of $B$, $C$

Here, it holds that $P(B, C) = P(B) P(C)$. But, even though $B$ and $C$ are independent, $A$ depends on the combination of them. Can the probability $P(A| B, C)$ be further simplified, when allowing an arbitrary function $f$

\begin{equation}P(A| B, C) \stackrel{?}{=} f\big(P(A|B), P(A|C), \text{simpler terms}\big).\end{equation}

Here, *simpler terms* means $P(B)$, $P(C)$ etc.

Let's show that this is not possible.

\begin{align*}
P(B) &= \frac{1}{2} \quad \text{for } B \in \{0, 1\}, \\
P(C) &= \frac{1}{2} \quad \text{for } C \in \{0, 1\}, \\
P(A|B, C) &= \left\{ \begin{array}{l} 1 \quad \text{for } A = B + C\\ 0 \quad \text{else}, \end{array} \right. \\
P(A) &= \left\{ \begin{array}{l} \frac{1}{4} \quad \text{for } A = 0\\ \frac{1}{2} \quad \text{for } A = 1 \\ \frac{1}{4} \quad \text{for } A = 2, \end{array} \right. \\
P(A|B) &= \left\{ \begin{array}{l} \frac{1}{2} \quad \text{for } A = B\\ \frac{1}{2} \quad \text{for } A = B + 1, \end{array} \right. \\
P(A|C) &= \left\{ \begin{array}{l} \frac{1}{2} \quad \text{for } A = C\\ \frac{1}{2} \quad \text{for } A = C + 1, \end{array} \right. \\
\end{align*}

Assume $B=0, C=0$ and consider the cases $A=0$ / $A=1$. Evaluate equation (3) above, which gives

\begin{align*}
1 & \stackrel{?}{=} f\big(\frac{1}{2}, \frac{1}{2}, \text{simpler terms}\big) \quad \text{for } A = 0,\\
0 & \stackrel{?}{=} f\big(\frac{1}{2}, \frac{1}{2}, \text{simpler terms}\big) \quad \text{for } A = 1.
\end{align*}
This is impossible if the simpler terms are the same in both equations, which would be the case if taking terms like $P(B)$, $P(C)$. The equation can only agree if one adds pieces of the configuration $(A, B, C)$ as arguments to the function. But then, the complexity of the function increases so much that one would no longer refer to it as *decomposition* or *simplification*.

Instead of demanding an exact equality, you can see equation (3) as an ansatz in which you're free to choose any function. In this case, you should do some thorough checks on the errors that you generate. To make this transparent, start with a simple ansatz, something that's linear either directly or in log space.


### Example 2

Let us now also give an example for eq. (1) assuming conditional independence:

* $C \in \\{0, 1\\}$: result of coin toss
* $B \in \\{0, 1\\}$: if $C=0$, then $B=0$, if $C=1$, then $B$ is the result of a coin toss
* $A \in \\{0, 1\\}$: if $C=0$, then $A=0$, if $C=1$, then $A$ is the result of a coin toss

Then
$$P(A, B) \neq P(A) P(B),$$
but
$$P(A, B| C) = P(A|C) P(B|C)$$
and simplifying eq. (1) holds as given above.