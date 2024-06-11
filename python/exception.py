# Handling multiple exceptions
# The try...except allows you to handle multiple exceptions by specifying multiple except clauses:
try:
    # get input net sales
    print("Enter the net sales for")

    previous = float(input("- Prior period:"))
    current = float(input("- Current period:"))

    # calculate the change in percentage
    change = (current - previous) * 100 / previous

    # show the result
    if change > 0:
        result = f"Sales increase {abs(change)}%"
    else:
        result = f"Sales decrease {abs(change)}%"

    print(result)
except ValueError:
    print("Error! Please enter a number for net sales.")
except ZeroDivisionError:
    print("Error! The prior net sales cannot be zero.")

# try…except…finally
a = 10
b = 0

try:
    c = a / b
    print(c)
except ZeroDivisionError as error:
    print(error)
finally:
    print("Finishing up.")

# try…except…else
fruits = {"apple": 10, "orange": 20, "banana": 30}

key = None
while True:
    try:
        key = input("Enter a key to lookup:")
        fruit = fruits[key.lower()]
    except KeyError:
        print(f"Error! {key} does not exist.")
    except KeyboardInterrupt:
        break
    else:
        print(fruit)
    finally:
        print("Press Ctrl-C to exit.")

# raise
try:
    raise ValueError("The value error exception", "x", "y")
except ValueError as ex:
    print(ex.args)


def division(a, b):
    try:
        return a / b
    except ZeroDivisionError as ex:
        print("Logging exception:", str(ex))
        raise


def division(a, b):
    try:
        return a / b
    except ZeroDivisionError as ex:
        raise ValueError("b must not zero")


division(1, 0)
