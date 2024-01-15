#!/usr/bin/python3
''' UTF-8 encodin '''
NUMBER_OF_BITS_PER_BLOCK = 8
MAX_NUMBER_OF_ONES = 4

def validUTF8(data):
    ''' Validate utf-8 encodin '''
    data = iter(data)
    for leading_byte in data:
        leading_ones = count_leading_bits(leading_byte)
        if leading_ones in [1, 7, 8]:
            return False        # Illegal leading byte
        for _ in range(leading_ones - 1):
            trailing_byte = next(data, None)
            if trailing_byte is None or trailing_byte >> 6 != 0b10:
                return False    # Missing or illegal trailing byte
    return True

   
    
def count_leading_bits(byte):
    '''count the number of leading set bits in a byte'''
    for i in range(8):
        if byte >> (7 - i) == 0b11111111 >> (7 - i) & ~1:
            return i
    return 8   