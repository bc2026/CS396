import hashlib

with open('rockyou2000.txt', 'r', encoding='utf=8') as file1, open("rockyou2000md5.txt", 'w', encoding='utf-8') as file2:
    for line in file1:
        string = line.strip()
        hash = hashlib.md5(string.encode()).hexdigest()

        file2.write(f"{string}: {hash}\n")

print("Done!")