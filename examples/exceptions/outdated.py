months = {
    "January": 1,
    "February": 2,
    "March": 3,
    "April": 4,
    "May": 5,
    "June": 6,
    "July": 7,
    "August": 8,
    "September": 9,
    "October": 10,
    "November": 11,
    "December": 12,
}


def check(m, d):
    if not 1 <= m <= 12 or not 1 <= d <= 31:
        return False
    return True


def convertMonth(m):
    return months[m]


def main():

    while True:
        try:
            date = input("Date: ")
            if "/" in date:
                m, d, y = date.split("/")
            else:
                date = date.title()
                m, d, y = date.split()
                if not d.endswith(",") or d.count(",") != 1:
                    raise ValueError
                d = d.rstrip(",")
                m = convertMonth(m)
            d = int(d)
            m = int(m)
            y = int(y)
            if not check(m, d):
                raise ValueError
            break
        except (ValueError, KeyError):
            pass

    print(f"{y:04}-{m:02}-{d:02}")


main()
