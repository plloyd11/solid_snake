bunch_of_shit = [10, 2, 76, 23, 25, 1, 8123]

def largest_even_number(numbers):
  even_nums = []
  for num in numbers:
      if num % 2 == 0:
          even_nums.append(num)
  return max(even_nums)

print(largest_even_number(bunch_of_shit))
