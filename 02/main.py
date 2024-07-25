def eh_palindromo(texto):
    """
    Fun��o que verifica se uma string � um pal�ndromo.
    
    Um pal�ndromo � uma palavra ou frase que � lida da mesma forma de frente para tr�s e vice-versa,
    desconsiderando espa�os, pontua��es e diferen�as entre mai�sculas e min�sculas.
    
    Par�metros:
    texto (str): A string que ser� verificada.
    
    Retorna:
    bool: Retorna True se o texto for um pal�ndromo, caso contr�rio, False.
    """
    # Converter o texto para min�sculas e remover caracteres n�o alfanum�ricos
    texto_limpo = ''.join(c for c in texto.lower() if c.isalnum())
    
    # Verificar se o texto limpo � igual ao seu reverso
    return texto_limpo == texto_limpo[::-1]

# Exemplos de uso
print(eh_palindromo("Ol� mundo!"))  # Deve retornar False
print(eh_palindromo("Socorram-me, subi no �nibus em Marrocos!"))  # Deve retornar True
