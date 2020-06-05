kadanes_list = [5, 7, -3, 2, 9, 6, 16, 22, 21, 29, -14, 10, 12]

# 1. Iterate over the list
# 2. Add the first and second element
# 3. Store the value as curr value
# 4. If current value is greater than larger sum replace larger sum with new value
# 5. Else 

def kadanes(li):

	largest_current, largest_global = li[0]

	for i in range(1, len(li)-1):
		largest_current = max(li[i], largest_current + li[i])

		if largest_current > largest_global:
			largest_global = largest_current

	return largest_global

print(kadanes(kadanes_list))

