<?php
require "opendb.php";
if(isset($_GET['RegionName']) && ($_GET['Sub_Name']) && ($_GET['position'])){
	$RegionName = $_GET['RegionName'];
	$Sub_Name = $_GET['Sub_Name'];
	$marker_position = trim($_GET['position'], '()');
	$position = explode(',', $marker_position);
	// Insert data to table marker
    $sql = "INSERT INTO markers (RegionName,Sub_Name,markerLatitude,markerLongtitude) VALUES ('$RegionName','$Sub_Name','$position[0]','$position[1]')";
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
				window.alert("The SubNode exists");
				window.location.href = '../Farm.html?name='+"<?php echo $RegionName?>";
			</script>
			<?php
	}
}
