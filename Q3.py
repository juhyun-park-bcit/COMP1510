# a, b
destination_base = int(input("Please type number[2,9]\ndestination base? "))
the_maximum_number = destination_base**4 - 1
print(f"the maximum base 10 number that fits in 4 base {destination_base} digits is {the_maximum_number}.\nA base 10 number must be equal to or less than {the_maximum_number}")
the_number = int(input("What number would like you to change? "))

# c, d, e ,f, g, h, i, j, k
first_quotient = the_number // destination_base
first_remainder = the_number % destination_base

second_quotient = first_quotient // destination_base
second_remainder = first_quotient % destination_base

third_quotient = second_quotient // destination_base
third_remainder = second_quotient % destination_base

fourth_remainder = third_quotient % destination_base

converted_number = str(fourth_remainder) + str(third_remainder) + str(second_remainder) + str(first_remainder)

print(converted_number)