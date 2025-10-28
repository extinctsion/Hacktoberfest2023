def main():
    fraction = input("Fraction: ")
    percentage = convert(fraction)  # get the result from convert
    print(gauge(percentage))


def convert(fraction):
    while True:
        try:
            x, y = fraction.split("/")   # split string into two parts
            x = int(x)                   # convert numerator to int
            y = int(y)                   # convert denominator to int

            if x < 0 or y < 0 or x > y:
                raise ValueError
            result = x / y
            return result                # return instead of break
        except ValueError:
            fraction = input("Fraction: ")  # ask again if invalid
        except ZeroDivisionError:
            fraction = input("Fraction: ")  # ask again if denominator is 0


def gauge(percentage):
    if percentage >= 0.99:
        return "F"
    elif percentage <= 0.01:
        return "E"
    else:
        percent = round(percentage * 100)
        return f"{percent}%"


if __name__ == "__main__":
    main()
