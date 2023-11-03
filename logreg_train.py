import csv
import sys
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

def erase_missing_coeff_lines(arr_feature):
    print(f"Initial number of data : {len(arr_feature[0])}")
    for i in range(len(arr_feature)):
        j = 0
        while j < len(arr_feature[i]):
            if (arr_feature[i][j] == ''):
                for i2 in range(len(arr_feature)):
                    del(arr_feature[i2][j])
            else:
                j += 1
    print(f"Number of data without line without missing coefficient : {len(arr_feature[0])}")
    return arr_feature

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

def house_to_number(house):
    if house == "Gryffindor":
        return 1
    elif house == "Hufflepuff":
        return 2
    elif house == "Ravenclaw":
        return 3
    elif house == "Slytherin":
        return 4
    else:
        print(f"Error {house} is not a known house")
        exit(1)

def logistic_regression(arr_feature, list_house, nb_iter, lr):
    coeff = np.zeros((4, len(arr_feature)))
    print(coeff)

    # HERE FUTUR LOGISTIC REGRESSION
    return coeff

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
    print(f"Coefficients of logistic regression writed in {path_print_result}")

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

    # Transform list to be usable by logistic regression
    arr_feature_used = erase_missing_coeff_lines(arr_feature_used)
    arr_feature_used = np.array([list(map(float, feature)) for feature in arr_feature_used])

    # Normalize coeffs
    min_array = np.array([ft_min(feature) for feature in arr_feature_used])
    max_array = np.array([ft_max(feature) for feature in arr_feature_used])
    for i in range(len(arr_feature_used)):
        arr_feature_used[i] = (arr_feature_used[i] - min_array[i]) / (max_array[i] - min_array[i])

    # Create house list
    list_house = np.array(list(map(house_to_number, arr_feature[1][1:])))

    # Logistic regression
    arr_coeff = logistic_regression(arr_feature_used, list_house, 1000, 0.001)

    # Print final info in a csv
    print_final_coeff(path_print_result, [feature[0] for feature in arr_feature[6:]], used_feature, min_array, max_array, arr_coeff)

if __name__== "__main__":
  main()