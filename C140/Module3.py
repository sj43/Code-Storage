import random

# this function fills the value dictionaries.


def inner_dict(result, key, latest_status):
    if latest_status in result[key]:
        result[key][latest_status] += 1
    else:
        result[key][latest_status] = 1
    return result


# this function creates markov chain dictionary,
# and fills the value dictionaries with function 'dictionaryAtTheEnd'
def markov_chain(data, order):
    """
    Create a Markov chain with the given order from the
    given list of data.
    """
    # create an empty map called result
    # iterate for (length of data - order) number of times:
    #   create a tuple called temp_slice and assign order number of previous states from data.
    #   (starting from the state succeeding previous iteration's starting state)
    #   this will be used as the key in our map result.
    #   if temp_slice is not a key in result, then assign an empty map to the value of temp_slice.
    #   result <-- inner_dict function (with inputs as: result, temp_slice, succeeding state in data)
    #   (inner_dict is a helper function that helps increment the number of corresponding state outcome within the inner value map)
    # as of now, the values in result are maps inwhich each key-value pair shows the number of different state outcomes resulted from our given data
    # for Markov chain, we want probabilities for each possible state outcomes.
    # So, lets change the actual number of outcomes for each state to probabilities.
    # we will make an iteration within iteration
    # outer iteration's elements will consist of key-value pairs for result
    #   let value_sum be the sum of number of outcomes for each succeeding state
    #   inner iteration's elements will consist of another key-value pairs for each value within result
    #       we will replace the inner map's values (which were the number of outcomes for each succeeding state) with probabilites by dividing each of them by value_sum
    # return result

    result = {}
    for idx in range(len(data) - order):
        temp_slice = tuple(data[idx:idx + order])
        if temp_slice not in result:
            result[temp_slice] = {}
        result = inner_dict(result, temp_slice, data[idx + order])

    for key, value in result.items():
        value_sum = sum(value.values())
        for key2 in value.keys():
            result[key][key2] /= float(value_sum)

    return result


# # testing
# testcase1 = ['C', 'C', 'S', 'T', 'S', 'T', 'C', 'S', 'S', 'T', 'C',
#              'S', 'C', 'C', 'T', 'S', 'T', 'S', 'S', 'C', 'T']
# testresult1 = markov_chain(testcase1, 1)


# Predict

def weighted_random_choice(diction):
    rnum = random.random()
    cumprob = 0.0
    for key, value in diction.items():
        cumprob += value
        if rnum < cumprob:
            return key
    print("shouldn't reach here at all")
    return None


def predict(model, last, num):
    """
    Predict the next num values given the model and the last values.
    """
    pred = []
    for dummy_n in range(num):
        last_tuple = tuple(last)
        if last_tuple in model:
            last_state = weighted_random_choice(model[last_tuple])
        else:
            last_state = random.choice([0, 1, 2, 3])
        pred.append(last_state)
        if len(last) > 1:
            last = last[1:]
            last.append(last_state)
        else:
            last = [last_state]

    return pred


# print(predict({(0,): {1: 1}, (1,): {0: 1}}, [0], 3))
# print(predict({(0, 1): {1: 1}, (1, 0): {2: 1}, (0, 0): {1: 1}, (1, 1): {3: 1}}, [0, 0], 3))
# print(predict({(0,): {1: 1}, (1,): {0: 1}}, [0], 3)) # expected [1, 0, 1] but received [1, 2, 3]
# print(predict({(0,): {1: 1}, (1,): {0: 1}}, [0], 3)) # expected [1, 0, 1] but received [1, 0, 0]


# Error


def mse(result, expected):
    """
    Calculate the mean squared error between the sequences
    result and expected.
    """
    mse_sum = 0.0
    len_res = len(result)
    for idx in range(len_res):
        mse_sum += (result[idx] - expected[idx])**2
    return mse_sum / len_res


# print(mse([1, 1, 1], [1, 1, 2]))

# Experiment


def run_experiment(train, order, test, future, actual, trials):
    """
    Run an experiment to predict the future of the test
    data given the training data.  Returns the average
    mean squared error over the number of trials.

    train  - training data
    order  - order of the markov model to use
    test   - "order" days of testing data
    future - number of days to predict
    actual - actual results for next "future" days
    trials - number of trials to run
    """
    sum_of_mse = 0.0
    for dummy_trials in range(trials):
        predicted_data = predict(markov_chain(train, order), test, future)
        sum_of_mse += mse(predicted_data, actual)

    return sum_of_mse / trials


# Application

def run():
    # Get the supported stock symbols
    symbols = ('FSLR', 'GOOG', 'DJIA')

    bins = {'DJIA': [2, 2, 1, 1, 1, 2, 2, 1, 2, 2, 1, 1, 2, 2, 1, 2, 2, 0, 2, 3, 2, 2, 2, 2, 2, 2, 1, 2, 1, 1, 2, 2, 2, 0, 1, 1, 2, 2, 0, 2, 3, 1, 1, 3, 1, 0, 2, 1, 0, 0, 3, 2, 3, 1, 2, 2, 2, 1, 2, 2, 1, 2, 2, 1, 2, 1, 1, 2, 1, 2, 2, 2, 0, 2, 3, 2, 1, 2, 2, 2, 2, 1, 2, 1, 0, 2, 2, 2, 0, 2, 1, 1, 1, 2, 2, 1, 0, 1, 2, 2, 2, 3, 0, 1, 1, 1, 1, 1, 2, 0, 2, 3, 0, 2, 2, 2, 2, 1, 1, 1, 2, 3, 2, 3, 3, 1, 2, 2, 1, 0, 1, 2, 1, 2, 1, 3, 1, 3, 1, 1, 1, 0, 1, 1, 1, 0, 2, 0, 2, 0, 3, 0, 3, 3, 3, 1, 2, 0, 0, 2, 3, 3, 0, 3, 3, 2, 2, 0, 0, 1, 3, 0, 0, 2, 2, 3, 3, 2, 1, 2, 0, 0, 2, 3, 3, 0, 3, 0, 0, 3, 3, 3, 1, 3, 1, 2, 1, 3, 0, 3, 1, 2, 3, 2, 0, 3, 3, 2, 0, 0, 3, 3, 1, 2, 2, 0, 2, 3, 1, 2, 0, 0, 2, 0, 1, 0, 1, 3, 2, 3, 1, 1, 2, 2, 2, 0, 3, 0, 1, 0, 2, 1, 1, 3, 2, 2, 3, 1, 0, 3, 1, 3, 2, 1, 1, 2, 2, 1, 2, 1, 2, 2, 2, 2, 1, 1, 2, 1, 1, 1, 1, 2, 1, 3, 1, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 1, 2, 1, 1, 2, 1, 2, 1, 1, 0, 2, 2, 2, 2, 3, 2, 2, 1, 2, 1, 1, 1, 2, 3, 1, 1, 2, 2, 2, 1, 1, 1, 1, 0, 2, 3, 0, 2, 3, 1, 1, 2, 1, 2, 2, 2, 2, 1, 2, 1, 1, 0, 1, 1, 1, 2, 1, 1, 1, 1, 0, 1, 3, 1, 1, 2, 1, 3, 0, 1, 0, 1, 2, 3, 2, 2, 0, 3, 1, 3, 2, 1, 2, 1, 0, 2, 0, 2, 2, 1, 3, 1, 2, 1, 1, 1, 1, 1, 1, 3, 1, 2, 2, 2, 1, 1, 1, 2, 3, 3, 1, 1, 1, 1, 3, 2, 2, 2, 1, 2, 1, 2, 1, 2, 2, 1, 1, 1, 1, 2, 1, 1, 2, 1, 2, 1, 2, 3, 2, 1, 2, 2, 3, 2, 1, 2, 2, 2, 1, 1, 1, 1, 2, 1, 2, 1, 2, 2, 2, 1, 1, 1, 1, 2, 2, 2, 2, 1, 0, 2, 0, 1, 2, 2, 1, 3, 0, 2, 3, 0, 1, 2, 1, 1, 0, 1, 2, 3, 1, 2, 3, 1, 1, 2, 2, 2, 1, 1, 2, 2, 2, 2, 2, 1, 1, 1, 2, 2, 1, 2, 1, 1, 1, 1, 0, 3], 'FSLR': [0, 2, 3, 1, 3, 2, 3, 3, 1, 3, 0, 3, 2, 3, 0, 2, 1, 0, 3, 2, 3, 0, 0, 2, 1, 0, 3, 3, 2, 1, 3, 3, 0, 0, 1, 3, 0, 0, 1, 0, 2, 2, 0, 2, 1, 0, 1, 3, 3, 0, 1, 0, 2, 1, 2, 2, 2, 3, 3, 1, 3, 1, 0, 0, 0, 0, 1, 0, 1, 2, 0, 0, 1, 0, 3, 1, 0, 3, 3, 1, 2, 0, 0, 0, 3, 3, 2, 0, 0, 3, 0, 1, 3, 3, 1, 0, 0, 1, 0, 0, 3, 3, 0, 2, 0, 0, 3, 0, 1, 3, 1, 3, 0, 3, 3, 3, 1, 0, 1, 0, 2, 3, 3, 3, 2, 1, 1, 3, 1, 0, 0, 2, 0, 3, 0, 3, 1, 3, 1, 0, 1, 0, 2, 2, 1, 0, 2, 0, 0, 0, 1, 2, 3, 3, 3, 0, 0, 0, 0, 0, 3, 3, 2, 3, 3, 1, 0, 0, 0, 0, 3, 0, 0, 3, 3, 2, 0, 0, 0, 0, 0, 0, 3, 3, 2, 0, 2, 0, 0, 1, 3, 3, 0, 2, 0, 3, 1, 0, 0, 3, 0, 3, 3, 3, 0, 3, 3, 3, 0, 0, 2, 3, 3, 0, 1, 0, 2, 3, 0, 2, 0, 3, 1, 0, 0, 3, 0, 3, 0, 3, 1, 2, 1, 0, 3, 0, 3, 0, 0, 0, 0, 3, 0, 3, 0, 3, 3, 0,
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              0, 3, 3, 3, 0, 3, 1, 3, 3, 3, 1, 0, 2, 3, 0, 1, 0, 2, 3, 3, 3, 0, 0, 2, 3, 2, 3, 2, 0, 3, 0, 0, 0, 1, 3, 3, 1, 0, 0, 0, 3, 2, 0, 0, 0, 0, 0, 0, 3, 3, 0, 3, 1, 3, 3, 0, 0, 0, 3, 0, 3, 0, 0, 2, 1, 0, 0, 0, 0, 0, 3, 3, 0, 0, 1, 3, 0, 2, 0, 0, 0, 0, 2, 2, 2, 2, 0, 1, 0, 3, 0, 3, 0, 2, 2, 0, 0, 3, 0, 3, 0, 3, 1, 2, 1, 0, 0, 0, 3, 3, 3, 0, 1, 0, 3, 0, 0, 3, 3, 3, 0, 0, 3, 0, 0, 3, 0, 3, 3, 3, 0, 0, 0, 0, 3, 0, 3, 3, 0, 2, 3, 0, 0, 0, 2, 0, 3, 0, 3, 0, 3, 0, 3, 3, 3, 3, 0, 0, 0, 3, 3, 0, 3, 3, 1, 3, 2, 3, 2, 0, 0, 3, 0, 0, 3, 3, 3, 3, 3, 2, 3, 0, 1, 3, 0, 0, 1, 0, 3, 3, 0, 1, 3, 0, 3, 0, 2, 3, 3, 3, 3, 2, 3, 3, 1, 0, 3, 0, 2, 3, 2, 3, 3, 0, 3, 3, 0, 3, 3, 3, 0, 0, 1, 3, 3, 0, 3, 1, 3, 3, 3, 1, 1, 3, 3, 3, 3, 0, 2, 3, 3, 1, 3, 0, 1, 3, 0, 0, 0, 3, 0, 1, 3], 'GOOG': [1, 3, 2, 2, 1, 2, 2, 1, 3, 3, 0, 1, 0, 1, 3, 1, 2, 0, 1, 3, 2, 1, 2, 2, 2, 1, 1, 3, 2, 1, 2, 2, 2, 0, 2, 1, 2, 2, 0, 2, 3, 0, 0, 2, 1, 0, 1, 0, 1, 0, 2, 1, 3, 2, 2, 2, 0, 1, 3, 2, 2, 2, 1, 0, 2, 3, 1, 1, 0, 2, 2, 0, 1, 0, 2, 1, 1, 3, 2, 2, 3, 0, 1, 2, 1, 2, 2, 2, 0, 1, 0, 0, 3, 1, 2, 0, 0, 1, 2, 1, 2, 3, 1, 2, 1, 1, 1, 2, 1, 0, 1, 2, 0, 1, 0, 1, 3, 0, 0, 0, 3, 3, 2, 3, 3, 3, 2, 3, 0, 1, 3, 2, 0, 3, 1, 3, 0, 3, 3, 2, 2, 0, 2, 0, 2, 0, 3, 0, 2, 0, 3, 0, 3, 2, 0, 0, 0, 0, 0, 3, 3, 2, 1, 3, 3, 2, 2, 0, 0, 1, 3, 2, 0, 3, 1, 2, 3, 2, 1, 1, 0, 0, 2, 3, 3, 0, 1, 0, 0, 3, 2, 3, 2, 3, 3, 2, 3, 3, 0, 3, 0, 2, 3, 3, 0, 2, 3, 2, 0, 0, 3, 3, 1, 3, 2, 0, 1, 3, 2, 2, 1, 0, 1, 0, 1, 0, 0, 3, 1, 3, 3, 3, 2, 1, 1, 0, 3, 1, 2, 0, 2, 3, 1, 3, 1, 2, 2, 3, 1, 2, 2, 3, 2, 0, 0, 0, 2, 2, 2, 1, 2, 2, 3, 0, 1, 1, 0, 1, 3, 1, 2, 2, 2, 3, 3, 1, 2, 2, 1, 3, 1, 1, 2, 1, 3, 1, 1, 2, 1, 3, 1, 2, 1, 0, 0, 2, 2, 0, 2, 3, 1, 2, 2, 3, 1, 3, 2, 1, 3, 1, 3, 0, 0, 2, 1, 0, 1, 1, 1, 3, 3, 0, 0, 2, 1, 0, 1, 2, 2, 3, 2, 1, 0, 1, 2, 2, 0, 3, 2, 1, 2, 0, 1, 3, 3, 1, 0, 3, 0, 3, 1, 0, 2, 0, 0, 0, 3, 0, 3, 1, 2, 0, 1, 1, 1, 2, 3, 3, 1, 0, 3, 0, 2, 2, 1, 3, 2, 3, 3, 0, 2, 1, 0, 1, 3, 1, 2, 2, 3, 3, 2, 0, 2, 2, 3, 1, 2, 1, 1, 3, 2, 1, 2, 2, 1, 3, 3, 1, 2, 2, 1, 1, 3, 1, 2, 0, 3, 3, 1, 2, 1, 1, 3, 2, 1, 0, 1, 3, 2, 2, 3, 3, 2, 2, 3, 1, 2, 2, 1, 2, 1, 2, 2, 1, 0, 0, 2, 2, 1, 1, 2, 3, 0, 0, 1, 2, 1, 2, 1, 2, 3, 2, 1, 1, 0, 0, 3, 2, 0, 1, 1, 1, 3, 2, 1, 2, 0, 3, 3, 3, 2, 1, 1, 1, 2, 0, 2, 3, 2, 2, 1, 3, 2, 1, 2, 1, 1, 1, 1, 1, 3]}

    testbins = {'FSLR': [3, 0, 0, 0, 3, 2, 2, 0, 3, 0, 1, 0, 3, 0, 0, 1, 0], 'GOOG': [
        2, 3, 1, 1, 2, 2, 1, 0, 2, 0, 1, 1, 1, 3, 3, 1, 1], 'DJIA': [1, 2, 1, 1, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 1]}

    # Run experiments
    orders = [1, 3, 5, 7, 9]
    ntrials = 500
    days = 5

    for symbol in symbols:
        print(symbol)
        print("====")
        print("Actual:", testbins[symbol][-days:])
        for order in orders:
            error = run_experiment(bins[symbol], order,
                                   testbins[symbol][-order - days:-days], days,
                                   testbins[symbol][-days:], ntrials)
            print("Order", order, ":", error)
        print

run()
