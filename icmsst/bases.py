"""
§ 1° Os percentuais de Margem de Valor Agregado - MVA constantes nas tabelas referidas no caput
deste artigo serão utilizados, exclusivamente, por estabelecimentos enquadrados, alternativamente,
como: (Nova redação dada ao § 1º pela Port. 215/19, efeitos a partir de 1°.01.2020)
I - optantes pelo benefício fiscal de crédito outorgado, previsto no inciso I e na alínea a do inciso II
do artigo 2° do Anexo XVII do Regulamento do ICMS, aprovado pelo Decreto n° 2.212, de 20 de março de 2014;
II - optantes pelo tratamento diferenciado e favorecido previsto na Lei Complementar (federal) n° 123/2006 - Simples Nacional.
"""

# REGRA ACIMA
ENQUADRAMENTO = {
    'OBFCO':'optantes pelo benefício fiscal de crédito outorgado',
    'OTDSN':'optantes pelo tratamento diferenciado e favorecido'
    +'previsto na Lei Complementar (federal) n° 123/2006 - Simples Nacional',
    'OROST': 'optante pelo benefício fiscal de crédito outorgado de que trata a'
    +'alínea a do inciso II do artigo 2° do Anexo XVII do Regulamento do ICMS mato-grossense',
    'CST': 'for credenciado como substituto tributário',
    }

"""
§ 2° A utilização da Margem de Valor Agregado - MVA, em relação às aquisições interestaduais de bens
e mercadorias para revenda, nos termos deste artigo, limita o valor do imposto a ser utilizado como
crédito a 7% (sete por cento) do valor da operação, conforme disposto no inciso I do § 2° do artigo
2° do Anexo XVII do RICMS, desde que não superior ao valor destacado no correspondente documento fiscal.
(Redação dada pela Port. 208/19, que alterou a íntegra do art. 1º, efeitos a partir de 1°.01.20)
"""

# REGRA ACIMA
LIMITES = {
    'OBFCO': 7,
    'OTDSN': 7,
    'ATACADISTA': 7,
}

"""
§ 3° O limite do crédito a 7% (sete por cento), conforme definido § 2° deste artigo, não se aplica
às aquisições interestaduais de bens e mercadorias enquadradas nos itens das tabelas divulgadas no
Anexo Único desta portaria, arrolados nos incisos deste parágrafo, cujo percentual da MVA foi fixado
sem dedução de crédito outorgado: (Redação dada ao artigo pela Port. 208/19,

§ 4° Nas hipóteses arroladas no § 3° deste artigo, será respeitado como limite do crédito o valor do
imposto destacado na Nota Fiscal, exceto quando a saída subsequente for amparada por benefício fiscal
que implique vedação de crédito ou exija o estorno proporcional do crédito. (redação dada ao artigo
pela Port. 208/19, que alterou a íntegra do art. 1º, efeitos a partir de 1°.01.2020)

§ 5° O disposto nos §§ 3° e 4° deste artigo aplica-se, ainda, na hipótese prevista no inciso II do § 1°
também deste artigo. (Acrescentado o § 5º pela Port. 215/19, efeitos a partir de 1°.01.20)
"""

# REGRA ACIMA
ITEMS_PERMITIDOS_CREDITO_TOTAL = {

    'I': {'92.0': True},
    'I': {'93.0': True},
    'I': {'94.0': True},
    'I': {'95.0': True},
    'II': {"*": True},
    'III': {"*": True},
    '19.1': {'V': True},
    '1.0': {'XVII': True},
}

"""
Art. 2°-A Os contribuintes, estabelecidos no território mato-grossense, inscritos no Cadastro de Contribuintes do ICMS,
cuja atividade econômica principal esteja enquadrada na Classificação Nacional de Atividades Econômicas - CNAE como
estabelecimento comercial atacadista, para fins de definição da base de cálculo do imposto devido por substituição tributária,
nas operações com mercadorias constantes das tabelas I a XIX do Anexo Único desta portaria, ficam autorizados a aplicarem a
redução de 50% (cinquenta por cento) sobre o respectivo percentual de Margem de Valor Agregado - MVA fixado na tabela pertinente.
(Acrescentado pela Port. 208/19, efeitos a partir de 1°.01.2020)
"""
# REGRA ACIMA
EMPRESA_ATACADISTA = {
    'reduz_aliquota': lambda x: True if str(x).startswith('46') else False
}

"""
Art. 2°-B Ficam divulgados os percentuais de Margem de Valor Agregado - MVA a serem utilizados nas operações destinadas a contribuintes inscritos
no Cadastro de Contribuintes do ICMS, que não forem optantes pelo benefício fiscal de crédito outorgado, constante do inciso I e da alínea a do
inciso II do artigo 2° do Anexo XVII do RICMS/2014, ou que não forem contemplados com o referido benefício ou, ainda, cuja utilização do referido
benefício fiscal seja vedada pela Lei Complementar n° 631/2019: (Acrescentado pela Port. 208/19, efeitos a partir de 1°.01.2020)
"""

# REGRA ACIMA

MVA_CHEIO = {
'I': lambda x: '65,29' if int(x) >= 100100 and int(x) <= 199900 else False,
'II': lambda x: '67,49' if int(x) >= 200100 and int(x) <= 299900 else False,
'III': lambda x: '73,63' if int(x) >= 300100 and int(x) <= 302500 else False,
'IV': lambda x: '29,94' if int(x) >= 500100 and int(x) <= 500100 else False,
'V': lambda x: '55,61' if int(x) >= 800100 and int(x) <= 801900 else '55,61' if int(x) >= 802000 and int(x) <= 802300 else False,
'VI': lambda x: '65,29' if int(x) >= 801901 and int(x) <= 801901 else False,
'VII': lambda x: '83,24' if int(x) >= 900100 and int(x) <= 900200 else False,
'VIII': lambda x: '108,84' if int(x) >= 900300 and int(x) <= 900400 else False,
'IX': lambda x: '64,06' if int(x) >= 900500 and int(x) <= 900500 else False,
'X': lambda x: '74,75' if int(x) >= 1000100 and int(x) <= 1008000 else False,
'XI': lambda x: '75,80' if int(x) >= 1100100 and int(x) <= 1101200 else False,
'XII': lambda x: '63,28' if int(x) >= 1200100 and int(x) <= 1200900 else False,
'XII-A': lambda x: '60,35' if int(x) >= 1300100 and int(x) <= 1301600 else False,
'XIII': lambda x: '66,52' if int(x) >= 1400100 and int(x) <= 1401300 else False,
'XIV': lambda x: '78,79' if int(x) >= 1600100 and int(x) <= 1600900 else False,
'XV': lambda x: '59,75' if int(x) >= 1700100 and int(x) <= 1711700 else False,
'XVI': lambda x: '73,90' if int(x) >= 1900100 and int(x) <= 1903300 else False,
'XVII': lambda x: '75,80' if int(x) >= 2000100 and int(x) <= 2006500 else False,
'XVIII': lambda x: '53,86' if int(x) >= 2100100 and int(x) <= 2112600 else False,
'XIX': lambda x: '68,57' if int(x) >= 2200100 and int(x) <= 2200100 else False,
'XX': lambda x: '61,78' if int(x) >= 2300100 and int(x) <= 2300200 else False,
'XXI': lambda x: '72,12' if int(x) >= 2400100 and int(x) <= 2400300 else False,
'XXII': lambda x: '94,70' if int(x) >= 400100 and int(x) <= 400200 else False,
}

"""
Art. 2°-C Nas operações com produtos listados na tabela NCM, identificados como Bens de Informática e Telecomunicações, destinados
a contribuintes inscritos no Cadastro de Contribuintes do ICMS, não compreendidas nos artigos 1° e 2°-B desta portaria, o percentual
de Margem de Valor Agregado - MVA a ser utilizado será de 53,86%. (Acrescentado pela Port. 200/2020)
"""
# REGRA ACIMA

BEM_DE_INFORMATICA_OU_TELECOMUNICACAO = '53,86'