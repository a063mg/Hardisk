<html>
<head>
  <meta charset="UTF-8">
  <title>Verstka</title>
  <link rel="stylesheet" href="styles/reset.css">
  <link rel="stylesheet" href="styles/regist_style.css">
</head>
  <body>
<!--WHALTER>WHITE www.metwan.net-->


<header><br><br>
<a class="header_txt">Нa глaвнyю</a>
<a class="header_txt">Зaдaчи</a>
<a class="header_txt">Пoдгoтовкa</a>
<a class="header_txt">Кyрсы</a>
<a class="header_txt">Об прoгрaммe</a>
</header><br>
<!--WHALTER>WHITE www.metwan.net-->


<center><div class="form"><br>
<span id="form_txt" class="form_header">Регистрация</span>
<form class="enter" action="http://alekseev700.esy.es/Site/reg.php" method="post">
<div class="form_txt">Email: </div><input class="edit" type="text" name="Email" value="">
<div class="form_txt">Логин: </div><input class="edit" type="text" name="Login" value="">
<div class="form_txt">Пароль: </div><input class="edit" type="password" name="Password" value="">
<div class="form_txt">Повторите пароль: </div><input class="edit" type="password" name="Password_repeat" value=""><br><br><br>
<button type="submit" name="button" class="regist">Pегистрация</button></center><br>
<!--<a class="submit_button" type="submit">Зарегистрироваться</a>-->
</form>
</div><br>
<!--WHALTER>WHITE www.metwan.net-->


<div class="vk_btn">Войти через ВК</div>
  <script src="https://ajax.googleapis.com/ajax/libs/jquery/2.2.0/jquery.min.js"></script>
  <script text="javascript">
     var url =  window.location.search;
     if (url == "?error"){
     	document.getElementById("form_txt").innerHTML="Неверный логин или пароль";
     }
     else{
     	document.getElementById("form_txt").innerHTML="Регистрация";
     }
  </script>
  </body>
</html>
