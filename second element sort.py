#sorting list using second item

def second(item):
    return item[1]

lst=[[1,2],[2,3],[6,1]]
sorted= sorted(lst, key=second)
print(sorted)