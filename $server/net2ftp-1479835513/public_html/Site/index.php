<?php
$file = file_get_contents('Pass/pass.json');
$json = json_decode($file, TRUE);
$user = 'null';
$login = $_POST['Login']; 
$password = $_POST['Password'];
if (empty($login) or empty($password)) {
  echo '<meta http-equiv="refresh" content="0;URL=http://alekseev700.esy.es/Site/enter.php">';
} 
foreach($json as $item)
{
    if ($item['Login'].$item['Password'] == $login.$password){
      $user = $login;
    }
}
if ($user == 'null')
{
  echo '<meta http-equiv="refresh" content="0;URL=http://alekseev700.esy.es/Site/enter.php?error">';
}
?>
<html>
<head>
  <meta charset="UTF-8">
  <title>Verstka</title>
  <link rel="stylesheet" href="styles/reset.css">
  <link rel="stylesheet" href="styles/style.css">
  <link rel="stylesheet" type="text/css" href="Slick/slick-1.5.9/slick/slick.css">
  <link rel="stylesheet" type="text/css" href="Slick/slick-1.5.9/slick/slick-theme.css">
</head>
  <body>


<header><br><br>
<a class="header_txt">Нa глaвнyю</a>
<a class="header_txt">Зaдaчи</a>
<a class="header_txt">Пoдгoтовкa</a>
<a class="header_txt">Кyрсы</a>
<a class="header_txt">Об прoгрaммe</a>
<span class="login"><?php echo $user;?></span>
</header><br>
</div></center>
  </body>
</html>
