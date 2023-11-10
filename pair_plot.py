#! /usr/bin/python3
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

def make_pair_plot(arr_feature):

	fig, axs = plt.subplots(13, 13, tight_layout=False, figsize=(20, 15))
	all_feature_array = arr_feature[6:]

	for i in range (0, 13):
		feature_array = arr_feature[6 + i][1:]
		name_feature = arr_feature[6 + i][0]

		for j in [x for x in range(13)]:
			current_axs = axs[i][j]
			# Ignore same feature plot
			if i == j:
				if i == 12:
					current_axs.set_xlabel(f"{all_feature_array[j][0]}".replace(" ", "\n"), fontsize=9)
				if j == 0:
					current_axs.set_ylabel(f"{name_feature}".replace(" ", "\n"), fontsize=9)
				continue

			(cur, oth, color_map) = ([], [], [])
			for id, (it1, it2) in enumerate(zip(feature_array, all_feature_array[j][1:]), start=1):
				if it1 and it2:
					cur.append(float(it1))
					oth.append(float(it2))
					if arr_feature[1][id] == "Gryffindor":
						color_map.append("crimson")
					elif arr_feature[1][id] == "Hufflepuff":
						color_map.append("yellow")
					elif arr_feature[1][id] == "Ravenclaw":
						color_map.append("blue")
					elif arr_feature[1][id] == "Slytherin":
						color_map.append("green")

			min_feature, max_feature = (ft_min(cur), ft_max(cur))
			min_other, max_other = (ft_min(oth), ft_max(oth))

			current_axs.scatter(cur, oth, s=1.0, color = color_map, alpha = 0.6)
			current_axs.set_xlim(min_feature, max_feature)
			current_axs.set_ylim(min_other, max_other)
			if i == 12:
				current_axs.set_xlabel(f"{all_feature_array[j][0]}".replace(" ", "\n"), fontsize=9)
			if j == 0:
				current_axs.set_ylabel(f"{name_feature}".replace(" ", "\n"), fontsize=9)

	plt.tight_layout()
	plt.show()

	# Show correlation best hand by house
	arr_hand = [1 if best_hand == "Left"
			 	else -1 for best_hand in arr_feature[5][1:]]

	plt.scatter(arr_feature[0][1:], arr_hand, color = color_map, alpha = 0.6)
	plt.title("Bests hand - houses")
	plt.show()

	plt.close()

def main():
	path_dataset = "datasets/dataset_train.csv"

	# Create array of features
	arr_csv = csv_to_arr(path_dataset)
	arr_feature = sort_arr_by_feature(arr_csv)

	# Plot pair plot
	make_pair_plot(arr_feature)

if __name__== "__main__":
  main()
