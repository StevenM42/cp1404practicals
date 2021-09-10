"""
CP1404/CP5632 Practical
Colours hexadecimal code in a dictionary
"""

COLOUR_HEX_CODES = {"AliceBlue": "#f0f8ff", "AntiqueWhite": "#faebd7", "AntiqueWhite1": "#ffefdb",
                    "AntiqueWhite2": "#eedfcc", "AntiqueWhite3": "#cdc0b0", "AntiqueWhite4": "#8b8378",
                    "aquamarine1": "#7fffd4", "aquamarine2": "#76eec6", "aquamarine4": "#458b74", "azure1": "#f0ffff"}

colour_name = input("Enter colour name: ")
while colour_name != "":
    colour_hex_code = COLOUR_HEX_CODES.get(colour_name)
    print("The hexadecimal colour code of {} is {}".format(colour_name, colour_hex_code))
    colour_name = input("Enter colour name: ")
