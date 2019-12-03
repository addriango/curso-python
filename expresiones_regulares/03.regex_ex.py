import re

lista_urls=[
    'https://pildorasinformaticas.es',
    'ftp://pildorasinformaticas.com',
    'https://pildorasinformaticas.com',
    'ftp://pildorasinformaticas.es',
]

#busca urls que termien en .es
for elemento in lista_urls:
    if re.findall('.es$',elemento):
        print(elemento)

print('')
#urls que comiencen por http
for elemento in lista_urls:
    if re.findall('^http',elemento):
        print(elemento)