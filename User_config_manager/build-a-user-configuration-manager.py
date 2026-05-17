** start of main.py **

def add_setting(dicc,tup):
    key,value = tup
    key = key.lower()
    value = value.lower()

    if key in dicc:
        return f"Setting '{key}' already exists! Cannot add a new setting with this name."
    else:
        dicc[key] = value
        return f"Setting '{key}' added with value '{value}' successfully!"


def update_setting(dicc,tup):
    key,value = tup
    key = key.lower()
    value = value.lower()

    if key in dicc:
        dicc[key] = value
        return f"Setting '{key}' updated to '{value}' successfully!"
    else:
        return f"Setting '{key}' does not exist! Cannot update a non-existing setting."

def delete_setting(dicc,key):
    key = key.lower()

    if key in dicc:
        dicc.pop(key)
        return f"Setting '{key}' deleted successfully!"
    else:
        return f"Setting not found!"

def view_settings(dicc):
    if dicc == {}:
        return f"No settings available."
    else:
        output = 'Current User Settings:\n'
        for key,value in dicc.items():
            key = key.capitalize()
            output = output + key + ':' + ' ' + value +'\n'
    
    return output
    


test_settings = {}

print("--- Testing Add ---")
print(add_setting(test_settings, ('Theme', 'Dark'))) 
print(add_setting(test_settings, ('VOLUME', 'High')))

print("\n--- Testing Update ---")
print(update_setting(test_settings, ('theme', 'Light')))

print("\n--- Testing View ---")
print(view_settings(test_settings))

print("--- Testing Delete ---")
print(delete_setting(test_settings, 'volume'))
print(view_settings(test_settings))

** end of main.py **

