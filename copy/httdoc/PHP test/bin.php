<?php 
$word = 'artem';
$key = 'misha';

$file = file_get_contents('down4.jpg');

function RandomString($max)
{
    $characters = '01';
    $randstring = '';
    for ($i = 0; $i < $max; $i++) {
        $randstring .= $characters[rand(0, strlen($characters)-1)];
    }
    return $randstring;
}
function encode($str){
	for ($i = 0; $i < strlen($str); $i++) {
		$char = $str[$i];
		$bin .= decbin(ord($char)); 
	}
	return $bin;
}


function shifr($word, $key){
	$code = '';
	$j = 0;
	for ($j=0; $j < strlen($word); $j++){
		if ($key[$j] == $word[$j]){
			$code .= '0';
		}
		else{
			$code .= '1';
		}
	}
	return $code;
}

$file = encode($file);
$max = strlen($file);
$ran = RandomString($max);

echo $file;
echo '<br>';
echo $ran;
echo '<br>';
echo strlen($ran);
echo '<br>';
echo strlen($file);
echo '<br>';
$code = shifr($file, $ran);
echo $code;
$bin = $code;
echo '<br>';
for ($i = 0; $i < strlen($bin); $i+=6) {
	$char = $bin[$i].$bin[$i+1].$bin[$i+2].$bin[$i+3].$bin[$i+4].$bin[$i+5];
	$ans .= chr(bindec($char));
}
echo $ans;


// ________________________________________________________________________________________________________________________________________

echo '<br>';
echo '<br>';
$buf = encode($ans);
echo $buf;
$imgbin = shifr($buf, $ran);
echo $imgbin;














?>