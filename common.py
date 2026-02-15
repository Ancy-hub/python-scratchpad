def comm(lst1,lst2):
    comm_lst=[]
    for ele in lst1:
         if ele in lst2:
              comm_lst.append(ele)
    return comm_lst

lst1=[2,3,4,5,6,7]

lst2=[3,4,5,6,9,0]

print(comm(lst1,lst2))