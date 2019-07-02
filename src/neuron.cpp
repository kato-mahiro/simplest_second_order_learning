#include "random.cpp"
#include<iostream>
#include<iomanip>

enum TypeOfNeuron
{
    Input = 0,
    Hidden = 1,
    Output = 2,
    Moduration_1 = 3,
    Moduration_2 = 4,
    Moduration_3 = 5,
};

class Neuron
{
    private:
    float bias;
    float activation;
    TypeOfNeuron type;

    public:
    Neuron(TypeOfNeuron type);
    void self_introduction(void);
};

Neuron::Neuron(TypeOfNeuron t) //initialize randomly
{
    bias = rnd(-1000000,1000000) / 1000000.0;
    activation = 0.0;
    type = t;
}

void Neuron::self_introduction(void)
{
    std::cout << "---" << std::endl;
    std::cout << "I am a neuron." << std::endl;
    std::cout << "my bias is: " << std::setprecision(10) << bias << std::endl;
    std::cout << "my type is: " << type << std::endl;
}

int main(void)
{
    Neuron n(Input);
    Neuron n2(Output);
    n.self_introduction();
    n2.self_introduction();
    return 0;
}
