# This function is used to obtain the level of the model file in order to determine the used BSIM model
# This function is written on 31/1/2020
import string


def read_model_file(path):

    # Open the model file
    with open(path, 'r') as x:
        model_file = x.read()

    # Strip the model file of all whitespaces
    model_file_stripped = model_file.translate({ord(c): None for c in string.whitespace})

    # Find the index of the word "Level" or "level"
    if model_file_stripped.find('Level') != -1:
        level_idx = model_file_stripped.find('Level')
    else:
        level_idx = model_file_stripped.find('level')

    # Obtain the number of the level
    bsim_model_level = model_file_stripped[level_idx+6] + model_file_stripped[level_idx+7]

    # Create a list of strings of the numbers from 0 to 9
    list_str = []
    for i in range(10):
        list_str.append(str(i))

    # Find if the level number is one or two decimals
    if bsim_model_level[0] in list_str and bsim_model_level[1] in list_str:
        pass
    else:
        bsim_model_level = bsim_model_level[0]

    # Comparing the level number to the level numbers of various BSIM Models
    if bsim_model_level == '49' or bsim_model_level == '8':
        bsim_model = 3
    elif bsim_model_level == '54' or bsim_model_level == '14':
        bsim_model = 4
    if bsim_model_level == '5':
        bsim_model = 2
    if bsim_model_level == '4':
        bsim_model = 1
    if bsim_model_level == '10' or bsim_model_level == '58' or bsim_model_level == '55' or bsim_model_level == '56' or bsim_model_level == '57':
        bsim_model = 'bsim_soi'
    if bsim_model_level == '60':
        bsim_model = 'bsim_soi_3'

    return bsim_model

