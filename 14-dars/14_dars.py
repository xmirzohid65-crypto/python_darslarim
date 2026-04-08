# import funksiya
#
# avto1 = funksiya.avto_info('GM', 'tracker', 'darkmoon', 'avtomat', 2024, 30000)
# funksiya.info_print(avto1)

# import funksiya as fun
#
# avto1 = fun.avto_info('GM', 'jentra', 'Qora', 'avtomat', 2022, 13300)
# fun.info_print(avto1)

# from funksiya import avto_info, info_print
#
# avto1 = avto_info('GM', 'cobalt', 'oq', 'mexanik', 2024, 12000)
# info_print(avto1)

# from funksiya import avto_info as ai, info_print as ip
#
# avto1 = ai('GM', 'Malibu', 'Qora', 'avtomat', 2020, 40000)
# ip(avto1)

from funksiya import *

avto1 = avto_info('GM', 'cobalt', 'oq', 'mexanik', 2024, 12000)
info_print(avto1)