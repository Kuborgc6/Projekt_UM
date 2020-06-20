from Training_data_class import Training_data_class

def make_training_data(data, no_trees, size):
    size_temp = int(size)
    training_data = []
    for x in range(no_trees):
        training_data.append(Training_data_class(data[(x*size_temp):(x*size_temp+size_temp)]))
    return training_data