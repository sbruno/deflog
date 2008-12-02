# -*- coding: utf-8 -*-
#*********************************************************
#* DeFlog 2008-11-02                                     *
#* Traduce Fotolog/SMS a español                         *
#* http://www.santiagobruno.com.ar/programas.html#deflog *
#* Licencia: GPL v3                                      *
#********************************************************/

import re

def dessimbolizar(word):
    word = word.replace('@', 'a')
    word = word.replace('ª', 'a')
    word = word.replace('º', 'o')
    word = word.replace(' = ', ' igual ')
    word = re.sub(r"(\w*?)!(\w)", r"\1i\2", word)
    word = re.sub(r"(\w+?)¡", r"\1i", word)
    return word

def deleet(word):
    if not re.match(r"\b\d+\b", word):
        word = word.replace('0','o')
        word = word.replace('1','i')
        word = word.replace('3','e')
        word = word.replace('4','a')
        word = word.replace('5','s')
        word = word.replace('7','t')
    return word

def desalternar(word):
    """
    Convierte palabras con mayusculas y minusculas alternadas a minusculas
    
    >>> desalternar("hola")
    'hola'
    >>> desalternar("Hola")
    'Hola'
    >>> desalternar("HOLA")
    'HOLA'
    >>> desalternar("HoLa")
    'hola'
    >>> desalternar("hOlA")
    'hola'
    """
    
    if word.isupper() or word.islower() or word.istitle():
        return word
    else:
        return word.lower()


def desmultiplicar(word):
    """
    Elimina las repeticiones de letras
    
    >>> desmultiplicar("hola")
    'hola'
    >>> desmultiplicar("holaaaaaaa")
    'hola'
    >>> desmultiplicar("holaa")
    'hola'
    >>> desmultiplicar("hhhhoooooollllaaaaa")
    'hola'
    >>> desmultiplicar("millones")
    'millones'
    >>> desmultiplicar("aburrido")
    'aburrido'
    >>> desmultiplicar("www")
    'www'
    """

    exceptions = ['http','www','://', 'ss', 'ppio', 'ff', 'bb', 'kiss']

    lword = word.lower()

    if re.match(r"^bs[s]+$",lword):
        return 'besos'

    if re.match(r"^mm[m]+[h]*$",lword):
        return 'mmmh'

    if re.match(r"^aa[a]+[h]*$",lword):
        return 'aaah'

    if re.match(r"^ba[a]+[h]*$",lword):
        return 'baaah'

    if re.match(r"^bu[u]+[h]*$",lword):
        return 'buuu'
    
    if not lword in exceptions and lword[:3] != '...' :
        if re.match(r"(^|[^l]+)[l][l]([^l])+",lword):
            pos = lword.index('ll')
            return desmultiplicar(lword[:pos]) + 'll' + desmultiplicar(lword[pos+2:])

        if re.match(r"([^r])+[r][r]([^r])+",lword):
            pos = lword.index('rr')
            return desmultiplicar(lword[:pos]) + 'rr' + desmultiplicar(lword[pos+2:])

        ##Los dos casos siguientes se pueden sacar si no se esperan muchas
        ##palabras en inglés. Sirve para pasar google, good, teen, etc
        if re.match(r"([^o])+[o][o]([^o])+",lword):
            pos = lword.index('oo')
            return desmultiplicar(lword[:pos]) + 'oo' + desmultiplicar(lword[pos+2:])
        
        if re.match(r"([^e])+[e][e]([^e])+",lword):
            pos = lword.index('ee')
            return desmultiplicar(lword[:pos]) + 'ee' + desmultiplicar(lword[pos+2:])

        return re.sub(r'(.)\1+',r'\1',word)
    else:
        return word;
    
    
    
def desms(word):
    """
    Reemplaza algunas abreviaturas tipicas del sms
    >>> desms('porke')
    'porque'
    >>> desms('pq')
    'porque'
    >>> desms('xq')
    'porque'
    >>> desms('porqe')
    'porque'
    """
    
    translations = {'+': 'm&aacute;s',
                    '+a': 'masa',
                    'ad+': 'adem&aacute;s',
                    'ak': 'ac&aacute;',
                    'asc': 'al salir de clase',
                    'asdc': 'al salir de clase',
                    'bb': 'beb&eacute;',
                    'bld': 'boludo',
                    'blds': 'boludos',
                    'bn': 'bien',
                    'bno': 'bueno',
                    'bss': 'besos',
                    'c': 'se',
                    'cdo': 'cuando',
                    'cel': 'celular',
                    'clp': 'chupame la pija',
                    'cmo': 'como',
                    'd': 'de',
                    'dle': 'dale',
                    'dnd': 'donde',
                    'dsd': 'desde',
                    'dsp': 'despu&eacute;s',
                    'flia': 'familia',
                    'fto': 'foto',
                    'hdp': 'hijo de puta',
                    'hexo': 'hecho',
                    'hlqp': 'hacemos lo que podemos',
                    'hna': 'hermana',
                    'hno': 'hermano',
                    'hsta': 'hasta',
                    'k': 'que',
                    'kpo': 'capo',
                    'ksa': 'casa',
                    'lpm': 'la puta madre',
                    'lpmqtp': 'la puta madre que te pari&oacute;',
                    'lpqtp': 'la puta que te pari&oacute;',
                    'm': 'me',
                    'mjor': 'mejor',
                    'mjr': 'mejor',
                    'msj': 'mensaje',
                    'n': 'en',
                    'nd': 'nada',
                    'nxe': 'noche',
                    'ppio': 'principio',
                    'pq': 'porque',
                    'ps': 'pues',
                    'pso': 'paso',
                    'pt': 'pete',
                    'q': 'que',
                    'qn': 'quien',
                    'salu2': 'saludos',
                    'ss': 'sos',
                    'sta': 'est&aacute;',
                    'stan': 'est&aacute;n',
                    'stamos': 'estamos',
                    'stes': 'est&eacute;s',
                    't': 'te',
                    'tas': 'est&aacute;s',
                    'tb': 'tambi&eacute;n',
                    'tbj': 'trabajo',
                    'tbn': 'tambi&eacute;n',
                    'tdo': 'todo',
                    'tdos': 'todos',
                    'tds': 'todos',
                    'tgo': 'tengo',
                    'tkm': 'te quiero mucho',
                    'tmb': 'tambi&eacute;n',
                    'tmbn': 'tambi&eacute;n',
                    'tmp': 'tampoco',
                    'tngo': 'tengo',
                    'tp': 'tampoco',
                    'toy': 'estoy',
                    'tk': 'te quiero',
                    'tq': 'te quiero',
                    'vac': 'vacaciones',
                    'vr': 'ver',
                    'x': 'por',
                    'xa': 'para',
                    'xat': 'chat',
                    'xk': 'porque',
                    'xke': 'porque',
                    'xo': 'pero',
                    'xq': 'porque',
                    'xqe': 'porque'
                    }

    if word.lower() in translations:
        return translations[word.lower()]
    else:
        lword = word.lower()
        if 'qe' in lword or 'ke' in lword or 'qi' in lword:
            lword = lword.replace('qi', 'qui')
            lword = lword.replace('qe', 'que')
            lword = lword.replace('ke', 'que')
            word = lword
        if lword.endswith('q') and len(lword) > 2:
            lword = lword[:-1] + " que"
            word = lword
        if lword.endswith('ms') and len(lword) > 3:
            lword = lword[:-1] + "os"
            word = lword
        if lword.startswith('cn'):
            lword = "co" + lword[1:]
            word = lword
        if lword.startswith('bso'):
            lword = "be" + lword[1:]
            word = lword
        if lword.startswith('bld'):
            lword = "bolu" + lword[2:]
            word = lword
        if lword.startswith('efea') and len(lword) > 3:
            lword = "agrega" + lword[4:] + " a favoritos"
            word = lword
        if lword.startswith('efen') and len(lword) > 3:
            lword = "agreguen" + lword[4:] + " a favoritos"
            word = lword
        if lword.startswith('mux') and len(lword) > 3:
            lword = "much" + lword[3:]
            word = lword
        
        return word

def desestupidizar(word):
    translations = {'10pre': 'siempre',
                    'arre': '&lt;alguna sensaci&oacute;n&gt;',
                    'ahrre': '&lt;alguna sensaci&oacute;n&gt;',
                    'ahre': '&lt;alguna sensaci&oacute;n&gt;',
                    'ai': 'ah&iacute;/hay/ay',
                    'aios': 'adi&oacute;s',
                    'aka': 'ac&aacute;',
                    'aki': 'aqu&iacute;',
                    'akí': 'aqu&iacute;',
                    'anio': 'a&ntilde;o',
                    'bai': 'bye',
                    'ben': 'bien',
                    'bem': 'bien',
                    'bue': 'bueno',
                    'bzo': 'beso',
                    'doi': 'doy',
                    'efe': 'favorito',
                    'efeo': 'agrego a mis favoritos',
                    'efen': 'agreguen a favoritos',
                    'efes': 'favoritos',
                    'efs': 'favoritos',
                    'estoi': 'estoy',
                    'ff': 'favoritos',
                    'fs': 'favoritos',
                    'grax': 'gracias',
                    'groxo': 'grosso',
                    'hai': 'hay',
                    'hoi': 'hoy',
                    'i': 'y',
                    'ia': 'ya',
                    'io': 'yo',
                    'ise': 'hice',
                    'iwal': 'igual',
                    'kmo': 'como',
                    'kn': 'con',
                    'oi': 'hoy',
                    'moy': 'muy',
                    'muchio': 'mucho',
                    'mu': 'muy',
                    'mui': 'muy',
                    'nah': 'nada',
                    'nuche': 'no se',
                    'nus': 'nos',
                    'nuse': 'no se',
                    'ola': 'hola',
                    'olas': 'hola',
                    'olaz': 'hola',
                    'pic': 'foto',
                    'pick': 'foto',
                    'pik': 'foto',
                    'plis': 'por favor',
                    'pliz': 'por favor',
                    'plz': 'por favor',
                    'sho': 'yo',
                    'sip': 'si',
                    'soi': 'soy',
                    'stoi': 'estoy',
                    'sullo': 'suyo',
                    'ta': 'est&aacute;',
                    'tawena': 'est&aacute; buena',
                    'tap': 'top',
                    'taz': 'est&aacute;s',
                    'teno': 'tengo',
                    'toi': 'estoy',
                    'toos': 'todos',
                    'tullo': 'tuyo',
                    'lav': 'love',
                    'lov': 'love',
                    'lendo': 'lindo',
                    'llendo': 'yendo',
                    'mua': 'besos',
                    'muak': 'besos',
                    'muac': 'besos',
                    'muack': 'besos',
                    'muto': 'mucho',
                    'nah': 'nada',
                    'nu': 'no',
                    'nueo': 'nuevo',
                    'nunk': 'nunca',
                    'nuc': 'no se',
                    'voi': 'voy',
                    'we': 'bueno',
                    'wem': 'bueno',
                    'wno': 'bueno',
                    'xau': 'chau',
                    'xfa': 'por favor'
                   }

    if word.lower() in translations:
        return translations[word.lower()]
    else:
        lword = word.lower()
        if 'emd' in lword:
            word = lword.replace('emd', 'ind')
        if 'md' in lword:
            word = lword.replace('md', 'nd')
        if re.match(r'^[i]+$',lword):
            word = 'y'
        if len(lword) > 2 and lword[:3] == 'wen':
            word = "buen" + lword[3:]
        if len(lword) > 2 and lword[:3] == 'oka':
            word = "ok"

        #posible risa
        if len(lword) > 6:
            if re.match(r"^((j|a|k)+)$",lword):
                return "jajaja"
            elif len(lword) > 8 and re.match("^((j|a|k|h|l|s|d|ñ)+)j((j|a|k|h|l|s|d|ñ)+)j((j|a|k|h|l|s|d|ñ)*)$",lword):
                return "jajaja"

        return word

def desk(word):
    exceptions = ['kiosco', 'kilo', 'kiló', 'fuck', 'punk', 'rock', 'look', 'kiss']
    vocales = ['a', 'e', 'i', 'o','u']

    lword = word.lower()

    if lword == 'ok':
        return word
    
    for a in exceptions:
        if a in lword:
            return word
    
    if "ki" in lword:
        word = word.lower().replace('ki', 'qui')
    
    if "ke" in word:
        word = word.lower().replace('ke', 'que')

    if len(word) > 2 and word[0].lower() == 'k' and word[1].lower() not in vocales:
        word = "ka" + word[1:].lower()
    
    word = word.replace('k','c')
    word = word.replace('K','C')
    return word


def desporteniar(word):
    lword = word.lower()
    if len(lword) > 5 and lword[-4:] == 'stes':
        word = lword[:-1]
    return word


def deszezear(word):
    exceptions = ['arroz', 'feliz', 'zorr', 'azul', 'azucar', 'azúcar', 'conoz', 'zapa']

    lword = word.lower()
    
    for a in exceptions:
        if a in lword:
            return word
    
    word = word.replace('z','s')
    word = word.replace('Z','S')
    return word


def fixmissingvowels(word):
    exceptions = ['get', 'cat', 'that', 'best', 'post', 'net', 'chat']
    vocales = ['a', 'e', 'i', 'o','u']
    followsd = ['a', 'e', 'i', 'o','u', 'r', 'h', 'y']

    lword = word.lower()
    if not lword in exceptions:
        if len(lword) > 1 and lword[0] == 'n' and not lword[1] in vocales:
            lword = "en" + lword[1:]
            word = lword
        
        wlen = len(word)
        if wlen > 1 and lword[wlen-1] == 't':
            lword += 'e'
            word = lword
        
        if len(lword) > 2 and lword[:2] == "vr" and not lword[2] in vocales:
            lword = "ver" + lword[2:]
            word = lword

        if len(lword) > 2 and lword[0] == 'd' and not lword[1] in followsd:
            lword = "de" + lword[1:]
            word = lword

        if len(lword) > 2 and lword[:2] == "sp" and not lword[2] in vocales:
            lword = "esp" + lword[2:]
            word = lword

        if len(lword) > 2 and lword[:2] == "st" and not lword[2] in vocales:
            lword = "est" + lword[2:]
            word = lword

    return word
