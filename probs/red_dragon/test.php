<?php
    echo is_numeric("\n\t  123") ? 'yes' : 'no';
    echo '<br>';
    echo is_numeric($_GET[no]) ? 'yes' : 'no';
    echo '<br>';
    echo is_numeric("0x12") ? 'yes' : 'no';
?>