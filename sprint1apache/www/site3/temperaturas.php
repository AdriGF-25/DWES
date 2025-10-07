<?php
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $c = $_POST['cantidad'];
    $conv = $_POST['conversion'];
    if ($conv == 'c_a_f') {
        $res = $c * 9/5 + 32;
        echo "$c °C = $res °F";
    } elseif ($conv == 'f_a_c') {
        $res = ($c - 32) * 5/9;
        echo "$c °F = $res °C";
    }
}
?>

<form method="post" action="">
    Cantidad: <input type="number" step="any" name="cantidad" required><br>
    <input type="radio" name="conversion" value="c_a_f" required> Celsius → Fahrenheit<br>
    <input type="radio" name="conversion" value="f_a_c" required> Fahrenheit → Celsius<br>
    <button type="submit">Convertir</button>
</form>
