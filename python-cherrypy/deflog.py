#!/usr/bin/python
# -*- coding: iso-8859-1 -*-
#*********************************************************
#* DeFlog 2008-05-29                                     *
#* Traduce Fotolog/SMS a español                         *
#* http://www.santiagobruno.com.ar/programas.html#deflog *
#* Licencia: GPL v3                                      *
#********************************************************/

try:
    import cherrypy
except ImportError:
    import sys
    sys.exit("Error importando cherrypy. Comporobar su correcta instalación. http://www.cherrypy.org/")
import re


def tohtml(word):
    """ \r\n -> <br/> """
    return word.replace("<", "&lt;").replace(">", "&gt;").replace("\r\n", "<br/>")

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

    if translations.has_key(word.lower()):
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

    if translations.has_key(word.lower()):
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
            elif len(lword) > 8 and re.match("^((j|a|k|l|s|d|ñ)+)j((j|a|k|l|s|d|ñ)+)j((j|a|k|l|s|d|ñ)+)$",lword):
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
        lword.replace('ki', 'qui')
        word = lword
    
    if "ke" in lword:
        lword.replace('ke', 'que')
        word = lword

    if len(lword) > 2 and lword[0] == 'k' and lword[1] not in vocales:
        lword = "ka" + lword[1:]
        word = lword
    
    
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



class Desfotologueador:

    def index(self, text = "", desmultiplicarval = 'on', deszezearval = 'off', deskarval = 'off', desmsarval = 'on', desestupidizarval = 'on', desalternarval = 'on',  desporteniarval = 'on', deleetval = "on", fixmissingvowelsval = "on", **kwargs):

        if desmultiplicarval == 'on':
            desmultiplicar_checked_yes = 'CHECKED'
            desmultiplicar_checked_no = ''
        else:
            desmultiplicar_checked_yes = ''
            desmultiplicar_checked_no = 'CHECKED'
            
        if deszezearval == 'on':
            deszezear_checked_yes = 'CHECKED'
            deszezear_checked_no = ''
        else:
            deszezear_checked_yes = ''
            deszezear_checked_no = 'CHECKED'
            
        if deskarval == 'on':
            deskar_checked_yes = 'CHECKED'
            deskar_checked_no = ''
        else:
            deskar_checked_yes = ''
            deskar_checked_no = 'CHECKED'
            
        if desmsarval == 'on':
            desmsar_checked_yes = 'CHECKED'
            desmsar_checked_no = ''
        else:
            desmsar_checked_yes = ''
            desmsar_checked_no = 'CHECKED'
            
        if desestupidizarval == 'on':
            desestupidizar_checked_yes = 'CHECKED'
            desestupidizar_checked_no = ''
        else:
            desestupidizar_checked_yes = ''
            desestupidizar_checked_no = 'CHECKED'
            
        if desalternarval == 'on':
            desalternar_checked_yes = 'CHECKED'
            desalternar_checked_no = ''
        else:
            desalternar_checked_yes = ''
            desalternar_checked_no = 'CHECKED'
            
        if desporteniarval == 'on':
            desporteniar_checked_yes = 'CHECKED'
            desporteniar_checked_no = ''
        else:
            desporteniar_checked_yes = ''
            desporteniar_checked_no = 'CHECKED'
            
        if deleetval == 'on':
            deleet_checked_yes = 'CHECKED'
            deleet_checked_no = ''
        else:
            deleet_checked_yes = ''
            deleet_checked_no = 'CHECKED'
            
        if fixmissingvowelsval == 'on':
            fixmissingvowels_checked_yes = 'CHECKED'
            fixmissingvowels_checked_no = ''
        else:
            fixmissingvowels_checked_yes = ''
            fixmissingvowels_checked_no = 'CHECKED'
            
            
        #words = re.split(r"(([\w]|"+unicode_chars+")+)",text)
        # $words = preg_split("/([\w\dÃ¡Ã©Ã­Ã³ÃºÃ±+]+)/", dessimbolizar($text), -1, PREG_SPLIT_DELIM_CAPTURE | PREG_SPLIT_NO_EMPTY);

        words = re.split(u"([\\w\\dáéíóúñ+]+)",dessimbolizar(text))
        print text
        print unicode(text,'latin-1')
        print words
        html = '<html xmlns="http://www.w3.org/1999/xhtml">\
<head>\
<meta http-equiv="Content-Language" content="es"/>\
<meta name="description" content="Traducir texto en idioma fotolog, sms, etc a espa&ntilde;ol legible"/>\
<meta name="keywords" content="flog flogger floggers fotolog sms traductor translator"/>\
<meta http-equiv="Content-Type" content="text/html; charset=ISO-8859-1" />\
<link type="text/css" href="desfotologuear.css" rel="stylesheet" />\
\
<title>Desfotologueador</title>\
</head>\
\
<body>\
<div align="right" style="font-size: medium; font-family: arial,sans-serif; width:100%">\
    <span style="font-size: 84%;">\
    <a href="#" onclick="alert(\'CLP!!!!\');" >Ayuda</a>\
    </span>\
    </div>\
    <table width="100%" cellspacing="0" cellpadding="0" border="0" style="font-size: medium;">\
    <tr>\
    <td width="1%" height="62">\
    <img width="150" height="62" border="0" style="margin: 0pt 4px 0pt 0pt;" src="deflog.gif" alt="Deflog"/>\
    </td>\
    <td width="100%" align="right">\
    </td>\
    </tr>\
    </table>\
\
    <h4>Desfotologuear texto:</h4>\
    <form action="index" method="post" name="form1" id="form1">\
\
        <table id="texttable">\
        <tr>\
            <td id="original_text" colspan="2">\
            Texto Original:\
            </td>\
            <td id="autotrans">\
            Texto Traducido:\
            </td>\
        </tr>\
        <tr valign="top">\
            <td id="sourcecell">\
                <textarea id="source" name="text">' + text + '</textarea>\
            </td>\
            <td id="gap">\
                &nbsp;\
            </td>\
            <td class="almost_half_cell">\
            <div id="result_box" dir="ltr">\
'
        if words:
            words = map(tohtml, words)
            if deleetval == 'on':
                words = map(deleet, words)
            if desalternarval == 'on':
                words = map(desalternar, words)
            if desmultiplicarval == 'on':
                words = map(desmultiplicar, words)
            if desmsarval == 'on':
                words = map(desms, words)
            if desestupidizarval == 'on':
                words = map(desestupidizar, words)
            if deszezearval == 'on':
                words = map(deszezear, words)
            if deskarval == 'on':
                words = map(desk, words)
            if desporteniarval == 'on':
                words = map(desporteniar, words)
            if fixmissingvowelsval == 'on':
                words = map(fixmissingvowels, words)
            html += "".join( [ w for w in words] ) 
        html += '</div></td>\
        </tr>\
        \
        <tr>\
            <td id="submitcell">\
                <table>\
\
                <tr>\
\
                <td id="selectcell">\
                    <select name="langpair">\
                        <option value="flog|es">Fotolog a Espa&ntilde;ol</option>\
                    </select>\
                </td>\
                <td>\
                    <input type="submit" value="Traducir"/>\
                </td>\
\
                </tr>\
\
                <tr>\
                <td class="select_metodos_title"> M&eacute;todos a aplicar al texto:</td>\
                </tr>\
\
                <tr>\
                <td>Desmultiplicar</td>\
                <td><input type="radio" name="desmultiplicarval" value="on" ' + desmultiplicar_checked_yes + ' > Si</td>\
                <td><input type="radio" name="desmultiplicarval" value="off" ' + desmultiplicar_checked_no + ' > No</td>\
                </tr>\
\
                <tr>\
                <td>Deszezear</td>\
                <td><input type="radio" name="deszezearval" value="on" ' + deszezear_checked_yes + ' > Si</td>\
                <td><input type="radio" name="deszezearval" value="off" ' + deszezear_checked_no + ' > No</td>\
                </tr>\
\
                <tr>\
                <td>Des-k-ar</td>\
                <td><input type="radio" name="deskarval" value="on" ' + deskar_checked_yes + ' > Si</td>\
                <td><input type="radio" name="deskarval" value="off" ' + deskar_checked_no + ' > No</td>\
                </tr>\
\
                <tr>\
                <td>DesSMSar</td>\
                <td><input type="radio" name="desmsarval" value="on" ' + desmsar_checked_yes + ' > Si</td>\
                <td><input type="radio" name="desmsarval" value="off" ' + desmsar_checked_no + ' > No</td>\
                </tr>\
\
                <tr>\
                <td>Desestupidizar</td>\
                <td><input type="radio" name="desestupidizarval" value="on" ' + desestupidizar_checked_yes + ' > Si</td>\
                <td><input type="radio" name="desestupidizarval" value="off" ' + desestupidizar_checked_no + ' > No</td>\
                </tr>\
\
                <tr>\
                <td>Desalternar</td>\
                <td><input type="radio" name="desalternarval" value="on" ' + desalternar_checked_yes + ' > Si</td>\
                <td><input type="radio" name="desalternarval" value="off" ' + desalternar_checked_no + ' > No</td>\
                </tr>\
\
                <tr>\
                <td>Desporteñar</td>\
                <td><input type="radio" name="desporteniarval" value="on" ' + desporteniar_checked_yes + ' > Si</td>\
                <td><input type="radio" name="desporteniarval" value="off" ' + desporteniar_checked_no + ' > No</td>\
                </tr>\
\
                <tr>\
                <td>Deleet</td>\
                <td><input type="radio" name="deleetval" value="on" ' + deleet_checked_yes + ' > Si</td>\
                <td><input type="radio" name="deleetval" value="off" ' + deleet_checked_no + ' > No</td>\
                </tr>\
\
\
                <tr>\
                <td>Fix missing vowels</td>\
                <td><input type="radio" name="fixmissingvowelsval" value="on" ' + fixmissingvowels_checked_yes + ' > Si</td>\
                <td><input type="radio" name="fixmissingvowelsval" value="off" ' + fixmissingvowels_checked_no + ' > No</td>\
                </tr>\
\
\
                </table>\
            </td>\
\
            <td>\
            </td>\
\
            <td align="right">\
            <span id="zippyspan" onclick="alert(\'SS 1 BLD!!!!\');" style="visibility: visible;">\
            <img style="margin-right: 0.33em;" src="icono_mas.gif" alt="Sugerir mejor traducci&oacute;n"/>Proponer una traducci&oacute;n mejor\
            </span>\
            </td>\
        </tr>\
    \
    \
        </table>\
    </form>\
\
    <div class="footer">\
    <a href="http://www.santiagobruno.com.ar/programas.html#deflog">More info on my website</a> - <a href="http://cervezaconlupines.blogspot.com/2008/03/presentando-deflog.html">About This Shit</a> - <a href="index?text=LocURaAAaaA%21%21%21%0D%0Ake+loko+estoooo+mIeRdA%21%21%21%0D%0A%0D%0AAaAaAAAaaAiiiii++firmeeennnn+leeemmmddoooo%21%21%21%0D%0A%0D%0Anuc+k+pasa+ak.+t+voi+a+ver+dsp.%0D%0Aqe+andes+d+mil%21%21%0D%0AbesOtte%0D%0A%0D%0Aesto+q+m+dijistes+ta+groxo+maallll+grax+xq+m+dijistessss+cdo+lo+vistessssss%0D%0A%0D%0Atoy+reeee+lokooo+blds%21%21%0D%0Aaahhrrreee%0D%0At+qiero%2C+we%2C+chauuuu%21%21%21%0D%0Abss.%0D%0Aazi+ez+ezto%2C+nos+vems%2C+stamos.+dspu%E9s+dcime.+4gu4n73+a77aqu3%0D%0Ajkajkajkaajkajk">Translation Example</a><br/><br/>This site is not affiliated with Google and is not against floggers or any internet community<br/><br/>©2008 Santiago Bruno</div>\
\
</body>\
</html>'
                
        return html

    index.exposed = True

cherrypy.tree.mount(Desfotologueador())


if __name__ == '__main__':
    import os.path
    current_dir = os.path.dirname(os.path.abspath(__file__))
    thisdir = os.path.dirname(__file__)
    cherrypy.config.update({'environment': 'production',
                            'log.error_file': 'site.log',
                            'log.screen': True})

    conf = {'/desfotologuear.css': {'tools.staticfile.on': True,
                               'tools.staticfile.filename': os.path.join(current_dir, 'desfotologuear.css')},
            '/icono_mas.gif': {'tools.staticfile.on': True,
                               'tools.staticfile.filename': os.path.join(current_dir, 'icono_mas.gif')},
            '/deflog.gif': {'tools.staticfile.on': True,
                               'tools.staticfile.filename': os.path.join(current_dir, 'deflog.gif')}}

    cherrypy.quickstart(Desfotologueador(), config=conf)
