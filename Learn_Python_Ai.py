revenue = 50
expenses = 10
print(type(revenue))

profit = revenue - expenses
print(profit)
print(type(profit))

margin = (profit/revenue)*100
print(margin)
print(type(margin))
print(id(margin))

expenses = "I'd love the food"
print(type(expenses))

expense_description = ''' There is a new car.
It is blue in color.
 '''

len(expense_description)
print(type(expense_description))


#last 
revenue = [50, 60, 70, 100]
expenses = [20, 30, 50, 23]
print(type(revenue))
print(revenue[0])
print(revenue[-1])
print(revenue[1:3])
print(len(revenue))


for rev in revenue:
    print("Revenues", rev)


# Loop through all the indexes of the revenue list (0, 1, 2, 3, ...)
# range(len(revenue)) generates the index numbers, and i stores one index at a time.
for i in range(len(revenue)):  # Len(revenue) stores the length of the revenue string which is 4 
    
    # Print the current index.
    print(i) 

    # Access and print the revenue value at the current index.
    # Here, i is NOT the value—it is only the index.
    print(revenue[i])

    # Calculate the profit for the current index by subtracting
    # the expense at the same index from the revenue.
    # The same index (i) is used to access both lists.
    progit = revenue[i] - expenses[i]
    margin = profit * 100 / revenue[i]
    print(margin)

    # Dictionary - A dictionary in python stores data as key-value pairs
    data = {"name":"Hardik", "age":19, "marks":{"maths":90, "science":97}}  
    # Keys: name, age, marks
    # Values: Hardik, 19, 90
    print(data)
   # Adding a new key 
    data["city"] = "Jaipur"
    print(data)
   # Updating a value
    data["age"] = 21
   #Removing an Item
del data["marks"]["science"]
print(data)
    #Get - get() safely looks for a key. If the key doesn't exist, it returns None instead of giving an error
    
# looping in the dictionary
for key in data:
    print(key, data[key])   



    # Tuples in python
    # A tuple cannot be changed after it is created it is (immutable).
    person = (10.5,"Hardik",True,50)
    print(person)
    print(person[2])
    print(type(person))
    print(len(person))
    print(person.index(10.5))
    # looping in number
    for human in person:
        print(human)
    