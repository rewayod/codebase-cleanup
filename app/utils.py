


 

def to_usd(my_price):
    """
    This is a docstring. It tells us what this function is about.
    What its responsibilities ar.
    What the params are ab9out.
    What datatypes the params are.
    What this function will return.
    Example of invoking the function.

    Invoke like this: to_usd(9.9999)
    """
    return '${:,.2f}'.format(my_price)


def determine_winner(user_choice, computer_choice):

    """
    :param user_choice: rock/paper/scissors
    :param computer_choice: rock/paper/scissors
    :return: winner: user/computer based on both params
    """

    winners = {
        "rock": {
            "rock": None,
            "paper": "paper",
            "scissors": "rock",
        },
        "paper": {
            "rock": "paper",
            "paper": None,
            "scissors": "scissors",
        },
        "scissors": {
            "rock": "rock",
            "paper": "scissors",
            "scissors": None,
        }
    }
    winning_choice = winners[user_choice][computer_choice]
    return winning_choice



## if this code is in the global scope
## ... of a file we're trying to import from
## ... it will throw errors when we try to run those other files
#price = input("Please choose a price like 4.9999")
#
#print(to_usd(float(price)))


if __name__ == "__main__":

    # nesting code in the main condition will
    # allow other scripts to cleanly import functions from this file
    # without running this code

    # this code still gets run when we invoke the script from the command line
    price = input("Please choose a price like 4.9999")

    print(to_usd(float(price))) 
