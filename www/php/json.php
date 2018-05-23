<?php
include "Opendb.php";
$data=array();
$q=mysqli_query($con,"select * from `test`");
while ($row=mysqli_fetch_object($q)){
 $data[]=$row;
}
echo json_encode($data);
?>