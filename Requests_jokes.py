import requests

listOfEndpoints = ['https://official-joke-api.appspot.com/random_joke', 'https://official-joke-api.appspot.com/jokes/random',
                   'https://official-joke-api.appspot.com/random_ten', 'https://official-joke-api.appspot.com/jokes/ten',
                   'https://official-joke-api.appspot.com/jokes/programming/random', 'https://official-joke-api.appspot.com/jokes/programming/ten']

#1. For each endpoint write a method that retrieves the information.
#2. Format the output of the above mentioned methods in order to be more user friedly.
#3. Retrieve 10 random jokes by type and for each joke verify if the type is correct. If not, raise an error.
#4. Retrieve 10 random jokes and display only the ones that have an odd/even ID.


#1
def get_information(path = '/random_joke'):

    root = 'https://official-joke-api.appspot.com'
    endpoint = root + path
    response = requests.get(endpoint)

    return response.json()

#2
def making_reading_friendly(path = '/random_joke'):

    result = get_information(path)

    if (type(result) == dict):

        friendlyResult = result['setup'] + '\n ' + result['punchline']

    else:

        friendlyResult = []
        for dictionary in result:
            friendlyResult.add(dictionary['setup'] + '\n ' + dictionary['punchline'])

    return friendlyResult

#3
def checking_type(path = '/jokes/programming/ten', type = 'programming'):

    result = get_information(path)

    if type not in path:
        print('Path must contain type!')

    for i in result:
        if i['type'] != type:
            print('There is a missmatch type!')
            return False

    return True

#4
def displayng_odd_IDs(path = '/jokes/programming/ten'):

    result = get_information(path)

    print('displayng jokes with odd ID')
    for i in result:
        if int(i['id']) % 2 == 0:
            print(i)

print("Test #1: ",get_information())
print("Test #2: ",making_reading_friendly())
print("Test #3: ",checking_type())
print("Test #4: ",displayng_odd_IDs())

