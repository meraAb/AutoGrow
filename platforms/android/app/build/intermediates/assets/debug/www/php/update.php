<?php
 include "Opendb.php";
 if(isset($_POST['update']))
 {
 $id=$_POST['id'];
 $name=$_POST['name'];
 $number=$_POST['number'];
 $q=mysqli_query($con,"UPDATE `test` SET `name`='$name',`number`='$number' where `id`='$id'");
 if($q)
 echo "success";
 else
 echo "error";
 }
 ?>