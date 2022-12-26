#! /usr/bin/python3
from ast import literal_eval
import html
import sys
import re


def sanitize(value):
    if isinstance(value, list):
        return sanitize_list(value)
    if isinstance(value, dict):
        return sanitize_dict(value)
    if isinstance(value, str):
        return sanitize_str(value)

    return True, value


def sanitize_dict(data: dict):
    try:
        status_data = True
        secure_data = {}

        for key in data:
            value = data[key]  # ATRIBUI O VALOR DIGITADO PARA A VAR INPUT
            status_value, secure_value = sanitize(value)
            secure_data[key] = secure_value
            if not status_value:
                status_data = False

        return status_data, secure_data

    except Exception as error:
        secure_data.update({"error": error})
        return False, secure_data


def sanitize_list(data: list):
    status = True
    new_list = []

    for value in data:
        status_data, secure_input = sanitize(value)
        new_list.append(secure_input)
        if not status_data:
            status = False

    return status, new_list


def sanitize_str(value: str):
    value = html.escape(value)  # ENCODA CARACTERES DE TAG HTML
    if len(value) > 100:
        return False, "a quantidade de caracteres inseridos ultrapassa o limite de 100"
    if not bool(re.match("^[A-Za-z0-9./:]*$", value)):
        return False, "foi inserido um caractere invalido"

    return True, value


if __name__ == "__main__":
    data = literal_eval(sys.argv[1])
    response = sanitize(data)
    print(response)