seconds = int(input("Введіть кількість секунд від 1 до 8640000: "))

SECONDS_IN_DAY = 86400
SECONDS_IN_HOUR = 3600
SECONDS_IN_MINUTE = 60

days, remainder = divmod(seconds, SECONDS_IN_DAY)
hours, remainder = divmod(remainder, SECONDS_IN_HOUR)
minutes, seconds = divmod(remainder, SECONDS_IN_MINUTE)

if 11 <= days % 100 <= 14:
    day_word = "днів"
elif days % 10 == 1:
    day_word = "день"
elif 2 <= days % 10 <= 4:
    day_word = "дні"
else:
    day_word = "днів"

print(f"{days} {day_word}, {str(hours).zfill(2)}:{str(minutes).zfill(2)}:{str(seconds).zfill(2)}")
