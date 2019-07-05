#include "random.cpp"
#include<iostream>
#include<iomanip>

enum TypeOfNeuron
{
    Input = 0,
    Hidden = 1,
    Output = 2,
    Moduration = 3,
};

class Neuron
{
    private:
    float bias;
    float activation;
    TypeOfNeuron type;

    public:
    Neuron(TypeOfNeuron type);
    float get_bias(void){return bias;}
    float get_activation(void){return activation;}
    void  set_activation(float a){activation = a;}
    TypeOfNeuron get_type(void){return type;}
    void self_introduction(void);
};

Neuron::Neuron(TypeOfNeuron t) //initialize bias randomly
{
    int random_v = rnd(-1000000,1000000);
    if(!random_v){ bias = 0.0; }
    else{ bias = random_v / 1000000.0; }
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
