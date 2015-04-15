#! /bin/bash
set -e

make clean
make html
rsync -av _build/html/* blog.vrplumber.com:/var/cc/www/
rsync -av exercises/* blog.vrplumber.com:/var/cc/www/exercises/
