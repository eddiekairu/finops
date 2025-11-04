print("Hello, world!")
print(1+2)
print(9-5)
print(3*4)
print(8/2)
print(3**2)
print(((1+3)*(9-2)/2)**2)
#Multiply 3 by 2
print(3*2)
#Create a variable called test_var and give it a value of 4+5
test_var=4+5
#print the value of test_var
print(test_var)
#set the value of a new variable to 3
my_var=3
#print the value assigned to new_var
print(my_var)
#change value of the variable to 100
my_var=100
print(my_var)
print(my_var)
print(test_var)
#increase the value by 3
my_var=my_var+3
print(my_var)
#create variables
number_of_years=4
days_per_year=365
hours_per_day=24
mins_per_hour=60
secs_per_min=60
#calculate number of seconds in four years
Total_secs=secs_per_min*mins_per_hour*hours_per_day*days_per_year*number_of_years
print(Total_secs)
#update to include a leap year
days_per_year=365.25
Total_secs=secs_per_min*mins_per_hour*hours_per_day*days_per_year*number_of_years
print(Total_secs)
print(hours_per_day)
print(hours_per_day)
#geeting help and functions
help(round)
help(print)
help(abs)
round(3.7564)
print(round(3.7564))
print(abs(-56))
print("meaning:", help)
def least_difference(a, b, c):
    diff1 = abs(a - b)
    diff2 = abs(b - c)
    diff3 = abs(a - c)
    return min(diff1, diff2, diff3)
help(least_difference)