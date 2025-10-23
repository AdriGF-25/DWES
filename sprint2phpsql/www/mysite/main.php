<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Mariadb</title>
  <style>
    h1{
      text-align: center;
      text-transform: uppercase; 
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
    div{
      display: inline-block;
      padding-right: 20px;
    }
    hr{
      border: 2px solid lightgreen;
      
    }
  </style>
</head>
<body>
  <?php
  $db = mysqli_connect('localhost','root','1234','mysitedb') or die('Fail');
?>
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
     <a href="http://localhost:8083/detail.php?id='.$row[0].'"><img src='.$row[2].'></a>
     <br>
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


</body>
</html>
