import argparse
from helper_modules.response_messages import success_preprocessed

#Function to preprocess data. Reads all the lines in a file and strips it of its space
#get the arguments parsed
parser = argparse.ArgumentParser()
parser.add_argument("-f","--filename", help="directory for file to be preprocessed, default directory is data/canopy_technical_test_input.txt",default="data/canopy_technical_test_input.txt")
args = parser.parse_args()

def preprocess(filename):
    #Open file and get all lnes
    with open(filename, 'r') as f:
        lines = f.readlines()

    #Remove all the spaces present
    lines = [line.replace(" ", '') for line in lines]

    # finally, write lines in the file
    with open('data/preprocessed_canopy_technical_test_input.txt', 'w') as f:
        f.writelines(lines)
    success_preprocessed()

preprocess(args.filename)
