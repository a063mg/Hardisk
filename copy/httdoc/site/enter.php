<!DOCTYPE html>
<html>
  <head>
    <meta charset="utf-8">
    <link rel="stylesheet" href="styles/reset.css">
    <link rel="stylesheet" href="styles/enter_style.css">
    <link href="https://fonts.googleapis.com/css?family=Quicksand" rel="stylesheet">
    <title>Enter</title>
  </head>
  <body>
    <header class="header">
      <center><a href="#" class="header_txt">Lecipher</a></center>
    </header>

    <section>
      <center><div class="form"><br>
      <div class="regist_header_text"><span id="form_txt" class="form_txt">Вход</span></div>
      <form class="enter" action="index.php" method="post"><br>
      <div class="form_item"><input class="edit password" type="text" name="Login" placeholder=" Логин" value="">
      <input class="edit password_repeat" type="password" name="Password" placeholder=" Пароль" value=""></div>
      <div class="item_button"><a href="login.php" class="button_text_regist">Регистрация</a><button type="submit" name="button" class="regist">Вход</button></div>
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
          document.getElementById("form_txt").innerHTML="Неверный Логин или Пароль";
      }
      else if (url == "?login_empty") {
          document.getElementById("form_txt").innerHTML='Поле "Логин" не заполнино';
      }
      else if (url == "?password_empty") {
          document.getElementById("form_txt").innerHTML='Поле "Пароль" не заполнино';
      }
      else{
          document.getElementById("form_txt").innerHTML="Вход";
      }
   </script>
  </body>
</html>
