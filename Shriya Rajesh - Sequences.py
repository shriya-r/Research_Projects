# Shriya Rajesh
# 9/1/2023

# Description:
# This program identifies the type of sequence for a list of numbers.

#input sequence and store as a list

series = []

series.append(int (input("Enter the first term of a sequence: ")))
series.append(int (input("Enter the second term of a sequence: ")))
series.append(int (input("Enter the third term of a sequence: ")))
series.append(int (input("Enter the fourth term of a sequence: ")))


#checking if sequence is prime numbers
prime = 0;
if (series[0] < series[1] < series[2] < series[3]) :
    i = 2
    while (i < series[0]):
        if ( series[0] % i != 0) :
            i = i+1
        else:
            i = series[0]+1
    if (i == series[0]) :
        i = 2
        while (i < series[1]) :
            if ( series[1] % i != 0) :
                i = i+1
            else :
                i = series[1]+1
        if (i == series[1]) :
            i = 2
            while (i < series[2]) :
                if ( series[2] % i != 0) :
                    i = i+1
                
                else :
                    i = series[2]+1
            
          
            if (i == series[2]) :
                i = 2
                while (i < series[3]) :
                    if ( series[3] % i != 0) :
                        i = i+1
               
                    else :
                        i = series[3]+1
              
            
                if (i == series[3]) :
                    n5 = series[3]+1
                    while (prime == 0) :
                        i = 2
                        while (i < n5) : #calculating next prime number
                            if ( n5 % i != 0) :
                                i = i+1
                         
                            else :
                                i = n5+1
                         
                       
                        if (n5 == i) :
                            prime = 1
                       
                        else :
                            n5 = n5+1
                      
                
                    print("These are prime numbers and the next number is: " , n5)

if (prime == 1) :
    prime = 1; # if statement ensures that 'please enter a different sequence' does not print
  


#checking if sequence is arithmetic
elif ((series[1] - series[0])  == (series[2] - series[1]) == (series[3] - series[2])):
    difference = series[1] - series[0]
    print("This is an arithmetic sequence. The next number is:", series[3] + difference)

#checking if sequence is geometric
elif ((series[1] / series[0])  == (series[2] / series[1]) == (series[3] / series[2])):
    ratio = series[1] / series[0]
    print("This is a geometric sequence. The next number is:", series[3] * ratio)

#checking if it is a specific letter sequence
elif (series == [1, 4, 7, 11]):
    print("These amount of letters in each number increases by one. The next number is:", 15)

#three letter numbers
elif (series == [1, 2, 6, 10]):
    print("These are three-letter numbers and there is no next number.")

#checking if it follows the pattern of a Fibonacci Sequence
elif (((series[1] + series[0])  == series[2]) and (series[3] == (series[1] + series[2]))):
    next_num = series[2] + series[3]
    print("This is the Fibonacci Sequence. The next number is:", next_num)

#response if the sequence is not identifiable
else:
    print("Please enter a different sequence.")


