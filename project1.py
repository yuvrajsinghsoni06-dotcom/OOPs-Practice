class PredatorPrey:
    # Phase - 1 physical model of the environment
    def __init__(self,alpha,beta,delta,gamma):
        self.alpha = alpha
        self.beta = beta
        self.delta = delta
        self.gamma = gamma

    def get_derivative(self,state,t):
        R = state[0]
        F = state[1]

        dR_dt = (self.alpha * R) - (self.beta * R * F)
        dF_dt = (self.delta * R * F) - (self.gamma * F)
        return [dR_dt , dF_dt]
    
    # Phase-2 the engine of the car
class EulerSolver:
    def step(self,model,current_state, dt, current_time):
        rates = model.get_derivative(current_state,current_time)
        dR_dt = rates[0]
        dF_dt = rates[1]

        current_R = current_state[0]
        current_F = current_state[1]

        new_R =  current_R + (dR_dt * dt)
        new_F =  current_F + (dF_dt * dt)

        
        return [new_R,new_F]
    
class RK4Solver:
    def step(self, model, state, dt, t):
        # Unpack state
        # (We keep it generic so it works for ANY model)
        
        # k1: Slope at the beginning
        k1 = model.get_derivative(state, t)
        
        # k2: Slope at the midpoint (using k1 to look ahead)
        state_k2 = [s + k * dt / 2 for s, k in zip(state, k1)]
        k2 = model.get_derivative(state_k2, t + dt / 2)
        
        # k3: Another slope at the midpoint (using k2)
        state_k3 = [s + k * dt / 2 for s, k in zip(state, k2)]
        k3 = model.get_derivative(state_k3, t + dt / 2)
        
        # k4: Slope at the end
        state_k4 = [s + k * dt for s, k in zip(state, k3)]
        k4 = model.get_derivative(state_k4, t + dt)
        
        # Combine them (Weighted Average)
        # New = Old + (k1 + 2k2 + 2k3 + k4) * dt / 6
        new_state = []
        for i in range(len(state)):
            change = (k1[i] + 2*k2[i] + 2*k3[i] + k4[i]) / 6
            new_state.append(state[i] + change * dt)
            
        return new_state
    
#phase-3 the simulation loop 
world = PredatorPrey(1.1,0.4,0.1,0.4)
solver = RK4Solver()

t = 0
dt = 0.01
state = [10,5]

history_R = []
history_F = []
history_t = []

while t < 50:
    history_R.append(state[0])
    history_F.append(state[1])
    history_t.append(t)
    
    # B. Calculate the NEXT state using the solver
    # HINT: Call solver.step(...) and save the result back into 'state'
    state = solver.step(world,state,dt,t)
    
    # C. Move time forward
    t += dt

# 4. Print the final results
print(f"Final Rabbits: {state[0]:.2f}")
print(f"Final Foxes: {state[1]:.2f}")


    
