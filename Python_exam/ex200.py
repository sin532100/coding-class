ohlc = [["open", "high", "low", "close"],
        [100, 110, 70, 100],
        [200, 210, 180, 190],
        [300, 310, 300, 310]]

a = 0

for i in range(1, 4):
    a += ohlc[i][0] - ohlc[i][3]

print(a)