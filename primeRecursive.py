#Recursive prime function
def is_prime(a,N):
    #print(a, N)
    if N <= 1:
        return 
    else:
        if a >= N:
            print(str(N) + " is the primest of primes, broski.")
            return True
        else:
            if N == 2: 
                print("Bro, " + str(N) + "is totally prime. It's the first prime number, my man.")
                return True
            elif (N % a) == 0:
                print(str(N) + " is not prime, dude. Tough.")
                return True
            else:
                return is_prime(a+1,N)

    print("Welp, " + str(N) + " is totally not prime. I'm sorry brodude.")
    return False

numberToCalc = input("Which number are you not sure is prime or not, just asking for a friend.  ")
response = is_prime(2,int(numberToCalc))

print(response)