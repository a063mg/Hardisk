<!DOCTYPE html>
<html>
<head>
	<title>Mikhail Alekseev</title>
	<link rel="stylesheet" type="text/css" href="styles/reset.css">
	<link href="https://fonts.googleapis.com/css?family=Raleway" rel="stylesheet">
	<link rel="stylesheet" type="text/css" href="styles/style.css">
</head>
<body>

	<header>
		<a class="header_text">Mikhail Alekseev</a>
		<a href="https://www.instagram.com/m_alekseev/?hl=ru" class="insta"></a>
	</header>

	<div class="gallery">
<?php
    $directory = "./photo";    // Папка с изображениями
    $allowed_types=array("jpg", "png", "gif");  //разрешеные типы изображений
    $file_parts = array();
      $ext="";
      $title="";
      $i=0;
    //пробуем открыть папку
      $dir_handle = @opendir($directory) or die("Ошибка при открытии папки !!!");
    while ($file = readdir($dir_handle))    //поиск по файлам
      {
      if($file=="." || $file == "..") continue;  //пропустить ссылки на другие папки
      $file_parts = explode(".",$file);          //разделить имя файла и поместить его в массив
      $ext = strtolower(array_pop($file_parts));   //последний элеменет - это расширение


      if(in_array($ext,$allowed_types))
      {
      echo '<div class="photo" style="background-image: url(photo/'.$file.');">
           </div>';
     $i++;
      }

      }
    closedir($dir_handle);  //закрыть папку
    ?>
		<div class="photo" style="background-image: url(photo/photo1.png);">
			<div class="layer"><a href="" class="gallery_text">Vine</a></div>
		</div>
	</div>



</body>
</html>