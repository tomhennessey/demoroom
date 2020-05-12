<!doctype html>
<html>
<head>
<meta charset="utf-8">
<title>Demo Request Form</title>
<link href="style.css" rel="stylesheet" type="text/css">
<script type="text/javascript" src="site.js"></script>
</head>
	
<?php 
	error_reporting(E_ALL);
	ini_set('display_errors', '1');
	$con = mysqli_connect("localhost:3306", "chemdemoroom_admin", "EB%&W~&R#cGJ");
	// localhost is location of server, root = username, third is password 
	mysqli_select_db($con, "chemdemoroom_demos");
	if(!$con) {
		die('Could not connect: ' . mysqli_error());
	}
?>
	
<body>
<header id="header">
  <h1>Chemistry Demo Room</h1>
	
  <nav id="nav-bar">
	<a class="nav-link" href="./index.html">Home</a>
	<a class="nav-link" href="#top">Request a Demo</a>
	<a class="nav-link" href="https://chemistry.illinois.edu/holiday-magic" target="_blank">Holiday Demo Show</a>
	<a class="nav-link" href="./about_us.html">About Us</a>
	<a class ="nav-link" href="./contact_us.html">Contact Us</a>
  </nav>
	</header>
	
<main class="main" id="index_main">
	
<?php 
	$query = $_GET['query'];
	$query = htmlspecialchars($query);
	$query = mysqli_real_escape_string($con, $query);
	$raw_results = mysqli_query($con, "SELECT * FROM DEMOS WHERE (`name` LIKE '%".$query."%') OR (`text` LIKE '%".$query."%') OR (`proper_name` LIKE '%".$query."%') ", MYSQLI_STORE_RESULT);
	
	//echo "<main class=\"main\" id=\"index_main\">";
	echo "<div class=\"row\" id=\"demo_list\">";
	echo "<button type=\"button\" class=\"collapsible column\">Results</button>";
	echo "<div class=\"content-result\">";
	
	if(mysqli_num_rows($raw_results) > 0) {
		//display results
		while ($results = mysqli_fetch_array($raw_results, MYSQLI_ASSOC)) {
			echo "<div class=\"demo\">".$results['PROPER_NAME']." - <a href=\"./demos/".$results['NAME'].".pdf\" target =\"_blank\">View Demo Sheet</a> - <a href=\"./request_page.html?demo-name0=".$results['PROPER_NAME']."\">Request This Demo</a></div>";
			//<a href="./request_page.html?demo-name0=Colorful_Indicators">Request This Demo</a>
		}
	}
	else {
		echo "<div class=\"demo\">No results</div>";
	}
	echo "</div></div>";
?>
	
</main>

</body>
</html>