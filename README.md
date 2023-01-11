# Python Safe Input

Esse projeto visa tratar os dados de entrada digitados pelo usuário, com a ideia de não permitir a injeção de comandos maliciosos digitados em campos de formulário.
## Exemplos de uso
Se a resposta for **True** o dado de entrada é seguro, se retornar **False** o dado é inseguro, e é retornado a mensagem de erro.
### String
```console
$ python3 safe_input.py "'PayloadDoBem'"
(True, 'PayloadDoBem')

$ python3 safe_input.py "'<script>alert(1)</script>'"
(False, 'foi inserido um caractere invalido')
```
### Array
```console
$ python3 safe_input.py "['PayloadDoBem']"
(True, ['PayloadDoBem'])

$ python3 safe_input.py "['<script>alert(1)</script>']"
(False, ['foi inserido um caractere invalido'])
```
### Objeto
```console
$ python3 safe_input.py "{'value': 'PayloadDoBem'}"
(True, {'value': 'PayloadDoBem'})

$ python3 safe_input.py "{'value': '<script>alert(1)</script>'}"
(False, {'value': 'foi inserido um caractere invalido'})
```
### Array dentro de objeto
```console
$ python3 safe_input.py "{'value':['PayloadDoBem']}"
(True, {'value': ['PayloadDoBem']})

$ python3 safe_input.py "{'value':['<script>alert(1)</script>']}"
(False, {'value': ['foi inserido um caractere invalido']})
```

Dentro de payload deverá ser inserido o dado que é digitado pelo usuário.

### Caracteres permitidos:

+ Alfanuméricos;
+ Os seguintes caracteres **.** **/** **:**
  
Se quiser editar a regra da validação dos dados, pode editar a expressão regular na linha 55.

### Adicionando 'espaço' a regra de caracteres seguros
Adicionar '\s' na regex:
```console
55    if not bool(re.match("^[A-Za-z0-9./:\s]*$", value)):
```

<hr>

## Contribuidores

<a href="https://github.com/jmessiass/python_safe_input/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=jmessiass/python_safe_input"/>
</a>
