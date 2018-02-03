from os.path import basename


def clean_line(line):
    res = line.strip("# ")
    res = res.rstrip('\n')
    res = res.replace(" ", "")
    return res


def split_and_get(string, split, position):
    return string.split(split)[position]


def get_user_id(line):
    return split_and_get(clean_line(line), ".", 0)


def get_alcoholic(line):
    return line[3]


def get_experiment(line):
    return clean_line(line).replace("trial", "").split(",")


def get_channel(line):
    return clean_line(line)


def get_reading(line):
    return " " + line.rstrip('\n').split(" ")[3]


def process_file(file_name, overwrite=False):

    raw_file = open(file_name, "r")
    splitted_file_name = "results/" + basename(file_name).split('.')[0]+".txt"

    if overwrite:
        result_file = open(splitted_file_name, 'w')

    else:
        result_file = open(splitted_file_name, 'a')
    user_id = get_user_id(raw_file.readline())
    alcoholic = get_alcoholic(user_id)
    raw_file.readline()
    raw_file.readline()
    experiment = get_experiment(raw_file.readline())
    paradigm = experiment[0]
    repetition = experiment[1]
    readings = ""

    for line in raw_file:
        if line[0] is '#':
            if len(readings) > 0:
                result_file.write(readings + '\n')
            channel = get_channel(line)
            readings = ""
            result_file.write(user_id + " " + alcoholic + " " + paradigm + " " + repetition + " " + channel)
        else:
            readings += get_reading(line)
    result_file.write(readings + '\n')

    raw_file.close()
    result_file.close()
