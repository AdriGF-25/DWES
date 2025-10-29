<?php
$db = mysqli_connect('localhost', 'root', '1234', 'mysitedb') or die('Fail');
session_start();
?>
<html>
<body>
<?php
    $user_id_a_insertar = 'NULL';
    if (!empty($_SESSION['user_id'])) {
        $user_id_a_insertar = $_SESSION['user_id']; 
    }


    if (!isset($_POST['libro_id']) || !isset($_POST['new_comment'])) {
        echo 'Faltan datos.<br><a href="javascript:history.back()">Volver</a>';
        exit;
    }

    $libro_id = $_POST['libro_id'];
    $comentario = $_POST['new_comment'];


    $comentario = mysqli_real_escape_string($db, $comentario);


    $query = "INSERT INTO comentarios(comentario, libro_id, usuario_id)
              VALUES ('".$comentario."', ".$libro_id.", ".$user_id_a_insertar.")";

    if (!mysqli_query($db, $query)) {
        die('Error al insertar comentario: ' . mysqli_error($db));
    }

    echo "<p>Nuevo comentario añadido por ID de usuario " . $user_id_a_insertar . ".</p>";
    echo "<p>Comentario ID: " . mysqli_insert_id($db) . "</p>";
    echo "<a href='/detail.php?id=".$libro_id."'>Volver</a>";

    mysqli_close($db);
?>
</body>
</html>
