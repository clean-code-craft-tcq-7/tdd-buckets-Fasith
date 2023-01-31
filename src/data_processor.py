def get_range_and_frequency(data : list):
    sorted_data = sorted(data)
    output = []
    if len(sorted_data) == 0:
        return output 

    min_val, max_val, freq = sorted_data[0], sorted_data[0], 1
    for i in range(1, len(sorted_data)):
        cur_val = sorted_data[i]
        if(cur_val > max_val + 1):
            output.append((min_val, max_val, freq))
            min_val = cur_val
            max_val = cur_val
            freq = 1
        else:
            max_val = cur_val
            freq += 1
    
    return output


