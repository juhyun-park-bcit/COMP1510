# a, b
the_number = int(input("What number would like you to change? "))
destination_base = int(input("destination base? "))

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