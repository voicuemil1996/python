import requests

listOfEndpoints = ['https://official-joke-api.appspot.com/random_joke', 'https://official-joke-api.appspot.com/jokes/random',
                   'https://official-joke-api.appspot.com/random_ten', 'https://official-joke-api.appspot.com/jokes/ten',
                   'https://official-joke-api.appspot.com/jokes/programming/random', 'https://official-joke-api.appspot.com/jokes/programming/ten']

#1. For each endpoint write a method that retrieves the information.
#2. Format the output of the above mentioned methods in order to be more user friedly.
#3. Retrieve 10 random jokes by type and for each joke verify if the type is correct. If not, raise an error.
#4. Retrieve 10 random jokes and display only the ones that have an odd/even ID.

#1 and 2
print("1 and 2")
def problemSolve(listOfEndpoints):

    for endPoint in listOfEndpoints:

        response = requests.get(endPoint)
        result = response.json()

        if(type(result) == dict):

            friendlyResult = result['setup'] + '\n ' + result['punchline']
            print(friendlyResult, '\n')

        else:

            for dictionary in result:

                friendlyResult = dictionary['setup'] + '\n ' + dictionary['punchline']
                print(friendlyResult, '\n')

problemSolve(listOfEndpoints)

#3 and 4

root_endpoint = 'https://official-joke-api.appspot.com'
type = 'programming'
endpoint = root_endpoint + '/' + 'jokes' + '/' + type + '/' + 'ten'

response = requests.get(endpoint)
result = response.json()

print("3 and 4")
for i in result:

    if i['type'] != 'programming':

        print('There is a missmatch type!')

    if int(i['id']) % 2 == 0:

        print(i)

