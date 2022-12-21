#! /usr/bin/python3
from ast import literal_eval
import html
import sys
import re


def sanitize_input(param):
    try:
        secure_data = {}
        status_data = False
        data = dict(literal_eval(param)) # DEV
        # data = dict(param) # PROD

        for key in data:
            input_data = data[key]  # ATRIBUI O VALOR DIGITADO PARA A VAR INPUT

            if isinstance(input_data, list):
                new_input_list = []
                for data in input_data:
                    safe_code = escape_input(data)
                    status_data, secure_input = safe_code_verifier(safe_code, key)
                    if not status_data:
                        return status_data, secure_input
                    new_input_list.append(secure_input[key])

                secure_data.update({key: new_input_list})

            else:
                safe_code = escape_input(input_data)
                status_data, secure_input = safe_code_verifier(safe_code, key)
                secure_data.update(secure_input)

        return status_data, secure_data

    except Exception as error:
        secure_data.update({"error": error})
        return False, secure_data


# ENCODA CARACTERES DE TAG HTML
def escape_input(data_input):
    return data_input if isinstance(data_input, int) else html.escape(data_input)


def safe_code_verifier(safe_code, dict_key):
    safe_input = str(safe_code)
    secure_data = {dict_key: safe_input}
    status_data = True

    if len(safe_input) > 100:  # SE A QUANTIDADE DE CARACTERES INSERIDOS FOR MAIOR QUE 100, RETORNA FALSO E MENSAGEM DE ERRO
        secure_data.update({dict_key: "a quantidade de caracteres inseridos ultrapassa o limite de 100"})
        status_data = False

    # VALIDA SE FOI DIGITADO APENAS LETRAS NUMEROS E . : /
    if not bool(re.match("^[A-Za-z0-9./:]*$", safe_input)):
        secure_data.update({dict_key: "foi inserido um caractere invalido"})
        status_data = False

    return status_data, secure_data


if __name__ == "__main__":
    response = sanitize_input(sys.argv[1])
    print(response)