def celsius_to_fahrenheit(c):
    return ((c + 40) * 1.8) - 40


daily_temp_c = [20.5, 19, 15, 25, 27, 30, 31, 29, 26, 21,
                19, 25, 27.5, 28, 26, 29.5, 31, 27.5, 26, 29,
                18, 17.5, 17, 16.5, 19, 20, 25, 26.5, 27, 28,
                20.5, 19, 25, 27.5, 28, 26, 15, 25, 27, 28]

daily_temp_f = list(map(lambda f: celsius_to_fahrenheit(f), daily_temp_c))
# print(daily_temp_f)

temp_above_80 = list(filter(lambda h: h > 80, daily_temp_f))

print(len(temp_above_80))