import csv
import sys
import matplotlib.pyplot as plt
import numpy as np
import copy

def csv_to_arr(filename):
    file = open(filename, 'r')
    csvreader = csv.reader(file)
    arr = []
    for row in csvreader:
        arr.append(row)
    return arr

def sort_arr_by_feature(arr_csv):
    arr_feature = []

    nbr_row = len(arr_csv)
    nbr_col = len(arr_csv[0])

    for j in range(0, nbr_col):
        arr_feature.append([arr_csv[0][j]])
        for i in range(1, nbr_row):
            arr_feature[j].append(arr_csv[i][j])
    return arr_feature

def erase_missing_coeff_lines(arr_feature, list_house):
    print(f"Initial number of data items : {len(arr_feature[0])}")
    for i in range(len(arr_feature)):
        j = 0
        while j < len(arr_feature[i]):
            if (arr_feature[i][j] == ''):
                for i2 in range(len(arr_feature)):
                    del(arr_feature[i2][j])
                del(list_house[j])
            else:
                j += 1
    print(f"Number of data items used : {len(arr_feature[0])}")
    return (arr_feature, list_house)

def ft_min(arr_feature):
    min = arr_feature[0]
    for feature in arr_feature:
        if feature < min :
            min = feature
    return min

def ft_max(arr_feature):
    max = arr_feature[0]
    for feature in arr_feature:
        if feature > max :
            max = feature
    return max

def sigmoid_function(x):
    return 1. / (1 + np.exp(-x))

# Cost function of h : vector of logistic value and y : the predictions
def cost_function(y, h):
        m = len(y)
        cost = (1 / m) * (np.sum(-y.dot(np.log(h)) - (1 - y).dot(np.log(1 - h))))
        return cost

def grad_descent(arr_data, h, y):
    return np.matmul(arr_data.T, (h - y)) / len(y)

def print_cost(list_cost_functions):
    x = np.linspace(0, len(list_cost_functions[0]), len(list_cost_functions[0]))

    # Plot the curves
    plt.plot(x, list_cost_functions[0], label='Gryffindor')
    plt.plot(x, list_cost_functions[1], label='Hufflepuff')
    plt.plot(x, list_cost_functions[2], label='Ravenclaw')
    plt.plot(x, list_cost_functions[3], label='Slytherin')

    # Add a legend
    plt.legend()

    # Add labels and title
    plt.xlabel('Iteration')
    plt.ylabel('Value')
    plt.title('Cost functions')

    # Show the plot
    plt.show()

def logistic_regression(X, list_house, nb_iter, lr):

    # Initialize coeff thetas, y value, cost function
    thetas = np.zeros((4, len(X[0])))
    y_G = [1 if (house == "Gryffindor") else 0 for house in list_house]
    y_H = [1 if (house == "Hufflepuff") else 0 for house in list_house]
    y_R = [1 if (house == "Ravenclaw") else 0 for house in list_house]
    y_S = [1 if (house == "Slytherin") else 0 for house in list_house]
    Y = np.array([y_G, y_H, y_R, y_S])
    list_cost_functions = [[] for _ in range(4)]

    for _ in range(nb_iter):
        for house_nb in range(4):
            y = Y[house_nb]
            theta = thetas[house_nb]

            # Compute gradient descent and cost function from sigmoid
            predictions = np.matmul(X, theta)
            h = sigmoid_function(predictions)
            gradient = grad_descent(X, h, y)
            current_cost = cost_function(y, h)

            # Update the model parameters
            thetas[house_nb] = theta - lr * gradient
            list_cost_functions[house_nb].append(current_cost)

    print_cost(list_cost_functions)

    return thetas

def print_final_coeff(path_print_result, name_feature, used_feature, min_array, max_array, arr_coeff):
    final_min_coeffs = []
    final_max_coeffs = []
    final_G_coeffs = []
    final_H_coeffs = []
    final_R_coeffs = []
    final_S_coeffs = []
    ind = 0
    for is_used in used_feature:
        if is_used:
            final_min_coeffs.append(min_array[ind])
            final_max_coeffs.append(max_array[ind])
            final_G_coeffs.append(arr_coeff[0][ind])
            final_H_coeffs.append(arr_coeff[1][ind])
            final_R_coeffs.append(arr_coeff[2][ind])
            final_S_coeffs.append(arr_coeff[3][ind])
            ind += 1
        else:
            final_min_coeffs.append(0)
            final_max_coeffs.append(1)
            final_G_coeffs.append(0)
            final_H_coeffs.append(0)
            final_R_coeffs.append(0)
            final_S_coeffs.append(0)

    header_csv = ['Name feature', 'Min', 'Max', 'Coeff Gryffindor', 'Coeff Hufflepuff', 'Coeff Ravenclaw', 'Coeff Slytherin']
    data_csv = np.transpose(np.array([name_feature, final_min_coeffs, final_max_coeffs, final_G_coeffs, final_H_coeffs, final_R_coeffs, final_S_coeffs])).tolist()

    # Print coefficients in a csv
    f = open(path_print_result, 'w')
    writer = csv.writer(f)
    writer.writerow(header_csv)
    writer.writerows(data_csv)
    print(f"Coefficients written in \"{path_print_result}\"")

def main():
    path_dataset = "datasets/dataset_train.csv"
    path_print_result = "coeffs_logistic_regression.csv"
    if len(sys.argv) > 1:
         path_print_result = sys.argv[1]

    # Create array of features from csv
    arr_csv = csv_to_arr(path_dataset)
    arr_feature = sort_arr_by_feature(arr_csv)

    # Select features
    #            Arithm,Astron,Herbol,DefAgDrk,Div,MugglStud,AncRunes,HistOMag,Transfig,Potions,CarOMagicCreat,Charms,Flying
    used_feature = [0,     0,     1,      1,    1,      1,      1,        1,        0,      0,       0,           1,     0]
    arr_feature_used = []
    for pos, is_used in enumerate(used_feature) :
        if is_used:
            arr_feature_used.append(copy.deepcopy(arr_feature[6 + pos][1:]))

    # Transform lists to be usable by logistic regression
    arr_feature_used, list_house = erase_missing_coeff_lines(arr_feature_used, arr_feature[1][1:])
    arr_feature_used = [list(map(float, feature)) for feature in arr_feature_used]

    # Add constant term to compute bias during logistic regression
    arr_feature_used.insert(0, np.ones(len(arr_feature_used[0])).tolist())
    used_feature.insert(0, 1)

    arr_feature_used = np.array(arr_feature_used)

    # Normalize coeffs
    min_array = np.array([ft_min(feature) for feature in arr_feature_used])
    max_array = np.array([ft_max(feature) for feature in arr_feature_used])
    min_array[0] = 0.
    for i in range(1, len(arr_feature_used)):
        arr_feature_used[i] = (arr_feature_used[i] - min_array[i]) / (max_array[i] - min_array[i])

    # Logistic regression
    print("Performing logistic regression...")
    arr_coeff = logistic_regression(np.transpose(arr_feature_used), list_house, 3000, 0.5)

    # Print final info in a csv
    name_feature = [feature[0] for feature in arr_feature[6:]]
    name_feature.insert(0, "Bias")
    print_final_coeff(path_print_result, name_feature, used_feature, min_array, max_array, arr_coeff)

if __name__== "__main__":
  main()