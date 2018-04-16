from logger import Logger

__logger = Logger()

def unify_to_months(raw_value):
    if raw_value.startswith('>'):
        raw_range = raw_value.split(' ')[1]
        unit = raw_value.split(' ')[2]
        range_from = int(raw_range.split('>')[0])
        range_to = 100
        pass
    else:
        raw_range = raw_value.split(' ')[0]
        unit = raw_value.split(' ')[1]
        range_from = int(raw_range.split('–')[0])  # It is not a pause char!
        range_to = int(raw_range.split('–')[1])  # It is not a pause char!

    if unit == 'y':
        range_from = range_from * 12
        range_to = range_to * 12 + 11

    __logger.debug("Unifying range to months. Result: from={}, to={}", range_from, range_to)
    return range_from, range_to
