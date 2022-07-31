root = convert_block = lambda x: int(x) if x != "null" else None
raw_array = list(map(convert_block, input().split(' ')))