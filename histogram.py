import csv
import matplotlib.pyplot as plt

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

# Create an unique histogram for the feature
def make_one_histogram(arr_house, name_feature, arr_feature, axis):
	arr_Gryffindor = []
	arr_Hufflepuff = []
	arr_Ravenclaw = []
	arr_Slytherin = []

	for i in range(1, len(arr_feature)):
		if arr_house[i] == "Gryffindor" :
			arr_Gryffindor.append(arr_feature[i])
		elif arr_house[i] == "Hufflepuff" :
			arr_Hufflepuff.append(arr_feature[i])
		elif arr_house[i] == "Ravenclaw" :
			arr_Ravenclaw.append(arr_feature[i])
		elif arr_house[i] == "Slytherin" :
			arr_Slytherin.append(arr_feature[i])
		else :
			print(f"Unknown house : {arr_house[i]}")
			exit(1)
	axis.hist(arr_Gryffindor, ec="black", color="crimson", bins=25, alpha=0.8, label='Gryffindor')
	axis.hist(arr_Hufflepuff, ec="black", color="yellow",  bins=25, alpha=0.6, label='Hufflepuff')
	axis.hist(arr_Ravenclaw,  ec="black", color="blue",    bins=25, alpha=0.6, label='Ravenclaw')
	axis.hist(arr_Slytherin,  ec="black", color="green",   bins=25, alpha=0.6, label='Slytherin')
	axis.legend(loc='upper right')
	axis.set_title(name_feature)

# Make an histogram by house
def make_hist_by_house(arr_house, name_feature, arr_feature):
	arr_Gryffindor = []
	arr_Hufflepuff = []
	arr_Ravenclaw = []
	arr_Slytherin = []

	[min, max] = [ft_min(arr_feature), ft_max(arr_feature)]

	for i in range(1, len(arr_feature)):
		if arr_house[i] == "Gryffindor" :
			arr_Gryffindor.append(arr_feature[i])
		elif arr_house[i] == "Hufflepuff" :
			arr_Hufflepuff.append(arr_feature[i])
		elif arr_house[i] == "Ravenclaw" :
			arr_Ravenclaw.append(arr_feature[i])
		elif arr_house[i] == "Slytherin" :
			arr_Slytherin.append(arr_feature[i])
		else :
			print(f"Unknown house : {arr_house[i]}")
			exit(1)
	fig, axs = plt.subplots(2, 2, sharey=True, tight_layout=True, figsize=(15, 10))
	fig.suptitle(f"{name_feature}", fontsize=30)

	axs[0][0].hist(arr_Gryffindor, ec="black", color="darkred", bins=25, alpha=1, label='Gryffindor')
	axs[0][0].set_title("Gryffindor")
	axs[0][0].set_xlim(min, max)

	axs[0][1].hist(arr_Hufflepuff, ec="black", color="yellow", bins=25, alpha=1, label='Hufflepuff')
	axs[0][1].set_title("Hufflepuff")
	axs[0][1].set_xlim(min, max)

	axs[1][0].hist(arr_Ravenclaw, ec="black", color="blue", bins=25, alpha=1, label='Ravenclaw')
	axs[1][0].set_title("Ravenclaw")
	axs[1][0].set_xlim(min, max)

	axs[1][1].hist(arr_Slytherin, ec="black", color="green", bins=25, alpha=1, label='Slytherin')
	axs[1][1].set_title("Slytherin")
	axs[1][1].set_xlim(min, max)

def main():
	path_dataset = "datasets/dataset_train.csv"
	# Create array of features
	arr_csv = csv_to_arr(path_dataset)
	arr_feature = sort_arr_by_feature(arr_csv)

	# Unique plot
	fig, axs = plt.subplots(2, 7, sharey=True, tight_layout=True, figsize=(20, 15))
	fig.suptitle(f"Global distribution", fontsize=20)

	for i in range (0, 13):
		make_one_histogram(arr_feature[1], arr_feature[6 + i][0],
				 		list(map(float, arr_feature[6 + i][1:])), axs[i // 7][i % 7])
	plt.show()

	# Plot by feature
	for i in range (0, 13):
		make_hist_by_house(arr_feature[1], arr_feature[6 + i][0],
				 		list(map(float, arr_feature[6 + i][1:])))
		plt.show()

	plt.close()

if __name__== "__main__":
  main()