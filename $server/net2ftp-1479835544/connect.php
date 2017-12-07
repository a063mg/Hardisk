<?php
$link = $_GET['q'];
echo $link;
$file = fopen("coordinates.txt", "a");
fwrite($file, $link."\n");
fclose($file);
?>