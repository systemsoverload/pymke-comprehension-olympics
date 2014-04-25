"""Reverse and add
Given a list of numbers, reverse and add the reverse to the original number.

Ex.
42 + 24 = 66
15 + 51 = 66
"""

input = xrange(1, 999)

output = [x + int(str(x)[::-1]) for x in input]

expected = [2, 4, 6, 8, 10, 12, 14, 16, 18, 11, 22, 33, 44, 55, 66, 77, 88, 99, 110, 22, 33, 44, 55, 66, 77, 88, 99, 110, 121, 33, 44, 55, 66, 77, 88, 99, 110, 121, 132, 44, 55, 66, 77, 88, 99, 110, 121, 132, 143, 55, 66, 77, 88, 99, 110, 121, 132, 143, 154, 66, 77, 88, 99, 110, 121, 132, 143, 154, 165, 77, 88, 99, 110, 121, 132, 143, 154, 165, 176, 88, 99, 110, 121, 132, 143, 154, 165, 176, 187, 99, 110, 121, 132, 143, 154, 165, 176, 187, 198, 101, 202, 303, 404, 505, 606, 707, 808, 909, 1010, 121, 222, 323, 424, 525, 626, 727, 828, 929, 1030, 141, 242, 343, 444, 545, 646, 747, 848, 949, 1050, 161, 262, 363, 464, 565, 666, 767, 868, 969, 1070, 181, 282, 383, 484, 585, 686, 787, 888, 989, 1090, 201, 302, 403, 504, 605, 706, 807, 908, 1009, 1110, 221, 322, 423, 524, 625, 726, 827, 928, 1029, 1130, 241, 342, 443, 544, 645, 746, 847, 948, 1049, 1150, 261, 362, 463, 564, 665, 766, 867, 968, 1069, 1170, 281, 382, 483, 584, 685, 786, 887, 988, 1089, 1190, 202, 303, 404, 505, 606, 707, 808, 909, 1010, 1111, 222, 323, 424, 525, 626, 727, 828, 929, 1030, 1131, 242, 343, 444, 545, 646, 747, 848, 949, 1050, 1151, 262, 363, 464, 565, 666, 767, 868, 969, 1070, 1171, 282, 383, 484, 585, 686, 787, 888, 989, 1090, 1191, 302, 403, 504, 605, 706, 807, 908, 1009, 1110, 1211, 322, 423, 524, 625, 726, 827, 928, 1029, 1130, 1231, 342, 443, 544, 645, 746, 847, 948, 1049, 1150, 1251, 362, 463, 564, 665, 766, 867, 968, 1069, 1170, 1271, 382, 483, 584, 685, 786, 887, 988, 1089, 1190, 1291, 303, 404, 505, 606, 707, 808, 909, 1010, 1111, 1212, 323, 424, 525, 626, 727, 828, 929, 1030, 1131, 1232, 343, 444, 545, 646, 747, 848, 949, 1050, 1151, 1252, 363, 464, 565, 666, 767, 868, 969, 1070, 1171, 1272, 383, 484, 585, 686, 787, 888, 989, 1090, 1191, 1292, 403, 504, 605, 706, 807, 908, 1009, 1110, 1211, 1312, 423, 524, 625, 726, 827, 928, 1029, 1130, 1231, 1332, 443, 544, 645, 746, 847, 948, 1049, 1150, 1251, 1352, 463, 564, 665, 766, 867, 968, 1069, 1170, 1271, 1372, 483, 584, 685, 786, 887, 988, 1089, 1190, 1291, 1392, 404, 505, 606, 707, 808, 909, 1010, 1111, 1212, 1313, 424, 525, 626, 727, 828, 929, 1030, 1131, 1232, 1333, 444, 545, 646, 747, 848, 949, 1050, 1151, 1252, 1353, 464, 565, 666, 767, 868, 969, 1070, 1171, 1272, 1373, 484, 585, 686, 787, 888, 989, 1090, 1191, 1292, 1393, 504, 605, 706, 807, 908, 1009, 1110, 1211, 1312, 1413, 524, 625, 726, 827, 928, 1029, 1130, 1231, 1332, 1433, 544, 645, 746, 847, 948, 1049, 1150, 1251, 1352, 1453, 564, 665, 766, 867, 968, 1069, 1170, 1271, 1372, 1473, 584, 685, 786, 887, 988, 1089, 1190, 1291, 1392, 1493, 505, 606, 707, 808, 909, 1010, 1111, 1212, 1313, 1414, 525, 626, 727, 828, 929, 1030, 1131, 1232, 1333, 1434, 545, 646, 747, 848, 949, 1050, 1151, 1252, 1353, 1454, 565, 666, 767, 868, 969, 1070, 1171, 1272, 1373, 1474, 585, 686, 787, 888, 989, 1090, 1191, 1292, 1393, 1494, 605, 706, 807, 908, 1009, 1110, 1211, 1312, 1413, 1514, 625, 726, 827, 928, 1029, 1130, 1231, 1332, 1433, 1534, 645, 746, 847, 948, 1049, 1150, 1251, 1352, 1453, 1554, 665, 766, 867, 968, 1069, 1170, 1271, 1372, 1473, 1574, 685, 786, 887, 988, 1089, 1190, 1291, 1392, 1493, 1594, 606, 707, 808, 909, 1010, 1111, 1212, 1313, 1414, 1515, 626, 727, 828, 929, 1030, 1131, 1232, 1333, 1434, 1535, 646, 747, 848, 949, 1050, 1151, 1252, 1353, 1454, 1555, 666, 767, 868, 969, 1070, 1171, 1272, 1373, 1474, 1575, 686, 787, 888, 989, 1090, 1191, 1292, 1393, 1494, 1595, 706, 807, 908, 1009, 1110, 1211, 1312, 1413, 1514, 1615, 726, 827, 928, 1029, 1130, 1231, 1332, 1433, 1534, 1635, 746, 847, 948, 1049, 1150, 1251, 1352, 1453, 1554, 1655, 766, 867, 968, 1069, 1170, 1271, 1372, 1473, 1574, 1675, 786, 887, 988, 1089, 1190, 1291, 1392, 1493, 1594, 1695, 707, 808, 909, 1010, 1111, 1212, 1313, 1414, 1515, 1616, 727, 828, 929, 1030, 1131, 1232, 1333, 1434, 1535, 1636, 747, 848, 949, 1050, 1151, 1252, 1353, 1454, 1555, 1656, 767, 868, 969, 1070, 1171, 1272, 1373, 1474, 1575, 1676, 787, 888, 989, 1090, 1191, 1292, 1393, 1494, 1595, 1696, 807, 908, 1009, 1110, 1211, 1312, 1413, 1514, 1615, 1716, 827, 928, 1029, 1130, 1231, 1332, 1433, 1534, 1635, 1736, 847, 948, 1049, 1150, 1251, 1352, 1453, 1554, 1655, 1756, 867, 968, 1069, 1170, 1271, 1372, 1473, 1574, 1675, 1776, 887, 988, 1089, 1190, 1291, 1392, 1493, 1594, 1695, 1796, 808, 909, 1010, 1111, 1212, 1313, 1414, 1515, 1616, 1717, 828, 929, 1030, 1131, 1232, 1333, 1434, 1535, 1636, 1737, 848, 949, 1050, 1151, 1252, 1353, 1454, 1555, 1656, 1757, 868, 969, 1070, 1171, 1272, 1373, 1474, 1575, 1676, 1777, 888, 989, 1090, 1191, 1292, 1393, 1494, 1595, 1696, 1797, 908, 1009, 1110, 1211, 1312, 1413, 1514, 1615, 1716, 1817, 928, 1029, 1130, 1231, 1332, 1433, 1534, 1635, 1736, 1837, 948, 1049, 1150, 1251, 1352, 1453, 1554, 1655, 1756, 1857, 968, 1069, 1170, 1271, 1372, 1473, 1574, 1675, 1776, 1877, 988, 1089, 1190, 1291, 1392, 1493, 1594, 1695, 1796, 1897, 909, 1010, 1111, 1212, 1313, 1414, 1515, 1616, 1717, 1818, 929, 1030, 1131, 1232, 1333, 1434, 1535, 1636, 1737, 1838, 949, 1050, 1151, 1252, 1353, 1454, 1555, 1656, 1757, 1858, 969, 1070, 1171, 1272, 1373, 1474, 1575, 1676, 1777, 1878, 989, 1090, 1191, 1292, 1393, 1494, 1595, 1696, 1797, 1898, 1009, 1110, 1211, 1312, 1413, 1514, 1615, 1716, 1817, 1918, 1029, 1130, 1231, 1332, 1433, 1534, 1635, 1736, 1837, 1938, 1049, 1150, 1251, 1352, 1453, 1554, 1655, 1756, 1857, 1958, 1069, 1170, 1271, 1372, 1473, 1574, 1675, 1776, 1877, 1978, 1089, 1190, 1291, 1392, 1493, 1594, 1695, 1796, 1897]

assert(output == expected)
