<?php
    include_once("db.php");

    $Key = 0;
    $pas = 0;

    $email = $_POST['Email'];
    $login = $_POST['Login'];
    $password = $_POST['Password'];
    $repeat = $_POST['Password_repeat'];
    if ($repeat != $password){
        $pas = 1;
        header('Location: login.php?password_not_confirm');
    }
    if (empty($login)){
        $pas = 1;
        header('Location: login.php?login_empty');
    }
    if (empty($email)){
        $pas = 1;
        header('Location: login.php?email_empty');
    }
    if (empty($password) && empty($repeat)){
        $pas = 1;
        header('Location: login.php?password_empty');
    }

    while($data = mysqli_fetch_array($qr_result)){
        if ($data['Id'] > $Key){
        $Key = $data['Id'];
        }
        if ($data['Login'] == $login){
            $pas = 1;
            header('Location: login.php?login_exist');
        }
        elseif ($data['Email'] == $email){
            $pas = 1;
            header('Location: login.php?email_exist');
        }
    }
    if ($pas == 0){
        $Id = $Key+1;
        $Login = $login;
        $Password = $password;
        $Email = $email;
        $insert_sql = "INSERT INTO Login (Id, Login, Password, Email)" .
        "VALUES('{$Id}', '{$Login}', '{$Password}', '{$Email}')";
        $sql = mysqli_query($connect_to_db, $insert_sql);
        if ($sql) {
        } else {
            echo header('Location: login.php?error');
        }
        mysqli_close($connect_to_db);
        echo header('Location: index.php');
    }
?>
