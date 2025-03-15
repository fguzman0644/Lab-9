#Fernando Guzman
#03/15/25

##Function asks user to enter number and appends the number to a list
##and adds them until it reaches higher than 100

my_list = []

list_sum = 0

while list_sum <= 100:
    user_input = int(input("Please enter a number: "))
    my_list.append(user_input)
    list_sum = sum(my_list)

print("The numbers you have entered are ", my_list)

print("The total sum is ", list_sum)
