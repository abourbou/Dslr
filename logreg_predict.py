#! /usr/bin/python3
import sys
import csv
import numpy as np

def csv_to_arr(filename):
    file = open(filename, 'r')
    csvreader = csv.reader(file)
    arr = []
    for row in csvreader:
        arr.append(row)
    if len(arr) == 0 :
        print("empty data")
        exit(1)

    return arr

def load_coeffs(filename):
    min_arr = []
    max_arr = []
    coeffs = [[], [], [], []]

    # Create a CSV reader object
    file = open(filename, 'r')
    reader = csv.reader(file)
    next(reader)

    # Load the data
    for row in reader:
        min_arr.append(float(row[1]))
        max_arr.append(float(row[2]))
        coeffs[0].append(float(row[3]))
        coeffs[1].append(float(row[4]))
        coeffs[2].append(float(row[5]))
        coeffs[3].append(float(row[6]))

    return (np.array(min_arr), np.array(max_arr), np.array(coeffs))

def sigmoid_function(x):
    return 1. / (1. + np.exp(-x))

def predict(dataset_test, coeffs):
    # Predict the house of the dataset
    predictions = sigmoid_function(np.matmul(dataset_test, coeffs))

    # Take the best prediction
    result = []
    for prediction in predictions:
        result.append(np.argmax(prediction))
    return result

def write_result(prediction):
    file = open("houses.csv", "w")
    file.write(f"Index,Hogwarts House\n")
    for i in range(len(prediction)):
        house = ""
        if prediction[i] == 0:
            house = "Gryffindor"
        elif prediction[i] == 1:
            house = "Hufflepuff"
        elif prediction[i] == 2:
            house = "Ravenclaw"
        else:
            house = "Slytherin"
        file.write(f"{i},{house}\n")
    print(f"Results written to house.csv file")

def main():
    if (len(sys.argv) != 3):
        print ("use : python3 logreg_predict.py datasets/dataset_test.csv coeffs_logistic_regression.csv")
        return(1)

    # Load coefficients of logistic regression
    min_arr, max_arr, coeffs = load_coeffs(sys.argv[2])

    # Create array of features
    dataset_test = csv_to_arr(sys.argv[1])
    dataset_test = [[float(elem) if elem != ''
                 else 0.
                 for elem in feature[6:]] for feature in dataset_test[1:]]

    # # Insert bias
    for i in range(len(dataset_test)):
        dataset_test[i].insert(0, 1)

    # Normalize data
    dataset_test = np.array(dataset_test).transpose()
    for i in range(len(dataset_test)):
        dataset_test[i] = (dataset_test[i] - min_arr[i]) / (max_arr[i] - min_arr[i])

    prediction = predict(dataset_test.T, coeffs.T)
    write_result(prediction)

if __name__== "__main__":
  main()