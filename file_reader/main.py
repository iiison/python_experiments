file = open('./data.txt', 'r')

# Read Mode
if file.readable() :
    file_content = file.readlines()

    for line in file_content :
        print(line)
else :
    print('file is not readable')

file.close()
#######################################

# Append Mode
file = open('./data.txt', 'a')
new_line = input('What do you want to add? \n')
file.write('\n' + new_line + '\n')

file.close()
#######################################

# Write Mode
file = open('./data.txt', 'w')
# Write mode overrites the current data. That means if you want to keep the
# existing data in the file, either open it in read mode, save the content in a variable
# and then close the file and open in write mode. Or open the file in read-write mode(r+)
new_content = input('What do you want to write in the file? \n')
file.write(new_content + '\n')

print('The file cont has been updated!')
file.close()

# Create new File
file_name = input('Enter the new file name: ')
file = open('./' + file_name, 'w')
file_content = input('Enter file content: \n')
file.write(file_content + '\n')

print('A new file with {} name has been created!'.format(file_name))

file.close()
#######################################

