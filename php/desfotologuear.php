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
<?php require ("deflog.php");?>

    <?php
        $text = $_POST[text];
        if (!$text) {
            $text = $_GET[text];
        }

        $desmultiplicar = $_POST[desmultiplicar];
        if (empty($desmultiplicar)) {
            $desmultiplicar = $_GET[desmultiplicar];
        }
        if (empty($desmultiplicar) || $desmultiplicar == "on") {
            $desmultiplicar = 1;
        }
        else {
            $desmultiplicar = 0;
        }


        $deszezear = $_POST[deszezear];
        if (empty($deszezear)) {
            $deszezear = $_GET[deszezear];
        }
        if (empty($deszezear) || $deszezear == "off") {
            $deszezear = 0;
        }
        else {
            $deszezear = 1;
        }

        $deskar = $_POST[deskar];
        if (empty($deskar)) {
            $deskar = $_GET[deskar];
        }
        if (empty($deskar) || $deskar == "off") {
            $deskar = 0;
        }
        else {
            $deskar = 1;
        }

        $dessmsar = $_POST[dessmsar];
        if (empty($dessmsar)) {
            $dessmsar = $_GET[dessmsar];
        }
        if (empty($dessmsar) || $dessmsar == "on") {
            $dessmsar = 1;
        }
        else {
            $dessmsar = 0;
        }

        $desestupidizar = $_POST[desestupidizar];
        if (empty($desestupidizar)) {
            $desestupidizar = $_GET[desestupidizar];
        }
        if (empty($desestupidizar) || $desestupidizar == "on") {
            $desestupidizar = 1;
        }
        else {
            $desestupidizar = 0;
        }

        $desalternar = $_POST[desalternar];
        if (empty($desalternar)) {
            $desalternar = $_GET[desalternar];
        }
        if (empty($desalternar) || $desalternar == "on") {
            $desalternar = 1;
        }
        else {
            $desalternar = 0;
        }

        $desporteniar = $_POST[desporteniar];
        if (empty($desporteniar)) {
            $desporteniar = $_GET[desporteniar];
        }
        if (empty($desporteniar) || $desporteniar == "on") {
            $desporteniar = 1;
        }
        else {
            $desporteniar = 0;
        }

        $deleet = $_POST[deleet];
        if (empty($deleet)) {
            $deleet = $_GET[deleet];
        }
        if (empty($deleet) || $deleet == "on") {
            $deleet = 1;
        }
        else {
            $deleet = 0;
        }

        $fixmissingvowels = $_POST[fixmissingvowels];
        if (empty($fixmissingvowels)) {
            $fixmissingvowels = $_GET[fixmissingvowels];
        }
        if (empty($fixmissingvowels) || $fixmissingvowels == "on") {
            $fixmissingvowels = 1;
        }
        else {
            $fixmissingvowels = 0;
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
                        $result = tohtml(stripslashes($word));

                        if ($deleet) {
                            $result = deleet($result);
                        }

                        if ($desalternar) {
                            $result = desalternar($result);
                        }

                        if ($desmultiplicar) {
                            $result = desmultiplicar($result);
                        }

                        if ($dessmsar) {
                            $result = desms($result);
                        }

                        if ($desestupidizar) {
                            $result = desestupidizar($result);
                        }

                        if ($deszezear) {
                            $result = deszezear($result);
                        }

                        if ($deskar) {
                            $result = desk($result);
                        }

                        if ($desporteniar) {
                            $result = desporteniar($result);
                        }

                        if ($fixmissingvowels) {
                            $result = fixmissingvowels($result);
                        }

                        echo $result;
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
                <td class="select_metodos_title"> M&eacute;todos a aplicar al texto:</td>
                </tr>

                <tr>
                <td>Desmultiplicar</td>
                <td><input type="radio" name="desmultiplicar" value="on" <?php if ($desmultiplicar) { echo "CHECKED"; } ?> > Si</td>
                <td><input type="radio" name="desmultiplicar" value="off" <?php if (!$desmultiplicar) { echo "CHECKED"; } ?>> No</td>
                </tr>

                <tr>
                <td>Deszezear</td>
                <td><input type="radio" name="deszezear" value="on" <?php if ($deszezear) { echo "CHECKED"; } ?> > Si</td>
                <td><input type="radio" name="deszezear" value="off" <?php if (!$deszezear) { echo "CHECKED"; } ?>> No</td>
                </tr>

                <tr>
                <td>Des-k-ar</td>
                <td><input type="radio" name="deskar" value="on" <?php if ($deskar) { echo "CHECKED"; } ?> > Si</td>
                <td><input type="radio" name="deskar" value="off" <?php if (!$deskar) { echo "CHECKED"; } ?>> No</td>
                </tr>

                <tr>
                <td>DesSMSar</td>
                <td><input type="radio" name="dessmsar" value="on" <?php if ($dessmsar) { echo "CHECKED"; } ?> > Si</td>
                <td><input type="radio" name="dessmsar" value="off" <?php if (!$dessmsar) { echo "CHECKED"; } ?>> No</td>
                </tr>

                <tr>
                <td>Desestupidizar</td>
                <td><input type="radio" name="desestupidizar" value="on" <?php if ($desestupidizar) { echo "CHECKED"; } ?> > Si</td>
                <td><input type="radio" name="desestupidizar" value="off" <?php if (!$desestupidizar) { echo "CHECKED"; } ?>> No</td>
                </tr>

                <tr>
                <td>Desalternar</td>
                <td><input type="radio" name="desalternar" value="on" <?php if ($desalternar) { echo "CHECKED"; } ?> > Si</td>
                <td><input type="radio" name="desalternar" value="off" <?php if (!$desalternar) { echo "CHECKED"; } ?>> No</td>
                </tr>

                <tr>
                <td>Desporteñar</td>
                <td><input type="radio" name="desporteniar" value="on" <?php if ($desporteniar) { echo "CHECKED"; } ?> > Si</td>
                <td><input type="radio" name="desporteniar" value="off" <?php if (!$desporteniar) { echo "CHECKED"; } ?>> No</td>
                </tr>

                <tr>
                <td>Deleet</td>
                <td><input type="radio" name="deleet" value="on" <?php if ($deleet) { echo "CHECKED"; } ?> > Si</td>
                <td><input type="radio" name="deleet" value="off" <?php if (!$deleet) { echo "CHECKED"; } ?>> No</td>
                </tr>


                <tr>
                <td>Fix missing vowels</td>
                <td><input type="radio" name="fixmissingvowels" value="on" <?php if ($fixmissingvowels) { echo "CHECKED"; } ?> > Si</td>
                <td><input type="radio" name="fixmissingvowels" value="off" <?php if (!$fixmissingvowels) { echo "CHECKED"; } ?>> No</td>
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
    <a href="http://www.santiagobruno.com.ar/programas.html#deflog">More info on my website</a> - <a href="http://cervezaconlupines.blogspot.com/2008/03/presentando-deflog.html">About This Shit</a> - <a href="desfotologuear.php?text=LocURaAAaaA%21%21%21%0D%0Ake+loko+estoooo+mIeRdA%21%21%21%0D%0A%0D%0AAaAaAAAaaAiiiii++firmeeennnn+leeemmmddoooo%21%21%21%0D%0A%0D%0Anuc+k+pasa+ak.+t+voi+a+ver+dsp.%0D%0Aqe+andes+d+mil%21%21%0D%0AbesOtte%0D%0A%0D%0Aesto+q+m+dijistes+ta+groxo+maallll+grax+xq+m+dijistessss+cdo+lo+vistessssss%0D%0A%0D%0Atoy+reeee+lokooo+blds%21%21%0D%0Aaahhrrreee%0D%0At+qiero%2C+we%2C+chauuuu%21%21%21%0D%0Abss.%0D%0Aazi+ez+ezto%2C+nos+vems%2C+stamos.+dspu%E9s+dcime.+4gu4n73+a77aqu3%0D%0Ajkajkajkaajkajk">Translation Example</a><br/><br/>This site is not affiliated with Google and is not against floggers or any internet community<br/><br/>©2008 Santiago Bruno</div>

</body>
</html>
