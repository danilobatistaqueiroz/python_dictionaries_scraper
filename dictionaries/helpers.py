
def red(text):
    return colored(255, 0, 0, text)

def blue(text):
    return colored(0, 200, 0, text)

def colored(r, g, b, text):
    return "\033[38;2;{};{};{}m{} \033[38;2;255;255;255m".format(r, g, b, text)