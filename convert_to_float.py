import re
REG_EXPRESION_FIRST_NUMBER = r"[+-] ?\d*,"
REG_EXPRESION_SECOND_NUMBER = r",\d* ?€"


class Str_Number:
    first: str
    second: str
    postiv: bool = True

    def set_first(self, num):
        self.first = num
        if self.first[0] == "-":
            self.postiv = False

    def set_second(self, num):
        self.second = num

    def get_float(self) -> float:
        num = float(f"{self.first[1:-1]}.{self.second[1:-1]}")
        if not self.postiv:
            num *= -1
        return num


def get_number(pattern, raw_entry):
    raw = pattern.findall(raw_entry)
    assert (len(raw) == 1)
    raw = raw[0].replace(" ", "")
    return raw


def convert_to_float(raw_entrys):
    pattern_first_number = re.compile(REG_EXPRESION_FIRST_NUMBER)
    pattern_second_number = re.compile(REG_EXPRESION_SECOND_NUMBER)

    result_as_float = []
    for raw_entry in raw_entrys:
        entry = Str_Number()
        entry.set_first(get_number(pattern_first_number, raw_entry))
        entry.set_second(get_number(pattern_second_number, raw_entry))
        result_as_float.append(entry.get_float())

    return result_as_float
