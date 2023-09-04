# list[items, items] | separated by comma
mylist = ["Book", "Pen", "Erase"]
print(mylist)
count_item = len(mylist)  # len() function to count item on the list
print(count_item)

# get item on the list
data0 = mylist[0]
print(data0)
data1 = mylist[-1]
print(data1)

# change item on the list
mylist[0] = "Bag"
print(mylist)

# adding item on the list
mylist.append("Story Book")  # single item on the end
print(mylist)

mylist.extend(["Manggo", "Apple"])  # multiple item
print(mylist)

mylist.insert(1, "Pencil")  # insert(index, item). single item base on index
print(mylist)

# Delete items
mylist.remove("Pen")
print(mylist)
