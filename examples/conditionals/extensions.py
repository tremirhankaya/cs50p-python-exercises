def main():
    print(find_file_type(input("File Name: ")))


def normalize_input(file_name):
    return file_name.strip().lower()


def find_file_type(file_name):
    file_name = normalize_input(file_name)
    if file_name.endswith(".gif"):
        return "image/gif"
    elif file_name.endswith(".jpeg") or file_name.endswith(".jpg"):
        return "image/jpeg"
    elif file_name.endswith(".png"):
        return "image/png"
    elif file_name.endswith(".pdf"):
        return "application/pdf"
    elif file_name.endswith(".txt"):
        return "text/plain"
    elif file_name.endswith(".zip"):
        return "application/zip"
    else:
        return "application/octet-stream"


main()
