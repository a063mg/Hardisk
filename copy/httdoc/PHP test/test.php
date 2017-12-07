<?php 
// $file = file_get_contents('down4.jpg');
// echo $file;

$echo = false;
$img = 'down4.jpg';
function insert_base64_encoded_image($img, $echo){
	$imageSize = getimagesize($img);
	$imageData = base64_encode(file_get_contents($img));
	$imageHTML = "<img src='data:{$imageSize['mime']};base64,{$imageData}' {$imageSize[3]} />";
	if($echo == true){
		echo $imageHTML;
	} else {
		return $imageData;
	}
}
$file = insert_base64_encoded_image($img, $echo);
echo $file;



?>