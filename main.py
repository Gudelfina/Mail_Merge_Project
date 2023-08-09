#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

with open("input/Names/invited_names.txt", mode='r') as name:
    names = name.readlines()
    # new_names = [name.rstrip() for name in names]

with open("input/Letters/starting_letter.txt") as letter:
    contents = letter.read()
    for n in names:
        name = n.strip()
        with open(f"Output/ReadyToSend/{n}_invite.txt", 'w') as invite:
            new_contents = invite.write(contents.replace("[name]", name))

