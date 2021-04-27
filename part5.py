################################################
#### Onomateponimo: Vasileios Gkotzagiannis ####
#### Arithmos Mitrwou: 2672                 ####
#### Part 5                                 ####
################################################

def fix_line(line):
    return [line.split()[0], int(line.split()[1])]

def merge(left, right):
    #print("Merging the list.... \n {} \n with \n {}\n End of list.\n".format(left, right))
    result = []
    
    while left and right:

        if (left[0][0] == right[0][0]):

            result.append([left[0][0], right[0][1] + left[0][1]])
            right.pop(0)
            left.pop(0)

        elif (left[0][0] > right[0][0]):
            result.append(right[0])
            right.pop(0)

        else:
            result.append(left[0])
            left.pop(0)
   
    while left:        
        result.append(left[0])
        left.pop(0)

    while right:
        result.append(right[0])
        right.pop(0)
   
    #print("Merge result is the list.... \n {} \n End of list.\n".format(result))
    return result

def sort_merge(r_list):
    #print("Sorting the list.... \n {} \n Size of: {} \nEnd of list.\n".format(r_list, len(r_list)))
    if len(r_list) <= 1:
        return r_list

    mid = int(len(r_list)/2)

    left = sort_merge(r_list[:mid])
    right = sort_merge(r_list[mid:])

    return merge(left,right)
        
def groupby_sum(R, RS):

    r_list = []
    for l in R:
        r_list.append(fix_line(l))
    
    #print(r_list)
    #print(len(r_list))

    r_list = sort_merge(r_list)
    
    for r in r_list:
        RS.write("{key}\t{value}\n".format(key = r[0], value= r[1]))

def main():
    with open('R.tsv', 'r') as R, open('Rgroupby.tsv', 'w') as RS:  
        groupby_sum(R, RS)

main()