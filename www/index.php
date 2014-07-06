<?php
require '../vendor/autoload.php';

require '../config.php';
$app = new \Slim\Slim(array(
    'custom' => $config
));
$app->get('/test', function() use ($app) {  $custom = $app->config('custom'); echo $custom['greeting']; });
$app->run();

?>