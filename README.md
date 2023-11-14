Show your appreciation to those who have contributed to the project.

## License

This is not an open source project and cloning of this code from anywhere
can put you into serious legal issues.

## CLONE AT YOUR OWN RISK!!!

## Project status

If you have run out of energy or time for your project, put a note at the top of the README saying that development has slowed down or stopped completely. Someone may choose to fork your project or volunteer to step in as a maintainer or owner, allowing your project to keep going. You can also make an explicit request for maintainers.

#### $$$ PROJECT CONFIGURATIONS

    > admin-login-url: {{protocol}}/{{domain}}/lionnic-admin-login/
    > username: None(set own)
    > email: None(set own)

### MINI ADMIN LOGIN

    - [] {{protocol}}/{{domain}}/lionnic-dashboard-admin/
            (credentials will be provied by the superadmin)

## FRONTEND ADMIN FOR WRITERS

    - [] {{protocol}}/{{domain}}/dashboard/
        AUTHENTICATED USERS ONLY AND ADMIN

=======
Show your appreciation to those who have contributed to the project.

## License

For open source projects, say how it is licensed.

## Project status

If you have run out of energy or time for your project, put a note at the top of the README saying that development has slowed down or stopped completely. Someone may choose to fork your project or volunteer to step in as a maintainer or owner, allowing your project to keep going. You can also make an explicit request for maintainers.

server{
listen 81;
server_name ip_address lionnic.com;
#return 301 https://lionnic.com;
#location = /favicon.ico { access_log off; log_not_found off; }
location /static/ {
root /home/kwasa/myprojectdir/blogmag;
}
    
    location / {
    proxy_pass http://ip_address:8100;
    }

}

