
# Seung Hun Jang
# COMP140 - Code to implement the game of Spot it!
#
# This code creates a deck of playable Spot It cards,considering
# the equivalency and incidency between points(imgaes on card) and lines(cards).
#
# Actual game: http://www.blueorangegames.com/spotit/


def modmult(num1, num2, mod):
    """
    Performs modular multiplication of two input numbers and returns the result
    """
    return (num1 * num2) % mod


def modadd(num1, num2, mod):
    """
    Performs modular addition of two input numbers and returns the result
    """
    return (num1 + num2) % mod


def mymod(num1, mod):
    """
    Returns the remainder when the input number is divided by mod
    """
    return num1 % mod


def equivalent(trip1, trip2, mod):
    """
    Given two points, represented as tuples of 3 elements (trip1 and
    trip2), determine if they are equivalent under the given modulus
    (mod).
    """
    # perform cross product
    for idx in range(3):
        if mymod(modmult(trip1[mymod(idx + 1, 3)], trip2[mymod(idx + 2, 3)], mod) -
           modmult(trip1[mymod(idx + 2, 3)], trip2[mymod(idx + 1, 3)], mod), mod) != 0:
            return False
    return True


def incident(point, line, mod):
    """
    Given a point and a line, each represented as tuples of 3
    elements, determine if the point lies on that line under the given
    modulus (mod).
    """
    sum_all = 0
    for idx in range(3):
        sum_all = modadd(sum_all, modmult(point[idx], line[idx], mod), mod)
    return sum_all == 0


def generate_all_points(mod):
    """
    Generate all unique points for the given modulus (mod).  Returns a
    list of unique points, each represented as a tuple of 3 elements.
    """
    all_points = []

    # generate all possible points
    for idx1 in range(mod):
        for idx2 in range(mod):
            for idx3 in range(mod):
                all_points.append(tuple((idx1, idx2, idx3)))

    # get rid of (0,0,0)
    all_points.pop(0)

    # check for equivalence

    # create empty list, tobe_removed, to keep track of removable elements
    tobe_removed = []

    for point1 in all_points:
        for idx in range(all_points.index(point1) + 1, len(all_points)):
            if equivalent(point1, all_points[idx], mod):
                if all_points[idx] in all_points:
                    tobe_removed.append(all_points[idx])

    # create empty list, result, and append elements that are not in tobe_removed.
    result = []
    for idx in all_points:
        if (idx not in tobe_removed):
            result.append(idx)

    return result


def create_cards(points, lines, mod):
    """
    Return a list of cards given a list of points, list of lines, and
    a modulus (mod).  Each element of the returned list should be a
    list of integers.
    """
    list_of_cards_in_integers = []
    for line in lines:
        card = []
        for idx in range(len(points)):
            if incident(points[idx], line, mod):
                card.append(idx)
        list_of_cards_in_integers.append(card)

    return list_of_cards_in_integers


def run():
    """
    Create the deck and play the game.
    """
    # Prime modulus
    # Set to 2 or 3 during development
    # Set to 7 for the actual game
    modulus = 7

    # Generate all unique points for the given modulus
    points = generate_all_points(modulus)

    # Lines are the same as points, so make a copy
    lines = points[:]

    # Generate a deck of cards given the points and lines
    deck = create_cards(points, lines, modulus)

    print(deck)
    # Run GUI - uncomment the line below after you have implemented
    #           everything and you can play your game.  The GUI does
    #           not work if the modulus is larger than 7.

    # spotit.start(deck)


run()
