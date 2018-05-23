<?php
	require "/opendb.php";
	// Elegxos an exei dwthei timh sta antistoixa pedia ths formas 
if(isset($_POST['region_name']) && ($_POST['region_desc']) && ($_POST['nw-lat']) && ($_POST['nw-lng']) && ($_POST['se-lat']) && ($_POST['se-lng'])){
    $RegionName = $_POST['region_name'];
    $Description = $_POST['region_desc'];
	$NorhtWestLat = $_POST['nw-lat'];
	$NorhtWestLong = $_POST['nw-lng'];
	$SouthEastLat = $_POST['se-lat'];
	$SouthEastLong = $_POST['se-lng'];
	// Eisagwgh twn timwn autwn ston pinaka sub_node LocalHost
    $sql = "INSERT INTO ktimata (RegionName,Description,NorhtWestLat,NorhtWestLong,SouthEastLat,SouthEastLong) VALUES ('$RegionName','$Description','$NorhtWestLat','$NorhtWestLong','$SouthEastLat','$SouthEastLong')";
	if ($conn->query($sql) === TRUE) {
	?>
		<script>
			window.alert("Η Εισαγωγή ολοκληρώθηκε επιτυχώς!");
			window.location.href = '../index.html';
		</script>
		<?php
	}else {
		?>
		<script>
			window.alert("Έχει εκχωρηθεί αυτό το κτήμα");
			window.location.href = '../map.html';
		</script>
		<?php
	} 
	
}else { ?>
		<script>
				window.alert("Λάθος καταχώρηση!");
				window.location.href = '../map.html';
		</script>
	<?php
	}


?>