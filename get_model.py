# This function finds the model type used for the MOSFET under test
# This function was written on 31/1/2020
import re


def get_model(path):

    # Open the model file
    try:
        with open(path) as my_file:
            s = my_file.read()
    except:
        print("Model path is wrong")

    # Finding the word ".model" or ".MODEL"
    try:
        strn = re.findall(".[modelMODEL]{5}\s+(\S*)\s+[nmosNMOS]{4}", s)[0]
        strp = re.findall(".[modelMODEL]{5}\s+(\S*)\s+[pmosPMOS]{4}", s)[0]
        return strn, strp
    except:
        print("Model file does not contain MOSFET model")
        return

