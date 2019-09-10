import pickle

def get(name):
    with open(name,'rb') as f:
        agents = pickle.load(f)
        return agents
