################################################
#### Onomateponimo: Vasileios Gkotzagiannis ####
#### Arithmos Mitrwou: 2672                 ####
#### Part 3                                 ####
################################################
#from part2 import write_to_file,next_line,check_for_dups

# Util method to write to output file
def write_to_file(ptr, RS):
    RS.write("{key}\t{r_value}\n".format(key = ptr[0], r_value = ptr[1]))

# Util method to read next line from params file (f) and split it by any white space
def next_line(f):
    retList = []
    line = f.readline().split()
    if line:
        retList.append(line[0])
        retList.append(int(line[1]))
    return retList

def check_for_dups(new_ptr, old_ptr, file):
    while new_ptr and old_ptr == new_ptr:
        old_ptr = new_ptr
        new_ptr = next_line(file)
    return new_ptr

# Main method that implements the intersection
def intersection(R, S, RS):
    r_ptr = next_line(R)         # First line of R
    s_ptr = next_line(S)         # First line of S

    while r_ptr and s_ptr:      # loop until r_ptr or s_ptr reaches end of file

        if r_ptr == s_ptr:
            write_to_file(r_ptr, RS)
            r_ptr = check_for_dups(next_line(R), r_ptr, R)
            s_ptr = check_for_dups(next_line(S), s_ptr, S)
 
        elif r_ptr > s_ptr:  
            s_ptr = check_for_dups(next_line(S), s_ptr, S)

        elif r_ptr < s_ptr:  
            r_ptr = check_for_dups(next_line(R), r_ptr, R)



def main():
    with open('R_sorted.tsv', 'r') as R, open('S_sorted.tsv', 'r') as S, open('RintersectionS.tsv', 'w') as RS:  
        intersection(R, S, RS)

main()
