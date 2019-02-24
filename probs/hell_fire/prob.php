<?php
  include "./config.php";
  login_chk();
  dbconnect();
  
  if(preg_match('/prob|_|\.|proc|union/i', $_GET[order])) exit("No Hack ~_~");
  
  $query = "select id,email,score from prob_hell_fire where 1 order by {$_GET[order]}";
  echo "<table border=1><tr><th>id</th><th>email</th><th>score</th>";
  $rows = mysql_query($query);
  
  while(($result = mysql_fetch_array($rows))){
    if($result['id'] == "admin") $result['email'] = "**************";
    echo "<tr><td>{$result[id]}</td><td>{$result[email]}</td><td>{$result[score]}</td></tr>";
  }
  echo "</table><hr>query : <strong>{$query}</strong><hr>";

  $_GET[email] = addslashes($_GET[email]);
  $query = "select email from prob_hell_fire where id='admin' and email='{$_GET[email]}'";
  $result = @mysql_fetch_array(mysql_query($query));
  
  if(($result['email']) && ($result['email'] === $_GET['email'])) solve("hell_fire");
  highlight_file(__FILE__);
?>