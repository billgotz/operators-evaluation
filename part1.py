################################################
#### Onomateponimo: Vasileios Gkotzagiannis ####
#### Arithmos Mitrwou: 2672                 ####
#### Part 1                                 ####
################################################

# Util method to write to output file
def write_to_file(r_ptr, s_ptr, RS):
    RS.write("{key} \t {r_value} \t {s_value}\n".format(key = r_ptr[0], r_value = r_ptr[1], s_value = s_ptr[1]))

# Util method to read next line from params file (f) and split it by any white space
def next_line(f):
    retList = []
    line = f.readline().split()
    if line:
        retList.append(line[0])
        retList.append(int(line[1]))
    return retList


# Main method that implements the merge-join
def merge_join(R, S, RS):
    r_ptr = next_line(R)                    # First line of R
    s_ptr = next_line(S)                    # First line of S

    same_lines = []                         # buffer that will be used to save values of s when r==s
    max_buff_size = 0                       # will be used to calculate the maximum size of the same_lines buffer

    while r_ptr and s_ptr:                  # loop until r_ptr or s_ptr reaches end of file

        if r_ptr[0] == s_ptr[0]:            # check if r equals s 

            same_lines.append(s_ptr)        # add the line s into same_lines buffer     
            write_to_file(r_ptr,s_ptr, RS)  # write the line to output file

            s_ptr = next_line(S)            # read next line for s          
        
        elif r_ptr[0] > s_ptr[0]:           # check if r bigger than s
            s_ptr = next_line(S)            # if so, read next line of s
 
        elif r_ptr[0] < s_ptr[0]:           # check if r is smaller than s
            r_ptr_old = r_ptr               
            r_ptr = next_line(R)            # if so, read next line of s

            while r_ptr and r_ptr[0] == r_ptr_old[0]:   # check if next line is same as previous         
                for line in same_lines:                 # if so, join the r line with the same_lines buffer
                    write_to_file(r_ptr, line, RS)      
                r_ptr_old = r_ptr
                r_ptr = next_line(R)                    # check for next line of R

            # check for max buffer size
            if len(same_lines) > max_buff_size:         # check if the current iteration same_lines buffer 
                max_buff_size = len(same_lines)         # is bigger in size than previous buffer and if so, change the max_buff_size

            same_lines.clear()                          # clear the same_lines buffer

    # check the remaining r lines (if any) if they are the same with the last r
    if r_ptr:
        r_ptr_old = r_ptr
        r_ptr = next_line(R)

        while r_ptr and r_ptr[0] == r_ptr_old[0]:    # if they are the same join them with the same_lines buffer
            for line in same_lines:
                write_to_file(r_ptr, line, RS)
            r_ptr_old = r_ptr
            r_ptr = next_line(R)   

            if len(same_lines) > max_buff_size:
                max_buff_size = len(same_lines)

            same_lines.clear()  

    print("[Max buffer size: {max}]".format(max=max_buff_size))   

def main():
    with open('R_sorted.tsv', 'r') as R, open('S_sorted.tsv', 'r') as S, open('RjoinS.tsv', 'w') as RS:  
        merge_join(R, S, RS)

main()