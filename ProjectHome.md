# Deflog #

## Descripción ##

Este programa intenta eliminar varias de las características del lenguaje flogger, como repetición de letras, alternación de mayúsculas y minúsculas, abreviaturas de sms, etc.
Se presenta en un varias versiones:

### Versiones web ###
  * PHP
  * Javascript
  * Python usando cherrypy

### Versiones desktop ###
  * PyQT4

### Otras ###
  * Como un plugin para Messenger Plus! Live.
  * Módulo python con las funciones utilizadas.


## Capturas de pantalla ##

### Captura de la versión online: ###

[http://bananabruno.googlepages.com/deflog-javascript-screenshot-small.jpg ](http://bananabruno.googlepages.com/deflog-javascript-screenshot.jpg)


### Captura del plugin para Messenger Plus! Live: ###

[http://bananabruno.googlepages.com/deflog-msnlive-screenshot-small.jpg ](http://bananabruno.googlepages.com/deflog-msnlive-screenshot.jpg)



## Descargas ##

Las descargas recomendadas para las cuatro variantes del programa son las que aparecen en Featured Downloads

El plugin puede ser descargado también desde el [sitio de Messenger Plus! Live](http://www.msgpluslive.net/scripts/view/404-DeFlog/):

Pero esa puede no ser la última versión. Para descargar la última versión, hacerlo desde http://code.google.com/p/deflog/downloads/list

O para ver alguna novedad experimental (?), el trunk del repositorio:
http://deflog.googlecode.com/svn/trunk/msnlive_plugin/package/deflog.plsc

DISCLAIMER: El plugin solo puede aplicar todos los métodos correctamente a los mensajes salientes. Es una limitación del messenger como se dice en mi página o la página del plugin en el sitio de Messenger Plus! Live

## Probar Online ##
[Versión en PHP](http://www.santiagobruno.com.ar/php/desfotologuear.php)

[Versión en Javascript](http://www.santiagobruno.com.ar/javascript/desfotologuear.html)

## Descripción de los métodos aplicables al texto ##

**Desmultiplicar:** Elimina repeticiones de letras (holaaaaa -> hola)

**Deszezear:** Transforma zetas en eses (Desactivado por defecto ya que no es nada inteligente, y si el texto está relativamente bien escrito generará más errores de ortografía de los que solucionará)

**Des-k-ar:** Similar a Deszezear pero para k -> c. Además transforma ki en qui.

**DesSMSar:** Elimina abreviaturas SMS (xq -> por que, dsp -> después)

**Desestupidizar:** (toi -> estoy, i -> y, lemdo -> lindo)

**Desalternar:** Convierte palabras con mezcla de mayúsculas y minúsculas a minúscula (LeTrA dE uNa CaNcIoN -> letra de una cancion)

**Desporteñar:** Elimina las eses finales en palabras que terminan en istes (lo vistes y me dijistes -> lo viste y me dijiste)

**Deleet:** Convierte a letra los números que se usan como letra (3s7o e5 un 73x70 f30 -> esto es un texto feo)

**Fix missing vowels:** Arega vocales omitidas el final de las palabras (va a fallar en palabras en inglés, porque se supone que en español muy pocas palabras finalizan por ejemplo en 't', entonces se asume que se le debe agregar una e) (stamos -> estamos, spero -> espero, dcile -> decile, nterado -> enterado, vrdad -> verdad, comprart, comprarte)

Todos los métodos pueden aplicarse selectivamente