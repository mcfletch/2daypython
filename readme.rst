Notes for Instructors
===============================

To regenerate the session site and downloads:

.. code-block:: bash

    aptitude install python-sphinx
    ./fakedata.py 
    # TODO: this wasn't really supposed to get checked in...
    bzr revert sample_data.csv 
    make html # to just build the HTML site
    make download # to build the HTML site and create a download

To serve it on the day of the lesson:

.. code-block:: bash

    $ aptitude install nginx

Then use this nginx config-file::

    server {
            #listen   80; ## listen for ipv4; this line is default and implied
            #listen   [::]:80 default ipv6only=on; ## listen for ipv6

            #root /usr/share/nginx/www;
            root /usr/share/nginx/carpentry;
            index index.html index.htm;

            # Make site accessible from http://localhost/
            server_name localhost sturm.local;

            location / {
                    # First attempt to serve request as file, then
                    # as directory, then fall back to index.html
                    try_files $uri $uri/ /index.html;
            }

    }

And link ``/usr/share/nginx/carpentry`` to your _build/html directory:

.. code-block:: bash 

    $ sudo ln -s /home/mcfletch/carpentry-dev/_build/html /usr/share/nginx/carpentry
