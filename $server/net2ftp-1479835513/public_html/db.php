<!-- <?php
$host = "mysql.hostinger.ru";
$user = "u554877504_admin";
$password = "7777777";

// Производим попытку подключения к серверу MySQL:
$conn = mysqli_connect($host, $user, $password, "u554877504_alex");
if (!$conn)
{
die("Connected failed ".mysqli_connect_error());
}
echo "Connected succesfull!";

 //Выбираем базу данных:
 // $db_select = mysqli_select_db($conn, "u554877504_alex");
 // if (!$db_select) {
 //     die("Database selection failed: ".mysqli_error($conn));
 // }

// Выводим заголовок таблицы:

 // SQL-запрос:
$q = mysqli_query($conn, "SELECT * FROM Pass");
  if ($q == False){
   	echo "1";
    }
  // $q = mysqli_query($db, "SELECT * FROM Pass");

//echo "В таблице mytable ".mysql_num_rows($q)." записей";
// Выводим таблицу:
  for ($c=0; $c<mysqli_num_rows($q); $c++)
  {

  $f = mysqli_fetch_array($q);
  echo $f;
  echo $f[login];

  }
?> -->

<?php 
    // определяем начальные данные
    $db_host = 'mysql.hostinger.ru';
    $db_name = 'u554877504_alex';
    $db_username = 'u554877504_admin';
    $db_password = '7777777';
    $db_table_to_show = 'Pass';

    // соединяемся с сервером базы данных
    $connect_to_db = mysqli_connect($db_host, $db_username, $db_password)
    or die("Could not connect: " . mysqli_error());

    // подключаемся к базе данных
    mysqli_select_db($connect_to_db, $db_name)
    or die("Could not select DB: " . mysql_error());

    // выбираем все значения из таблицы "student"
    $qr_result = mysqli_query( $connect_to_db, "select * from " . $db_table_to_show)
    or die(mysqli_error());

    // выводим на страницу сайта заголовки HTML-таблицы
    echo '<table border="1">';
  echo '<thead>';
  echo '<tr>';
  echo '<th>Key</th>';
  echo '<th>Login</th>';
  echo '<th>Password</th>';
  echo '<th>Email</th>';
  echo '</tr>';
  echo '</thead>';
  echo '<tbody>';
  
   // выводим в HTML-таблицу все данные клиентов из таблицы MySQL 
  while($data = mysqli_fetch_array($qr_result)){ 
    echo '<tr>';
    echo '<td>' . $data['Key'] . '</td>';
    echo '<td>' . $data['Login'] . '</td>';
    echo '<td>' . $data['Password'] . '</td>';
    echo '<td>' . $data['Email'] . '</td>';
    echo '</tr>';
  }
  
    echo '</tbody>';
  echo '</table>';

    // закрываем соединение с сервером  базы данных
    mysqli_close($connect_to_db);
?>


