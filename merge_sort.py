

class SortedList:
	def __init__(self, array):
		self.array = array
		self.length = len(array)
	
	def __getitem__(self, position):
		return self.array[position]
	
	def __str__(self):
		return str(self.array)

	def __len__(self):
		return self.length
	
	def __add__(self, second_sorted_list):
		i = j = 0
		new_array = []
		while True:
			if self[i] < second_sorted_list[j]:
				new_array.append(self[i])
				i = i + 1
				if i == self.length:
					new_array = new_array + second_sorted_list[j:]
					break
			else:
				new_array.append(second_sorted_list[j])
				j = j + 1
				if j == second_sorted_list.length:
					new_array = new_array + self[i:]
					break
		
		return SortedList(new_array)

		


def mergeSort(array):
	array_length = len(array)
	if array_length == 1:
		return array
	else:
		first_half = int(array_length/2)
		second_half = int(array_length/2)
		first_half_array = mergeSort(array[:first_half])
		second_half_array = mergeSort(array[second_half:]) 		
		new_array = SortedList(first_half_array) + SortedList(second_half_array)

	return new_array


print(mergeSort([2, 1, 4, 3, 9 , 8]))