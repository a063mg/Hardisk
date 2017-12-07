<html>
<head>
  <meta charset="UTF-8">
  <title>Verstka</title>
  <link rel="stylesheet" href="styles/reset.css">
  <link rel="stylesheet" href="styles/style_enter.css">

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
<span id="form_txt" class="form_txt">Зарегестрируйтесь или войдите</span>
<form class="enter" action="http://alekseev700.esy.es/Site/index.php" method="post">
<a class="form_txt login_txt">Логин: </a><input class="edit" type="text" name="Login" value=""><br>
<a class="form_txt">Пароль: </a><input class="edit" type="password" name="Password" value=""><br><br><br>
<button type="submit" name="button" class="regist">Войти</button> 
<a href="http://alekseev700.esy.es/Site/regist.php" class="regist">Pегистрация</a>
</form>
</div></center>

  <script text="javascript">
     var url =  window.location.search;
     if (url == "?error"){
     	document.getElementById("form_txt").innerHTML="Неверный логин или пароль";
     }
     else{
     	document.getElementById("form_txt").innerHTML="Зарегестрируйтесь или войдите";
     }
  </script>
  </body>
</html>
