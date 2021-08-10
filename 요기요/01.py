S = "John Doe; Peter Benjamin Parker; Mary Jane Watson-Parker; John Elvis Doe; John Evan Doe; Jane Doe; Peter Brian Parker"
C = "Example"

def solution(S, C):
    def deleteLastSemicolon(companyEmails):
        return companyEmails[:len(companyEmails) - 1]

    companyEmails = ""
    emailForm = "@" + C.lower() + ".com; "
    MAX_LENGTH_LAST_NAME = 8
    sameFullNameCount = {}
    fullNames = S.split("; ")

    for fullName in fullNames:
        splitedFullName = fullName.lower().split(" ")
        firstName = splitedFullName[0]
        lastName = "".join(splitedFullName[-1].split("-"))[:MAX_LENGTH_LAST_NAME]
        changedFullName = firstName + "." + lastName

        if changedFullName not in sameFullNameCount:
            sameFullNameCount[changedFullName] = 1
            companyEmails += changedFullName + emailForm

        else:
            sameFullNameCount[changedFullName] += 1
            companyEmails += changedFullName + str(sameFullNameCount[changedFullName]) + emailForm

    companyEmails = deleteLastSemicolon(companyEmails.rstrip())

    return companyEmails

print(solution(S, C))

a = 1.0 / 7.0
b = 0
for _ in range(7):
    b += a
print(b)
print(b == 1)

print(1.0 / 7.0)