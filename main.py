# Terá função principal de gerar string com link padrão

from os import link


def generate_link(country: int, number: int, message: str) -> str:
    ddi = country
    message = message.replace(" ", "%20")
    link = f"https://wa.me/{ddi}{number}?text={message}"
    return link


pais = 55
numero = 31991691477
mensagem = "Olá tudo bem?"

link_criado = generate_link(pais, numero, mensagem)
print(link_criado)