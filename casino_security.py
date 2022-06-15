"""
You're head of security at a casino that has money being stolen from it. You get the data in the form of strings and you have to set off an alarm if a thief is detected.

    If there is no guard between thief and money, return "ALARM!"
    If the money is protected, return "Safe"

String Components

    x - Empty Space
    T - Thief
    G - Guard
    $ - Money
"""


def security(input):
    parsed = input.split('x')
    #remove empty elements from array
    parsed = list(filter(None, parsed))
    parsed = ''.join(parsed)
    for i in range(len(parsed)):
        if parsed[i] == "$":
            # check if next element is T
            if i+1 < len(parsed): 
                if parsed[i+1] == "T":
                    return "ALARM"
            # check if previous element is T
            if i-1 >= 0:
                if parsed[i-1] == "T":
                    return "ALARM"
    return "Safe"

print(security("xxTxxx$xxxTxxxGxxT"))
print(security("xGxx$xxGxxxTTT"))
print(security("TxGxx$xxx$xxxGxxT"))
print(security("GxxxTxxGxxTxx$xx$xxTxxG"))
print(security("xxGTxx$xx$xxxxxxG"))
print(security("xxTxxxxxxxx$xGxxxxxxT"))
print(security("xx$xxGxxxx$xxxxxxxxxxT"))
print(security("xxxTxxxxT"))
print(security("xxGxxxGGG"))
print(security("x$xx$x$x$xx"))