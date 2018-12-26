# Three events, two independent

<br>

### Decomposing joint probabilities

Consider the two equalities

\begin{align}
P(A, B, C) & = P(A, B | C) P(C),    \\
P(A, B, C) & = P(A | B, C) P(B, C).
\end{align}

Conditional independence holds (by definition) if

$$ P(A, B | C) =  P(B | C) P(A | C).$$

This can be used to further simplify the joint probability, using equation (1), given $B$ and $A$ are in fact conditionally independent on $C$,

$$ P(A, B, C) = P(B | C) P(A | C) P(C).$$

Independence holds (by definition) if

$$ P(B, C) = P(B) P(C).$$

Assume $B$ and $C$ are independent, can we further simplify the joint probability $P(A, B, C)$ in equation (2)? The result is

$$ P(A, B, C) =  P(A | B, C) P(B) P(C).$$

Only the second term can be decomposed, not the first. Let us give a counterexample.

#### Example 1

Let

* $B \in \\{0, 1\\}$: result of coin toss
* $C \in \\{0, 1\\}$: result of another coin toss
* $A \in \\{0, 1, 2\\}$: sum of $B$, $C$

Obviously

$$P(B, C) = P(B) P(C)$$

But, even though $B$ and $C$ are independent, $A$ depends on the combination of them. Can the probability $P(A| B, C)$ be further simplified, when allowing an arbitrary function $f$

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
This is contradiction if the simpler terms are the same in both equations. This is evidently the case if taking terms like $P(B)$, $P(C)$ etc. The equation can only agree if one adds pieces of the configuration $(A, B, C)$ as arguments to the function. But then, the complexity of the function increases so much that one would no longer refer to it as *decomposition* or *simplification*.

#### Example 2

One can also construct cases in which a simplification is possible. Take the same example as above but let

*  $A \in \\{0, 1\\}$: sum of $B$ and another coin toss

Evidently, then $P(A| B, C) = P(A| B)$.

#### Approximation

Instead of demanding an exact equality, you can see equation (3) as an *ansatz* in which you're free to choose any function. In this case, you should do some thorough checks on the errors that you generate. For convenience, start with a simple ansatz. Something that's linear either directly or in log space.

#### Example 3

Contrast all of the above with an example, in which you can make use of conditional independence and "everything factorizes".

* $C \in \\{0, 1\\}$: result of coin toss
* $B \in \\{0, 1\\}$: if $C=0$, then $B=0$, if $C=1$, then $B$ is the result of a coin toss
* $A \in \\{0, 1\\}$: if $C=0$, then $A=0$, if $C=1$, then $A$ is the result of a coin toss

Then
$$P(A, B) \neq P(A) P(B),$$
but
$$P(A, B| C) = P(A|C) P(B|C).$$