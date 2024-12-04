def Ex12(arr, start, sum):
	if start == len(arr) - 1:
		return sum
	sum += arr[start + 1]
	return Ex12(arr, start + 1, sum)

example = [94, 6, 50, 140]
print(Ex12(example, 0, example[0])) 
# Parameters: Array, IDX to start, Initial value/sum for the first iteration.