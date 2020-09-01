import requests


listOfEndpoints = ['https://official-joke-api.appspot.com/random_joke', 'https://official-joke-api.appspot.com/jokes/random',
                   'https://official-joke-api.appspot.com/random_ten', 'https://official-joke-api.appspot.com/jokes/ten',
                   'https://official-joke-api.appspot.com/jokes/programming/random', 'https://official-joke-api.appspot.com/jokes/programming/ten']

root = 'https://official-joke-api.appspot.com'
#1. For each endpoint write a method that retrieves the information.
#2. Format the output of the above mentioned methods in order to be more user friedly.
#3. Retrieve 10 random jokes by type and for each joke verify if the type is correct. If not, raise an error.
#4. Retrieve 10 random jokes and display only the ones that have an odd/even ID.


#1
def get_information(path):

    endpoint = root + path
    response = requests.get(endpoint)

    if type(response.json()) == list:

        return response.json()

    else:

        return [response.json()]

def get_friendly_information(path):
    return making_reading_friendly(get_information(path))

def get_random_joke():
    return get_friendly_information('/random_joke')

def get_random_ten():
    return get_friendly_information('/random_ten')

def get_random_ten_by_type():
    return get_friendly_information('/jokes/programming/ten')

def get_random_joke_by_type():
    return get_friendly_information('/jokes/programming/joke')


#2
def making_reading_friendly(jokes):

    friendlyJokes = []
    for dictionary in jokes:
        friendlyJokes.append(dictionary['setup'] + '\n ' + dictionary['punchline'])

    return friendlyJokes

#3
def checking_type_for_10(type='programming'):

    path = '/jokes/programming/ten'
    jokes = get_information(path)

    if type not in path:
        print('Type should be contained in path')
        return False

    for i in jokes:
        if i['type'] != type:
            print('There is a missmatch type!')
            return False

    return True

#4
def displayng_odd_IDs_for_10():

    jokes = get_information('/jokes/ten')
    goodJokes = []


    for i in jokes:
        if int(i['id']) % 2 == 0:
            goodJokes.append(i)

    print('displayng jokes with odd ID\n')
    for i in making_reading_friendly(goodJokes):
        print(i)

print("Test #1 and #2: ",get_random_ten(), "\n", get_random_joke())
print("Test #3: ",checking_type_for_10())
print("Test #4: ")
displayng_odd_IDs_for_10()

