"""Random code """
class EmptyFileError(Exception): 
    pass

filenames = ["myfile1", "nonExistent", "emptyFile", "myfile2"]
for file in filenames:
    try:
        f = open(file, 'r')
        line = f.readline()
        if line == "":
            f.close()
            raise EmptyFileError("%s: is empty" % file)
    except IOError as error:
        print("%s: could not be opened: %s"% (file, error.strerror))
    except EmptyFileError as error:
        print(error)
    else:
        print("%s: %s" % (file, f.readline()))
    finally:
        print("Done processing", file)

filename = "myfile.txt"
with open(filename, "r") as f:
    for line in f:
        print(f)

"""wo module. Contains function: words_occur()"""
# interface functions
def words_occur():
    file_name = input("Enter the name of the file: ")
    # Open the file, read it and store its words in a list
    f = open(file_name, 'r')
    word_list = f.read().split()
    f.close()
    # Count the number of occurences of each word in the file
    occurs_dict = {}
    for word in word_list:
        # increment the occurrences count for this world
        occurs_dict[word] = occurs_dict.get(word, 0) + 1
    # Print out the results
    print("File %s has %words (%d are unique)" % (file_name, len(word_list), len(occurs_dict)))
    print(occurs_dict)

if __name__ == '__main__':
    words_occur()