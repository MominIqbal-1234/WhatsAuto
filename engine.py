# file_handler.py

def write(file_path, content):
   
    try:
        with open(file_path, 'w') as file:
            file.write(content)
        print(f"Content successfully written to {file_path}")
    except Exception as e:
        print(f"Error writing to file: {e}")


def append(file_path, content):
   
    try:
        with open(file_path, 'a') as file:
            file.write(content)
        print(f"Content successfully appended to {file_path}")
    except Exception as e:
        print(f"Error appending to file: {e}")


def read(file_path):
   
    try:
        with open(file_path, 'r') as file:
            content = file.read()
        print(f"Content successfully read from {file_path}")
        return content
    except Exception as e:
        print(f"Error reading from file: {e}")
        return None
