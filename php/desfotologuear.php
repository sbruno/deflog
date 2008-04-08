<html xmlns="http://www.w3.org/1999/xhtml">
<head>
<meta http-equiv="Content-Language" content="es"/>
<meta name="description" content="Traducir texto en idioma fotolog, sms, etc a espa&ntilde;ol legible"/>
<meta name="keywords" content="flog flogger floggers fotolog sms traductor translator"/>
<meta http-equiv="Content-Type" content="text/html; charset=ISO-8859-1" />
<link type="text/css" href="desfotologuear.css" rel="stylesheet" />

<title>Desfotologueador</title>
</head>

<body>

    <?php

        function stringrpos($haystack,$needle,$offset=NULL)
        {
            return strlen($haystack)
                - strpos( strrev($haystack) , strrev($needle) , $offset)
                - strlen($needle);
        }

        function tohtml($text) {
            $text = str_replace("<", "&lt;", $text);
            $text = str_replace(">", "&gt;", $text);
            $text = str_replace("\r\n", "</br>", $text);
            return $text;
        }

        function dessimbolizar($text) {
            $text = str_replace("@", "a", $text);
            $text = str_replace("ª", "a", $text);
            $text = str_replace("º", "o", $text);
            $text = str_replace(" = "," igual ",$text);
            $text = preg_replace("/(\w*?)[¡!](\w)/","\\1i\\2",$text);

/*            $text = str_replace("â&#128;¢", "o", $text);*/
/*            $text = preg_replace("/[fF]\/[fF]/","ff",$text);*/
            return $text;
        }

        function deleet($text) {
            if (!preg_match("/\b\d+\b/",$text)) {
                $text = str_replace("0", "o", $text);
                $text = str_replace("1", "i", $text);
                $text = str_replace("3", "e", $text);
                $text = str_replace("4", "a", $text);
                $text = str_replace("5", "s", $text);
                $text = str_replace("7", "t", $text);

    /*            $text = preg_replace("/(\w*?)[0](\w*?)/","\\1o\\2",$text);
                $text = preg_replace("/(\w*?)[1](\w*?)/","\\1i\\2",$text);
                $text = preg_replace("/(\w*?)[3](\w*?)/","\\1e\\2",$text);
                $text = preg_replace("/(\w*?)[4](\w*?)/","\\1a\\2",$text);
                $text = preg_replace("/(\w*?)[5](\w*?)/","\\1a\\2",$text);
                $text = preg_replace("/(\w*?)[7](\w*?)/","\\1t\\2",$text);
    */        }
            return $text;
        }



        function desalternar($word) {

// mejor pasamos todo a minusculas
//             if (strlen($word) > 1 and !ctype_lower($word) and !ctype_upper($word) and !(ctype_upper($word[0]) and ctype_lower(substr($word,1)))) {
//                 return strtolower($word);
//             }


            if (strlen($word) > 1 and !(ctype_upper($word[0]) and ctype_lower(substr($word,1)))) {
                return strtolower($word);
            }
            else {
                return $word;
            }

        }


        function desmultiplicar($word) {
            $exceptions = array('http','www','://', 'ss', 'ppio', 'ff', 'bb', 'kiss');

            $lword = strtolower($word);

            if (preg_match("/^bs[s]+$/",$lword)) {
                return 'besos';
            }

            if (preg_match("/^mm[m]+[h]*$/",$lword)) {
                return 'mmmh';
            }

            if (preg_match("/^aa[a]+[h]*$/",$lword)) {
                return 'aaah';
            }

            if (preg_match("/^ba[a]+[h]*$/",$lword)) {
                return 'baaah';
            }

            if (preg_match("/^bu[u]+[h]*$/",$lword)) {
                return 'buuu';
            }



/*            if (!preg_match("/(^[\w])(\\1)*$/",$word)) {*/
           if (!in_array($lword, $exceptions) and substr($lword,0,3) != '...') {
                if (preg_match("/(^|[^l])[l][l]([^l])+/",$lword)) {
                    #en awardspace no anda porque es php4
//                     $pos = strrpos($lword,'ll');
                    $pos = stringrpos($lword,'ll');
                    return desmultiplicar(substr($lword,0,$pos)).'ll'.desmultiplicar(substr($lword,$pos+2));
                }
                if (preg_match("/([^r])+[r][r]([^r])+/",$lword)) {
//                     $pos = strrpos($lword,'rr');
                    $pos = stringrpos($lword,'rr');
                    return desmultiplicar(substr($lword,0,$pos)).'rr'.desmultiplicar(substr($lword,$pos+2));

                }

                /*Los dos casos siguientes se pueden sacar si no se esperan muchas */
                /*palabras en inglï¿½s. Sirve para pasar google, good, teen, etc     */
                if (preg_match("/([^o])+[o][o]([^o])+/",$lword)) {
//                     $pos = strrpos($lword,'oo');
                    $pos = stringrpos($lword,'oo');
                    return desmultiplicar(substr($lword,0,$pos)).'oo'.desmultiplicar(substr($lword,$pos+2));

                }
                if (preg_match("/([^e])+[e][e]([^e])+/",$lword)) {
//                     $pos = strrpos($lword,'ee');
                    $pos = stringrpos($lword,'ee');
                    return desmultiplicar(substr($lword,0,$pos)).'ee'.desmultiplicar(substr($lword,$pos+2));

                }

                return preg_replace("/(.)\\1+/","\\1",$word);

            }
            else {
                return $word;
            }
        }

        function desms($word) {
            $translations = array(
                    '+' => 'm&aacute;s',
                    '+a' => 'masa',
                    'ad+' => 'adem&aacute;s',
                    'ak' => 'ac&aacute;',
                    'asc' => 'al salir de clase',
                    'asdc' => 'al salir de clase',
                    'bb' => 'beb&eacute;',
                    'bld' => 'boludo',
                    'blds' => 'boludos',
                    'bn' => 'bien',
                    'bno' => 'bueno',
                    'bss' => 'besos',
                    'c' => 'se',
                    'cdo' => 'cuando',
                    'cel' => 'celular',
                    'clp' => 'chupame la pija',
                    'cmo' => 'como',
                    'd' => 'de',
                    'dle' => 'dale',
                    'dsd' => 'desde',
                    'dsp' => 'despu&eacute;s',
                    'flia' => 'familia',
                    'fto' => 'foto',
                    'hdp' => 'hijo de puta',
                    'hexo' => 'hecho',
                    'hlqp' => 'hacemos lo que podemos',
                    'hna' => 'hermana',
                    'hno' => 'hermano',
                    'hsta' => 'hasta',
                    'k' => 'que',
                    'kpo' => 'capo',
                    'ksa' => 'casa',
                    'lpm' => 'la puta madre',
                    'lpmqtp' => 'la puta madre que te pari&oacute;',
                    'lpqtp' => 'la puta que te pari&oacute;',
                    'm' => 'me',
                    'mjor' => 'mejor',
                    'mjr' => 'mejor',
                    'msj' => 'mensaje',
                    'n' => 'en',
                    'nd' => 'nada',
                    'nxe' => 'noche',
                    'ppio' => 'principio',
                    'pq' => 'porque',
                    'ps' => 'pues',
                    'pso' => 'paso',
                    'pt' => 'pete',
                    'q' => 'que',
                    'qn' => 'quien',
                    'salu2' => 'saludos',
                    'ss' => 'sos',
                    'sta' => 'est&aacute;',
                    'stan' => 'est&aacute;n',
                    'stamos' => 'estamos',
                    'stes' => 'est&eacute;s',
                    't' => 'te',
                    'tas' => 'est&aacute;s',
                    'tb' => 'tambi&eacute;n',
                    'tbj' => 'trabajo',
                    'tbn' => 'tambi&eacute;n',
                    'tdo' => 'todo',
                    'tdos' => 'todos',
                    'tds' => 'todos',
                    'tgo' => 'tengo',
                    'tkm' => 'te quiero mucho',
                    'tmb' => 'tambi&eacute;n',
                    'tmbn' => 'tambi&eacute;n',
                    'tp' => 'tampoco',
                    'toy' => 'estoy',
                    'tk' => 'te quiero',
                    'tq' => 'te quiero',
                    'vac' => 'vacaciones',
                    'x' => 'por',
                    'xa' => 'para',
                    'xat' => 'chat',
                    'xk' => 'porque',
                    'xo' => 'pero',
                    'xq' => 'porque',
                    'xqe' => 'porque'

);


            if (array_key_exists  ( strtolower($word)  , $translations  )) {
                return $translations[strtolower($word)];
            }
            else {
                $lword = strtolower($word);
                if (preg_match("/qe/",$lword)   or preg_match("/ke/",$lword) or preg_match("/qi/",$lword)) {
                    $lword = str_replace('qe', 'que', $lword);
                    $lword = str_replace('ke', 'que', $lword);
                    $lword = str_replace('qi', 'qui', $lword);
                    $word = $lword;
                }

                if (strlen($lword) > 2 and $lword{strlen($lword)-1} == 'q')  {
                    $lword = substr($lword,0,-1)." que";
                    $word = $lword;
                }

                if (strlen($lword) > 3 and substr($lword,-2) == 'ms')  {
                    $lword = substr($lword,0,-1)."os";
                    $word = $lword;
                }
                if (strlen($lword) > 1 and substr($lword,0,2) == 'cn')  {
                    $lword = "con".substr($lword,2);
                    $word = $lword;
                }
                if (strlen($lword) > 2 and substr($lword,0,3) == 'bso')  {
                    $lword = "be".substr($lword,1);
                    $word = $lword;
                }
                if (strlen($lword) > 2 and substr($lword,0,3) == 'bld')  {
                    $lword = "bolu".substr($lword,2);
                    $word = $lword;
                }
                if (strlen($lword) > 3 and substr($lword,0,4) == 'efea')  {
                    $lword = "agrega".substr($lword,4)." a favoritos";
                    $word = $lword;
                }
                if (strlen($lword) > 4 and substr($lword,0,5) == 'efeen')  {
                    $lword = "agreguen".substr($lword,5)." a favoritos";
                    $word = $lword;
                }
                if (strlen($lword) > 3 and substr($lword,0,3) == 'mux')  {
                    $lword = "much".substr($lword,3);
                    $word = $lword;
                }
//                 if ($lword != '=p' and $lword != '=d' and substr($lword,0,1) == '=')  {
//                     $lword = "igual".substr($lword,1);
//                     $word = $lword;
//                 }

                return $word;
            }

        }

        function desestupidizar($word) {
            $translations = array(
                    '10pre' => 'siempre',
                    'arre' => '&lt;alguna sensaci&oacute;n&gt;',
                    'ahrre' => '&lt;alguna sensaci&oacute;n&gt;',
                    'ahre' => '&lt;alguna sensaci&oacute;n&gt;',
                    'ai' => 'ah&iacute;/hay/ay',
                    'aios' => 'adi&oacute;s',
                    'aka' => 'ac&aacute;',
                    'aki' => 'aqu&iacute;',
                    'akí' => 'aqu&iacute;',
                    'anio' => 'a&ntilde;o',
                    'bai' => 'bye',
                    'ben' => 'bien',
                    'bem' => 'bien',
                    'bue' => 'bueno',
                    'bzo' => 'beso',
                    'doi' => 'doy',
                    'efe' => 'favorito',
                    'efeo' => 'agrego a mis favoritos',
                    'efen' => 'agreguen a favoritos',
                    'efes' => 'favoritos',
                    'efs' => 'favoritos',
                    'estoi' => 'estoy',
                    'ff' => 'favoritos',
                    'fs' => 'favoritos',
                    'grax'=> 'gracias',
                    'groxo'=> 'grosso',
                    'hai' => 'hay',
                    'hoi'=> 'hoy',
                    'i' => 'y',
                    'ia' => 'ya',
                    'io' => 'yo',
                    'ise' => 'hice',
                    'iwal' => 'igual',
                    'kmo' => 'como',
                    'kn' => 'con',
                    'oi' => 'hoy',
                    'muchio' => 'mucho',
                    'mu' => 'muy',
                    'mui' => 'muy',
                    'nah' => 'nada',
                    'nuche' => 'no se',
                    'nus' => 'nos',
                    'nuse' => 'no se',
                    'ola' => 'hola',
                    'olas' => 'hola',
                    'olaz' => 'hola',
                    'pic' => 'foto',
                    'pick' => 'foto',
                    'pik' => 'foto',
                    'plis' => 'por favor',
                    'pliz' => 'por favor',
                    'plz' => 'por favor',
                    'sho' => 'yo',
                    'sip' => 'si',
                    'soi' => 'soy',
                    'stoi' => 'estoy',
                    'sullo' => 'suyo',
                    'ta' => 'est&aacute;',
                    'tawena' => 'est&aacute; buena',
                    'tap' => 'top',
                    'taz' => 'est&aacute;s',
                    'teno' => 'tengo',
                    'toi' => 'estoy',
                    'toos' => 'todos',
                    'tullo' => 'tuyo',
                    'lav' => 'love',
                    'lov' => 'love',
                    'lendo' => 'lindo',
                    'llendo' => 'yendo',
                    'mua' => 'besos',
                    'muak' => 'besos',
                    'muac' => 'besos',
                    'muack' => 'besos',
                    'muto' => 'mucho',
                    'nah' => 'nada',
                    'nu' => 'no',
                    'nueo' => 'nuevo',
                    'nunk'=> 'nunca',
                    'nuc' => 'no se',
                    'voi'=> 'voy',
                    'we' => 'bueno',
                    'wem' => 'bueno',
                    'wno' => 'bueno',
                    'xau' => 'chau',
                    'xfa' => 'por favor');


            if (array_key_exists  ( strtolower($word)  , $translations  )) {
                return $translations[strtolower($word)];
            }
            else {
                $lword = strtolower($word);
                if (preg_match("/emd/",$lword)) {
                    $lword = str_replace('emd', 'ind', $lword);
                    $word = $lword;
                }
                else if (preg_match("/md/",$lword)) {
                    $lword = str_replace('md', 'nd', $lword);
                    $word = $lword;
                }
                if (preg_match("/^[i]+$/",$lword)) {
                   $word = 'y';
                }
                if (strlen($lword) > 2 and substr($lword,0,3) == 'wen')  {
                    $lword = "buen".substr($lword,3);
                    $word = $lword;
                }
                if (strlen($lword) > 2 and substr($lword,0,3) == 'oka')  {
                    $lword = "ok";
                    $word = $lword;
                }

                return $word;
            }
        }

        function desk($word) {
            $exceptions = array('kiosco', 'kilo', 'kiló', 'fuck', 'punk', 'rock', 'look', 'kiss');
            $vocales = array('a', 'e', 'i', 'o','u');
            $lword = strtolower($word);

            if ($lword == 'ok') {
                return $word;
            }

            foreach ($exceptions as $a) {
                if (preg_match("/".$a."/", $lword)){
                    return $word;
                }
            }
            if (preg_match("/ki/",$lword)) {
                $lword = str_replace('ki', 'qui', $lword);
                $word = $lword;
            }
            if (preg_match("/ke/",$lword)) {
                $lword = str_replace('ke', 'que', $lword);
                $word = $lword;
            }

            if (strlen($lword) > 2 and $lword{0} == 'k' and !in_array($lword{1}, $vocales))  {
                $lword = "ka".substr($lword,1);
                $word = $lword;
            }


            $word = str_replace('k','c', $word);
            $word = str_replace('K','C', $word);
            return $word;
        }

        function desporteniar($word) {
            $lword = strtolower($word);
            if (strlen($lword) > 5 and substr($lword,-4) == 'stes')  {
                $lword = substr($lword,0,-1);
                $word = $lword;
            }
            return $word;
        }


        function deszezear($word) {
            $exceptions = array('arroz', 'feliz', 'zorr', 'azul', 'azucar', 'azúcar', 'conoz');
            $lword = strtolower($word);
            foreach ($exceptions as $a) {
                if (preg_match("/".$a."/", $lword)){
                    return $word;
                }
            }
            $word = str_replace('z','s', $word);
            $word = str_replace('Z','S', $word);
            return $word;
        }

        function fixmissingvowels($word) {
            $vocales = array('a', 'e', 'i', 'o','u');
            $exceptions = array('get', 'cat', 'that', 'best', 'post', 'net', 'chat');
            $lword = strtolower($word);
            if (!in_array($lword, $exceptions)) {
                if (strlen($lword) > 1 and $lword{0} == 'n' and !in_array($lword{1}, $vocales))  {
                    $lword = "en".substr($lword,1);
                    $word = $lword;
                }
    
                $len = strlen($lword);
                if ($len > 1 and $lword{$len-1} == 't')  {
                    $lword .= 'e';
                    $word = $lword;
                }
    
                if (strlen($lword) > 2 and substr($lword,0,2) == 'vr' and !in_array($lword{2}, $vocales))  {
                    $lword = "ver".substr($lword,2);
                    $word = $lword;
                }
    
                if (strlen($lword) > 2 and substr($lword,0,2) == 'ds')  {
                    $lword = "des".substr($lword,2);
                    $word = $lword;
                }
    
                if (strlen($lword) > 2 and substr($lword,0,2) == 'sp')  {
                    $lword = "esp".substr($lword,2);
                    $word = $lword;
                }
    
                if (strlen($lword) > 2 and substr($lword,0,2) == 'st')  {
                    $lword = "est".substr($lword,2);
                    $word = $lword;
                }
            }
            return $word;

        }



        $text = $_POST[text];
        if (!$text) {
            $text = $_GET[text];
        }

        $deszezear = $_POST[deszezear];
        if (!$deszezear) {
            $deszezear = $_GET[deszezear];
        }

        $nodesk = $_POST[nodesk];
        if (!$nodesk) {
            $nodesk = $_GET[nodesk];
        }


    ?>



    <div align="right" style="font-size: medium; font-family: arial,sans-serif; width:100%">
    <span style="font-size: 84%;">
    <a href="#" onclick="alert('CLP!!!!');" >Ayuda</a>
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
    <form action="desfotologuear.php" method="post" name="form1" id="form1">

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
                <textarea id="source" name="text"><?php
                echo stripslashes($text);
                ?></textarea>
            </td>
            <td id="gap">
                &nbsp;
            </td>
            <td class="almost_half_cell">
            <div id="result_box" dir="ltr">
                <?php
                    $words = preg_split("/([\w\dáéíóúñ+]+)/", dessimbolizar($text), -1, PREG_SPLIT_DELIM_CAPTURE | PREG_SPLIT_NO_EMPTY);

                    foreach ($words as $word) {
                        $result = desestupidizar(desms(desmultiplicar(desalternar(deleet(tohtml(stripslashes($word)))))));
    
                        if (!$deszezear and !$nodesk) {
                            $result = desk($result);
                        }
    
                        else if ($deszezear and $nodesk) {
                            $result = deszezear($result);
                        }
    
                        else if ($deszezear and !$nodesk) {
                            $result = deszezear(desk($result));
                        }
    
                        echo fixmissingvowels(desporteniar($result));
                    }
                ?>
            </div></td>
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
                <td>
                <input type=checkbox name="deszezear" <?php if ($deszezear) { echo "CHECKED"; } ?> >Deszezear
                </td>
                <td>
                <input type=checkbox name="nodesk" <?php if ($nodesk) { echo "CHECKED"; } ?> >No des-k-ar
                </td>
                </tr>


                </table>
            </td>

            <td>
            </td>

            <td align="right">
            <span id="zippyspan" onclick="alert('SS 1 BLD!!!!');" style="visibility: visible;">
            <img style="margin-right: 0.33em;" src="icono_mas.gif" alt="Sugerir mejor traducci&oacute;n"/>Proponer una traducci&oacute;n mejor
            </span>
            </td>
        </tr>
    
    
        </table>
    </form>

    <div class="footer">
    <a href="http://www.santiagobruno.com.ar/programas.html#deflog">More info on my website</a> - <a href="http://cervezaconlupines.blogspot.com/2008/03/presentando-deflog.html">About This Shit</a> - <a href="http://www.santiagobruno.com.ar/php/desfotologuear.php?text=LocURaAAaaA%21%21%21%0D%0Ake+loko+estoooo+mIeRdA%21%21%21%0D%0A%0D%0AAaAaAAAaaAiiiii++firmeeennnn+leeemmmddoooo%21%21%21%0D%0A%0D%0Anuc+k+pasa+ak.+t+voi+a+ver+dsp.%0D%0Aqe+andes+d+mil%21%21%0D%0AbesOtte%0D%0A%0D%0Aesto+q+m+dijistes+ta+groxo+maallll+grax+xq+m+dijistessss+cdo+lo+vistessssss%0D%0A%0D%0Atoy+reeee+lokooo+blds%21%21%0D%0Aaahhrrreee%0D%0At+qiero%2C+we%2C+chauuuu%21%21%21%0D%0Abss.&amp;langpair=flog%7Ces">Translation Example</a><br/><br/>This site is not affiliated with Google and is not against floggers or any internet community<br/><br/>©2008 Santiago Bruno</div>

</body>
</html>
