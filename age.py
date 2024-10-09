def within_range(num: int, min: int, max: int) -> bool:
    return (min < num and num <= max)


def give_message(number: int) -> None:
    state: str = ""
    if 0 < number and number <= 99:
        if number < 25:
            state = "Young"
        elif number < 50:
            state = "Adult"
        elif number < 75:
            state = "Elderly"
        elif number <= 99:
            state = "Ghost"

    match state:
        case "Young":
            print("Lucky SZJA")
        case "Adult":
            print("♥")
        case "Elderly":
            print("Legend")
        case "Ghost":
            print("Fart")
        case _:
            pass


while (True):
    answer: str = input("How old are you?")

    # 1. Check if valid number
    try:
        number = int(answer)
    except ValueError as err:
        print("Give valid  umber")
        continue
    # Check if input is between 0 and 99
    valid: bool = within_range(number, 0, 99)
    if not valid:
        print("You gave a wrong number (0 - 99)")
        continue
    give_message(number)
    break
