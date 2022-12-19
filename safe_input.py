#! /usr/bin/python3
from ast import literal_eval
import html
import sys
import re

def sanitize_input(param):
    secure_data = {}
    status_data = False
    data = dict(literal_eval(param)) # DEV
    # data = dict(param) # PROD

    for key in data:
        input = data[key] # ATRIBUI O VALOR DIGITADO PARA A VAR INPUT
        safe_code1 = html.escape(input) if type(input) != int else input # ENCODA CARACTERES DE TAG HTML
        safe_code2 = str(safe_code1) # FORCA O VALOR SER UMA STRING

        if len(safe_code2) > 100: # SE A QUANTIDADE DE CARACTERES INSERIDOS FOR MAIOR QUE 100, RETORNA FALSO E MENSAGEM DE ERRO
            secure_data.update({key: "a quantidade de caracteres inseridos ultrapassa o limite de 100"})
            status_data = False
            return status_data, secure_data

        # VALIDA SE FOI DIGITADO APENAS LETRAS NUMEROS E . : /
        if not bool(re.match("^[A-Za-z0-9./:]*$", safe_code2)):
                # import ipdb;ipdb.set_trace()
                secure_data.update({key: "foi inserido um caractere invalido"})
                status_data = False
                return status_data, secure_data

        secure_data.update({key: safe_code2})  # ATUALIZA DICIONARIO COM OS DADOS TRATADOS
        status_data = True

    return status_data, secure_data

if __name__ == "__main__":
    response = sanitize_input(sys.argv[1])
    print(response)