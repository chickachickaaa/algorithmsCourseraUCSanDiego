# Uses python3
import sys

def get_optimal_value(capacity, weights, values):
    arrayOfSelectedItems = [0] * (n + 1)
    value = 0
    for i in range(n):
        if capacity == 0:
            return(value, arrayOfSelectedItems )
        max_index = select_max_index(values, weights)
        if max_index >= 0:
            available_Weight = min(weights[max_index],capacity)
            value = value + available_Weight*(values[max_index]/weights[max_index])
            weights[max_index] = weights[max_index] - available_Weight
            arrayOfSelectedItems[max_index] = arrayOfSelectedItems[max_index] + available_Weight
            capacity = capacity - available_Weight
    #type(value) is float
    #type(value) is int
    return value, arrayOfSelectedItems


def select_max_index(values, weights):
    index = -1
    max = 0
    for i in range(n):
        if weights[i] > 0 and (values[i] / weights[i]) > max:
            max = values[i] / weights[i]
            index = i
    return index

if __name__ == "__main__":
    data = list(map(int, sys.stdin.read().split()))
    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]
    opt_value = get_optimal_value(capacity, weights, values)
    #print("{!s:10}".format(opt_value)) #works kinda but returns (180.0, [20, 0, 30, 0])
    #print("{:.10f}".format(opt_value)) #came with starter file
    #print'{!s:20s}'.format(b"Hi")"b'Hi' right. wrong --> "{:20}".format(b"hi")
    #print("{0:.15f}".format(opt_value)) TypeError: non-empty format string passed to object.__format__
    #print("{!s:.10}".format(opt_value)) wrong output format: could not convert string to float: '(180.0,' (180.0, [2
    #print("{0:.2f}".format(opt_value)) TypeError: non-empty format string passed to object.
    #print("{!f:.2}".format(opt_value)) wrong output format: list index out of range
    #print("% .4f".format(opt_value)) # wrong output format: could not convert string to float: '%'  % .4f
    #print("{% .4f}".format(opt_value)) wrong output format: list index out of range
    #float(opt_value)
    #opt_value = (float(opt_value[0])) TypeError: 'float' object is not subscriptable #print("{:.10f}".format(opt_value))
    opt_value = ((opt_value[0]))
    print("{:.10f}".format(float(opt_value)))

    #print(opt_value) (180.0, [20, 0, 30, 0])