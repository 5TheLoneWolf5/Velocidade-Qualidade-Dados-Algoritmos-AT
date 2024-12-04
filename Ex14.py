def Ex14(arr, start, sum):
	if start == len(arr) - 1:
		return sum
	sum = int(sum + arr[start + 1])
	return Ex14(arr, start + 1, sum)

example = [1, 2, 3, 4, 5]
print(Ex14(example, 0, example[0])) 