''' 
    

    Writing python function to give the frequcney of digits appearing after the decimal places


'''


def freqofDecimalPoints(dividend, divisor, lenth):

    number = dividend / divisor  # Initialise number and dividing parameters

    if(number % 2 == 1):

        # Saperating Decimal point value number = 3.1428571428 (3.0, 0.1428571428)

        number = number % 1

        C = 10 ** lenth  # storing 10^lenth for make number Interger point

        number = int(number*C)  # convert number into interger form

    else:

        number = int(number)

    Dict = {}  # Initialise dictionary to track digits

    print("\nNumber: ", number, "\n")

    for i in range(0, 10):
        frequency_counter = 0

        # Store value into Temporary variable
        temp = number

        while temp > 0:  # loop untill `temp` became Zero

            # getting the last digit

            '''

                digit = 12345 % 10 = 5, [By Iteration] - digit = 4, digit = 3, digit = 2, digit = 1

            '''

            digit = temp % 10

            if digit == i:  # if `digit` is equal to `i`, Increasing `count`
                frequency_counter = frequency_counter + 1

            temp = temp // 10  # if dosen't not initialize value for the corresponding key
        if frequency_counter >= 0:

            # print(i, ":", count, "\n")

            Dict[i] = frequency_counter

    print(Dict)


# Taking input for Divident, Divisor, Digits to show as {lenth}
Dividend = int(input("Enter Dividend: "))

Divisor = int(input("Enter Divisor: "))

lenth = int(input("Enter Lenth: "))


# Calling function freqofDecimalPoints()

freqofDecimalPoints(Dividend, Divisor, lenth)
# freqofDecimalPoints(dividend=int(input("Enter Dividend: ")), divisor=int(input("Enter Divisor: ")), lenth=int(input("Enter Lenth: ")))
