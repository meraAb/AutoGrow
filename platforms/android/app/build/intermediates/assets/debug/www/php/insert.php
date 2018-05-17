<?php
header("Access-Control-Allow-Origin: *");
header("Access-Control-Allow-Methods: *");
$conn = mysqli_connect("localhost", "root", "", "autogrow1");
    

    if (!$conn) {
        die("Connection failed: " . mysqli_connect_error());
    }
       
    mysqli_set_charset($conn,"utf8");
	 
   if(isset($_POST['insert'])){
$name = isset($_POST['name']) ? $_POST['name'] : 'qq';
$number = isset($_POST['number']) ? $_POST['number'] : '11';
	
	 $q=mysqli_query($conn,"INSERT INTO `test` (`name`,`number`) VALUES ('$name','$number')");

if($q)
  echo "success";
 else
  echo "error";
 }
	
	
	



?>