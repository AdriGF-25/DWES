<?php
session_start();
if ($_SERVER['REQUEST_METHOD'] !== 'POST') {
    header('Location: change_password.html');
    exit;
}
if (empty($_SESSION['user_id'])) {
    echo 'Debes iniciar sesión.<br><a href="login.html">Login</a>';
    exit;
}
$current = $_POST['current_password'] ?? '';
$new = $_POST['new_password'] ?? '';
$confirm = $_POST['confirm_password'] ?? '';
if ($current === '' || $new === '' || $confirm === '') {
    echo 'Rellena todos los campos.<br><a href="change_password.html">Volver</a>';
    exit;
}
if ($new !== $confirm) {
    echo 'Las contraseñas nuevas no coinciden.<br><a href="change_password.html">Volver</a>';
    exit;
}
$host = 'localhost';
$db   = 'mysitedb';
$user = 'root';
$pass = '1234';
$dsn = "mysql:host=$host;dbname=$db;charset=utf8mb4";
try {
    $pdo = new PDO($dsn, $user, $pass, [PDO::ATTR_ERRMODE => PDO::ERRMODE_EXCEPTION]);
} catch (Exception $e) {
    echo 'Error de conexión a la base de datos.<br>';
    exit;
}
try {
    $stmt = $pdo->prepare('SELECT password FROM usuarios WHERE id = ? LIMIT 1');
    $stmt->execute([$_SESSION['user_id']]);
    $row = $stmt->fetch(PDO::FETCH_ASSOC);
    if (!$row) {
        echo 'Usuario no encontrado.<br><a href="main.php">Volver</a>';
        exit;
    }
    if (!password_verify($current, $row['password'])) {
        echo 'Contraseña actual incorrecta.<br><a href="change_password.html">Volver</a>';
        exit;
    }
    $hash = password_hash($new, PASSWORD_DEFAULT);
    $up = $pdo->prepare('UPDATE usuarios SET password = ? WHERE id = ?');
    $up->execute([$hash, $_SESSION['user_id']]);
    echo 'Contraseña actualizada.<br><a href="main.php">Volver</a>';
    exit;
} catch (Exception $e) {
    echo 'Error.<br><a href="change_password.html">Volver</a>';
    exit;
}
?>