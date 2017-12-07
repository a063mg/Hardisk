<?php
$host = "mysql.hostinger.ru";
$user = "u554877504_admin";
$password = "7777777";

$conn = mysqli_connect($host, $user, $password);
if (!$conn)
{
die("Connected failed ".mysqli_connect_error());
}
echo "Connected succesfull!";

 mysqli_select_db($conn, "u554877504_alex");

// SQL-запрос
$result = SELECT * FROM "pass" or die(mysql_error());

//$rs = mysql_query($strSQL);
echo $result;

while ($row = mysql_fetch_assoc($result)) {
    
    $name = $row['Login'];
    $pass = $row['Password'];
        
    echo $name;
    echo $pass;
}
?>


