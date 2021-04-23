DECODE = {".-": "A", "-...": "B", "-.-.": "C",
          "-..": "D", ".": "E", "..-.": "F",
          "--.": "G", "....": "H", "..": "I",
          ".---": "J", "-.-": "K", ".-..": "L",
          "--": "M", "-.": "N", "---": "O",
          ".--.": "P", "--.-": "Q", ".-.": "R",
          "...": "S", "-": "T", "..-": "U",
          "...-": "V", ".--": "W", "-..-": "X",
          "-.--": "Y", "--..": "Z", ".-.-.-": ".",
          "--..--": ",", "..--..": "?", "-....-": "-",
          "-..-.": "/", "-----": "0", ".----": "1",
          "..---": "2", "...--": "3", "....-": "4",
          ".....": "5", "-....": "6", "--...": "7",
          "---..": "8", "----.": "9", "   ": " "
          }
ENCODE = {value: key for key, value in DECODE.items()}

while True:
    ins = input("You want decode or encode?: ")
    try:
        if ins.strip().lower() == "decode":
            de_code = input("Enter the morse codes you want to decode: ")

            print(' '.join(''.join(DECODE[x] for x in zac.split()) for zac in de_code.strip().split('   ')))

        elif ins.strip().lower() == "encode":
            en_code = input("Enter the morse codes you want to encode: ")

            print(' '.join([ENCODE[x] for x in en_code.strip().upper()]))

    except ValueError:
        print('Please enter valid value')
