<?php
require "opendb.php";
if(isset($_GET['RegionName']) && ($_GET['Sub_Name']) && ($_GET['position'])){
	$RegionName = $_GET['RegionName'];
	$Sub_Name = $_GET['Sub_Name'];
	$position = $_GET['position'];

	// Insert data to table marker
    $sql = "DELETE FROM markers WHERE RegionName='$RegionName' AND Sub_Name = '$Sub_Name' AND markerPosition = '$position'";
	if ($conn->query($sql) === TRUE) {
		?>
			<script>
				window.alert("Successfully deleted!");
				window.location.href = '../Farm.html?name='+"<?php echo $RegionName?>";
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
