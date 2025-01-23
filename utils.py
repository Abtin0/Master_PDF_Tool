import re


def input_to_list(raw_input):
    return re.split(r"[,\-]+", raw_input.replace(" ", ""))


def input_extention(file_name):
    return file_name + ".pdf".lower() if ".pdf" not in file_name else file_name.lower()
