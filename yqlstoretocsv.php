<?php
header("Access-Control-Allow-Origin: *");
$version = "0.0.1";

// store
if (isset($_GET["s"])){
	$store = $_GET["s"];
} else {
	$store = "";
}

$yql = "https://query.yahooapis.com/v1/public/yql?format=json&callback=&q=select%20*%20from%20yql.storage%20where%20name%3D%22store%3A%2F%2F";

if (strlen($store)>0){
	$c = json_decode(file_get_contents($yql . $store . "%22"),true);
	//echo var_dump($c);
	//echo "<br/><br/>";
	echo $c[query][results][result][value];
	//echo "<br/>ok";
}

?>
