<?php

function encode($word){
	$bin = '';
	for($i=0; $i<strlen($word); $i++){
		$char = $word[$i];
		if($char == 'A'){
			$bin .= '000000';
		}
		if($char == 'B'){
			$bin .= '000001';
		}
		if($char == 'C'){
			$bin .= '000010';
		}
		if($char == 'D'){
			$bin .= '000011';
		}
		if($char == 'E'){
			$bin .= '000100';
		}
		if($char == 'F'){
			$bin .= '000101';
		}
		if($char == 'G'){
			$bin .= '000110';
		}
		if($char == 'H'){
			$bin .= '000111';
		}
		if($char == 'I'){
			$bin .= '001000';
		}
		if($char == 'J'){
			$bin .= '001001';
		}
		if($char == 'K'){
			$bin .= '001010';
		}
		if($char == 'L'){
			$bin .= '001011';
		}
		if($char == 'M'){
			$bin .= '001100';
		}
		if($char == 'N'){
			$bin .= '001101';
		}
		if($char == 'O'){
			$bin .= '001110';
		}
		if($char == 'P'){
			$bin .= '001111';
		}
		if($char == 'Q'){
			$bin .= '010000';
		}
		if($char == 'R'){
			$bin .= '010001';
		}
		if($char == 'S'){
			$bin .= '010010';
		}
		if($char == 'T'){
			$bin .= '010011';
		}
		if($char == 'U'){
			$bin .= '010100';
		}
		if($char == 'V'){
			$bin .= '010101';
		}
		if($char == 'W'){
			$bin .= '010110';
		}
		if($char == 'X'){
			$bin .= '010111';
		}
		if($char == 'Y'){
			$bin .= '011000';
		}
		if($char == 'Z'){
			$bin .= '011001';
		}
		if($char == 'a'){
			$bin .= '011010';
		}
		if($char == 'b'){
			$bin .= '011011';
		}
		if($char == 'c'){
			$bin .= '011100';
		}
		if($char == 'd'){
			$bin .= '011101';
		}
		if($char == 'e'){
			$bin .= '011110';
		}
		if($char == 'f'){
			$bin .= '011111';
		}
		if($char == 'g'){
			$bin .= '100000';
		}
		if($char == 'h'){
			$bin .= '100001';
		}
		if($char == 'i'){
			$bin .= '100010';
		}
		if($char == 'j'){
			$bin .= '100011';
		}
		if($char == 'k'){
			$bin .= '100100';
		}
		if($char == 'l'){
			$bin .= '100101';
		}
		if($char == 'm'){
			$bin .= '100110';
		}
		if($char == 'n'){
			$bin .= '100111';
		}
		if($char == 'o'){
			$bin .= '101000';
		}
		if($char == 'p'){
			$bin .= '101001';
		}
		if($char == 'q'){
			$bin .= '101010';
		}
		if($char == 'r'){
			$bin .= '101011';
		}
		if($char == 's'){
			$bin .= '101100';
		}
		if($char == 't'){
			$bin .= '101101';
		}
		if($char == 'u'){
			$bin .= '101110';
		}
		if($char == 'v'){
			$bin .= '101111';
		}
		if($char == 'w'){
			$bin .= '110000';
		}
		if($char == 'x'){
			$bin .= '110001';
		}
		if($char == 'y'){
			$bin .= '110010';
		}
		if($char == 'z'){
			$bin .= '110011';
		}
		if($char == '0'){
			$bin .= '110100';
		}
		if($char == '1'){
			$bin .= '110101';
		}
		if($char == '2'){
			$bin .= '110110';
		}
		if($char == '3'){
			$bin .= '110111';
		}
		if($char == '4'){
			$bin .= '111000';
		}
		if($char == '5'){
			$bin .= '111001';
		}
		if($char == '6'){
			$bin .= '111010';
		}
		if($char == '7'){
			$bin .= '111011';
		}
		if($char == '8'){
			$bin .= '111100';
		}
		if($char == '9'){
			$bin .= '111101';
		}
		if($char == '+'){
			$bin .= '111110';
		}
		if($char == '/'){
			$bin .= '111111';
		}
	}
	return $bin;
}

function decode($word){
	$bin = '';
	for($i=0; $i<strlen($word); $i+=6){
		$char = $word[$i].$word[$i+1].$word[$i+2].$word[$i+3].$word[$i+4].$word[$i+5];
		if($char == '000000'){
			$bin .= 'A';
		}
		if($char == '000001'){
			$bin .= 'B';
		}
		if($char == '000010'){
			$bin .= 'C';
		}
		if($char == '000011'){
			$bin .= 'D';
		}
		if($char == '000100'){
			$bin .= 'E';
		}
		if($char == '000101'){
			$bin .= 'F';
		}
		if($char == '000110'){
			$bin .= 'G';
		}
		if($char == '000111'){
			$bin .= 'H';
		}
		if($char == '001000'){
			$bin .= 'I';
		}
		if($char == '001001'){
			$bin .= 'J';
		}
		if($char == '001010'){
			$bin .= 'K';
		}
		if($char == '001011'){
			$bin .= 'L';
		}
		if($char == '001100'){
			$bin .= 'M';
		}
		if($char == '001101'){
			$bin .= 'N';
		}
		if($char == '001110'){
			$bin .= 'O';
		}
		if($char == '001111'){
			$bin .= 'P';
		}
		if($char == '010000'){
			$bin .= 'Q';
		}
		if($char == '010001'){
			$bin .= 'R';
		}
		if($char == '010010'){
			$bin .= 'S';
		}
		if($char == '010011'){
			$bin .= 'T';
		}
		if($char == '010100'){
			$bin .= 'U';
		}
		if($char == '010101'){
			$bin .= 'V';
		}
		if($char == '010110'){
			$bin .= 'W';
		}
		if($char == '010111'){
			$bin .= 'X';
		}
		if($char == '011000'){
			$bin .= 'Y';
		}
		if($char == '011001'){
			$bin .= 'Z';
		}
		if($char == '011010'){
			$bin .= 'a';
		}
		if($char == '011011'){
			$bin .= 'b';
		}
		if($char == '011100'){
			$bin .= 'c';
		}
		if($char == '011101'){
			$bin .= 'd';
		}
		if($char == '011110'){
			$bin .= 'e';
		}
		if($char == '011111'){
			$bin .= 'f';
		}
		if($char == '100000'){
			$bin .= 'g';
		}
		if($char == '100001'){
			$bin .= 'h';
		}
		if($char == '100010'){
			$bin .= 'i';
		}
		if($char == '100011'){
			$bin .= 'j';
		}
		if($char == '100100'){
			$bin .= 'k';
		}
		if($char == '100101'){
			$bin .= 'l';
		}
		if($char == '100110'){
			$bin .= 'm';
		}
		if($char == '100111'){
			$bin .= 'n';
		}
		if($char == '101000'){
			$bin .= 'o';
		}
		if($char == '101001'){
			$bin .= 'p';
		}
		if($char == '101010'){
			$bin .= 'q';
		}
		if($char == '101011'){
			$bin .= 'r';
		}
		if($char == '101100'){
			$bin .= 's';
		}
		if($char == '101101'){
			$bin .= 't';
		}
		if($char == '101110'){
			$bin .= 'u';
		}
		if($char == '101111'){
			$bin .= 'v';
		}
		if($char == '110000'){
			$bin .= 'w';
		}
		if($char == '110001'){
			$bin .= 'x';
		}
		if($char == '110010'){
			$bin .= 'y';
		}
		if($char == '110011'){
			$bin .= 'z';
		}
		if($char == '110100'){
			$bin .= '0';
		}
		if($char == '110101'){
			$bin .= '1';
		}
		if($char == '110110'){
			$bin .= '2';
		}
		if($char == '110111'){
			$bin .= '3';
		}
		if($char == '111000'){
			$bin .= '4';
		}
		if($char == '111001'){
			$bin .= '5';
		}
		if($char == '111010'){
			$bin .= '6';
		}
		if($char == '111011'){
			$bin .= '7';
		}
		if($char == '111100'){
			$bin .= '8';
		}
		if($char == '111101'){
			$bin .= '9';
		}
		if($char == '111110'){
			$bin .= '+';
		}
		if($char == '111111'){
			$bin .= '/';
		}
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

function RandomString($max)
{
    $characters = '01';
    $randstring = '';
    for ($i = 0; $i < $max; $i++) {
        $randstring .= $characters[rand(0, strlen($characters)-1)];
    }
    return $randstring;
}



$file = base64_encode(file_get_contents('down1.jpg'));
$cur_file = $file;
echo $file;
echo '<br>';
$bin = encode($file);
echo $bin;
echo '<br>';
$max = strlen($bin);
$key = RandomString($max);
echo $key;
echo '<br>';
$code = shifr($bin, $key);
echo $code;
echo '<br>';
$decode = shifr($code, $key);
echo $decode;
echo '<br>';
$text = decode($decode);
echo $cur_file;
echo '<br>';
echo $text;



?>