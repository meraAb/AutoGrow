<?php
require "opendb.php";
if(isset($_GET['RegionName'])){
	$RegionName = $_GET['RegionName'];
	// Insert data to table marker
    $sql = "DELETE FROM farms WHERE RegionName='$RegionName'";
	if ($conn->query($sql) === TRUE) {
		?>
			<script>
				window.alert("The Farm successfully deleted ");
				window.location.href = '../index.html';
			</script>
			<?php
		} else {
			?>
			<script>
				window.alert("Try again");
				window.location.href = '../Farm.html?name='+"<?php echo $RegionName?>";
			</script>
			<?php
	}
}
