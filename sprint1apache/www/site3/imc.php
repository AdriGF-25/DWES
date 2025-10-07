<?php
function calcular_imc($peso, $altura) {
    return $peso / ($altura * $altura);
}

$peso = isset($_GET['peso']) ? floatval($_GET['peso']) : null;
$altura = isset($_GET['altura']) ? floatval($_GET['altura']) : null;

if ($peso !== null && $altura !== null && $peso > 0 && $altura > 0) {
    $imc = calcular_imc($peso, $altura);

    echo "IMC: $imc<br>";

    if ($imc < 18.5) {
        echo "Bajo peso";
    } elseif ($imc <= 24.9) {
        echo "Normal";
    } else {
        echo "Sobrepeso";
    }
}
?>
