#! /bin/bash
set -e

make clean
make html
rsync -av _build/html/* blog2:/var/cc/static/
rsync -av exercises/* blog2:/var/cc/static/exercises/
