<?php
require "/opendb.php";

if(isset($_POST['SubNode'])){
    $Sub_Name = $_POST['SubNode'];
	// Insert data to table sub_node
    $sql = "DELETE FROM sub_node WHERE Sub_Name='$Sub_Name'";
	if ($conn->query($sql) === TRUE) {
	?>
		<script>
			window.alert("Successfully deleted!");
			window.location.href = 'php/DeleteNode.php';
		</script>
		<?php
	} else {
		?>
		<script>
			window.alert("Try again");
			window.location.href = 'php/DeleteNode.php';
		</script>
		<?php
	}

    $conn->query($sql);
    $conn->close();

}
	
?>