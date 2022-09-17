# utils for file encryption and decryption
import os

def plain_text(file):
    return

# transpose encryption for reversing words in file
def transpose_encryption(file):
    current_file = file.split('.')
    file1 = open(current_file[0] + '1.' + current_file[1], 'w')
    file2 = open(file, 'r')

    for line in file2:
        word = line.split()
        for i in range(len(word)):
            new_word = word[i]
            file1.write(new_word[::-1])
            if (i != len(word) - 1):
                file1.write(' ')
        file1.write('\n')

    file1.truncate()
    file1.close()
    file2.close()
    try:
        os.remove('./' + file)
    except:
        os.remove(file)

    file1 = open(current_file[0] + '1.' + current_file[1], 'r')
    file2 = open(file, 'w')

    for line in file1:
        word = line.split()
        for i in range(len(word)):
            new_word = word[i]
            file2.write(new_word)
            if (i != len(word) - 1):
                file2.write(' ')
        file2.write('\n')

    file2.truncate()
    file2.close()
    file1.close()
    try:
        os.remove('./' + current_file[0] + '1.' + current_file[1])
    except:
        os.remove(current_file[0] + '1.' + current_file[1])



# Substitue encryption
def substitute_encode(file):
    current_file = file.split('.')
    file1 = open(current_file[0] + '1.' + current_file[1], 'w')
    file2 = open(file, 'r')

    file3 = file2.read(1)
    while file3:
        file1.write(chr((ord(file3) + 2) % 256))
        file3 = file2.read(1)

    file1.close()
    file2.close()

    try:
        os.remove('./' + file)
    except:
        os.remove(file)
    
    file1 = open(current_file[0] + '1.' + current_file[1], 'r')
    file2 = open(file, 'w')

    for line in file1:
        word = line.split()
        for i in range(len(word)):
            new_word = word[i]
            file2.write(new_word)
            if (i != len(word) - 1):
                file2.write(' ')
        file2.write('\n')

    file2.truncate()
    file2.close()
    file1.close()
    try:
        os.remove('./' + current_file[0] + '1.' + current_file[1])
    except:
        os.remove(current_file[0] + '1.' + current_file[1])

# substitute decryption
def substitute_decode(file):
    current_file = file.split('.')
    file1 = open(current_file[0] + '1.' + current_file[1], 'w')
    file2 = open(file, 'r')

    file3 = file2.read(1)
    while file3:
        file1.write(chr((ord(file3) - 2) % 256))
        file3 = file2.read(1)

    file1.close()
    file2.close()

    try:
        os.remove('./' + file)
    except:
        os.remove(file)
    
    file1 = open(current_file[0] + '1.' + current_file[1], 'r')
    file2 = open(file, 'w')

    for line in file1:
        word = line.split()
        for i in range(len(word)):
            new_word = word[i]
            file2.write(new_word)
            if (i != len(word) - 1):
                file2.write(' ')
        file2.write('\n')

    file2.truncate()
    file2.close()
    file1.close()
    try:
        os.remove('./' + current_file[0] + '1.' + current_file[1])
    except:
        os.remove(current_file[0] + '1.' + current_file[1])
