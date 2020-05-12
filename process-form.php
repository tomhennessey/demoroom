<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<title>Process Form</title>
<link href="style.css" rel="stylesheet" type="text/css">
</head>
<?php
	if(isset($_POST['name'])) {
	
		// define variables from _POST[]
		$name = $_POST['name'];
		$email_from = $_POST['email'];
		$demo_array = [];
		
		// check if multiple demoes requested and add them all
		array_push($demo_array, $_POST['demo-name0']);
		if(isset($_POST['demo-name1'])) {
			for ($i = 1; isset($_POST['demo-name' . $i]); $i++) {
				array_push($demo_array, $_POST['demo-name' . $i]);
			}		
		}

		
		$date_time = $_POST['dateTime'];
		$comments = $_POST['info'];
		
		$demo_string = "";
		for ($i = 0; $i < count($demo_array); $i++) {
			if (count($demo_array) == 1) {
				$demo_string .= $demo_array[$i];
			}
			else if ($i + 1 == count($demo_array)) {
				$demo_string .= "and " . $demo_array[$i]; 
			}
			else {
				$demo_string .= $demo_array[$i] . ", ";
			}
		}
		
		// format date and time string
		$dateTimeNew = DateTime::createFromFormat('Y-m-d\TG\:i', $date_time);
		$dateTimeNew = $dateTimeNew->format('l F dS \a\t\ g\:ia \(m-d-Y \- H:i\)');
		
		// compose message that will be sent to demo room email
		$email_message = "$name ($email_from) has requested the following demo(s):\n" . $demo_string . "\n" . $dateTimeNew . "\n" . $comments;
		
		// email and subject to send
		$email_to = "thennes2@illinois.edu";
		$email_subject = "Demo Request from Website";
		
		// create email headers and send
		$headers = 'From: chem-demoroom@illinois.edu' . "\r\n" .
		'Reply-To: chem-demoroom@illinois.edu' . "\r\n" .
		'X-Mailer: PHP/' . phpversion();
		if (mail($email_to, $email_subject, $email_message, $headers)) {
		}
		else {
			echo "There was an error processing your request. Please send an email to chem-demoroom@illinois.edu with your demo request.";
		}
		
		// confirmation email for requester
		$email_confirmation_subject = "Demo Request Confirmation";
		$email_confirmation = "This email is to confirm you request of $demo_string on $dateTimeNew. If any of this information is incorrect, please reply to this email with the corrected information. Thank you!";
		if(mail($email_from, $email_confirmation_subject, $email_confirmation, $headers)) {
		}
		else {
			echo "There was an error processing your request. Please send an email to chem-demoroom@illinois.edu with your demo request."; 
		}
	}
  ?>
<body>
		<h1> Thank You</h1>
        <p> You should receive an email confirming your demonstration request shortly. If you do not, please email chemdemoroom@illinois.edu to request your demo.</p>

</body>
</html>