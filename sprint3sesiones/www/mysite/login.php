<?php
ini_set('display_errors',1);
error_reporting(E_ALL);
session_start();

$host = 'localhost';
$db   = 'mysitedb';
$user = 'root';
$pass = '1234';
$dsn = "mysql:host=$host;dbname=$db;charset=utf8mb4";

if ($_SERVER['REQUEST_METHOD'] !== 'POST') {
    header('Location: login.html');
    exit;
}

$email = trim($_POST['f_email'] ?? '');
$password = $_POST['f_password'] ?? '';

if ($email === '' || $password === '') {
    echo 'Rellena todos los campos.<br><a href="login.html">Volver</a>';
    exit;
}

if (!filter_var($email, FILTER_VALIDATE_EMAIL)) {
    echo 'Email no válido.<br><a href="login.html">Volver</a>';
    exit;
}

try {
    $pdo = new PDO($dsn, $user, $pass, [PDO::ATTR_ERRMODE => PDO::ERRMODE_EXCEPTION]);
} catch (Exception $e) {
    echo 'Error de conexión a la base de datos.<br>';
    exit;
}

try {
    $stmt = $pdo->prepare('SELECT id, nombre, apellidos, password FROM usuarios WHERE email = ? LIMIT 1');
    $stmt->execute([$email]);
    $userRow = $stmt->fetch(PDO::FETCH_ASSOC);

    if (!$userRow) {
        echo 'Email no encontrado.<br><a href="login.html">Volver</a>';
        exit;
    }

    if (!password_verify($password, $userRow['password'])) {
        echo 'Contraseña incorrecta.<br><a href="login.html">Volver</a>';
        exit;
    }
    $_SESSION['user_id'] = $userRow['id'];
    $_SESSION['user_name'] = $userRow['nombre'] . ' ' . $userRow['apellidos'];

    header('Location: main.php');
    exit;
} catch (Exception $e) {
    echo 'Error: ' . htmlspecialchars($e->getMessage()) . '<br><a href="login.html">Volver</a>';
    exit;
}
?>