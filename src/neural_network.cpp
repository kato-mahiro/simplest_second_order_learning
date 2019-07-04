#include "random.cpp"
#include "neuron.cpp"
#include<iostream>

class NeuralNetwork
{
    private:
    int num_of_neurons;
    float connections; //2x2 list
    int input_vector[];

    Neuron *neurons;

    public:
    NeuralNetwork(int num_of_neurons);
    void add_a_neuron(int no);
    void delete_a_neuron(int no);
    void update_output();
    void hebbian_update(void);
    void 1st_moduratory_update(void);
    void 2nd_moduratory_update(void);
    void 3rd_moduratory_update(void);
};

NeuralNetwork::NeuralNetwork(int num_of_neurons)
{
    
}
