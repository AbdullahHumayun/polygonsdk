def find_gaps(o, h, l, c, t):
    gap_ups = []
    gap_downs = []

    for i in range(1, len(o)):
        if o[i] > c[i-1]:  # Check if the opening price is greater than the previous high price
            gap_ups.append(i)
        elif o[i] < c[i-1]:  # Check if the opening price is less than the previous low price
            gap_downs.append(i)

    gap_ups_with_timestamps = [(t[i], i) for i in gap_ups]
    gap_downs_with_timestamps = [(t[i], i) for i in gap_downs]

    return gap_ups_with_timestamps, gap_downs_with_timestamps


def find_gap_price_range(o, h, l, c, t, candle, filled=None):
    if o[candle] > h[candle - 1]:
        direction = "up"
        gap_low = l[candle - 1]
        gap_high = h[candle]
    elif o[candle] < l[candle - 1]:
        direction = "down"
        gap_low = l[candle]
        gap_high = h[candle - 1]
    else:
        direction = "unknown"
        gap_low = None
        gap_high = None

    if filled is None:
        return gap_low, gap_high
    else:
        fill_index = None
        for i in range(candle + 1, len(c)):
            if direction == "up":
                if l[i] <= gap_high and h[i] >= gap_low:
                    fill_index = i
                    break
            elif direction == "down":
                if h[i] >= gap_high and l[i] <= gap_low:
                    fill_index = i
                    break

        if filled is True:
            if fill_index is not None:
                return t[fill_index]
            else:
                return None
        else:
            if fill_index is not None:
                return t[fill_index]
            else:
                return None