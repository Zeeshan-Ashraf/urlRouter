def getRegex(path: str):
    pathSplit = path.split("*")

    regexGlobal = ""
    for item in pathSplit:
        regexLocal = ""
        for c in item:
            if c == "/":
                regexLocal += "\/"
            else:
                regexLocal += c
        regexGlobal += regexLocal
        regexGlobal += "[\w\d\/]*"
    regexGlobal = regexGlobal[:-9]

    return regexGlobal