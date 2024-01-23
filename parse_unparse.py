# this file contains the helper functions to parse and unparse JSON to Python Dict

import json

def parse_json_to_dict(file_path):
    """
    Parses a JSON file on disc into a Python dictionary of dictionaries.

    Args:
    file_path (str): The path to the JSON file.

    Returns:
    dict: A dictionary where each key is a UserID and the value is another dictionary of user details.

    Example usage
    file_path = "path_to_your_json_file.json"
    user_data = parse_json_to_dict(file_path)
    """
    try:
        with open(file_path, 'r') as file:
            user_data = json.load(file)
        
        # Optionally, print the data (can be commented out or removed)
        for user_id, details in user_data.items():
            print(f"User ID: {user_id}")
            for key, value in details.items():
                print(f"{key}: {value}")
            print()

        return user_data
    except Exception as e:
        print(f"An error occurred: {e}")
        return {}

import json

def unparse_dict_to_json(user_data):
    """
    Converts a Python dictionary of dictionaries to a JSON-formatted string.

    Args:
    user_data (dict): A dictionary where each key is a UserID and the value is another dictionary of user details.

    Returns:
    str: A JSON-formatted string representing the user data.

    Example usage
    user_data = {
        "12345": {
            "First_Name": "John",
            "Last_Name": "Doe",
            # other details...
        },
        "67890": {
            "First_Name": "Jane",
            "Last_Name": "Smith",
            # other details...
        }
    }
    json_data = unparse_dict_to_json(user_data)
    print(json_data)

    """
    try:
        # Convert the dictionary to a JSON string
        json_data = json.dumps(user_data, indent=4) # 'indent' for pretty-printing
        return json_data
    except TypeError as e:
        print(f"TypeError occurred: {e}")
        return ""
    except Exception as e:
        print(f"An error occurred: {e}")
        return ""


