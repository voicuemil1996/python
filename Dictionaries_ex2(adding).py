
dict = {'key1':'value1', 'key2':'value2'}
print('Current dict: ', dict)

dict['new_key'] = 'new_value'
print('New dict: ', dict)

#also, it can be used the update function

dict1 = {'other_key1':'other_value1', 'other_key2':'other_value2'}
dict.update(dict1)
print('Newest dict: ', dict)