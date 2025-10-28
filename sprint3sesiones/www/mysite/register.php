<?php
ini_set('display_errors', 1);
ini_set('display_startup_errors', 1);
error_reporting(E_ALL);

$host = 'localhost';
$db   = 'mysitedb';
$user = 'root';
$pass = '1234';
$dsn = "mysql:host=$host;dbname=$db;charset=utf8mb4";

if ($_SERVER['REQUEST_METHOD'] !== 'POST') {
    header('Location: register.html');
    exit;
}

$nombre   = trim($_POST['nombre'] ?? '');
$apellidos= trim($_POST['apellidos'] ?? '');
$email    = trim($_POST['email'] ?? '');
$p1       = $_POST['password1'] ?? '';
$p2       = $_POST['password2'] ?? '';

if ($nombre === '' || $apellidos === '' || $email === '' || $p1 === '' || $p2 === '') {
    echo 'Rellena todos los campos.'; exit;
}
if (!filter_var($email, FILTER_VALIDATE_EMAIL)) { echo 'Email no válido.'; exit; }
if ($p1 !== $p2) { echo 'Las contraseñas no coinciden.'; exit; }

try {
    $pdo = new PDO($dsn, $user, $pass, [PDO::ATTR_ERRMODE => PDO::ERRMODE_EXCEPTION]);
} catch (Exception $e) {
    echo 'Error de conexión: ' . htmlspecialchars($e->getMessage());
    exit;
}

try {
    $stmt = $pdo->prepare('SELECT id FROM usuarios WHERE email = ? LIMIT 1');
    $stmt->execute([$email]);
    if ($stmt->fetch()) { echo 'El correo ya existe.'; exit; }

    $hash = password_hash($p1, PASSWORD_DEFAULT);
    $ins = $pdo->prepare('INSERT INTO usuarios (nombre, apellidos, email, password) VALUES (?, ?, ?, ?)');
    $ins->execute([$nombre, $apellidos, $email, $hash]);

    header('Location: main.php');
    exit;
} catch (Exception $e) {
    echo 'Error: ' . htmlspecialchars($e->getMessage());
    exit;
}
?>