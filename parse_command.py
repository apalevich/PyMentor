#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
Function designed to parse commands. It takes strings and return dict containing:

action - required action
instrument - required instrument
value - value for calculation
value2 - second value for calculation (optional)

Simple way to use the function:
>>> parse_command('add gazp 100')
{'action': 'add', 'instrument': 'gazp', 'value': 100}

You can add second value:
>>> parse_command('add gazp 100 150')
{'action': 'add', 'instrument': 'gazp', 'value': 100, 'value2': 150}

Values can be separated not only by spaces:
>>> parse_command('add gazp 100-150')
{'action': 'add', 'instrument': 'gazp', 'value': 100, 'value2': 150}

But beware giving no values:
>>> parse_command('add gazp')
Exception: 'Укажите значение цены'

Value should be a number:
>>> parse_command('add gazp asdf')
'Значение должно быть числом'

Both of values should be a numbers:
>>> parse_command('add gazp asdf 1')
'Значение должно быть числом'
"""

def parse_command(cmd:str) -> dict:
    cmd_list = cmd.split()
    cmd_dict = {}

    # make some warnings
    if len(cmd_list) < 3:
        raise Exception('Укажите значение цены')

    if cmd_list[0].isalpha():
        cmd_dict['action'] = cmd_list[0]
    else:
        raise Exception('Используйте действующую команду')

    if cmd_list[1].isalpha():
        cmd_dict['instrument'] = cmd_list[1]
    else:
        raise Exception('Используйте действующий инструмент')

    # parce values
    values = []
    if cmd_list[2].isdigit() and len(cmd_list) == 3:
        cmd_dict['value'] = int(cmd_list[2])
    else:
        separator = ' '
        for c in cmd_list[2]:
            if not c.isdigit():
                separator = c
        values = cmd_list[2].split(separator)
        cmd_dict['value'] = int(values[0])
        if len(values) > 1:
            cmd_dict['value2'] = int(values[1])

    for value in values:
        if not value.isdigit():
            raise Exception('Значение должно быть числом')

    return cmd_dict

if __name__ == '__main__':

    	import doctest
    	doctest.testmod()
