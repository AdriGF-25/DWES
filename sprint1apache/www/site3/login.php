<?php
if ($_POST) {
    if ($_POST['usuario'] == 'admin' && $_POST['contrasena'] == '1234') {
        echo "Acceso concedido";
    } else {
        echo "Acceso denegado";
    }
}
?>

<form method="post">
    Usuario: <input name="usuario"><br>
    Contraseña: <input name="contrasena" type="password"><br>
    <button>Entrar</button>
</form>
