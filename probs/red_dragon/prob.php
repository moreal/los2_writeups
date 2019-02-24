<?php
  include "./config.php";
  login_chk();
  dbconnect();
  if(preg_match('/prob|_|\./i', $_GET['id'])) exit("No Hack ~_~");
  if(strlen($_GET['id']) > 7) exit("too long string");
  $no = is_numeric($_GET['no']) ? $_GET['no'] : 1;
  $query = "select id from prob_red_dragon where id='{$_GET[id]}' and no={$no}";
  echo "<hr>query : <strong>{$query}</strong><hr><br>";
  $result = @mysql_fetch_array(mysql_query($query));
  if($result['id']) echo "<h2>Hello {$result['id']}</h2>";

  $_GET[pw] = addslashes($_GET[pw]);
  $query = "select pw from prob_red_dragon where id='admin' and pw='{$_GET[pw]}'";
  $result = @mysql_fetch_array(mysql_query($query));
  if(($result['pw']) && ($result['pw'] === $_GET['pw'])) solve("red_dragon");
  highlight_file(__FILE__);
?>