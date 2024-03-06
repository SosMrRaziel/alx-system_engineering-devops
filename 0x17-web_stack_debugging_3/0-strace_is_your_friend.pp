# Task 0: Fix error on why Apache is returning a 500 error after using strace
exec { 'command':
  command  => 'sed -i \'s/phpp/php/g\' /var/www/html/wp-settings.php',
  provider => 'shell',
}
