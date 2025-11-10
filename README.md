# RND_Assignment_AI
# Research and Development / AI Assignment

## Problem
Find the values of unknown variables (θ, M, X) in the parametric equations:

\[
x = t\cos(\theta) - e^{M|t|}\sin(0.3t)\sin(\theta) + X
\]
\[
y = 42 + t\sin(\theta) + e^{M|t|}\sin(0.3t)\cos(\theta)
\]

---

## Results

**Estimated Parameters:**

Theta (radians): 0.490759,  Degrees: 28.118
M: 0.021389
X: 54.900778

| Variable | Value | Description |
|-----------|--------|-------------|
| θ | 0.490759 rad (≈ 28.118°) | Rotation angle |
| M | 0.021389 | Exponential growth rate |
| X | 54.900778 | Translation along x-axis |

---

## Final Equation (Submission Format)

\[
\left(t\cos(0.490759) - e^{0.021389|t|}\cdot\sin(0.3t)\sin(0.490759) + 54.900778,\ 42 + t\sin(0.490759) + e^{0.021389|t|}\cdot\sin(0.3t)\cos(0.490759)\right)
\]

---

## L1 Error

**Total L1 Error:**  37865.093872

---

## Visualization

- Red points = Given data  
- Blue curve = Fitted parametric model  

You can also visualize this equation interactively here:  
👉 [Desmos Graphing Calculator](https://www.desmos.com/calculator/rfj91yrxob)

---
