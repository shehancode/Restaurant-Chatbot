import re


def extract_session_id(session_str: str) -> str:
    # Define the regular expression pattern
    pattern = r"/sessions/(.*?)/contexts"

    # Search for the pattern in the input text
    match = re.search(pattern, session_str)

    if match:
        # Return the matched group (the session ID)
        extracted_string = match.group(1)
        return extracted_string

    return "No session ID found."


def get_str_from_food_dict(food_dict: dict):
    return ", ".join([f"{int(value)} {key}" for key, value in food_dict.items()])


if __name__ == "__main__":
    print(get_str_from_food_dict({'pizza': 2, 'lime': 1}))
