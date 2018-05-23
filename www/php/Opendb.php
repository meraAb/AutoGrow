<?php
header("Access-Control-Allow-Origin: *");
header("Access-Control-Allow-Methods: *");
$conn = mysqli_connect("localhost", "root", "", "autogrow1");
    

    if (!$conn) {
        die("Connection failed: " . mysqli_connect_error());
    }
       
    mysqli_set_charset($conn,"utf8");
	 
?>