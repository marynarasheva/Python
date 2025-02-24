import random
import string

def generate_random_dict():
    num_keys = random.randint(2, 3)  # Random number of keys in each dict
    keys = random.sample(string.ascii_lowercase, num_keys)  # Random unique letters as keys
    values = [random.randint(0, 100) for e in range(num_keys)]  # Random values (0-100)
    return dict(zip(keys, values))

def generate_list_of_dicts():
    num_dicts = random.randint(2, 3)  # Random number of dictionaries in the list
    return [generate_random_dict() for e in range(num_dicts)]

def merge_dicts(dict_list):
    merged_dict = {}  # Initialize an empty dictionary for the result
    key_sources = {}  # Dictionary to track which dict has the max value for a key

    for i, d in enumerate(dict_list, start=1):  # Iterate over list of dicts with index starting from 1
        for key, value in d.items():  # Iterate through key-value pairs of each dict
            if key in merged_dict:  # If key already exists in merged_dict
                if value > merged_dict[key]:  # Update if the new value is greater
                    merged_dict[key] = value  # Store the max value
                    key_sources[key] = i  # Track which dictionary had the max value
            else:
                merged_dict[key] = value  # Store key-value pair if key is new
                key_sources[key] = i  # Track source dict

    # Rename keys with the dictionary number that had the max value
    renamed_dict = {
        f"{key}_{key_sources[key]}" if list(key_sources.values()).count(key_sources[key]) > 1 else key: value for
        key, value in merged_dict.items()}

    return renamed_dict  # Return the merged dictionary with renamed keys


random_dict_list = generate_list_of_dicts()
print("Generated List of Dicts:", random_dict_list)
merged_dict = merge_dicts(random_dict_list)
print("Merged Dict:", merged_dict)


