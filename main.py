MORSE_CODE_DICT: dict = {
  "0": "-----",
  "1": ".----",
  "2": "..---",
  "3": "...--",
  "4": "....-",
  "5": ".....",
  "6": "-....",
  "7": "--...",
  "8": "---..",
  "9": "----.",
  "a": ".-",
  "b": "-...",
  "c": "-.-.",
  "d": "-..",
  "e": ".",
  "f": "..-.",
  "g": "--.",
  "h": "....",
  "i": "..",
  "j": ".---",
  "k": "-.-",
  "l": ".-..",
  "m": "--",
  "n": "-.",
  "o": "---",
  "p": ".--.",
  "q": "--.-",
  "r": ".-.",
  "s": "...",
  "t": "-",
  "u": "..-",
  "v": "...-",
  "w": ".--",
  "x": "-..-",
  "y": "-.--",
  "z": "--..",
  ".": ".-.-.-",
  ",": "--..--",
  "?": "..--..",
  "!": "-.-.--",
  "-": "-....-",
  "/": "-..-.",
  "@": ".--.-.",
  "(": "-.--.",
  ")": "-.--.-"
}


def translate(query: str) -> str:
    """
    Takes a String and converts it to morsecode.


    :parameter query: str = A word or sentence you want to translate

    :returns '......-...-..---'
    """
    answer = ""
    for symbol in query:
        if symbol == " ":
            answer += symbol
        else:
            answer += MORSE_CODE_DICT[symbol]
    return answer


run: bool = True

while run:
    string: str = input("Type a query you want to translate\n").lower()
    print(translate(string))
    run_test: str = input("Translate another one? (y/n)\n")
    if run_test == "n":
        run = False
