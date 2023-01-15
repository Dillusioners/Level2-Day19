#Program to shorten any number and encrypt it

def display():
    print("#"*30)
    print("Welcome to the number shortener ")
    print("#"*30)

def main():
    display()
    sum1 = 0
    try:
        num = int(input(">> Enter a number number : "))
    except Exception as e:
        print("OOPs\n",e)
        exit()
    for nums in str(num):
        sum1 += int(nums)

    num_sum_str = str(num) + str(sum1)

    odd = ""
    even = ""
    
    for i in range(1, len(num_sum_str)):
        if i % 2 == 0:
            even += num_sum_str[i - 1]
        else:
            odd += num_sum_str[i - 1]
    
    odd_odd = ""
    even_odd = ""

    for i in range(1, len(odd)):
        if i % 2 == 0:
            even_odd += odd[i - 1]
        else:
            odd_odd += odd[i - 1]
    
    odd_even = ""
    even_even = ""

    for i in range(1, len(even)):
        if i % 2 == 0:
            even_even += even[i - 1]
        else:
            odd_even += even[i - 1]

    main = odd_odd[::-1] + odd_even[::-1] + even_odd[::-1] + even_even[::-1]

    alphabets = ""
    i = 0
    while i <= len(main) - 1:
        try:
            ascii = (int(main[i]) * 10) + int(main[i + 1])
            if ascii >= 48 and ascii <= 57:
                digit = chr(ascii)
                alphabets += str(digit)
                i+=2
            elif ascii >= 65 and ascii <= 90:
                digit = chr(ascii)
                alphabets += str(digit)
                i+=2
            elif ascii >= 97 and ascii <= 122:
                digit = chr(ascii)
                alphabets += str(digit)
                i+=2
            else:
                alphabets += str(ascii)
                i+=2
        except:
            break

    print("New encrypyted and shortened form is : ",alphabets)

main()
