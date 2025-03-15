#Fernando Guzman
#03/15/25

##Function that initializes counter and if divisible by 10 appends it to list

counter = 0

tens = []

while counter <=50:
    counter +=1
    if counter % 10 == 0:
        tens.append(counter)
        
print(tens)
