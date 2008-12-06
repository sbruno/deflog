# -*- coding: utf-8 -*-
#*********************************************************
#* DeFlog 2008-11-02                                     *
#* Traduce Fotolog/SMS a español                         *
#* http://www.santiagobruno.com.ar/programas.html#deflog *
#* Licencia: GPL v3                                      *
#********************************************************/

import re
from htmlentitydefs import name2codepoint 

#<code from http://www.gossamer-threads.com/lists/python/python/623437>
EntityPattern = re.compile(u'&(?:#(\d+)|(?:#x([\da-fA-F]+))|([a-zA-Z]+));')

def decodeEntities(s, encoding='utf-8'):
    def unescape(match):
        code = match.group(1)
        if code:
            return unichr(int(code, 10))
        else:
            code = match.group(2)
        if code:
            return unichr(int(code, 16))
        else:
            code = match.group(3)
        if code in name2codepoint:
            return unichr(name2codepoint[code])
        return match.group(0)

    return EntityPattern.sub(unescape, s) 
#</code from http://www.gossamer-threads.com/lists/python/python/623437>


def dessimbolizar(word, format='html'):
    word = word.replace(u'@', u'a')
    word = word.replace(u'ª', u'a')
    word = word.replace(u'º', u'o')
    word = word.replace(u' = ', u' igual ')
    word = re.sub(r"(\w*?)!(\w)", r"\1i\2", word)
    word = re.sub(r"(\w+?)¡", r"\1i", word)
    return word

def deleet(word, format='html'):
    if not re.match(r"\b\d+\b", word):
        word = word.replace(u'0',u'o')
        word = word.replace(u'1',u'i')
        word = word.replace(u'3',u'e')
        word = word.replace(u'4',u'a')
        word = word.replace(u'5',u's')
        word = word.replace(u'7',u't')
    return word

def desalternar(word, format='html'):
    """
    Convierte palabras con mayusculas y minusculas alternadas a minusculas
    
    >>> desalternar(u"hola")
    u'hola'
    >>> desalternar(u"Hola")
    u'Hola'
    >>> desalternar(u"HOLA")
    u'HOLA'
    >>> desalternar(u"HoLa")
    u'hola'
    >>> desalternar(u"hOlA")
    u'hola'
    """
    
    if word.isupper() or word.islower() or word.istitle():
        return word
    else:
        return word.lower()


def desmultiplicar(word, format='html'):
    """
    Elimina las repeticiones de letras
    
    >>> desmultiplicar(u"hola")
    u'hola'
    >>> desmultiplicar(u"holaaaaaaa")
    u'hola'
    >>> desmultiplicar(u"holaa")
    u'hola'
    >>> desmultiplicar(u"hhhhoooooollllaaaaa")
    u'hola'
    >>> desmultiplicar(u"millones")
    u'millones'
    >>> desmultiplicar(u"aburrido")
    u'aburrido'
    >>> desmultiplicar(u"www")
    u'www'
    """

    exceptions = [u'http',u'www',u'://', u'ss', u'ppio', u'ff', u'bb', u'kiss']

    lword = word.lower()

    if re.match(r"^bs[s]+$",lword):
        return u'besos'

    if re.match(r"^mm[m]+[h]*$",lword):
        return u'mmmh'

    if re.match(r"^aa[a]+[h]*$",lword):
        return u'aaah'

    if re.match(r"^ba[a]+[h]*$",lword):
        return u'baaah'

    if re.match(r"^bu[u]+[h]*$",lword):
        return u'buuu'
    
    if not lword in exceptions and lword[:3] != u'...' :
        if re.match(r"(^|[^l]+)[l][l]([^l])+",lword):
            pos = lword.index(u'll')
            return desmultiplicar(lword[:pos]) + u'll' + desmultiplicar(lword[pos+2:])

        if re.match(r"([^r])+[r][r]([^r])+",lword):
            pos = lword.index(u'rr')
            return desmultiplicar(lword[:pos]) + u'rr' + desmultiplicar(lword[pos+2:])

        ##Los dos casos siguientes se pueden sacar si no se esperan muchas
        ##palabras en inglés. Sirve para pasar google, good, teen, etc
        if re.match(r"([^o])+[o][o]([^o])+",lword):
            pos = lword.index(u'oo')
            return desmultiplicar(lword[:pos]) + u'oo' + desmultiplicar(lword[pos+2:])
        
        if re.match(r"([^e])+[e][e]([^e])+",lword):
            pos = lword.index(u'ee')
            return desmultiplicar(lword[:pos]) + u'ee' + desmultiplicar(lword[pos+2:])

        return re.sub(r'(.)\1+',r'\1',word)
    else:
        return word;
    
    
    
def desms(word, format='html'):
    """
    Reemplaza algunas abreviaturas tipicas del sms
    Con el formato plain, reemplaza las entidades html

    >>> desms(u'porke')
    u'porque'
    >>> desms(u'pq')
    u'porque'
    >>> desms(u'xq')
    u'porque'
    >>> desms(u'porqe')
    u'porque'
    >>> desms(u'ak')
    u'ac&aacute;'
    >>> desms(u'ak', format='html')
    u'ac&aacute;'
    >>> #no se como hacer que pase sin hacer esta cosa
    >>> print desms(u'ak', format='plain').encode('utf-8')
    ac\xc3\xa1
    """
    
    translations = {u'+': u'm&aacute;s',
                    u'+a': u'masa',
                    u'ad+': u'adem&aacute;s',
                    u'ak': u'ac&aacute;',
                    u'asc': u'al salir de clase',
                    u'asdc': u'al salir de clase',
                    u'bb': u'beb&eacute;',
                    u'bld': u'boludo',
                    u'blds': u'boludos',
                    u'bn': u'bien',
                    u'bno': u'bueno',
                    u'bss': u'besos',
                    u'c': u'se',
                    u'cdo': u'cuando',
                    u'cel': u'celular',
                    u'clp': u'chupame la pija',
                    u'cmo': u'como',
                    u'd': u'de',
                    u'dle': u'dale',
                    u'dnd': u'donde',
                    u'dsd': u'desde',
                    u'dsp': u'despu&eacute;s',
                    u'flia': u'familia',
                    u'fto': u'foto',
                    u'hdp': u'hijo de puta',
                    u'hexo': u'hecho',
                    u'hlqp': u'hacemos lo que podemos',
                    u'hna': u'hermana',
                    u'hno': u'hermano',
                    u'hsta': u'hasta',
                    u'k': u'que',
                    u'kpo': u'capo',
                    u'ksa': u'casa',
                    u'lpm': u'la puta madre',
                    u'lpmqtp': u'la puta madre que te pari&oacute;',
                    u'lpqtp': u'la puta que te pari&oacute;',
                    u'm': u'me',
                    u'mjor': u'mejor',
                    u'mjr': u'mejor',
                    u'msj': u'mensaje',
                    u'n': u'en',
                    u'nd': u'nada',
                    u'nxe': u'noche',
                    u'ppio': u'principio',
                    u'pq': u'porque',
                    u'ps': u'pues',
                    u'pso': u'paso',
                    u'pt': u'pete',
                    u'q': u'que',
                    u'qn': u'quien',
                    u'salu2': u'saludos',
                    u'ss': u'sos',
                    u'sta': u'est&aacute;',
                    u'stan': u'est&aacute;n',
                    u'stamos': u'estamos',
                    u'stes': u'est&eacute;s',
                    u't': u'te',
                    u'tas': u'est&aacute;s',
                    u'tb': u'tambi&eacute;n',
                    u'tbj': u'trabajo',
                    u'tbn': u'tambi&eacute;n',
                    u'tdo': u'todo',
                    u'tdos': u'todos',
                    u'tds': u'todos',
                    u'tgo': u'tengo',
                    u'tkm': u'te quiero mucho',
                    u'tmb': u'tambi&eacute;n',
                    u'tmbn': u'tambi&eacute;n',
                    u'tmp': u'tampoco',
                    u'tngo': u'tengo',
                    u'tp': u'tampoco',
                    u'toy': u'estoy',
                    u'tk': u'te quiero',
                    u'tq': u'te quiero',
                    u'vac': u'vacaciones',
                    u'vr': u'ver',
                    u'x': u'por',
                    u'xa': u'para',
                    u'xat': u'chat',
                    u'xk': u'porque',
                    u'xke': u'porque',
                    u'xo': u'pero',
                    u'xq': u'porque',
                    u'xqe': u'porque'
                    }

    if word.lower() in translations:
        word = translations[word.lower()]
    else:
        lword = word.lower()
        if u'qe' in lword or u'ke' in lword or u'qi' in lword:
            lword = lword.replace(u'qi', u'qui')
            lword = lword.replace(u'qe', u'que')
            lword = lword.replace(u'ke', u'que')
            word = lword
        if lword.endswith(u'q') and len(lword) > 2:
            lword = lword[:-1] + u" que"
            word = lword
        if lword.endswith(u'ms') and len(lword) > 3:
            lword = lword[:-1] + u"os"
            word = lword
        if lword.startswith(u'cn'):
            lword = u"co" + lword[1:]
            word = lword
        if lword.startswith(u'bso'):
            lword = u"be" + lword[1:]
            word = lword
        if lword.startswith(u'bld'):
            lword = u"bolu" + lword[2:]
            word = lword
        if lword.startswith(u'efea') and len(lword) > 3:
            lword = u"agrega" + lword[4:] + u" a favoritos"
            word = lword
        if lword.startswith(u'efen') and len(lword) > 3:
            lword = u"agreguen" + lword[4:] + u" a favoritos"
            word = lword
        if lword.startswith(u'mux') and len(lword) > 3:
            lword = u"much" + lword[3:]
            word = lword

    if format == 'plain':
        word = decodeEntities(word)

    return word

def desestupidizar(word, format='html'):
    """
    Corrige algunas estupideces
    Con el formato plain, reemplaza las entidades html

    >>> desestupidizar(u'soi')
    u'soy'
    >>> desestupidizar(u'kajsklklskljasla\xf1aks')
    u'jajaja'
    >>> desestupidizar(u'taz')
    u'est&aacute;s'
    >>> desestupidizar(u'taz', format='html')
    u'est&aacute;s'
    >>> #no se como hacer que pase sin hacer esta cosa
    >>> print desestupidizar(u'taz', format='plain').encode('utf-8')
    est\xc3\xa1s
    """
    translations = {u'10pre': u'siempre',
                    u'arre': u'&lt;alguna sensaci&oacute;n&gt;',
                    u'ahrre': u'&lt;alguna sensaci&oacute;n&gt;',
                    u'ahre': u'&lt;alguna sensaci&oacute;n&gt;',
                    u'ai': u'ah&iacute;/hay/ay',
                    u'aios': u'adi&oacute;s',
                    u'aka': u'ac&aacute;',
                    u'aki': u'aqu&iacute;',
                    u'akí': u'aqu&iacute;',
                    u'anio': u'a&ntilde;o',
                    u'bai': u'bye',
                    u'ben': u'bien',
                    u'bem': u'bien',
                    u'bue': u'bueno',
                    u'bzo': u'beso',
                    u'doi': u'doy',
                    u'efe': u'favorito',
                    u'efeo': u'agrego a mis favoritos',
                    u'efen': u'agreguen a favoritos',
                    u'efes': u'favoritos',
                    u'efs': u'favoritos',
                    u'estoi': u'estoy',
                    u'ff': u'favoritos',
                    u'fs': u'favoritos',
                    u'grax': u'gracias',
                    u'groxo': u'grosso',
                    u'hai': u'hay',
                    u'hoi': u'hoy',
                    u'i': u'y',
                    u'ia': u'ya',
                    u'io': u'yo',
                    u'ise': u'hice',
                    u'iwal': u'igual',
                    u'kmo': u'como',
                    u'kn': u'con',
                    u'oi': u'hoy',
                    u'moy': u'muy',
                    u'muchio': u'mucho',
                    u'mu': u'muy',
                    u'mui': u'muy',
                    u'nah': u'nada',
                    u'nuche': u'no se',
                    u'nus': u'nos',
                    u'nuse': u'no se',
                    u'ola': u'hola',
                    u'olas': u'hola',
                    u'olaz': u'hola',
                    u'pic': u'foto',
                    u'pick': u'foto',
                    u'pik': u'foto',
                    u'plis': u'por favor',
                    u'pliz': u'por favor',
                    u'plz': u'por favor',
                    u'sho': u'yo',
                    u'sip': u'si',
                    u'soi': u'soy',
                    u'stoi': u'estoy',
                    u'sullo': u'suyo',
                    u'ta': u'est&aacute;',
                    u'tawena': u'est&aacute; buena',
                    u'tap': u'top',
                    u'taz': u'est&aacute;s',
                    u'teno': u'tengo',
                    u'toi': u'estoy',
                    u'toos': u'todos',
                    u'tullo': u'tuyo',
                    u'lav': u'love',
                    u'lov': u'love',
                    u'lendo': u'lindo',
                    u'llendo': u'yendo',
                    u'mua': u'besos',
                    u'muak': u'besos',
                    u'muac': u'besos',
                    u'muack': u'besos',
                    u'muto': u'mucho',
                    u'nah': u'nada',
                    u'nu': u'no',
                    u'nueo': u'nuevo',
                    u'nunk': u'nunca',
                    u'nuc': u'no se',
                    u'voi': u'voy',
                    u'we': u'bueno',
                    u'wem': u'bueno',
                    u'wno': u'bueno',
                    u'xau': u'chau',
                    u'xfa': u'por favor'
                   }

    lword = word.lower()
    if u'emd' in lword:
        word = lword.replace(u'emd', u'ind')
    if u'md' in lword:
        word = lword.replace(u'md', u'nd')
    if re.match(r'^[i]+$',lword):
        word = u'y'
    if len(lword) > 2 and lword[:3] == u'wen':
        word = u"buen" + lword[3:]
    if len(lword) > 2 and lword[:3] == u'oka':
        word = u"ok"

    #posible risa
    if len(lword) > 6:
        if re.match(u"^((j|a|k)+)$",lword):
            return u"jajaja"
        elif len(lword) > 8 and re.match(u"^((j|a|k|h|l|s|d|ñ)+)j((j|a|k|h|l|s|d|ñ)+)j((j|a|k|h|l|s|d|ñ)*)$",lword):
            return u"jajaja"


    if word.lower() in translations:
        word = translations[word.lower()]

    if format == 'plain':
        word = decodeEntities(word)

    return word

def desk(word, format='html'):
    exceptions = [u'kiosco', u'kilo', u'kiló', u'fuck', u'punk', u'rock', u'look', u'kiss']
    vocales = [u'a', u'e', u'i', u'o',u'u']

    lword = word.lower()

    if lword == u'ok':
        return word
    
    for a in exceptions:
        if a in lword:
            return word
    
    if u"ki" in lword:
        word = word.lower().replace(u'ki', u'qui')
    
    if u"ke" in word:
        word = word.lower().replace(u'ke', u'que')

    if len(word) > 2 and word[0].lower() == u'k' and word[1].lower() not in vocales:
        word = u"ka" + word[1:].lower()
    
    word = word.replace(u'k',u'c')
    word = word.replace(u'K',u'C')
    return word


def desporteniar(word, format='html'):
    lword = word.lower()
    if len(lword) > 5 and lword[-4:] == u'stes':
        word = lword[:-1]
    return word


def deszezear(word, format='html'):
    exceptions = [u'arroz', u'feliz', u'zorr', u'azul', u'azucar', u'azúcar', u'conoz', u'zapa']

    lword = word.lower()
    
    for a in exceptions:
        if a in lword:
            return word
    
    word = word.replace(u'z',u's')
    word = word.replace(u'Z',u'S')
    return word


def fixmissingvowels(word, format='html'):
    exceptions = [u'get', u'cat', u'that', u'best', u'post', u'net', u'chat']
    vocales = [u'a', u'e', u'i', u'o',u'u']
    followsd = [u'a', u'e', u'i', u'o',u'u', u'r', u'h', u'y']

    lword = word.lower()
    if not lword in exceptions:
        if len(lword) > 1 and lword[0] == u'n' and not lword[1] in vocales:
            lword = u"en" + lword[1:]
            word = lword
        
        wlen = len(word)
        if wlen > 1 and lword[wlen-1] == u't':
            lword += u'e'
            word = lword
        
        if len(lword) > 2 and lword[:2] == u"vr" and not lword[2] in vocales:
            lword = u"ver" + lword[2:]
            word = lword

        if len(lword) > 2 and lword[0] == u'd' and not lword[1] in followsd:
            lword = u"de" + lword[1:]
            word = lword

        if len(lword) > 2 and lword[:2] == u"sp" and not lword[2] in vocales:
            lword = u"esp" + lword[2:]
            word = lword

        if len(lword) > 2 and lword[:2] == u"st" and not lword[2] in vocales:
            lword = u"est" + lword[2:]
            word = lword

    return word


def _test():
    import doctest
    doctest.testmod()
 
if __name__ == "__main__":
    _test()
