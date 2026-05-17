** start of main.py **

def add_setting(dicc: dict, tup: tuple) -> str:
    """
    Adds a new setting to the configuration dictionary.

    Args:
        dicc (dict): The dictionary storing the configuration settings.
        tup (tuple): A tuple containing the (key, value) pair to add.

    Returns:
        str: A message indicating success or failure.
    """
    key, value = tup
    
    # Convert to lowercase to ensure case-insensitive consistency
    key = key.lower()
    value = value.lower()

    if key in dicc:
        return f"Setting '{key}' already exists! Cannot add a new setting with this name."
    else:
        dicc[key] = value
        return f"Setting '{key}' added with value '{value}' successfully!"


def update_setting(dicc: dict, tup: tuple) -> str:
    """
    Updates an existing setting in the configuration dictionary.

    Args:
        dicc (dict): The dictionary storing the configuration settings.
        tup (tuple): A tuple containing the (key, new_value) pair.

    Returns:
        str: A message indicating success or failure.
    """
    key, value = tup
    
    # Standardize input to lowercase
    key = key.lower()
    value = value.lower()

    if key in dicc:
        dicc[key] = value
        return f"Setting '{key}' updated to '{value}' successfully!"
    else:
        return f"Setting '{key}' does not exist! Cannot update a non-existing setting."


def delete_setting(dicc: dict, key: str) -> str:
    """
    Deletes a setting from the configuration dictionary.

    Args:
        dicc (dict): The dictionary storing the configuration settings.
        key (str): The name of the setting to delete.

    Returns:
        str: A message indicating success or failure.
    """
    key = key.lower()

    if key in dicc:
        dicc.pop(key)
        return f"Setting '{key}' deleted successfully!"
    else:
        return "Setting not found!"


def view_settings(dicc: dict) -> str:
    """
    Returns a formatted string of all current user settings.

    Args:
        dicc (dict): The dictionary storing the configuration settings.

    Returns:
        str: A formatted string of settings or a message if empty.
    """
    # PEP 8 recommendation: check for empty sequences/dicts using 'if not'
    if not dicc:
        return "No settings available."
    else:
        output = 'Current User Settings:\n'
        for key, value in dicc.items():
            # Capitalize the key for better display formatting
            key = key.capitalize()
            # Using f-strings for cleaner and more readable string concatenation
            output += f"{key}: {value}\n"
            
        return output


# --- Testing block ---
if __name__ == "__main__":
    test_settings = {}

    print("--- Testing Add ---")
    print(add_setting(test_settings, ('Theme', 'Dark'))) 
    print(add_setting(test_settings, ('VOLUME', 'High')))

    print("\n--- Testing Update ---")
    print(update_setting(test_settings, ('theme', 'Light')))

    print("\n--- Testing View ---")
    print(view_settings(test_settings))

    print("\n--- Testing Delete ---")
    print(delete_setting(test_settings, 'volume'))
    print(view_settings(test_settings))

** end of main.py **

