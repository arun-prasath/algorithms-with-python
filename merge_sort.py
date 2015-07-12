def merge_sort(arr_A):
    length_A = len(arr_A)
    
    if length_A == 1: 
        return arr_A
    
    else :
        arr_B = merge_sort(arr_A[:length_A/2])
        arr_C = merge_sort(arr_A[length_A/2:])
        arr_D = merge_and_sort(arr_B, arr_C)
            
    return arr_D
    
def merge_and_sort(arr_B, arr_C):
    length_B, length_C = len(arr_B), len(arr_C)
    output_len = length_B + length_C
    i = j = 0
    arr_D = []
    
    for k in range(0, output_len):
        if i == length_B:
            arr_D += arr_C[j:]
            break
        elif j == length_C:
            arr_D += arr_B[i:]
            break
        elif arr_B[i] < arr_C[j]:
            arr_D.append(arr_B[i])
            i += 1
        else:
            arr_D.append(arr_C[j])
            j += 1
    
    return arr_D

a = [5, 6, 16, 2, 7, 1, 12, 15, 9, 10, 8, 3, 4, 14, 11, 13]
print merge_sort(a)