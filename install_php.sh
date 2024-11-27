

!apt-get update && apt-get install -y php php-curl php-xml unzip

!php -r "copy('https://getcomposer.org/installer', 'composer-setup.php');"
!php composer-setup.php
!php -r "unlink('composer-setup.php');"
!mv composer.phar /usr/local/bin/composer

!echo '{"require": {"fabpot/goutte": "^4.0"}}' > composer.json
!composer install

