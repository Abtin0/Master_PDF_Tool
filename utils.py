def input_to_list(raw_input):
    return raw_input.replace(" ", "").split(",")


def input_extention(path):
    return path + ".pdf" if ".pdf" not in path else path
