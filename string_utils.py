def split_at_first_digit(formula):
    prefix = ""
    number_start_index = -1

    for i, char in enumerate(formula):
        if char.isdigit():
            number_start_index = i
            break
        prefix += char

    if number_start_index == -1:
        return formula, 1   
    
    number_part = formula[number_start_index:]
    return prefix, int(number_part)


def split_before_each_uppercase(formula):
    if not formula:
        return []

    results = []
    current_chunk = formula[0]

    for i in range (1, len(formula)):
        char = formula[i]

        if char.isupper():
            results.append(current_chunk)
            current_chunk = char
        else:
            current_chunk += char

    if current_chunk:
        results.append(current_chunk)
        
    return results
    
