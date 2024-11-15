def checkMatches(file):
    f = open(file, 'r')
    lines = [line.strip().replace(" ", "") for line in f.readlines()]

    leaked = open("leakedhashes.txt", "r")
    leaked_lines = leaked.readlines()                                                                                                                                                                                                                                                                                                                                       

    leaked_lines = [line.strip().replace(" ", "").split(":") for line in leaked_lines]
    leaked_dict = {key: value for key, value in leaked_lines}
    
    #print(lines)
    #print(leaked_dict.values())

    for value in lines:
        if value in leaked_dict.values(): print(            )
        
    # print(matching_values)

    f.close()
    leaked.close()

checkMatches("rockyou2000sha256_dummy.txt")
