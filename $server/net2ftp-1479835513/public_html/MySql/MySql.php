<head>
<meta charset="utf-8">
</head>

<?php
if (!mysql_connect("u554877504_login", "u554877504_alex" ,"9948450")) {
echo "Ошибка подключения к серверу MySQL";
exit;
}
else
{
	echo 'Соединение успешно установлено';
}
?>