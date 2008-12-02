#!/usr/bin/python
# -*- coding: iso-8859-1 -*-
#*********************************************************
#* DeFlog 2008-11-02                                     *
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
from urllib import urlopen
from BeautifulSoup import BeautifulSoup
from BeautifulSoup import BeautifulStoneSoup
from BeautifulSoup import NavigableString
from BeautifulSoup import CData
from BeautifulSoup import ProcessingInstruction
from BeautifulSoup import Comment
from BeautifulSoup import Declaration

from pylibdeflog.libdeflog import *

def tohtml(word):
    """ \r\n -> <br/> """
    return word.replace("<", "&lt;").replace(">", "&gt;").replace("\r\n", "<br/>")

def traducir(sopa, deleetval, desalternarval, desmultiplicarval, desmsarval, desestupidizarval, deszezearval, deskarval, desporteniarval, fixmissingvowelsval):
    for c in sopa.contents:
        if isinstance(c, NavigableString) and not isinstance(c, (CData, ProcessingInstruction, Comment, Declaration)):
            try:
                c.replaceWith(unicode(desfotologuear(c.encode('utf-8'), deleetval, desalternarval, desmultiplicarval, desmsarval, desestupidizarval, deszezearval, deskarval, desporteniarval, fixmissingvowelsval), 'utf-8'))
            except:
                print "error con %s" % c.encode('utf-8')
        elif c and not isinstance(c, (CData, ProcessingInstruction, Comment, Declaration)) and c.name not in ('style', 'script'):
            traducir(c, deleetval, desalternarval, desmultiplicarval, desmsarval, desestupidizarval, deszezearval, deskarval, desporteniarval, fixmissingvowelsval)


def desfotologuear(text, deleetval, desalternarval, desmultiplicarval, desmsarval, desestupidizarval, deszezearval, deskarval, desporteniarval, fixmissingvowelsval):
    words = re.split(u"([\\w\\dáéíóúñ+]+)",dessimbolizar(text))
    
    html = ""

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
    return html



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
        
        words = re.split(u"([\\w\\dáéíóúñ+]+)",dessimbolizar(text))
        
        html = """<html xmlns="http://www.w3.org/1999/xhtml">
<head>
<meta http-equiv="Content-Language" content="es"/>
<meta name="description" content="Traducir texto en idioma fotolog, sms, etc a espa&ntilde;ol legible"/>
<meta name="keywords" content="flog flogger floggers fotolog sms traductor translator"/>
<meta http-equiv="Content-Type" content="text/html; charset=ISO-8859-1" />
<link type="text/css" href="desfotologuear.css" rel="stylesheet" />

<title>Traductor de lenguaje flogger, sms, etc a Español (Desfotologueador)</title>
</head>

<body>
<div align="right" style="font-size: medium; font-family: arial,sans-serif; width:100%">
    <span style="font-size: 84%;">
    <a href="#" onclick="alert(\'CLP!!!!\');" >Ayuda</a>
    </span>
    </div>
    <table width="100%" cellspacing="0" cellpadding="0" border="0" style="font-size: medium;">
    <tr>
    <td width="1%" height="62">
    <img width="150" height="62" border="0" style="margin: 0pt 4px 0pt 0pt;" src="deflog.gif" alt="Deflog"/>
    </td>
    <td width="100%" align="right">
    </td>
    </tr>
    </table>

    <h4>Desfotologuear texto:</h4>
    <form action="index" method="post" name="form1" id="form1">

        <table id="texttable">
        <tr>
            <td id="original_text" colspan="2">
            Texto Original:
            </td>
            <td id="autotrans">
            Texto Traducido:
            </td>
        </tr>
        <tr valign="top">
            <td id="sourcecell">
                <textarea id="source" name="text">""" + text + """</textarea>
            </td>
            <td id="gap">
                &nbsp;
            </td>
            <td class="almost_half_cell">
            <div id="result_box" dir="ltr">
"""
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
        html += """</div></td>
        </tr>

        <tr>
            <td id="submitcell">
                <table>

                <tr>

                <td id="selectcell">
                    <select name="langpair">
                        <option value="flog|es">Fotolog a Espa&ntilde;ol</option>
                    </select>
                </td>
                <td>
                    <input type="submit" value="Traducir"/>
                </td>

                </tr>

                <tr>
                <td class="select_metodos_title"> M&eacute;todos a aplicar al texto:</td>
                </tr>

                <tr>
                <td>Desmultiplicar</td>
                <td><input type="radio" name="desmultiplicarval" value="on" """ + desmultiplicar_checked_yes + """ > Si</td>
                <td><input type="radio" name="desmultiplicarval" value="off" """ + desmultiplicar_checked_no + """ > No</td>
                </tr>

                <tr>
                <td>Deszezear</td>
                <td><input type="radio" name="deszezearval" value="on" """ + deszezear_checked_yes + """ > Si</td>
                <td><input type="radio" name="deszezearval" value="off" """ + deszezear_checked_no + """ > No</td>
                </tr>

                <tr>
                <td>Des-k-ar</td>
                <td><input type="radio" name="deskarval" value="on" """ + deskar_checked_yes + """ > Si</td>
                <td><input type="radio" name="deskarval" value="off" """ + deskar_checked_no + """ > No</td>
                </tr>

                <tr>
                <td>DesSMSar</td>
                <td><input type="radio" name="desmsarval" value="on" """ + desmsar_checked_yes + """ > Si</td>
                <td><input type="radio" name="desmsarval" value="off" """ + desmsar_checked_no + """ > No</td>
                </tr>

                <tr>
                <td>Desestupidizar</td>
                <td><input type="radio" name="desestupidizarval" value="on" """ + desestupidizar_checked_yes + """ > Si</td>
                <td><input type="radio" name="desestupidizarval" value="off" """ + desestupidizar_checked_no + """ > No</td>
                </tr>

                <tr>
                <td>Desalternar</td>
                <td><input type="radio" name="desalternarval" value="on" """ + desalternar_checked_yes + """ > Si</td>
                <td><input type="radio" name="desalternarval" value="off" """ + desalternar_checked_no + """ > No</td>
                </tr>

                <tr>
                <td>Desporteñar</td>
                <td><input type="radio" name="desporteniarval" value="on" """ + desporteniar_checked_yes + """ > Si</td>
                <td><input type="radio" name="desporteniarval" value="off" """ + desporteniar_checked_no + """ > No</td>
                </tr>

                <tr>
                <td>Deleet</td>
                <td><input type="radio" name="deleetval" value="on" """ + deleet_checked_yes + """ > Si</td>
                <td><input type="radio" name="deleetval" value="off" """ + deleet_checked_no + """ > No</td>
                </tr>


                <tr>
                <td>Fix missing vowels</td>
                <td><input type="radio" name="fixmissingvowelsval" value="on" """ + fixmissingvowels_checked_yes + """ > Si</td>
                <td><input type="radio" name="fixmissingvowelsval" value="off" """ + fixmissingvowels_checked_no + """ > No</td>
                </tr>


                </table>
            </td>

            <td>
            </td>

            <td align="right">
            <span id="zippyspan" onclick="alert(\'SS 1 BLD!!!!\');" style="visibility: visible;">
            <img style="margin-right: 0.33em;" src="icono_mas.gif" alt="Sugerir mejor traducci&oacute;n"/>Proponer una traducci&oacute;n mejor
            </span>
            </td>
        </tr>

        </table>
    </form>

<h4>Traducir una p&aacute;gina web</h4>
<form id="web_form" action="/translate">
    <table id="webtable">
        <tbody>
            <tr>
                <td width="100%">
                    <input type="text" tabindex="0" dir="ltr" value="http://" id="url" name="u"/>
                </td>
            </tr>
            <tr>
            <td id="submitcell">
                <table>

                <tr>

                <td id="selectcell">
                    <select name="langpair">
                        <option value="flog|es">Fotolog a Espa&ntilde;ol</option>
                    </select>
                </td>
                <td>
                    <input type="submit" value="Traducir"/>
                </td>

                </tr>

                <tr>
                <td class="select_metodos_title"> M&eacute;todos a aplicar al texto:</td>
                </tr>

                <tr>
                <td>Desmultiplicar</td>
                <td><input type="radio" name="desmultiplicarval" value="on" """ + desmultiplicar_checked_yes + """ > Si</td>
                <td><input type="radio" name="desmultiplicarval" value="off" """ + desmultiplicar_checked_no + """ > No</td>
                </tr>

                <tr>
                <td>Deszezear</td>
                <td><input type="radio" name="deszezearval" value="on" """ + deszezear_checked_yes + """ > Si</td>
                <td><input type="radio" name="deszezearval" value="off" """ + deszezear_checked_no + """ > No</td>
                </tr>

                <tr>
                <td>Des-k-ar</td>
                <td><input type="radio" name="deskarval" value="on" """ + deskar_checked_yes + """ > Si</td>
                <td><input type="radio" name="deskarval" value="off" """ + deskar_checked_no + """ > No</td>
                </tr>

                <tr>
                <td>DesSMSar</td>
                <td><input type="radio" name="desmsarval" value="on" """ + desmsar_checked_yes + """ > Si</td>
                <td><input type="radio" name="desmsarval" value="off" """ + desmsar_checked_no + """ > No</td>
                </tr>

                <tr>
                <td>Desestupidizar</td>
                <td><input type="radio" name="desestupidizarval" value="on" """ + desestupidizar_checked_yes + """ > Si</td>
                <td><input type="radio" name="desestupidizarval" value="off" """ + desestupidizar_checked_no + """ > No</td>
                </tr>

                <tr>
                <td>Desalternar</td>
                <td><input type="radio" name="desalternarval" value="on" """ + desalternar_checked_yes + """ > Si</td>
                <td><input type="radio" name="desalternarval" value="off" """ + desalternar_checked_no + """ > No</td>
                </tr>

                <tr>
                <td>Desporteñar</td>
                <td><input type="radio" name="desporteniarval" value="on" """ + desporteniar_checked_yes + """ > Si</td>
                <td><input type="radio" name="desporteniarval" value="off" """ + desporteniar_checked_no + """ > No</td>
                </tr>

                <tr>
                <td>Deleet</td>
                <td><input type="radio" name="deleetval" value="on" """ + deleet_checked_yes + """ > Si</td>
                <td><input type="radio" name="deleetval" value="off" """ + deleet_checked_no + """ > No</td>
                </tr>


                <tr>
                <td>Fix missing vowels</td>
                <td><input type="radio" name="fixmissingvowelsval" value="on" """ + fixmissingvowels_checked_yes + """ > Si</td>
                <td><input type="radio" name="fixmissingvowelsval" value="off" """ + fixmissingvowels_checked_no + """ > No</td>
                </tr>


                </table>
            </td>

            <td>
            </td>
            </tr>
        </tbody>
    </table>
</form>

    <div class="footer">
    <a href="http://www.santiagobruno.com.ar/programas.html#deflog">More info on my website</a> - <a href="http://cervezaconlupines.blogspot.com/2008/03/presentando-deflog.html">About This Shit</a> - <a href="index?text=LocURaAAaaA%21%21%21%0D%0Ake+loko+estoooo+mIeRdA%21%21%21%0D%0A%0D%0AAaAaAAAaaAiiiii++firmeeennnn+leeemmmddoooo%21%21%21%0D%0A%0D%0Anuc+k+pasa+ak.+t+voi+a+ver+dsp.%0D%0Aqe+andes+d+mil%21%21%0D%0AbesOtte%0D%0A%0D%0Aesto+q+m+dijistes+ta+groxo+maallll+grax+xq+m+dijistessss+cdo+lo+vistessssss%0D%0A%0D%0Atoy+reeee+lokooo+blds%21%21%0D%0Aaahhrrreee%0D%0At+qiero%2C+we%2C+chauuuu%21%21%21%0D%0Abss.%0D%0Aazi+ez+ezto%2C+nos+vems%2C+stamos.+dspu%E9s+dcime.+4gu4n73+a77aqu3%0D%0Ajkajkajkaajkajk">Translation Example</a><br/><br/>This site is not affiliated with Google and is not against floggers or any internet community<br/><br/>©2008 Santiago Bruno</div>

</body>
</html>"""

        return html

    def translate(self, u = "", desmultiplicarval = 'on', deszezearval = 'off', deskarval = 'off', desmsarval = 'on', desestupidizarval = 'on', desalternarval = 'on',  desporteniarval = 'on', deleetval = "on", fixmissingvowelsval = "on", **kwargs):

        try:
            url = urlopen(u)
            archivo = url.read()
        except:
            return ""
        
        soup = BeautifulSoup(archivo, convertEntities=BeautifulStoneSoup.ALL_ENTITIES)

        traducir(soup, deleetval, desalternarval, desmultiplicarval, desmsarval, desestupidizarval, deszezearval, deskarval, desporteniarval, fixmissingvowelsval)
            
        return soup.prettify()




    index.exposed = True
    translate.exposed = True

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
