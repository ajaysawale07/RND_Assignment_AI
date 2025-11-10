import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.optimize import minimize

# -------------------------------------------------------
# Step 1: Load the data
# -------------------------------------------------------
data = pd.read_csv("xy_data.csv")
x_data = data["x"].values
y_data = data["y"].values

# If 't' column is not given in the CSV, we assume it's equally spaced
t = np.linspace(6, 60, len(x_data))

# -------------------------------------------------------
# Step 2: Define the parametric equation
# -------------------------------------------------------
def curve(t, theta, M, X):
    x = t * np.cos(theta) - np.exp(M * np.abs(t)) * np.sin(0.3 * t) * np.sin(theta) + X
    y = 42 + t * np.sin(theta) + np.exp(M * np.abs(t)) * np.sin(0.3 * t) * np.cos(theta)
    return x, y

# -------------------------------------------------------
# Step 3: Define cost function (L1 distance)
# -------------------------------------------------------
def cost(params, t, x_data, y_data):
    theta, M, X = params
    x_pred, y_pred = curve(t, theta, M, X)
    error = np.abs(x_pred - x_data) + np.abs(y_pred - y_data)
    return np.sum(error)

# -------------------------------------------------------
# Step 4: Optimize parameters
# -------------------------------------------------------
# Initial guess (theta in radians)
initial_guess = [np.deg2rad(25), 0.0, 50]

# Bounds for (theta, M, X)
bounds = [
    (np.deg2rad(0), np.deg2rad(50)),  # theta
    (-0.05, 0.05),  # M
    (0, 100)        # X
]

result = minimize(cost, initial_guess, args=(t, x_data, y_data), bounds=bounds, method='L-BFGS-B')

theta_opt, M_opt, X_opt = result.x

# -------------------------------------------------------
# Step 5: Print results
# -------------------------------------------------------
print("✅ Estimated Parameters:")
print(f"Theta (radians): {theta_opt:.6f},  Degrees: {np.rad2deg(theta_opt):.3f}")
print(f"M: {M_opt:.6f}")
print(f"X: {X_opt:.6f}")
print("\nFinal Equation:")
print(f'(t*cos({theta_opt:.6f}) - exp({M_opt:.6f}*|t|)*sin(0.3*t)*sin({theta_opt:.6f}) + {X_opt:.6f}, '
      f'42 + t*sin({theta_opt:.6f}) + exp({M_opt:.6f}*|t|)*sin(0.3*t)*cos({theta_opt:.6f}))')

# -------------------------------------------------------
# Step 6: Visualize the curve
# -------------------------------------------------------
x_fit, y_fit = curve(t, theta_opt, M_opt, X_opt)

plt.figure(figsize=(8, 6))
plt.plot(x_data, y_data, 'ro', label='Given Data')
plt.plot(x_fit, y_fit, 'b-', label='Fitted Curve')
plt.legend()
plt.xlabel('x')
plt.ylabel('y')
plt.title('Curve Fitting Result')
plt.grid(True)
plt.show()

# -------------------------------------------------------
# Step 7: Compute L1 error
# -------------------------------------------------------
final_error = cost([theta_opt, M_opt, X_opt], t, x_data, y_data)
print(f"\nTotal L1 Error = {final_error:.6f}")
