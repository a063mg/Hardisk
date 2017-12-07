<?php 
 $email = $_POST['Email']; 
 $login = $_POST['Login']; 
 $password = $_POST['Password'];
$file = file_get_contents('Pass/pass.json');
$json = json_decode($file, TRUE);
if ($json == "")
{
    unset($file);       
    $json[] = array('Login'=>$login, 'Password'=>$password, 'Email'=>$email);
    file_put_contents('Pass/pass.json',json_encode($json));
    unset($json);
    echo '<meta http-equiv="refresh" content="0;URL=http://alekseev700.esy.es/Site/enter.php">'; 
}
else
{
    foreach($json as $item)
    {
        if ($item['Login'] == $login){
    	   echo '<meta http-equiv="refresh" content="0;URL=http://alekseev700.esy.es/Site/regist.php?error">';
        }
    elseif ($item['Email'] == $email){
        	echo '<meta http-equiv="refresh" content="0;URL=http://alekseev700.esy.es/Site/regist.php?error">';
        }
        else{
        	unset($file);       
	   	   $json[] = array('Login'=>$login, 'Password'=>$password, 'Email'=>$email);
		  file_put_contents('Pass/pass.json',json_encode($json));
		  unset($json);
		  echo '<meta http-equiv="refresh" content="0;URL=http://alekseev700.esy.es/Site/enter.php">';
        }
    }
}
?> 