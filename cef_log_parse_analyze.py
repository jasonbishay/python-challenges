"""
Create a function that performs CEF event log parsing and analyze a set of events to detect a user loging in from different IP addresses

CEF:Version|Device Vendor|Device Product|Device Version|Device Event Class ID|Name|Severity|[Extension]

Oct 12 04:16:11 localhost CEF:0|nxlog.org|nxlog|2.7.1243|Executable Code was Detected|Advanced exploit detected|100|src=192.168.255.110 spt=46117 dst=172.25.212.204 dpt=80

"""

def parse_extentions(extField):
    extDict = {}
    #check if extension field has at least 1 = sign:
    if "=" in extField:
        split_ext = extField.split(' ')
        for i in split_ext:
            kv = i.split('=')
            #need some error handling...
            extDict[kv[0]]=[kv[1]]

    return extDict


def parse_cef(cefLog):
    event = {
        "CEF Version" : "",
        "Vendor" : "",
        "Product" : "",
        "ProductVersion" : "",
        "EventID" : "",
        "EventName" : "",
        "Severity" : "",
        "Extension" : {}
    }
    split = cefLog.split('|')

    # Throw error if event doesn't have required fields
    if len(split) != 7 and len(split) != 8:
        raise ValueError("Input is not in proper CEF Format, expecting 7 or 8 fields but found: " + str(len(split)) + " fields.")

    event["CEF Version"] = split[0].split(':')[1]
    event["Vendor"] = split[1]
    event["Product"] = split[2]
    event["ProductVersion"] = split[3]
    event["EventID"] = split[4]
    event["EventName"] = split[5]
    event["Severity"] = split[6]
    if len(split) == 8:
        event["Extension"] = parse_extentions(split[7])

    return event



def test(input):
   event = parse_cef(input)
   print(event)
    #assert input == unshifted, "Shift/Unshift didn't match"

# Happy Case
test("CEF:0|nxlog.org|nxlog|2.7.1243|Executable Code was Detected|Advanced exploit detected|100|src=192.168.255.110 spt=46117 dst=172.25.212.204 dpt=80")

# Empty field
#test("CEF:0|nxlog.org||2.7.1243|Executable Code was Detected|Advanced exploit detected|100|src=192.168.255.110 spt=46117 dst=172.25.212.204 dpt=80")

# Empty extensions field
test("CEF:0|nxlog.org|2.7.1243|Executable Code was Detected|Advanced exploit detected|100|")

# Extra field
#test("CEF:0|nxlog.org|2.7.1243|Executable Code was Detected|Advanced exploit detected|100|fasd|fas|")

# Bad extensions field
test("CEF:0|nxlog.org|ngxlog.org|2.7.1243|Executable Code was Detected|Advanced exploit detected|100|fasd")

# Remove field
"""
try:
    test("CEF:0|nxlog.org|2.7.1243|Executable Code was Detected|Advanced exploit detected|100|src=192.168.255.110 spt=46117 dst=172.25.212.204 dpt=80")
except ValueError as err:
    print("Error Occured: "+ str(err))
"""

