from re import S
import sys
import csv

def csv_to_arr(filename):
	file = open(filename, 'r')
	csvreader = csv.reader(file)
	arr = []
	for row in csvreader:
		arr.append(row)
	return arr

def main():
	if (len(sys.argv) != 2):
		print ("put one and only one argument")
		return(1)
	arr_csv = csv_to_arr(sys.argv[1])
	if len(arr_csv) == 0 :
		print("empty data")
		return 1
	nbr_row = len(arr_csv)
	nbr_col = len(arr_csv[0])
	print ("nbr row arr : " + str(len(arr_csv)) + ", nbr column : " + str(len(arr_csv[0])))
	arr_feature = []
	for j in range(0, nbr_col - 1):
		print ("j : " + str(j))
		arr_feature.append([arr_csv[0][j]])
		for i in range(1, nbr_row):
			arr_feature[j].append(arr_csv[i][j])
	print(arr_feature[0])
	print(arr_feature[6])

if __name__== "__main__":
  main()