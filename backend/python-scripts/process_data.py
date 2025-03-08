def process_data(data):
    processed = {key: str(value).upper() for key, value in data.items()}
    return processed

