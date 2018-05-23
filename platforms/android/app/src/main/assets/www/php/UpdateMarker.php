<?php
require "opendb.php";
if(isset($_GET['RegionName']) && ($_GET['Sub_Name']) && ($_GET['position'])){
	$RegionName = $_GET['RegionName'];
	$Sub_Name = $_GET['Sub_Name'];
	$marker_position = trim($_GET['position'], '()');
	$position = explode(',', $marker_position);
	//$markerLatitude = $_GET['lat'];
	//$markerLongtitude = $_GET['long'];
	// Insert data to table marker
    $sql = "UPDATE markers SET Sub_Name='$Sub_Name' WHERE markerLatitude='$position[0]'";
	if ($conn->query($sql) === TRUE) {
		?>
			<script>
				window.alert("Updated successfully");
				window.location.href = '../farm.html?name='+"<?php echo $RegionName?>";
			</script>
			<?php
		} else {
			?>
			<script>
				window.alert("Updated unsuccessfully");
				window.location.href = '../farm.html?name='+"<?php echo $RegionName?>";
			</script>
			<?php
	}
}
