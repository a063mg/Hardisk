<!DOCTYPE html>
<html>
  <head>
    <meta charset="utf-8">
    <title>Login</title>
    <link rel="stylesheet" href="styles/reset.css">
    <link rel="stylesheet" href="styles/regist_style.css">
    <link href="https://fonts.googleapis.com/css?family=Quicksand" rel="stylesheet">
  </head>
  <body>
    <header class="header">
      <center><a href="#" class="header_txt">Lecipher</a></center>
    </header>

    <section>
      <center><div class="form"><br>
      <div class="regist_header_text"><span id="form_txt" class="form_txt">Регистрация</span><div>
      <form class="enter" action="regist.php" method="post"><br>
      <div class="form_item"><input class="edit" type="text" name="Email" placeholder=" E-mail" value="">
      <input class="edit password" type="text" name="Login" placeholder=" Логин" value="">
      <input class="edit password_repeat" type="password" name="Password" placeholder=" Пароль" value="">
      <input class="edit" type="password" name="Password_repeat" placeholder=" Повторите Пароль" value=""></div>
      <div class="item_button"><a href="enter.php" class="button_text_regist">Уже есть аккаунт?</a><button type="submit" name="button" class="regist">Pегистрация</button></div>
      </form>
      </div></center>
    </section>

    <!-- <div class="container">
        <div class="line"></div>
        <center><a class="split">Lecipher | Программа</a><br>
        <a class="split">© 2017 | Россия, г. Москва</a></center>
    </div> -->

    <script src="https://cdnjs.cloudflare.com/ajax/libs/jquery.isotope/2.2.2/isotope.pkgd.js"></script>
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/2.2.0/jquery.min.js"></script>
    <script text="javascript">
      var url =  window.location.search;
      if (url == "?error"){
          document.getElementById("form_txt").innerHTML="Ошибка";
      }
      else if (url == "?password_not_confirm") {
          document.getElementById("form_txt").innerHTML="Пароли не совпадают";
      }
      else if (url == "?login_empty") {
          document.getElementById("form_txt").innerHTML='Поле "Логин" не заполнино';
      }
      else if (url == "?email_empty") {
          document.getElementById("form_txt").innerHTML='Поле "E-mail" не заполнино';
      }
      else if (url == "?login_exist") {
          document.getElementById("form_txt").innerHTML="Такой логин уже существует";
      }
      else if (url == "?email_exist") {
          document.getElementById("form_txt").innerHTML='Такой "E-mail" уже существует';
      }
      else if (url == "?password_empty") {
          document.getElementById("form_txt").innerHTML='Поле "Пароль" не заполнино';
      }
      else{
      document.getElementById("form_txt").innerHTML="Регистрация";
      }
   </script>
  </body>
</html>
