import re
from convert_to_float import convert_to_float
import matplotlib.pyplot as plt
import numpy as np


def parese_text(text):
    REG_EXPRESION = r"[+-] ?\d*,\d* ?€"
    # Regulärer Ausdruck für das gewünschte Muster
    pattern = re.compile(REG_EXPRESION)

    # Alle Treffer im Text finden
    return pattern.findall(text)


def read_file(path):
    with open(path, "r") as file:
        content = file.read()
    content = content.replace("\n", "")
    content = content.replace("", "")
    return content


def plot(entrys, name):
    plt.cla()
    plt.plot(entrys, marker='o', linestyle='-',
             color='b', label='Datenverlauf')
    plt.grid()
    plt.xticks([])  # X-Achsen-Beschriftung entfernen
    plt.xlabel(name)
    plt.savefig(name + ".pdf", format='pdf')


def create_absolut(end, entrys):
    current_number = end
    result_as_absolut = [current_number]
    for entry in entrys:
        current_number += (entry * -1)
        result_as_absolut.append(current_number)
    return reversed(result_as_absolut)


def parse_month(path, end) -> float:
    text = read_file(path)
    raw_entrys = parese_text(text)
    float_entrys = convert_to_float(raw_entrys)
    # print(*float_entrys, sep="\n")
    # print("----------------------")
    absolut_entrys = list(create_absolut(end, float_entrys))
    plot(absolut_entrys, path[:-4])
    return end + sum(x * -1 for x in float_entrys)


def main():
    END = 0
    new_end = parse_month("abrechnung/maerz_25.txt", END)
    print(new_end)
    parse_month("abrechnung/februar_25.txt", new_end)


if __name__ == "__main__":
    main()
