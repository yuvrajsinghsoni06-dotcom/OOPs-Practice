import matplotlib.pyplot as plt

def solve_euler(k, y0, dt, total_time):
    # Initialize lists to store history
    times = [0]
    y_values = [y0]
    
    current_y = y0
    current_t = 0
    
    # The Loop
    while current_t < total_time:
        # 1. Calculate the derivative (slope) based on the DE
        dydt = -k * current_y
        
        # 2. Update y
        current_y = current_y + (dydt * dt)
        
        # 3. Step time forward
        current_t += dt
        
        # Store results
        times.append(current_t)
        y_values.append(current_y)
        
    return times, y_values

# Run the simulation
t, y = solve_euler(k=0.5, y0=5, dt=0.1, total_time=10)

plt.plot(t, y)
plt.title("Euler's Method: Exponential Decay")
plt.show()