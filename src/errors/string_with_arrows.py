
def string_with_arrows(text, pos_start, pos_end):
    result = ''
    
    # calculate indices
    index_start = max(text.rfind('\n', 0, pos_start.index), 0)
    index_end = text.find('\n', index_start + 1)
    if index_end < 0: index_end = len(text)
    
    # generate each line
    line_count = pos_end.line_no - pos_start.line_no +1
    for i in range(line_count):
        # calculate line columns
        line = text[index_start:index_end]
        col_start = pos_start.cols if i == 0 else 0
        col_end = pos_end.cols if i == line_count -1 else len(line) - 1
        
        # append result
        result += line + '\n'
        result += ' ' * col_start + '^' * (col_end - col_start)
        
        # re-calculate indices
        index_start = index_end
        index_end = text.find('\n', index_start + 1)
        if index_end < 0: index_end = len(text)
        
    return result.replace('\t', '')