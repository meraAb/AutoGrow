<?php
require "/opendb.php";
require "/opendbserver.php";
// Elegxos an exei dwthei timh sta antistoixa pedia ths formas 
if(isset($_POST['Sub_Name']) && ($_POST['Protocol'])){
    $Sub_Name = $_POST['Sub_Name'];
    $Protocol = $_POST['Protocol'];
	$PortA = $_POST['PortA'];
	$PortB = $_POST['PortB'];
	$PortC = $_POST['PortC'];
	$PortD = $_POST['PortD'];
	$PortE = $_POST['PortE'];
	$id_sub = 'node3';
	// Insert data to tables sub_node
    $sql = "INSERT INTO sub_node (Sub_Name, Sub_Id, Protocol) VALUES ('$Sub_Name','$id_sub','$Protocol')";
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
			window.alert("The SubNode exists");
			window.location.href = '../index.html';
		</script>
		<?php
	}
	
	// Insert data to table sub_node 
	$sql = "INSERT INTO sub_node (Sub_Name, Sub_Id, Protocol) VALUES ('$Sub_Name','$id_sub','$Protocol')";
	if ($connserver->query($sql) === TRUE) {
	?>
		<script>
			window.alert("Successfully inserted");
			window.location.href = '../index.html';
		</script>
		<?php
	} else {
		?>
		<script>
			window.alert("The SubNode exists");
			window.location.href = '../index.html';
		</script>
		<?php
	}
	
	
	//PORT A
	//Select id from table sensor depends of name
	$sql = "SELECT Sensor_Id FROM sensors WHERE Name = '$PortA'";
	$result = $conn->query($sql);
	if ($result->num_rows > 0) {
    // output data of each row
		while($row = $result->fetch_assoc()) {
			$sen_id = $row['Sensor_Id'];
		}
	} else {
		echo "0 results";
	}

	// Insert data to table subwithsensors
    $sql = "INSERT INTO subwithsensors (Sub_Id,Sensor_Id,Port) VALUES ('$id_sub','$sen_id','A')";
	if ($conn->query($sql) === TRUE) {
	?>
		<script>
			window.alert("Successfully inserted");
			window.location.href = '../index.html';
		</script>
		<?php
	} else {
		?>
		<script>
			window.alert("The SubNode exists");
			window.location.href = '../index.html';
		</script>
		
	<?php	}
	//PORT B
	//Select id from table sensor depends of name
	$sql = "SELECT Sensor_Id FROM sensors WHERE Name = '$PortB'";
	$result = $conn->query($sql);
	if ($result->num_rows > 0) {
    // output data of each row
		while($row = $result->fetch_assoc()) {
			$sen_id = $row['Sensor_Id'];
		}
	} else {
		echo "0 results";
	}

	// Insert data to table subwithsensors
    $sql = "INSERT INTO subwithsensors (Sub_Id,Sensor_Id,Port) VALUES ('$id_sub','$sen_id','B')";
	if ($conn->query($sql) === TRUE) {
	?>
		<script>
			window.alert("Successfully inserted");
			window.location.href = '../index.html';
		</script>
		<?php
	} else {
		?>
		<script>
			window.alert("The SubNode exists");
			window.location.href = '../index.html';
		</script>
	<?php
	}
	//PORT C
	//Select id from table sensor depends of name
	$sql = "SELECT Sensor_Id FROM sensors WHERE Name = '$PortC'";
	$result = $conn->query($sql);
	if ($result->num_rows > 0) {
    // output data of each row
		while($row = $result->fetch_assoc()) {
			$sen_id = $row['Sensor_Id'];
		}
	} else {
		echo "0 results";
	}

	// Insert data to table subwithsensors
    $sql = "INSERT INTO subwithsensors (Sub_Id,Sensor_Id,Port) VALUES ('$id_sub','$sen_id','C')";
	if ($conn->query($sql) === TRUE) {
	?>
		<script>
			window.alert("Successfully inserted");
			window.location.href = '../index.html';
		</script>
		<?php
	} else {
		?>
		<script>
			window.alert("The SubNode exists");
			window.location.href = '../index.html';
		</script>
	<?php
	}
	
	//PORT D
	//Select id from table sensor depends of name
	$sql = "SELECT Sensor_Id FROM sensors WHERE Name = '$PortD'";
	$result = $conn->query($sql);
	if ($result->num_rows > 0) {
    // output data of each row
		while($row = $result->fetch_assoc()) {
			$sen_id = $row['Sensor_Id'];
		}
	} else {
		echo "0 results";
	}

	// Insert data to table subwithsensors
    $sql = "INSERT INTO subwithsensors (Sub_Id,Sensor_Id,Port) VALUES ('$id_sub','$sen_id','D')";
	if ($conn->query($sql) === TRUE) {
	?>
		<script>
			window.alert("Successfully inserted");
			window.location.href = '../index.html';
		</script>
		<?php
	} else {
		?>
		<script>
			window.alert("The SubNode exists");
			window.location.href = '../index.html';
		</script>
	<?php 
	}
	
	//PORT E
	//Select id from table sensor depends of name
	$sql = "SELECT Sensor_Id FROM sensors WHERE Name = '$PortE'";
	$result = $conn->query($sql);
	if ($result->num_rows > 0) {
    // output data of each row
		while($row = $result->fetch_assoc()) {
			$sen_id = $row['Sensor_Id'];
		}
	} else {
		echo "0 results";
	}

	// Insert data to table subwithsensors
    $sql = "INSERT INTO subwithsensors (Sub_Id,Sensor_Id,Port) VALUES ('$id_sub','$sen_id','E')";
	if ($conn->query($sql) === TRUE) {
	?>
		<script>
			window.alert("Successfully inserted");
			window.location.href = '../index.html';
		</script>
		<?php
	} else {
		?>
		<script>
			window.alert("The SubNode exists");
			window.location.href = '../index.html';
		</script>
	<?php 
	}
    $conn->query($sql);
    $conn->close();

}
	
?>