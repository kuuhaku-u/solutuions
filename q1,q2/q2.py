def difference(string1, string2):


    if len(string1) > len(string2):
        diff = len(string1) - len(string2)
        string1[:diff]

    elif len(string2) > len(string1):
        diff = len(string2) - len(string1)
        string2[:diff]

    else:
        diff = 0

    for i in range(len(string1)):
        if string1[i] != string2[i]:
            diff += 1

    return diff


if __name__=="__main__":
    print(difference("Quantom", "Quantum")) 
    