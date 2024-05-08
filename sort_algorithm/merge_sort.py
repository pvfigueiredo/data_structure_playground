class MergeSort:
    @staticmethod
    def sort(in_list: list):
        if (length := len(in_list)) > 1:
            mid = length // 2
            left = in_list[:mid]
            right = in_list[mid:]
            
            MergeSort.sort(in_list=left)
            MergeSort.sort(in_list=right)
            i = j = k = 0

            while i < len(left) and j < len(right):
                if left[i] < right[j]:
                    in_list[k] = left[i]
                    i += 1
                else:                
                    in_list[k] = right[j]
                    j += 1
                k += 1
            
            while i < len(left):
                in_list[k] = left[i]
                i += 1
                k += 1
            
            while j < len(right):
                in_list[k] = right[j]
                j += 1
                k += 1               
