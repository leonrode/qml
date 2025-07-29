# Fixed version of the run function
def run():
    theta = 0.01
    eta = 0.1
    epochs = 200
    thetas = [None] * epochs
    costs = [None] * epochs
    
    initial_state = [complex(1), complex(0)]
    for epoch_num in range(epochs):
        state = circuit(theta)
        print(qml.draw(circuit)(theta))
        print(state)
        g, theta = update_rule(theta, eta, initial_state)

run() 