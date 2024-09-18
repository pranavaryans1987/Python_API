<?php
	$con = mysqli_connect("localhost","u998488001_bcapythondemo","BcaPython@5","u998488001_bcapythondemo");
	$action = $_POST['action'];
	if($action == "Search")
	{
		$id = $_POST['id'];
		$sql = "select * from `user_info` where id='$id'";
		$res = mysqli_query($con,$sql);
		if(mysqli_num_rows($res) >= 1)
		{
			$ar1 = array();
			$ar2 = array();
			$row = mysqli_fetch_assoc($res);
			array_push($ar1,$row['name']);
			array_push($ar2,$row['result']);
			echo json_encode(["data"=>$ar1,"data1"=>$ar2]);
		}
		else
		{
			echo json_encode(["data"=>"0"]);
		}
	}
	else if($action == "Insert")
	{
		$name = $_POST['name'];
		$result = $_POST['result'];
		$sql = "insert into `user_info` (`name`,`result`) values ('$name','$result')";
		$res = mysqli_query($con,$sql);
		$affected = mysqli_affected_rows($con);
		if($affected == 1)
		{
			echo json_encode(["data"=>"1"]);
		}
		else
		{
			echo json_encode(["data"=>"0"]);
		}
	}
	else if($action == "Update")
	{
		$id = $_POST['id'];
		$name = $_POST['name'];
		$result = $_POST['result'];
		$sql = "update `user_info` set `name`='$name',`result`='$result' where `id`='$id'";
		$res = mysqli_query($con,$sql);
		$affected = mysqli_affected_rows($con);
		if($affected == 1)
		{
			echo json_encode(["data"=>"1"]);
		}
		else
		{
			echo json_encode(["data"=>"0"]);
		}
	}
	else if($action == "Delete")
	{
		$id = $_POST['id'];
		$sql = "delete from `user_info` where `id`='$id'";
		$res = mysqli_query($con,$sql);
		$affected = mysqli_affected_rows($con);
		if($affected == 1)
		{
			echo json_encode(["data"=>"1"]);
		}
		else
		{
			echo json_encode(["data"=>"0"]);
		}
	}
?>