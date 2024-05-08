array = [1,2,3,4,5,6,7,8,9,10]
result = 8

def find_sum(array, result):
  end = len(array)
  begin = 0

  while begin < end:
    if array[begin] + array[end] == result:
      return begin, end
    elif array[begin] + array[end] < result:
      begin += 1
    else:
      end -= 1

  return -1, -1

print(find_sum(array, result))

