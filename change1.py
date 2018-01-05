# Uses python3
#import sys

def change(to_be_changed):
    denomination = [10, 5, 1]
    resulting_change = list()
    #print(denomination)
    for bill in denomination:
        while to_be_changed >= bill:
            resulting_change.append(bill)
            to_be_changed = to_be_changed - bill
    #return resulting_change, len(resulting_change)
    return len(resulting_change)
    #print(resulting_change)


if __name__ == '__main__':
    input = input()
    to_be_changed = int(input)
    print(change(to_be_changed))