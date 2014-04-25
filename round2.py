"""FizzBuzz.
Write a program that prints the integers from 1 to 100. But for multiples of
three print "fizz" instead of the number and for the multiples of five print
"buzz". For numbers which are multiples of both three and five print "fizzbuzz"
"""

input = xrange(99, 336)

output = [("fizzbuzz" if (x % 15==0) else ("fizz" if x % 3 == 0 else ("buzz" if x % 5 == 0 else str(x)))) for x in input]

expected = ['fizz', 'buzz', '101', 'fizz', '103', '104', 'fizzbuzz', '106', '107', 'fizz', '109', 'buzz', 'fizz', '112', '113', 'fizz', 'buzz', '116', 'fizz', '118', '119', 'fizzbuzz', '121', '122', 'fizz', '124', 'buzz', 'fizz', '127', '128', 'fizz', 'buzz', '131', 'fizz', '133', '134', 'fizzbuzz', '136', '137', 'fizz', '139', 'buzz', 'fizz', '142', '143', 'fizz', 'buzz', '146', 'fizz', '148', '149', 'fizzbuzz', '151', '152', 'fizz', '154', 'buzz', 'fizz', '157', '158', 'fizz', 'buzz', '161', 'fizz', '163', '164', 'fizzbuzz', '166', '167', 'fizz', '169', 'buzz', 'fizz', '172', '173', 'fizz', 'buzz', '176', 'fizz', '178', '179', 'fizzbuzz', '181', '182', 'fizz', '184', 'buzz', 'fizz', '187', '188', 'fizz', 'buzz', '191', 'fizz', '193', '194', 'fizzbuzz', '196', '197', 'fizz', '199', 'buzz', 'fizz', '202', '203', 'fizz', 'buzz', '206', 'fizz', '208', '209', 'fizzbuzz', '211', '212', 'fizz', '214', 'buzz', 'fizz', '217', '218', 'fizz', 'buzz', '221', 'fizz', '223', '224', 'fizzbuzz', '226', '227', 'fizz', '229', 'buzz', 'fizz', '232', '233', 'fizz', 'buzz', '236', 'fizz', '238', '239', 'fizzbuzz', '241', '242', 'fizz', '244', 'buzz', 'fizz', '247', '248', 'fizz', 'buzz', '251', 'fizz', '253', '254', 'fizzbuzz', '256', '257', 'fizz', '259', 'buzz', 'fizz', '262', '263', 'fizz', 'buzz', '266', 'fizz', '268', '269', 'fizzbuzz', '271', '272', 'fizz', '274', 'buzz', 'fizz', '277', '278', 'fizz', 'buzz', '281', 'fizz', '283', '284', 'fizzbuzz', '286', '287', 'fizz', '289', 'buzz', 'fizz', '292', '293', 'fizz', 'buzz', '296', 'fizz', '298', '299', 'fizzbuzz', '301', '302', 'fizz', '304', 'buzz', 'fizz', '307', '308', 'fizz', 'buzz', '311', 'fizz', '313', '314', 'fizzbuzz', '316', '317', 'fizz', '319', 'buzz', 'fizz', '322', '323', 'fizz', 'buzz', '326', 'fizz', '328', '329', 'fizzbuzz', '331', '332', 'fizz', '334', 'buzz']

assert(output == expected)
