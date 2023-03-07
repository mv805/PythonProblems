# As an example, here is an implementation of
# the first problem "Ryerson Letter Grade":

# def ryerson_letter_grade(n):
#     if n < 50:
#         return 'F'
#     elif n > 89:
#         return 'A+'
#     elif n > 84:
#         return 'A'
#     elif n > 79:
#         return 'A-'
#     tens = n // 10
#     ones = n % 10
#     if ones < 3:
#         adjust = "-"
#     elif ones > 6:
#         adjust = "+"
#     else:
#         adjust = ""
#     return "DCB"[tens - 5] + adjust

# 1: Ryerson letter grade
def ryerson_letter_grade(pct):

    grades = [
        ('A+', 90, 150),
        ('A', 85, 89),
        ('A-', 80, 84),
        ('B+', 77, 79),
        ('B', 73, 76),
        ('B-', 70, 72),
        ('C+', 67, 69),
        ('C', 63, 66),
        ('C-', 60, 62),
        ('D+', 57, 59),
        ('D', 53, 56),
        ('D-', 50, 52),
        ('F', 0, 49),
    ]

    for grade, minPct, maxPct in grades:
        if pct >= minPct and pct <= maxPct:
            return grade

# 2: Ascending List


def is_ascending(items):

    if len(items) <= 1:
        return True

    for i, number in enumerate(items):
        if i == len(items) - 1:
            break
        elif items[i] < items[i+1]:
            continue
        else:
            return False

    return True

# 3: Riffle shuffle kerfuffle


def riffle(items, out=True):

    if len(items) < 2:
        return items

    half = int((len(items)/2))

    if out == True:
        front = items[:half]
        back = items[half:]
    else:
        front = items[half:]
        back = items[:half]

    riffled = []

    for index in range(half):
        riffled.append(front[index])
        riffled.append(back[index])

    return riffled

# 4: Even the odds


def only_odd_digits(n):
    while n != 0:
        if (n % 2 != 0):
            n = n // 10
        else:
            return False
    return True

# 5: Cyclops numbers


def is_cyclops(n):
    if n == 0:
        return True
    elif (int(len(str(n))) % 2 == 0):
        return False

    remainderLength = int(len(str(n))//2)

    while (int(len(str(n))) > remainderLength + 1):
        if (n % 10 == 0):
            return False
        else:
            n = n // 10

    if (n % 10 != 0):
        return False
    else:
        return True


print(is_cyclops(6754009820))
