import json, jmespath
from pprint import pprint
from os.path import exists

def user_interaction() -> str:
    path = input(
        'Please, insert full path to the json file you want to analyse\n'
    )
    return path


def read_json_file(path: str) -> dict:
    '''
    '''
    with open(path) as file:
        json_info = json.load(file)
    return json_info

def invalid_input() -> str:
    value = input('Invalid input. PLease, try again:\n')
    return value


def analyze_json(json_info: dict):
    while True:
        if isinstance(json_info, dict):
            keys_info_lst = list(json_info.keys())
            print(f'There are {len(keys_info_lst)} keys in this dictionary. Here they are:')
            pprint(keys_info_lst)
            key = input(
                '\nPlease, input one of these keys to get further information\
or press "Enter" to quit the programm.\n')
            if len(key) < 1:
                print('Thank you for using the programm!')
                break
            
            try:
                json_info = json_info[key]
            except KeyError:
                print('Invalid input. Please, try again')
                continue
        else:
            if isinstance(json_info, list):
                if len(json_info) < 1:
                    print('There is no information here. Thank you for using the programm!')
                else:
                    print(f'The length of a list is {len(json_info)}.')
                    idx = int(input(
                        f'Please, type index of an element of list you want to get info\
 about in range from 0 to {len(json_info) - 1}.\n'))
                json_info = json_info[idx]
            else:
                print(f'Within a key "{key}" and index "{idx}" there is following information:\n{json_info}.\n\
Thank you for using the programm!')
                break

def main():
    '''
    Main function combining everything into a working project
    '''
    path = user_interaction()
    if not exists(path):
        while not exists(path):
            path = input('Path is invalid, please, enter valid path to the json file:\n')
    json_info = read_json_file(path)
    analyze_json(json_info)


if __name__ == '__main__':
    main()
    #print(exists('/Users/shevdan/Documents/Programming/Python/semester2/lab3/twitter_json/user_timeline_of'))