'''
bytes.py - Byte conversion module for Sopel
Copyright © 2015, Richard Petrie, <rap1011@ksu.edu>
Licensed under The MIT License
'''
from sopel.module import commands, example

ORDER_BYTES = ['B', 'KB', 'MB', 'GB', 'TB', 'PB', 'EB', 'ZB', 'YB']


@commands('bytes')
@example('2048', '2048 B = 2 KB')
@example('160 KB', '163840 B = 160 KB = 0.156 MB')
@example('160 Kb', '20480 B = 20 KB')
def do_bytes(bot, trigger):
    inp = trigger.group(2).split()
    number = inp[0]
    unit = None
    if len(inp) > 1:
        unit = inp[1]
    response = convert_bytes(bot, number, unit)
    new_response = ''
    for elem in response:
        if elem[0:3] != '0.0':
            new_response += elem + ' = '
    new_response = new_response.replace(".0", "")[:-2]
    bot.say(new_response)


def convert_bytes(bot, number, unit):
    if not unit:
        unit = "B"
    response = []
    num_bytes = int(number)
    if unit in ORDER_BYTES or unit.upper() in ORDER_BYTES:
        if 'b' in unit:
            if num_bytes % 8 != 0:
                bot.reply('Invalid number of bits')
                exit()
            else:
                num_bytes /= 8
                unit = unit.upper()
        sent_type = ORDER_BYTES.index(unit)
        num_bytes *= (1024 ** sent_type)
    else:
        bot.reply('Unknown type')
        exit()
    for size in ORDER_BYTES:
        response.append(str(round(num_bytes / (1024 ** ORDER_BYTES.index(size)), 3)) + " " + size)
    return response
