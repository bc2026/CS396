import os

def checkMatches(file):
    f = open(file, 'r')
    passwords = [line.strip().replace(" ", "").split(":") for line in f.readlines()]
    pw_hashes = {key: value for key, value in passwords}
    
    #print(pw_hsh)

    # Need to look at leaked hashes
    # See if pw_hsh value matches leaked hashes value
    
    leaked = open("leakedhashes.txt", "r")                                                                                                                                                                                                                                                                                                         
    leaked_lines = [line.strip().replace(" ", "").split(":") for line in leaked.readlines()]
    user_pw_leaked_hash = {key: value for key, value in leaked_lines}

    hits = open("hits.txt", "w")

    for pw_hsh in pw_hashes.values():
        if(pw_hsh in user_pw_leaked_hash.values()):
            hits.write(f"{list(user_pw_leaked_hash.keys())[list(user_pw_leaked_hash.values()).index(pw_hsh)]}:{list(pw_hashes.keys())[list(pw_hashes.values()).index(pw_hsh)]}")
            hits.write("\n")
    hits.close()


print("SHA256 Matches:")
checkMatches("rockyou2000sha256.txt")

print("MD5 Matches:")
checkMatches("rockyou2000md5.txt")

