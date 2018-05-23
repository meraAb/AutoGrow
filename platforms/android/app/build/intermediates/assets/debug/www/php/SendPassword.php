<html>
<head>
    <meta http-equiv="Content-Type" content="text/html;charset=utf-8" >
</head>
<body>
    <?php
	require "/opendb.php";
        // Check if email and password exist
        if(isset($_POST['sendPass'])){
            $email = $_POST['sendPass'];

			$sql = "SELECT Password FROM users WHERE Email='$email'";
			$result = $conn->query($sql);
			if ($result->num_rows > 0) {
				// output data of each row
				while($row = $result->fetch_assoc()) {
					// Try to send email but first you have to install SMTP SERVER
					$msg = $row['Password'];
					$msg = wordwrap($msg,70);
					mail("$email","My subject",$msg);
				}
					?>
	
				<script>
					window.alert("Your password sended to your email");
					window.location.href = '../login.html';
				</script>
			<?php
			} else { ?>
				<script>
					window.alert("Your e-mail doesnt exists");
					window.location.href = '../login.html';
				</script>
			<?php
			}
					$conn->close();
}
					?>
</body>
</html>