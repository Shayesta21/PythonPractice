# range(): to print values between a range

print (list(range(10)))

#it will always print no n-1 in the end
print (list(range(1,10)))

# print odd numbers 1-10
print (list(range(1,10,2))) #[1, 3, 5, 7, 9]

#print even numbers
print(list(range(0,10,2))) #[0, 2, 4, 6, 8]

#print numbers in descending order
print(list(range(10,1,-1)))#[10, 9, 8, 7, 6, 5, 4, 3, 2]

#print range of no between -10 and -5
print (list(range(-10,-5))) #[-10, -9, -8, -7, -6]

print(list(range(-10,-5,2))) #[-10, -8, -6]