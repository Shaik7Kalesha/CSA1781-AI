import math

# Define sigmoid activation function
def sigmoid(x):
    return 1 / (1 + math.exp(-x))

# Define the feedforward neural network class
class NeuralNetwork:
    def __init__(self, input_size, hidden_size, output_size):
        self.input_size = input_size
        self.hidden_size = hidden_size
        self.output_size = output_size
        
        # Initialize weights and biases for the hidden layer and output layer
        self.hidden_weights = [[0.1] * self.input_size for _ in range(self.hidden_size)]
        self.hidden_bias = [0.1] * self.hidden_size
        
        self.output_weights = [[0.1] * self.hidden_size for _ in range(self.output_size)]
        self.output_bias = [0.1] * self.output_size
    
    def forward(self, input_data):
        # Calculate hidden layer outputs
        hidden_outputs = []
        for i in range(self.hidden_size):
            weighted_sum = sum(input_data[j] * self.hidden_weights[i][j] for j in range(self.input_size))
            weighted_sum += self.hidden_bias[i]
            hidden_outputs.append(sigmoid(weighted_sum))
        
        # Calculate final outputs
        final_outputs = []
        for i in range(self.output_size):
            weighted_sum = sum(hidden_outputs[j] * self.output_weights[i][j] for j in range(self.hidden_size))
            weighted_sum += self.output_bias[i]
            final_outputs.append(sigmoid(weighted_sum))
        
        return final_outputs

# Create a neural network with 2 input neurons, 2 hidden neurons, and 1 output neuron
nn = NeuralNetwork(input_size=2, hidden_size=2, output_size=1)

# Sample input data
input_data = [0.5, 0.8]

# Make a forward pass through the neural network
output = nn.forward(input_data)

print("Input Data:", input_data)
print("Output:", output)
