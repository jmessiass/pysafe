# Python Safe Input

Esse projeto visa tratar os dados de entrada digitados pelo usuário, com a ideia de não permitir scripts maliciosos digitados em campos de formulário.


## Exemplo de uso

```console
$ python3 safe_input.py "{'value': 'PAYLOAD'}"
```

Dentro de payload deverá ser inserido o dado que é digitado pelo usuário.

### Caracteres permitidos:

+ Alfanuméricos;
+ Os seguintes caracteres **.** **/** **:**

Se retornar **True** o dado de entrada é seguro, se retornar **False** o dado é inseguro, e é retornado a mensagem de erro.

<hr>

## Contribuidores

- Ítalo Pinto @italopinto
- Raphael Fleury @raphael-fleury