import sys
import csv
import math
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
			if arr_csv[i][j] != '' :
				arr_feature[j].append(arr_csv[i][j])
	return arr_feature

def is_float(string):
    try:
        float(string)
        return True
    except ValueError:
        return False

def describe_arr(arr_feature):
	arr_name = [subarray[0] for subarray in arr_feature]
	arr_data = [subarray[1:] for subarray in arr_feature]

	means = [sum(map(float, subarray)) / len(subarray) if (subarray and is_float(subarray[0]))
			else float('nan')
			for subarray in arr_data]

	std_devs = []
	for i in range(len(arr_data)):
		subarray = arr_data[i]
		std_dev = 0
		if (subarray and is_float(subarray[0])):
			for elem in subarray:
				std_dev += (float(elem) - means[i]) ** 2
			std_dev = math.sqrt(std_dev / len(subarray))
		else:
			std_dev = float('nan')
		std_devs.append(std_dev)

	mins = []
	first_quartiles = []
	medians = []
	third_quartiles = []
	maxs = []
	for i in range(len(arr_data)):
		fst_quart_pos = math.ceil(len(subarray) / 4)
		trd_quart_pos = math.ceil(len(subarray) / 4 * 3)

		subarray = copy.deepcopy(arr_data[i])
		if (subarray and is_float(subarray[0])):
			subarray = list(map(float, subarray))
			subarray.sort()
			mins.append(subarray[0])
			first_quartiles.append(subarray[fst_quart_pos] - 1)
			median_pos = len(subarray) / 2.
			if (median_pos.is_integer()) :
				medians.append((subarray[int(median_pos) - 1] + subarray[int(median_pos)]) / 2.)
			else :
				medians.append(subarray[math.ceil(median_pos) - 1])
			third_quartiles.append(subarray[trd_quart_pos] - 1)
			maxs.append(subarray[-1])
		else :
			mins.append(float('nan'))
			first_quartiles.append(float('nan'))
			medians.append(float('nan'))
			third_quartiles.append(float('nan'))
			maxs.append(float('nan'))


	print("*********************************************************************************************************************************************")
	print(f"{'Name' [:15]:<20}\t{'Count':<10}\t{'Mean':<10}\t{'Std':<10}\t{'Min':<10}\t{'25%':<10}\t{'50%':<10}\t{'75%':<10}\t{'Max':<10}")
	print("---------------------------------------------------------------------------------------------------------------------------------------------")
	for i in range(len(arr_name)):
		print(f"{arr_name[i] [:15]:<20}\t", end="")
		print(f"{len(arr_data[i]) :<10}\t", end="")
		print(f"{means[i] :<10.3f}\t", end="")
		print(f"{std_devs[i] :<10.3f}\t", end="")
		print(f"{mins[i] :<10.3f}\t", end="")
		print(f"{first_quartiles[i] :<10.3f}\t", end="")
		print(f"{medians[i] :<10.3f}\t", end="")
		print(f"{third_quartiles[i] :<10.3f}\t", end="")
		print(f"{maxs[i] :<10.3f}\t", end="")
		print()

def main():
	if (len(sys.argv) != 2):
		print ("put one and only one argument")
		return(1)
	# Create array of features
	arr_csv = csv_to_arr(sys.argv[1])
	if len(arr_csv) == 0 :
		print("empty data")
		return 1
	arr_feature = sort_arr_by_feature(arr_csv)


	# Describe the array
	describe_arr(arr_feature)

if __name__== "__main__":
  main()