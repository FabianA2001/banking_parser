PRE = "abrechnung/"
YEAR = 26
monate = ["Januar", "Februar", "März", "April", "Mai", "Juni",
          "Juli", "August", "September", "Oktober", "November", "Dezember"]


if __name__ == "__main__":
    for i in range(12):
        null = ""
        if i < 10:
            null = "0"
        with open(PRE + f"{YEAR}_{null}{i+1}_{monate[i]}.txt", "w") as file:
            pass  # Creates an empty file
