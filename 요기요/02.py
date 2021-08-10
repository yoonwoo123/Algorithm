S = """  root r-x delete-this.xls
  root r-- bug-report.pdf
  root r-- doc.xls
  root r-- podcast.flac
 alice r-- system.xls
  root --x invoices.pdf
 admin rwx SETUP.PY"""

def solution(S):
    minFileLength = 999
    findOwner = "root"
    readOnly = {"r--", "r-x"}
    binaryDocumentData = {"doc", "xls", "pdf"}
    lines = S.split("\n")

    for i in range(len(lines)):
        lines[i] = lines[i].lstrip()

    for line in lines:
        owner, perm, name = line.split(" ")
        extension = name.split(".")[-1]

        if owner == findOwner and perm in readOnly and extension in binaryDocumentData:
            minFileLength = min(minFileLength, len(name))

    if minFileLength == 999:
        return "NO FILES"

    return str(minFileLength)

print(solution(S))