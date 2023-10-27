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

def make_scatter_plot(nb_feature, feature_array, name_feature, all_feature_array):

	fig, axs = plt.subplots(2, 6, figsize=(20, 15))
	fig.suptitle(f"{name_feature}", fontsize=20)
	for i in [x for x in range(13) if x != nb_feature]:
		axs_pos = i if i < nb_feature else i - 1
		current_axs = axs[axs_pos // 6][axs_pos % 6]

		current_feature = []
		other_feature = []

		for it1, it2 in zip(feature_array, all_feature_array[i][1:]):
			if it1 and it2:
				current_feature.append(float(it1))
				other_feature.append(float(it2))

		min_feature, max_feature = (ft_min(current_feature), ft_max(current_feature))
		min_other, max_other = (ft_min(other_feature), ft_max(other_feature))

		current_axs.scatter(current_feature, other_feature, label=f"Compare with {all_feature_array[i][0]}")
		current_axs.set_xlabel(f"{name_feature}")
		current_axs.set_ylabel(f"{all_feature_array[i][0]}")
		current_axs.set_xlim(min_feature, max_feature)
		current_axs.set_ylim(min_other, max_other)

	plt.tight_layout()
	plt.show()

def main():
	path_dataset = "datasets/dataset_train.csv"
	# Create array of features
	arr_csv = csv_to_arr(path_dataset)
	arr_feature = sort_arr_by_feature(arr_csv)

	# Plot by feature
	for i in range (0, 13):
		make_scatter_plot(i, arr_feature[6 + i][1:], arr_feature[6 + i][0], arr_feature[6:])
	plt.close()

if __name__== "__main__":
  main()