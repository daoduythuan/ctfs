<?php

$URL = $_SERVER['REQUEST_URI'];
$matches = array();
preg_match('/^([a-z\/.]+)$/', $URL, $matches); 
if(strpos($URL, './') !== FALSE){
    exit('./');
}
else if(strpos($URL, '\\') !== FALSE){
    exit('\\');
}
else if(empty($matches) || $matches[1] != $URL){
    exit('empty($matches) || $matches[1] != $URL');
} 
else if(strpos($URL, '//') !== FALSE){
    exit('//');
} 
else if(substr($URL, -10) !== '/index.php'){
    exit('substr($URL, -10) !== \'/index.php\'');
} 
else if(strpos($URL, 'p.') !== FALSE){
    exit('p.');
} 
else if($URL == '/admin/index.php'){
    exit('$URL == \'/admin/index.php\'');
}
else {
    if($URL !== '/admin/index.php'){
  session_start();
        $_SESSION['power'] = 1;
  echo "Ok,ok...<br>";
        exit("<center style=\"font-size:36px;\"><a href=\"../../../another/index.php?source\">Click here</a></center>");
    }
}
?>