import re

class ExtratorUrl:
    def __init__(self,url):
        self.url = self.limpa_url(url)
        self.valida_url()
    
    def limpa_url(self,url):
        if type(url) == str:
            return url.strip()
        else:
            return ""    
        

    def valida_url(self):
        if not bool(self.url):
            raise ValueError("A Url esta vazia")
        
        padrao_url = re.compile("(http(s)?://)?(www.)?bytebank.com(.br)?/cambio")
        match = padrao_url.match(self.url)

        if not match:
            raise ValueError("A URL não é valida")

        print ("A URL é valida!")
    
    def get_url_base(self):
        indice_interrogacao = self.url.find("?")
        url_base = self.url[:indice_interrogacao]
        return url_base

    def get_url_parametros(self):
        indice_interrogacao = self.url.find("?")
        url_parametros = self.url[indice_interrogacao+1:]
        return url_parametros
    
    def get_valor_parametros(self, parametro_busca):
        indice_parametro = self.get_url_parametros().find(parametro_busca)
        indice_valor = indice_parametro + len(parametro_busca)+1
        indice_e_comercial = self.get_url_parametros().find("&", indice_valor)
        if indice_e_comercial == -1:
            valor = self.get_url_parametros()[indice_valor:]
        else:
            valor = self.get_url_parametros()[indice_valor:indice_e_comercial]
        return valor





extrator_url = ExtratorUrl("bytebank.com/cambio?quantidade=100&moedaOrigem=real&moedaDestino=real")
valor_quantidade = extrator_url.get_valor_parametros("quantidade")
print(valor_quantidade)