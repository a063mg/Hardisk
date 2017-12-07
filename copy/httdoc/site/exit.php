<?php
include_once("index.php");

unset($_SESSION['password']);
unset($_SESSION['login']);

header('Location: enter.php');
?>
