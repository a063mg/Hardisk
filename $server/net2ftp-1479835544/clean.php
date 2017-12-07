<?php
$link = $_GET['q'];
$file = fopen("coordinates.txt", "w");
$test = fwrite($file, "");
fclose($file);
?>