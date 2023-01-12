import string


def convert_class_name_to_snake_case(class_name: str) -> str:
    converted_class_name = ''
    for index, symbol in enumerate(class_name):
        converted_class_name += symbol.lower()
        if class_name[index + 1:index + 2].isupper() and not symbol.isupper() and index:
            converted_class_name += '_'
        elif class_name[index:index + 2].isupper() and not class_name[index + 2:index + 3] in string.ascii_uppercase:
            converted_class_name += '_'

    return converted_class_name.rstrip('_')
