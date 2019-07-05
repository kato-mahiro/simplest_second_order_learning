#include<vector>
#include"../neuron.cpp"

int main(void)
{
    Neuron n1(Input);
    Neuron n2(Output);
    n1.self_introduction();
    n2.self_introduction();

    std::vector<Neuron> neurons;
    neurons.push_back(n1);
    neurons.push_back(n2);
    neurons.push_back(Neuron(Moduration));

    for(int i=0; i<3; i++)
    {
        neurons[i].self_introduction();
    }
    return 0;
}
