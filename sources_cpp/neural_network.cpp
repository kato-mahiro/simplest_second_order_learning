#include "random.cpp"
#include "neuron.cpp"
#include<vector>
#include<iostream>

class NeuralNetwork
{
    private:
    int num_of_neurons;
    std::vector<int> input_vector;
    std::vector<float> output_vefctor;
    std::vector<Neuron> neuron_array;
    std::vector< std::vector<float> > weight_matrix;

    public:
    NeuralNetwork(int num_of_neurons);
    void add_a_neuron(int no);
    void delete_a_neuron(int no);
    void update_output();
    *int get_output();
    void hebbian_update(void);
};

NeuralNetwork::NeuralNetwork(int num_of_neurons)
{
    
}
