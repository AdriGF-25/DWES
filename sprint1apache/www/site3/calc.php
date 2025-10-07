<?php
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $a = $_POST['num1'];
    $b = $_POST['num2'];
    $op = $_POST['operacion'];

    switch ($op) {
        case 'suma':
            $res = $a + $b;
            echo "$a + $b = $res";
            break;
        case 'resta':
            $res = $a - $b;
            echo "$a - $b = $res";
            break;
        case 'multiplicacion':
            $res = $a * $b;
            echo "$a * $b = $res";
            break;
        case 'division':
            if ($b == 0) {
                echo "Error: División por cero";
            } else {
                $res = $a / $b;
                echo "$a / $b = $res";
            }
            break;
    }
}
?>

<form method="post" action="">
    Número 1: <input type="text" name="num1" required><br>
    Número 2: <input type="text" name="num2" required><br>
    Operación:
    <select name="operacion" required>
        <option value="suma">Suma</option>
        <option value="resta">Resta</option>
        <option value="multiplicacion">Multiplicación</option>
        <option value="division">División</option>
    </select><br>
    <button type="submit">Calcular</button>
</form>
