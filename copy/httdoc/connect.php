<?php 
$user = 'root';
$password = 'root';
$db = 'Pass';
$host = 'localhost';
$table = 'Login';

$connect_to_db = mysqli_connect($host, $user, $password)
or die("Could not connect: " . mysqli_error());

mysqli_select_db($connect_to_db, $db)
or die("Could not select DB: " . mysql_error());

$qr_result = mysqli_query( $connect_to_db, "select * from " . $table)
or die(mysqli_error());

$data = mysqli_fetch_array($qr_result);

echo $data['Login'];
?>