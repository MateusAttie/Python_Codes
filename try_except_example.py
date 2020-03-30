import zipfile

"""Tratamento de Exceções"""

try:
    banco_zip = zipfile.ZipFile("saida.zip")
    banco_zip.extractall(path="banco")
    banco_zip.close()
except FileNotFoundError:
    print ("Arquivo Inexistente")
except PermissionError as pme:
    print("Erro de permissão")


""" Podemos garantir a execução de alguma linha desejada da seguinte maneira"""

try:
    banco_zip = zipfile.ZipFile("saida.zip")
except (FileNotFoundError, PermissionError):
    print("Erro ao abrir o arquivo")
else:
    banco_zip.extractall(path="banco")

""" Ações de limpeza se baseiam em executar comandos mesmo após o tratamento da exception """

banco_zip = None

try:
    banco_zip = zipfile.ZipFile("saida.zip")
    banco_zip.extractall(path="banco")
except PermissionError:
    print("Erro de permissão ao abrir o arquivo")
finally;
    banco_zip.close()

"""Invocando uma exception (Raise)"""

def validate_kind(kind):
    if not kind in ('bigint', 'numeric', 'varchar'):
        raise Exception("Tipo Inválido")
