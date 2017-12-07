<?php
	include_once("db.php");

    $user = 'null';
    $login = $_POST['Login'];
    $password = $_POST['Password'];

    if (empty($_SESSION['password']) or empty($_SESSION['login'])) {

    	if (empty($login) or empty($password) or (empty($login) and empty($password))) {
    	   header('Location: enter.php');
    	}

    	while($data = mysqli_fetch_array($qr_result)){
    		if ($data['Login'] == $login and $data['Password'] == $password){
        		$_SESSION['password'] = $password;
        		$_SESSION['login'] = $login;
        		$user = $_SESSION['login'];
      		}
    	}

    }
    else{

    	while($data = mysqli_fetch_array($qr_result)){
    		if ($data['Login'] == $_SESSION['login'] and $data['Password'] == $_SESSION['password']){
        		$user = $_SESSION['login'];
      		}
    	}

    }
if ($user == 'null')
{
  header('Location: enter.php?error');
}

mysqli_close($connect_to_db);
?>

<html>
  <head>
    <meta charset="utf-8">
    <link rel="stylesheet" href="styles/reset.css">
    <link rel="stylesheet" href="styles/main_style.css">
    <link href="https://fonts.googleapis.com/css?family=Quicksand" rel="stylesheet">
    <title>Lecipher</title>
  </head>
  <body>

<div class="block">
    <header class="header">
      <a href="#" align="center" class="header_txt">Lecipher</a>
    </header>
    <div class="header_block">
      <span class="login"><?php echo $user?><br></span><a href="exit.php" class="exit_button">Выйти</a></form>
    </div>
</div>


			<div class="from_block">
				<form  action=upload.php method=post enctype=multipart/form-data>
					<div class="fileform">
					<div id="fileformlabel"></div>
					<div class="selectbutton">Обзор</div>
					<input type="file" name="imgfile" id="upload" onchange="getName(this.value);" />
					</div>
					<center><input class="submit_button" type="submit" value="Отправить"></cenetr>
				</form>
			</div>


		<script type="text/javascript">
				function getName (str){
				if (str.lastIndexOf('\\')){
						var i = str.lastIndexOf('\\')+1;
				}
				else{
						var i = str.lastIndexOf('/')+1;
				}
				var filename = str.slice(i);
				var uploaded = document.getElementById("fileformlabel");
				uploaded.innerHTML = filename;
			  }
		</script>

  </body>
</html>
