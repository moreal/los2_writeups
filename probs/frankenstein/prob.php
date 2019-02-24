<?php
  include "./config.php";
  login_chk();
  dbconnect();
  if(preg_match('/prob|_|\.|\(|\)|union/i', $_GET[pw])) exit("No Hack ~_~");
  $query = "select id,pw from prob_frankenstein where id='frankenstein' and pw='{$_GET[pw]}'";
  echo "<hr>query : <strong>{$query}</strong><hr><br>";
  $result = @mysql_fetch_array(mysql_query($query));
  if(mysql_error()) exit("error");

  $_GET[pw] = addslashes($_GET[pw]);
  $query = "select pw from prob_frankenstein where id='admin' and pw='{$_GET[pw]}'";
  $result = @mysql_fetch_array(mysql_query($query));
  if(($result['pw']) && ($result['pw'] == $_GET['pw'])) solve("frankenstein");
  highlight_file(__FILE__);
?>