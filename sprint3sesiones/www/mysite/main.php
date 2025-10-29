<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="utf-8">
<title>Main</title>
<style>
.item {
  transition: opacity 0.5s ease, transform 0.3s ease;
}

.item:hover {
  opacity: 0.7;
  transform: scale(1.03);
}
body {
  background: linear-gradient(180deg,#f7fbff,#ffffff);
  font-family: Arial, Helvetica, sans-serif;
  padding: 20px;
  position: relative;
}
h1 {
  text-align: center;
  text-transform: uppercase;
  letter-spacing: 1px;
  margin-bottom: 16px;
  color: #155;
  margin-top: 60px; /* Espacio adicional para separar el título de los botones */
}

.item {
  margin: 10px;
  text-align: center;
  width: 200px;
}

.item img {
  width: auto;
  height: 200px;
  display: block;
  margin: 0 auto;
}

div {
  display: inline-block;
  padding-right: 20px;
}

hr {
  border: 2px solid lightgreen;
}

hr {
  border: none;
  height: 2px;
  background: linear-gradient(90deg, transparent, #bfe6c8, transparent);
  margin: 18px 0;
}

.button-container {
  display: flex;
  justify-content: flex-start;
  gap: 20px;
  position: absolute;
  top: 20px;  /* Separación de 20px desde la parte superior de la página */
  right: 20px; /* Alineado a la derecha */
}

a[href="/logout.php"], .change-password-button {
  color: #0a5;
  text-decoration: none;
  padding: 8px 12px;
  border-radius: 6px;
  background: rgba(10,170,90,0.06);
  transition: background 180ms ease, transform 180ms ease;
}

a[href="/logout.php"]:hover, .change-password-button:hover {
  background: rgba(10,170,90,0.1);
  transform: scale(1.05);
}
</style>
</head>
<body>

<?php
session_start();
$db = mysqli_connect('localhost','root','1234','mysitedb') or die('Fail');
?>

<div class="button-container">
  <?php
  if (!empty($_SESSION['user_id'])) {
      echo '<a href="change_password.html" class="change-password-button">Cambiar Contraseña</a>
            <a href="/logout.php" class="change-password-button">Logout</a>';
  }
  ?>
</div>

<h1>Conexión establecida</h1>
<hr>
<hr>

<?php
$query = 'SELECT * FROM libros';
$result = mysqli_query($db, $query) or die('Query error');
while ($row = mysqli_fetch_array($result)) {
    echo '<div class="item">
         '.$row[0].'
         <br>
         '.$row[1].'
         <br>
         <a href="http://localhost:8084/detail.php?id='.$row[0].'"><img src='.$row[2].'></a>
         <br>S
         '.$row[3].'
         <br>
         '.$row[4].'
          <br>
          </div>';
}
?>

<?php
mysqli_close($db);
?>

<hr>
<hr>

<script>
document.addEventListener('DOMContentLoaded', function(){
  var lists = document.querySelectorAll('ul, ol');
  lists.forEach(function(l){
    l.classList.add('animated-list');
    Array.from(l.children).forEach(function(li){
      li.classList.add('animated-fade');
    });
  });
});
</script>

</body>
</html>
