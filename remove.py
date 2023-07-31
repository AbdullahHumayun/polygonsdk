def delete_between_quotes(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()

    inside_quotes = False
    new_content = ''
    for char in content:
        if char == '"':
            inside_quotes = not inside_quotes
            continue

        if not inside_quotes:
            new_content += char

    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(new_content)


# Example usage
file_path = 'api_master/cfg.py'
delete_between_quotes(file_path)