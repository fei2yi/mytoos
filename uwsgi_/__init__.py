*** Starting uWSGI 2.0.17.1 (64bit) on [Fri Nov 30 15:01:49 2018] ***
compiled with version: 4.4.7 20120313 (Red Hat 4.4.7-23) on 30 November 2018 04:50:16
os: Linux-2.6.32-696.6.3.el6.x86_64 #1 SMP Wed Jul 12 14:17:22 UTC 2017
nodename: iZ2zegdkenf5ki7xp8k3wkZ
machine: x86_64
clock source: unix
pcre jit disabled
detected number of CPU cores: 2
current working directory: /root/script
writing pidfile to /root/script/uwsgi.pid
detected binary path: /usr/local/bin/uwsgi
*** WARNING: you are running uWSGI as root !!! (use the --uid flag) ***
chdir() to /root/twodj/
your processes number limit is 15245
your memory page size is 4096 bytes
detected max file descriptor number: 65535
building mime-types dictionary from file /etc/mime.types...883 entry found
lock engine: pthread robust mutexes
thunder lock: enabled
uWSGI http bound on 0.0.0.0:8000 fd 3
uwsgi socket 0 bound to UNIX address /root/script/uwsgi.sock fd 6
*** WARNING: you are running uWSGI as root !!! (use the --uid flag) ***
Python version: 3.6.7 (default, Nov  9 2018, 10:03:30)  [GCC 4.4.7 20120313 (Red Hat 4.4.7-23)]
Python main interpreter initialized at 0x20d9a10
*** WARNING: you are running uWSGI as root !!! (use the --uid flag) ***
python threads support enabled
your server socket listen backlog is limited to 100 connections
your mercy for graceful operations on workers is 60 seconds
mapped 486672 bytes (475 KB) for 5 cores
*** Operational MODE: preforking ***
WSGI app 0 (mountpoint='') ready in 0 seconds on interpreter 0x20d9a10 pid: 23182 (default app)
*** WARNING: you are running uWSGI as root !!! (use the --uid flag) ***
*** uWSGI is running in multiple interpreter mode ***
spawned uWSGI master process (pid: 23182)
spawned uWSGI worker 1 (pid: 23184, cores: 1)
spawned uWSGI worker 2 (pid: 23185, cores: 1)
spawned uWSGI worker 3 (pid: 23186, cores: 1)
spawned uWSGI worker 4 (pid: 23187, cores: 1)
spawned uWSGI worker 5 (pid: 23188, cores: 1)
spawned uWSGI http 1 (pid: 23189)
[pid: 23184|app: 0|req: 1/1] 218.247.217.98 () {38 vars in 675 bytes} [Fri Nov 30 07:02:02 2018] GET /index => generated 7174 bytes in 19 msecs (HTTP/1.1 200) 3 headers in 110 bytes (1 switches on core 0)
[pid: 23185|app: 0|req: 1/2] 218.247.217.98 () {38 vars in 715 bytes} [Fri Nov 30 07:02:03 2018] GET /demo/welcome.html => generated 24253 bytes in 19 msecs (HTTP/1.1 200) 3 headers in 111 bytes (1 switches on core 0)
[pid: 23186|app: 0|req: 1/3] 218.247.217.98 () {36 vars in 598 bytes} [Fri Nov 30 07:02:03 2018] GET /js/index.js => generated 7174 bytes in 18 msecs (HTTP/1.1 200) 3 headers in 110 bytes (1 switches on core 0)
Not Found: /frame/static/js/vip_nav.js
[pid: 23188|app: 0|req: 1/4] 218.247.217.98 () {36 vars in 616 bytes} [Fri Nov 30 07:02:03 2018] GET /frame/static/js/vip_nav.js => generated 4584 bytes in 17 msecs (HTTP/1.1 404) 3 headers in 102 bytes (1 switches on core 0)
Not Found: /demo/vip_tab.js
[pid: 23187|app: 0|req: 1/5] 218.247.217.98 () {36 vars in 606 bytes} [Fri Nov 30 07:02:03 2018] GET /demo/vip_tab.js => generated 4551 bytes in 17 msecs (HTTP/1.1 404) 3 headers in 102 bytes (1 switches on core 0)
[pid: 23184|app: 0|req: 2/6] 218.247.217.98 () {38 vars in 673 bytes} [Fri Nov 30 07:02:42 2018] GET /index => generated 7174 bytes in 1 msecs (HTTP/1.1 200) 3 headers in 110 bytes (1 switches on core 0)
[pid: 23185|app: 0|req: 2/7] 218.247.217.98 () {38 vars in 713 bytes} [Fri Nov 30 07:02:42 2018] GET /demo/welcome.html => generated 24253 bytes in 1 msecs (HTTP/1.1 200) 3 headers in 111 bytes (1 switches on core 0)
[pid: 23186|app: 0|req: 2/8] 218.247.217.98 () {36 vars in 596 bytes} [Fri Nov 30 07:02:42 2018] GET /js/index.js => generated 7174 bytes in 1 msecs (HTTP/1.1 200) 3 headers in 110 bytes (1 switches on core 0)
Not Found: /frame/static/js/vip_nav.js
[pid: 23188|app: 0|req: 2/9] 218.247.217.98 () {36 vars in 615 bytes} [Fri Nov 30 07:02:42 2018] GET /frame/static/js/vip_nav.js => generated 4584 bytes in 4 msecs (HTTP/1.1 404) 3 headers in 102 bytes (1 switches on core 0)
Not Found: /demo/vip_tab.js
[pid: 23187|app: 0|req: 2/10] 218.247.217.98 () {36 vars in 605 bytes} [Fri Nov 30 07:02:43 2018] GET /demo/vip_tab.js => generated 4551 bytes in 4 msecs (HTTP/1.1 404) 3 headers in 102 bytes (1 switches on core 0)
[pid: 23184|app: 0|req: 3/11] 218.247.217.98 () {38 vars in 714 bytes} [Fri Nov 30 07:02:44 2018] GET /spider/basic.html => generated 12233 bytes in 2 msecs (HTTP/1.1 200) 3 headers in 111 bytes (1 switches on core 0)
[pid: 23185|app: 0|req: 3/12] 218.247.217.98 () {38 vars in 698 bytes} [Fri Nov 30 07:02:44 2018] GET /data/?page=1&limit=30 => generated 11497 bytes in 36 msecs (HTTP/1.1 200) 3 headers in 102 bytes (2 switches on core 0)
[pid: 23186|app: 0|req: 3/13] 218.247.217.98 () {38 vars in 724 bytes} [Fri Nov 30 07:02:45 2018] GET /spider/distribute.html => generated 3960 bytes in 2 msecs (HTTP/1.1 200) 3 headers in 110 bytes (1 switches on core 0)
[pid: 23188|app: 0|req: 3/14] 218.247.217.98 () {38 vars in 717 bytes} [Fri Nov 30 07:02:45 2018] GET /distribute_/?page=1&limit=20 => generated 6706 bytes in 36 msecs (HTTP/1.1 200) 3 headers in 101 bytes (2 switches on core 0)
[pid: 23187|app: 0|req: 3/15] 218.247.217.98 () {38 vars in 710 bytes} [Fri Nov 30 07:02:46 2018] GET /spider/pid.html => generated 3845 bytes in 8 msecs (HTTP/1.1 200) 3 headers in 110 bytes (1 switches on core 0)
[pid: 23184|app: 0|req: 4/16] 218.247.217.98 () {38 vars in 696 bytes} [Fri Nov 30 07:02:46 2018] GET /pid_/?page=1&limit=16 => generated 3261 bytes in 27 msecs (HTTP/1.1 200) 3 headers in 101 bytes (2 switches on core 0)
[pid: 23185|app: 0|req: 4/17] 218.247.217.98 () {38 vars in 714 bytes} [Fri Nov 30 07:02:46 2018] GET /spider/mysql.html => generated 3240 bytes in 1 msecs (HTTP/1.1 200) 3 headers in 110 bytes (1 switches on core 0)
[pid: 23186|app: 0|req: 4/18] 218.247.217.98 () {38 vars in 702 bytes} [Fri Nov 30 07:02:46 2018] GET /mysql_/?page=1&limit=16 => generated 7667 bytes in 40 msecs (HTTP/1.1 200) 3 headers in 101 bytes (2 switches on core 0)
[pid: 23188|app: 0|req: 4/19] 218.247.217.98 () {38 vars in 720 bytes} [Fri Nov 30 07:02:47 2018] GET /spider/rebbitmq.html => generated 3995 bytes in 8 msecs (HTTP/1.1 200) 3 headers in 110 bytes (1 switches on core 0)
[pid: 23187|app: 0|req: 4/20] 218.247.217.98 () {38 vars in 711 bytes} [Fri Nov 30 07:02:47 2018] GET /rebbitmq_/?page=1&limit=16 => generated 7351 bytes in 32 msecs (HTTP/1.1 200) 3 headers in 101 bytes (2 switches on core 0)
[pid: 23184|app: 0|req: 5/21] 218.247.217.98 () {38 vars in 716 bytes} [Fri Nov 30 07:02:47 2018] GET /spider/server.html => generated 3582 bytes in 1 msecs (HTTP/1.1 200) 3 headers in 110 bytes (1 switches on core 0)
[pid: 23185|app: 0|req: 5/22] 218.247.217.98 () {38 vars in 705 bytes} [Fri Nov 30 07:02:47 2018] GET /server_/?page=1&limit=16 => generated 1099 bytes in 18 msecs (HTTP/1.1 200) 3 headers in 101 bytes (2 switches on core 0)
Fri Nov 30 07:04:41 2018 - uWSGI worker 3 screams: UAAAAAAH my master disconnected: i will kill myself !!!
Fri Nov 30 07:04:41 2018 - uWSGI worker 5 screams: UAAAAAAH my master disconnected: i will kill myself !!!
Fri Nov 30 07:04:41 2018 - uWSGI worker 4 screams: UAAAAAAH my master disconnected: i will kill myself !!!
*** Starting uWSGI 2.0.17.1 (64bit) on [Fri Nov 30 15:06:17 2018] ***
compiled with version: 4.4.7 20120313 (Red Hat 4.4.7-23) on 30 November 2018 04:50:16
os: Linux-2.6.32-696.6.3.el6.x86_64 #1 SMP Wed Jul 12 14:17:22 UTC 2017
nodename: iZ2zegdkenf5ki7xp8k3wkZ
machine: x86_64
clock source: unix
pcre jit disabled
detected number of CPU cores: 2
current working directory: /root/script
writing pidfile to /root/script/uwsgi.pid
detected binary path: /usr/local/bin/uwsgi
*** WARNING: you are running uWSGI as root !!! (use the --uid flag) ***
chdir() to /root/twodj/
your processes number limit is 15245
your memory page size is 4096 bytes
detected max file descriptor number: 65535
building mime-types dictionary from file /etc/mime.types...883 entry found
lock engine: pthread robust mutexes
thunder lock: enabled
uWSGI http bound on 0.0.0.0:8000 fd 3
uwsgi socket 0 bound to UNIX address /root/script/uwsgi.sock fd 6
*** WARNING: you are running uWSGI as root !!! (use the --uid flag) ***
Python version: 3.6.7 (default, Nov  9 2018, 10:03:30)  [GCC 4.4.7 20120313 (Red Hat 4.4.7-23)]
Python main interpreter initialized at 0x22a4a10
*** WARNING: you are running uWSGI as root !!! (use the --uid flag) ***
python threads support enabled
your server socket listen backlog is limited to 100 connections
your mercy for graceful operations on workers is 60 seconds
mapped 486672 bytes (475 KB) for 5 cores
*** Operational MODE: preforking ***
WSGI app 0 (mountpoint='') ready in 0 seconds on interpreter 0x22a4a10 pid: 23203 (default app)
*** WARNING: you are running uWSGI as root !!! (use the --uid flag) ***
*** uWSGI is running in multiple interpreter mode ***
spawned uWSGI master process (pid: 23203)
spawned uWSGI worker 1 (pid: 23205, cores: 1)
spawned uWSGI worker 2 (pid: 23206, cores: 1)
spawned uWSGI worker 3 (pid: 23207, cores: 1)
spawned uWSGI worker 4 (pid: 23208, cores: 1)
spawned uWSGI worker 5 (pid: 23209, cores: 1)
spawned uWSGI http 1 (pid: 23210)
[pid: 23205|app: 0|req: 1/1] 218.247.217.98 () {38 vars in 675 bytes} [Fri Nov 30 07:06:39 2018] GET /index => generated 7174 bytes in 18 msecs (HTTP/1.1 200) 3 headers in 110 bytes (1 switches on core 0)
[pid: 23206|app: 0|req: 1/2] 218.247.217.98 () {38 vars in 715 bytes} [Fri Nov 30 07:06:39 2018] GET /demo/welcome.html => generated 24253 bytes in 18 msecs (HTTP/1.1 200) 3 headers in 111 bytes (1 switches on core 0)
[pid: 23207|app: 0|req: 1/3] 218.247.217.98 () {36 vars in 598 bytes} [Fri Nov 30 07:06:39 2018] GET /js/index.js => generated 7174 bytes in 17 msecs (HTTP/1.1 200) 3 headers in 110 bytes (1 switches on core 0)
Not Found: /frame/static/js/vip_nav.js
[pid: 23209|app: 0|req: 1/4] 218.247.217.98 () {36 vars in 616 bytes} [Fri Nov 30 07:06:39 2018] GET /frame/static/js/vip_nav.js => generated 4584 bytes in 16 msecs (HTTP/1.1 404) 3 headers in 102 bytes (1 switches on core 0)
Not Found: /demo/vip_tab.js
[pid: 23208|app: 0|req: 1/5] 218.247.217.98 () {36 vars in 606 bytes} [Fri Nov 30 07:06:39 2018] GET /demo/vip_tab.js => generated 4551 bytes in 16 msecs (HTTP/1.1 404) 3 headers in 102 bytes (1 switches on core 0)
[pid: 23205|app: 0|req: 2/6] 218.247.217.98 () {38 vars in 715 bytes} [Fri Nov 30 07:06:40 2018] GET /spider/basic.html => generated 12233 bytes in 2 msecs (HTTP/1.1 200) 3 headers in 111 bytes (1 switches on core 0)
[pid: 23206|app: 0|req: 2/7] 218.247.217.98 () {38 vars in 699 bytes} [Fri Nov 30 07:06:40 2018] GET /data/?page=1&limit=30 => generated 11497 bytes in 30 msecs (HTTP/1.1 200) 3 headers in 102 bytes (2 switches on core 0)
[pid: 23207|app: 0|req: 2/8] 218.247.217.98 () {38 vars in 725 bytes} [Fri Nov 30 07:06:41 2018] GET /spider/distribute.html => generated 3960 bytes in 2 msecs (HTTP/1.1 200) 3 headers in 110 bytes (1 switches on core 0)
[pid: 23209|app: 0|req: 2/9] 218.247.217.98 () {38 vars in 718 bytes} [Fri Nov 30 07:06:41 2018] GET /distribute_/?page=1&limit=20 => generated 6706 bytes in 33 msecs (HTTP/1.1 200) 3 headers in 101 bytes (2 switches on core 0)
[pid: 23208|app: 0|req: 2/10] 218.247.217.98 () {38 vars in 715 bytes} [Fri Nov 30 07:06:46 2018] GET /spider/mysql.html => generated 3240 bytes in 8 msecs (HTTP/1.1 200) 3 headers in 110 bytes (1 switches on core 0)
[pid: 23205|app: 0|req: 3/11] 218.247.217.98 () {38 vars in 703 bytes} [Fri Nov 30 07:06:46 2018] GET /mysql_/?page=1&limit=16 => generated 7666 bytes in 23 msecs (HTTP/1.1 200) 3 headers in 101 bytes (2 switches on core 0)
[pid: 23206|app: 0|req: 3/12] 218.247.217.98 () {38 vars in 711 bytes} [Fri Nov 30 07:06:48 2018] GET /spider/pid.html => generated 3845 bytes in 1 msecs (HTTP/1.1 200) 3 headers in 110 bytes (1 switches on core 0)
[pid: 23207|app: 0|req: 3/13] 218.247.217.98 () {38 vars in 697 bytes} [Fri Nov 30 07:06:48 2018] GET /pid_/?page=1&limit=16 => generated 3261 bytes in 22 msecs (HTTP/1.1 200) 3 headers in 101 bytes (2 switches on core 0)
[pid: 23209|app: 0|req: 3/14] 218.247.217.98 () {38 vars in 717 bytes} [Fri Nov 30 07:06:50 2018] GET /spider/server.html => generated 3582 bytes in 7 msecs (HTTP/1.1 200) 3 headers in 110 bytes (1 switches on core 0)
[pid: 23208|app: 0|req: 3/15] 218.247.217.98 () {38 vars in 706 bytes} [Fri Nov 30 07:06:50 2018] GET /server_/?page=1&limit=16 => generated 1099 bytes in 35 msecs (HTTP/1.1 200) 3 headers in 101 bytes (2 switches on core 0)
[pid: 23205|app: 0|req: 4/16] 218.247.217.98 () {38 vars in 721 bytes} [Fri Nov 30 07:06:51 2018] GET /spider/rebbitmq.html => generated 3995 bytes in 1 msecs (HTTP/1.1 200) 3 headers in 110 bytes (1 switches on core 0)
[pid: 23206|app: 0|req: 4/17] 218.247.217.98 () {38 vars in 712 bytes} [Fri Nov 30 07:06:51 2018] GET /rebbitmq_/?page=1&limit=16 => generated 7351 bytes in 24 msecs (HTTP/1.1 200) 3 headers in 101 bytes (2 switches on core 0)
[pid: 23207|app: 0|req: 4/18] 218.247.217.98 () {38 vars in 675 bytes} [Fri Nov 30 07:09:13 2018] GET /index => generated 7174 bytes in 1 msecs (HTTP/1.1 200) 3 headers in 110 bytes (1 switches on core 0)
[pid: 23209|app: 0|req: 4/19] 218.247.217.98 () {38 vars in 715 bytes} [Fri Nov 30 07:09:13 2018] GET /demo/welcome.html => generated 24253 bytes in 1 msecs (HTTP/1.1 200) 3 headers in 111 bytes (1 switches on core 0)
[pid: 23208|app: 0|req: 4/20] 218.247.217.98 () {36 vars in 598 bytes} [Fri Nov 30 07:09:13 2018] GET /js/index.js => generated 7174 bytes in 1 msecs (HTTP/1.1 200) 3 headers in 110 bytes (1 switches on core 0)
Not Found: /frame/static/js/vip_nav.js
[pid: 23205|app: 0|req: 5/21] 218.247.217.98 () {36 vars in 616 bytes} [Fri Nov 30 07:09:14 2018] GET /frame/static/js/vip_nav.js => generated 4584 bytes in 6 msecs (HTTP/1.1 404) 3 headers in 102 bytes (1 switches on core 0)
Not Found: /demo/vip_tab.js
[pid: 23206|app: 0|req: 5/22] 218.247.217.98 () {36 vars in 606 bytes} [Fri Nov 30 07:09:14 2018] GET /demo/vip_tab.js => generated 4551 bytes in 5 msecs (HTTP/1.1 404) 3 headers in 102 bytes (1 switches on core 0)
[pid: 23207|app: 0|req: 5/23] 218.247.217.98 () {38 vars in 715 bytes} [Fri Nov 30 07:09:15 2018] GET /spider/basic.html => generated 12233 bytes in 1 msecs (HTTP/1.1 200) 3 headers in 111 bytes (1 switches on core 0)
[pid: 23209|app: 0|req: 5/24] 218.247.217.98 () {38 vars in 699 bytes} [Fri Nov 30 07:09:15 2018] GET /data/?page=1&limit=30 => generated 11497 bytes in 27 msecs (HTTP/1.1 200) 3 headers in 102 bytes (2 switches on core 0)
Fri Nov 30 07:19:36 2018 - uWSGI worker 4 screams: UAAAAAAH my master disconnected: i will kill myself !!!
Fri Nov 30 07:19:36 2018 - uWSGI worker 3 screams: UAAAAAAH my master disconnected: i will kill myself !!!
Fri Nov 30 07:19:36 2018 - uWSGI worker 5 screams: UAAAAAAH my master disconnected: i will kill myself !!!
*** Starting uWSGI 2.0.17.1 (64bit) on [Fri Nov 30 15:21:08 2018] ***
compiled with version: 4.4.7 20120313 (Red Hat 4.4.7-23) on 30 November 2018 04:50:16
os: Linux-2.6.32-696.6.3.el6.x86_64 #1 SMP Wed Jul 12 14:17:22 UTC 2017
nodename: iZ2zegdkenf5ki7xp8k3wkZ
machine: x86_64
clock source: unix
pcre jit disabled
detected number of CPU cores: 2
current working directory: /root
writing pidfile to /root/script/uwsgi.pid
detected binary path: /usr/local/bin/uwsgi
*** WARNING: you are running uWSGI as root !!! (use the --uid flag) ***
chdir() to /root/twodj/
your processes number limit is 15245
your memory page size is 4096 bytes
detected max file descriptor number: 65535
building mime-types dictionary from file /etc/mime.types...883 entry found
lock engine: pthread robust mutexes
thunder lock: enabled
uWSGI http bound on 0.0.0.0:8000 fd 3
uwsgi socket 0 bound to UNIX address /root/script/uwsgi.sock fd 6
*** WARNING: you are running uWSGI as root !!! (use the --uid flag) ***
Python version: 3.6.7 (default, Nov  9 2018, 10:03:30)  [GCC 4.4.7 20120313 (Red Hat 4.4.7-23)]
Python main interpreter initialized at 0x2631a10
*** WARNING: you are running uWSGI as root !!! (use the --uid flag) ***
python threads support enabled
your server socket listen backlog is limited to 100 connections
your mercy for graceful operations on workers is 60 seconds
mapped 486672 bytes (475 KB) for 5 cores
*** Operational MODE: preforking ***
WSGI app 0 (mountpoint='') ready in 1 seconds on interpreter 0x2631a10 pid: 23255 (default app)
*** WARNING: you are running uWSGI as root !!! (use the --uid flag) ***
*** uWSGI is running in multiple interpreter mode ***
spawned uWSGI master process (pid: 23255)
spawned uWSGI worker 1 (pid: 23257, cores: 1)
spawned uWSGI worker 2 (pid: 23258, cores: 1)
spawned uWSGI worker 3 (pid: 23259, cores: 1)
spawned uWSGI worker 4 (pid: 23260, cores: 1)
spawned uWSGI worker 5 (pid: 23261, cores: 1)
spawned uWSGI http 1 (pid: 23262)
[pid: 23257|app: 0|req: 1/1] 218.247.217.98 () {38 vars in 675 bytes} [Fri Nov 30 07:21:34 2018] GET /index => generated 7174 bytes in 19 msecs (HTTP/1.1 200) 3 headers in 110 bytes (1 switches on core 0)
[pid: 23258|app: 0|req: 1/2] 218.247.217.98 () {38 vars in 715 bytes} [Fri Nov 30 07:21:34 2018] GET /demo/welcome.html => generated 24253 bytes in 19 msecs (HTTP/1.1 200) 3 headers in 111 bytes (1 switches on core 0)
[pid: 23259|app: 0|req: 1/3] 218.247.217.98 () {36 vars in 598 bytes} [Fri Nov 30 07:21:34 2018] GET /js/index.js => generated 7174 bytes in 19 msecs (HTTP/1.1 200) 3 headers in 110 bytes (1 switches on core 0)
Not Found: /frame/static/js/vip_nav.js
[pid: 23261|app: 0|req: 1/4] 218.247.217.98 () {36 vars in 616 bytes} [Fri Nov 30 07:21:34 2018] GET /frame/static/js/vip_nav.js => generated 4584 bytes in 17 msecs (HTTP/1.1 404) 3 headers in 102 bytes (1 switches on core 0)
Not Found: /demo/vip_tab.js
[pid: 23260|app: 0|req: 1/5] 218.247.217.98 () {36 vars in 606 bytes} [Fri Nov 30 07:21:34 2018] GET /demo/vip_tab.js => generated 4551 bytes in 17 msecs (HTTP/1.1 404) 3 headers in 102 bytes (1 switches on core 0)
[pid: 23257|app: 0|req: 2/6] 218.247.217.98 () {38 vars in 715 bytes} [Fri Nov 30 07:21:35 2018] GET /spider/basic.html => generated 12233 bytes in 2 msecs (HTTP/1.1 200) 3 headers in 111 bytes (1 switches on core 0)
[pid: 23258|app: 0|req: 2/7] 218.247.217.98 () {38 vars in 699 bytes} [Fri Nov 30 07:21:35 2018] GET /data/?page=1&limit=30 => generated 11497 bytes in 34 msecs (HTTP/1.1 200) 3 headers in 102 bytes (2 switches on core 0)
[pid: 23259|app: 0|req: 2/8] 218.247.217.98 () {38 vars in 725 bytes} [Fri Nov 30 07:21:36 2018] GET /spider/distribute.html => generated 3960 bytes in 2 msecs (HTTP/1.1 200) 3 headers in 110 bytes (1 switches on core 0)
[pid: 23261|app: 0|req: 2/9] 218.247.217.98 () {38 vars in 718 bytes} [Fri Nov 30 07:21:36 2018] GET /distribute_/?page=1&limit=20 => generated 6706 bytes in 41 msecs (HTTP/1.1 200) 3 headers in 101 bytes (2 switches on core 0)
[pid: 23260|app: 0|req: 2/10] 218.247.217.98 () {38 vars in 709 bytes} [Fri Nov 30 07:21:37 2018] GET /spider/pid.html => generated 3845 bytes in 8 msecs (HTTP/1.1 200) 3 headers in 110 bytes (1 switches on core 0)
[pid: 23257|app: 0|req: 3/11] 218.247.217.98 () {38 vars in 696 bytes} [Fri Nov 30 07:21:37 2018] GET /pid_/?page=1&limit=16 => generated 3261 bytes in 29 msecs (HTTP/1.1 200) 3 headers in 101 bytes (2 switches on core 0)
[pid: 23258|app: 0|req: 3/12] 218.247.217.98 () {38 vars in 714 bytes} [Fri Nov 30 07:21:39 2018] GET /spider/mysql.html => generated 3240 bytes in 1 msecs (HTTP/1.1 200) 3 headers in 110 bytes (1 switches on core 0)
[pid: 23259|app: 0|req: 3/13] 218.247.217.98 () {38 vars in 702 bytes} [Fri Nov 30 07:21:39 2018] GET /mysql_/?page=1&limit=16 => generated 7665 bytes in 28 msecs (HTTP/1.1 200) 3 headers in 101 bytes (2 switches on core 0)
[pid: 23261|app: 0|req: 3/14] 218.247.217.98 () {38 vars in 720 bytes} [Fri Nov 30 07:21:40 2018] GET /spider/rebbitmq.html => generated 3995 bytes in 8 msecs (HTTP/1.1 200) 3 headers in 110 bytes (1 switches on core 0)
[pid: 23260|app: 0|req: 3/15] 218.247.217.98 () {38 vars in 711 bytes} [Fri Nov 30 07:21:40 2018] GET /rebbitmq_/?page=1&limit=16 => generated 7351 bytes in 32 msecs (HTTP/1.1 200) 3 headers in 101 bytes (2 switches on core 0)
[pid: 23257|app: 0|req: 4/16] 218.247.217.98 () {38 vars in 716 bytes} [Fri Nov 30 07:21:41 2018] GET /spider/server.html => generated 3582 bytes in 1 msecs (HTTP/1.1 200) 3 headers in 110 bytes (1 switches on core 0)
[pid: 23258|app: 0|req: 4/17] 218.247.217.98 () {38 vars in 705 bytes} [Fri Nov 30 07:21:41 2018] GET /server_/?page=1&limit=16 => generated 1099 bytes in 19 msecs (HTTP/1.1 200) 3 headers in 101 bytes (2 switches on core 0)
[pid: 23259|app: 0|req: 4/18] 218.247.217.98 () {38 vars in 675 bytes} [Fri Nov 30 07:36:42 2018] GET /index => generated 7174 bytes in 1 msecs (HTTP/1.1 200) 3 headers in 110 bytes (1 switches on core 0)
[pid: 23261|app: 0|req: 4/19] 218.247.217.98 () {38 vars in 715 bytes} [Fri Nov 30 07:36:42 2018] GET /demo/welcome.html => generated 24253 bytes in 1 msecs (HTTP/1.1 200) 3 headers in 111 bytes (1 switches on core 0)
[pid: 23260|app: 0|req: 4/20] 218.247.217.98 () {36 vars in 598 bytes} [Fri Nov 30 07:36:42 2018] GET /js/index.js => generated 7174 bytes in 1 msecs (HTTP/1.1 200) 3 headers in 110 bytes (1 switches on core 0)
Not Found: /frame/static/js/vip_nav.js
[pid: 23257|app: 0|req: 5/21] 218.247.217.98 () {36 vars in 616 bytes} [Fri Nov 30 07:36:43 2018] GET /frame/static/js/vip_nav.js => generated 4584 bytes in 6 msecs (HTTP/1.1 404) 3 headers in 102 bytes (1 switches on core 0)
Not Found: /demo/vip_tab.js
[pid: 23258|app: 0|req: 5/22] 218.247.217.98 () {36 vars in 606 bytes} [Fri Nov 30 07:36:43 2018] GET /demo/vip_tab.js => generated 4551 bytes in 5 msecs (HTTP/1.1 404) 3 headers in 102 bytes (1 switches on core 0)
[pid: 23259|app: 0|req: 5/23] 218.247.217.98 () {38 vars in 715 bytes} [Fri Nov 30 07:36:44 2018] GET /spider/basic.html => generated 12233 bytes in 1 msecs (HTTP/1.1 200) 3 headers in 111 bytes (1 switches on core 0)
[pid: 23261|app: 0|req: 5/24] 218.247.217.98 () {38 vars in 699 bytes} [Fri Nov 30 07:36:44 2018] GET /data/?page=1&limit=30 => generated 11497 bytes in 20 msecs (HTTP/1.1 200) 3 headers in 102 bytes (2 switches on core 0)
[pid: 23260|app: 0|req: 5/25] 218.247.217.98 () {38 vars in 725 bytes} [Fri Nov 30 07:36:45 2018] GET /spider/distribute.html => generated 3960 bytes in 1 msecs (HTTP/1.1 200) 3 headers in 110 bytes (1 switches on core 0)
[pid: 23257|app: 0|req: 6/26] 218.247.217.98 () {38 vars in 718 bytes} [Fri Nov 30 07:36:45 2018] GET /distribute_/?page=1&limit=20 => generated 6706 bytes in 30 msecs (HTTP/1.1 200) 3 headers in 101 bytes (2 switches on core 0)
[pid: 23258|app: 0|req: 6/27] 218.247.217.98 () {38 vars in 711 bytes} [Fri Nov 30 07:36:46 2018] GET /spider/pid.html => generated 3845 bytes in 1 msecs (HTTP/1.1 200) 3 headers in 110 bytes (1 switches on core 0)
[pid: 23259|app: 0|req: 6/28] 218.247.217.98 () {38 vars in 697 bytes} [Fri Nov 30 07:36:46 2018] GET /pid_/?page=1&limit=16 => generated 3261 bytes in 23 msecs (HTTP/1.1 200) 3 headers in 101 bytes (2 switches on core 0)
[pid: 23261|app: 0|req: 6/29] 218.247.217.98 () {38 vars in 715 bytes} [Fri Nov 30 07:36:47 2018] GET /spider/mysql.html => generated 3240 bytes in 1 msecs (HTTP/1.1 200) 3 headers in 110 bytes (1 switches on core 0)
[pid: 23260|app: 0|req: 6/30] 218.247.217.98 () {38 vars in 703 bytes} [Fri Nov 30 07:36:47 2018] GET /mysql_/?page=1&limit=16 => generated 7665 bytes in 19 msecs (HTTP/1.1 200) 3 headers in 101 bytes (2 switches on core 0)
[pid: 23257|app: 0|req: 7/31] 218.247.217.98 () {38 vars in 721 bytes} [Fri Nov 30 07:36:48 2018] GET /spider/rebbitmq.html => generated 3995 bytes in 1 msecs (HTTP/1.1 200) 3 headers in 110 bytes (1 switches on core 0)
[pid: 23258|app: 0|req: 7/32] 218.247.217.98 () {38 vars in 712 bytes} [Fri Nov 30 07:36:48 2018] GET /rebbitmq_/?page=1&limit=16 => generated 7351 bytes in 18 msecs (HTTP/1.1 200) 3 headers in 101 bytes (2 switches on core 0)
[pid: 23259|app: 0|req: 7/33] 218.247.217.98 () {38 vars in 717 bytes} [Fri Nov 30 07:36:48 2018] GET /spider/server.html => generated 3582 bytes in 1 msecs (HTTP/1.1 200) 3 headers in 110 bytes (1 switches on core 0)
[pid: 23261|app: 0|req: 7/34] 218.247.217.98 () {38 vars in 706 bytes} [Fri Nov 30 07:36:49 2018] GET /server_/?page=1&limit=16 => generated 1099 bytes in 19 msecs (HTTP/1.1 200) 3 headers in 101 bytes (2 switches on core 0)
Fri Nov 30 07:37:37 2018 - uWSGI worker 4 screams: UAAAAAAH my master disconnected: i will kill myself !!!
Fri Nov 30 07:37:37 2018 - uWSGI worker 5 screams: UAAAAAAH my master disconnected: i will kill myself !!!
*** Starting uWSGI 2.0.17.1 (64bit) on [Fri Nov 30 15:37:51 2018] ***
compiled with version: 4.4.7 20120313 (Red Hat 4.4.7-23) on 30 November 2018 04:50:16
os: Linux-2.6.32-696.6.3.el6.x86_64 #1 SMP Wed Jul 12 14:17:22 UTC 2017
nodename: iZ2zegdkenf5ki7xp8k3wkZ
machine: x86_64
clock source: unix
pcre jit disabled
detected number of CPU cores: 2
current working directory: /root
writing pidfile to /root/script/uwsgi.pid
detected binary path: /usr/local/bin/uwsgi
*** WARNING: you are running uWSGI as root !!! (use the --uid flag) ***
chdir() to /root/twodj/
your processes number limit is 15245
your memory page size is 4096 bytes
detected max file descriptor number: 65535
building mime-types dictionary from file /etc/mime.types...883 entry found
lock engine: pthread robust mutexes
thunder lock: enabled
probably another instance of uWSGI is running on the same address (0.0.0.0:8000).
bind(): Address already in use [core/socket.c line 769]
*** Starting uWSGI 2.0.17.1 (64bit) on [Fri Nov 30 16:48:46 2018] ***
compiled with version: 4.4.7 20120313 (Red Hat 4.4.7-23) on 30 November 2018 04:50:16
os: Linux-2.6.32-696.6.3.el6.x86_64 #1 SMP Wed Jul 12 14:17:22 UTC 2017
nodename: iZ2zegdkenf5ki7xp8k3wkZ
machine: x86_64
clock source: unix
pcre jit disabled
detected number of CPU cores: 2
current working directory: /etc/nginx/conf.d
writing pidfile to /root/script/uwsgi.pid
detected binary path: /usr/local/bin/uwsgi
*** WARNING: you are running uWSGI as root !!! (use the --uid flag) ***
chdir() to /root/twodj/
your processes number limit is 15245
your memory page size is 4096 bytes
detected max file descriptor number: 65535
building mime-types dictionary from file /etc/mime.types...883 entry found
lock engine: pthread robust mutexes
thunder lock: enabled
probably another instance of uWSGI is running on the same address (0.0.0.0:8000).
bind(): Address already in use [core/socket.c line 769]
*** Starting uWSGI 2.0.17.1 (64bit) on [Fri Nov 30 16:50:24 2018] ***
compiled with version: 4.4.7 20120313 (Red Hat 4.4.7-23) on 30 November 2018 04:50:16
os: Linux-2.6.32-696.6.3.el6.x86_64 #1 SMP Wed Jul 12 14:17:22 UTC 2017
nodename: iZ2zegdkenf5ki7xp8k3wkZ
machine: x86_64
clock source: unix
pcre jit disabled
detected number of CPU cores: 2
current working directory: /etc/nginx/conf.d
writing pidfile to /root/script/uwsgi.pid
detected binary path: /usr/local/bin/uwsgi
*** WARNING: you are running uWSGI as root !!! (use the --uid flag) ***
chdir() to /root/twodj/
your processes number limit is 15245
your memory page size is 4096 bytes
detected max file descriptor number: 65535
building mime-types dictionary from file /etc/mime.types...883 entry found
lock engine: pthread robust mutexes
thunder lock: enabled
uWSGI http bound on 0.0.0.0:8000 fd 3
uwsgi socket 0 bound to UNIX address /root/script/uwsgi.sock fd 6
*** WARNING: you are running uWSGI as root !!! (use the --uid flag) ***
Python version: 3.6.7 (default, Nov  9 2018, 10:03:30)  [GCC 4.4.7 20120313 (Red Hat 4.4.7-23)]
Python main interpreter initialized at 0xa57a10
*** WARNING: you are running uWSGI as root !!! (use the --uid flag) ***
python threads support enabled
your server socket listen backlog is limited to 100 connections
your mercy for graceful operations on workers is 60 seconds
mapped 486672 bytes (475 KB) for 5 cores
*** Operational MODE: preforking ***
WSGI app 0 (mountpoint='') ready in 0 seconds on interpreter 0xa57a10 pid: 23565 (default app)
*** WARNING: you are running uWSGI as root !!! (use the --uid flag) ***
*** uWSGI is running in multiple interpreter mode ***
spawned uWSGI master process (pid: 23565)
spawned uWSGI worker 1 (pid: 23567, cores: 1)
spawned uWSGI worker 2 (pid: 23568, cores: 1)
spawned uWSGI worker 3 (pid: 23569, cores: 1)
spawned uWSGI worker 4 (pid: 23570, cores: 1)
spawned uWSGI worker 5 (pid: 23571, cores: 1)
spawned uWSGI http 1 (pid: 23572)
[pid: 23567|app: 0|req: 1/1] 218.247.217.98 () {38 vars in 675 bytes} [Fri Nov 30 08:50:29 2018] GET /index => generated 7174 bytes in 19 msecs (HTTP/1.1 200) 3 headers in 110 bytes (1 switches on core 0)
[pid: 23568|app: 0|req: 1/2] 218.247.217.98 () {38 vars in 715 bytes} [Fri Nov 30 08:50:29 2018] GET /demo/welcome.html => generated 24253 bytes in 19 msecs (HTTP/1.1 200) 3 headers in 111 bytes (1 switches on core 0)
[pid: 23569|app: 0|req: 1/3] 218.247.217.98 () {36 vars in 598 bytes} [Fri Nov 30 08:50:29 2018] GET /js/index.js => generated 7174 bytes in 18 msecs (HTTP/1.1 200) 3 headers in 110 bytes (1 switches on core 0)
Not Found: /frame/static/js/vip_nav.js
[pid: 23571|app: 0|req: 1/4] 218.247.217.98 () {36 vars in 616 bytes} [Fri Nov 30 08:50:29 2018] GET /frame/static/js/vip_nav.js => generated 4584 bytes in 17 msecs (HTTP/1.1 404) 3 headers in 102 bytes (1 switches on core 0)
Not Found: /demo/vip_tab.js
[pid: 23570|app: 0|req: 1/5] 218.247.217.98 () {36 vars in 606 bytes} [Fri Nov 30 08:50:30 2018] GET /demo/vip_tab.js => generated 4551 bytes in 17 msecs (HTTP/1.1 404) 3 headers in 102 bytes (1 switches on core 0)
[pid: 23567|app: 0|req: 2/6] 218.247.217.98 () {38 vars in 715 bytes} [Fri Nov 30 08:50:31 2018] GET /spider/basic.html => generated 12233 bytes in 2 msecs (HTTP/1.1 200) 3 headers in 111 bytes (1 switches on core 0)
[pid: 23568|app: 0|req: 2/7] 218.247.217.98 () {38 vars in 699 bytes} [Fri Nov 30 08:50:31 2018] GET /data/?page=1&limit=30 => generated 11497 bytes in 25 msecs (HTTP/1.1 200) 3 headers in 102 bytes (2 switches on core 0)
[pid: 23569|app: 0|req: 2/8] 218.247.217.98 () {38 vars in 725 bytes} [Fri Nov 30 08:50:32 2018] GET /spider/distribute.html => generated 3960 bytes in 2 msecs (HTTP/1.1 200) 3 headers in 110 bytes (1 switches on core 0)
[pid: 23571|app: 0|req: 2/9] 218.247.217.98 () {38 vars in 718 bytes} [Fri Nov 30 08:50:32 2018] GET /distribute_/?page=1&limit=20 => generated 6706 bytes in 38 msecs (HTTP/1.1 200) 3 headers in 101 bytes (2 switches on core 0)
[pid: 23570|app: 0|req: 2/10] 218.247.217.98 () {38 vars in 711 bytes} [Fri Nov 30 08:50:32 2018] GET /spider/pid.html => generated 3845 bytes in 8 msecs (HTTP/1.1 200) 3 headers in 110 bytes (1 switches on core 0)
[pid: 23567|app: 0|req: 3/11] 218.247.217.98 () {38 vars in 697 bytes} [Fri Nov 30 08:50:32 2018] GET /pid_/?page=1&limit=16 => generated 3261 bytes in 36 msecs (HTTP/1.1 200) 3 headers in 101 bytes (2 switches on core 0)
[pid: 23568|app: 0|req: 3/12] 218.247.217.98 () {38 vars in 715 bytes} [Fri Nov 30 08:50:33 2018] GET /spider/mysql.html => generated 3240 bytes in 1 msecs (HTTP/1.1 200) 3 headers in 110 bytes (1 switches on core 0)
[pid: 23569|app: 0|req: 3/13] 218.247.217.98 () {38 vars in 703 bytes} [Fri Nov 30 08:50:33 2018] GET /mysql_/?page=1&limit=16 => generated 7669 bytes in 23 msecs (HTTP/1.1 200) 3 headers in 101 bytes (2 switches on core 0)
[pid: 23571|app: 0|req: 3/14] 218.247.217.98 () {38 vars in 721 bytes} [Fri Nov 30 08:50:33 2018] GET /spider/rebbitmq.html => generated 3995 bytes in 7 msecs (HTTP/1.1 200) 3 headers in 110 bytes (1 switches on core 0)
[pid: 23570|app: 0|req: 3/15] 218.247.217.98 () {38 vars in 712 bytes} [Fri Nov 30 08:50:33 2018] GET /rebbitmq_/?page=1&limit=16 => generated 7351 bytes in 33 msecs (HTTP/1.1 200) 3 headers in 101 bytes (2 switches on core 0)
[pid: 23567|app: 0|req: 4/16] 218.247.217.98 () {38 vars in 717 bytes} [Fri Nov 30 08:50:34 2018] GET /spider/server.html => generated 3582 bytes in 1 msecs (HTTP/1.1 200) 3 headers in 110 bytes (1 switches on core 0)
[pid: 23568|app: 0|req: 4/17] 218.247.217.98 () {38 vars in 706 bytes} [Fri Nov 30 08:50:34 2018] GET /server_/?page=1&limit=16 => generated 1099 bytes in 19 msecs (HTTP/1.1 200) 3 headers in 101 bytes (2 switches on core 0)
[pid: 23569|app: 0|req: 4/18] 218.247.217.98 () {38 vars in 675 bytes} [Fri Nov 30 09:02:03 2018] GET /index => generated 7174 bytes in 1 msecs (HTTP/1.1 200) 3 headers in 110 bytes (1 switches on core 0)
[pid: 23571|app: 0|req: 4/19] 218.247.217.98 () {38 vars in 715 bytes} [Fri Nov 30 09:02:03 2018] GET /demo/welcome.html => generated 24253 bytes in 1 msecs (HTTP/1.1 200) 3 headers in 111 bytes (1 switches on core 0)
[pid: 23570|app: 0|req: 4/20] 218.247.217.98 () {36 vars in 598 bytes} [Fri Nov 30 09:02:03 2018] GET /js/index.js => generated 7174 bytes in 1 msecs (HTTP/1.1 200) 3 headers in 110 bytes (1 switches on core 0)
Not Found: /frame/static/js/vip_nav.js
[pid: 23567|app: 0|req: 5/21] 218.247.217.98 () {36 vars in 616 bytes} [Fri Nov 30 09:02:03 2018] GET /frame/static/js/vip_nav.js => generated 4584 bytes in 6 msecs (HTTP/1.1 404) 3 headers in 102 bytes (1 switches on core 0)
Not Found: /demo/vip_tab.js
[pid: 23568|app: 0|req: 5/22] 218.247.217.98 () {36 vars in 606 bytes} [Fri Nov 30 09:02:03 2018] GET /demo/vip_tab.js => generated 4551 bytes in 5 msecs (HTTP/1.1 404) 3 headers in 102 bytes (1 switches on core 0)
*** Starting uWSGI 2.0.17.1 (64bit) on [Mon Dec  3 15:35:55 2018] ***
compiled with version: 4.4.7 20120313 (Red Hat 4.4.7-23) on 30 November 2018 04:50:16
os: Linux-2.6.32-696.6.3.el6.x86_64 #1 SMP Wed Jul 12 14:17:22 UTC 2017
nodename: iZ2zegdkenf5ki7xp8k3wkZ
machine: x86_64
clock source: unix
pcre jit disabled
detected number of CPU cores: 2
current working directory: /root/el_spiders/monitor
writing pidfile to /root/script/uwsgi.pid
detected binary path: /usr/local/bin/uwsgi
*** WARNING: you are running uWSGI as root !!! (use the --uid flag) ***
chdir() to /root/twodj/
your processes number limit is 15245
your memory page size is 4096 bytes
detected max file descriptor number: 65535
building mime-types dictionary from file /etc/mime.types...883 entry found
lock engine: pthread robust mutexes
thunder lock: enabled
probably another instance of uWSGI is running on the same address (0.0.0.0:8000).
bind(): Address already in use [core/socket.c line 769]
*** Starting uWSGI 2.0.17.1 (64bit) on [Mon Dec  3 15:36:26 2018] ***
compiled with version: 4.4.7 20120313 (Red Hat 4.4.7-23) on 30 November 2018 04:50:16
os: Linux-2.6.32-696.6.3.el6.x86_64 #1 SMP Wed Jul 12 14:17:22 UTC 2017
nodename: iZ2zegdkenf5ki7xp8k3wkZ
machine: x86_64
clock source: unix
pcre jit disabled
detected number of CPU cores: 2
current working directory: /root/el_spiders/monitor
writing pidfile to /root/script/uwsgi.pid
detected binary path: /usr/local/bin/uwsgi
*** WARNING: you are running uWSGI as root !!! (use the --uid flag) ***
chdir() to /root/twodj/
your processes number limit is 15245
your memory page size is 4096 bytes
detected max file descriptor number: 65535
building mime-types dictionary from file /etc/mime.types...883 entry found
lock engine: pthread robust mutexes
thunder lock: enabled
probably another instance of uWSGI is running on the same address (0.0.0.0:8000).
bind(): Address already in use [core/socket.c line 769]
*** Starting uWSGI 2.0.17.1 (64bit) on [Mon Dec  3 15:36:46 2018] ***
compiled with version: 4.4.7 20120313 (Red Hat 4.4.7-23) on 30 November 2018 04:50:16
os: Linux-2.6.32-696.6.3.el6.x86_64 #1 SMP Wed Jul 12 14:17:22 UTC 2017
nodename: iZ2zegdkenf5ki7xp8k3wkZ
machine: x86_64
clock source: unix
pcre jit disabled
detected number of CPU cores: 2
current working directory: /root/el_spiders/monitor
writing pidfile to /root/script/uwsgi.pid
detected binary path: /usr/local/bin/uwsgi
*** WARNING: you are running uWSGI as root !!! (use the --uid flag) ***
chdir() to /root/twodj/
your processes number limit is 15245
your memory page size is 4096 bytes
detected max file descriptor number: 65535
building mime-types dictionary from file /etc/mime.types...883 entry found
lock engine: pthread robust mutexes
thunder lock: enabled
probably another instance of uWSGI is running on the same address (0.0.0.0:8000).
bind(): Address already in use [core/socket.c line 769]
*** Starting uWSGI 2.0.17.1 (64bit) on [Mon Dec  3 15:49:37 2018] ***
compiled with version: 4.4.7 20120313 (Red Hat 4.4.7-23) on 30 November 2018 04:50:16
os: Linux-2.6.32-696.6.3.el6.x86_64 #1 SMP Wed Jul 12 14:17:22 UTC 2017
nodename: iZ2zegdkenf5ki7xp8k3wkZ
machine: x86_64
clock source: unix
pcre jit disabled
detected number of CPU cores: 2
current working directory: /root/twodj
writing pidfile to /root/script/uwsgi.pid
detected binary path: /usr/local/bin/uwsgi
*** WARNING: you are running uWSGI as root !!! (use the --uid flag) ***
chdir() to /root/twodj/
your processes number limit is 15245
your memory page size is 4096 bytes
detected max file descriptor number: 65535
building mime-types dictionary from file /etc/mime.types...883 entry found
lock engine: pthread robust mutexes
thunder lock: enabled
uWSGI http bound on 0.0.0.0:8000 fd 3
uwsgi socket 0 bound to UNIX address /root/script/uwsgi.sock fd 6
*** WARNING: you are running uWSGI as root !!! (use the --uid flag) ***
Python version: 3.6.7 (default, Nov  9 2018, 10:03:30)  [GCC 4.4.7 20120313 (Red Hat 4.4.7-23)]
Python main interpreter initialized at 0x27f3a20
*** WARNING: you are running uWSGI as root !!! (use the --uid flag) ***
python threads support enabled
your server socket listen backlog is limited to 100 connections
your mercy for graceful operations on workers is 60 seconds
mapped 486672 bytes (475 KB) for 5 cores
*** Operational MODE: preforking ***
WSGI app 0 (mountpoint='') ready in 0 seconds on interpreter 0x27f3a20 pid: 2680 (default app)
*** WARNING: you are running uWSGI as root !!! (use the --uid flag) ***
*** uWSGI is running in multiple interpreter mode ***
spawned uWSGI master process (pid: 2680)
spawned uWSGI worker 1 (pid: 2682, cores: 1)
spawned uWSGI worker 2 (pid: 2683, cores: 1)
spawned uWSGI worker 3 (pid: 2684, cores: 1)
spawned uWSGI worker 4 (pid: 2685, cores: 1)
spawned uWSGI worker 5 (pid: 2686, cores: 1)
spawned uWSGI http 1 (pid: 2687)
[pid: 2682|app: 0|req: 1/1] 218.247.217.98 () {38 vars in 675 bytes} [Mon Dec  3 07:49:40 2018] GET /index => generated 7174 bytes in 19 msecs (HTTP/1.1 200) 3 headers in 110 bytes (1 switches on core 0)
[pid: 2683|app: 0|req: 1/2] 218.247.217.98 () {38 vars in 715 bytes} [Mon Dec  3 07:49:40 2018] GET /demo/welcome.html => generated 24253 bytes in 18 msecs (HTTP/1.1 200) 3 headers in 111 bytes (1 switches on core 0)
[pid: 2685|app: 0|req: 1/3] 218.247.217.98 () {36 vars in 598 bytes} [Mon Dec  3 07:49:41 2018] GET /js/index.js => generated 7174 bytes in 17 msecs (HTTP/1.1 200) 3 headers in 110 bytes (1 switches on core 0)
Not Found: /frame/static/js/vip_nav.js
[pid: 2686|app: 0|req: 1/4] 218.247.217.98 () {36 vars in 616 bytes} [Mon Dec  3 07:49:41 2018] GET /frame/static/js/vip_nav.js => generated 4584 bytes in 16 msecs (HTTP/1.1 404) 3 headers in 102 bytes (1 switches on core 0)
Not Found: /demo/vip_tab.js
[pid: 2684|app: 0|req: 1/5] 218.247.217.98 () {36 vars in 606 bytes} [Mon Dec  3 07:49:41 2018] GET /demo/vip_tab.js => generated 4551 bytes in 17 msecs (HTTP/1.1 404) 3 headers in 102 bytes (1 switches on core 0)
[pid: 2682|app: 0|req: 2/6] 218.247.217.98 () {38 vars in 675 bytes} [Mon Dec  3 07:49:42 2018] GET /index => generated 7174 bytes in 1 msecs (HTTP/1.1 200) 3 headers in 110 bytes (1 switches on core 0)
[pid: 2683|app: 0|req: 2/7] 218.247.217.98 () {38 vars in 715 bytes} [Mon Dec  3 07:49:42 2018] GET /demo/welcome.html => generated 24253 bytes in 1 msecs (HTTP/1.1 200) 3 headers in 111 bytes (1 switches on core 0)
[pid: 2685|app: 0|req: 2/8] 218.247.217.98 () {36 vars in 598 bytes} [Mon Dec  3 07:49:42 2018] GET /js/index.js => generated 7174 bytes in 1 msecs (HTTP/1.1 200) 3 headers in 110 bytes (1 switches on core 0)
Not Found: /frame/static/js/vip_nav.js
[pid: 2686|app: 0|req: 2/9] 218.247.217.98 () {36 vars in 616 bytes} [Mon Dec  3 07:49:42 2018] GET /frame/static/js/vip_nav.js => generated 4584 bytes in 4 msecs (HTTP/1.1 404) 3 headers in 102 bytes (1 switches on core 0)
Not Found: /demo/vip_tab.js
[pid: 2684|app: 0|req: 2/10] 218.247.217.98 () {36 vars in 606 bytes} [Mon Dec  3 07:49:42 2018] GET /demo/vip_tab.js => generated 4551 bytes in 4 msecs (HTTP/1.1 404) 3 headers in 102 bytes (1 switches on core 0)
[pid: 2682|app: 0|req: 3/11] 218.247.217.98 () {38 vars in 675 bytes} [Mon Dec  3 07:49:43 2018] GET /index => generated 7174 bytes in 1 msecs (HTTP/1.1 200) 3 headers in 110 bytes (1 switches on core 0)
[pid: 2683|app: 0|req: 3/12] 218.247.217.98 () {38 vars in 715 bytes} [Mon Dec  3 07:49:43 2018] GET /demo/welcome.html => generated 24253 bytes in 1 msecs (HTTP/1.1 200) 3 headers in 111 bytes (1 switches on core 0)
[pid: 2685|app: 0|req: 3/13] 218.247.217.98 () {36 vars in 598 bytes} [Mon Dec  3 07:49:43 2018] GET /js/index.js => generated 7174 bytes in 1 msecs (HTTP/1.1 200) 3 headers in 110 bytes (1 switches on core 0)
Not Found: /frame/static/js/vip_nav.js
[pid: 2686|app: 0|req: 3/14] 218.247.217.98 () {36 vars in 616 bytes} [Mon Dec  3 07:49:43 2018] GET /frame/static/js/vip_nav.js => generated 4584 bytes in 4 msecs (HTTP/1.1 404) 3 headers in 102 bytes (1 switches on core 0)
Not Found: /demo/vip_tab.js
[pid: 2684|app: 0|req: 3/15] 218.247.217.98 () {36 vars in 606 bytes} [Mon Dec  3 07:49:43 2018] GET /demo/vip_tab.js => generated 4551 bytes in 4 msecs (HTTP/1.1 404) 3 headers in 102 bytes (1 switches on core 0)
[pid: 2682|app: 0|req: 4/16] 218.247.217.98 () {38 vars in 675 bytes} [Mon Dec  3 07:49:44 2018] GET /index => generated 7174 bytes in 1 msecs (HTTP/1.1 200) 3 headers in 110 bytes (1 switches on core 0)
[pid: 2683|app: 0|req: 4/17] 218.247.217.98 () {38 vars in 715 bytes} [Mon Dec  3 07:49:44 2018] GET /demo/welcome.html => generated 24253 bytes in 1 msecs (HTTP/1.1 200) 3 headers in 111 bytes (1 switches on core 0)
Not Found: /frame/static/js/vip_nav.js
[pid: 2685|app: 0|req: 4/18] 218.247.217.98 () {36 vars in 616 bytes} [Mon Dec  3 07:49:44 2018] GET /frame/static/js/vip_nav.js => generated 4584 bytes in 7 msecs (HTTP/1.1 404) 3 headers in 102 bytes (1 switches on core 0)
[pid: 2686|app: 0|req: 4/19] 218.247.217.98 () {36 vars in 598 bytes} [Mon Dec  3 07:49:44 2018] GET /js/index.js => generated 7174 bytes in 8 msecs (HTTP/1.1 200) 3 headers in 110 bytes (1 switches on core 0)
Not Found: /demo/vip_tab.js
[pid: 2684|app: 0|req: 4/20] 218.247.217.98 () {36 vars in 606 bytes} [Mon Dec  3 07:49:44 2018] GET /demo/vip_tab.js => generated 4551 bytes in 4 msecs (HTTP/1.1 404) 3 headers in 102 bytes (1 switches on core 0)
[pid: 2682|app: 0|req: 5/21] 218.247.217.98 () {38 vars in 675 bytes} [Mon Dec  3 07:49:49 2018] GET /index => generated 7174 bytes in 1 msecs (HTTP/1.1 200) 3 headers in 110 bytes (1 switches on core 0)
[pid: 2683|app: 0|req: 5/22] 218.247.217.98 () {38 vars in 715 bytes} [Mon Dec  3 07:49:49 2018] GET /demo/welcome.html => generated 24253 bytes in 1 msecs (HTTP/1.1 200) 3 headers in 111 bytes (1 switches on core 0)
[pid: 2685|app: 0|req: 5/23] 218.247.217.98 () {36 vars in 598 bytes} [Mon Dec  3 07:49:50 2018] GET /js/index.js => generated 7174 bytes in 1 msecs (HTTP/1.1 200) 3 headers in 110 bytes (1 switches on core 0)
Not Found: /frame/static/js/vip_nav.js
[pid: 2686|app: 0|req: 5/24] 218.247.217.98 () {36 vars in 616 bytes} [Mon Dec  3 07:49:50 2018] GET /frame/static/js/vip_nav.js => generated 4584 bytes in 4 msecs (HTTP/1.1 404) 3 headers in 102 bytes (1 switches on core 0)
Not Found: /demo/vip_tab.js
[pid: 2684|app: 0|req: 5/25] 218.247.217.98 () {36 vars in 606 bytes} [Mon Dec  3 07:49:50 2018] GET /demo/vip_tab.js => generated 4551 bytes in 4 msecs (HTTP/1.1 404) 3 headers in 102 bytes (1 switches on core 0)
[pid: 2682|app: 0|req: 6/26] 218.247.217.98 () {38 vars in 715 bytes} [Mon Dec  3 07:49:51 2018] GET /spider/basic.html => generated 12233 bytes in 2 msecs (HTTP/1.1 200) 3 headers in 111 bytes (1 switches on core 0)
[pid: 2683|app: 0|req: 6/27] 218.247.217.98 () {38 vars in 699 bytes} [Mon Dec  3 07:49:51 2018] GET /data/?page=1&limit=30 => generated 11502 bytes in 31 msecs (HTTP/1.1 200) 3 headers in 102 bytes (2 switches on core 0)
[pid: 2685|app: 0|req: 6/28] 218.247.217.98 () {38 vars in 715 bytes} [Mon Dec  3 07:49:54 2018] GET /spider/mysql.html => generated 3240 bytes in 1 msecs (HTTP/1.1 200) 3 headers in 110 bytes (1 switches on core 0)
[pid: 2686|app: 0|req: 6/29] 218.247.217.98 () {38 vars in 703 bytes} [Mon Dec  3 07:49:54 2018] GET /mysql_/?page=1&limit=16 => generated 7544 bytes in 28 msecs (HTTP/1.1 200) 3 headers in 101 bytes (2 switches on core 0)
Mon Dec  3 07:52:49 2018 - uWSGI worker 3 screams: UAAAAAAH my master disconnected: i will kill myself !!!
Mon Dec  3 07:52:49 2018 - uWSGI worker 1 screams: UAAAAAAH my master disconnected: i will kill myself !!!
Mon Dec  3 07:52:49 2018 - uWSGI worker 2 screams: UAAAAAAH my master disconnected: i will kill myself !!!
Mon Dec  3 07:52:49 2018 - uWSGI worker 4 screams: UAAAAAAH my master disconnected: i will kill myself !!!
Mon Dec  3 07:52:49 2018 - uWSGI worker 5 screams: UAAAAAAH my master disconnected: i will kill myself !!!
*** Starting uWSGI 2.0.17.1 (64bit) on [Mon Dec  3 16:42:52 2018] ***
compiled with version: 4.4.7 20120313 (Red Hat 4.4.7-23) on 30 November 2018 04:50:16
os: Linux-2.6.32-696.6.3.el6.x86_64 #1 SMP Wed Jul 12 14:17:22 UTC 2017
nodename: iZ2zegdkenf5ki7xp8k3wkZ
machine: x86_64
clock source: unix
pcre jit disabled
detected number of CPU cores: 2
current working directory: /root/twodj
writing pidfile to /root/script/uwsgi.pid
detected binary path: /usr/local/bin/uwsgi
*** WARNING: you are running uWSGI as root !!! (use the --uid flag) ***
chdir() to /root/twodj/
your processes number limit is 15245
your memory page size is 4096 bytes
detected max file descriptor number: 65535
building mime-types dictionary from file /etc/mime.types...883 entry found
lock engine: pthread robust mutexes
thunder lock: enabled
probably another instance of uWSGI is running on the same address (0.0.0.0:8000).
bind(): Address already in use [core/socket.c line 769]
*** Starting uWSGI 2.0.17.1 (64bit) on [Mon Dec  3 19:23:08 2018] ***
compiled with version: 4.4.7 20120313 (Red Hat 4.4.7-23) on 30 November 2018 04:50:16
os: Linux-2.6.32-696.6.3.el6.x86_64 #1 SMP Wed Jul 12 14:17:22 UTC 2017
nodename: iZ2zegdkenf5ki7xp8k3wkZ
machine: x86_64
clock source: unix
pcre jit disabled
detected number of CPU cores: 2
current working directory: /root/twodj
writing pidfile to /root/script/uwsgi.pid
detected binary path: /usr/local/bin/uwsgi
*** WARNING: you are running uWSGI as root !!! (use the --uid flag) ***
chdir() to /root/twodj/
your processes number limit is 15245
your memory page size is 4096 bytes
detected max file descriptor number: 65535
building mime-types dictionary from file /etc/mime.types...883 entry found
lock engine: pthread robust mutexes
thunder lock: enabled
uWSGI http bound on 0.0.0.0:8000 fd 3
uwsgi socket 0 bound to UNIX address /root/script/uwsgi.sock fd 6
*** WARNING: you are running uWSGI as root !!! (use the --uid flag) ***
Python version: 3.6.7 (default, Nov  9 2018, 10:03:30)  [GCC 4.4.7 20120313 (Red Hat 4.4.7-23)]
Python main interpreter initialized at 0xf0da20
*** WARNING: you are running uWSGI as root !!! (use the --uid flag) ***
python threads support enabled
your server socket listen backlog is limited to 100 connections
your mercy for graceful operations on workers is 60 seconds
mapped 486672 bytes (475 KB) for 5 cores
*** Operational MODE: preforking ***
WSGI app 0 (mountpoint='') ready in 0 seconds on interpreter 0xf0da20 pid: 3160 (default app)
*** WARNING: you are running uWSGI as root !!! (use the --uid flag) ***
*** uWSGI is running in multiple interpreter mode ***
spawned uWSGI master process (pid: 3160)
spawned uWSGI worker 1 (pid: 3162, cores: 1)
spawned uWSGI worker 2 (pid: 3163, cores: 1)
spawned uWSGI worker 3 (pid: 3164, cores: 1)
spawned uWSGI worker 4 (pid: 3165, cores: 1)
spawned uWSGI worker 5 (pid: 3166, cores: 1)
spawned uWSGI http 1 (pid: 3167)
[pid: 3162|app: 0|req: 1/1] 218.247.217.98 () {38 vars in 675 bytes} [Mon Dec  3 11:23:16 2018] GET /index => generated 7174 bytes in 19 msecs (HTTP/1.1 200) 3 headers in 110 bytes (1 switches on core 0)
[pid: 3163|app: 0|req: 1/2] 218.247.217.98 () {38 vars in 715 bytes} [Mon Dec  3 11:23:16 2018] GET /demo/welcome.html => generated 24253 bytes in 19 msecs (HTTP/1.1 200) 3 headers in 111 bytes (1 switches on core 0)
[pid: 3164|app: 0|req: 1/3] 218.247.217.98 () {36 vars in 598 bytes} [Mon Dec  3 11:23:16 2018] GET /js/index.js => generated 7174 bytes in 18 msecs (HTTP/1.1 200) 3 headers in 110 bytes (1 switches on core 0)
Not Found: /frame/static/js/vip_nav.js
[pid: 3165|app: 0|req: 1/4] 218.247.217.98 () {36 vars in 616 bytes} [Mon Dec  3 11:23:17 2018] GET /frame/static/js/vip_nav.js => generated 4584 bytes in 17 msecs (HTTP/1.1 404) 3 headers in 102 bytes (1 switches on core 0)
Not Found: /demo/vip_tab.js
[pid: 3166|app: 0|req: 1/5] 218.247.217.98 () {36 vars in 606 bytes} [Mon Dec  3 11:23:17 2018] GET /demo/vip_tab.js => generated 4551 bytes in 17 msecs (HTTP/1.1 404) 3 headers in 102 bytes (1 switches on core 0)
[pid: 3162|app: 0|req: 2/6] 218.247.217.98 () {38 vars in 675 bytes} [Mon Dec  3 11:23:53 2018] GET /index => generated 7174 bytes in 1 msecs (HTTP/1.1 200) 3 headers in 110 bytes (1 switches on core 0)
[pid: 3163|app: 0|req: 2/7] 218.247.217.98 () {38 vars in 715 bytes} [Mon Dec  3 11:23:53 2018] GET /demo/welcome.html => generated 24253 bytes in 1 msecs (HTTP/1.1 200) 3 headers in 111 bytes (1 switches on core 0)
[pid: 3164|app: 0|req: 2/8] 218.247.217.98 () {36 vars in 598 bytes} [Mon Dec  3 11:23:54 2018] GET /js/index.js => generated 7174 bytes in 1 msecs (HTTP/1.1 200) 3 headers in 110 bytes (1 switches on core 0)
Not Found: /frame/static/js/vip_nav.js
[pid: 3165|app: 0|req: 2/9] 218.247.217.98 () {36 vars in 616 bytes} [Mon Dec  3 11:23:54 2018] GET /frame/static/js/vip_nav.js => generated 4584 bytes in 4 msecs (HTTP/1.1 404) 3 headers in 102 bytes (1 switches on core 0)
Not Found: /demo/vip_tab.js
[pid: 3166|app: 0|req: 2/10] 218.247.217.98 () {36 vars in 606 bytes} [Mon Dec  3 11:23:54 2018] GET /demo/vip_tab.js => generated 4551 bytes in 4 msecs (HTTP/1.1 404) 3 headers in 102 bytes (1 switches on core 0)
Not Found: /
[pid: 3162|app: 0|req: 3/11] 218.247.217.98 () {38 vars in 656 bytes} [Mon Dec  3 11:23:56 2018] GET / => generated 4488 bytes in 7 msecs (HTTP/1.1 404) 3 headers in 102 bytes (1 switches on core 0)
Not Found: /favicon.ico
[pid: 3163|app: 0|req: 3/12] 218.247.217.98 () {36 vars in 615 bytes} [Mon Dec  3 11:23:56 2018] GET /favicon.ico => generated 4539 bytes in 6 msecs (HTTP/1.1 404) 3 headers in 102 bytes (1 switches on core 0)
Not Found: /
[pid: 3164|app: 0|req: 3/13] 218.247.217.98 () {38 vars in 664 bytes} [Mon Dec  3 11:23:57 2018] GET / => generated 4488 bytes in 7 msecs (HTTP/1.1 404) 3 headers in 102 bytes (1 switches on core 0)
Not Found: /
[pid: 3165|app: 0|req: 3/14] 218.247.217.98 () {38 vars in 664 bytes} [Mon Dec  3 11:23:58 2018] GET / => generated 4488 bytes in 4 msecs (HTTP/1.1 404) 3 headers in 102 bytes (1 switches on core 0)
[pid: 3166|app: 0|req: 3/15] 218.247.217.98 () {36 vars in 643 bytes} [Mon Dec  3 11:24:01 2018] GET /index => generated 7174 bytes in 8 msecs (HTTP/1.1 200) 3 headers in 110 bytes (1 switches on core 0)
[pid: 3162|app: 0|req: 4/16] 218.247.217.98 () {38 vars in 714 bytes} [Mon Dec  3 11:24:01 2018] GET /demo/welcome.html => generated 24253 bytes in 1 msecs (HTTP/1.1 200) 3 headers in 111 bytes (1 switches on core 0)
[pid: 3163|app: 0|req: 4/17] 218.247.217.98 () {36 vars in 597 bytes} [Mon Dec  3 11:24:01 2018] GET /js/index.js => generated 7174 bytes in 1 msecs (HTTP/1.1 200) 3 headers in 110 bytes (1 switches on core 0)
Not Found: /frame/static/js/vip_nav.js
[pid: 3164|app: 0|req: 4/18] 218.247.217.98 () {36 vars in 615 bytes} [Mon Dec  3 11:24:02 2018] GET /frame/static/js/vip_nav.js => generated 4584 bytes in 4 msecs (HTTP/1.1 404) 3 headers in 102 bytes (1 switches on core 0)
Not Found: /demo/vip_tab.js
[pid: 3165|app: 0|req: 4/19] 218.247.217.98 () {36 vars in 605 bytes} [Mon Dec  3 11:24:02 2018] GET /demo/vip_tab.js => generated 4551 bytes in 4 msecs (HTTP/1.1 404) 3 headers in 102 bytes (1 switches on core 0)
[pid: 3166|app: 0|req: 4/20] 47.95.122.113 () {30 vars in 362 bytes} [Mon Dec  3 11:26:06 2018] GET /index => generated 7174 bytes in 1 msecs (HTTP/1.0 200) 3 headers in 110 bytes (1 switches on core 0)
[pid: 3162|app: 0|req: 5/21] 47.95.122.113 () {30 vars in 362 bytes} [Mon Dec  3 11:26:25 2018] GET /index => generated 7174 bytes in 1 msecs (HTTP/1.0 200) 3 headers in 110 bytes (1 switches on core 0)
[pid: 3163|app: 0|req: 5/22] 47.95.122.113 () {30 vars in 362 bytes} [Mon Dec  3 11:26:27 2018] GET /index => generated 7174 bytes in 1 msecs (HTTP/1.0 200) 3 headers in 110 bytes (1 switches on core 0)
Mon Dec  3 11:30:47 2018 - uWSGI worker 3 screams: UAAAAAAH my master disconnected: i will kill myself !!!
Mon Dec  3 11:30:47 2018 - uWSGI worker 4 screams: UAAAAAAH my master disconnected: i will kill myself !!!
Mon Dec  3 11:30:47 2018 - uWSGI worker 5 screams: UAAAAAAH my master disconnected: i will kill myself !!!
*** Starting uWSGI 2.0.17.1 (64bit) on [Mon Dec  3 19:30:58 2018] ***
compiled with version: 4.4.7 20120313 (Red Hat 4.4.7-23) on 30 November 2018 04:50:16
os: Linux-2.6.32-696.6.3.el6.x86_64 #1 SMP Wed Jul 12 14:17:22 UTC 2017
nodename: iZ2zegdkenf5ki7xp8k3wkZ
machine: x86_64
clock source: unix
pcre jit disabled
detected number of CPU cores: 2
current working directory: /root/twodj
writing pidfile to /root/script/uwsgi.pid
detected binary path: /usr/local/bin/uwsgi
*** WARNING: you are running uWSGI as root !!! (use the --uid flag) ***
chdir() to /root/twodj/
your processes number limit is 15245
your memory page size is 4096 bytes
detected max file descriptor number: 65535
building mime-types dictionary from file /etc/mime.types...883 entry found
lock engine: pthread robust mutexes
thunder lock: enabled
uWSGI http bound on 0.0.0.0:6379 fd 3
uwsgi socket 0 bound to UNIX address /root/script/uwsgi.sock fd 6
*** WARNING: you are running uWSGI as root !!! (use the --uid flag) ***
Python version: 3.6.7 (default, Nov  9 2018, 10:03:30)  [GCC 4.4.7 20120313 (Red Hat 4.4.7-23)]
Python main interpreter initialized at 0x1081a20
*** WARNING: you are running uWSGI as root !!! (use the --uid flag) ***
python threads support enabled
your server socket listen backlog is limited to 100 connections
your mercy for graceful operations on workers is 60 seconds
mapped 486672 bytes (475 KB) for 5 cores
*** Operational MODE: preforking ***
WSGI app 0 (mountpoint='') ready in 0 seconds on interpreter 0x1081a20 pid: 3190 (default app)
*** WARNING: you are running uWSGI as root !!! (use the --uid flag) ***
*** uWSGI is running in multiple interpreter mode ***
spawned uWSGI master process (pid: 3190)
spawned uWSGI worker 1 (pid: 3192, cores: 1)
spawned uWSGI worker 2 (pid: 3193, cores: 1)
spawned uWSGI worker 3 (pid: 3194, cores: 1)
spawned uWSGI worker 4 (pid: 3195, cores: 1)
spawned uWSGI worker 5 (pid: 3196, cores: 1)
spawned uWSGI http 1 (pid: 3197)
[pid: 3192|app: 0|req: 1/1] 218.247.217.98 () {36 vars in 644 bytes} [Mon Dec  3 11:31:20 2018] GET /index => generated 7174 bytes in 19 msecs (HTTP/1.1 200) 3 headers in 110 bytes (1 switches on core 0)
Not Found: /src/frame/static/js/vip_comm.js
[pid: 3192|app: 0|req: 2/2] 218.247.217.98 () {36 vars in 626 bytes} [Mon Dec  3 11:31:20 2018] GET /src/frame/static/js/vip_comm.js => generated 4599 bytes in 18 msecs (HTTP/1.1 404) 3 headers in 102 bytes (2 switches on core 0)
Not Found: /src/frame/layui/css/layui.css
[pid: 3193|app: 0|req: 1/3] 218.247.217.98 () {36 vars in 637 bytes} [Mon Dec  3 11:31:20 2018] GET /src/frame/layui/css/layui.css => generated 4593 bytes in 47 msecs (HTTP/1.1 404) 3 headers in 102 bytes (1 switches on core 0)
Not Found: /src/frame/static/image/zfb.png
Not Found: /src/frame/static/css/style.css
[pid: 3196|app: 0|req: 1/4] 218.247.217.98 () {36 vars in 660 bytes} [Mon Dec  3 11:31:20 2018] GET /src/frame/static/image/zfb.png => generated 4596 bytes in 35 msecs (HTTP/1.1 404) 3 headers in 102 bytes (2 switches on core 0)
[pid: 3194|app: 0|req: 1/5] 218.247.217.98 () {36 vars in 639 bytes} [Mon Dec  3 11:31:20 2018] GET /src/frame/static/css/style.css => generated 4596 bytes in 47 msecs (HTTP/1.1 404) 3 headers in 102 bytes (2 switches on core 0)
Not Found: /src/frame/static/image/code.png
[pid: 3192|app: 0|req: 3/6] 218.247.217.98 () {36 vars in 662 bytes} [Mon Dec  3 11:31:20 2018] GET /src/frame/static/image/code.png => generated 4599 bytes in 14 msecs (HTTP/1.1 404) 3 headers in 102 bytes (1 switches on core 0)
[pid: 3193|app: 0|req: 2/7] 218.247.217.98 () {38 vars in 715 bytes} [Mon Dec  3 11:31:20 2018] GET /demo/welcome.html => generated 24253 bytes in 10 msecs (HTTP/1.1 200) 3 headers in 111 bytes (1 switches on core 0)
Not Found: /src/frame/static/image/wx.png
Not Found: /src/frame/layui/layui.js
[pid: 3196|app: 0|req: 2/8] 218.247.217.98 () {36 vars in 658 bytes} [Mon Dec  3 11:31:20 2018] GET /src/frame/static/image/wx.png => generated 4593 bytes in 5 msecs (HTTP/1.1 404) 3 headers in 102 bytes (1 switches on core 0)
[pid: 3195|app: 0|req: 1/9] 218.247.217.98 () {36 vars in 612 bytes} [Mon Dec  3 11:31:20 2018] GET /src/frame/layui/layui.js => generated 4578 bytes in 55 msecs (HTTP/1.1 404) 3 headers in 102 bytes (2 switches on core 0)
Not Found: /src/frame/static/css/style.css
[pid: 3192|app: 0|req: 4/10] 218.247.217.98 () {36 vars in 651 bytes} [Mon Dec  3 11:31:20 2018] GET /src/frame/static/css/style.css => generated 4596 bytes in 6 msecs (HTTP/1.1 404) 3 headers in 102 bytes (1 switches on core 0)
Not Found: /src/frame/layui/css/layui.css
Not Found: /src/layui/layui.js
[pid: 3194|app: 0|req: 2/11] 218.247.217.98 () {36 vars in 649 bytes} [Mon Dec  3 11:31:20 2018] GET /src/frame/layui/css/layui.css => generated 4593 bytes in 13 msecs (HTTP/1.1 404) 3 headers in 102 bytes (1 switches on core 0)
[pid: 3193|app: 0|req: 3/12] 218.247.217.98 () {36 vars in 612 bytes} [Mon Dec  3 11:31:20 2018] GET /src/layui/layui.js => generated 4560 bytes in 7 msecs (HTTP/1.1 404) 3 headers in 102 bytes (1 switches on core 0)
Not Found: /src/frame/echarts/echarts.min.js
[pid: 3192|app: 0|req: 5/13] 218.247.217.98 () {36 vars in 640 bytes} [Mon Dec  3 11:31:20 2018] GET /src/frame/echarts/echarts.min.js => generated 4602 bytes in 5 msecs (HTTP/1.1 404) 3 headers in 102 bytes (1 switches on core 0)
[pid: 3195|app: 0|req: 2/14] 218.247.217.98 () {36 vars in 598 bytes} [Mon Dec  3 11:31:20 2018] GET /js/index.js => generated 7174 bytes in 14 msecs (HTTP/1.1 200) 3 headers in 110 bytes (1 switches on core 0)
Not Found: /src/frame/static/js/vip_comm.js
[pid: 3196|app: 0|req: 3/15] 218.247.217.98 () {36 vars in 626 bytes} [Mon Dec  3 11:31:20 2018] GET /src/frame/static/js/vip_comm.js => generated 4599 bytes in 15 msecs (HTTP/1.1 404) 3 headers in 102 bytes (1 switches on core 0)
Not Found: /src/frame/echarts/echarts.min.js
[pid: 3194|app: 0|req: 3/16] 218.247.217.98 () {36 vars in 640 bytes} [Mon Dec  3 11:31:20 2018] GET /src/frame/echarts/echarts.min.js => generated 4602 bytes in 3 msecs (HTTP/1.1 404) 3 headers in 102 bytes (1 switches on core 0)
Not Found: /src/frame/static/image/code.png
[pid: 3193|app: 0|req: 4/17] 218.247.217.98 () {36 vars in 662 bytes} [Mon Dec  3 11:31:21 2018] GET /src/frame/static/image/code.png => generated 4599 bytes in 4 msecs (HTTP/1.1 404) 3 headers in 102 bytes (1 switches on core 0)
[pid: 3192|app: 0|req: 6/18] 218.247.217.98 () {38 vars in 675 bytes} [Mon Dec  3 11:31:30 2018] GET /index => generated 7174 bytes in 1 msecs (HTTP/1.1 200) 3 headers in 110 bytes (1 switches on core 0)
Not Found: /src/frame/layui/css/layui.css
[pid: 3195|app: 0|req: 3/19] 218.247.217.98 () {36 vars in 637 bytes} [Mon Dec  3 11:31:30 2018] GET /src/frame/layui/css/layui.css => generated 4593 bytes in 4 msecs (HTTP/1.1 404) 3 headers in 102 bytes (1 switches on core 0)
Not Found: /src/frame/static/css/style.css
Not Found: /src/frame/static/js/vip_comm.js
[pid: 3193|app: 0|req: 5/21] 218.247.217.98 () {36 vars in 626 bytes} [Mon Dec  3 11:31:30 2018] GET /src/frame/static/js/vip_comm.js => generated 4599 bytes in 9 msecs (HTTP/1.1 404) 3 headers in 102 bytes (1 switches on core 0)
[pid: 3196|app: 0|req: 4/21] 218.247.217.98 () {36 vars in 639 bytes} [Mon Dec  3 11:31:30 2018] GET /src/frame/static/css/style.css => generated 4596 bytes in 12 msecs (HTTP/1.1 404) 3 headers in 102 bytes (1 switches on core 0)
[pid: 3193|app: 0|req: 6/22] 218.247.217.98 () {38 vars in 715 bytes} [Mon Dec  3 11:31:31 2018] GET /demo/welcome.html => generated 24253 bytes in 1 msecs (HTTP/1.1 200) 3 headers in 111 bytes (1 switches on core 0)
Not Found: /src/frame/static/image/zfb.png
[pid: 3192|app: 0|req: 7/23] 218.247.217.98 () {36 vars in 660 bytes} [Mon Dec  3 11:31:30 2018] GET /src/frame/static/image/zfb.png => generated 4596 bytes in 9 msecs (HTTP/1.1 404) 3 headers in 102 bytes (1 switches on core 0)
Not Found: /src/frame/layui/layui.js
[pid: 3194|app: 0|req: 4/24] 218.247.217.98 () {36 vars in 612 bytes} [Mon Dec  3 11:31:30 2018] GET /src/frame/layui/layui.js => generated 4578 bytes in 16 msecs (HTTP/1.1 404) 3 headers in 102 bytes (1 switches on core 0)
Not Found: /src/frame/static/image/code.png
[pid: 3195|app: 0|req: 4/25] 218.247.217.98 () {36 vars in 662 bytes} [Mon Dec  3 11:31:30 2018] GET /src/frame/static/image/code.png => generated 4599 bytes in 7 msecs (HTTP/1.1 404) 3 headers in 102 bytes (1 switches on core 0)
Not Found: /src/frame/static/image/wx.png
[pid: 3196|app: 0|req: 5/26] 218.247.217.98 () {36 vars in 658 bytes} [Mon Dec  3 11:31:31 2018] GET /src/frame/static/image/wx.png => generated 4593 bytes in 3 msecs (HTTP/1.1 404) 3 headers in 102 bytes (1 switches on core 0)
Not Found: /src/frame/static/js/vip_comm.js
[pid: 3193|app: 0|req: 7/27] 218.247.217.98 () {36 vars in 626 bytes} [Mon Dec  3 11:31:31 2018] GET /src/frame/static/js/vip_comm.js => generated 4599 bytes in 3 msecs (HTTP/1.1 404) 3 headers in 102 bytes (1 switches on core 0)
[pid: 3195|app: 0|req: 5/28] 218.247.217.98 () {36 vars in 598 bytes} [Mon Dec  3 11:31:31 2018] GET /js/index.js => generated 7174 bytes in 1 msecs (HTTP/1.1 200) 3 headers in 110 bytes (1 switches on core 0)
Not Found: /src/frame/layui/css/layui.css
[pid: 3192|app: 0|req: 8/29] 218.247.217.98 () {36 vars in 649 bytes} [Mon Dec  3 11:31:31 2018] GET /src/frame/layui/css/layui.css => generated 4593 bytes in 6 msecs (HTTP/1.1 404) 3 headers in 102 bytes (1 switches on core 0)
Not Found: /src/frame/static/css/style.css
[pid: 3194|app: 0|req: 5/30] 218.247.217.98 () {36 vars in 651 bytes} [Mon Dec  3 11:31:31 2018] GET /src/frame/static/css/style.css => generated 4596 bytes in 5 msecs (HTTP/1.1 404) 3 headers in 102 bytes (1 switches on core 0)
Not Found: /src/frame/echarts/echarts.min.js
[pid: 3193|app: 0|req: 8/31] 218.247.217.98 () {36 vars in 640 bytes} [Mon Dec  3 11:31:31 2018] GET /src/frame/echarts/echarts.min.js => generated 4602 bytes in 5 msecs (HTTP/1.1 404) 3 headers in 102 bytes (1 switches on core 0)
Not Found: /src/layui/layui.js
[pid: 3196|app: 0|req: 6/32] 218.247.217.98 () {36 vars in 612 bytes} [Mon Dec  3 11:31:31 2018] GET /src/layui/layui.js => generated 4560 bytes in 5 msecs (HTTP/1.1 404) 3 headers in 102 bytes (1 switches on core 0)
Not Found: /src/frame/echarts/echarts.min.js
[pid: 3195|app: 0|req: 6/33] 218.247.217.98 () {36 vars in 640 bytes} [Mon Dec  3 11:31:31 2018] GET /src/frame/echarts/echarts.min.js => generated 4602 bytes in 4 msecs (HTTP/1.1 404) 3 headers in 102 bytes (1 switches on core 0)
[pid: 3192|app: 0|req: 9/34] 218.247.217.98 () {38 vars in 675 bytes} [Mon Dec  3 11:31:33 2018] GET /index => generated 7174 bytes in 1 msecs (HTTP/1.1 200) 3 headers in 110 bytes (1 switches on core 0)
Not Found: /src/frame/layui/css/layui.css
[pid: 3194|app: 0|req: 6/35] 218.247.217.98 () {36 vars in 637 bytes} [Mon Dec  3 11:31:33 2018] GET /src/frame/layui/css/layui.css => generated 4593 bytes in 4 msecs (HTTP/1.1 404) 3 headers in 102 bytes (1 switches on core 0)
Not Found: /src/frame/static/css/style.css
[pid: 3193|app: 0|req: 9/36] 218.247.217.98 () {36 vars in 639 bytes} [Mon Dec  3 11:31:33 2018] GET /src/frame/static/css/style.css => generated 4596 bytes in 6 msecs (HTTP/1.1 404) 3 headers in 102 bytes (1 switches on core 0)
Not Found: /src/frame/static/image/zfb.png
[pid: 3194|app: 0|req: 7/37] 218.247.217.98 () {36 vars in 660 bytes} [Mon Dec  3 11:31:33 2018] GET /src/frame/static/image/zfb.png => generated 4596 bytes in 5 msecs (HTTP/1.1 404) 3 headers in 102 bytes (1 switches on core 0)
Not Found: /src/frame/layui/layui.js
[pid: 3196|app: 0|req: 7/38] 218.247.217.98 () {36 vars in 612 bytes} [Mon Dec  3 11:31:33 2018] GET /src/frame/layui/layui.js => generated 4578 bytes in 11 msecs (HTTP/1.1 404) 3 headers in 102 bytes (1 switches on core 0)
[pid: 3193|app: 0|req: 10/39] 218.247.217.98 () {38 vars in 715 bytes} [Mon Dec  3 11:31:33 2018] GET /demo/welcome.html => generated 24253 bytes in 1 msecs (HTTP/1.1 200) 3 headers in 111 bytes (1 switches on core 0)
Not Found: /src/frame/static/image/code.png
[pid: 3192|app: 0|req: 10/40] 218.247.217.98 () {36 vars in 662 bytes} [Mon Dec  3 11:31:33 2018] GET /src/frame/static/image/code.png => generated 4599 bytes in 7 msecs (HTTP/1.1 404) 3 headers in 102 bytes (1 switches on core 0)
Not Found: /src/frame/static/js/vip_comm.js
[pid: 3195|app: 0|req: 7/41] 218.247.217.98 () {36 vars in 626 bytes} [Mon Dec  3 11:31:33 2018] GET /src/frame/static/js/vip_comm.js => generated 4599 bytes in 5 msecs (HTTP/1.1 404) 3 headers in 102 bytes (1 switches on core 0)
Not Found: /src/frame/static/image/wx.png
[pid: 3194|app: 0|req: 8/42] 218.247.217.98 () {36 vars in 658 bytes} [Mon Dec  3 11:31:33 2018] GET /src/frame/static/image/wx.png => generated 4593 bytes in 3 msecs (HTTP/1.1 404) 3 headers in 102 bytes (1 switches on core 0)
Not Found: /src/frame/layui/css/layui.css
[pid: 3196|app: 0|req: 8/43] 218.247.217.98 () {36 vars in 649 bytes} [Mon Dec  3 11:31:33 2018] GET /src/frame/layui/css/layui.css => generated 4593 bytes in 5 msecs (HTTP/1.1 404) 3 headers in 102 bytes (1 switches on core 0)
Not Found: /src/frame/static/css/style.css
[pid: 3193|app: 0|req: 11/44] 218.247.217.98 () {36 vars in 651 bytes} [Mon Dec  3 11:31:33 2018] GET /src/frame/static/css/style.css => generated 4596 bytes in 5 msecs (HTTP/1.1 404) 3 headers in 102 bytes (1 switches on core 0)
[pid: 3195|app: 0|req: 8/45] 218.247.217.98 () {36 vars in 598 bytes} [Mon Dec  3 11:31:33 2018] GET /js/index.js => generated 7174 bytes in 1 msecs (HTTP/1.1 200) 3 headers in 110 bytes (1 switches on core 0)
Not Found: /src/frame/echarts/echarts.min.js
[pid: 3192|app: 0|req: 11/46] 218.247.217.98 () {36 vars in 638 bytes} [Mon Dec  3 11:31:33 2018] GET /src/frame/echarts/echarts.min.js => generated 4602 bytes in 5 msecs (HTTP/1.1 404) 3 headers in 102 bytes (2 switches on core 0)
Not Found: /src/layui/layui.js
[pid: 3194|app: 0|req: 9/47] 218.247.217.98 () {36 vars in 610 bytes} [Mon Dec  3 11:31:33 2018] GET /src/layui/layui.js => generated 4560 bytes in 5 msecs (HTTP/1.1 404) 3 headers in 102 bytes (1 switches on core 0)
Not Found: /src/frame/echarts/echarts.min.js
[pid: 3196|app: 0|req: 9/48] 218.247.217.98 () {36 vars in 638 bytes} [Mon Dec  3 11:31:33 2018] GET /src/frame/echarts/echarts.min.js => generated 4602 bytes in 3 msecs (HTTP/1.1 404) 3 headers in 102 bytes (1 switches on core 0)
[pid: 3193|app: 0|req: 12/49] 218.247.217.98 () {38 vars in 674 bytes} [Mon Dec  3 11:31:35 2018] GET /index => generated 7174 bytes in 1 msecs (HTTP/1.1 200) 3 headers in 110 bytes (1 switches on core 0)
Not Found: /src/frame/layui/css/layui.css
[pid: 3195|app: 0|req: 9/50] 218.247.217.98 () {36 vars in 636 bytes} [Mon Dec  3 11:31:35 2018] GET /src/frame/layui/css/layui.css => generated 4593 bytes in 4 msecs (HTTP/1.1 404) 3 headers in 102 bytes (1 switches on core 0)
Not Found: /src/frame/layui/layui.js
[pid: 3194|app: 0|req: 10/51] 218.247.217.98 () {36 vars in 611 bytes} [Mon Dec  3 11:31:35 2018] GET /src/frame/layui/layui.js => generated 4578 bytes in 6 msecs (HTTP/1.1 404) 3 headers in 102 bytes (1 switches on core 0)
Not Found: /src/frame/static/css/style.css
[pid: 3192|app: 0|req: 12/52] 218.247.217.98 () {36 vars in 638 bytes} [Mon Dec  3 11:31:35 2018] GET /src/frame/static/css/style.css => generated 4596 bytes in 12 msecs (HTTP/1.1 404) 3 headers in 102 bytes (1 switches on core 0)
Not Found: /src/frame/static/image/zfb.png
[pid: 3196|app: 0|req: 10/53] 218.247.217.98 () {36 vars in 659 bytes} [Mon Dec  3 11:31:35 2018] GET /src/frame/static/image/zfb.png => generated 4596 bytes in 7 msecs (HTTP/1.1 404) 3 headers in 102 bytes (1 switches on core 0)
Not Found: /src/frame/static/image/code.png
[pid: 3193|app: 0|req: 13/54] 218.247.217.98 () {36 vars in 661 bytes} [Mon Dec  3 11:31:35 2018] GET /src/frame/static/image/code.png => generated 4599 bytes in 6 msecs (HTTP/1.1 404) 3 headers in 102 bytes (1 switches on core 0)
Not Found: /src/frame/static/js/vip_comm.js
[pid: 3195|app: 0|req: 10/55] 218.247.217.98 () {36 vars in 625 bytes} [Mon Dec  3 11:31:35 2018] GET /src/frame/static/js/vip_comm.js => generated 4599 bytes in 5 msecs (HTTP/1.1 404) 3 headers in 102 bytes (1 switches on core 0)
[pid: 3194|app: 0|req: 11/56] 218.247.217.98 () {38 vars in 714 bytes} [Mon Dec  3 11:31:35 2018] GET /demo/welcome.html => generated 24253 bytes in 10 msecs (HTTP/1.1 200) 3 headers in 111 bytes (1 switches on core 0)
Not Found: /src/frame/static/image/wx.png
[pid: 3192|app: 0|req: 13/57] 218.247.217.98 () {36 vars in 657 bytes} [Mon Dec  3 11:31:35 2018] GET /src/frame/static/image/wx.png => generated 4593 bytes in 5 msecs (HTTP/1.1 404) 3 headers in 102 bytes (1 switches on core 0)
Not Found: /src/frame/layui/css/layui.css
[pid: 3196|app: 0|req: 11/58] 218.247.217.98 () {36 vars in 648 bytes} [Mon Dec  3 11:31:35 2018] GET /src/frame/layui/css/layui.css => generated 4593 bytes in 5 msecs (HTTP/1.1 404) 3 headers in 102 bytes (1 switches on core 0)
[pid: 3194|app: 0|req: 12/59] 218.247.217.98 () {36 vars in 597 bytes} [Mon Dec  3 11:31:35 2018] GET /js/index.js => generated 7174 bytes in 1 msecs (HTTP/1.1 200) 3 headers in 110 bytes (1 switches on core 0)
Not Found: /src/frame/static/css/style.css
[pid: 3193|app: 0|req: 14/60] 218.247.217.98 () {36 vars in 650 bytes} [Mon Dec  3 11:31:35 2018] GET /src/frame/static/css/style.css => generated 4596 bytes in 7 msecs (HTTP/1.1 404) 3 headers in 102 bytes (1 switches on core 0)
Not Found: /src/layui/layui.js
[pid: 3195|app: 0|req: 11/61] 218.247.217.98 () {36 vars in 611 bytes} [Mon Dec  3 11:31:35 2018] GET /src/layui/layui.js => generated 4560 bytes in 6 msecs (HTTP/1.1 404) 3 headers in 102 bytes (1 switches on core 0)
Not Found: /src/frame/echarts/echarts.min.js
[pid: 3192|app: 0|req: 14/62] 218.247.217.98 () {36 vars in 639 bytes} [Mon Dec  3 11:31:35 2018] GET /src/frame/echarts/echarts.min.js => generated 4602 bytes in 4 msecs (HTTP/1.1 404) 3 headers in 102 bytes (1 switches on core 0)
[pid: 3196|app: 0|req: 12/63] 218.247.217.98 () {38 vars in 675 bytes} [Mon Dec  3 11:32:17 2018] GET /index => generated 7174 bytes in 8 msecs (HTTP/1.1 200) 3 headers in 110 bytes (1 switches on core 0)
Not Found: /src/frame/layui/css/layui.css
[pid: 3194|app: 0|req: 13/64] 218.247.217.98 () {36 vars in 637 bytes} [Mon Dec  3 11:32:17 2018] GET /src/frame/layui/css/layui.css => generated 4593 bytes in 4 msecs (HTTP/1.1 404) 3 headers in 102 bytes (1 switches on core 0)
Not Found: /src/frame/static/css/style.css
[pid: 3195|app: 0|req: 12/65] 218.247.217.98 () {36 vars in 639 bytes} [Mon Dec  3 11:32:17 2018] GET /src/frame/static/css/style.css => generated 4596 bytes in 6 msecs (HTTP/1.1 404) 3 headers in 102 bytes (1 switches on core 0)
Not Found: /src/frame/layui/layui.js
Not Found: /src/frame/static/js/vip_comm.js
Not Found: /src/frame/static/image/zfb.png
[pid: 3194|app: 0|req: 14/67] 218.247.217.98 () {36 vars in 660 bytes} [Mon Dec  3 11:32:17 2018] GET /src/frame/static/image/zfb.png => generated 4596 bytes in 5 msecs (HTTP/1.1 404) 3 headers in 102 bytes (1 switches on core 0)
[pid: 3192|app: 0|req: 15/67] 218.247.217.98 () {36 vars in 626 bytes} [Mon Dec  3 11:32:17 2018] GET /src/frame/static/js/vip_comm.js => generated 4599 bytes in 7 msecs (HTTP/1.1 404) 3 headers in 102 bytes (1 switches on core 0)
[pid: 3193|app: 0|req: 15/68] 218.247.217.98 () {36 vars in 612 bytes} [Mon Dec  3 11:32:17 2018] GET /src/frame/layui/layui.js => generated 4578 bytes in 13 msecs (HTTP/1.1 404) 3 headers in 102 bytes (1 switches on core 0)
[pid: 3195|app: 0|req: 13/69] 218.247.217.98 () {38 vars in 715 bytes} [Mon Dec  3 11:32:17 2018] GET /demo/welcome.html => generated 24253 bytes in 1 msecs (HTTP/1.1 200) 3 headers in 111 bytes (1 switches on core 0)
Not Found: /src/frame/static/image/code.png
[pid: 3196|app: 0|req: 13/70] 218.247.217.98 () {36 vars in 662 bytes} [Mon Dec  3 11:32:17 2018] GET /src/frame/static/image/code.png => generated 4599 bytes in 6 msecs (HTTP/1.1 404) 3 headers in 102 bytes (1 switches on core 0)
Not Found: /src/frame/static/image/wx.png
[pid: 3194|app: 0|req: 15/71] 218.247.217.98 () {36 vars in 658 bytes} [Mon Dec  3 11:32:17 2018] GET /src/frame/static/image/wx.png => generated 4593 bytes in 4 msecs (HTTP/1.1 404) 3 headers in 102 bytes (1 switches on core 0)
Not Found: /src/frame/static/css/style.css
Not Found: /src/layui/layui.js
[pid: 3195|app: 0|req: 14/72] 218.247.217.98 () {36 vars in 651 bytes} [Mon Dec  3 11:32:17 2018] GET /src/frame/static/css/style.css => generated 4596 bytes in 6 msecs (HTTP/1.1 404) 3 headers in 102 bytes (1 switches on core 0)
[pid: 3196|app: 0|req: 14/73] 218.247.217.98 () {36 vars in 598 bytes} [Mon Dec  3 11:32:17 2018] GET /js/index.js => generated 7174 bytes in 1 msecs (HTTP/1.1 200) 3 headers in 110 bytes (1 switches on core 0)
Not Found: /src/frame/echarts/echarts.min.js
[pid: 3193|app: 0|req: 16/74] 218.247.217.98 () {36 vars in 612 bytes} [Mon Dec  3 11:32:17 2018] GET /src/layui/layui.js => generated 4560 bytes in 12 msecs (HTTP/1.1 404) 3 headers in 102 bytes (1 switches on core 0)
[pid: 3194|app: 0|req: 16/75] 218.247.217.98 () {36 vars in 640 bytes} [Mon Dec  3 11:32:17 2018] GET /src/frame/echarts/echarts.min.js => generated 4602 bytes in 6 msecs (HTTP/1.1 404) 3 headers in 102 bytes (1 switches on core 0)
Not Found: /src/frame/layui/css/layui.css
[pid: 3192|app: 0|req: 16/76] 218.247.217.98 () {36 vars in 649 bytes} [Mon Dec  3 11:32:17 2018] GET /src/frame/layui/css/layui.css => generated 4593 bytes in 13 msecs (HTTP/1.1 404) 3 headers in 102 bytes (1 switches on core 0)
Not Found: /src/frame/echarts/echarts.min.js
[pid: 3195|app: 0|req: 15/77] 218.247.217.98 () {36 vars in 640 bytes} [Mon Dec  3 11:32:17 2018] GET /src/frame/echarts/echarts.min.js => generated 4602 bytes in 4 msecs (HTTP/1.1 404) 3 headers in 102 bytes (1 switches on core 0)
[pid: 3196|app: 0|req: 15/78] 218.247.217.98 () {38 vars in 675 bytes} [Mon Dec  3 11:32:18 2018] GET /index => generated 7174 bytes in 1 msecs (HTTP/1.1 200) 3 headers in 110 bytes (1 switches on core 0)
Not Found: /src/frame/layui/css/layui.css
[pid: 3193|app: 0|req: 17/79] 218.247.217.98 () {36 vars in 637 bytes} [Mon Dec  3 11:32:18 2018] GET /src/frame/layui/css/layui.css => generated 4593 bytes in 7 msecs (HTTP/1.1 404) 3 headers in 102 bytes (1 switches on core 0)
Not Found: /src/frame/static/css/style.css
[pid: 3194|app: 0|req: 17/80] 218.247.217.98 () {36 vars in 639 bytes} [Mon Dec  3 11:32:18 2018] GET /src/frame/static/css/style.css => generated 4596 bytes in 4 msecs (HTTP/1.1 404) 3 headers in 102 bytes (1 switches on core 0)
[pid: 3193|app: 0|req: 18/81] 218.247.217.98 () {38 vars in 715 bytes} [Mon Dec  3 11:32:18 2018] GET /demo/welcome.html => generated 24253 bytes in 1 msecs (HTTP/1.1 200) 3 headers in 111 bytes (1 switches on core 0)
Not Found: /src/frame/static/image/code.png
[pid: 3195|app: 0|req: 16/82] 218.247.217.98 () {36 vars in 662 bytes} [Mon Dec  3 11:32:18 2018] GET /src/frame/static/image/code.png => generated 4599 bytes in 6 msecs (HTTP/1.1 404) 3 headers in 102 bytes (1 switches on core 0)
Not Found: /src/frame/static/js/vip_comm.js
[pid: 3196|app: 0|req: 16/83] 218.247.217.98 () {36 vars in 626 bytes} [Mon Dec  3 11:32:18 2018] GET /src/frame/static/js/vip_comm.js => generated 4599 bytes in 8 msecs (HTTP/1.1 404) 3 headers in 102 bytes (1 switches on core 0)
Not Found: /src/frame/layui/layui.js
[pid: 3192|app: 0|req: 17/84] 218.247.217.98 () {36 vars in 612 bytes} [Mon Dec  3 11:32:18 2018] GET /src/frame/layui/layui.js => generated 4578 bytes in 11 msecs (HTTP/1.1 404) 3 headers in 102 bytes (1 switches on core 0)
Not Found: /src/frame/static/image/zfb.png
[pid: 3194|app: 0|req: 18/85] 218.247.217.98 () {36 vars in 660 bytes} [Mon Dec  3 11:32:18 2018] GET /src/frame/static/image/zfb.png => generated 4596 bytes in 4 msecs (HTTP/1.1 404) 3 headers in 102 bytes (1 switches on core 0)
Not Found: /src/frame/static/image/wx.png
[pid: 3193|app: 0|req: 19/86] 218.247.217.98 () {36 vars in 658 bytes} [Mon Dec  3 11:32:18 2018] GET /src/frame/static/image/wx.png => generated 4593 bytes in 4 msecs (HTTP/1.1 404) 3 headers in 102 bytes (1 switches on core 0)
Not Found: /src/frame/static/js/vip_comm.js
[pid: 3195|app: 0|req: 17/87] 218.247.217.98 () {36 vars in 626 bytes} [Mon Dec  3 11:32:18 2018] GET /src/frame/static/js/vip_comm.js => generated 4599 bytes in 3 msecs (HTTP/1.1 404) 3 headers in 102 bytes (1 switches on core 0)
Not Found: /src/frame/layui/css/layui.css
[pid: 3196|app: 0|req: 17/88] 218.247.217.98 () {36 vars in 649 bytes} [Mon Dec  3 11:32:18 2018] GET /src/frame/layui/css/layui.css => generated 4593 bytes in 3 msecs (HTTP/1.1 404) 3 headers in 102 bytes (1 switches on core 0)
[pid: 3193|app: 0|req: 20/89] 218.247.217.98 () {36 vars in 598 bytes} [Mon Dec  3 11:32:18 2018] GET /js/index.js => generated 7174 bytes in 1 msecs (HTTP/1.1 200) 3 headers in 110 bytes (1 switches on core 0)
Not Found: /src/frame/static/css/style.css
[pid: 3194|app: 0|req: 19/90] 218.247.217.98 () {36 vars in 651 bytes} [Mon Dec  3 11:32:18 2018] GET /src/frame/static/css/style.css => generated 4596 bytes in 5 msecs (HTTP/1.1 404) 3 headers in 102 bytes (1 switches on core 0)
Not Found: /src/frame/echarts/echarts.min.js
[pid: 3195|app: 0|req: 18/91] 218.247.217.98 () {36 vars in 640 bytes} [Mon Dec  3 11:32:18 2018] GET /src/frame/echarts/echarts.min.js => generated 4602 bytes in 6 msecs (HTTP/1.1 404) 3 headers in 102 bytes (1 switches on core 0)
Not Found: /src/layui/layui.js
[pid: 3192|app: 0|req: 18/92] 218.247.217.98 () {36 vars in 612 bytes} [Mon Dec  3 11:32:18 2018] GET /src/layui/layui.js => generated 4560 bytes in 9 msecs (HTTP/1.1 404) 3 headers in 102 bytes (1 switches on core 0)
Not Found: /src/frame/echarts/echarts.min.js
[pid: 3196|app: 0|req: 18/93] 218.247.217.98 () {36 vars in 640 bytes} [Mon Dec  3 11:32:18 2018] GET /src/frame/echarts/echarts.min.js => generated 4602 bytes in 3 msecs (HTTP/1.1 404) 3 headers in 102 bytes (1 switches on core 0)
[pid: 3193|app: 0|req: 21/94] 218.247.217.98 () {38 vars in 675 bytes} [Mon Dec  3 11:32:19 2018] GET /index => generated 7174 bytes in 1 msecs (HTTP/1.1 200) 3 headers in 110 bytes (1 switches on core 0)
Not Found: /src/frame/layui/css/layui.css
[pid: 3194|app: 0|req: 20/95] 218.247.217.98 () {36 vars in 637 bytes} [Mon Dec  3 11:32:19 2018] GET /src/frame/layui/css/layui.css => generated 4593 bytes in 4 msecs (HTTP/1.1 404) 3 headers in 102 bytes (1 switches on core 0)
Not Found: /src/frame/static/css/style.css
[pid: 3195|app: 0|req: 19/96] 218.247.217.98 () {36 vars in 639 bytes} [Mon Dec  3 11:32:19 2018] GET /src/frame/static/css/style.css => generated 4596 bytes in 5 msecs (HTTP/1.1 404) 3 headers in 102 bytes (1 switches on core 0)
[pid: 3194|app: 0|req: 21/97] 218.247.217.98 () {38 vars in 715 bytes} [Mon Dec  3 11:32:19 2018] GET /demo/welcome.html => generated 24253 bytes in 1 msecs (HTTP/1.1 200) 3 headers in 111 bytes (1 switches on core 0)
Not Found: /src/frame/static/image/code.png
[pid: 3193|app: 0|req: 22/98] 218.247.217.98 () {36 vars in 662 bytes} [Mon Dec  3 11:32:19 2018] GET /src/frame/static/image/code.png => generated 4599 bytes in 7 msecs (HTTP/1.1 404) 3 headers in 102 bytes (1 switches on core 0)
Not Found: /src/frame/static/js/vip_comm.js
[pid: 3196|app: 0|req: 19/99] 218.247.217.98 () {36 vars in 626 bytes} [Mon Dec  3 11:32:19 2018] GET /src/frame/static/js/vip_comm.js => generated 4599 bytes in 7 msecs (HTTP/1.1 404) 3 headers in 102 bytes (1 switches on core 0)
Not Found: /src/frame/layui/layui.js
[pid: 3192|app: 0|req: 19/100] 218.247.217.98 () {36 vars in 612 bytes} [Mon Dec  3 11:32:19 2018] GET /src/frame/layui/layui.js => generated 4578 bytes in 14 msecs (HTTP/1.1 404) 3 headers in 102 bytes (1 switches on core 0)
Not Found: /src/frame/static/image/zfb.png
[pid: 3195|app: 0|req: 20/101] 218.247.217.98 () {36 vars in 660 bytes} [Mon Dec  3 11:32:19 2018] GET /src/frame/static/image/zfb.png => generated 4596 bytes in 5 msecs (HTTP/1.1 404) 3 headers in 102 bytes (1 switches on core 0)
Not Found: /src/frame/static/image/wx.png
[pid: 3194|app: 0|req: 22/102] 218.247.217.98 () {36 vars in 658 bytes} [Mon Dec  3 11:32:19 2018] GET /src/frame/static/image/wx.png => generated 4593 bytes in 3 msecs (HTTP/1.1 404) 3 headers in 102 bytes (1 switches on core 0)
Not Found: /src/frame/static/js/vip_comm.js
[pid: 3193|app: 0|req: 23/103] 218.247.217.98 () {36 vars in 626 bytes} [Mon Dec  3 11:32:19 2018] GET /src/frame/static/js/vip_comm.js => generated 4599 bytes in 3 msecs (HTTP/1.1 404) 3 headers in 102 bytes (1 switches on core 0)
Not Found: /src/frame/layui/css/layui.css
[pid: 3196|app: 0|req: 20/104] 218.247.217.98 () {36 vars in 649 bytes} [Mon Dec  3 11:32:19 2018] GET /src/frame/layui/css/layui.css => generated 4593 bytes in 4 msecs (HTTP/1.1 404) 3 headers in 102 bytes (1 switches on core 0)
Not Found: /src/frame/static/css/style.css
[pid: 3192|app: 0|req: 20/105] 218.247.217.98 () {36 vars in 651 bytes} [Mon Dec  3 11:32:19 2018] GET /src/frame/static/css/style.css => generated 4596 bytes in 4 msecs (HTTP/1.1 404) 3 headers in 102 bytes (1 switches on core 0)
Not Found: /src/layui/layui.js
[pid: 3195|app: 0|req: 21/106] 218.247.217.98 () {36 vars in 612 bytes} [Mon Dec  3 11:32:19 2018] GET /src/layui/layui.js => generated 4560 bytes in 5 msecs (HTTP/1.1 404) 3 headers in 102 bytes (1 switches on core 0)
[pid: 3193|app: 0|req: 24/107] 218.247.217.98 () {36 vars in 598 bytes} [Mon Dec  3 11:32:19 2018] GET /js/index.js => generated 7174 bytes in 1 msecs (HTTP/1.1 200) 3 headers in 110 bytes (1 switches on core 0)
Not Found: /src/frame/echarts/echarts.min.js
[pid: 3194|app: 0|req: 23/108] 218.247.217.98 () {36 vars in 640 bytes} [Mon Dec  3 11:32:19 2018] GET /src/frame/echarts/echarts.min.js => generated 4602 bytes in 4 msecs (HTTP/1.1 404) 3 headers in 102 bytes (1 switches on core 0)
Not Found: /src/layui/layui.js
[pid: 3196|app: 0|req: 21/109] 218.247.217.98 () {36 vars in 612 bytes} [Mon Dec  3 11:32:19 2018] GET /src/layui/layui.js => generated 4560 bytes in 3 msecs (HTTP/1.1 404) 3 headers in 102 bytes (1 switches on core 0)
Not Found: /src/frame/echarts/echarts.min.js
[pid: 3192|app: 0|req: 21/110] 218.247.217.98 () {36 vars in 640 bytes} [Mon Dec  3 11:32:19 2018] GET /src/frame/echarts/echarts.min.js => generated 4602 bytes in 3 msecs (HTTP/1.1 404) 3 headers in 102 bytes (1 switches on core 0)
[pid: 3195|app: 0|req: 22/111] 218.247.217.98 () {38 vars in 675 bytes} [Mon Dec  3 11:32:27 2018] GET /index => generated 7174 bytes in 1 msecs (HTTP/1.1 200) 3 headers in 110 bytes (1 switches on core 0)
Not Found: /src/frame/layui/css/layui.css
[pid: 3193|app: 0|req: 25/112] 218.247.217.98 () {36 vars in 637 bytes} [Mon Dec  3 11:32:27 2018] GET /src/frame/layui/css/layui.css => generated 4593 bytes in 4 msecs (HTTP/1.1 404) 3 headers in 102 bytes (1 switches on core 0)
Not Found: /src/frame/static/css/style.css
[pid: 3194|app: 0|req: 24/113] 218.247.217.98 () {36 vars in 639 bytes} [Mon Dec  3 11:32:27 2018] GET /src/frame/static/css/style.css => generated 4596 bytes in 6 msecs (HTTP/1.1 404) 3 headers in 102 bytes (1 switches on core 0)
Not Found: /src/frame/layui/layui.js
[pid: 3196|app: 0|req: 22/114] 218.247.217.98 () {36 vars in 612 bytes} [Mon Dec  3 11:32:27 2018] GET /src/frame/layui/layui.js => generated 4578 bytes in 6 msecs (HTTP/1.1 404) 3 headers in 102 bytes (1 switches on core 0)
[pid: 3193|app: 0|req: 26/115] 218.247.217.98 () {38 vars in 715 bytes} [Mon Dec  3 11:32:27 2018] GET /demo/welcome.html => generated 24253 bytes in 1 msecs (HTTP/1.1 200) 3 headers in 111 bytes (1 switches on core 0)
Not Found: /src/frame/static/image/code.png
[pid: 3195|app: 0|req: 23/116] 218.247.217.98 () {36 vars in 662 bytes} [Mon Dec  3 11:32:27 2018] GET /src/frame/static/image/code.png => generated 4599 bytes in 6 msecs (HTTP/1.1 404) 3 headers in 102 bytes (1 switches on core 0)
Not Found: /src/frame/static/js/vip_comm.js
[pid: 3192|app: 0|req: 22/117] 218.247.217.98 () {36 vars in 626 bytes} [Mon Dec  3 11:32:27 2018] GET /src/frame/static/js/vip_comm.js => generated 4599 bytes in 5 msecs (HTTP/1.1 404) 3 headers in 102 bytes (1 switches on core 0)
Not Found: /src/frame/static/image/zfb.png
[pid: 3194|app: 0|req: 25/118] 218.247.217.98 () {36 vars in 660 bytes} [Mon Dec  3 11:32:27 2018] GET /src/frame/static/image/zfb.png => generated 4596 bytes in 3 msecs (HTTP/1.1 404) 3 headers in 102 bytes (1 switches on core 0)
Not Found: /src/frame/static/image/wx.png
[pid: 3196|app: 0|req: 23/119] 218.247.217.98 () {36 vars in 658 bytes} [Mon Dec  3 11:32:27 2018] GET /src/frame/static/image/wx.png => generated 4593 bytes in 3 msecs (HTTP/1.1 404) 3 headers in 102 bytes (1 switches on core 0)
Not Found: /src/frame/layui/css/layui.css
[pid: 3193|app: 0|req: 27/120] 218.247.217.98 () {36 vars in 649 bytes} [Mon Dec  3 11:32:27 2018] GET /src/frame/layui/css/layui.css => generated 4593 bytes in 3 msecs (HTTP/1.1 404) 3 headers in 102 bytes (1 switches on core 0)
Not Found: /src/frame/static/css/style.css
[pid: 3194|app: 0|req: 26/121] 218.247.217.98 () {36 vars in 598 bytes} [Mon Dec  3 11:32:27 2018] GET /js/index.js => generated 7174 bytes in 1 msecs (HTTP/1.1 200) 3 headers in 110 bytes (1 switches on core 0)
[pid: 3195|app: 0|req: 24/122] 218.247.217.98 () {36 vars in 651 bytes} [Mon Dec  3 11:32:27 2018] GET /src/frame/static/css/style.css => generated 4596 bytes in 4 msecs (HTTP/1.1 404) 3 headers in 102 bytes (1 switches on core 0)
Not Found: /src/layui/layui.js
[pid: 3192|app: 0|req: 23/123] 218.247.217.98 () {36 vars in 612 bytes} [Mon Dec  3 11:32:27 2018] GET /src/layui/layui.js => generated 4560 bytes in 5 msecs (HTTP/1.1 404) 3 headers in 102 bytes (1 switches on core 0)
Not Found: /src/frame/echarts/echarts.min.js
[pid: 3196|app: 0|req: 24/124] 218.247.217.98 () {36 vars in 640 bytes} [Mon Dec  3 11:32:27 2018] GET /src/frame/echarts/echarts.min.js => generated 4602 bytes in 3 msecs (HTTP/1.1 404) 3 headers in 102 bytes (1 switches on core 0)
Not Found: /src/frame/echarts/echarts.min.js
[pid: 3193|app: 0|req: 28/125] 218.247.217.98 () {36 vars in 640 bytes} [Mon Dec  3 11:32:28 2018] GET /src/frame/echarts/echarts.min.js => generated 4602 bytes in 4 msecs (HTTP/1.1 404) 3 headers in 102 bytes (1 switches on core 0)
[pid: 3194|app: 0|req: 27/126] 218.247.217.98 () {38 vars in 675 bytes} [Mon Dec  3 11:32:28 2018] GET /index => generated 7174 bytes in 1 msecs (HTTP/1.1 200) 3 headers in 110 bytes (1 switches on core 0)
Not Found: /src/frame/layui/css/layui.css
[pid: 3195|app: 0|req: 25/127] 218.247.217.98 () {36 vars in 637 bytes} [Mon Dec  3 11:32:28 2018] GET /src/frame/layui/css/layui.css => generated 4593 bytes in 4 msecs (HTTP/1.1 404) 3 headers in 102 bytes (1 switches on core 0)
Not Found: /src/frame/static/css/style.css
[pid: 3192|app: 0|req: 24/128] 218.247.217.98 () {36 vars in 639 bytes} [Mon Dec  3 11:32:28 2018] GET /src/frame/static/css/style.css => generated 4596 bytes in 5 msecs (HTTP/1.1 404) 3 headers in 102 bytes (1 switches on core 0)
[pid: 3194|app: 0|req: 28/129] 218.247.217.98 () {38 vars in 715 bytes} [Mon Dec  3 11:32:28 2018] GET /demo/welcome.html => generated 24253 bytes in 1 msecs (HTTP/1.1 200) 3 headers in 111 bytes (1 switches on core 0)
Not Found: /src/frame/static/js/vip_comm.js
Not Found: /src/frame/layui/layui.js
[pid: 3196|app: 0|req: 25/130] 218.247.217.98 () {36 vars in 612 bytes} [Mon Dec  3 11:32:28 2018] GET /src/frame/layui/layui.js => generated 4578 bytes in 12 msecs (HTTP/1.1 404) 3 headers in 102 bytes (1 switches on core 0)
[pid: 3193|app: 0|req: 29/131] 218.247.217.98 () {36 vars in 626 bytes} [Mon Dec  3 11:32:28 2018] GET /src/frame/static/js/vip_comm.js => generated 4599 bytes in 8 msecs (HTTP/1.1 404) 3 headers in 102 bytes (1 switches on core 0)
Not Found: /src/frame/static/image/code.png
[pid: 3195|app: 0|req: 26/132] 218.247.217.98 () {36 vars in 662 bytes} [Mon Dec  3 11:32:28 2018] GET /src/frame/static/image/code.png => generated 4599 bytes in 7 msecs (HTTP/1.1 404) 3 headers in 102 bytes (1 switches on core 0)
Not Found: /src/frame/static/image/zfb.png
[pid: 3192|app: 0|req: 25/133] 218.247.217.98 () {36 vars in 660 bytes} [Mon Dec  3 11:32:28 2018] GET /src/frame/static/image/zfb.png => generated 4596 bytes in 5 msecs (HTTP/1.1 404) 3 headers in 102 bytes (1 switches on core 0)
Not Found: /src/frame/static/image/wx.png
[pid: 3194|app: 0|req: 29/134] 218.247.217.98 () {36 vars in 658 bytes} [Mon Dec  3 11:32:28 2018] GET /src/frame/static/image/wx.png => generated 4593 bytes in 3 msecs (HTTP/1.1 404) 3 headers in 102 bytes (1 switches on core 0)
Not Found: /src/frame/static/js/vip_comm.js
[pid: 3196|app: 0|req: 26/135] 218.247.217.98 () {36 vars in 626 bytes} [Mon Dec  3 11:32:28 2018] GET /src/frame/static/js/vip_comm.js => generated 4599 bytes in 3 msecs (HTTP/1.1 404) 3 headers in 102 bytes (1 switches on core 0)
Not Found: /src/layui/layui.js
Not Found: /src/frame/static/css/style.css
[pid: 3193|app: 0|req: 30/136] 218.247.217.98 () {36 vars in 651 bytes} [Mon Dec  3 11:32:28 2018] GET /src/frame/static/css/style.css => generated 4596 bytes in 9 msecs (HTTP/1.1 404) 3 headers in 102 bytes (1 switches on core 0)
[pid: 3196|app: 0|req: 27/137] 218.247.217.98 () {36 vars in 598 bytes} [Mon Dec  3 11:32:28 2018] GET /js/index.js => generated 7174 bytes in 1 msecs (HTTP/1.1 200) 3 headers in 110 bytes (1 switches on core 0)
Not Found: /src/frame/echarts/echarts.min.js
Not Found: /src/frame/layui/css/layui.css
[pid: 3194|app: 0|req: 30/138] 218.247.217.98 () {36 vars in 640 bytes} [Mon Dec  3 11:32:28 2018] GET /src/frame/echarts/echarts.min.js => generated 4602 bytes in 8 msecs (HTTP/1.1 404) 3 headers in 102 bytes (1 switches on core 0)
[pid: 3195|app: 0|req: 27/139] 218.247.217.98 () {36 vars in 649 bytes} [Mon Dec  3 11:32:28 2018] GET /src/frame/layui/css/layui.css => generated 4593 bytes in 11 msecs (HTTP/1.1 404) 3 headers in 102 bytes (1 switches on core 0)
[pid: 3192|app: 0|req: 26/140] 218.247.217.98 () {36 vars in 612 bytes} [Mon Dec  3 11:32:28 2018] GET /src/layui/layui.js => generated 4560 bytes in 9 msecs (HTTP/1.1 404) 3 headers in 102 bytes (1 switches on core 0)
Not Found: /src/frame/echarts/echarts.min.js
[pid: 3193|app: 0|req: 31/141] 218.247.217.98 () {36 vars in 640 bytes} [Mon Dec  3 11:32:29 2018] GET /src/frame/echarts/echarts.min.js => generated 4602 bytes in 3 msecs (HTTP/1.1 404) 3 headers in 102 bytes (1 switches on core 0)
Not Found: /
[pid: 3196|app: 0|req: 28/142] 218.247.217.98 () {36 vars in 634 bytes} [Mon Dec  3 11:32:31 2018] GET / => generated 4488 bytes in 4 msecs (HTTP/1.1 404) 3 headers in 102 bytes (1 switches on core 0)
Not Found: /favicon.ico
[pid: 3194|app: 0|req: 31/143] 218.247.217.98 () {36 vars in 617 bytes} [Mon Dec  3 11:32:32 2018] GET /favicon.ico => generated 4539 bytes in 4 msecs (HTTP/1.1 404) 3 headers in 102 bytes (1 switches on core 0)
Not Found: /src/frame/echarts/echarts.min.js
[pid: 3195|app: 0|req: 28/144] 218.247.217.98 () {36 vars in 640 bytes} [Mon Dec  3 11:32:34 2018] GET /src/frame/echarts/echarts.min.js => generated 4602 bytes in 4 msecs (HTTP/1.1 404) 3 headers in 102 bytes (1 switches on core 0)
[pid: 3192|app: 0|req: 27/145] 218.247.217.98 () {38 vars in 675 bytes} [Mon Dec  3 11:32:35 2018] GET /index => generated 7174 bytes in 1 msecs (HTTP/1.1 200) 3 headers in 110 bytes (1 switches on core 0)
Not Found: /src/frame/layui/css/layui.css
[pid: 3193|app: 0|req: 32/146] 218.247.217.98 () {36 vars in 637 bytes} [Mon Dec  3 11:32:35 2018] GET /src/frame/layui/css/layui.css => generated 4593 bytes in 4 msecs (HTTP/1.1 404) 3 headers in 102 bytes (1 switches on core 0)
Not Found: /src/frame/layui/layui.js
[pid: 3196|app: 0|req: 29/147] 218.247.217.98 () {36 vars in 612 bytes} [Mon Dec  3 11:32:35 2018] GET /src/frame/layui/layui.js => generated 4578 bytes in 6 msecs (HTTP/1.1 404) 3 headers in 102 bytes (1 switches on core 0)
[pid: 3196|app: 0|req: 30/148] 218.247.217.98 () {38 vars in 715 bytes} [Mon Dec  3 11:32:35 2018] GET /demo/welcome.html => generated 24253 bytes in 1 msecs (HTTP/1.1 200) 3 headers in 111 bytes (1 switches on core 0)
Not Found: /src/frame/static/js/vip_comm.js
[pid: 3195|app: 0|req: 29/149] 218.247.217.98 () {36 vars in 626 bytes} [Mon Dec  3 11:32:35 2018] GET /src/frame/static/js/vip_comm.js => generated 4599 bytes in 7 msecs (HTTP/1.1 404) 3 headers in 102 bytes (1 switches on core 0)
Not Found: /src/frame/static/image/zfb.png
[pid: 3193|app: 0|req: 33/150] 218.247.217.98 () {36 vars in 660 bytes} [Mon Dec  3 11:32:35 2018] GET /src/frame/static/image/zfb.png => generated 4596 bytes in 5 msecs (HTTP/1.1 404) 3 headers in 102 bytes (1 switches on core 0)
Not Found: /src/frame/static/image/code.png
[pid: 3192|app: 0|req: 28/151] 218.247.217.98 () {36 vars in 662 bytes} [Mon Dec  3 11:32:35 2018] GET /src/frame/static/image/code.png => generated 4599 bytes in 9 msecs (HTTP/1.1 404) 3 headers in 102 bytes (1 switches on core 0)
Not Found: /src/frame/static/css/style.css
[pid: 3194|app: 0|req: 32/152] 218.247.217.98 () {36 vars in 639 bytes} [Mon Dec  3 11:32:35 2018] GET /src/frame/static/css/style.css => generated 4596 bytes in 15 msecs (HTTP/1.1 404) 3 headers in 102 bytes (1 switches on core 0)
Not Found: /src/frame/static/image/wx.png
[pid: 3196|app: 0|req: 31/153] 218.247.217.98 () {36 vars in 658 bytes} [Mon Dec  3 11:32:35 2018] GET /src/frame/static/image/wx.png => generated 4593 bytes in 3 msecs (HTTP/1.1 404) 3 headers in 102 bytes (1 switches on core 0)
Not Found: /src/frame/static/js/vip_comm.js
[pid: 3195|app: 0|req: 30/154] 218.247.217.98 () {36 vars in 626 bytes} [Mon Dec  3 11:32:35 2018] GET /src/frame/static/js/vip_comm.js => generated 4599 bytes in 3 msecs (HTTP/1.1 404) 3 headers in 102 bytes (1 switches on core 0)
[pid: 3196|app: 0|req: 32/155] 218.247.217.98 () {36 vars in 598 bytes} [Mon Dec  3 11:32:35 2018] GET /js/index.js => generated 7174 bytes in 0 msecs (HTTP/1.1 200) 3 headers in 110 bytes (1 switches on core 0)
Not Found: /src/layui/layui.js
[pid: 3194|app: 0|req: 33/156] 218.247.217.98 () {36 vars in 612 bytes} [Mon Dec  3 11:32:35 2018] GET /src/layui/layui.js => generated 4560 bytes in 6 msecs (HTTP/1.1 404) 3 headers in 102 bytes (1 switches on core 0)
Not Found: /src/frame/layui/css/layui.css
[pid: 3193|app: 0|req: 34/157] 218.247.217.98 () {36 vars in 649 bytes} [Mon Dec  3 11:32:35 2018] GET /src/frame/layui/css/layui.css => generated 4593 bytes in 11 msecs (HTTP/1.1 404) 3 headers in 102 bytes (1 switches on core 0)
Not Found: /src/frame/static/css/style.css
[pid: 3192|app: 0|req: 29/158] 218.247.217.98 () {36 vars in 651 bytes} [Mon Dec  3 11:32:35 2018] GET /src/frame/static/css/style.css => generated 4596 bytes in 10 msecs (HTTP/1.1 404) 3 headers in 102 bytes (1 switches on core 0)
Not Found: /src/frame/echarts/echarts.min.js
[pid: 3195|app: 0|req: 31/159] 218.247.217.98 () {36 vars in 640 bytes} [Mon Dec  3 11:32:35 2018] GET /src/frame/echarts/echarts.min.js => generated 4602 bytes in 5 msecs (HTTP/1.1 404) 3 headers in 102 bytes (1 switches on core 0)
Not Found: /src/frame/echarts/echarts.min.js
[pid: 3196|app: 0|req: 33/160] 218.247.217.98 () {36 vars in 640 bytes} [Mon Dec  3 11:32:35 2018] GET /src/frame/echarts/echarts.min.js => generated 4602 bytes in 3 msecs (HTTP/1.1 404) 3 headers in 102 bytes (1 switches on core 0)
[deadlock-detector] a process holding a robust mutex died. recovering...
Mon Dec  3 11:34:16 2018 - uWSGI worker 5 screams: UAAAAAAH my master disconnected: i will kill myself !!!
*** Starting uWSGI 2.0.17.1 (64bit) on [Mon Dec  3 19:34:19 2018] ***
compiled with version: 4.4.7 20120313 (Red Hat 4.4.7-23) on 30 November 2018 04:50:16
os: Linux-2.6.32-696.6.3.el6.x86_64 #1 SMP Wed Jul 12 14:17:22 UTC 2017
nodename: iZ2zegdkenf5ki7xp8k3wkZ
machine: x86_64
clock source: unix
pcre jit disabled
detected number of CPU cores: 2
current working directory: /root/twodj
writing pidfile to /root/script/uwsgi.pid
detected binary path: /usr/local/bin/uwsgi
*** WARNING: you are running uWSGI as root !!! (use the --uid flag) ***
chdir() to /root/twodj/
your processes number limit is 15245
your memory page size is 4096 bytes
detected max file descriptor number: 65535
building mime-types dictionary from file /etc/mime.types...883 entry found
lock engine: pthread robust mutexes
thunder lock: enabled
uWSGI http bound on 0.0.0.0:6379 fd 3
uwsgi socket 0 bound to UNIX address /root/script/uwsgi.sock fd 6
*** WARNING: you are running uWSGI as root !!! (use the --uid flag) ***
Python version: 3.6.7 (default, Nov  9 2018, 10:03:30)  [GCC 4.4.7 20120313 (Red Hat 4.4.7-23)]
Python main interpreter initialized at 0x2931a20
*** WARNING: you are running uWSGI as root !!! (use the --uid flag) ***
python threads support enabled
your server socket listen backlog is limited to 100 connections
your mercy for graceful operations on workers is 60 seconds
mapped 486672 bytes (475 KB) for 5 cores
*** Operational MODE: preforking ***
WSGI app 0 (mountpoint='') ready in 0 seconds on interpreter 0x2931a20 pid: 3201 (default app)
*** WARNING: you are running uWSGI as root !!! (use the --uid flag) ***
*** uWSGI is running in multiple interpreter mode ***
spawned uWSGI master process (pid: 3201)
spawned uWSGI worker 1 (pid: 3203, cores: 1)
spawned uWSGI worker 2 (pid: 3204, cores: 1)
spawned uWSGI worker 3 (pid: 3205, cores: 1)
spawned uWSGI worker 4 (pid: 3206, cores: 1)
spawned uWSGI worker 5 (pid: 3207, cores: 1)
spawned uWSGI http 1 (pid: 3208)
[pid: 3203|app: 0|req: 1/1] 218.247.217.98 () {38 vars in 675 bytes} [Mon Dec  3 11:34:24 2018] GET /index => generated 7174 bytes in 19 msecs (HTTP/1.1 200) 3 headers in 110 bytes (1 switches on core 0)
[pid: 3204|app: -1|req: -1/2] 218.247.217.98 () {36 vars in 637 bytes} [Mon Dec  3 11:34:24 2018] GET /src/frame/layui/css/layui.css => generated 50971 bytes in 0 msecs via sendfile() (HTTP/1.1 200) 3 headers in 112 bytes (0 switches on core 0)
[pid: 3205|app: -1|req: -1/3] 218.247.217.98 () {36 vars in 639 bytes} [Mon Dec  3 11:34:24 2018] GET /src/frame/static/css/style.css => generated 11288 bytes in 0 msecs via sendfile() (HTTP/1.1 200) 3 headers in 112 bytes (0 switches on core 0)
[pid: 3207|app: -1|req: -1/4] 218.247.217.98 () {36 vars in 612 bytes} [Mon Dec  3 11:34:24 2018] GET /src/frame/layui/layui.js => generated 5923 bytes in 0 msecs via sendfile() (HTTP/1.1 200) 3 headers in 118 bytes (0 switches on core 0)
[pid: 3206|app: -1|req: -1/5] 218.247.217.98 () {36 vars in 662 bytes} [Mon Dec  3 11:34:24 2018] GET /src/frame/static/image/code.png => generated 2108 bytes in 0 msecs via sendfile() (HTTP/1.1 200) 3 headers in 112 bytes (0 switches on core 0)
[pid: 3203|app: -1|req: -1/6] 218.247.217.98 () {36 vars in 626 bytes} [Mon Dec  3 11:34:24 2018] GET /src/frame/static/js/vip_comm.js => generated 9870 bytes in 0 msecs via sendfile() (HTTP/1.1 200) 3 headers in 118 bytes (1 switches on core 0)
[pid: 3204|app: -1|req: -1/7] 218.247.217.98 () {36 vars in 660 bytes} [Mon Dec  3 11:34:24 2018] GET /src/frame/static/image/zfb.png => generated 25040 bytes in 0 msecs via sendfile() (HTTP/1.1 200) 3 headers in 113 bytes (0 switches on core 0)
[pid: 3205|app: -1|req: -1/8] 218.247.217.98 () {36 vars in 658 bytes} [Mon Dec  3 11:34:24 2018] GET /src/frame/static/image/wx.png => generated 39482 bytes in 0 msecs via sendfile() (HTTP/1.1 200) 3 headers in 113 bytes (0 switches on core 0)
[pid: 3207|app: 0|req: 1/9] 218.247.217.98 () {38 vars in 715 bytes} [Mon Dec  3 11:34:24 2018] GET /demo/welcome.html => generated 24253 bytes in 18 msecs (HTTP/1.1 200) 3 headers in 111 bytes (1 switches on core 0)
[pid: 3206|app: -1|req: -1/10] 218.247.217.98 () {38 vars in 711 bytes} [Mon Dec  3 11:34:24 2018] GET /src/frame/layui/font/iconfont.woff?v=2.0.0 => generated 21680 bytes in 0 msecs via sendfile() (HTTP/1.1 200) 2 headers in 88 bytes (0 switches on core 0)
[pid: 3203|app: -1|req: -1/11] 218.247.217.98 () {36 vars in 612 bytes} [Mon Dec  3 11:34:24 2018] GET /src/layui/layui.js => generated 9616 bytes in 0 msecs via sendfile() (HTTP/1.1 200) 3 headers in 118 bytes (0 switches on core 0)
[pid: 3204|app: 0|req: 1/12] 218.247.217.98 () {36 vars in 598 bytes} [Mon Dec  3 11:34:24 2018] GET /js/index.js => generated 7174 bytes in 19 msecs (HTTP/1.1 200) 3 headers in 110 bytes (1 switches on core 0)
[pid: 3207|app: -1|req: -1/13] 218.247.217.98 () {36 vars in 636 bytes} [Mon Dec  3 11:34:24 2018] GET /src/frame/layui/lay/modules/layer.js => generated 21862 bytes in 0 msecs via sendfile() (HTTP/1.1 200) 3 headers in 119 bytes (0 switches on core 0)
[pid: 3206|app: -1|req: -1/14] 218.247.217.98 () {36 vars in 696 bytes} [Mon Dec  3 11:34:25 2018] GET /src/frame/layui/css/modules/layer/default/layer.css?v=3.0.3 => generated 14364 bytes in 0 msecs via sendfile() (HTTP/1.1 200) 3 headers in 112 bytes (0 switches on core 0)
[pid: 3203|app: -1|req: -1/15] 218.247.217.98 () {36 vars in 638 bytes} [Mon Dec  3 11:34:25 2018] GET /src/frame/layui/lay/modules/jquery.js => generated 97647 bytes in 0 msecs via sendfile() (HTTP/1.1 200) 3 headers in 119 bytes (0 switches on core 0)
[pid: 3204|app: -1|req: -1/16] 218.247.217.98 () {36 vars in 640 bytes} [Mon Dec  3 11:34:27 2018] GET /src/frame/layui/lay/modules/element.js => generated 6959 bytes in 0 msecs via sendfile() (HTTP/1.1 200) 3 headers in 118 bytes (0 switches on core 0)
Not Found: /frame/static/js/vip_nav.js
[pid: 3207|app: 0|req: 2/17] 218.247.217.98 () {36 vars in 616 bytes} [Mon Dec  3 11:34:27 2018] GET /frame/static/js/vip_nav.js => generated 4584 bytes in 7 msecs (HTTP/1.1 404) 3 headers in 102 bytes (1 switches on core 0)
[pid: 3206|app: -1|req: -1/18] 218.247.217.98 () {36 vars in 634 bytes} [Mon Dec  3 11:34:27 2018] GET /src/frame/layui/lay/modules/util.js => generated 1760 bytes in 0 msecs via sendfile() (HTTP/1.1 200) 3 headers in 118 bytes (0 switches on core 0)
[pid: 3203|app: 0|req: 2/19] 218.247.217.98 () {38 vars in 715 bytes} [Mon Dec  3 11:34:27 2018] GET /spider/basic.html => generated 12233 bytes in 2 msecs (HTTP/1.1 200) 3 headers in 111 bytes (1 switches on core 0)
[pid: 3204|app: -1|req: -1/20] 218.247.217.98 () {36 vars in 625 bytes} [Mon Dec  3 11:34:27 2018] GET /src/css/layui.css => generated 69092 bytes in 0 msecs via sendfile() (HTTP/1.1 200) 3 headers in 112 bytes (0 switches on core 0)
[pid: 3206|app: -1|req: -1/21] 218.247.217.98 () {36 vars in 600 bytes} [Mon Dec  3 11:34:27 2018] GET /src/layui.js => generated 15036 bytes in 0 msecs via sendfile() (HTTP/1.1 200) 3 headers in 119 bytes (0 switches on core 0)
[pid: 3207|app: -1|req: -1/22] 218.247.217.98 () {36 vars in 616 bytes} [Mon Dec  3 11:34:27 2018] GET /src/jquery-latest.js => generated 282766 bytes in 3183 msecs via sendfile() (HTTP/1.1 200) 3 headers in 120 bytes (2 switches on core 0)
[pid: 3205|app: -1|req: -1/23] 218.247.217.98 () {36 vars in 640 bytes} [Mon Dec  3 11:34:24 2018] GET /src/frame/echarts/echarts.min.js => generated 577370 bytes in 6548 msecs via sendfile() (HTTP/1.1 200) 3 headers in 120 bytes (6 switches on core 0)
[pid: 3203|app: -1|req: -1/24] 218.247.217.98 () {36 vars in 624 bytes} [Mon Dec  3 11:34:32 2018] GET /src/lay/modules/table.js => generated 42522 bytes in 0 msecs via sendfile() (HTTP/1.1 200) 3 headers in 119 bytes (0 switches on core 0)
[pid: 3204|app: -1|req: -1/25] 218.247.217.98 () {36 vars in 640 bytes} [Mon Dec  3 11:34:32 2018] GET /src/layui/lay/modules/element.js => generated 7264 bytes in 0 msecs via sendfile() (HTTP/1.1 200) 3 headers in 118 bytes (0 switches on core 0)
[pid: 3206|app: -1|req: -1/26] 218.247.217.98 () {36 vars in 638 bytes} [Mon Dec  3 11:34:32 2018] GET /src/layui/lay/modules/jquery.js => generated 97648 bytes in 0 msecs via sendfile() (HTTP/1.1 200) 3 headers in 119 bytes (0 switches on core 0)
[pid: 3207|app: -1|req: -1/27] 218.247.217.98 () {36 vars in 634 bytes} [Mon Dec  3 11:34:33 2018] GET /src/layui/lay/modules/form.js => generated 9146 bytes in 0 msecs via sendfile() (HTTP/1.1 200) 3 headers in 118 bytes (0 switches on core 0)
[pid: 3205|app: -1|req: -1/28] 218.247.217.98 () {36 vars in 636 bytes} [Mon Dec  3 11:34:33 2018] GET /src/layui/lay/modules/layer.js => generated 22041 bytes in 0 msecs via sendfile() (HTTP/1.1 200) 3 headers in 119 bytes (0 switches on core 0)
[pid: 3203|app: -1|req: -1/29] 218.247.217.98 () {36 vars in 696 bytes} [Mon Dec  3 11:34:34 2018] GET /src/layui/css/modules/layer/default/layer.css?v=3.1.1 => generated 14425 bytes in 0 msecs via sendfile() (HTTP/1.1 200) 3 headers in 112 bytes (0 switches on core 0)
[pid: 3204|app: -1|req: -1/30] 218.247.217.98 () {36 vars in 636 bytes} [Mon Dec  3 11:34:34 2018] GET /src/layui/lay/modules/table.js => generated 30342 bytes in 0 msecs via sendfile() (HTTP/1.1 200) 3 headers in 119 bytes (0 switches on core 0)
[pid: 3206|app: -1|req: -1/31] 218.247.217.98 () {36 vars in 638 bytes} [Mon Dec  3 11:34:34 2018] GET /src/layui/lay/modules/laytpl.js => generated 1836 bytes in 0 msecs via sendfile() (HTTP/1.1 200) 3 headers in 118 bytes (0 switches on core 0)
[pid: 3207|app: -1|req: -1/32] 218.247.217.98 () {36 vars in 640 bytes} [Mon Dec  3 11:34:34 2018] GET /src/layui/lay/modules/laypage.js => generated 4472 bytes in 0 msecs via sendfile() (HTTP/1.1 200) 3 headers in 118 bytes (0 switches on core 0)
[pid: 3205|app: -1|req: -1/33] 218.247.217.98 () {36 vars in 634 bytes} [Mon Dec  3 11:34:34 2018] GET /src/layui/lay/modules/util.js => generated 3458 bytes in 0 msecs via sendfile() (HTTP/1.1 200) 3 headers in 118 bytes (0 switches on core 0)
Not Found: /demo/vip_tab.js
[pid: 3203|app: 0|req: 3/34] 218.247.217.98 () {36 vars in 606 bytes} [Mon Dec  3 11:34:34 2018] GET /demo/vip_tab.js => generated 4551 bytes in 6 msecs (HTTP/1.1 404) 3 headers in 102 bytes (1 switches on core 0)
[pid: 3204|app: -1|req: -1/35] 218.247.217.98 () {36 vars in 626 bytes} [Mon Dec  3 11:34:35 2018] GET /src/lay/modules/laytpl.js => generated 3229 bytes in 0 msecs via sendfile() (HTTP/1.1 200) 3 headers in 118 bytes (0 switches on core 0)
[pid: 3206|app: -1|req: -1/36] 218.247.217.98 () {36 vars in 628 bytes} [Mon Dec  3 11:34:35 2018] GET /src/lay/modules/laypage.js => generated 9151 bytes in 0 msecs via sendfile() (HTTP/1.1 200) 3 headers in 118 bytes (0 switches on core 0)
[pid: 3207|app: -1|req: -1/37] 218.247.217.98 () {36 vars in 624 bytes} [Mon Dec  3 11:34:35 2018] GET /src/lay/modules/layer.js => generated 39377 bytes in 0 msecs via sendfile() (HTTP/1.1 200) 3 headers in 119 bytes (0 switches on core 0)
[pid: 3203|app: -1|req: -1/38] 218.247.217.98 () {36 vars in 684 bytes} [Mon Dec  3 11:34:35 2018] GET /src/css/modules/layer/default/layer.css?v=3.1.1 => generated 15585 bytes in 0 msecs via sendfile() (HTTP/1.1 200) 3 headers in 112 bytes (1 switches on core 0)
[pid: 3205|app: 0|req: 1/39] 218.247.217.98 () {38 vars in 725 bytes} [Mon Dec  3 11:34:35 2018] GET /spider/distribute.html => generated 3960 bytes in 19 msecs (HTTP/1.1 200) 3 headers in 110 bytes (1 switches on core 0)
[pid: 3204|app: -1|req: -1/40] 218.247.217.98 () {36 vars in 622 bytes} [Mon Dec  3 11:34:35 2018] GET /src/lay/modules/form.js => generated 22243 bytes in 0 msecs via sendfile() (HTTP/1.1 200) 3 headers in 119 bytes (0 switches on core 0)
[pid: 3207|app: -1|req: -1/41] 218.247.217.98 () {36 vars in 625 bytes} [Mon Dec  3 11:34:35 2018] GET /src/lib/layui/layui.js => generated 6542 bytes in 0 msecs via sendfile() (HTTP/1.1 200) 3 headers in 118 bytes (1 switches on core 0)
[pid: 3203|app: -1|req: -1/42] 218.247.217.98 () {36 vars in 649 bytes} [Mon Dec  3 11:34:35 2018] GET /src/lib/layui/lay/modules/table.js => generated 20828 bytes in 0 msecs via sendfile() (HTTP/1.1 200) 3 headers in 119 bytes (0 switches on core 0)
[pid: 3206|app: 0|req: 1/43] 218.247.217.98 () {38 vars in 699 bytes} [Mon Dec  3 11:34:35 2018] GET /data/?page=1&limit=30 => generated 11502 bytes in 41 msecs (HTTP/1.1 200) 3 headers in 102 bytes (2 switches on core 0)
[pid: 3205|app: -1|req: -1/44] 218.247.217.98 () {36 vars in 650 bytes} [Mon Dec  3 11:34:35 2018] GET /src/lib/layui/lay/modules/laytpl.js => generated 1836 bytes in 0 msecs via sendfile() (HTTP/1.1 200) 3 headers in 118 bytes (0 switches on core 0)
[pid: 3204|app: -1|req: -1/45] 218.247.217.98 () {36 vars in 652 bytes} [Mon Dec  3 11:34:35 2018] GET /src/lib/layui/lay/modules/laypage.js => generated 4319 bytes in 0 msecs via sendfile() (HTTP/1.1 200) 3 headers in 118 bytes (0 switches on core 0)
[pid: 3207|app: -1|req: -1/46] 218.247.217.98 () {36 vars in 648 bytes} [Mon Dec  3 11:34:35 2018] GET /src/lib/layui/lay/modules/layer.js => generated 22063 bytes in 0 msecs via sendfile() (HTTP/1.1 200) 3 headers in 119 bytes (0 switches on core 0)
[pid: 3203|app: -1|req: -1/47] 218.247.217.98 () {36 vars in 708 bytes} [Mon Dec  3 11:34:35 2018] GET /src/lib/layui/css/modules/layer/default/layer.css?v=3.1.1 => generated 14425 bytes in 0 msecs via sendfile() (HTTP/1.1 200) 3 headers in 112 bytes (0 switches on core 0)
[pid: 3206|app: -1|req: -1/48] 218.247.217.98 () {36 vars in 650 bytes} [Mon Dec  3 11:34:35 2018] GET /src/lib/layui/lay/modules/jquery.js => generated 97648 bytes in 0 msecs via sendfile() (HTTP/1.1 200) 3 headers in 119 bytes (0 switches on core 0)
[pid: 3205|app: 0|req: 2/49] 218.247.217.98 () {38 vars in 710 bytes} [Mon Dec  3 11:34:36 2018] GET /spider/pid.html => generated 3845 bytes in 1 msecs (HTTP/1.1 200) 3 headers in 110 bytes (1 switches on core 0)
[pid: 3204|app: -1|req: -1/50] 218.247.217.98 () {36 vars in 639 bytes} [Mon Dec  3 11:34:36 2018] GET /src/lib/layui/lay/modules/form.js => generated 7925 bytes in 0 msecs via sendfile() (HTTP/1.1 200) 3 headers in 118 bytes (0 switches on core 0)
[pid: 3203|app: 0|req: 4/51] 218.247.217.98 () {38 vars in 696 bytes} [Mon Dec  3 11:34:37 2018] GET /pid_/?page=1&limit=16 => generated 3191 bytes in 32 msecs (HTTP/1.1 200) 3 headers in 101 bytes (2 switches on core 0)
[pid: 3207|app: 0|req: 3/52] 218.247.217.98 () {38 vars in 717 bytes} [Mon Dec  3 11:34:37 2018] GET /distribute_/?page=1&limit=20 => generated 6706 bytes in 45 msecs (HTTP/1.1 200) 3 headers in 101 bytes (2 switches on core 0)
[pid: 3206|app: -1|req: -1/53] 218.247.217.98 () {38 vars in 670 bytes} [Mon Dec  3 11:34:37 2018] GET /src/font/iconfont.woff?v=230 => generated 26328 bytes in 0 msecs via sendfile() (HTTP/1.1 200) 2 headers in 88 bytes (0 switches on core 0)
[pid: 3205|app: 0|req: 3/54] 218.247.217.98 () {38 vars in 714 bytes} [Mon Dec  3 11:34:40 2018] GET /spider/mysql.html => generated 3240 bytes in 1 msecs (HTTP/1.1 200) 3 headers in 110 bytes (1 switches on core 0)
[pid: 3204|app: 0|req: 2/55] 218.247.217.98 () {38 vars in 702 bytes} [Mon Dec  3 11:34:40 2018] GET /mysql_/?page=1&limit=16 => generated 7513 bytes in 35 msecs (HTTP/1.1 200) 3 headers in 101 bytes (2 switches on core 0)
[pid: 3203|app: 0|req: 5/56] 218.247.217.98 () {38 vars in 720 bytes} [Mon Dec  3 11:34:40 2018] GET /spider/rebbitmq.html => generated 3995 bytes in 1 msecs (HTTP/1.1 200) 3 headers in 110 bytes (1 switches on core 0)
[pid: 3207|app: 0|req: 4/57] 218.247.217.98 () {38 vars in 711 bytes} [Mon Dec  3 11:34:40 2018] GET /rebbitmq_/?page=1&limit=16 => generated 7351 bytes in 27 msecs (HTTP/1.1 200) 3 headers in 101 bytes (2 switches on core 0)
[pid: 3206|app: 0|req: 2/58] 218.247.217.98 () {38 vars in 716 bytes} [Mon Dec  3 11:34:41 2018] GET /spider/server.html => generated 3582 bytes in 8 msecs (HTTP/1.1 200) 3 headers in 110 bytes (1 switches on core 0)
[pid: 3205|app: 0|req: 4/59] 218.247.217.98 () {38 vars in 705 bytes} [Mon Dec  3 11:34:41 2018] GET /server_/?page=1&limit=16 => generated 1099 bytes in 28 msecs (HTTP/1.1 200) 3 headers in 101 bytes (2 switches on core 0)
[pid: 3204|app: 0|req: 3/60] 47.95.122.113 () {30 vars in 362 bytes} [Mon Dec  3 11:35:24 2018] GET /index => generated 7174 bytes in 1 msecs (HTTP/1.0 200) 3 headers in 110 bytes (1 switches on core 0)
[deadlock-detector] a process holding a robust mutex died. recovering...
Mon Dec  3 11:36:03 2018 - uWSGI worker 5 screams: UAAAAAAH my master disconnected: i will kill myself !!!
Mon Dec  3 11:36:03 2018 - uWSGI worker 4 screams: UAAAAAAH my master disconnected: i will kill myself !!!
*** Starting uWSGI 2.0.17.1 (64bit) on [Mon Dec  3 19:36:09 2018] ***
compiled with version: 4.4.7 20120313 (Red Hat 4.4.7-23) on 30 November 2018 04:50:16
os: Linux-2.6.32-696.6.3.el6.x86_64 #1 SMP Wed Jul 12 14:17:22 UTC 2017
nodename: iZ2zegdkenf5ki7xp8k3wkZ
machine: x86_64
clock source: unix
pcre jit disabled
detected number of CPU cores: 2
current working directory: /root/twodj
writing pidfile to /root/script/uwsgi.pid
detected binary path: /usr/local/bin/uwsgi
*** WARNING: you are running uWSGI as root !!! (use the --uid flag) ***
chdir() to /root/twodj/
your processes number limit is 15245
your memory page size is 4096 bytes
detected max file descriptor number: 65535
building mime-types dictionary from file /etc/mime.types...883 entry found
lock engine: pthread robust mutexes
thunder lock: enabled
uWSGI http bound on 127.0.0.1:6379 fd 3
uwsgi socket 0 bound to UNIX address /root/script/uwsgi.sock fd 6
*** WARNING: you are running uWSGI as root !!! (use the --uid flag) ***
Python version: 3.6.7 (default, Nov  9 2018, 10:03:30)  [GCC 4.4.7 20120313 (Red Hat 4.4.7-23)]
Python main interpreter initialized at 0x16a8a20
*** WARNING: you are running uWSGI as root !!! (use the --uid flag) ***
python threads support enabled
your server socket listen backlog is limited to 100 connections
your mercy for graceful operations on workers is 60 seconds
mapped 486672 bytes (475 KB) for 5 cores
*** Operational MODE: preforking ***
WSGI app 0 (mountpoint='') ready in 0 seconds on interpreter 0x16a8a20 pid: 3215 (default app)
*** WARNING: you are running uWSGI as root !!! (use the --uid flag) ***
*** uWSGI is running in multiple interpreter mode ***
spawned uWSGI master process (pid: 3215)
spawned uWSGI worker 1 (pid: 3217, cores: 1)
spawned uWSGI worker 2 (pid: 3218, cores: 1)
spawned uWSGI worker 3 (pid: 3219, cores: 1)
spawned uWSGI worker 4 (pid: 3220, cores: 1)
spawned uWSGI worker 5 (pid: 3221, cores: 1)
spawned uWSGI http 1 (pid: 3222)
[pid: 3217|app: 0|req: 1/1] 127.0.0.1 () {30 vars in 354 bytes} [Mon Dec  3 11:36:34 2018] GET /index => generated 7174 bytes in 18 msecs (HTTP/1.0 200) 3 headers in 110 bytes (1 switches on core 0)
[pid: 3218|app: 0|req: 1/2] 127.0.0.1 () {30 vars in 354 bytes} [Mon Dec  3 11:46:12 2018] GET /index => generated 7174 bytes in 19 msecs (HTTP/1.0 200) 3 headers in 110 bytes (1 switches on core 0)
[pid: 3219|app: 0|req: 1/3] 127.0.0.1 () {30 vars in 354 bytes} [Mon Dec  3 12:29:27 2018] GET /index => generated 7174 bytes in 19 msecs (HTTP/1.0 200) 3 headers in 110 bytes (1 switches on core 0)
[pid: 3221|app: 0|req: 1/4] 127.0.0.1 () {30 vars in 354 bytes} [Tue Dec  4 02:16:25 2018] GET /index => generated 7174 bytes in 19 msecs (HTTP/1.0 200) 3 headers in 110 bytes (1 switches on core 0)
*** Starting uWSGI 2.0.17.1 (64bit) on [Tue Dec  4 10:19:50 2018] ***
compiled with version: 4.4.7 20120313 (Red Hat 4.4.7-23) on 30 November 2018 04:50:16
os: Linux-2.6.32-696.6.3.el6.x86_64 #1 SMP Wed Jul 12 14:17:22 UTC 2017
nodename: iZ2zegdkenf5ki7xp8k3wkZ
machine: x86_64
clock source: unix
pcre jit disabled
detected number of CPU cores: 2
current working directory: /root/twodj
writing pidfile to /root/script/uwsgi.pid
detected binary path: /usr/local/bin/uwsgi
*** WARNING: you are running uWSGI as root !!! (use the --uid flag) ***
chdir() to /root/twodj/
your processes number limit is 15245
your memory page size is 4096 bytes
detected max file descriptor number: 65535
building mime-types dictionary from file /etc/mime.types...883 entry found
lock engine: pthread robust mutexes
thunder lock: enabled
uWSGI http bound on 0.0.0.0:8000 fd 3
uwsgi socket 0 bound to UNIX address /root/script/uwsgi.sock fd 6
*** WARNING: you are running uWSGI as root !!! (use the --uid flag) ***
Python version: 3.6.7 (default, Nov  9 2018, 10:03:30)  [GCC 4.4.7 20120313 (Red Hat 4.4.7-23)]
Python main interpreter initialized at 0x19b9a20
*** WARNING: you are running uWSGI as root !!! (use the --uid flag) ***
python threads support enabled
your server socket listen backlog is limited to 100 connections
your mercy for graceful operations on workers is 60 seconds
mapped 486672 bytes (475 KB) for 5 cores
*** Operational MODE: preforking ***
WSGI app 0 (mountpoint='') ready in 0 seconds on interpreter 0x19b9a20 pid: 3766 (default app)
*** WARNING: you are running uWSGI as root !!! (use the --uid flag) ***
*** uWSGI is running in multiple interpreter mode ***
spawned uWSGI master process (pid: 3766)
spawned uWSGI worker 1 (pid: 3768, cores: 1)
spawned uWSGI worker 2 (pid: 3769, cores: 1)
spawned uWSGI worker 3 (pid: 3770, cores: 1)
spawned uWSGI worker 4 (pid: 3771, cores: 1)
spawned uWSGI worker 5 (pid: 3772, cores: 1)
spawned uWSGI http 1 (pid: 3773)
[pid: 3768|app: 0|req: 1/1] 218.247.217.98 () {38 vars in 675 bytes} [Tue Dec  4 02:19:56 2018] GET /index => generated 7174 bytes in 18 msecs (HTTP/1.1 200) 3 headers in 110 bytes (1 switches on core 0)
[pid: 3769|app: 0|req: 1/2] 218.247.217.98 () {38 vars in 715 bytes} [Tue Dec  4 02:19:56 2018] GET /demo/welcome.html => generated 24253 bytes in 18 msecs (HTTP/1.1 200) 3 headers in 111 bytes (1 switches on core 0)
[pid: 3771|app: -1|req: -1/3] 218.247.217.98 () {38 vars in 667 bytes} [Tue Dec  4 02:19:57 2018] GET /src/layui/layui.js => generated 0 bytes in 0 msecs (HTTP/1.1 304) 0 headers in 29 bytes (0 switches on core 0)
[pid: 3772|app: 0|req: 1/4] 218.247.217.98 () {36 vars in 598 bytes} [Tue Dec  4 02:19:57 2018] GET /js/index.js => generated 7174 bytes in 19 msecs (HTTP/1.1 200) 3 headers in 110 bytes (1 switches on core 0)
Not Found: /frame/static/js/vip_nav.js
[pid: 3770|app: 0|req: 1/5] 218.247.217.98 () {36 vars in 616 bytes} [Tue Dec  4 02:19:57 2018] GET /frame/static/js/vip_nav.js => generated 4584 bytes in 18 msecs (HTTP/1.1 404) 3 headers in 102 bytes (1 switches on core 0)
Not Found: /demo/vip_tab.js
[pid: 3768|app: 0|req: 2/6] 218.247.217.98 () {36 vars in 606 bytes} [Tue Dec  4 02:19:57 2018] GET /demo/vip_tab.js => generated 4551 bytes in 7 msecs (HTTP/1.1 404) 3 headers in 102 bytes (1 switches on core 0)
[pid: 3769|app: 0|req: 2/7] 47.95.122.113 () {30 vars in 362 bytes} [Tue Dec  4 02:20:08 2018] GET /index => generated 7174 bytes in 1 msecs (HTTP/1.0 200) 3 headers in 110 bytes (1 switches on core 0)
[pid: 3771|app: 0|req: 1/8] 127.0.0.1 () {30 vars in 354 bytes} [Tue Dec  4 02:20:21 2018] GET /index => generated 7174 bytes in 18 msecs (HTTP/1.0 200) 3 headers in 110 bytes (1 switches on core 0)
[pid: 3772|app: 0|req: 2/9] 218.247.217.98 () {38 vars in 715 bytes} [Tue Dec  4 02:20:36 2018] GET /spider/basic.html => generated 12233 bytes in 2 msecs (HTTP/1.1 200) 3 headers in 111 bytes (1 switches on core 0)
[pid: 3770|app: 0|req: 2/10] 218.247.217.98 () {38 vars in 699 bytes} [Tue Dec  4 02:20:36 2018] GET /data/?page=1&limit=30 => generated 11502 bytes in 32 msecs (HTTP/1.1 200) 3 headers in 102 bytes (2 switches on core 0)
[pid: 3768|app: -1|req: -1/11] 218.247.217.98 () {36 vars in 727 bytes} [Tue Dec  4 02:20:53 2018] GET /src/css/modules/layer/default/loading-2.gif => generated 1787 bytes in 0 msecs via sendfile() (HTTP/1.1 200) 3 headers in 112 bytes (0 switches on core 0)
[pid: 3769|app: 0|req: 3/12] 218.247.217.98 () {38 vars in 698 bytes} [Tue Dec  4 02:20:53 2018] GET /data/?page=3&limit=30 => generated 374 bytes in 33 msecs (HTTP/1.1 200) 3 headers in 100 bytes (2 switches on core 0)
[pid: 3771|app: 0|req: 2/13] 218.247.217.98 () {38 vars in 698 bytes} [Tue Dec  4 02:20:56 2018] GET /data/?page=2&limit=30 => generated 10882 bytes in 31 msecs (HTTP/1.1 200) 3 headers in 102 bytes (2 switches on core 0)
[pid: 3772|app: 0|req: 3/14] 218.247.217.98 () {38 vars in 699 bytes} [Tue Dec  4 02:21:38 2018] GET /data/?page=1&limit=30 => generated 11502 bytes in 31 msecs (HTTP/1.1 200) 3 headers in 102 bytes (2 switches on core 0)
[pid: 3770|app: 0|req: 3/15] 218.247.217.98 () {38 vars in 699 bytes} [Tue Dec  4 02:21:40 2018] GET /data/?page=2&limit=30 => generated 10882 bytes in 20 msecs (HTTP/1.1 200) 3 headers in 102 bytes (2 switches on core 0)
[pid: 3768|app: 0|req: 3/16] 218.247.217.98 () {38 vars in 699 bytes} [Tue Dec  4 02:21:41 2018] GET /data/?page=3&limit=30 => generated 374 bytes in 37 msecs (HTTP/1.1 200) 3 headers in 100 bytes (2 switches on core 0)
[pid: 3769|app: 0|req: 4/17] 218.247.217.98 () {38 vars in 699 bytes} [Tue Dec  4 02:21:42 2018] GET /data/?page=2&limit=30 => generated 10882 bytes in 21 msecs (HTTP/1.1 200) 3 headers in 102 bytes (2 switches on core 0)
[pid: 3771|app: 0|req: 3/18] 218.247.217.98 () {38 vars in 699 bytes} [Tue Dec  4 02:21:44 2018] GET /data/?page=1&limit=30 => generated 11502 bytes in 26 msecs (HTTP/1.1 200) 3 headers in 102 bytes (2 switches on core 0)
[pid: 3772|app: -1|req: -1/19] 218.247.217.98 () {36 vars in 728 bytes} [Tue Dec  4 02:21:48 2018] GET /src/css/modules/layer/default/loading-1.gif => generated 701 bytes in 0 msecs via sendfile() (HTTP/1.1 200) 3 headers in 111 bytes (0 switches on core 0)
[pid: 3768|app: -1|req: -1/20] 218.247.217.98 () {36 vars in 718 bytes} [Tue Dec  4 02:21:48 2018] GET /src/css/modules/layer/default/icon.png => generated 11493 bytes in 0 msecs via sendfile() (HTTP/1.1 200) 3 headers in 113 bytes (0 switches on core 0)
[pid: 3770|app: 0|req: 4/21] 218.247.217.98 () {38 vars in 754 bytes} [Tue Dec  4 02:21:48 2018] GET /demo/form?path_name=yf_icp_info => generated 9531 bytes in 8 msecs (HTTP/1.1 200) 3 headers in 110 bytes (1 switches on core 0)
[pid: 3769|app: -1|req: -1/22] 218.247.217.98 () {38 vars in 681 bytes} [Tue Dec  4 02:21:48 2018] GET /src/layui/layui.js => generated 0 bytes in 0 msecs (HTTP/1.1 304) 0 headers in 29 bytes (0 switches on core 0)
[pid: 3771|app: 0|req: 4/23] 218.247.217.98 () {44 vars in 837 bytes} [Tue Dec  4 02:21:48 2018] POST /select/by_path_name/ => generated 780 bytes in 26 msecs (HTTP/1.1 200) 3 headers in 101 bytes (1 switches on core 0)
[pid: 3772|app: -1|req: -1/24] 218.247.217.98 () {38 vars in 689 bytes} [Tue Dec  4 02:21:48 2018] GET /src/layui/font/iconfont.woff?v=240 => generated 26744 bytes in 0 msecs via sendfile() (HTTP/1.1 200) 2 headers in 88 bytes (0 switches on core 0)
[pid: 3770|app: -1|req: -1/25] 218.247.217.98 () {36 vars in 736 bytes} [Tue Dec  4 02:21:52 2018] GET /src/layui/css/modules/layer/default/icon.png => generated 11493 bytes in 0 msecs via sendfile() (HTTP/1.1 200) 3 headers in 113 bytes (0 switches on core 0)
[pid: 3768|app: 0|req: 4/26] 218.247.217.98 () {44 vars in 831 bytes} [Tue Dec  4 02:21:52 2018] POST /update/spider_basic_info/by_path_name/ => generated 0 bytes in 47 msecs (HTTP/1.1 200) 3 headers in 107 bytes (1 switches on core 0)
[pid: 3769|app: 0|req: 5/27] 218.247.217.98 () {38 vars in 764 bytes} [Tue Dec  4 02:21:56 2018] GET /demo/form?path_name=yf_court_execute => generated 9536 bytes in 1 msecs (HTTP/1.1 200) 3 headers in 110 bytes (1 switches on core 0)
[pid: 3771|app: -1|req: -1/28] 218.247.217.98 () {38 vars in 686 bytes} [Tue Dec  4 02:21:56 2018] GET /src/layui/layui.js => generated 0 bytes in 0 msecs (HTTP/1.1 304) 0 headers in 29 bytes (0 switches on core 0)
[pid: 3772|app: 0|req: 4/29] 218.247.217.98 () {44 vars in 842 bytes} [Tue Dec  4 02:21:56 2018] POST /select/by_path_name/ => generated 821 bytes in 28 msecs (HTTP/1.1 200) 3 headers in 101 bytes (1 switches on core 0)
[pid: 3770|app: 0|req: 5/30] 218.247.217.98 () {38 vars in 774 bytes} [Tue Dec  4 02:22:01 2018] GET /demo/form?path_name=yf_B_03_1_amac_org_sm => generated 9541 bytes in 1 msecs (HTTP/1.1 200) 3 headers in 110 bytes (1 switches on core 0)
[pid: 3768|app: -1|req: -1/31] 218.247.217.98 () {38 vars in 691 bytes} [Tue Dec  4 02:22:01 2018] GET /src/layui/layui.js => generated 0 bytes in 0 msecs (HTTP/1.1 304) 0 headers in 29 bytes (0 switches on core 0)
[pid: 3769|app: 0|req: 6/32] 218.247.217.98 () {44 vars in 847 bytes} [Tue Dec  4 02:22:01 2018] POST /select/by_path_name/ => generated 828 bytes in 25 msecs (HTTP/1.1 200) 3 headers in 101 bytes (1 switches on core 0)
[pid: 3771|app: 0|req: 5/33] 218.247.217.98 () {38 vars in 778 bytes} [Tue Dec  4 02:22:04 2018] GET /demo/form?path_name=yf_B_03_1_amac_infodisc => generated 9543 bytes in 1 msecs (HTTP/1.1 200) 3 headers in 110 bytes (1 switches on core 0)
[pid: 3772|app: -1|req: -1/34] 218.247.217.98 () {38 vars in 693 bytes} [Tue Dec  4 02:22:04 2018] GET /src/layui/layui.js => generated 0 bytes in 0 msecs (HTTP/1.1 304) 0 headers in 29 bytes (0 switches on core 0)
[pid: 3770|app: 0|req: 6/35] 218.247.217.98 () {44 vars in 849 bytes} [Tue Dec  4 02:22:04 2018] POST /select/by_path_name/ => generated 771 bytes in 21 msecs (HTTP/1.1 200) 3 headers in 101 bytes (1 switches on core 0)
[pid: 3768|app: 0|req: 5/36] 218.247.217.98 () {38 vars in 754 bytes} [Tue Dec  4 02:22:07 2018] GET /demo/form?path_name=yf_icp_info => generated 9531 bytes in 1 msecs (HTTP/1.1 200) 3 headers in 110 bytes (1 switches on core 0)
[pid: 3769|app: -1|req: -1/37] 218.247.217.98 () {38 vars in 681 bytes} [Tue Dec  4 02:22:07 2018] GET /src/layui/layui.js => generated 0 bytes in 0 msecs (HTTP/1.1 304) 0 headers in 29 bytes (0 switches on core 0)
[pid: 3771|app: 0|req: 6/38] 218.247.217.98 () {44 vars in 837 bytes} [Tue Dec  4 02:22:07 2018] POST /select/by_path_name/ => generated 776 bytes in 18 msecs (HTTP/1.1 200) 3 headers in 101 bytes (1 switches on core 0)
[pid: 3772|app: 0|req: 5/39] 218.247.217.98 () {38 vars in 762 bytes} [Tue Dec  4 02:22:11 2018] GET /demo/form?path_name=yf_C_court_fygg => generated 9535 bytes in 1 msecs (HTTP/1.1 200) 3 headers in 110 bytes (1 switches on core 0)
[pid: 3770|app: -1|req: -1/40] 218.247.217.98 () {38 vars in 685 bytes} [Tue Dec  4 02:22:12 2018] GET /src/layui/layui.js => generated 0 bytes in 0 msecs (HTTP/1.1 304) 0 headers in 29 bytes (0 switches on core 0)
[pid: 3768|app: 0|req: 6/41] 218.247.217.98 () {44 vars in 841 bytes} [Tue Dec  4 02:22:12 2018] POST /select/by_path_name/ => generated 752 bytes in 27 msecs (HTTP/1.1 200) 3 headers in 101 bytes (1 switches on core 0)
Internal Server Error: /update/spider_basic_info/by_path_name/
Traceback (most recent call last):
  File "/usr/local/lib/python3.6/site-packages/django/core/handlers/exception.py", line 34, in inner
    response = get_response(request)
  File "/usr/local/lib/python3.6/site-packages/django/core/handlers/base.py", line 126, in _get_response
    response = self.process_exception_by_middleware(e, request)
  File "/usr/local/lib/python3.6/site-packages/django/core/handlers/base.py", line 124, in _get_response
    response = wrapped_callback(request, *callback_args, **callback_kwargs)
  File "./twodj/views.py", line 311, in update_basic_info_by_path_name
    ip = va[0].__getattribute__('ip')
IndexError: list index out of range
[pid: 3769|app: 0|req: 7/42] 218.247.217.98 () {44 vars in 835 bytes} [Tue Dec  4 02:22:19 2018] POST /update/spider_basic_info/by_path_name/ => generated 12185 bytes in 57 msecs (HTTP/1.1 500) 4 headers in 145 bytes (1 switches on core 0)
[pid: 3771|app: 0|req: 7/43] 218.247.217.98 () {38 vars in 752 bytes} [Tue Dec  4 02:22:28 2018] GET /demo/form?path_name=yf_alibaba => generated 9530 bytes in 1 msecs (HTTP/1.1 200) 3 headers in 110 bytes (1 switches on core 0)
[pid: 3772|app: -1|req: -1/44] 218.247.217.98 () {38 vars in 680 bytes} [Tue Dec  4 02:22:28 2018] GET /src/layui/layui.js => generated 0 bytes in 0 msecs (HTTP/1.1 304) 0 headers in 29 bytes (0 switches on core 0)
[pid: 3770|app: 0|req: 7/45] 218.247.217.98 () {44 vars in 836 bytes} [Tue Dec  4 02:22:28 2018] POST /select/by_path_name/ => generated 795 bytes in 20 msecs (HTTP/1.1 200) 3 headers in 101 bytes (1 switches on core 0)
[pid: 3768|app: 0|req: 7/46] 218.247.217.98 () {38 vars in 749 bytes} [Tue Dec  4 02:22:32 2018] GET /demo/form?path_name=yf_A_38_3 => generated 9529 bytes in 1 msecs (HTTP/1.1 200) 3 headers in 110 bytes (1 switches on core 0)
[pid: 3769|app: -1|req: -1/47] 218.247.217.98 () {38 vars in 678 bytes} [Tue Dec  4 02:22:32 2018] GET /src/layui/layui.js => generated 0 bytes in 0 msecs (HTTP/1.1 304) 0 headers in 29 bytes (0 switches on core 0)
[pid: 3771|app: 0|req: 8/48] 218.247.217.98 () {44 vars in 834 bytes} [Tue Dec  4 02:22:32 2018] POST /select/by_path_name/ => generated 886 bytes in 25 msecs (HTTP/1.1 200) 3 headers in 101 bytes (1 switches on core 0)
[pid: 3772|app: 0|req: 6/49] 218.247.217.98 () {38 vars in 753 bytes} [Tue Dec  4 02:22:35 2018] GET /demo/form?path_name=yf_zspolicy => generated 9531 bytes in 1 msecs (HTTP/1.1 200) 3 headers in 110 bytes (1 switches on core 0)
[pid: 3770|app: -1|req: -1/50] 218.247.217.98 () {38 vars in 680 bytes} [Tue Dec  4 02:22:35 2018] GET /src/layui/layui.js => generated 0 bytes in 0 msecs (HTTP/1.1 304) 0 headers in 29 bytes (0 switches on core 0)
[pid: 3768|app: 0|req: 8/51] 218.247.217.98 () {44 vars in 836 bytes} [Tue Dec  4 02:22:35 2018] POST /select/by_path_name/ => generated 823 bytes in 24 msecs (HTTP/1.1 200) 3 headers in 101 bytes (1 switches on core 0)
[pid: 3769|app: 0|req: 8/52] 218.247.217.98 () {38 vars in 749 bytes} [Tue Dec  4 02:22:38 2018] GET /demo/form?path_name=yf_A_03_1 => generated 9529 bytes in 1 msecs (HTTP/1.1 200) 3 headers in 110 bytes (1 switches on core 0)
[pid: 3771|app: -1|req: -1/53] 218.247.217.98 () {38 vars in 678 bytes} [Tue Dec  4 02:22:38 2018] GET /src/layui/layui.js => generated 0 bytes in 0 msecs (HTTP/1.1 304) 0 headers in 29 bytes (0 switches on core 0)
[pid: 3772|app: 0|req: 7/54] 218.247.217.98 () {44 vars in 834 bytes} [Tue Dec  4 02:22:38 2018] POST /select/by_path_name/ => generated 1151 bytes in 19 msecs (HTTP/1.1 200) 3 headers in 102 bytes (1 switches on core 0)
[pid: 3770|app: 0|req: 8/55] 218.247.217.98 () {38 vars in 769 bytes} [Tue Dec  4 02:22:42 2018] GET /demo/form?path_name=yf_court_lesscredit => generated 9539 bytes in 1 msecs (HTTP/1.1 200) 3 headers in 110 bytes (1 switches on core 0)
[pid: 3768|app: -1|req: -1/56] 218.247.217.98 () {38 vars in 689 bytes} [Tue Dec  4 02:22:42 2018] GET /src/layui/layui.js => generated 0 bytes in 0 msecs (HTTP/1.1 304) 0 headers in 29 bytes (0 switches on core 0)
[pid: 3769|app: 0|req: 9/57] 218.247.217.98 () {44 vars in 845 bytes} [Tue Dec  4 02:22:42 2018] POST /select/by_path_name/ => generated 847 bytes in 18 msecs (HTTP/1.1 200) 3 headers in 101 bytes (1 switches on core 0)
[pid: 3771|app: 0|req: 9/58] 218.247.217.98 () {38 vars in 754 bytes} [Tue Dec  4 02:22:50 2018] GET /demo/form?path_name=yf_icp_info => generated 9531 bytes in 1 msecs (HTTP/1.1 200) 3 headers in 110 bytes (1 switches on core 0)
[pid: 3772|app: -1|req: -1/59] 218.247.217.98 () {38 vars in 681 bytes} [Tue Dec  4 02:22:50 2018] GET /src/layui/layui.js => generated 0 bytes in 0 msecs (HTTP/1.1 304) 0 headers in 29 bytes (0 switches on core 0)
[pid: 3770|app: 0|req: 9/60] 218.247.217.98 () {44 vars in 837 bytes} [Tue Dec  4 02:22:50 2018] POST /select/by_path_name/ => generated 776 bytes in 29 msecs (HTTP/1.1 200) 3 headers in 101 bytes (1 switches on core 0)
[pid: 3768|app: 0|req: 9/61] 218.247.217.98 () {38 vars in 675 bytes} [Tue Dec  4 02:25:10 2018] GET /index => generated 7174 bytes in 1 msecs (HTTP/1.1 200) 3 headers in 110 bytes (1 switches on core 0)
[pid: 3769|app: 0|req: 10/62] 218.247.217.98 () {38 vars in 715 bytes} [Tue Dec  4 02:25:10 2018] GET /demo/welcome.html => generated 24253 bytes in 1 msecs (HTTP/1.1 200) 3 headers in 111 bytes (1 switches on core 0)
[pid: 3771|app: -1|req: -1/63] 218.247.217.98 () {38 vars in 667 bytes} [Tue Dec  4 02:25:10 2018] GET /src/layui/layui.js => generated 0 bytes in 0 msecs (HTTP/1.1 304) 0 headers in 29 bytes (0 switches on core 0)
[pid: 3772|app: 0|req: 8/64] 218.247.217.98 () {36 vars in 598 bytes} [Tue Dec  4 02:25:10 2018] GET /js/index.js => generated 7174 bytes in 1 msecs (HTTP/1.1 200) 3 headers in 110 bytes (1 switches on core 0)
Not Found: /frame/static/js/vip_nav.js
[pid: 3770|app: 0|req: 10/65] 218.247.217.98 () {36 vars in 616 bytes} [Tue Dec  4 02:25:11 2018] GET /frame/static/js/vip_nav.js => generated 4584 bytes in 4 msecs (HTTP/1.1 404) 3 headers in 102 bytes (1 switches on core 0)
Not Found: /demo/vip_tab.js
[pid: 3768|app: 0|req: 10/66] 218.247.217.98 () {36 vars in 606 bytes} [Tue Dec  4 02:25:11 2018] GET /demo/vip_tab.js => generated 4551 bytes in 4 msecs (HTTP/1.1 404) 3 headers in 102 bytes (1 switches on core 0)
[pid: 3769|app: 0|req: 11/67] 218.247.217.98 () {38 vars in 715 bytes} [Tue Dec  4 02:25:12 2018] GET /spider/basic.html => generated 12233 bytes in 1 msecs (HTTP/1.1 200) 3 headers in 111 bytes (1 switches on core 0)
[pid: 3771|app: 0|req: 10/68] 218.247.217.98 () {38 vars in 699 bytes} [Tue Dec  4 02:25:12 2018] GET /data/?page=1&limit=30 => generated 11502 bytes in 29 msecs (HTTP/1.1 200) 3 headers in 102 bytes (2 switches on core 0)
Tue Dec  4 04:56:28 2018 - uWSGI worker 4 screams: UAAAAAAH my master disconnected: i will kill myself !!!
Tue Dec  4 04:56:28 2018 - uWSGI worker 5 screams: UAAAAAAH my master disconnected: i will kill myself !!!
Tue Dec  4 04:56:28 2018 - uWSGI worker 3 screams: UAAAAAAH my master disconnected: i will kill myself !!!
Tue Dec  4 04:56:28 2018 - uWSGI worker 1 screams: UAAAAAAH my master disconnected: i will kill myself !!!
*** Starting uWSGI 2.0.17.1 (64bit) on [Tue Dec  4 12:59:36 2018] ***
compiled with version: 4.4.7 20120313 (Red Hat 4.4.7-23) on 30 November 2018 04:50:16
os: Linux-2.6.32-696.6.3.el6.x86_64 #1 SMP Wed Jul 12 14:17:22 UTC 2017
nodename: iZ2zegdkenf5ki7xp8k3wkZ
machine: x86_64
clock source: unix
pcre jit disabled
detected number of CPU cores: 2
current working directory: /root/twodj/twodj
writing pidfile to /root/script/uwsgi.pid
detected binary path: /usr/local/bin/uwsgi
*** WARNING: you are running uWSGI as root !!! (use the --uid flag) ***
chdir() to /root/twodj/
your processes number limit is 15245
your memory page size is 4096 bytes
detected max file descriptor number: 65535
building mime-types dictionary from file /etc/mime.types...883 entry found
lock engine: pthread robust mutexes
thunder lock: enabled
uWSGI http bound on 127.0.0.1:8080 fd 3
uwsgi socket 0 bound to UNIX address /root/script/uwsgi.sock fd 6
*** WARNING: you are running uWSGI as root !!! (use the --uid flag) ***
Python version: 3.6.7 (default, Nov  9 2018, 10:03:30)  [GCC 4.4.7 20120313 (Red Hat 4.4.7-23)]
Python main interpreter initialized at 0x286fa20
*** WARNING: you are running uWSGI as root !!! (use the --uid flag) ***
python threads support enabled
your server socket listen backlog is limited to 100 connections
your mercy for graceful operations on workers is 60 seconds
mapped 486672 bytes (475 KB) for 5 cores
*** Operational MODE: preforking ***
WSGI app 0 (mountpoint='') ready in 0 seconds on interpreter 0x286fa20 pid: 3997 (default app)
*** WARNING: you are running uWSGI as root !!! (use the --uid flag) ***
*** uWSGI is running in multiple interpreter mode ***
spawned uWSGI master process (pid: 3997)
spawned uWSGI worker 1 (pid: 3999, cores: 1)
spawned uWSGI worker 2 (pid: 4000, cores: 1)
spawned uWSGI worker 3 (pid: 4001, cores: 1)
spawned uWSGI worker 4 (pid: 4002, cores: 1)
spawned uWSGI worker 5 (pid: 4003, cores: 1)
spawned uWSGI http 1 (pid: 4004)
[pid: 3999|app: 0|req: 1/1] 127.0.0.1 () {30 vars in 353 bytes} [Tue Dec  4 04:59:54 2018] GET /index => generated 7174 bytes in 19 msecs (HTTP/1.0 200) 3 headers in 110 bytes (1 switches on core 0)
[deadlock-detector] a process holding a robust mutex died. recovering...
Tue Dec  4 05:19:20 2018 - uWSGI worker 3 screams: UAAAAAAH my master disconnected: i will kill myself !!!
Tue Dec  4 05:19:20 2018 - uWSGI worker 4 screams: UAAAAAAH my master disconnected: i will kill myself !!!
Tue Dec  4 05:19:20 2018 - uWSGI worker 5 screams: UAAAAAAH my master disconnected: i will kill myself !!!
*** Starting uWSGI 2.0.17.1 (64bit) on [Tue Dec  4 13:19:38 2018] ***
compiled with version: 4.4.7 20120313 (Red Hat 4.4.7-23) on 30 November 2018 04:50:16
os: Linux-2.6.32-696.6.3.el6.x86_64 #1 SMP Wed Jul 12 14:17:22 UTC 2017
nodename: iZ2zegdkenf5ki7xp8k3wkZ
machine: x86_64
clock source: unix
pcre jit disabled
detected number of CPU cores: 2
current working directory: /etc/nginx/conf.d
writing pidfile to /root/script/uwsgi.pid
detected binary path: /usr/local/bin/uwsgi
*** WARNING: you are running uWSGI as root !!! (use the --uid flag) ***
chdir() to /root/twodj/
your processes number limit is 15245
your memory page size is 4096 bytes
detected max file descriptor number: 65535
building mime-types dictionary from file /etc/mime.types...883 entry found
lock engine: pthread robust mutexes
thunder lock: enabled
uwsgi socket 0 bound to TCP address 127.0.0.1:8080 fd 3
*** WARNING: you are running uWSGI as root !!! (use the --uid flag) ***
Python version: 3.6.7 (default, Nov  9 2018, 10:03:30)  [GCC 4.4.7 20120313 (Red Hat 4.4.7-23)]
Python main interpreter initialized at 0x27a4970
*** WARNING: you are running uWSGI as root !!! (use the --uid flag) ***
python threads support enabled
your server socket listen backlog is limited to 100 connections
your mercy for graceful operations on workers is 60 seconds
mapped 486672 bytes (475 KB) for 5 cores
*** Operational MODE: preforking ***
WSGI app 0 (mountpoint='') ready in 0 seconds on interpreter 0x27a4970 pid: 4069 (default app)
*** WARNING: you are running uWSGI as root !!! (use the --uid flag) ***
*** uWSGI is running in multiple interpreter mode ***
spawned uWSGI master process (pid: 4069)
spawned uWSGI worker 1 (pid: 4071, cores: 1)
spawned uWSGI worker 2 (pid: 4072, cores: 1)
spawned uWSGI worker 3 (pid: 4073, cores: 1)
spawned uWSGI worker 4 (pid: 4074, cores: 1)
spawned uWSGI worker 5 (pid: 4075, cores: 1)
invalid request block size: 21573 (max 4096)...skip
invalid request block size: 21573 (max 4096)...skip
invalid request block size: 21573 (max 4096)...skip
invalid request block size: 21573 (max 4096)...skip
invalid request block size: 21573 (max 4096)...skip
invalid request block size: 21573 (max 4096)...skip
invalid request block size: 21573 (max 4096)...skip
[pid: 4073|app: 0|req: 1/1] 218.247.217.98 () {42 vars in 724 bytes} [Tue Dec  4 05:26:01 2018] GET /index => generated 7174 bytes in 18 msecs (HTTP/1.1 200) 3 headers in 110 bytes (1 switches on core 0)
[pid: 4075|app: 0|req: 1/2] 218.247.217.98 () {42 vars in 764 bytes} [Tue Dec  4 05:26:01 2018] GET /demo/welcome.html => generated 24253 bytes in 19 msecs (HTTP/1.1 200) 3 headers in 111 bytes (1 switches on core 0)
[pid: 4074|app: 0|req: 1/3] 218.247.217.98 () {40 vars in 647 bytes} [Tue Dec  4 05:26:01 2018] GET /js/index.js => generated 7174 bytes in 19 msecs (HTTP/1.1 200) 3 headers in 110 bytes (1 switches on core 0)
[pid: 4071|app: 0|req: 1/4] 218.247.217.98 () {42 vars in 724 bytes} [Tue Dec  4 05:30:34 2018] GET /index => generated 7174 bytes in 19 msecs (HTTP/1.1 200) 3 headers in 110 bytes (1 switches on core 0)
[pid: 4072|app: -1|req: -1/5] 218.247.217.98 () {40 vars in 686 bytes} [Tue Dec  4 05:30:34 2018] GET /src/frame/layui/css/layui.css => generated 50971 bytes in 0 msecs via sendfile() (HTTP/1.1 200) 3 headers in 112 bytes (0 switches on core 0)
[pid: 4073|app: -1|req: -1/6] 218.247.217.98 () {40 vars in 688 bytes} [Tue Dec  4 05:30:34 2018] GET /src/frame/static/css/style.css => generated 11288 bytes in 0 msecs via sendfile() (HTTP/1.1 200) 3 headers in 112 bytes (0 switches on core 0)
[pid: 4075|app: -1|req: -1/7] 218.247.217.98 () {40 vars in 661 bytes} [Tue Dec  4 05:30:34 2018] GET /src/frame/layui/layui.js => generated 5923 bytes in 0 msecs via sendfile() (HTTP/1.1 200) 3 headers in 118 bytes (0 switches on core 0)
[pid: 4074|app: -1|req: -1/8] 218.247.217.98 () {40 vars in 675 bytes} [Tue Dec  4 05:30:35 2018] GET /src/frame/static/js/vip_comm.js => generated 9870 bytes in 0 msecs via sendfile() (HTTP/1.1 200) 3 headers in 118 bytes (0 switches on core 0)
[pid: 4071|app: -1|req: -1/9] 218.247.217.98 () {40 vars in 711 bytes} [Tue Dec  4 05:30:35 2018] GET /src/frame/static/image/code.png => generated 2108 bytes in 0 msecs via sendfile() (HTTP/1.1 200) 3 headers in 112 bytes (0 switches on core 0)
[pid: 4072|app: -1|req: -1/10] 218.247.217.98 () {40 vars in 709 bytes} [Tue Dec  4 05:30:35 2018] GET /src/frame/static/image/zfb.png => generated 25040 bytes in 0 msecs via sendfile() (HTTP/1.1 200) 3 headers in 113 bytes (0 switches on core 0)
[pid: 4073|app: -1|req: -1/11] 218.247.217.98 () {40 vars in 707 bytes} [Tue Dec  4 05:30:35 2018] GET /src/frame/static/image/wx.png => generated 39482 bytes in 0 msecs via sendfile() (HTTP/1.1 200) 3 headers in 113 bytes (0 switches on core 0)
[pid: 4075|app: 0|req: 2/12] 218.247.217.98 () {42 vars in 764 bytes} [Tue Dec  4 05:30:35 2018] GET /demo/welcome.html => generated 24253 bytes in 1 msecs (HTTP/1.1 200) 3 headers in 111 bytes (1 switches on core 0)
[pid: 4074|app: -1|req: -1/13] 218.247.217.98 () {42 vars in 740 bytes} [Tue Dec  4 05:30:35 2018] GET /src/frame/layui/lay/modules/layer.js => generated 0 bytes in 0 msecs (HTTP/1.1 304) 0 headers in 29 bytes (0 switches on core 0)
[pid: 4071|app: -1|req: -1/14] 218.247.217.98 () {44 vars in 815 bytes} [Tue Dec  4 05:30:35 2018] GET /src/frame/layui/font/iconfont.woff?v=2.0.0 => generated 0 bytes in 0 msecs (HTTP/1.1 304) 0 headers in 29 bytes (0 switches on core 0)
[pid: 4072|app: -1|req: -1/15] 218.247.217.98 () {40 vars in 661 bytes} [Tue Dec  4 05:30:35 2018] GET /src/layui/layui.js => generated 9616 bytes in 0 msecs via sendfile() (HTTP/1.1 200) 3 headers in 118 bytes (0 switches on core 0)
[pid: 4073|app: 0|req: 2/16] 218.247.217.98 () {40 vars in 647 bytes} [Tue Dec  4 05:30:35 2018] GET /js/index.js => generated 7174 bytes in 1 msecs (HTTP/1.1 200) 3 headers in 110 bytes (1 switches on core 0)
[pid: 4075|app: -1|req: -1/17] 218.247.217.98 () {40 vars in 689 bytes} [Tue Dec  4 05:30:35 2018] GET /src/frame/echarts/echarts.min.js => generated 577370 bytes in 0 msecs via sendfile() (HTTP/1.1 200) 3 headers in 120 bytes (0 switches on core 0)
[pid: 4074|app: -1|req: -1/18] 218.247.217.98 () {42 vars in 800 bytes} [Tue Dec  4 05:30:35 2018] GET /src/frame/layui/css/modules/layer/default/layer.css?v=3.0.3 => generated 0 bytes in 0 msecs (HTTP/1.1 304) 0 headers in 29 bytes (0 switches on core 0)
[pid: 4071|app: -1|req: -1/19] 218.247.217.98 () {42 vars in 742 bytes} [Tue Dec  4 05:30:35 2018] GET /src/frame/layui/lay/modules/jquery.js => generated 0 bytes in 0 msecs (HTTP/1.1 304) 0 headers in 29 bytes (0 switches on core 0)
[pid: 4072|app: -1|req: -1/20] 218.247.217.98 () {42 vars in 744 bytes} [Tue Dec  4 05:30:35 2018] GET /src/frame/layui/lay/modules/element.js => generated 0 bytes in 0 msecs (HTTP/1.1 304) 0 headers in 29 bytes (0 switches on core 0)
Not Found: /frame/static/js/vip_nav.js
[pid: 4073|app: 0|req: 3/21] 218.247.217.98 () {40 vars in 665 bytes} [Tue Dec  4 05:30:35 2018] GET /frame/static/js/vip_nav.js => generated 4584 bytes in 6 msecs (HTTP/1.1 404) 3 headers in 102 bytes (1 switches on core 0)
[pid: 4075|app: -1|req: -1/22] 218.247.217.98 () {42 vars in 738 bytes} [Tue Dec  4 05:30:35 2018] GET /src/frame/layui/lay/modules/util.js => generated 0 bytes in 0 msecs (HTTP/1.1 304) 0 headers in 29 bytes (0 switches on core 0)
[pid: 4074|app: 0|req: 2/23] 218.247.217.98 () {42 vars in 764 bytes} [Tue Dec  4 05:30:36 2018] GET /spider/basic.html => generated 12233 bytes in 2 msecs (HTTP/1.1 200) 3 headers in 111 bytes (1 switches on core 0)
[pid: 4071|app: -1|req: -1/24] 218.247.217.98 () {42 vars in 729 bytes} [Tue Dec  4 05:30:36 2018] GET /src/css/layui.css => generated 0 bytes in 0 msecs (HTTP/1.1 304) 0 headers in 29 bytes (0 switches on core 0)
[pid: 4072|app: -1|req: -1/25] 218.247.217.98 () {42 vars in 720 bytes} [Tue Dec  4 05:30:36 2018] GET /src/jquery-latest.js => generated 0 bytes in 0 msecs (HTTP/1.1 304) 0 headers in 29 bytes (0 switches on core 0)
[pid: 4073|app: -1|req: -1/26] 218.247.217.98 () {42 vars in 704 bytes} [Tue Dec  4 05:30:36 2018] GET /src/layui.js => generated 0 bytes in 0 msecs (HTTP/1.1 304) 0 headers in 29 bytes (0 switches on core 0)
[pid: 4075|app: -1|req: -1/27] 218.247.217.98 () {42 vars in 728 bytes} [Tue Dec  4 05:30:36 2018] GET /src/lay/modules/table.js => generated 0 bytes in 0 msecs (HTTP/1.1 304) 0 headers in 29 bytes (0 switches on core 0)
[pid: 4074|app: -1|req: -1/28] 218.247.217.98 () {42 vars in 730 bytes} [Tue Dec  4 05:30:36 2018] GET /src/lay/modules/laytpl.js => generated 0 bytes in 0 msecs (HTTP/1.1 304) 0 headers in 29 bytes (0 switches on core 0)
[pid: 4071|app: -1|req: -1/29] 218.247.217.98 () {42 vars in 732 bytes} [Tue Dec  4 05:30:36 2018] GET /src/lay/modules/laypage.js => generated 0 bytes in 0 msecs (HTTP/1.1 304) 0 headers in 29 bytes (0 switches on core 0)
[pid: 4072|app: -1|req: -1/30] 218.247.217.98 () {42 vars in 728 bytes} [Tue Dec  4 05:30:36 2018] GET /src/lay/modules/layer.js => generated 0 bytes in 0 msecs (HTTP/1.1 304) 0 headers in 29 bytes (0 switches on core 0)
[pid: 4073|app: -1|req: -1/31] 218.247.217.98 () {42 vars in 788 bytes} [Tue Dec  4 05:30:36 2018] GET /src/css/modules/layer/default/layer.css?v=3.1.1 => generated 0 bytes in 0 msecs (HTTP/1.1 304) 0 headers in 29 bytes (0 switches on core 0)
[pid: 4075|app: -1|req: -1/32] 218.247.217.98 () {42 vars in 726 bytes} [Tue Dec  4 05:30:36 2018] GET /src/lay/modules/form.js => generated 0 bytes in 0 msecs (HTTP/1.1 304) 0 headers in 29 bytes (0 switches on core 0)
[pid: 4074|app: 0|req: 3/33] 218.247.217.98 () {42 vars in 748 bytes} [Tue Dec  4 05:30:36 2018] GET /data/?page=1&limit=30 => generated 11502 bytes in 26 msecs (HTTP/1.1 200) 3 headers in 102 bytes (2 switches on core 0)
[pid: 4071|app: -1|req: -1/34] 218.247.217.98 () {44 vars in 775 bytes} [Tue Dec  4 05:30:37 2018] GET /src/font/iconfont.woff?v=230 => generated 0 bytes in 0 msecs (HTTP/1.1 304) 0 headers in 29 bytes (0 switches on core 0)
[pid: 4072|app: -1|req: -1/35] 218.247.217.98 () {42 vars in 744 bytes} [Tue Dec  4 05:30:40 2018] GET /src/layui/lay/modules/element.js => generated 0 bytes in 0 msecs (HTTP/1.1 304) 0 headers in 29 bytes (0 switches on core 0)
[pid: 4073|app: -1|req: -1/36] 218.247.217.98 () {42 vars in 742 bytes} [Tue Dec  4 05:30:40 2018] GET /src/layui/lay/modules/jquery.js => generated 0 bytes in 0 msecs (HTTP/1.1 304) 0 headers in 29 bytes (0 switches on core 0)
[pid: 4075|app: -1|req: -1/37] 218.247.217.98 () {42 vars in 738 bytes} [Tue Dec  4 05:30:40 2018] GET /src/layui/lay/modules/form.js => generated 0 bytes in 0 msecs (HTTP/1.1 304) 0 headers in 29 bytes (0 switches on core 0)
[pid: 4074|app: -1|req: -1/38] 218.247.217.98 () {42 vars in 740 bytes} [Tue Dec  4 05:30:40 2018] GET /src/layui/lay/modules/layer.js => generated 0 bytes in 0 msecs (HTTP/1.1 304) 0 headers in 29 bytes (0 switches on core 0)
[pid: 4071|app: -1|req: -1/39] 218.247.217.98 () {42 vars in 800 bytes} [Tue Dec  4 05:30:40 2018] GET /src/layui/css/modules/layer/default/layer.css?v=3.1.1 => generated 0 bytes in 0 msecs (HTTP/1.1 304) 0 headers in 29 bytes (0 switches on core 0)
[pid: 4072|app: -1|req: -1/40] 218.247.217.98 () {42 vars in 740 bytes} [Tue Dec  4 05:30:40 2018] GET /src/layui/lay/modules/table.js => generated 0 bytes in 0 msecs (HTTP/1.1 304) 0 headers in 29 bytes (0 switches on core 0)
[pid: 4073|app: -1|req: -1/41] 218.247.217.98 () {42 vars in 742 bytes} [Tue Dec  4 05:30:40 2018] GET /src/layui/lay/modules/laytpl.js => generated 0 bytes in 0 msecs (HTTP/1.1 304) 0 headers in 29 bytes (0 switches on core 0)
[pid: 4075|app: -1|req: -1/42] 218.247.217.98 () {42 vars in 744 bytes} [Tue Dec  4 05:30:40 2018] GET /src/layui/lay/modules/laypage.js => generated 0 bytes in 0 msecs (HTTP/1.1 304) 0 headers in 29 bytes (0 switches on core 0)
[pid: 4074|app: -1|req: -1/43] 218.247.217.98 () {42 vars in 738 bytes} [Tue Dec  4 05:30:40 2018] GET /src/layui/lay/modules/util.js => generated 0 bytes in 0 msecs (HTTP/1.1 304) 0 headers in 29 bytes (0 switches on core 0)
Not Found: /demo/vip_tab.js
[pid: 4071|app: 0|req: 2/44] 218.247.217.98 () {40 vars in 655 bytes} [Tue Dec  4 05:30:40 2018] GET /demo/vip_tab.js => generated 4551 bytes in 6 msecs (HTTP/1.1 404) 3 headers in 102 bytes (1 switches on core 0)
[pid: 4072|app: 0|req: 1/45] 218.247.217.98 () {42 vars in 724 bytes} [Tue Dec  4 05:30:49 2018] GET /index => generated 7174 bytes in 19 msecs (HTTP/1.1 200) 3 headers in 110 bytes (1 switches on core 0)
[pid: 4073|app: 0|req: 4/46] 218.247.217.98 () {42 vars in 764 bytes} [Tue Dec  4 05:30:49 2018] GET /demo/welcome.html => generated 24253 bytes in 1 msecs (HTTP/1.1 200) 3 headers in 111 bytes (1 switches on core 0)
[pid: 4075|app: 0|req: 3/47] 218.247.217.98 () {40 vars in 647 bytes} [Tue Dec  4 05:30:49 2018] GET /js/index.js => generated 7174 bytes in 1 msecs (HTTP/1.1 200) 3 headers in 110 bytes (1 switches on core 0)
Not Found: /frame/static/js/vip_nav.js
[pid: 4074|app: 0|req: 4/48] 218.247.217.98 () {40 vars in 665 bytes} [Tue Dec  4 05:30:49 2018] GET /frame/static/js/vip_nav.js => generated 4584 bytes in 6 msecs (HTTP/1.1 404) 3 headers in 102 bytes (1 switches on core 0)
Not Found: /demo/vip_tab.js
[pid: 4071|app: 0|req: 3/49] 218.247.217.98 () {40 vars in 655 bytes} [Tue Dec  4 05:30:49 2018] GET /demo/vip_tab.js => generated 4551 bytes in 4 msecs (HTTP/1.1 404) 3 headers in 102 bytes (1 switches on core 0)
[pid: 4072|app: 0|req: 2/50] 218.247.217.98 () {42 vars in 724 bytes} [Tue Dec  4 05:30:50 2018] GET /index => generated 7174 bytes in 1 msecs (HTTP/1.1 200) 3 headers in 110 bytes (1 switches on core 0)
[pid: 4073|app: 0|req: 5/51] 218.247.217.98 () {42 vars in 764 bytes} [Tue Dec  4 05:30:50 2018] GET /demo/welcome.html => generated 24253 bytes in 1 msecs (HTTP/1.1 200) 3 headers in 111 bytes (1 switches on core 0)
[pid: 4075|app: 0|req: 4/52] 218.247.217.98 () {40 vars in 647 bytes} [Tue Dec  4 05:30:50 2018] GET /js/index.js => generated 7174 bytes in 1 msecs (HTTP/1.1 200) 3 headers in 110 bytes (1 switches on core 0)
Not Found: /frame/static/js/vip_nav.js
[pid: 4074|app: 0|req: 5/53] 218.247.217.98 () {40 vars in 665 bytes} [Tue Dec  4 05:30:50 2018] GET /frame/static/js/vip_nav.js => generated 4584 bytes in 4 msecs (HTTP/1.1 404) 3 headers in 102 bytes (1 switches on core 0)
Not Found: /demo/vip_tab.js
[pid: 4071|app: 0|req: 4/54] 218.247.217.98 () {40 vars in 655 bytes} [Tue Dec  4 05:30:50 2018] GET /demo/vip_tab.js => generated 4551 bytes in 4 msecs (HTTP/1.1 404) 3 headers in 102 bytes (1 switches on core 0)
[pid: 4072|app: 0|req: 3/55] 218.247.217.98 () {42 vars in 764 bytes} [Tue Dec  4 05:30:51 2018] GET /spider/basic.html => generated 12233 bytes in 2 msecs (HTTP/1.1 200) 3 headers in 111 bytes (1 switches on core 0)
[pid: 4073|app: 0|req: 6/56] 218.247.217.98 () {42 vars in 748 bytes} [Tue Dec  4 05:30:51 2018] GET /data/?page=1&limit=30 => generated 11502 bytes in 33 msecs (HTTP/1.1 200) 3 headers in 102 bytes (2 switches on core 0)
[pid: 4075|app: 0|req: 5/57] 218.247.217.98 () {42 vars in 774 bytes} [Tue Dec  4 05:30:52 2018] GET /spider/distribute.html => generated 3960 bytes in 1 msecs (HTTP/1.1 200) 3 headers in 110 bytes (1 switches on core 0)
[pid: 4074|app: -1|req: -1/58] 218.247.217.98 () {42 vars in 729 bytes} [Tue Dec  4 05:30:52 2018] GET /src/lib/layui/layui.js => generated 0 bytes in 0 msecs (HTTP/1.1 304) 0 headers in 29 bytes (0 switches on core 0)
[pid: 4071|app: -1|req: -1/59] 218.247.217.98 () {42 vars in 753 bytes} [Tue Dec  4 05:30:52 2018] GET /src/lib/layui/lay/modules/table.js => generated 0 bytes in 0 msecs (HTTP/1.1 304) 0 headers in 29 bytes (0 switches on core 0)
[pid: 4072|app: -1|req: -1/60] 218.247.217.98 () {42 vars in 755 bytes} [Tue Dec  4 05:30:52 2018] GET /src/lib/layui/lay/modules/laytpl.js => generated 0 bytes in 0 msecs (HTTP/1.1 304) 0 headers in 29 bytes (0 switches on core 0)
[pid: 4073|app: -1|req: -1/61] 218.247.217.98 () {42 vars in 757 bytes} [Tue Dec  4 05:30:52 2018] GET /src/lib/layui/lay/modules/laypage.js => generated 0 bytes in 0 msecs (HTTP/1.1 304) 0 headers in 29 bytes (0 switches on core 0)
[pid: 4075|app: -1|req: -1/62] 218.247.217.98 () {42 vars in 753 bytes} [Tue Dec  4 05:30:52 2018] GET /src/lib/layui/lay/modules/layer.js => generated 0 bytes in 0 msecs (HTTP/1.1 304) 0 headers in 29 bytes (0 switches on core 0)
[pid: 4074|app: -1|req: -1/63] 218.247.217.98 () {42 vars in 813 bytes} [Tue Dec  4 05:30:52 2018] GET /src/lib/layui/css/modules/layer/default/layer.css?v=3.1.1 => generated 0 bytes in 0 msecs (HTTP/1.1 304) 0 headers in 29 bytes (0 switches on core 0)
[pid: 4071|app: -1|req: -1/64] 218.247.217.98 () {42 vars in 755 bytes} [Tue Dec  4 05:30:52 2018] GET /src/lib/layui/lay/modules/jquery.js => generated 0 bytes in 0 msecs (HTTP/1.1 304) 0 headers in 29 bytes (0 switches on core 0)
[pid: 4072|app: -1|req: -1/65] 218.247.217.98 () {42 vars in 751 bytes} [Tue Dec  4 05:30:52 2018] GET /src/lib/layui/lay/modules/form.js => generated 0 bytes in 0 msecs (HTTP/1.1 304) 0 headers in 29 bytes (0 switches on core 0)
[pid: 4073|app: 0|req: 7/66] 218.247.217.98 () {42 vars in 767 bytes} [Tue Dec  4 05:30:52 2018] GET /distribute_/?page=1&limit=20 => generated 6706 bytes in 31 msecs (HTTP/1.1 200) 3 headers in 101 bytes (2 switches on core 0)
[pid: 4075|app: 0|req: 6/67] 218.247.217.98 () {42 vars in 760 bytes} [Tue Dec  4 05:30:53 2018] GET /spider/pid.html => generated 3845 bytes in 1 msecs (HTTP/1.1 200) 3 headers in 110 bytes (1 switches on core 0)
[pid: 4074|app: 0|req: 6/68] 218.247.217.98 () {42 vars in 746 bytes} [Tue Dec  4 05:30:53 2018] GET /pid_/?page=1&limit=16 => generated 3243 bytes in 25 msecs (HTTP/1.1 200) 3 headers in 101 bytes (2 switches on core 0)
[pid: 4071|app: 0|req: 5/69] 218.247.217.98 () {42 vars in 764 bytes} [Tue Dec  4 05:30:53 2018] GET /spider/mysql.html => generated 3240 bytes in 1 msecs (HTTP/1.1 200) 3 headers in 110 bytes (1 switches on core 0)
[pid: 4072|app: 0|req: 4/70] 218.247.217.98 () {42 vars in 752 bytes} [Tue Dec  4 05:30:53 2018] GET /mysql_/?page=1&limit=16 => generated 7320 bytes in 27 msecs (HTTP/1.1 200) 3 headers in 101 bytes (2 switches on core 0)
[pid: 4073|app: 0|req: 8/71] 218.247.217.98 () {42 vars in 770 bytes} [Tue Dec  4 05:30:54 2018] GET /spider/rebbitmq.html => generated 3995 bytes in 1 msecs (HTTP/1.1 200) 3 headers in 110 bytes (1 switches on core 0)
[pid: 4075|app: 0|req: 7/72] 218.247.217.98 () {42 vars in 761 bytes} [Tue Dec  4 05:30:54 2018] GET /rebbitmq_/?page=1&limit=16 => generated 7351 bytes in 27 msecs (HTTP/1.1 200) 3 headers in 101 bytes (2 switches on core 0)
[pid: 4074|app: 0|req: 7/73] 218.247.217.98 () {42 vars in 766 bytes} [Tue Dec  4 05:30:55 2018] GET /spider/server.html => generated 3582 bytes in 1 msecs (HTTP/1.1 200) 3 headers in 110 bytes (1 switches on core 0)
[pid: 4071|app: 0|req: 6/74] 218.247.217.98 () {42 vars in 755 bytes} [Tue Dec  4 05:30:55 2018] GET /server_/?page=1&limit=16 => generated 1099 bytes in 31 msecs (HTTP/1.1 200) 3 headers in 101 bytes (2 switches on core 0)
Not Found: /cache/global/img/gs.gif
[pid: 4072|app: 0|req: 5/75] 80.82.70.187 () {32 vars in 435 bytes} [Tue Dec  4 05:32:49 2018] GET /cache/global/img/gs.gif => generated 4570 bytes in 5 msecs (HTTP/1.1 404) 3 headers in 102 bytes (1 switches on core 0)
[pid: 4073|app: 0|req: 9/76] 218.247.217.98 () {42 vars in 724 bytes} [Tue Dec  4 05:41:10 2018] GET /index => generated 7174 bytes in 1 msecs (HTTP/1.1 200) 3 headers in 110 bytes (1 switches on core 0)
[pid: 4075|app: 0|req: 8/77] 218.247.217.98 () {42 vars in 764 bytes} [Tue Dec  4 05:41:10 2018] GET /demo/welcome.html => generated 24253 bytes in 1 msecs (HTTP/1.1 200) 3 headers in 111 bytes (1 switches on core 0)
[pid: 4074|app: 0|req: 8/78] 218.247.217.98 () {40 vars in 647 bytes} [Tue Dec  4 05:41:10 2018] GET /js/index.js => generated 7174 bytes in 1 msecs (HTTP/1.1 200) 3 headers in 110 bytes (1 switches on core 0)
Not Found: /frame/static/js/vip_nav.js
[pid: 4071|app: 0|req: 7/79] 218.247.217.98 () {40 vars in 665 bytes} [Tue Dec  4 05:41:10 2018] GET /frame/static/js/vip_nav.js => generated 4584 bytes in 4 msecs (HTTP/1.1 404) 3 headers in 102 bytes (1 switches on core 0)
Not Found: /demo/vip_tab.js
[pid: 4072|app: 0|req: 6/80] 218.247.217.98 () {40 vars in 655 bytes} [Tue Dec  4 05:41:10 2018] GET /demo/vip_tab.js => generated 4551 bytes in 4 msecs (HTTP/1.1 404) 3 headers in 102 bytes (1 switches on core 0)
[pid: 4073|app: 0|req: 10/81] 218.247.217.98 () {42 vars in 724 bytes} [Tue Dec  4 05:41:10 2018] GET /index => generated 7174 bytes in 1 msecs (HTTP/1.1 200) 3 headers in 110 bytes (1 switches on core 0)
[pid: 4075|app: 0|req: 9/82] 218.247.217.98 () {42 vars in 764 bytes} [Tue Dec  4 05:41:10 2018] GET /demo/welcome.html => generated 24253 bytes in 1 msecs (HTTP/1.1 200) 3 headers in 111 bytes (1 switches on core 0)
Not Found: /frame/static/js/vip_nav.js
[pid: 4074|app: 0|req: 9/83] 218.247.217.98 () {40 vars in 665 bytes} [Tue Dec  4 05:41:10 2018] GET /frame/static/js/vip_nav.js => generated 4584 bytes in 4 msecs (HTTP/1.1 404) 3 headers in 102 bytes (1 switches on core 0)
[pid: 4071|app: 0|req: 8/84] 218.247.217.98 () {40 vars in 647 bytes} [Tue Dec  4 05:41:10 2018] GET /js/index.js => generated 7174 bytes in 1 msecs (HTTP/1.1 200) 3 headers in 110 bytes (1 switches on core 0)
Not Found: /demo/vip_tab.js
[pid: 4072|app: 0|req: 7/85] 218.247.217.98 () {40 vars in 655 bytes} [Tue Dec  4 05:41:11 2018] GET /demo/vip_tab.js => generated 4551 bytes in 4 msecs (HTTP/1.1 404) 3 headers in 102 bytes (1 switches on core 0)
[pid: 4073|app: 0|req: 11/86] 218.247.217.98 () {42 vars in 724 bytes} [Tue Dec  4 05:41:11 2018] GET /index => generated 7174 bytes in 1 msecs (HTTP/1.1 200) 3 headers in 110 bytes (1 switches on core 0)
[pid: 4075|app: 0|req: 10/87] 218.247.217.98 () {42 vars in 764 bytes} [Tue Dec  4 05:41:11 2018] GET /demo/welcome.html => generated 24253 bytes in 1 msecs (HTTP/1.1 200) 3 headers in 111 bytes (1 switches on core 0)
[pid: 4074|app: 0|req: 10/88] 218.247.217.98 () {40 vars in 647 bytes} [Tue Dec  4 05:41:11 2018] GET /js/index.js => generated 7174 bytes in 1 msecs (HTTP/1.1 200) 3 headers in 110 bytes (1 switches on core 0)
Not Found: /frame/static/js/vip_nav.js
[pid: 4071|app: 0|req: 9/89] 218.247.217.98 () {40 vars in 665 bytes} [Tue Dec  4 05:41:11 2018] GET /frame/static/js/vip_nav.js => generated 4584 bytes in 4 msecs (HTTP/1.1 404) 3 headers in 102 bytes (1 switches on core 0)
Not Found: /demo/vip_tab.js
[pid: 4072|app: 0|req: 8/90] 218.247.217.98 () {40 vars in 655 bytes} [Tue Dec  4 05:41:11 2018] GET /demo/vip_tab.js => generated 4551 bytes in 4 msecs (HTTP/1.1 404) 3 headers in 102 bytes (1 switches on core 0)
[pid: 4073|app: 0|req: 12/91] 218.247.217.98 () {42 vars in 724 bytes} [Tue Dec  4 05:41:11 2018] GET /index => generated 7174 bytes in 1 msecs (HTTP/1.1 200) 3 headers in 110 bytes (1 switches on core 0)
[pid: 4075|app: 0|req: 11/92] 218.247.217.98 () {42 vars in 764 bytes} [Tue Dec  4 05:41:12 2018] GET /demo/welcome.html => generated 24253 bytes in 1 msecs (HTTP/1.1 200) 3 headers in 111 bytes (1 switches on core 0)
Not Found: /frame/static/js/vip_nav.js
[pid: 4074|app: 0|req: 11/93] 218.247.217.98 () {40 vars in 665 bytes} [Tue Dec  4 05:41:12 2018] GET /frame/static/js/vip_nav.js => generated 4584 bytes in 4 msecs (HTTP/1.1 404) 3 headers in 102 bytes (1 switches on core 0)
[pid: 4071|app: 0|req: 10/94] 218.247.217.98 () {40 vars in 647 bytes} [Tue Dec  4 05:41:12 2018] GET /js/index.js => generated 7174 bytes in 1 msecs (HTTP/1.1 200) 3 headers in 110 bytes (1 switches on core 0)
Not Found: /demo/vip_tab.js
[pid: 4072|app: 0|req: 9/95] 218.247.217.98 () {40 vars in 655 bytes} [Tue Dec  4 05:41:12 2018] GET /demo/vip_tab.js => generated 4551 bytes in 4 msecs (HTTP/1.1 404) 3 headers in 102 bytes (1 switches on core 0)
[pid: 4073|app: 0|req: 13/96] 218.247.217.98 () {42 vars in 724 bytes} [Tue Dec  4 05:41:12 2018] GET /index => generated 7174 bytes in 1 msecs (HTTP/1.1 200) 3 headers in 110 bytes (1 switches on core 0)
[pid: 4075|app: 0|req: 12/97] 218.247.217.98 () {42 vars in 764 bytes} [Tue Dec  4 05:41:12 2018] GET /demo/welcome.html => generated 24253 bytes in 1 msecs (HTTP/1.1 200) 3 headers in 111 bytes (1 switches on core 0)
Not Found: /frame/static/js/vip_nav.js
[pid: 4074|app: 0|req: 12/98] 218.247.217.98 () {40 vars in 665 bytes} [Tue Dec  4 05:41:12 2018] GET /frame/static/js/vip_nav.js => generated 4584 bytes in 4 msecs (HTTP/1.1 404) 3 headers in 102 bytes (1 switches on core 0)
[pid: 4071|app: 0|req: 11/99] 218.247.217.98 () {40 vars in 647 bytes} [Tue Dec  4 05:41:12 2018] GET /js/index.js => generated 7174 bytes in 1 msecs (HTTP/1.1 200) 3 headers in 110 bytes (1 switches on core 0)
Not Found: /demo/vip_tab.js
[pid: 4072|app: 0|req: 10/100] 218.247.217.98 () {40 vars in 655 bytes} [Tue Dec  4 05:41:12 2018] GET /demo/vip_tab.js => generated 4551 bytes in 4 msecs (HTTP/1.1 404) 3 headers in 102 bytes (1 switches on core 0)
[pid: 4073|app: 0|req: 14/101] 218.247.217.98 () {42 vars in 724 bytes} [Tue Dec  4 05:41:13 2018] GET /index => generated 7174 bytes in 1 msecs (HTTP/1.1 200) 3 headers in 110 bytes (1 switches on core 0)
[pid: 4075|app: 0|req: 13/102] 218.247.217.98 () {42 vars in 764 bytes} [Tue Dec  4 05:41:13 2018] GET /demo/welcome.html => generated 24253 bytes in 1 msecs (HTTP/1.1 200) 3 headers in 111 bytes (1 switches on core 0)
[pid: 4074|app: 0|req: 13/103] 218.247.217.98 () {40 vars in 647 bytes} [Tue Dec  4 05:41:13 2018] GET /js/index.js => generated 7174 bytes in 1 msecs (HTTP/1.1 200) 3 headers in 110 bytes (1 switches on core 0)
Not Found: /frame/static/js/vip_nav.js
[pid: 4071|app: 0|req: 12/104] 218.247.217.98 () {40 vars in 665 bytes} [Tue Dec  4 05:41:14 2018] GET /frame/static/js/vip_nav.js => generated 4584 bytes in 4 msecs (HTTP/1.1 404) 3 headers in 102 bytes (1 switches on core 0)
Not Found: /demo/vip_tab.js
[pid: 4072|app: 0|req: 11/105] 218.247.217.98 () {40 vars in 655 bytes} [Tue Dec  4 05:41:14 2018] GET /demo/vip_tab.js => generated 4551 bytes in 4 msecs (HTTP/1.1 404) 3 headers in 102 bytes (1 switches on core 0)
[pid: 4073|app: 0|req: 15/106] 218.247.217.98 () {42 vars in 724 bytes} [Tue Dec  4 05:41:14 2018] GET /index => generated 7174 bytes in 1 msecs (HTTP/1.1 200) 3 headers in 110 bytes (1 switches on core 0)
[pid: 4075|app: 0|req: 14/107] 218.247.217.98 () {42 vars in 764 bytes} [Tue Dec  4 05:41:14 2018] GET /demo/welcome.html => generated 24253 bytes in 1 msecs (HTTP/1.1 200) 3 headers in 111 bytes (1 switches on core 0)
Not Found: /frame/static/js/vip_nav.js
[pid: 4074|app: 0|req: 14/108] 218.247.217.98 () {40 vars in 665 bytes} [Tue Dec  4 05:41:14 2018] GET /frame/static/js/vip_nav.js => generated 4584 bytes in 4 msecs (HTTP/1.1 404) 3 headers in 102 bytes (1 switches on core 0)
[pid: 4071|app: 0|req: 13/109] 218.247.217.98 () {40 vars in 647 bytes} [Tue Dec  4 05:41:14 2018] GET /js/index.js => generated 7174 bytes in 1 msecs (HTTP/1.1 200) 3 headers in 110 bytes (1 switches on core 0)
Not Found: /demo/vip_tab.js
[pid: 4072|app: 0|req: 12/110] 218.247.217.98 () {40 vars in 655 bytes} [Tue Dec  4 05:41:14 2018] GET /demo/vip_tab.js => generated 4551 bytes in 4 msecs (HTTP/1.1 404) 3 headers in 102 bytes (1 switches on core 0)
[pid: 4073|app: 0|req: 16/111] 218.247.217.98 () {42 vars in 724 bytes} [Tue Dec  4 05:41:15 2018] GET /index => generated 7174 bytes in 1 msecs (HTTP/1.1 200) 3 headers in 110 bytes (1 switches on core 0)
[pid: 4075|app: 0|req: 15/112] 218.247.217.98 () {42 vars in 764 bytes} [Tue Dec  4 05:41:15 2018] GET /demo/welcome.html => generated 24253 bytes in 1 msecs (HTTP/1.1 200) 3 headers in 111 bytes (1 switches on core 0)
Not Found: /frame/static/js/vip_nav.js
[pid: 4074|app: 0|req: 15/113] 218.247.217.98 () {40 vars in 665 bytes} [Tue Dec  4 05:41:15 2018] GET /frame/static/js/vip_nav.js => generated 4584 bytes in 4 msecs (HTTP/1.1 404) 3 headers in 102 bytes (1 switches on core 0)
[pid: 4071|app: 0|req: 14/114] 218.247.217.98 () {40 vars in 647 bytes} [Tue Dec  4 05:41:15 2018] GET /js/index.js => generated 7174 bytes in 1 msecs (HTTP/1.1 200) 3 headers in 110 bytes (1 switches on core 0)
Not Found: /demo/vip_tab.js
[pid: 4072|app: 0|req: 13/115] 218.247.217.98 () {40 vars in 655 bytes} [Tue Dec  4 05:41:15 2018] GET /demo/vip_tab.js => generated 4551 bytes in 4 msecs (HTTP/1.1 404) 3 headers in 102 bytes (1 switches on core 0)
[pid: 4073|app: 0|req: 17/116] 218.247.217.98 () {42 vars in 764 bytes} [Tue Dec  4 05:41:16 2018] GET /spider/basic.html => generated 12233 bytes in 1 msecs (HTTP/1.1 200) 3 headers in 111 bytes (1 switches on core 0)
[pid: 4075|app: 0|req: 16/117] 218.247.217.98 () {42 vars in 748 bytes} [Tue Dec  4 05:41:16 2018] GET /data/?page=1&limit=30 => generated 11503 bytes in 25 msecs (HTTP/1.1 200) 3 headers in 102 bytes (2 switches on core 0)
[pid: 4074|app: 0|req: 16/118] 218.247.217.98 () {42 vars in 774 bytes} [Tue Dec  4 05:41:17 2018] GET /spider/distribute.html => generated 3960 bytes in 1 msecs (HTTP/1.1 200) 3 headers in 110 bytes (1 switches on core 0)
[pid: 4071|app: 0|req: 15/119] 218.247.217.98 () {42 vars in 767 bytes} [Tue Dec  4 05:41:17 2018] GET /distribute_/?page=1&limit=20 => generated 6707 bytes in 21 msecs (HTTP/1.1 200) 3 headers in 101 bytes (2 switches on core 0)
[pid: 4072|app: 0|req: 14/120] 101.226.225.86 () {46 vars in 1414 bytes} [Tue Dec  4 05:41:47 2018] GET /index?nsukey=Inf5HA52FU2FUEdXAtdiw1Fzgw0bWbV3B2F7KHCw9AtVpVXE7h5KGNg5RY4lhauDcda2Fx1E7kV9rvlggi85kDHNupj2BPBMExWG82FSsPPFkklQQ2L37BchtM5XefAokT0q7fEmvq2WweQwsAsz5DnBH9KnJQ9Fn1ndZ7HbWLvGyEo95tOfrU2BIiHJSCrdrBcbR9QygH0Oh2BM3cmMwldNeojOPA3D3D => generated 7174 bytes in 1 msecs (HTTP/1.1 200) 3 headers in 110 bytes (1 switches on core 0)
[pid: 4073|app: -1|req: -1/121] 61.129.7.254 () {42 vars in 994 bytes} [Tue Dec  4 05:41:47 2018] GET /src/frame/layui/css/layui.css => generated 50971 bytes in 0 msecs via sendfile() (HTTP/1.1 200) 3 headers in 112 bytes (0 switches on core 0)
[pid: 4075|app: -1|req: -1/122] 61.129.8.199 () {42 vars in 996 bytes} [Tue Dec  4 05:41:47 2018] GET /src/frame/static/css/style.css => generated 11288 bytes in 0 msecs via sendfile() (HTTP/1.1 200) 3 headers in 112 bytes (0 switches on core 0)
[pid: 4074|app: 0|req: 17/123] 61.129.8.203 () {42 vars in 1015 bytes} [Tue Dec  4 05:41:47 2018] GET /demo/welcome.html => generated 24253 bytes in 1 msecs (HTTP/1.1 200) 3 headers in 111 bytes (1 switches on core 0)
[pid: 4071|app: -1|req: -1/124] 101.226.225.59 () {42 vars in 985 bytes} [Tue Dec  4 05:41:47 2018] GET /src/frame/static/js/vip_comm.js => generated 9870 bytes in 0 msecs via sendfile() (HTTP/1.1 200) 3 headers in 118 bytes (0 switches on core 0)
[pid: 4072|app: -1|req: -1/125] 61.129.10.43 () {42 vars in 983 bytes} [Tue Dec  4 05:41:47 2018] GET /src/frame/static/image/code.png => generated 2108 bytes in 0 msecs via sendfile() (HTTP/1.1 200) 3 headers in 112 bytes (0 switches on core 0)
[pid: 4073|app: -1|req: -1/126] 61.129.8.250 () {42 vars in 969 bytes} [Tue Dec  4 05:41:47 2018] GET /src/frame/layui/layui.js => generated 5923 bytes in 0 msecs via sendfile() (HTTP/1.1 200) 3 headers in 118 bytes (0 switches on core 0)
[pid: 4075|app: -1|req: -1/127] 61.129.7.254 () {42 vars in 979 bytes} [Tue Dec  4 05:41:47 2018] GET /src/frame/static/image/wx.png => generated 39482 bytes in 0 msecs via sendfile() (HTTP/1.1 200) 3 headers in 113 bytes (0 switches on core 0)
[pid: 4074|app: -1|req: -1/128] 61.151.207.252 () {42 vars in 983 bytes} [Tue Dec  4 05:41:47 2018] GET /src/frame/static/image/zfb.png => generated 25040 bytes in 0 msecs via sendfile() (HTTP/1.1 200) 3 headers in 113 bytes (0 switches on core 0)
[pid: 4072|app: -1|req: -1/129] 101.226.225.59 () {42 vars in 737 bytes} [Tue Dec  4 05:41:47 2018] GET /src/layui/layui.js => generated 9616 bytes in 0 msecs via sendfile() (HTTP/1.1 200) 3 headers in 118 bytes (0 switches on core 0)
[pid: 4071|app: 0|req: 16/130] 61.129.10.43 () {42 vars in 721 bytes} [Tue Dec  4 05:41:47 2018] GET /js/index.js => generated 7174 bytes in 1 msecs (HTTP/1.1 200) 3 headers in 110 bytes (1 switches on core 0)
[pid: 4073|app: -1|req: -1/131] 61.151.180.39 () {42 vars in 764 bytes} [Tue Dec  4 05:41:47 2018] GET /src/frame/echarts/echarts.min.js => generated 577370 bytes in 0 msecs via sendfile() (HTTP/1.1 200) 3 headers in 120 bytes (0 switches on core 0)
[pid: 4074|app: -1|req: -1/132] 61.151.178.167 () {42 vars in 995 bytes} [Tue Dec  4 05:41:48 2018] GET /src/frame/layui/lay/modules/layer.js => generated 21862 bytes in 0 msecs via sendfile() (HTTP/1.1 200) 3 headers in 119 bytes (0 switches on core 0)
[pid: 4075|app: -1|req: -1/133] 61.129.10.43 () {42 vars in 1002 bytes} [Tue Dec  4 05:41:48 2018] GET /src/frame/layui/font/iconfont.svg?v=2.0.0 => generated 205116 bytes in 0 msecs via sendfile() (HTTP/1.1 200) 3 headers in 118 bytes (0 switches on core 0)
[pid: 4072|app: -1|req: -1/134] 61.151.178.167 () {42 vars in 997 bytes} [Tue Dec  4 05:41:49 2018] GET /src/frame/layui/lay/modules/jquery.js => generated 97647 bytes in 0 msecs via sendfile() (HTTP/1.1 200) 3 headers in 119 bytes (0 switches on core 0)
[pid: 4071|app: -1|req: -1/135] 61.151.178.172 () {42 vars in 1055 bytes} [Tue Dec  4 05:41:49 2018] GET /src/frame/layui/css/modules/layer/default/layer.css?v=3.0.3 => generated 14364 bytes in 0 msecs via sendfile() (HTTP/1.1 200) 3 headers in 112 bytes (0 switches on core 0)
[pid: 4073|app: -1|req: -1/136] 61.129.6.148 () {42 vars in 997 bytes} [Tue Dec  4 05:41:50 2018] GET /src/frame/layui/lay/modules/element.js => generated 6959 bytes in 0 msecs via sendfile() (HTTP/1.1 200) 3 headers in 118 bytes (0 switches on core 0)
Not Found: /frame/static/js/vip_nav.js
[pid: 4074|app: 0|req: 18/137] 101.226.225.59 () {42 vars in 975 bytes} [Tue Dec  4 05:41:50 2018] GET /frame/static/js/vip_nav.js => generated 4584 bytes in 4 msecs (HTTP/1.1 404) 3 headers in 102 bytes (1 switches on core 0)
[pid: 4075|app: -1|req: -1/138] 61.129.8.199 () {42 vars in 991 bytes} [Tue Dec  4 05:41:51 2018] GET /src/frame/layui/lay/modules/util.js => generated 1760 bytes in 0 msecs via sendfile() (HTTP/1.1 200) 3 headers in 118 bytes (0 switches on core 0)
[pid: 4072|app: -1|req: -1/139] 101.226.225.86 () {42 vars in 784 bytes} [Tue Dec  4 05:41:52 2018] GET /src/frame/layui/font/iconfont.woff?v=2.0.0 => generated 21680 bytes in 0 msecs via sendfile() (HTTP/1.1 200) 2 headers in 88 bytes (0 switches on core 0)
[pid: 4071|app: -1|req: -1/140] 61.151.178.179 () {42 vars in 765 bytes} [Tue Dec  4 05:41:55 2018] GET /src/layui/lay/modules/element.js => generated 7264 bytes in 0 msecs via sendfile() (HTTP/1.1 200) 3 headers in 118 bytes (0 switches on core 0)
[pid: 4073|app: -1|req: -1/141] 61.129.6.148 () {42 vars in 761 bytes} [Tue Dec  4 05:41:55 2018] GET /src/layui/lay/modules/jquery.js => generated 97648 bytes in 0 msecs via sendfile() (HTTP/1.1 200) 3 headers in 119 bytes (0 switches on core 0)
[pid: 4074|app: -1|req: -1/142] 61.151.207.252 () {42 vars in 759 bytes} [Tue Dec  4 05:41:56 2018] GET /src/layui/lay/modules/form.js => generated 9146 bytes in 0 msecs via sendfile() (HTTP/1.1 200) 3 headers in 118 bytes (0 switches on core 0)
[pid: 4075|app: -1|req: -1/143] 101.226.225.59 () {42 vars in 761 bytes} [Tue Dec  4 05:41:56 2018] GET /src/layui/lay/modules/layer.js => generated 22041 bytes in 0 msecs via sendfile() (HTTP/1.1 200) 3 headers in 119 bytes (0 switches on core 0)
[pid: 4072|app: -1|req: -1/144] 61.151.180.39 () {42 vars in 820 bytes} [Tue Dec  4 05:41:56 2018] GET /src/layui/css/modules/layer/default/layer.css?v=3.1.1 => generated 14425 bytes in 0 msecs via sendfile() (HTTP/1.1 200) 3 headers in 112 bytes (0 switches on core 0)
[pid: 4071|app: -1|req: -1/145] 61.129.8.203 () {42 vars in 759 bytes} [Tue Dec  4 05:41:56 2018] GET /src/layui/lay/modules/table.js => generated 30342 bytes in 0 msecs via sendfile() (HTTP/1.1 200) 3 headers in 119 bytes (0 switches on core 0)
[pid: 4073|app: -1|req: -1/146] 61.129.7.254 () {42 vars in 761 bytes} [Tue Dec  4 05:41:56 2018] GET /src/layui/lay/modules/laytpl.js => generated 1836 bytes in 0 msecs via sendfile() (HTTP/1.1 200) 3 headers in 118 bytes (0 switches on core 0)
[pid: 4074|app: -1|req: -1/147] 61.151.178.176 () {42 vars in 765 bytes} [Tue Dec  4 05:41:56 2018] GET /src/layui/lay/modules/laypage.js => generated 4472 bytes in 0 msecs via sendfile() (HTTP/1.1 200) 3 headers in 118 bytes (0 switches on core 0)
[pid: 4075|app: -1|req: -1/148] 61.151.178.169 () {42 vars in 759 bytes} [Tue Dec  4 05:41:56 2018] GET /src/layui/lay/modules/util.js => generated 3458 bytes in 0 msecs via sendfile() (HTTP/1.1 200) 3 headers in 118 bytes (0 switches on core 0)
Not Found: /demo/vip_tab.js
[pid: 4072|app: 0|req: 15/149] 101.226.225.86 () {42 vars in 731 bytes} [Tue Dec  4 05:41:56 2018] GET /demo/vip_tab.js => generated 4551 bytes in 4 msecs (HTTP/1.1 404) 3 headers in 102 bytes (1 switches on core 0)
[pid: 4071|app: 0|req: 17/150] 218.247.217.98 () {40 vars in 1209 bytes} [Tue Dec  4 05:41:57 2018] GET /index?nsukey=Inf5HA5%2FU%2FUEdXAtdiw1Fzgw0bWbV3B%2F7KHCw9AtVpVXE7h5KGNg5RY4lhauDcda%2Fx1E7kV9rvlggi85kDHNupj%2BPBMExWG8%2FSsPPFkklQQ2L37BchtM5XefAokT0q7fEmvq2WweQwsAsz5DnBH9KnJQ9Fn1ndZ7HbWLvGyEo95tOfrU%2BIiHJSCrdrBcbR9QygH0Oh%2BM3cmMwldNeojOPA%3D%3D => generated 7174 bytes in 1 msecs (HTTP/1.0 200) 3 headers in 110 bytes (1 switches on core 0)
[pid: 4073|app: -1|req: -1/151] 218.247.217.98 () {40 vars in 981 bytes} [Tue Dec  4 05:41:57 2018] GET /src/frame/layui/css/layui.css => generated 50971 bytes in 0 msecs via sendfile() (HTTP/1.1 200) 3 headers in 112 bytes (0 switches on core 0)
[pid: 4074|app: -1|req: -1/152] 218.247.217.98 () {40 vars in 1028 bytes} [Tue Dec  4 05:41:57 2018] GET /src/frame/static/image/code.png => generated 2108 bytes in 0 msecs via sendfile() (HTTP/1.1 200) 3 headers in 112 bytes (0 switches on core 0)
[pid: 4075|app: -1|req: -1/153] 218.247.217.98 () {40 vars in 983 bytes} [Tue Dec  4 05:41:57 2018] GET /src/frame/static/css/style.css => generated 11288 bytes in 0 msecs via sendfile() (HTTP/1.1 200) 3 headers in 112 bytes (0 switches on core 0)
[pid: 4072|app: -1|req: -1/154] 218.247.217.98 () {40 vars in 1026 bytes} [Tue Dec  4 05:41:57 2018] GET /src/frame/static/image/zfb.png => generated 25040 bytes in 0 msecs via sendfile() (HTTP/1.1 200) 3 headers in 113 bytes (0 switches on core 0)
[pid: 4071|app: -1|req: -1/155] 218.247.217.98 () {40 vars in 956 bytes} [Tue Dec  4 05:41:57 2018] GET /src/frame/layui/layui.js => generated 5923 bytes in 0 msecs via sendfile() (HTTP/1.1 200) 3 headers in 118 bytes (0 switches on core 0)
[pid: 4073|app: -1|req: -1/156] 218.247.217.98 () {40 vars in 970 bytes} [Tue Dec  4 05:41:57 2018] GET /src/frame/static/js/vip_comm.js => generated 9870 bytes in 0 msecs via sendfile() (HTTP/1.1 200) 3 headers in 118 bytes (0 switches on core 0)
[pid: 4074|app: -1|req: -1/157] 218.247.217.98 () {40 vars in 1024 bytes} [Tue Dec  4 05:41:57 2018] GET /src/frame/static/image/wx.png => generated 39482 bytes in 0 msecs via sendfile() (HTTP/1.1 200) 3 headers in 113 bytes (0 switches on core 0)
[pid: 4075|app: 0|req: 17/158] 218.247.217.98 () {42 vars in 1037 bytes} [Tue Dec  4 05:41:57 2018] GET /demo/welcome.html => generated 24253 bytes in 1 msecs (HTTP/1.0 200) 3 headers in 111 bytes (1 switches on core 0)
[pid: 4072|app: -1|req: -1/159] 218.247.217.98 () {42 vars in 1035 bytes} [Tue Dec  4 05:41:57 2018] GET /src/frame/layui/lay/modules/layer.js => generated 0 bytes in 0 msecs (HTTP/1.1 304) 0 headers in 29 bytes (0 switches on core 0)
[pid: 4071|app: -1|req: -1/160] 218.247.217.98 () {40 vars in 1040 bytes} [Tue Dec  4 05:41:58 2018] GET /src/frame/layui/css/modules/layer/default/layer.css?v=3.0.3 => generated 14364 bytes in 0 msecs via sendfile() (HTTP/1.1 200) 3 headers in 112 bytes (0 switches on core 0)
[pid: 4073|app: -1|req: -1/161] 218.247.217.98 () {40 vars in 982 bytes} [Tue Dec  4 05:41:58 2018] GET /src/frame/layui/lay/modules/jquery.js => generated 97647 bytes in 0 msecs via sendfile() (HTTP/1.1 200) 3 headers in 119 bytes (0 switches on core 0)
[pid: 4074|app: -1|req: -1/162] 218.247.217.98 () {40 vars in 989 bytes} [Tue Dec  4 05:41:58 2018] GET /src/frame/layui/font/iconfont.svg?v=2.0.0 => generated 205116 bytes in 0 msecs via sendfile() (HTTP/1.0 200) 3 headers in 118 bytes (0 switches on core 0)
[pid: 4075|app: -1|req: -1/163] 218.247.217.98 () {40 vars in 712 bytes} [Tue Dec  4 05:41:58 2018] GET /src/layui/layui.js => generated 9616 bytes in 0 msecs via sendfile() (HTTP/1.1 200) 3 headers in 118 bytes (0 switches on core 0)
[pid: 4072|app: 0|req: 16/164] 218.247.217.98 () {40 vars in 698 bytes} [Tue Dec  4 05:41:58 2018] GET /js/index.js => generated 7174 bytes in 1 msecs (HTTP/1.1 200) 3 headers in 110 bytes (1 switches on core 0)
[pid: 4071|app: -1|req: -1/165] 218.247.217.98 () {42 vars in 795 bytes} [Tue Dec  4 05:41:58 2018] GET /src/frame/echarts/echarts.min.js => generated 0 bytes in 0 msecs (HTTP/1.1 304) 0 headers in 29 bytes (0 switches on core 0)
[pid: 4073|app: -1|req: -1/166] 218.247.217.98 () {42 vars in 795 bytes} [Tue Dec  4 05:41:59 2018] GET /src/layui/lay/modules/element.js => generated 0 bytes in 0 msecs (HTTP/1.1 304) 0 headers in 29 bytes (0 switches on core 0)
[pid: 4074|app: -1|req: -1/167] 218.247.217.98 () {40 vars in 738 bytes} [Tue Dec  4 05:41:59 2018] GET /src/layui/lay/modules/jquery.js => generated 97648 bytes in 0 msecs via sendfile() (HTTP/1.1 200) 3 headers in 119 bytes (0 switches on core 0)
Not Found: /frame/static/js/vip_nav.js
[pid: 4075|app: 0|req: 18/168] 218.247.217.98 () {40 vars in 960 bytes} [Tue Dec  4 05:41:59 2018] GET /frame/static/js/vip_nav.js => generated 4584 bytes in 5 msecs (HTTP/1.1 404) 3 headers in 102 bytes (1 switches on core 0)
[pid: 4072|app: -1|req: -1/169] 218.247.217.98 () {42 vars in 1039 bytes} [Tue Dec  4 05:41:59 2018] GET /src/frame/layui/lay/modules/element.js => generated 0 bytes in 0 msecs (HTTP/1.1 304) 0 headers in 29 bytes (0 switches on core 0)
[pid: 4071|app: -1|req: -1/170] 218.247.217.98 () {40 vars in 978 bytes} [Tue Dec  4 05:41:59 2018] GET /src/frame/layui/lay/modules/util.js => generated 1760 bytes in 0 msecs via sendfile() (HTTP/1.1 200) 3 headers in 118 bytes (0 switches on core 0)
[pid: 4073|app: -1|req: -1/171] 218.247.217.98 () {42 vars in 789 bytes} [Tue Dec  4 05:42:02 2018] GET /src/layui/lay/modules/form.js => generated 0 bytes in 0 msecs (HTTP/1.1 304) 0 headers in 29 bytes (0 switches on core 0)
[pid: 4074|app: -1|req: -1/172] 218.247.217.98 () {40 vars in 991 bytes} [Tue Dec  4 05:42:02 2018] GET /src/frame/layui/font/iconfont.woff?v=2.0.0 => generated 21680 bytes in 0 msecs via sendfile() (HTTP/1.0 200) 2 headers in 88 bytes (0 switches on core 0)
[pid: 4075|app: -1|req: -1/173] 218.247.217.98 () {42 vars in 791 bytes} [Tue Dec  4 05:42:02 2018] GET /src/layui/lay/modules/layer.js => generated 0 bytes in 0 msecs (HTTP/1.1 304) 0 headers in 29 bytes (0 switches on core 0)
[pid: 4072|app: -1|req: -1/174] 218.247.217.98 () {42 vars in 851 bytes} [Tue Dec  4 05:42:02 2018] GET /src/layui/css/modules/layer/default/layer.css?v=3.1.1 => generated 0 bytes in 0 msecs (HTTP/1.1 304) 0 headers in 29 bytes (0 switches on core 0)
[pid: 4071|app: -1|req: -1/175] 218.247.217.98 () {40 vars in 736 bytes} [Tue Dec  4 05:42:02 2018] GET /src/layui/lay/modules/table.js => generated 30342 bytes in 0 msecs via sendfile() (HTTP/1.1 200) 3 headers in 119 bytes (0 switches on core 0)
[pid: 4073|app: -1|req: -1/176] 218.247.217.98 () {40 vars in 738 bytes} [Tue Dec  4 05:42:02 2018] GET /src/layui/lay/modules/laytpl.js => generated 1836 bytes in 0 msecs via sendfile() (HTTP/1.1 200) 3 headers in 118 bytes (0 switches on core 0)
[pid: 4074|app: -1|req: -1/177] 218.247.217.98 () {40 vars in 740 bytes} [Tue Dec  4 05:42:02 2018] GET /src/layui/lay/modules/laypage.js => generated 4472 bytes in 0 msecs via sendfile() (HTTP/1.1 200) 3 headers in 118 bytes (0 switches on core 0)
[pid: 4075|app: -1|req: -1/178] 218.247.217.98 () {40 vars in 734 bytes} [Tue Dec  4 05:42:02 2018] GET /src/layui/lay/modules/util.js => generated 3458 bytes in 0 msecs via sendfile() (HTTP/1.1 200) 3 headers in 118 bytes (0 switches on core 0)
Not Found: /demo/vip_tab.js
[pid: 4072|app: 0|req: 17/179] 218.247.217.98 () {40 vars in 706 bytes} [Tue Dec  4 05:42:02 2018] GET /demo/vip_tab.js => generated 4551 bytes in 4 msecs (HTTP/1.1 404) 3 headers in 102 bytes (1 switches on core 0)
[pid: 4071|app: 0|req: 18/180] 218.247.217.98 () {42 vars in 1033 bytes} [Tue Dec  4 05:42:08 2018] GET /spider/pid.html => generated 3845 bytes in 1 msecs (HTTP/1.0 200) 3 headers in 110 bytes (1 switches on core 0)
[pid: 4073|app: -1|req: -1/181] 218.247.217.98 () {40 vars in 723 bytes} [Tue Dec  4 05:42:08 2018] GET /src/css/layui.css => generated 69092 bytes in 0 msecs via sendfile() (HTTP/1.1 200) 3 headers in 112 bytes (0 switches on core 0)
[pid: 4074|app: -1|req: -1/182] 218.247.217.98 () {40 vars in 718 bytes} [Tue Dec  4 05:42:08 2018] GET /src/lib/layui/layui.js => generated 6542 bytes in 0 msecs via sendfile() (HTTP/1.1 200) 3 headers in 118 bytes (0 switches on core 0)
[pid: 4075|app: -1|req: -1/183] 218.247.217.98 () {40 vars in 742 bytes} [Tue Dec  4 05:42:08 2018] GET /src/lib/layui/lay/modules/table.js => generated 20828 bytes in 0 msecs via sendfile() (HTTP/1.1 200) 3 headers in 119 bytes (0 switches on core 0)
[pid: 4072|app: -1|req: -1/184] 218.247.217.98 () {40 vars in 744 bytes} [Tue Dec  4 05:42:08 2018] GET /src/lib/layui/lay/modules/laytpl.js => generated 1836 bytes in 0 msecs via sendfile() (HTTP/1.1 200) 3 headers in 118 bytes (0 switches on core 0)
[pid: 4071|app: -1|req: -1/185] 218.247.217.98 () {40 vars in 746 bytes} [Tue Dec  4 05:42:08 2018] GET /src/lib/layui/lay/modules/laypage.js => generated 4319 bytes in 0 msecs via sendfile() (HTTP/1.1 200) 3 headers in 118 bytes (0 switches on core 0)
[pid: 4073|app: -1|req: -1/186] 218.247.217.98 () {40 vars in 742 bytes} [Tue Dec  4 05:42:08 2018] GET /src/lib/layui/lay/modules/layer.js => generated 22063 bytes in 0 msecs via sendfile() (HTTP/1.1 200) 3 headers in 119 bytes (0 switches on core 0)
[pid: 4074|app: -1|req: -1/187] 218.247.217.98 () {40 vars in 802 bytes} [Tue Dec  4 05:42:08 2018] GET /src/lib/layui/css/modules/layer/default/layer.css?v=3.1.1 => generated 14425 bytes in 0 msecs via sendfile() (HTTP/1.1 200) 3 headers in 112 bytes (0 switches on core 0)
[pid: 4075|app: -1|req: -1/188] 218.247.217.98 () {40 vars in 744 bytes} [Tue Dec  4 05:42:08 2018] GET /src/lib/layui/lay/modules/jquery.js => generated 97648 bytes in 0 msecs via sendfile() (HTTP/1.1 200) 3 headers in 119 bytes (0 switches on core 0)
[pid: 4072|app: -1|req: -1/189] 218.247.217.98 () {40 vars in 740 bytes} [Tue Dec  4 05:42:08 2018] GET /src/lib/layui/lay/modules/form.js => generated 7925 bytes in 0 msecs via sendfile() (HTTP/1.1 200) 3 headers in 118 bytes (0 switches on core 0)
[pid: 4071|app: 0|req: 19/190] 218.247.217.98 () {42 vars in 797 bytes} [Tue Dec  4 05:42:09 2018] GET /pid_/?page=1&limit=16 => generated 3350 bytes in 25 msecs (HTTP/1.1 200) 3 headers in 101 bytes (2 switches on core 0)
[pid: 4073|app: -1|req: -1/191] 218.247.217.98 () {42 vars in 782 bytes} [Tue Dec  4 05:42:09 2018] GET /src/font/iconfont.svg?v=230 => generated 0 bytes in 0 msecs (HTTP/1.0 304) 0 headers in 29 bytes (0 switches on core 0)
[pid: 4074|app: -1|req: -1/192] 218.247.217.98 () {40 vars in 729 bytes} [Tue Dec  4 05:42:09 2018] GET /src/font/iconfont.woff?v=230 => generated 26328 bytes in 0 msecs via sendfile() (HTTP/1.0 200) 2 headers in 88 bytes (0 switches on core 0)
[pid: 4075|app: 0|req: 19/193] 218.247.217.98 () {42 vars in 1037 bytes} [Tue Dec  4 05:42:11 2018] GET /spider/basic.html => generated 12233 bytes in 1 msecs (HTTP/1.0 200) 3 headers in 111 bytes (1 switches on core 0)
[pid: 4072|app: -1|req: -1/194] 218.247.217.98 () {40 vars in 700 bytes} [Tue Dec  4 05:42:12 2018] GET /src/layui.js => generated 15036 bytes in 0 msecs via sendfile() (HTTP/1.1 200) 3 headers in 119 bytes (0 switches on core 0)
[pid: 4071|app: -1|req: -1/195] 218.247.217.98 () {42 vars in 771 bytes} [Tue Dec  4 05:42:12 2018] GET /src/jquery-latest.js => generated 0 bytes in 0 msecs (HTTP/1.1 304) 0 headers in 29 bytes (0 switches on core 0)
[pid: 4073|app: -1|req: -1/196] 218.247.217.98 () {42 vars in 779 bytes} [Tue Dec  4 05:42:12 2018] GET /src/lay/modules/table.js => generated 0 bytes in 0 msecs (HTTP/1.1 304) 0 headers in 29 bytes (0 switches on core 0)
[pid: 4074|app: -1|req: -1/197] 218.247.217.98 () {42 vars in 781 bytes} [Tue Dec  4 05:42:12 2018] GET /src/lay/modules/laytpl.js => generated 0 bytes in 0 msecs (HTTP/1.1 304) 0 headers in 29 bytes (0 switches on core 0)
[pid: 4075|app: -1|req: -1/198] 218.247.217.98 () {40 vars in 728 bytes} [Tue Dec  4 05:42:12 2018] GET /src/lay/modules/laypage.js => generated 9151 bytes in 0 msecs via sendfile() (HTTP/1.1 200) 3 headers in 118 bytes (0 switches on core 0)
[pid: 4072|app: -1|req: -1/199] 218.247.217.98 () {42 vars in 779 bytes} [Tue Dec  4 05:42:12 2018] GET /src/lay/modules/layer.js => generated 0 bytes in 0 msecs (HTTP/1.1 304) 0 headers in 29 bytes (0 switches on core 0)
[pid: 4071|app: -1|req: -1/200] 218.247.217.98 () {40 vars in 722 bytes} [Tue Dec  4 05:42:12 2018] GET /src/lay/modules/form.js => generated 22243 bytes in 0 msecs via sendfile() (HTTP/1.1 200) 3 headers in 119 bytes (0 switches on core 0)
[pid: 4073|app: -1|req: -1/201] 218.247.217.98 () {42 vars in 839 bytes} [Tue Dec  4 05:42:12 2018] GET /src/css/modules/layer/default/layer.css?v=3.1.1 => generated 0 bytes in 0 msecs (HTTP/1.1 304) 0 headers in 29 bytes (0 switches on core 0)
[pid: 4074|app: 0|req: 19/202] 218.247.217.98 () {42 vars in 799 bytes} [Tue Dec  4 05:42:12 2018] GET /data/?page=1&limit=30 => generated 11503 bytes in 23 msecs (HTTP/1.1 200) 3 headers in 102 bytes (2 switches on core 0)
[pid: 4075|app: 0|req: 20/203] 101.89.29.97 () {36 vars in 676 bytes} [Tue Dec  4 05:42:43 2018] GET /index => generated 7174 bytes in 1 msecs (HTTP/1.1 200) 3 headers in 110 bytes (1 switches on core 0)
[pid: 4072|app: 0|req: 18/204] 101.89.29.97 () {38 vars in 747 bytes} [Tue Dec  4 05:42:43 2018] GET /demo/welcome.html => generated 24253 bytes in 1 msecs (HTTP/1.1 200) 3 headers in 111 bytes (1 switches on core 0)
[pid: 4071|app: -1|req: -1/205] 101.89.29.97 () {38 vars in 688 bytes} [Tue Dec  4 05:42:43 2018] GET /src/frame/layui/layui.js => generated 5923 bytes in 0 msecs via sendfile() (HTTP/1.1 200) 3 headers in 118 bytes (0 switches on core 0)
[pid: 4073|app: -1|req: -1/206] 101.89.29.97 () {38 vars in 749 bytes} [Tue Dec  4 05:42:43 2018] GET /src/frame/static/js/vip_comm.js => generated 9870 bytes in 0 msecs via sendfile() (HTTP/1.1 200) 3 headers in 118 bytes (0 switches on core 0)
[pid: 4074|app: -1|req: -1/207] 101.89.29.97 () {38 vars in 779 bytes} [Tue Dec  4 05:42:44 2018] GET /src/layui/layui.js => generated 9616 bytes in 0 msecs via sendfile() (HTTP/1.1 200) 3 headers in 118 bytes (0 switches on core 0)
[pid: 4075|app: 0|req: 21/208] 101.89.29.97 () {38 vars in 677 bytes} [Tue Dec  4 05:42:45 2018] GET /js/index.js => generated 7174 bytes in 1 msecs (HTTP/1.1 200) 3 headers in 110 bytes (1 switches on core 0)
[pid: 4072|app: -1|req: -1/209] 101.89.29.97 () {38 vars in 719 bytes} [Tue Dec  4 05:42:45 2018] GET /src/frame/echarts/echarts.min.js => generated 577370 bytes in 0 msecs via sendfile() (HTTP/1.1 200) 3 headers in 120 bytes (0 switches on core 0)
[pid: 4071|app: 0|req: 20/210] 101.89.239.230 () {36 vars in 1095 bytes} [Tue Dec  4 05:42:47 2018] GET /index?nsukey=Inf5HA5%2FU%2FUEdXAtdiw1Fzgw0bWbV3B%2F7KHCw9AtVpVXE7h5KGNg5RY4lhauDcda%2Fx1E7kV9rvlggi85kDHNupj%2BPBMExWG8%2FSsPPFkklQQ2L37BchtM5XefAokT0q7fEmvq2WweQwsAsz5DnBH9KnJQ9Fn1ndZ7HbWLvGyEo95tOfrU%2BIiHJSCrdrBcbR9QygH0Oh%2BM3cmMwldNeojOPA%3D%3D => generated 7174 bytes in 1 msecs (HTTP/1.1 200) 3 headers in 110 bytes (1 switches on core 0)
[pid: 4073|app: 0|req: 18/211] 101.89.239.230 () {38 vars in 923 bytes} [Tue Dec  4 05:42:47 2018] GET /demo/welcome.html => generated 24253 bytes in 1 msecs (HTTP/1.1 200) 3 headers in 111 bytes (1 switches on core 0)
[pid: 4074|app: -1|req: -1/212] 101.89.239.230 () {38 vars in 981 bytes} [Tue Dec  4 05:42:47 2018] GET /src/frame/layui/layui.js => generated 5923 bytes in 0 msecs via sendfile() (HTTP/1.1 200) 3 headers in 118 bytes (0 switches on core 0)
[pid: 4075|app: -1|req: -1/213] 101.89.239.230 () {38 vars in 997 bytes} [Tue Dec  4 05:42:47 2018] GET /src/frame/static/js/vip_comm.js => generated 9870 bytes in 0 msecs via sendfile() (HTTP/1.1 200) 3 headers in 118 bytes (0 switches on core 0)
[pid: 4072|app: -1|req: -1/214] 101.89.239.230 () {38 vars in 693 bytes} [Tue Dec  4 05:42:47 2018] GET /src/layui/layui.js => generated 9616 bytes in 0 msecs via sendfile() (HTTP/1.1 200) 3 headers in 118 bytes (0 switches on core 0)
[pid: 4071|app: 0|req: 21/215] 101.89.239.230 () {38 vars in 679 bytes} [Tue Dec  4 05:42:47 2018] GET /js/index.js => generated 7174 bytes in 1 msecs (HTTP/1.1 200) 3 headers in 110 bytes (1 switches on core 0)
[pid: 4073|app: -1|req: -1/216] 101.89.239.230 () {38 vars in 721 bytes} [Tue Dec  4 05:42:48 2018] GET /src/frame/echarts/echarts.min.js => generated 577370 bytes in 0 msecs via sendfile() (HTTP/1.1 200) 3 headers in 120 bytes (0 switches on core 0)
[pid: 4074|app: 0|req: 20/217] 218.247.217.98 () {42 vars in 724 bytes} [Tue Dec  4 06:00:25 2018] GET /index => generated 7174 bytes in 1 msecs (HTTP/1.1 200) 3 headers in 110 bytes (1 switches on core 0)
[pid: 4075|app: -1|req: -1/218] 218.247.217.98 () {42 vars in 716 bytes} [Tue Dec  4 06:00:25 2018] GET /src/frame/layui/layui.js => generated 0 bytes in 0 msecs (HTTP/1.1 304) 0 headers in 29 bytes (0 switches on core 0)
[pid: 4072|app: -1|req: -1/219] 218.247.217.98 () {42 vars in 730 bytes} [Tue Dec  4 06:00:25 2018] GET /src/frame/static/js/vip_comm.js => generated 0 bytes in 0 msecs (HTTP/1.1 304) 0 headers in 29 bytes (0 switches on core 0)
[pid: 4071|app: -1|req: -1/220] 218.247.217.98 () {42 vars in 766 bytes} [Tue Dec  4 06:00:25 2018] GET /src/frame/static/image/code.png => generated 0 bytes in 0 msecs (HTTP/1.1 304) 0 headers in 29 bytes (0 switches on core 0)
[pid: 4073|app: -1|req: -1/221] 218.247.217.98 () {42 vars in 764 bytes} [Tue Dec  4 06:00:25 2018] GET /src/frame/static/image/zfb.png => generated 0 bytes in 0 msecs (HTTP/1.1 304) 0 headers in 29 bytes (0 switches on core 0)
[pid: 4074|app: -1|req: -1/222] 218.247.217.98 () {42 vars in 762 bytes} [Tue Dec  4 06:00:25 2018] GET /src/frame/static/image/wx.png => generated 0 bytes in 0 msecs (HTTP/1.1 304) 0 headers in 29 bytes (0 switches on core 0)
[pid: 4075|app: 0|req: 22/223] 218.247.217.98 () {42 vars in 764 bytes} [Tue Dec  4 06:00:25 2018] GET /demo/welcome.html => generated 24253 bytes in 1 msecs (HTTP/1.1 200) 3 headers in 111 bytes (1 switches on core 0)
[pid: 4072|app: -1|req: -1/224] 218.247.217.98 () {44 vars in 815 bytes} [Tue Dec  4 06:00:25 2018] GET /src/frame/layui/font/iconfont.woff?v=2.0.0 => generated 0 bytes in 0 msecs (HTTP/1.1 304) 0 headers in 29 bytes (0 switches on core 0)
Not Found: /frame/static/js/vip_nav.js
[pid: 4071|app: 0|req: 22/225] 218.247.217.98 () {40 vars in 665 bytes} [Tue Dec  4 06:00:26 2018] GET /frame/static/js/vip_nav.js => generated 4584 bytes in 4 msecs (HTTP/1.1 404) 3 headers in 102 bytes (1 switches on core 0)
[pid: 4073|app: -1|req: -1/226] 218.247.217.98 () {42 vars in 716 bytes} [Tue Dec  4 06:00:26 2018] GET /src/layui/layui.js => generated 0 bytes in 0 msecs (HTTP/1.1 304) 0 headers in 29 bytes (0 switches on core 0)
[pid: 4074|app: 0|req: 21/227] 218.247.217.98 () {40 vars in 647 bytes} [Tue Dec  4 06:00:26 2018] GET /js/index.js => generated 7174 bytes in 1 msecs (HTTP/1.1 200) 3 headers in 110 bytes (1 switches on core 0)
[pid: 4075|app: -1|req: -1/228] 218.247.217.98 () {42 vars in 744 bytes} [Tue Dec  4 06:00:26 2018] GET /src/frame/echarts/echarts.min.js => generated 0 bytes in 0 msecs (HTTP/1.1 304) 0 headers in 29 bytes (0 switches on core 0)
Not Found: /demo/vip_tab.js
[pid: 4072|app: 0|req: 19/229] 218.247.217.98 () {40 vars in 655 bytes} [Tue Dec  4 06:00:26 2018] GET /demo/vip_tab.js => generated 4551 bytes in 4 msecs (HTTP/1.1 404) 3 headers in 102 bytes (1 switches on core 0)
[pid: 4071|app: 0|req: 23/230] 218.247.217.98 () {42 vars in 724 bytes} [Tue Dec  4 06:12:41 2018] GET /index => generated 7174 bytes in 1 msecs (HTTP/1.1 200) 3 headers in 110 bytes (1 switches on core 0)
[pid: 4073|app: 0|req: 19/231] 218.247.217.98 () {42 vars in 764 bytes} [Tue Dec  4 06:12:41 2018] GET /demo/welcome.html => generated 24253 bytes in 1 msecs (HTTP/1.1 200) 3 headers in 111 bytes (1 switches on core 0)
[pid: 4074|app: 0|req: 22/232] 218.247.217.98 () {40 vars in 647 bytes} [Tue Dec  4 06:12:41 2018] GET /js/index.js => generated 7174 bytes in 1 msecs (HTTP/1.1 200) 3 headers in 110 bytes (1 switches on core 0)
Not Found: /frame/static/js/vip_nav.js
[pid: 4075|app: 0|req: 23/233] 218.247.217.98 () {40 vars in 665 bytes} [Tue Dec  4 06:12:41 2018] GET /frame/static/js/vip_nav.js => generated 4584 bytes in 4 msecs (HTTP/1.1 404) 3 headers in 102 bytes (1 switches on core 0)
Not Found: /demo/vip_tab.js
[pid: 4072|app: 0|req: 20/234] 218.247.217.98 () {40 vars in 655 bytes} [Tue Dec  4 06:12:41 2018] GET /demo/vip_tab.js => generated 4551 bytes in 4 msecs (HTTP/1.1 404) 3 headers in 102 bytes (1 switches on core 0)
[pid: 4071|app: 0|req: 24/235] 218.247.217.98 () {42 vars in 764 bytes} [Tue Dec  4 06:12:42 2018] GET /spider/basic.html => generated 12233 bytes in 1 msecs (HTTP/1.1 200) 3 headers in 111 bytes (1 switches on core 0)
[pid: 4073|app: 0|req: 20/236] 218.247.217.98 () {42 vars in 748 bytes} [Tue Dec  4 06:12:42 2018] GET /data/?page=1&limit=30 => generated 11502 bytes in 16 msecs (HTTP/1.1 200) 3 headers in 102 bytes (2 switches on core 0)
Not Found: /404/search_children.js
[pid: 4074|app: 0|req: 23/237] 120.132.3.65 () {34 vars in 514 bytes} [Tue Dec  4 06:19:10 2018] GET /404/search_children.js => generated 4564 bytes in 4 msecs (HTTP/1.1 404) 3 headers in 102 bytes (1 switches on core 0)
Not Found: /
[pid: 4075|app: 0|req: 24/238] 218.247.217.98 () {42 vars in 714 bytes} [Tue Dec  4 06:42:40 2018] GET / => generated 4488 bytes in 4 msecs (HTTP/1.1 404) 3 headers in 102 bytes (1 switches on core 0)
[pid: 4072|app: 0|req: 21/239] 218.247.217.98 () {42 vars in 717 bytes} [Tue Dec  4 06:42:45 2018] GET /index => generated 7174 bytes in 1 msecs (HTTP/1.1 200) 3 headers in 110 bytes (1 switches on core 0)
[pid: 4071|app: 0|req: 25/240] 218.247.217.98 () {42 vars in 764 bytes} [Tue Dec  4 06:42:46 2018] GET /demo/welcome.html => generated 24253 bytes in 1 msecs (HTTP/1.1 200) 3 headers in 111 bytes (1 switches on core 0)
[pid: 4073|app: 0|req: 21/241] 218.247.217.98 () {40 vars in 647 bytes} [Tue Dec  4 06:42:46 2018] GET /js/index.js => generated 7174 bytes in 1 msecs (HTTP/1.1 200) 3 headers in 110 bytes (1 switches on core 0)
Not Found: /frame/static/js/vip_nav.js
[pid: 4074|app: 0|req: 24/242] 218.247.217.98 () {40 vars in 665 bytes} [Tue Dec  4 06:42:46 2018] GET /frame/static/js/vip_nav.js => generated 4584 bytes in 4 msecs (HTTP/1.1 404) 3 headers in 102 bytes (1 switches on core 0)
Not Found: /demo/vip_tab.js
[pid: 4075|app: 0|req: 25/243] 218.247.217.98 () {40 vars in 655 bytes} [Tue Dec  4 06:42:47 2018] GET /demo/vip_tab.js => generated 4551 bytes in 4 msecs (HTTP/1.1 404) 3 headers in 102 bytes (1 switches on core 0)
Not Found: /demo/vip_tab.js
[pid: 4072|app: 0|req: 22/244] 218.247.217.98 () {40 vars in 655 bytes} [Tue Dec  4 08:18:57 2018] GET /demo/vip_tab.js => generated 4551 bytes in 4 msecs (HTTP/1.1 404) 3 headers in 102 bytes (1 switches on core 0)
[pid: 4071|app: 0|req: 26/245] 218.247.217.98 () {42 vars in 724 bytes} [Tue Dec  4 08:18:58 2018] GET /index => generated 7174 bytes in 1 msecs (HTTP/1.1 200) 3 headers in 110 bytes (1 switches on core 0)
[pid: 4073|app: 0|req: 22/246] 218.247.217.98 () {42 vars in 764 bytes} [Tue Dec  4 08:18:58 2018] GET /demo/welcome.html => generated 24253 bytes in 1 msecs (HTTP/1.1 200) 3 headers in 111 bytes (1 switches on core 0)
[pid: 4074|app: 0|req: 25/247] 218.247.217.98 () {40 vars in 647 bytes} [Tue Dec  4 08:18:58 2018] GET /js/index.js => generated 7174 bytes in 1 msecs (HTTP/1.1 200) 3 headers in 110 bytes (1 switches on core 0)
Not Found: /frame/static/js/vip_nav.js
[pid: 4075|app: 0|req: 26/248] 218.247.217.98 () {40 vars in 665 bytes} [Tue Dec  4 08:18:58 2018] GET /frame/static/js/vip_nav.js => generated 4584 bytes in 4 msecs (HTTP/1.1 404) 3 headers in 102 bytes (1 switches on core 0)
Not Found: /demo/vip_tab.js
[pid: 4072|app: 0|req: 23/249] 218.247.217.98 () {40 vars in 655 bytes} [Tue Dec  4 08:18:58 2018] GET /demo/vip_tab.js => generated 4551 bytes in 4 msecs (HTTP/1.1 404) 3 headers in 102 bytes (1 switches on core 0)
[pid: 4071|app: 0|req: 27/250] 218.247.217.98 () {42 vars in 764 bytes} [Tue Dec  4 08:18:59 2018] GET /spider/basic.html => generated 12233 bytes in 1 msecs (HTTP/1.1 200) 3 headers in 111 bytes (1 switches on core 0)
[pid: 4073|app: 0|req: 23/251] 218.247.217.98 () {42 vars in 748 bytes} [Tue Dec  4 08:18:59 2018] GET /data/?page=1&limit=30 => generated 11502 bytes in 19 msecs (HTTP/1.1 200) 3 headers in 102 bytes (2 switches on core 0)
[pid: 4074|app: 0|req: 26/252] 218.247.217.98 () {42 vars in 724 bytes} [Tue Dec  4 08:19:01 2018] GET /index => generated 7174 bytes in 1 msecs (HTTP/1.1 200) 3 headers in 110 bytes (1 switches on core 0)
[pid: 4075|app: 0|req: 27/253] 218.247.217.98 () {42 vars in 764 bytes} [Tue Dec  4 08:19:01 2018] GET /demo/welcome.html => generated 24253 bytes in 1 msecs (HTTP/1.1 200) 3 headers in 111 bytes (1 switches on core 0)
[pid: 4072|app: 0|req: 24/254] 218.247.217.98 () {40 vars in 647 bytes} [Tue Dec  4 08:19:01 2018] GET /js/index.js => generated 7174 bytes in 1 msecs (HTTP/1.1 200) 3 headers in 110 bytes (1 switches on core 0)
Not Found: /frame/static/js/vip_nav.js
[pid: 4071|app: 0|req: 28/255] 218.247.217.98 () {40 vars in 665 bytes} [Tue Dec  4 08:19:01 2018] GET /frame/static/js/vip_nav.js => generated 4584 bytes in 4 msecs (HTTP/1.1 404) 3 headers in 102 bytes (1 switches on core 0)
Not Found: /demo/vip_tab.js
[pid: 4073|app: 0|req: 24/256] 218.247.217.98 () {40 vars in 655 bytes} [Tue Dec  4 08:19:01 2018] GET /demo/vip_tab.js => generated 4551 bytes in 4 msecs (HTTP/1.1 404) 3 headers in 102 bytes (1 switches on core 0)
[pid: 4074|app: 0|req: 27/257] 218.247.217.98 () {42 vars in 774 bytes} [Tue Dec  4 08:19:02 2018] GET /spider/distribute.html => generated 3960 bytes in 1 msecs (HTTP/1.1 200) 3 headers in 110 bytes (1 switches on core 0)
[pid: 4075|app: 0|req: 28/258] 218.247.217.98 () {42 vars in 767 bytes} [Tue Dec  4 08:19:03 2018] GET /distribute_/?page=1&limit=20 => generated 6706 bytes in 29 msecs (HTTP/1.1 200) 3 headers in 101 bytes (2 switches on core 0)
[pid: 4072|app: 0|req: 25/259] 218.247.217.98 () {42 vars in 764 bytes} [Tue Dec  4 08:19:26 2018] GET /spider/basic.html => generated 12233 bytes in 1 msecs (HTTP/1.1 200) 3 headers in 111 bytes (1 switches on core 0)
[pid: 4071|app: 0|req: 29/260] 218.247.217.98 () {42 vars in 748 bytes} [Tue Dec  4 08:19:27 2018] GET /data/?page=1&limit=30 => generated 11502 bytes in 25 msecs (HTTP/1.1 200) 3 headers in 102 bytes (2 switches on core 0)
[pid: 4073|app: 0|req: 25/261] 218.247.217.98 () {42 vars in 724 bytes} [Tue Dec  4 08:49:02 2018] GET /index => generated 7174 bytes in 1 msecs (HTTP/1.1 200) 3 headers in 110 bytes (1 switches on core 0)
[pid: 4074|app: 0|req: 28/262] 218.247.217.98 () {42 vars in 764 bytes} [Tue Dec  4 08:49:02 2018] GET /demo/welcome.html => generated 24253 bytes in 1 msecs (HTTP/1.1 200) 3 headers in 111 bytes (1 switches on core 0)
[pid: 4075|app: 0|req: 29/263] 218.247.217.98 () {40 vars in 647 bytes} [Tue Dec  4 08:49:02 2018] GET /js/index.js => generated 7174 bytes in 1 msecs (HTTP/1.1 200) 3 headers in 110 bytes (1 switches on core 0)
Not Found: /frame/static/js/vip_nav.js
[pid: 4072|app: 0|req: 26/264] 218.247.217.98 () {40 vars in 665 bytes} [Tue Dec  4 08:49:02 2018] GET /frame/static/js/vip_nav.js => generated 4584 bytes in 4 msecs (HTTP/1.1 404) 3 headers in 102 bytes (1 switches on core 0)
Not Found: /demo/vip_tab.js
[pid: 4071|app: 0|req: 30/265] 218.247.217.98 () {40 vars in 655 bytes} [Tue Dec  4 08:49:02 2018] GET /demo/vip_tab.js => generated 4551 bytes in 4 msecs (HTTP/1.1 404) 3 headers in 102 bytes (1 switches on core 0)
[pid: 4073|app: 0|req: 26/266] 218.247.217.98 () {42 vars in 764 bytes} [Tue Dec  4 08:49:03 2018] GET /spider/basic.html => generated 12237 bytes in 1 msecs (HTTP/1.1 200) 3 headers in 111 bytes (1 switches on core 0)
[pid: 4074|app: 0|req: 29/267] 218.247.217.98 () {42 vars in 748 bytes} [Tue Dec  4 08:49:03 2018] GET /data/?page=1&limit=30 => generated 11502 bytes in 22 msecs (HTTP/1.1 200) 3 headers in 102 bytes (2 switches on core 0)
[pid: 4075|app: 0|req: 30/268] 218.247.217.98 () {42 vars in 724 bytes} [Tue Dec  4 08:50:06 2018] GET /index => generated 7174 bytes in 1 msecs (HTTP/1.1 200) 3 headers in 110 bytes (1 switches on core 0)
[pid: 4072|app: 0|req: 27/269] 218.247.217.98 () {42 vars in 764 bytes} [Tue Dec  4 08:50:06 2018] GET /demo/welcome.html => generated 24253 bytes in 1 msecs (HTTP/1.1 200) 3 headers in 111 bytes (1 switches on core 0)
[pid: 4071|app: 0|req: 31/270] 218.247.217.98 () {40 vars in 647 bytes} [Tue Dec  4 08:50:06 2018] GET /js/index.js => generated 7174 bytes in 1 msecs (HTTP/1.1 200) 3 headers in 110 bytes (1 switches on core 0)
Not Found: /frame/static/js/vip_nav.js
[pid: 4073|app: 0|req: 27/271] 218.247.217.98 () {40 vars in 665 bytes} [Tue Dec  4 08:50:06 2018] GET /frame/static/js/vip_nav.js => generated 4584 bytes in 4 msecs (HTTP/1.1 404) 3 headers in 102 bytes (1 switches on core 0)
Not Found: /demo/vip_tab.js
[pid: 4074|app: 0|req: 30/272] 218.247.217.98 () {40 vars in 655 bytes} [Tue Dec  4 08:50:06 2018] GET /demo/vip_tab.js => generated 4551 bytes in 4 msecs (HTTP/1.1 404) 3 headers in 102 bytes (1 switches on core 0)
[pid: 4075|app: 0|req: 31/273] 218.247.217.98 () {42 vars in 764 bytes} [Tue Dec  4 08:50:08 2018] GET /spider/basic.html => generated 12237 bytes in 1 msecs (HTTP/1.1 200) 3 headers in 111 bytes (1 switches on core 0)
[pid: 4072|app: 0|req: 28/274] 218.247.217.98 () {42 vars in 748 bytes} [Tue Dec  4 08:50:08 2018] GET /data/?page=1&limit=30 => generated 11502 bytes in 29 msecs (HTTP/1.1 200) 3 headers in 102 bytes (2 switches on core 0)
[pid: 4071|app: 0|req: 32/275] 218.247.217.98 () {42 vars in 724 bytes} [Tue Dec  4 08:50:14 2018] GET /index => generated 7174 bytes in 1 msecs (HTTP/1.1 200) 3 headers in 110 bytes (1 switches on core 0)
[pid: 4073|app: 0|req: 28/276] 218.247.217.98 () {42 vars in 764 bytes} [Tue Dec  4 08:50:14 2018] GET /demo/welcome.html => generated 24253 bytes in 1 msecs (HTTP/1.1 200) 3 headers in 111 bytes (1 switches on core 0)
[pid: 4074|app: 0|req: 31/277] 218.247.217.98 () {40 vars in 647 bytes} [Tue Dec  4 08:50:14 2018] GET /js/index.js => generated 7174 bytes in 1 msecs (HTTP/1.1 200) 3 headers in 110 bytes (1 switches on core 0)
Not Found: /frame/static/js/vip_nav.js
[pid: 4075|app: 0|req: 32/278] 218.247.217.98 () {40 vars in 665 bytes} [Tue Dec  4 08:50:14 2018] GET /frame/static/js/vip_nav.js => generated 4584 bytes in 4 msecs (HTTP/1.1 404) 3 headers in 102 bytes (1 switches on core 0)
Not Found: /demo/vip_tab.js
[pid: 4072|app: 0|req: 29/279] 218.247.217.98 () {40 vars in 655 bytes} [Tue Dec  4 08:50:14 2018] GET /demo/vip_tab.js => generated 4551 bytes in 4 msecs (HTTP/1.1 404) 3 headers in 102 bytes (1 switches on core 0)
[pid: 4071|app: 0|req: 33/280] 218.247.217.98 () {42 vars in 724 bytes} [Tue Dec  4 08:50:15 2018] GET /index => generated 7174 bytes in 1 msecs (HTTP/1.1 200) 3 headers in 110 bytes (1 switches on core 0)
[pid: 4073|app: 0|req: 29/281] 218.247.217.98 () {42 vars in 764 bytes} [Tue Dec  4 08:50:15 2018] GET /demo/welcome.html => generated 24253 bytes in 1 msecs (HTTP/1.1 200) 3 headers in 111 bytes (1 switches on core 0)
[pid: 4074|app: 0|req: 32/282] 218.247.217.98 () {40 vars in 647 bytes} [Tue Dec  4 08:50:15 2018] GET /js/index.js => generated 7174 bytes in 1 msecs (HTTP/1.1 200) 3 headers in 110 bytes (1 switches on core 0)
Not Found: /frame/static/js/vip_nav.js
[pid: 4075|app: 0|req: 33/283] 218.247.217.98 () {40 vars in 665 bytes} [Tue Dec  4 08:50:15 2018] GET /frame/static/js/vip_nav.js => generated 4584 bytes in 4 msecs (HTTP/1.1 404) 3 headers in 102 bytes (1 switches on core 0)
Not Found: /demo/vip_tab.js
[pid: 4072|app: 0|req: 30/284] 218.247.217.98 () {40 vars in 655 bytes} [Tue Dec  4 08:50:15 2018] GET /demo/vip_tab.js => generated 4551 bytes in 4 msecs (HTTP/1.1 404) 3 headers in 102 bytes (1 switches on core 0)
[pid: 4071|app: 0|req: 34/285] 218.247.217.98 () {42 vars in 724 bytes} [Tue Dec  4 08:50:15 2018] GET /index => generated 7174 bytes in 1 msecs (HTTP/1.1 200) 3 headers in 110 bytes (1 switches on core 0)
[pid: 4073|app: 0|req: 30/286] 218.247.217.98 () {42 vars in 764 bytes} [Tue Dec  4 08:50:15 2018] GET /demo/welcome.html => generated 24253 bytes in 1 msecs (HTTP/1.1 200) 3 headers in 111 bytes (1 switches on core 0)
[pid: 4074|app: 0|req: 33/287] 218.247.217.98 () {40 vars in 647 bytes} [Tue Dec  4 08:50:16 2018] GET /js/index.js => generated 7174 bytes in 1 msecs (HTTP/1.1 200) 3 headers in 110 bytes (1 switches on core 0)
Not Found: /frame/static/js/vip_nav.js
[pid: 4075|app: 0|req: 34/288] 218.247.217.98 () {40 vars in 665 bytes} [Tue Dec  4 08:50:16 2018] GET /frame/static/js/vip_nav.js => generated 4584 bytes in 4 msecs (HTTP/1.1 404) 3 headers in 102 bytes (1 switches on core 0)
Not Found: /demo/vip_tab.js
[pid: 4072|app: 0|req: 31/289] 218.247.217.98 () {40 vars in 655 bytes} [Tue Dec  4 08:50:16 2018] GET /demo/vip_tab.js => generated 4551 bytes in 4 msecs (HTTP/1.1 404) 3 headers in 102 bytes (1 switches on core 0)
[pid: 4071|app: 0|req: 35/290] 218.247.217.98 () {42 vars in 764 bytes} [Tue Dec  4 08:50:16 2018] GET /spider/basic.html => generated 12237 bytes in 1 msecs (HTTP/1.1 200) 3 headers in 111 bytes (1 switches on core 0)
[pid: 4073|app: 0|req: 31/291] 218.247.217.98 () {42 vars in 748 bytes} [Tue Dec  4 08:50:16 2018] GET /data/?page=1&limit=30 => generated 11502 bytes in 22 msecs (HTTP/1.1 200) 3 headers in 102 bytes (2 switches on core 0)
[pid: 4074|app: 0|req: 34/292] 218.247.217.98 () {42 vars in 774 bytes} [Tue Dec  4 08:50:24 2018] GET /spider/distribute.html => generated 3960 bytes in 1 msecs (HTTP/1.1 200) 3 headers in 110 bytes (1 switches on core 0)
[pid: 4075|app: 0|req: 35/293] 218.247.217.98 () {42 vars in 767 bytes} [Tue Dec  4 08:50:24 2018] GET /distribute_/?page=1&limit=20 => generated 6706 bytes in 26 msecs (HTTP/1.1 200) 3 headers in 101 bytes (2 switches on core 0)
[pid: 4072|app: 0|req: 32/294] 218.247.217.98 () {42 vars in 760 bytes} [Tue Dec  4 08:50:26 2018] GET /spider/pid.html => generated 3845 bytes in 1 msecs (HTTP/1.1 200) 3 headers in 110 bytes (1 switches on core 0)
[pid: 4071|app: 0|req: 36/295] 218.247.217.98 () {42 vars in 746 bytes} [Tue Dec  4 08:50:26 2018] GET /pid_/?page=1&limit=16 => generated 3003 bytes in 15 msecs (HTTP/1.1 200) 3 headers in 101 bytes (2 switches on core 0)
[pid: 4073|app: 0|req: 32/296] 218.247.217.98 () {42 vars in 764 bytes} [Tue Dec  4 08:50:26 2018] GET /spider/mysql.html => generated 3240 bytes in 1 msecs (HTTP/1.1 200) 3 headers in 110 bytes (1 switches on core 0)
[pid: 4074|app: 0|req: 35/297] 218.247.217.98 () {42 vars in 752 bytes} [Tue Dec  4 08:50:26 2018] GET /mysql_/?page=1&limit=16 => generated 7344 bytes in 14 msecs (HTTP/1.1 200) 3 headers in 101 bytes (2 switches on core 0)
[pid: 4075|app: 0|req: 36/298] 218.247.217.98 () {42 vars in 770 bytes} [Tue Dec  4 08:50:27 2018] GET /spider/rebbitmq.html => generated 3995 bytes in 1 msecs (HTTP/1.1 200) 3 headers in 110 bytes (1 switches on core 0)
[pid: 4072|app: 0|req: 33/299] 218.247.217.98 () {42 vars in 761 bytes} [Tue Dec  4 08:50:27 2018] GET /rebbitmq_/?page=1&limit=16 => generated 7351 bytes in 27 msecs (HTTP/1.1 200) 3 headers in 101 bytes (2 switches on core 0)
[pid: 4071|app: 0|req: 37/300] 218.247.217.98 () {42 vars in 766 bytes} [Tue Dec  4 08:50:28 2018] GET /spider/server.html => generated 3582 bytes in 1 msecs (HTTP/1.1 200) 3 headers in 110 bytes (1 switches on core 0)
[pid: 4073|app: 0|req: 33/301] 218.247.217.98 () {42 vars in 755 bytes} [Tue Dec  4 08:50:28 2018] GET /server_/?page=1&limit=16 => generated 1099 bytes in 20 msecs (HTTP/1.1 200) 3 headers in 101 bytes (2 switches on core 0)
[pid: 4074|app: 0|req: 36/302] 218.247.217.98 () {42 vars in 724 bytes} [Tue Dec  4 08:53:18 2018] GET /index => generated 7174 bytes in 1 msecs (HTTP/1.1 200) 3 headers in 110 bytes (1 switches on core 0)
[pid: 4075|app: 0|req: 37/303] 218.247.217.98 () {42 vars in 764 bytes} [Tue Dec  4 08:53:18 2018] GET /demo/welcome.html => generated 24253 bytes in 1 msecs (HTTP/1.1 200) 3 headers in 111 bytes (1 switches on core 0)
[pid: 4072|app: 0|req: 34/304] 218.247.217.98 () {40 vars in 647 bytes} [Tue Dec  4 08:53:18 2018] GET /js/index.js => generated 7174 bytes in 1 msecs (HTTP/1.1 200) 3 headers in 110 bytes (1 switches on core 0)
Not Found: /frame/static/js/vip_nav.js
[pid: 4071|app: 0|req: 38/305] 218.247.217.98 () {40 vars in 665 bytes} [Tue Dec  4 08:53:18 2018] GET /frame/static/js/vip_nav.js => generated 4584 bytes in 4 msecs (HTTP/1.1 404) 3 headers in 102 bytes (1 switches on core 0)
Not Found: /demo/vip_tab.js
[pid: 4073|app: 0|req: 34/306] 218.247.217.98 () {40 vars in 655 bytes} [Tue Dec  4 08:53:18 2018] GET /demo/vip_tab.js => generated 4551 bytes in 4 msecs (HTTP/1.1 404) 3 headers in 102 bytes (1 switches on core 0)
[pid: 4074|app: 0|req: 37/307] 218.247.217.98 () {42 vars in 724 bytes} [Tue Dec  4 08:53:19 2018] GET /index => generated 7174 bytes in 1 msecs (HTTP/1.1 200) 3 headers in 110 bytes (1 switches on core 0)
[pid: 4075|app: 0|req: 38/308] 218.247.217.98 () {42 vars in 764 bytes} [Tue Dec  4 08:53:19 2018] GET /demo/welcome.html => generated 24253 bytes in 1 msecs (HTTP/1.1 200) 3 headers in 111 bytes (1 switches on core 0)
Not Found: /frame/static/js/vip_nav.js
[pid: 4072|app: 0|req: 35/309] 218.247.217.98 () {40 vars in 665 bytes} [Tue Dec  4 08:53:19 2018] GET /frame/static/js/vip_nav.js => generated 4584 bytes in 4 msecs (HTTP/1.1 404) 3 headers in 102 bytes (1 switches on core 0)
[pid: 4071|app: 0|req: 39/310] 218.247.217.98 () {40 vars in 647 bytes} [Tue Dec  4 08:53:19 2018] GET /js/index.js => generated 7174 bytes in 1 msecs (HTTP/1.1 200) 3 headers in 110 bytes (1 switches on core 0)
Not Found: /demo/vip_tab.js
[pid: 4073|app: 0|req: 35/311] 218.247.217.98 () {40 vars in 655 bytes} [Tue Dec  4 08:53:19 2018] GET /demo/vip_tab.js => generated 4551 bytes in 4 msecs (HTTP/1.1 404) 3 headers in 102 bytes (1 switches on core 0)
[pid: 4074|app: 0|req: 38/312] 218.247.217.98 () {42 vars in 764 bytes} [Tue Dec  4 08:53:20 2018] GET /spider/basic.html => generated 12237 bytes in 1 msecs (HTTP/1.1 200) 3 headers in 111 bytes (1 switches on core 0)
[pid: 4075|app: 0|req: 39/313] 218.247.217.98 () {42 vars in 748 bytes} [Tue Dec  4 08:53:20 2018] GET /data/?page=1&limit=30 => generated 11502 bytes in 18 msecs (HTTP/1.1 200) 3 headers in 102 bytes (2 switches on core 0)
[pid: 4072|app: 0|req: 36/314] 218.247.217.98 () {42 vars in 764 bytes} [Tue Dec  4 09:29:47 2018] GET /spider/mysql.html => generated 3240 bytes in 1 msecs (HTTP/1.1 200) 3 headers in 110 bytes (1 switches on core 0)
[pid: 4071|app: 0|req: 40/315] 218.247.217.98 () {42 vars in 752 bytes} [Tue Dec  4 09:29:47 2018] GET /mysql_/?page=1&limit=16 => generated 7347 bytes in 14 msecs (HTTP/1.1 200) 3 headers in 101 bytes (2 switches on core 0)
[pid: 4073|app: 0|req: 36/316] 218.247.217.98 () {42 vars in 774 bytes} [Tue Dec  4 09:29:48 2018] GET /spider/distribute.html => generated 3960 bytes in 1 msecs (HTTP/1.1 200) 3 headers in 110 bytes (1 switches on core 0)
[pid: 4074|app: 0|req: 39/317] 218.247.217.98 () {42 vars in 767 bytes} [Tue Dec  4 09:29:48 2018] GET /distribute_/?page=1&limit=20 => generated 6706 bytes in 27 msecs (HTTP/1.1 200) 3 headers in 101 bytes (2 switches on core 0)
[pid: 4075|app: 0|req: 40/318] 61.129.7.254 () {46 vars in 1408 bytes} [Tue Dec  4 10:28:19 2018] GET /index?nsukey=32FZeogGHVr1MvaL9OIA95O8mB3KU2BxosCF4e2ACIK2FMaf2BM5Tl8cQdWtfwUoMDz920d3Y7tGoeqSV8JvJM6hLvaspYAX9j0e6xkRsOfU2I2FB6JlGXFHQlR6r21lBDOgEfx6ZJXDA5wLFpEOOHXlwIcuz0Q2FmJjcscS5LgGd0oi0ZpSVBFiQWegT3OUWgF3iZ8T56y2p9BzHx35PClbKRhQ3D3D => generated 7174 bytes in 1 msecs (HTTP/1.1 200) 3 headers in 110 bytes (1 switches on core 0)
[pid: 4072|app: 0|req: 37/319] 101.226.225.85 () {42 vars in 1015 bytes} [Tue Dec  4 10:28:19 2018] GET /demo/welcome.html => generated 24253 bytes in 1 msecs (HTTP/1.1 200) 3 headers in 111 bytes (1 switches on core 0)
[pid: 4071|app: -1|req: -1/320] 61.129.8.250 () {42 vars in 981 bytes} [Tue Dec  4 10:28:19 2018] GET /src/frame/static/image/code.png => generated 2108 bytes in 0 msecs via sendfile() (HTTP/1.1 200) 3 headers in 112 bytes (0 switches on core 0)
[pid: 4073|app: -1|req: -1/321] 61.129.7.254 () {42 vars in 979 bytes} [Tue Dec  4 10:28:19 2018] GET /src/frame/static/image/zfb.png => generated 25040 bytes in 0 msecs via sendfile() (HTTP/1.1 200) 3 headers in 113 bytes (0 switches on core 0)
[pid: 4074|app: -1|req: -1/322] 61.129.8.203 () {42 vars in 977 bytes} [Tue Dec  4 10:28:19 2018] GET /src/frame/static/image/wx.png => generated 39482 bytes in 0 msecs via sendfile() (HTTP/1.1 200) 3 headers in 113 bytes (0 switches on core 0)
[pid: 4072|app: -1|req: -1/323] 61.151.178.168 () {42 vars in 1002 bytes} [Tue Dec  4 10:28:19 2018] GET /src/frame/layui/font/iconfont.svg?v=2.0.0 => generated 205116 bytes in 0 msecs via sendfile() (HTTP/1.1 200) 3 headers in 118 bytes (0 switches on core 0)
Not Found: /frame/static/js/vip_nav.js
[pid: 4075|app: 0|req: 41/324] 61.151.179.27 () {42 vars in 972 bytes} [Tue Dec  4 10:28:19 2018] GET /frame/static/js/vip_nav.js => generated 4584 bytes in 4 msecs (HTTP/1.1 404) 3 headers in 102 bytes (1 switches on core 0)
[pid: 4071|app: 0|req: 41/325] 61.151.179.27 () {42 vars in 722 bytes} [Tue Dec  4 10:28:20 2018] GET /js/index.js => generated 7174 bytes in 1 msecs (HTTP/1.1 200) 3 headers in 110 bytes (1 switches on core 0)
[pid: 4073|app: -1|req: -1/326] 61.151.179.27 () {42 vars in 1003 bytes} [Tue Dec  4 10:28:21 2018] GET /src/frame/layui/font/iconfont.woff?v=2.0.0 => generated 21680 bytes in 0 msecs via sendfile() (HTTP/1.1 200) 2 headers in 88 bytes (0 switches on core 0)
Not Found: /demo/vip_tab.js
[pid: 4074|app: 0|req: 40/327] 61.129.7.254 () {42 vars in 729 bytes} [Tue Dec  4 10:28:21 2018] GET /demo/vip_tab.js => generated 4551 bytes in 4 msecs (HTTP/1.1 404) 3 headers in 102 bytes (1 switches on core 0)
[pid: 4072|app: -1|req: -1/328] 218.247.217.98 () {38 vars in 763 bytes} [Tue Dec  4 10:28:21 2018] GET /src/frame/static/image/zfb.png => generated 25040 bytes in 0 msecs via sendfile() (HTTP/1.1 200) 3 headers in 113 bytes (0 switches on core 0)
[pid: 4075|app: -1|req: -1/329] 218.247.217.98 () {38 vars in 761 bytes} [Tue Dec  4 10:28:21 2018] GET /src/frame/static/image/wx.png => generated 39482 bytes in 0 msecs via sendfile() (HTTP/1.1 200) 3 headers in 113 bytes (0 switches on core 0)
[pid: 4071|app: 0|req: 42/330] 218.247.217.98 () {40 vars in 698 bytes} [Tue Dec  4 10:28:30 2018] GET /index => generated 7174 bytes in 1 msecs (HTTP/1.1 200) 3 headers in 110 bytes (1 switches on core 0)
[pid: 4073|app: -1|req: -1/331] 218.247.217.98 () {40 vars in 691 bytes} [Tue Dec  4 10:28:30 2018] GET /src/frame/layui/css/layui.css => generated 50971 bytes in 0 msecs via sendfile() (HTTP/1.1 200) 3 headers in 112 bytes (0 switches on core 0)
[pid: 4074|app: -1|req: -1/332] 218.247.217.98 () {40 vars in 693 bytes} [Tue Dec  4 10:28:30 2018] GET /src/frame/static/css/style.css => generated 11288 bytes in 0 msecs via sendfile() (HTTP/1.1 200) 3 headers in 112 bytes (0 switches on core 0)
[pid: 4072|app: -1|req: -1/333] 218.247.217.98 () {40 vars in 666 bytes} [Tue Dec  4 10:28:30 2018] GET /src/frame/layui/layui.js => generated 5923 bytes in 0 msecs via sendfile() (HTTP/1.1 200) 3 headers in 118 bytes (0 switches on core 0)
[pid: 4075|app: -1|req: -1/334] 218.247.217.98 () {40 vars in 680 bytes} [Tue Dec  4 10:28:30 2018] GET /src/frame/static/js/vip_comm.js => generated 9870 bytes in 0 msecs via sendfile() (HTTP/1.1 200) 3 headers in 118 bytes (0 switches on core 0)
[pid: 4071|app: -1|req: -1/335] 218.247.217.98 () {40 vars in 716 bytes} [Tue Dec  4 10:28:30 2018] GET /src/frame/static/image/code.png => generated 2108 bytes in 0 msecs via sendfile() (HTTP/1.1 200) 3 headers in 112 bytes (0 switches on core 0)
[pid: 4073|app: -1|req: -1/336] 218.247.217.98 () {40 vars in 714 bytes} [Tue Dec  4 10:28:30 2018] GET /src/frame/static/image/zfb.png => generated 25040 bytes in 0 msecs via sendfile() (HTTP/1.1 200) 3 headers in 113 bytes (0 switches on core 0)
[pid: 4074|app: 0|req: 41/337] 218.247.217.98 () {42 vars in 769 bytes} [Tue Dec  4 10:28:30 2018] GET /demo/welcome.html => generated 24253 bytes in 1 msecs (HTTP/1.1 200) 3 headers in 111 bytes (1 switches on core 0)
[pid: 4072|app: -1|req: -1/338] 218.247.217.98 () {40 vars in 712 bytes} [Tue Dec  4 10:28:30 2018] GET /src/frame/static/image/wx.png => generated 39482 bytes in 0 msecs via sendfile() (HTTP/1.1 200) 3 headers in 113 bytes (0 switches on core 0)
[pid: 4075|app: -1|req: -1/339] 218.247.217.98 () {40 vars in 666 bytes} [Tue Dec  4 10:28:30 2018] GET /src/layui/layui.js => generated 9616 bytes in 0 msecs via sendfile() (HTTP/1.1 200) 3 headers in 118 bytes (0 switches on core 0)
[pid: 4071|app: 0|req: 43/340] 218.247.217.98 () {40 vars in 652 bytes} [Tue Dec  4 10:28:30 2018] GET /js/index.js => generated 7174 bytes in 1 msecs (HTTP/1.1 200) 3 headers in 110 bytes (1 switches on core 0)
[pid: 4073|app: -1|req: -1/341] 218.247.217.98 () {40 vars in 694 bytes} [Tue Dec  4 10:28:30 2018] GET /src/frame/echarts/echarts.min.js => generated 577370 bytes in 0 msecs via sendfile() (HTTP/1.1 200) 3 headers in 120 bytes (0 switches on core 0)
[pid: 4074|app: -1|req: -1/342] 218.247.217.98 () {42 vars in 765 bytes} [Tue Dec  4 10:28:30 2018] GET /src/frame/layui/font/iconfont.woff?v=2.0.0 => generated 21680 bytes in 0 msecs via sendfile() (HTTP/1.1 200) 2 headers in 88 bytes (0 switches on core 0)
[pid: 4072|app: -1|req: -1/343] 218.247.217.98 () {40 vars in 690 bytes} [Tue Dec  4 10:28:31 2018] GET /src/frame/layui/lay/modules/layer.js => generated 21862 bytes in 0 msecs via sendfile() (HTTP/1.1 200) 3 headers in 119 bytes (0 switches on core 0)
[pid: 4075|app: -1|req: -1/344] 218.247.217.98 () {40 vars in 750 bytes} [Tue Dec  4 10:28:31 2018] GET /src/frame/layui/css/modules/layer/default/layer.css?v=3.0.3 => generated 14364 bytes in 0 msecs via sendfile() (HTTP/1.1 200) 3 headers in 112 bytes (0 switches on core 0)
[pid: 4071|app: -1|req: -1/345] 218.247.217.98 () {40 vars in 692 bytes} [Tue Dec  4 10:28:31 2018] GET /src/frame/layui/lay/modules/jquery.js => generated 97647 bytes in 0 msecs via sendfile() (HTTP/1.1 200) 3 headers in 119 bytes (0 switches on core 0)
[pid: 4073|app: -1|req: -1/346] 218.247.217.98 () {40 vars in 694 bytes} [Tue Dec  4 10:28:32 2018] GET /src/frame/layui/lay/modules/element.js => generated 6959 bytes in 0 msecs via sendfile() (HTTP/1.1 200) 3 headers in 118 bytes (0 switches on core 0)
Not Found: /frame/static/js/vip_nav.js
[pid: 4074|app: 0|req: 42/347] 218.247.217.98 () {40 vars in 670 bytes} [Tue Dec  4 10:28:32 2018] GET /frame/static/js/vip_nav.js => generated 4584 bytes in 4 msecs (HTTP/1.1 404) 3 headers in 102 bytes (1 switches on core 0)
[pid: 4072|app: -1|req: -1/348] 218.247.217.98 () {40 vars in 688 bytes} [Tue Dec  4 10:28:32 2018] GET /src/frame/layui/lay/modules/util.js => generated 1760 bytes in 0 msecs via sendfile() (HTTP/1.1 200) 3 headers in 118 bytes (0 switches on core 0)
[pid: 4075|app: -1|req: -1/349] 218.247.217.98 () {40 vars in 694 bytes} [Tue Dec  4 10:28:36 2018] GET /src/layui/lay/modules/element.js => generated 7264 bytes in 0 msecs via sendfile() (HTTP/1.1 200) 3 headers in 118 bytes (0 switches on core 0)
[pid: 4071|app: -1|req: -1/350] 218.247.217.98 () {40 vars in 692 bytes} [Tue Dec  4 10:28:36 2018] GET /src/layui/lay/modules/jquery.js => generated 97648 bytes in 0 msecs via sendfile() (HTTP/1.1 200) 3 headers in 119 bytes (0 switches on core 0)
[pid: 4073|app: 0|req: 37/351] 218.247.217.98 () {42 vars in 769 bytes} [Tue Dec  4 10:28:36 2018] GET /spider/basic.html => generated 12237 bytes in 1 msecs (HTTP/1.1 200) 3 headers in 111 bytes (1 switches on core 0)
[pid: 4074|app: -1|req: -1/352] 218.247.217.98 () {40 vars in 679 bytes} [Tue Dec  4 10:28:36 2018] GET /src/css/layui.css => generated 69092 bytes in 0 msecs via sendfile() (HTTP/1.1 200) 3 headers in 112 bytes (0 switches on core 0)
[pid: 4072|app: -1|req: -1/353] 218.247.217.98 () {40 vars in 670 bytes} [Tue Dec  4 10:28:36 2018] GET /src/jquery-latest.js => generated 282766 bytes in 0 msecs via sendfile() (HTTP/1.1 200) 3 headers in 120 bytes (0 switches on core 0)
[pid: 4075|app: -1|req: -1/354] 218.247.217.98 () {40 vars in 654 bytes} [Tue Dec  4 10:28:37 2018] GET /src/layui.js => generated 15036 bytes in 0 msecs via sendfile() (HTTP/1.1 200) 3 headers in 119 bytes (0 switches on core 0)
[pid: 4071|app: -1|req: -1/355] 218.247.217.98 () {40 vars in 688 bytes} [Tue Dec  4 10:28:37 2018] GET /src/layui/lay/modules/form.js => generated 9146 bytes in 0 msecs via sendfile() (HTTP/1.1 200) 3 headers in 118 bytes (0 switches on core 0)
[pid: 4073|app: -1|req: -1/356] 218.247.217.98 () {40 vars in 690 bytes} [Tue Dec  4 10:28:37 2018] GET /src/layui/lay/modules/layer.js => generated 22041 bytes in 0 msecs via sendfile() (HTTP/1.1 200) 3 headers in 119 bytes (0 switches on core 0)
[pid: 4074|app: -1|req: -1/357] 218.247.217.98 () {40 vars in 750 bytes} [Tue Dec  4 10:28:37 2018] GET /src/layui/css/modules/layer/default/layer.css?v=3.1.1 => generated 14425 bytes in 0 msecs via sendfile() (HTTP/1.1 200) 3 headers in 112 bytes (0 switches on core 0)
[pid: 4072|app: -1|req: -1/358] 218.247.217.98 () {40 vars in 690 bytes} [Tue Dec  4 10:28:37 2018] GET /src/layui/lay/modules/table.js => generated 30342 bytes in 0 msecs via sendfile() (HTTP/1.1 200) 3 headers in 119 bytes (0 switches on core 0)
[pid: 4075|app: -1|req: -1/359] 218.247.217.98 () {40 vars in 692 bytes} [Tue Dec  4 10:28:38 2018] GET /src/layui/lay/modules/laytpl.js => generated 1836 bytes in 0 msecs via sendfile() (HTTP/1.1 200) 3 headers in 118 bytes (0 switches on core 0)
[pid: 4071|app: -1|req: -1/360] 218.247.217.98 () {40 vars in 694 bytes} [Tue Dec  4 10:28:38 2018] GET /src/layui/lay/modules/laypage.js => generated 4472 bytes in 0 msecs via sendfile() (HTTP/1.1 200) 3 headers in 118 bytes (0 switches on core 0)
[pid: 4073|app: -1|req: -1/361] 218.247.217.98 () {40 vars in 688 bytes} [Tue Dec  4 10:28:39 2018] GET /src/layui/lay/modules/util.js => generated 3458 bytes in 0 msecs via sendfile() (HTTP/1.1 200) 3 headers in 118 bytes (0 switches on core 0)
Not Found: /demo/vip_tab.js
[pid: 4074|app: 0|req: 43/362] 218.247.217.98 () {40 vars in 660 bytes} [Tue Dec  4 10:28:39 2018] GET /demo/vip_tab.js => generated 4551 bytes in 4 msecs (HTTP/1.1 404) 3 headers in 102 bytes (1 switches on core 0)
[pid: 4072|app: -1|req: -1/363] 218.247.217.98 () {40 vars in 678 bytes} [Tue Dec  4 10:28:40 2018] GET /src/lay/modules/table.js => generated 42522 bytes in 0 msecs via sendfile() (HTTP/1.1 200) 3 headers in 119 bytes (0 switches on core 0)
[pid: 4075|app: -1|req: -1/364] 218.247.217.98 () {40 vars in 680 bytes} [Tue Dec  4 10:28:40 2018] GET /src/lay/modules/laytpl.js => generated 3229 bytes in 0 msecs via sendfile() (HTTP/1.1 200) 3 headers in 118 bytes (0 switches on core 0)
[pid: 4071|app: -1|req: -1/365] 218.247.217.98 () {40 vars in 682 bytes} [Tue Dec  4 10:28:40 2018] GET /src/lay/modules/laypage.js => generated 9151 bytes in 0 msecs via sendfile() (HTTP/1.1 200) 3 headers in 118 bytes (0 switches on core 0)
[pid: 4073|app: -1|req: -1/366] 218.247.217.98 () {40 vars in 678 bytes} [Tue Dec  4 10:28:41 2018] GET /src/lay/modules/layer.js => generated 39377 bytes in 0 msecs via sendfile() (HTTP/1.1 200) 3 headers in 119 bytes (0 switches on core 0)
[pid: 4074|app: -1|req: -1/367] 218.247.217.98 () {40 vars in 738 bytes} [Tue Dec  4 10:28:41 2018] GET /src/css/modules/layer/default/layer.css?v=3.1.1 => generated 15585 bytes in 0 msecs via sendfile() (HTTP/1.1 200) 3 headers in 112 bytes (0 switches on core 0)
[pid: 4072|app: -1|req: -1/368] 218.247.217.98 () {40 vars in 676 bytes} [Tue Dec  4 10:28:41 2018] GET /src/lay/modules/form.js => generated 22243 bytes in 0 msecs via sendfile() (HTTP/1.1 200) 3 headers in 119 bytes (0 switches on core 0)
[pid: 4075|app: 0|req: 42/369] 218.247.217.98 () {42 vars in 753 bytes} [Tue Dec  4 10:28:41 2018] GET /data/?page=1&limit=30 => generated 11502 bytes in 22 msecs (HTTP/1.1 200) 3 headers in 102 bytes (2 switches on core 0)
[pid: 4071|app: -1|req: -1/370] 218.247.217.98 () {42 vars in 725 bytes} [Tue Dec  4 10:28:41 2018] GET /src/font/iconfont.woff?v=230 => generated 26328 bytes in 0 msecs via sendfile() (HTTP/1.1 200) 2 headers in 88 bytes (0 switches on core 0)
[pid: 4073|app: 0|req: 38/371] 101.227.139.161 () {36 vars in 1131 bytes} [Tue Dec  4 10:29:19 2018] GET /index?nsukey=3%2FZeogGHVr1MvaL9OIA95O8mB3KU%2BxosCF4e2ACIK%2FMaf%2BM5Tl8cQdWtfwUoMDz920d3Y7tGoeqSV8JvJM6hLvaspYAX9j0e6xkRsOfU2I%2FB6JlGXFHQlR6r21lBDOgEfx6ZJXDA5wLFpEOOHXlwIcuz0Q%2FmJjcscS5LgGd0oi0ZpSVBFiQWegT3OUWgF3iZ8T56y2p9BzHx35PClbKRhQ%3D%3D => generated 7174 bytes in 1 msecs (HTTP/1.1 200) 3 headers in 110 bytes (1 switches on core 0)
[pid: 4074|app: 0|req: 44/372] 101.227.139.161 () {38 vars in 916 bytes} [Tue Dec  4 10:29:19 2018] GET /demo/welcome.html => generated 24253 bytes in 1 msecs (HTTP/1.1 200) 3 headers in 111 bytes (1 switches on core 0)
[pid: 4072|app: -1|req: -1/373] 101.227.139.161 () {38 vars in 930 bytes} [Tue Dec  4 10:29:20 2018] GET /src/frame/layui/layui.js => generated 5923 bytes in 0 msecs via sendfile() (HTTP/1.1 200) 3 headers in 118 bytes (0 switches on core 0)
[pid: 4075|app: -1|req: -1/374] 101.227.139.161 () {38 vars in 944 bytes} [Tue Dec  4 10:29:20 2018] GET /src/frame/static/js/vip_comm.js => generated 9870 bytes in 0 msecs via sendfile() (HTTP/1.1 200) 3 headers in 118 bytes (0 switches on core 0)
[pid: 4071|app: -1|req: -1/375] 101.227.139.161 () {38 vars in 737 bytes} [Tue Dec  4 10:29:20 2018] GET /src/layui/layui.js => generated 9616 bytes in 0 msecs via sendfile() (HTTP/1.1 200) 3 headers in 118 bytes (0 switches on core 0)
[pid: 4073|app: 0|req: 39/376] 101.227.139.161 () {38 vars in 744 bytes} [Tue Dec  4 10:29:20 2018] GET /js/index.js => generated 7174 bytes in 1 msecs (HTTP/1.1 200) 3 headers in 110 bytes (1 switches on core 0)
[pid: 4074|app: -1|req: -1/377] 101.227.139.161 () {38 vars in 765 bytes} [Tue Dec  4 10:29:20 2018] GET /src/frame/echarts/echarts.min.js => generated 577370 bytes in 0 msecs via sendfile() (HTTP/1.1 200) 3 headers in 120 bytes (0 switches on core 0)
[pid: 4072|app: -1|req: -1/378] 218.247.217.98 () {40 vars in 782 bytes} [Tue Dec  4 10:29:33 2018] GET /src/css/modules/layer/default/loading-2.gif => generated 1787 bytes in 0 msecs via sendfile() (HTTP/1.1 200) 3 headers in 112 bytes (0 switches on core 0)
[pid: 4075|app: 0|req: 43/379] 218.247.217.98 () {42 vars in 753 bytes} [Tue Dec  4 10:29:33 2018] GET /data/?page=3&limit=30 => generated 5442 bytes in 28 msecs (HTTP/1.1 200) 3 headers in 101 bytes (2 switches on core 0)
[pid: 4071|app: -1|req: -1/380] 218.247.217.98 () {40 vars in 772 bytes} [Tue Dec  4 10:30:01 2018] GET /src/css/modules/layer/default/icon.png => generated 11493 bytes in 0 msecs via sendfile() (HTTP/1.1 200) 3 headers in 113 bytes (0 switches on core 0)
[pid: 4073|app: 0|req: 40/381] 218.247.217.98 () {42 vars in 832 bytes} [Tue Dec  4 10:30:01 2018] GET /demo/detail_form?path_name=lyl_yyj_hebei_yj => generated 8868 bytes in 1 msecs (HTTP/1.1 200) 3 headers in 110 bytes (1 switches on core 0)
[pid: 4074|app: -1|req: -1/382] 218.247.217.98 () {40 vars in 782 bytes} [Tue Dec  4 10:30:01 2018] GET /src/css/modules/layer/default/loading-1.gif => generated 701 bytes in 0 msecs via sendfile() (HTTP/1.1 200) 3 headers in 111 bytes (0 switches on core 0)
[pid: 4072|app: -1|req: -1/383] 218.247.217.98 () {40 vars in 717 bytes} [Tue Dec  4 10:30:01 2018] GET /src/layui/css/layui.css => generated 69531 bytes in 0 msecs via sendfile() (HTTP/1.1 200) 3 headers in 112 bytes (0 switches on core 0)
[pid: 4075|app: -1|req: -1/384] 218.247.217.98 () {40 vars in 720 bytes} [Tue Dec  4 10:30:01 2018] GET /src/layui/lay/modules/layedit.js => generated 12635 bytes in 0 msecs via sendfile() (HTTP/1.1 200) 3 headers in 119 bytes (0 switches on core 0)
[pid: 4071|app: -1|req: -1/385] 218.247.217.98 () {40 vars in 720 bytes} [Tue Dec  4 10:30:01 2018] GET /src/layui/lay/modules/laydate.js => generated 27377 bytes in 0 msecs via sendfile() (HTTP/1.1 200) 3 headers in 119 bytes (0 switches on core 0)
[pid: 4073|app: -1|req: -1/386] 218.247.217.98 () {40 vars in 784 bytes} [Tue Dec  4 10:30:02 2018] GET /src/layui/css/modules/laydate/default/laydate.css?v=5.0.9 => generated 7537 bytes in 0 msecs via sendfile() (HTTP/1.1 200) 3 headers in 111 bytes (0 switches on core 0)
[pid: 4074|app: 0|req: 45/387] 218.247.217.98 () {48 vars in 963 bytes} [Tue Dec  4 10:30:02 2018] POST /select/by_path_name/ => generated 796 bytes in 20 msecs (HTTP/1.1 200) 3 headers in 101 bytes (1 switches on core 0)
[pid: 4072|app: -1|req: -1/388] 218.247.217.98 () {42 vars in 743 bytes} [Tue Dec  4 10:30:02 2018] GET /src/layui/font/iconfont.woff?v=240 => generated 26744 bytes in 0 msecs via sendfile() (HTTP/1.1 200) 2 headers in 88 bytes (0 switches on core 0)
[pid: 4075|app: 0|req: 44/389] 218.247.217.98 () {42 vars in 779 bytes} [Tue Dec  4 10:30:18 2018] GET /spider/distribute.html => generated 3960 bytes in 1 msecs (HTTP/1.1 200) 3 headers in 110 bytes (1 switches on core 0)
[pid: 4071|app: -1|req: -1/390] 218.247.217.98 () {40 vars in 679 bytes} [Tue Dec  4 10:30:18 2018] GET /src/lib/layui/layui.js => generated 6542 bytes in 0 msecs via sendfile() (HTTP/1.1 200) 3 headers in 118 bytes (0 switches on core 0)
[pid: 4073|app: -1|req: -1/391] 218.247.217.98 () {40 vars in 703 bytes} [Tue Dec  4 10:30:18 2018] GET /src/lib/layui/lay/modules/table.js => generated 20828 bytes in 0 msecs via sendfile() (HTTP/1.1 200) 3 headers in 119 bytes (0 switches on core 0)
[pid: 4074|app: -1|req: -1/392] 218.247.217.98 () {40 vars in 705 bytes} [Tue Dec  4 10:30:18 2018] GET /src/lib/layui/lay/modules/laytpl.js => generated 1836 bytes in 0 msecs via sendfile() (HTTP/1.1 200) 3 headers in 118 bytes (0 switches on core 0)
[pid: 4072|app: -1|req: -1/393] 218.247.217.98 () {40 vars in 707 bytes} [Tue Dec  4 10:30:18 2018] GET /src/lib/layui/lay/modules/laypage.js => generated 4319 bytes in 0 msecs via sendfile() (HTTP/1.1 200) 3 headers in 118 bytes (0 switches on core 0)
[pid: 4075|app: -1|req: -1/394] 218.247.217.98 () {40 vars in 703 bytes} [Tue Dec  4 10:30:18 2018] GET /src/lib/layui/lay/modules/layer.js => generated 22063 bytes in 0 msecs via sendfile() (HTTP/1.1 200) 3 headers in 119 bytes (0 switches on core 0)
[pid: 4071|app: -1|req: -1/395] 218.247.217.98 () {40 vars in 763 bytes} [Tue Dec  4 10:30:18 2018] GET /src/lib/layui/css/modules/layer/default/layer.css?v=3.1.1 => generated 14425 bytes in 0 msecs via sendfile() (HTTP/1.1 200) 3 headers in 112 bytes (0 switches on core 0)
[pid: 4073|app: -1|req: -1/396] 218.247.217.98 () {40 vars in 705 bytes} [Tue Dec  4 10:30:18 2018] GET /src/lib/layui/lay/modules/jquery.js => generated 97648 bytes in 0 msecs via sendfile() (HTTP/1.1 200) 3 headers in 119 bytes (0 switches on core 0)
[pid: 4074|app: -1|req: -1/397] 218.247.217.98 () {40 vars in 701 bytes} [Tue Dec  4 10:30:18 2018] GET /src/lib/layui/lay/modules/form.js => generated 7925 bytes in 0 msecs via sendfile() (HTTP/1.1 200) 3 headers in 118 bytes (0 switches on core 0)
[pid: 4072|app: 0|req: 38/398] 218.247.217.98 () {42 vars in 772 bytes} [Tue Dec  4 10:30:18 2018] GET /distribute_/?page=1&limit=20 => generated 6706 bytes in 24 msecs (HTTP/1.1 200) 3 headers in 101 bytes (2 switches on core 0)
[pid: 4075|app: 0|req: 45/399] 218.247.217.98 () {42 vars in 748 bytes} [Tue Dec  4 10:31:05 2018] GET /data/?page=3&limit=30 => generated 5442 bytes in 29 msecs (HTTP/1.1 200) 3 headers in 101 bytes (2 switches on core 0)
[pid: 4071|app: 0|req: 44/400] 218.247.217.98 () {42 vars in 813 bytes} [Tue Dec  4 10:31:08 2018] GET /demo/form?path_name=lyl_yyj_henan_yj => generated 9536 bytes in 1 msecs (HTTP/1.1 200) 3 headers in 110 bytes (1 switches on core 0)
[pid: 4073|app: -1|req: -1/401] 218.247.217.98 () {42 vars in 760 bytes} [Tue Dec  4 10:31:08 2018] GET /src/layui/css/layui.css => generated 0 bytes in 0 msecs (HTTP/1.1 304) 0 headers in 29 bytes (0 switches on core 0)
[pid: 4074|app: -1|req: -1/402] 218.247.217.98 () {42 vars in 763 bytes} [Tue Dec  4 10:31:08 2018] GET /src/layui/lay/modules/layedit.js => generated 0 bytes in 0 msecs (HTTP/1.1 304) 0 headers in 29 bytes (0 switches on core 0)
[pid: 4072|app: -1|req: -1/403] 218.247.217.98 () {42 vars in 763 bytes} [Tue Dec  4 10:31:08 2018] GET /src/layui/lay/modules/laydate.js => generated 0 bytes in 0 msecs (HTTP/1.1 304) 0 headers in 29 bytes (0 switches on core 0)
[pid: 4075|app: -1|req: -1/404] 218.247.217.98 () {42 vars in 827 bytes} [Tue Dec  4 10:31:08 2018] GET /src/layui/css/modules/laydate/default/laydate.css?v=5.0.9 => generated 0 bytes in 0 msecs (HTTP/1.1 304) 0 headers in 29 bytes (0 switches on core 0)
[pid: 4071|app: 0|req: 45/405] 218.247.217.98 () {48 vars in 951 bytes} [Tue Dec  4 10:31:08 2018] POST /select/by_path_name/ => generated 796 bytes in 29 msecs (HTTP/1.1 200) 3 headers in 101 bytes (1 switches on core 0)
[pid: 4074|app: -1|req: -1/406] 218.247.217.98 () {40 vars in 807 bytes} [Tue Dec  4 10:34:21 2018] GET /src/lib/layui/css/modules/layer/default/loading-2.gif => generated 1787 bytes in 0 msecs via sendfile() (HTTP/1.1 200) 3 headers in 112 bytes (0 switches on core 0)
[pid: 4073|app: 0|req: 41/407] 218.247.217.98 () {42 vars in 752 bytes} [Tue Dec  4 10:34:21 2018] GET /mysql_/?page=3&limit=16 => generated 2513 bytes in 18 msecs (HTTP/1.1 200) 3 headers in 101 bytes (2 switches on core 0)
[pid: 4072|app: 0|req: 39/408] 218.247.217.98 () {42 vars in 752 bytes} [Tue Dec  4 10:34:25 2018] GET /mysql_/?page=2&limit=16 => generated 7171 bytes in 19 msecs (HTTP/1.1 200) 3 headers in 101 bytes (2 switches on core 0)
[pid: 4075|app: 0|req: 46/409] 218.247.217.98 () {42 vars in 752 bytes} [Tue Dec  4 10:34:27 2018] GET /mysql_/?page=1&limit=16 => generated 7326 bytes in 23 msecs (HTTP/1.1 200) 3 headers in 101 bytes (2 switches on core 0)
[pid: 4071|app: 0|req: 46/410] 218.247.217.98 () {42 vars in 729 bytes} [Tue Dec  4 10:34:31 2018] GET /index => generated 7174 bytes in 1 msecs (HTTP/1.1 200) 3 headers in 110 bytes (1 switches on core 0)
[pid: 4074|app: 0|req: 46/411] 218.247.217.98 () {42 vars in 769 bytes} [Tue Dec  4 10:34:31 2018] GET /demo/welcome.html => generated 24253 bytes in 1 msecs (HTTP/1.1 200) 3 headers in 111 bytes (1 switches on core 0)
[pid: 4073|app: 0|req: 42/412] 218.247.217.98 () {40 vars in 652 bytes} [Tue Dec  4 10:34:31 2018] GET /js/index.js => generated 7174 bytes in 1 msecs (HTTP/1.1 200) 3 headers in 110 bytes (1 switches on core 0)
[pid: 4072|app: 0|req: 40/413] 218.247.217.98 () {42 vars in 752 bytes} [Tue Dec  4 10:34:32 2018] GET /mysql_/?page=3&limit=16 => generated 2513 bytes in 19 msecs (HTTP/1.1 200) 3 headers in 101 bytes (2 switches on core 0)
Not Found: /frame/static/js/vip_nav.js
[pid: 4075|app: 0|req: 47/414] 218.247.217.98 () {40 vars in 670 bytes} [Tue Dec  4 10:34:32 2018] GET /frame/static/js/vip_nav.js => generated 4584 bytes in 4 msecs (HTTP/1.1 404) 3 headers in 102 bytes (1 switches on core 0)
[pid: 4071|app: -1|req: -1/415] 218.247.217.98 () {44 vars in 769 bytes} [Tue Dec  4 10:34:32 2018] GET /src/frame/static/image/code.png => generated 2108 bytes in 0 msecs via sendfile() (HTTP/1.1 200) 3 headers in 112 bytes (0 switches on core 0)
Not Found: /demo/vip_tab.js
[pid: 4074|app: 0|req: 47/416] 218.247.217.98 () {40 vars in 660 bytes} [Tue Dec  4 10:34:32 2018] GET /demo/vip_tab.js => generated 4551 bytes in 4 msecs (HTTP/1.1 404) 3 headers in 102 bytes (1 switches on core 0)
[pid: 4073|app: 0|req: 43/417] 218.247.217.98 () {42 vars in 769 bytes} [Tue Dec  4 10:34:33 2018] GET /spider/basic.html => generated 12237 bytes in 1 msecs (HTTP/1.1 200) 3 headers in 111 bytes (1 switches on core 0)
[pid: 4072|app: 0|req: 41/418] 218.247.217.98 () {42 vars in 752 bytes} [Tue Dec  4 10:34:34 2018] GET /mysql_/?page=1&limit=16 => generated 7326 bytes in 20 msecs (HTTP/1.1 200) 3 headers in 101 bytes (2 switches on core 0)
[pid: 4075|app: 0|req: 48/419] 218.247.217.98 () {42 vars in 753 bytes} [Tue Dec  4 10:34:34 2018] GET /data/?page=1&limit=30 => generated 11502 bytes in 28 msecs (HTTP/1.1 200) 3 headers in 102 bytes (2 switches on core 0)
[pid: 4071|app: 0|req: 47/420] 218.247.217.98 () {42 vars in 753 bytes} [Tue Dec  4 10:34:38 2018] GET /data/?page=3&limit=30 => generated 5442 bytes in 23 msecs (HTTP/1.1 200) 3 headers in 101 bytes (2 switches on core 0)
[pid: 4074|app: 0|req: 48/421] 218.247.217.98 () {42 vars in 752 bytes} [Tue Dec  4 10:34:42 2018] GET /mysql_/?page=2&limit=16 => generated 7171 bytes in 21 msecs (HTTP/1.1 200) 3 headers in 101 bytes (2 switches on core 0)
[pid: 4073|app: 0|req: 44/422] 218.247.217.98 () {42 vars in 818 bytes} [Tue Dec  4 10:34:49 2018] GET /demo/form?path_name=lyl_yyj_henan_yj => generated 9536 bytes in 1 msecs (HTTP/1.1 200) 3 headers in 110 bytes (1 switches on core 0)
[pid: 4072|app: 0|req: 42/423] 218.247.217.98 () {48 vars in 956 bytes} [Tue Dec  4 10:34:49 2018] POST /select/by_path_name/ => generated 796 bytes in 26 msecs (HTTP/1.1 200) 3 headers in 101 bytes (1 switches on core 0)
[pid: 4075|app: 0|req: 49/424] 218.247.217.98 () {42 vars in 813 bytes} [Tue Dec  4 10:36:38 2018] GET /demo/form?path_name=lyl_yyj_henan_yj => generated 9536 bytes in 1 msecs (HTTP/1.1 200) 3 headers in 110 bytes (1 switches on core 0)
[pid: 4071|app: 0|req: 48/425] 218.247.217.98 () {48 vars in 951 bytes} [Tue Dec  4 10:36:38 2018] POST /select/by_path_name/ => generated 796 bytes in 25 msecs (HTTP/1.1 200) 3 headers in 101 bytes (1 switches on core 0)
[pid: 4074|app: -1|req: -1/426] 218.247.217.98 () {40 vars in 790 bytes} [Tue Dec  4 10:37:47 2018] GET /src/layui/css/modules/layer/default/icon.png => generated 11493 bytes in 0 msecs via sendfile() (HTTP/1.1 200) 3 headers in 113 bytes (0 switches on core 0)
[pid: 4073|app: 0|req: 45/427] 218.247.217.98 () {48 vars in 951 bytes} [Tue Dec  4 10:37:47 2018] POST /update/spider_basic_info/by_path_name/ => generated 0 bytes in 50 msecs (HTTP/1.1 200) 3 headers in 107 bytes (1 switches on core 0)
[pid: 4072|app: 0|req: 43/428] 218.247.217.98 () {42 vars in 832 bytes} [Tue Dec  4 10:37:58 2018] GET /demo/detail_form?path_name=lyl_yyj_henan_yj => generated 8868 bytes in 1 msecs (HTTP/1.1 200) 3 headers in 110 bytes (1 switches on core 0)
[pid: 4075|app: 0|req: 50/429] 218.247.217.98 () {48 vars in 963 bytes} [Tue Dec  4 10:37:58 2018] POST /select/by_path_name/ => generated 799 bytes in 24 msecs (HTTP/1.1 200) 3 headers in 101 bytes (1 switches on core 0)
[pid: 4071|app: 0|req: 49/430] 218.247.217.98 () {42 vars in 729 bytes} [Tue Dec  4 10:38:06 2018] GET /index => generated 7174 bytes in 1 msecs (HTTP/1.1 200) 3 headers in 110 bytes (1 switches on core 0)
[pid: 4074|app: 0|req: 49/431] 218.247.217.98 () {42 vars in 769 bytes} [Tue Dec  4 10:38:06 2018] GET /demo/welcome.html => generated 24253 bytes in 1 msecs (HTTP/1.1 200) 3 headers in 111 bytes (1 switches on core 0)
[pid: 4073|app: 0|req: 46/432] 218.247.217.98 () {40 vars in 652 bytes} [Tue Dec  4 10:38:06 2018] GET /js/index.js => generated 7174 bytes in 1 msecs (HTTP/1.1 200) 3 headers in 110 bytes (1 switches on core 0)
Not Found: /frame/static/js/vip_nav.js
[pid: 4072|app: 0|req: 44/433] 218.247.217.98 () {40 vars in 670 bytes} [Tue Dec  4 10:38:07 2018] GET /frame/static/js/vip_nav.js => generated 4584 bytes in 4 msecs (HTTP/1.1 404) 3 headers in 102 bytes (1 switches on core 0)
[pid: 4075|app: -1|req: -1/434] 218.247.217.98 () {44 vars in 769 bytes} [Tue Dec  4 10:38:07 2018] GET /src/frame/static/image/code.png => generated 2108 bytes in 0 msecs via sendfile() (HTTP/1.1 200) 3 headers in 112 bytes (0 switches on core 0)
Not Found: /demo/vip_tab.js
[pid: 4071|app: 0|req: 50/435] 218.247.217.98 () {40 vars in 660 bytes} [Tue Dec  4 10:38:07 2018] GET /demo/vip_tab.js => generated 4551 bytes in 4 msecs (HTTP/1.1 404) 3 headers in 102 bytes (1 switches on core 0)
[pid: 4074|app: 0|req: 50/436] 218.247.217.98 () {42 vars in 748 bytes} [Tue Dec  4 10:38:09 2018] GET /data/?page=1&limit=30 => generated 11502 bytes in 23 msecs (HTTP/1.1 200) 3 headers in 102 bytes (2 switches on core 0)
[pid: 4073|app: 0|req: 47/437] 218.247.217.98 () {42 vars in 769 bytes} [Tue Dec  4 10:38:11 2018] GET /spider/basic.html => generated 12237 bytes in 1 msecs (HTTP/1.1 200) 3 headers in 111 bytes (1 switches on core 0)
[pid: 4072|app: 0|req: 45/438] 218.247.217.98 () {42 vars in 753 bytes} [Tue Dec  4 10:38:11 2018] GET /data/?page=1&limit=30 => generated 11502 bytes in 29 msecs (HTTP/1.1 200) 3 headers in 102 bytes (2 switches on core 0)
[pid: 4075|app: 0|req: 51/439] 218.247.217.98 () {42 vars in 753 bytes} [Tue Dec  4 10:38:13 2018] GET /data/?page=3&limit=30 => generated 5445 bytes in 28 msecs (HTTP/1.1 200) 3 headers in 101 bytes (2 switches on core 0)
[pid: 4071|app: 0|req: 51/440] 218.247.217.98 () {42 vars in 748 bytes} [Tue Dec  4 10:38:14 2018] GET /data/?page=2&limit=30 => generated 10882 bytes in 30 msecs (HTTP/1.1 200) 3 headers in 102 bytes (2 switches on core 0)
[pid: 4074|app: 0|req: 51/441] 218.247.217.98 () {42 vars in 836 bytes} [Tue Dec  4 10:38:17 2018] GET /demo/detail_form?path_name=lyl_yyj_jiangsu_yj => generated 8870 bytes in 1 msecs (HTTP/1.1 200) 3 headers in 110 bytes (1 switches on core 0)
[pid: 4073|app: 0|req: 48/442] 218.247.217.98 () {48 vars in 965 bytes} [Tue Dec  4 10:38:17 2018] POST /select/by_path_name/ => generated 798 bytes in 25 msecs (HTTP/1.1 200) 3 headers in 101 bytes (1 switches on core 0)
[pid: 4072|app: 0|req: 46/443] 218.247.217.98 () {42 vars in 820 bytes} [Tue Dec  4 10:38:26 2018] GET /demo/form?path_name=yf_xzcf_env_hunan => generated 9537 bytes in 1 msecs (HTTP/1.1 200) 3 headers in 110 bytes (1 switches on core 0)
[pid: 4075|app: 0|req: 52/444] 218.247.217.98 () {48 vars in 957 bytes} [Tue Dec  4 10:38:26 2018] POST /select/by_path_name/ => generated 797 bytes in 29 msecs (HTTP/1.1 200) 3 headers in 101 bytes (1 switches on core 0)
[pid: 4071|app: 0|req: 52/445] 218.247.217.98 () {48 vars in 952 bytes} [Tue Dec  4 10:38:29 2018] POST /update/spider_basic_info/by_path_name/ => generated 0 bytes in 41 msecs (HTTP/1.1 200) 3 headers in 107 bytes (1 switches on core 0)
[pid: 4074|app: 0|req: 52/446] 218.247.217.98 () {42 vars in 824 bytes} [Tue Dec  4 10:38:34 2018] GET /demo/form?path_name=lyl_yyj_shanghai_yj => generated 9539 bytes in 1 msecs (HTTP/1.1 200) 3 headers in 110 bytes (1 switches on core 0)
[pid: 4073|app: 0|req: 49/447] 218.247.217.98 () {48 vars in 959 bytes} [Tue Dec  4 10:38:34 2018] POST /select/by_path_name/ => generated 802 bytes in 17 msecs (HTTP/1.1 200) 3 headers in 101 bytes (1 switches on core 0)
[pid: 4072|app: 0|req: 47/448] 218.247.217.98 () {48 vars in 954 bytes} [Tue Dec  4 10:38:37 2018] POST /update/spider_basic_info/by_path_name/ => generated 0 bytes in 58 msecs (HTTP/1.1 200) 3 headers in 107 bytes (1 switches on core 0)
[pid: 4075|app: 0|req: 53/449] 218.247.217.98 () {42 vars in 832 bytes} [Tue Dec  4 10:38:45 2018] GET /demo/form?path_name=lyl_yyj_heilongjiang_yj => generated 9543 bytes in 1 msecs (HTTP/1.1 200) 3 headers in 110 bytes (1 switches on core 0)
[pid: 4071|app: 0|req: 53/450] 218.247.217.98 () {48 vars in 963 bytes} [Tue Dec  4 10:38:45 2018] POST /select/by_path_name/ => generated 816 bytes in 29 msecs (HTTP/1.1 200) 3 headers in 101 bytes (1 switches on core 0)
[pid: 4074|app: 0|req: 53/451] 218.247.217.98 () {48 vars in 958 bytes} [Tue Dec  4 10:38:49 2018] POST /update/spider_basic_info/by_path_name/ => generated 0 bytes in 49 msecs (HTTP/1.1 200) 3 headers in 107 bytes (1 switches on core 0)
[pid: 4073|app: 0|req: 50/452] 218.247.217.98 () {42 vars in 818 bytes} [Tue Dec  4 10:38:55 2018] GET /demo/form?path_name=lyl_yyj_jilin_yj => generated 9536 bytes in 1 msecs (HTTP/1.1 200) 3 headers in 110 bytes (1 switches on core 0)
[pid: 4072|app: 0|req: 48/453] 218.247.217.98 () {48 vars in 956 bytes} [Tue Dec  4 10:38:55 2018] POST /select/by_path_name/ => generated 796 bytes in 25 msecs (HTTP/1.1 200) 3 headers in 101 bytes (1 switches on core 0)
[pid: 4075|app: 0|req: 54/454] 218.247.217.98 () {48 vars in 951 bytes} [Tue Dec  4 10:38:58 2018] POST /update/spider_basic_info/by_path_name/ => generated 0 bytes in 47 msecs (HTTP/1.1 200) 3 headers in 107 bytes (1 switches on core 0)
[pid: 4071|app: 0|req: 54/455] 218.247.217.98 () {42 vars in 818 bytes} [Tue Dec  4 10:39:06 2018] GET /demo/form?path_name=lyl_yyj_hebei_yj => generated 9536 bytes in 1 msecs (HTTP/1.1 200) 3 headers in 110 bytes (1 switches on core 0)
[pid: 4074|app: 0|req: 54/456] 218.247.217.98 () {48 vars in 956 bytes} [Tue Dec  4 10:39:06 2018] POST /select/by_path_name/ => generated 796 bytes in 30 msecs (HTTP/1.1 200) 3 headers in 101 bytes (1 switches on core 0)
[pid: 4073|app: 0|req: 51/457] 218.247.217.98 () {48 vars in 951 bytes} [Tue Dec  4 10:39:09 2018] POST /update/spider_basic_info/by_path_name/ => generated 0 bytes in 35 msecs (HTTP/1.1 200) 3 headers in 107 bytes (1 switches on core 0)
[pid: 4072|app: 0|req: 49/458] 218.247.217.98 () {42 vars in 729 bytes} [Tue Dec  4 10:39:13 2018] GET /index => generated 7174 bytes in 1 msecs (HTTP/1.1 200) 3 headers in 110 bytes (1 switches on core 0)
[pid: 4075|app: 0|req: 55/459] 218.247.217.98 () {42 vars in 769 bytes} [Tue Dec  4 10:39:13 2018] GET /demo/welcome.html => generated 24253 bytes in 1 msecs (HTTP/1.1 200) 3 headers in 111 bytes (1 switches on core 0)
[pid: 4071|app: 0|req: 55/460] 218.247.217.98 () {40 vars in 652 bytes} [Tue Dec  4 10:39:13 2018] GET /js/index.js => generated 7174 bytes in 1 msecs (HTTP/1.1 200) 3 headers in 110 bytes (1 switches on core 0)
Not Found: /frame/static/js/vip_nav.js
[pid: 4074|app: 0|req: 55/461] 218.247.217.98 () {40 vars in 670 bytes} [Tue Dec  4 10:39:13 2018] GET /frame/static/js/vip_nav.js => generated 4584 bytes in 4 msecs (HTTP/1.1 404) 3 headers in 102 bytes (1 switches on core 0)
[pid: 4073|app: -1|req: -1/462] 218.247.217.98 () {44 vars in 769 bytes} [Tue Dec  4 10:39:14 2018] GET /src/frame/static/image/code.png => generated 2108 bytes in 0 msecs via sendfile() (HTTP/1.1 200) 3 headers in 112 bytes (0 switches on core 0)
Not Found: /demo/vip_tab.js
[pid: 4072|app: 0|req: 50/463] 218.247.217.98 () {40 vars in 660 bytes} [Tue Dec  4 10:39:14 2018] GET /demo/vip_tab.js => generated 4551 bytes in 4 msecs (HTTP/1.1 404) 3 headers in 102 bytes (1 switches on core 0)
[pid: 4075|app: 0|req: 56/464] 218.247.217.98 () {42 vars in 769 bytes} [Tue Dec  4 10:39:14 2018] GET /spider/basic.html => generated 12237 bytes in 2 msecs (HTTP/1.1 200) 3 headers in 111 bytes (1 switches on core 0)
[pid: 4071|app: 0|req: 56/465] 218.247.217.98 () {42 vars in 753 bytes} [Tue Dec  4 10:39:15 2018] GET /data/?page=1&limit=30 => generated 11502 bytes in 29 msecs (HTTP/1.1 200) 3 headers in 102 bytes (2 switches on core 0)
[pid: 4074|app: 0|req: 56/466] 218.247.217.98 () {42 vars in 753 bytes} [Tue Dec  4 10:39:16 2018] GET /data/?page=3&limit=30 => generated 5457 bytes in 26 msecs (HTTP/1.1 200) 3 headers in 101 bytes (2 switches on core 0)
[pid: 4073|app: 0|req: 52/467] 218.247.217.98 () {42 vars in 822 bytes} [Tue Dec  4 10:39:21 2018] GET /demo/form?path_name=lyl_yyj_jiangsu_yj => generated 9538 bytes in 1 msecs (HTTP/1.1 200) 3 headers in 110 bytes (1 switches on core 0)
[pid: 4072|app: 0|req: 51/468] 218.247.217.98 () {48 vars in 958 bytes} [Tue Dec  4 10:39:21 2018] POST /select/by_path_name/ => generated 798 bytes in 21 msecs (HTTP/1.1 200) 3 headers in 101 bytes (1 switches on core 0)
[pid: 4075|app: 0|req: 57/469] 218.247.217.98 () {42 vars in 724 bytes} [Tue Dec  4 10:39:23 2018] GET /index => generated 7174 bytes in 1 msecs (HTTP/1.1 200) 3 headers in 110 bytes (1 switches on core 0)
[pid: 4071|app: 0|req: 57/470] 218.247.217.98 () {42 vars in 764 bytes} [Tue Dec  4 10:39:23 2018] GET /demo/welcome.html => generated 24253 bytes in 1 msecs (HTTP/1.1 200) 3 headers in 111 bytes (1 switches on core 0)
[pid: 4074|app: 0|req: 57/471] 218.247.217.98 () {40 vars in 647 bytes} [Tue Dec  4 10:39:23 2018] GET /js/index.js => generated 7174 bytes in 1 msecs (HTTP/1.1 200) 3 headers in 110 bytes (1 switches on core 0)
Not Found: /frame/static/js/vip_nav.js
[pid: 4073|app: 0|req: 53/472] 218.247.217.98 () {40 vars in 665 bytes} [Tue Dec  4 10:39:23 2018] GET /frame/static/js/vip_nav.js => generated 4584 bytes in 4 msecs (HTTP/1.1 404) 3 headers in 102 bytes (1 switches on core 0)
Not Found: /demo/vip_tab.js
[pid: 4072|app: 0|req: 52/473] 218.247.217.98 () {40 vars in 655 bytes} [Tue Dec  4 10:39:23 2018] GET /demo/vip_tab.js => generated 4551 bytes in 4 msecs (HTTP/1.1 404) 3 headers in 102 bytes (1 switches on core 0)
[pid: 4075|app: 0|req: 58/474] 218.247.217.98 () {42 vars in 764 bytes} [Tue Dec  4 10:39:24 2018] GET /spider/basic.html => generated 12249 bytes in 1 msecs (HTTP/1.1 200) 3 headers in 111 bytes (1 switches on core 0)
[pid: 4071|app: 0|req: 58/475] 218.247.217.98 () {42 vars in 748 bytes} [Tue Dec  4 10:39:25 2018] GET /data/?page=1&limit=30 => generated 11502 bytes in 30 msecs (HTTP/1.1 200) 3 headers in 102 bytes (2 switches on core 0)
[pid: 4074|app: 0|req: 58/476] 218.247.217.98 () {48 vars in 953 bytes} [Tue Dec  4 10:39:25 2018] POST /update/spider_basic_info/by_path_name/ => generated 0 bytes in 47 msecs (HTTP/1.1 200) 3 headers in 107 bytes (1 switches on core 0)
[pid: 4073|app: 0|req: 54/477] 218.247.217.98 () {42 vars in 753 bytes} [Tue Dec  4 10:39:29 2018] GET /data/?page=2&limit=30 => generated 10882 bytes in 28 msecs (HTTP/1.1 200) 3 headers in 102 bytes (2 switches on core 0)
[pid: 4072|app: 0|req: 53/478] 218.247.217.98 () {42 vars in 808 bytes} [Tue Dec  4 10:39:36 2018] GET /demo/form?path_name=lyl_landtax => generated 9531 bytes in 1 msecs (HTTP/1.1 200) 3 headers in 110 bytes (1 switches on core 0)
[pid: 4075|app: 0|req: 59/479] 218.247.217.98 () {48 vars in 951 bytes} [Tue Dec  4 10:39:37 2018] POST /select/by_path_name/ => generated 766 bytes in 30 msecs (HTTP/1.1 200) 3 headers in 101 bytes (1 switches on core 0)
[pid: 4071|app: 0|req: 59/480] 218.247.217.98 () {42 vars in 748 bytes} [Tue Dec  4 10:39:37 2018] GET /data/?page=3&limit=30 => generated 5460 bytes in 22 msecs (HTTP/1.1 200) 3 headers in 101 bytes (2 switches on core 0)
Internal Server Error: /update/spider_basic_info/by_path_name/
Traceback (most recent call last):
  File "/usr/local/lib/python3.6/site-packages/django/core/handlers/exception.py", line 34, in inner
    response = get_response(request)
  File "/usr/local/lib/python3.6/site-packages/django/core/handlers/base.py", line 126, in _get_response
    response = self.process_exception_by_middleware(e, request)
  File "/usr/local/lib/python3.6/site-packages/django/core/handlers/base.py", line 124, in _get_response
    response = wrapped_callback(request, *callback_args, **callback_kwargs)
  File "./twodj/views.py", line 301, in update_basic_info_by_path_name
    ip = va[0].__getattribute__('ip')
IndexError: list index out of range
[pid: 4074|app: 0|req: 59/481] 218.247.217.98 () {48 vars in 946 bytes} [Tue Dec  4 10:39:40 2018] POST /update/spider_basic_info/by_path_name/ => generated 12325 bytes in 50 msecs (HTTP/1.1 500) 4 headers in 145 bytes (1 switches on core 0)
[pid: 4073|app: 0|req: 55/482] 218.247.217.98 () {42 vars in 748 bytes} [Tue Dec  4 10:39:42 2018] GET /data/?page=2&limit=30 => generated 10885 bytes in 22 msecs (HTTP/1.1 200) 3 headers in 102 bytes (2 switches on core 0)
[pid: 4072|app: 0|req: 54/483] 218.247.217.98 () {42 vars in 808 bytes} [Tue Dec  4 10:39:49 2018] GET /demo/form?path_name=lyl_jiangsu => generated 9531 bytes in 1 msecs (HTTP/1.1 200) 3 headers in 110 bytes (1 switches on core 0)
[pid: 4075|app: 0|req: 60/484] 218.247.217.98 () {48 vars in 951 bytes} [Tue Dec  4 10:39:50 2018] POST /select/by_path_name/ => generated 707 bytes in 23 msecs (HTTP/1.1 200) 3 headers in 101 bytes (1 switches on core 0)
Internal Server Error: /update/spider_basic_info/by_path_name/
Traceback (most recent call last):
  File "/usr/local/lib/python3.6/site-packages/django/core/handlers/exception.py", line 34, in inner
    response = get_response(request)
  File "/usr/local/lib/python3.6/site-packages/django/core/handlers/base.py", line 126, in _get_response
    response = self.process_exception_by_middleware(e, request)
  File "/usr/local/lib/python3.6/site-packages/django/core/handlers/base.py", line 124, in _get_response
    response = wrapped_callback(request, *callback_args, **callback_kwargs)
  File "./twodj/views.py", line 311, in update_basic_info_by_path_name
    ip = va[0].__getattribute__('ip')
IndexError: list index out of range
[pid: 4071|app: 0|req: 60/485] 218.247.217.98 () {48 vars in 946 bytes} [Tue Dec  4 10:39:53 2018] POST /update/spider_basic_info/by_path_name/ => generated 12254 bytes in 37 msecs (HTTP/1.1 500) 4 headers in 145 bytes (1 switches on core 0)
[pid: 4074|app: 0|req: 60/486] 218.247.217.98 () {42 vars in 729 bytes} [Tue Dec  4 10:39:56 2018] GET /index => generated 7174 bytes in 1 msecs (HTTP/1.1 200) 3 headers in 110 bytes (1 switches on core 0)
[pid: 4073|app: 0|req: 56/487] 218.247.217.98 () {42 vars in 769 bytes} [Tue Dec  4 10:39:56 2018] GET /demo/welcome.html => generated 24253 bytes in 1 msecs (HTTP/1.1 200) 3 headers in 111 bytes (1 switches on core 0)
[pid: 4072|app: 0|req: 55/488] 218.247.217.98 () {40 vars in 652 bytes} [Tue Dec  4 10:39:56 2018] GET /js/index.js => generated 7174 bytes in 1 msecs (HTTP/1.1 200) 3 headers in 110 bytes (1 switches on core 0)
Not Found: /frame/static/js/vip_nav.js
[pid: 4075|app: 0|req: 61/489] 218.247.217.98 () {40 vars in 670 bytes} [Tue Dec  4 10:39:56 2018] GET /frame/static/js/vip_nav.js => generated 4584 bytes in 4 msecs (HTTP/1.1 404) 3 headers in 102 bytes (1 switches on core 0)
Not Found: /demo/vip_tab.js
[pid: 4071|app: 0|req: 61/490] 218.247.217.98 () {40 vars in 660 bytes} [Tue Dec  4 10:39:57 2018] GET /demo/vip_tab.js => generated 4551 bytes in 4 msecs (HTTP/1.1 404) 3 headers in 102 bytes (1 switches on core 0)
[pid: 4074|app: -1|req: -1/491] 218.247.217.98 () {44 vars in 769 bytes} [Tue Dec  4 10:39:57 2018] GET /src/frame/static/image/code.png => generated 2108 bytes in 0 msecs via sendfile() (HTTP/1.1 200) 3 headers in 112 bytes (0 switches on core 0)
[pid: 4073|app: 0|req: 57/492] 218.247.217.98 () {42 vars in 769 bytes} [Tue Dec  4 10:39:58 2018] GET /spider/basic.html => generated 12249 bytes in 1 msecs (HTTP/1.1 200) 3 headers in 111 bytes (1 switches on core 0)
[pid: 4072|app: 0|req: 56/493] 218.247.217.98 () {42 vars in 753 bytes} [Tue Dec  4 10:39:58 2018] GET /data/?page=1&limit=30 => generated 11502 bytes in 23 msecs (HTTP/1.1 200) 3 headers in 102 bytes (2 switches on core 0)
[pid: 4075|app: 0|req: 62/494] 218.247.217.98 () {42 vars in 753 bytes} [Tue Dec  4 10:40:12 2018] GET /data/?page=2&limit=30 => generated 10888 bytes in 26 msecs (HTTP/1.1 200) 3 headers in 102 bytes (2 switches on core 0)
[pid: 4071|app: 0|req: 62/495] 218.247.217.98 () {42 vars in 814 bytes} [Tue Dec  4 10:40:27 2018] GET /demo/form?path_name=lyl_beijing_ds => generated 9534 bytes in 1 msecs (HTTP/1.1 200) 3 headers in 110 bytes (1 switches on core 0)
[pid: 4074|app: 0|req: 61/496] 218.247.217.98 () {48 vars in 954 bytes} [Tue Dec  4 10:40:27 2018] POST /select/by_path_name/ => generated 740 bytes in 24 msecs (HTTP/1.1 200) 3 headers in 101 bytes (1 switches on core 0)
[pid: 4073|app: 0|req: 58/497] 218.247.217.98 () {48 vars in 949 bytes} [Tue Dec  4 10:40:53 2018] POST /update/spider_basic_info/by_path_name/ => generated 0 bytes in 59 msecs (HTTP/1.1 200) 3 headers in 107 bytes (1 switches on core 0)
[pid: 4072|app: 0|req: 57/498] 218.247.217.98 () {42 vars in 815 bytes} [Tue Dec  4 10:41:03 2018] GET /demo/form?path_name=yf_xzcf_env_jilin => generated 9537 bytes in 1 msecs (HTTP/1.1 200) 3 headers in 110 bytes (1 switches on core 0)
[pid: 4075|app: 0|req: 63/499] 218.247.217.98 () {48 vars in 952 bytes} [Tue Dec  4 10:41:03 2018] POST /select/by_path_name/ => generated 809 bytes in 26 msecs (HTTP/1.1 200) 3 headers in 101 bytes (1 switches on core 0)
[pid: 4071|app: 0|req: 63/500] 218.247.217.98 () {42 vars in 812 bytes} [Tue Dec  4 10:41:06 2018] GET /demo/form?path_name=lyl_dalian_ds => generated 9533 bytes in 1 msecs (HTTP/1.1 200) 3 headers in 110 bytes (1 switches on core 0)
[pid: 4074|app: 0|req: 62/501] 218.247.217.98 () {48 vars in 953 bytes} [Tue Dec  4 10:41:06 2018] POST /select/by_path_name/ => generated 738 bytes in 19 msecs (HTTP/1.1 200) 3 headers in 101 bytes (1 switches on core 0)
[pid: 4073|app: 0|req: 59/502] 218.247.217.98 () {48 vars in 948 bytes} [Tue Dec  4 10:41:27 2018] POST /update/spider_basic_info/by_path_name/ => generated 0 bytes in 53 msecs (HTTP/1.1 200) 3 headers in 107 bytes (1 switches on core 0)
[pid: 4072|app: 0|req: 58/503] 218.247.217.98 () {42 vars in 812 bytes} [Tue Dec  4 10:41:34 2018] GET /demo/form?path_name=lyl_hainan_ds => generated 9533 bytes in 1 msecs (HTTP/1.1 200) 3 headers in 110 bytes (1 switches on core 0)
[pid: 4075|app: 0|req: 64/504] 218.247.217.98 () {48 vars in 953 bytes} [Tue Dec  4 10:41:34 2018] POST /select/by_path_name/ => generated 742 bytes in 24 msecs (HTTP/1.1 200) 3 headers in 101 bytes (1 switches on core 0)
[pid: 4071|app: 0|req: 64/505] 218.247.217.98 () {48 vars in 948 bytes} [Tue Dec  4 10:41:46 2018] POST /update/spider_basic_info/by_path_name/ => generated 0 bytes in 45 msecs (HTTP/1.1 200) 3 headers in 107 bytes (1 switches on core 0)
[pid: 4074|app: 0|req: 63/506] 218.247.217.98 () {42 vars in 808 bytes} [Tue Dec  4 10:41:51 2018] GET /demo/form?path_name=lyl_jiangsu => generated 9531 bytes in 1 msecs (HTTP/1.1 200) 3 headers in 110 bytes (1 switches on core 0)
[pid: 4073|app: 0|req: 60/507] 218.247.217.98 () {48 vars in 951 bytes} [Tue Dec  4 10:41:51 2018] POST /select/by_path_name/ => generated 710 bytes in 18 msecs (HTTP/1.1 200) 3 headers in 101 bytes (1 switches on core 0)
[pid: 4072|app: 0|req: 59/508] 218.247.217.98 () {42 vars in 811 bytes} [Tue Dec  4 10:42:26 2018] GET /demo/detail_form?path_name=yf_weibo => generated 8860 bytes in 1 msecs (HTTP/1.1 200) 3 headers in 110 bytes (1 switches on core 0)
[pid: 4075|app: 0|req: 65/509] 218.247.217.98 () {48 vars in 950 bytes} [Tue Dec  4 10:42:26 2018] POST /select/by_path_name/ => generated 738 bytes in 25 msecs (HTTP/1.1 200) 3 headers in 101 bytes (1 switches on core 0)
[pid: 4071|app: 0|req: 65/510] 218.247.217.98 () {42 vars in 808 bytes} [Tue Dec  4 10:42:52 2018] GET /demo/form?path_name=lyl_jiangsu => generated 9531 bytes in 1 msecs (HTTP/1.1 200) 3 headers in 110 bytes (1 switches on core 0)
[pid: 4074|app: 0|req: 64/511] 218.247.217.98 () {48 vars in 951 bytes} [Tue Dec  4 10:42:52 2018] POST /select/by_path_name/ => generated 710 bytes in 19 msecs (HTTP/1.1 200) 3 headers in 101 bytes (1 switches on core 0)
[pid: 4073|app: 0|req: 61/512] 218.247.217.98 () {42 vars in 729 bytes} [Tue Dec  4 10:42:58 2018] GET /index => generated 7174 bytes in 1 msecs (HTTP/1.1 200) 3 headers in 110 bytes (1 switches on core 0)
[pid: 4072|app: 0|req: 60/513] 218.247.217.98 () {42 vars in 769 bytes} [Tue Dec  4 10:42:58 2018] GET /demo/welcome.html => generated 24253 bytes in 1 msecs (HTTP/1.1 200) 3 headers in 111 bytes (1 switches on core 0)
[pid: 4075|app: 0|req: 66/514] 218.247.217.98 () {40 vars in 652 bytes} [Tue Dec  4 10:42:58 2018] GET /js/index.js => generated 7174 bytes in 1 msecs (HTTP/1.1 200) 3 headers in 110 bytes (1 switches on core 0)
Not Found: /frame/static/js/vip_nav.js
[pid: 4071|app: 0|req: 66/515] 218.247.217.98 () {40 vars in 670 bytes} [Tue Dec  4 10:42:59 2018] GET /frame/static/js/vip_nav.js => generated 4584 bytes in 5 msecs (HTTP/1.1 404) 3 headers in 102 bytes (1 switches on core 0)
[pid: 4073|app: -1|req: -1/516] 218.247.217.98 () {44 vars in 769 bytes} [Tue Dec  4 10:42:59 2018] GET /src/frame/static/image/code.png => generated 2108 bytes in 0 msecs via sendfile() (HTTP/1.1 200) 3 headers in 112 bytes (0 switches on core 0)
Not Found: /demo/vip_tab.js
[pid: 4074|app: 0|req: 65/517] 218.247.217.98 () {40 vars in 660 bytes} [Tue Dec  4 10:42:59 2018] GET /demo/vip_tab.js => generated 4551 bytes in 4 msecs (HTTP/1.1 404) 3 headers in 102 bytes (1 switches on core 0)
[pid: 4072|app: 0|req: 61/518] 218.247.217.98 () {42 vars in 769 bytes} [Tue Dec  4 10:43:00 2018] GET /spider/basic.html => generated 12249 bytes in 1 msecs (HTTP/1.1 200) 3 headers in 111 bytes (1 switches on core 0)
[pid: 4075|app: 0|req: 67/519] 218.247.217.98 () {42 vars in 753 bytes} [Tue Dec  4 10:43:00 2018] GET /data/?page=1&limit=30 => generated 11502 bytes in 26 msecs (HTTP/1.1 200) 3 headers in 102 bytes (2 switches on core 0)
[pid: 4071|app: 0|req: 67/520] 218.247.217.98 () {42 vars in 753 bytes} [Tue Dec  4 10:43:04 2018] GET /data/?page=2&limit=30 => generated 11047 bytes in 24 msecs (HTTP/1.1 200) 3 headers in 102 bytes (2 switches on core 0)
[pid: 4073|app: 0|req: 62/521] 218.247.217.98 () {42 vars in 814 bytes} [Tue Dec  4 10:43:14 2018] GET /demo/form?path_name=lyl_beijing_yj => generated 9534 bytes in 1 msecs (HTTP/1.1 200) 3 headers in 110 bytes (1 switches on core 0)
[pid: 4074|app: 0|req: 66/522] 218.247.217.98 () {48 vars in 954 bytes} [Tue Dec  4 10:43:14 2018] POST /select/by_path_name/ => generated 796 bytes in 21 msecs (HTTP/1.1 200) 3 headers in 101 bytes (1 switches on core 0)
[pid: 4072|app: 0|req: 62/523] 218.247.217.98 () {48 vars in 949 bytes} [Tue Dec  4 10:43:19 2018] POST /update/spider_basic_info/by_path_name/ => generated 0 bytes in 43 msecs (HTTP/1.1 200) 3 headers in 107 bytes (1 switches on core 0)
[pid: 4075|app: 0|req: 68/524] 218.247.217.98 () {42 vars in 814 bytes} [Tue Dec  4 10:43:38 2018] GET /demo/form?path_name=lyl_jiangsu_ds => generated 9534 bytes in 1 msecs (HTTP/1.1 200) 3 headers in 110 bytes (1 switches on core 0)
[pid: 4071|app: 0|req: 68/525] 218.247.217.98 () {48 vars in 954 bytes} [Tue Dec  4 10:43:38 2018] POST /select/by_path_name/ => generated 772 bytes in 31 msecs (HTTP/1.1 200) 3 headers in 101 bytes (1 switches on core 0)
Internal Server Error: /update/spider_basic_info/by_path_name/
Traceback (most recent call last):
  File "/usr/local/lib/python3.6/site-packages/django/core/handlers/exception.py", line 34, in inner
    response = get_response(request)
  File "/usr/local/lib/python3.6/site-packages/django/core/handlers/base.py", line 126, in _get_response
    response = self.process_exception_by_middleware(e, request)
  File "/usr/local/lib/python3.6/site-packages/django/core/handlers/base.py", line 124, in _get_response
    response = wrapped_callback(request, *callback_args, **callback_kwargs)
  File "./twodj/views.py", line 301, in update_basic_info_by_path_name
    ip = va[0].__getattribute__('ip')
IndexError: list index out of range
[pid: 4073|app: 0|req: 63/526] 218.247.217.98 () {48 vars in 949 bytes} [Tue Dec  4 10:43:49 2018] POST /update/spider_basic_info/by_path_name/ => generated 12355 bytes in 62 msecs (HTTP/1.1 500) 4 headers in 145 bytes (1 switches on core 0)
[pid: 4074|app: 0|req: 67/527] 218.247.217.98 () {42 vars in 729 bytes} [Tue Dec  4 10:43:53 2018] GET /index => generated 7174 bytes in 2 msecs (HTTP/1.1 200) 3 headers in 110 bytes (1 switches on core 0)
[pid: 4072|app: 0|req: 63/528] 218.247.217.98 () {42 vars in 769 bytes} [Tue Dec  4 10:43:54 2018] GET /demo/welcome.html => generated 24253 bytes in 1 msecs (HTTP/1.1 200) 3 headers in 111 bytes (1 switches on core 0)
[pid: 4075|app: 0|req: 69/529] 218.247.217.98 () {40 vars in 652 bytes} [Tue Dec  4 10:43:54 2018] GET /js/index.js => generated 7174 bytes in 1 msecs (HTTP/1.1 200) 3 headers in 110 bytes (1 switches on core 0)
Not Found: /frame/static/js/vip_nav.js
[pid: 4071|app: 0|req: 69/530] 218.247.217.98 () {40 vars in 670 bytes} [Tue Dec  4 10:43:54 2018] GET /frame/static/js/vip_nav.js => generated 4584 bytes in 4 msecs (HTTP/1.1 404) 3 headers in 102 bytes (1 switches on core 0)
[pid: 4073|app: -1|req: -1/531] 218.247.217.98 () {44 vars in 769 bytes} [Tue Dec  4 10:43:54 2018] GET /src/frame/static/image/code.png => generated 2108 bytes in 0 msecs via sendfile() (HTTP/1.1 200) 3 headers in 112 bytes (0 switches on core 0)
Not Found: /demo/vip_tab.js
[pid: 4074|app: 0|req: 68/532] 218.247.217.98 () {40 vars in 660 bytes} [Tue Dec  4 10:43:54 2018] GET /demo/vip_tab.js => generated 4551 bytes in 4 msecs (HTTP/1.1 404) 3 headers in 102 bytes (1 switches on core 0)
[pid: 4072|app: 0|req: 64/533] 218.247.217.98 () {42 vars in 769 bytes} [Tue Dec  4 10:43:55 2018] GET /spider/basic.html => generated 12249 bytes in 1 msecs (HTTP/1.1 200) 3 headers in 111 bytes (1 switches on core 0)
[pid: 4075|app: 0|req: 70/534] 218.247.217.98 () {42 vars in 753 bytes} [Tue Dec  4 10:43:55 2018] GET /data/?page=1&limit=30 => generated 11502 bytes in 23 msecs (HTTP/1.1 200) 3 headers in 102 bytes (2 switches on core 0)
[pid: 4071|app: 0|req: 70/535] 218.247.217.98 () {42 vars in 753 bytes} [Tue Dec  4 10:43:58 2018] GET /data/?page=3&limit=30 => generated 5460 bytes in 22 msecs (HTTP/1.1 200) 3 headers in 101 bytes (2 switches on core 0)
[pid: 4073|app: 0|req: 64/536] 218.247.217.98 () {42 vars in 753 bytes} [Tue Dec  4 10:43:59 2018] GET /data/?page=2&limit=30 => generated 11103 bytes in 24 msecs (HTTP/1.1 200) 3 headers in 102 bytes (2 switches on core 0)
[pid: 4074|app: 0|req: 69/537] 218.247.217.98 () {42 vars in 808 bytes} [Tue Dec  4 10:44:10 2018] GET /demo/form?path_name=lyl_jiangsu => generated 9531 bytes in 1 msecs (HTTP/1.1 200) 3 headers in 110 bytes (1 switches on core 0)
[pid: 4072|app: 0|req: 65/538] 218.247.217.98 () {48 vars in 951 bytes} [Tue Dec  4 10:44:11 2018] POST /select/by_path_name/ => generated 710 bytes in 19 msecs (HTTP/1.1 200) 3 headers in 101 bytes (1 switches on core 0)
Internal Server Error: /update/spider_basic_info/by_path_name/
Traceback (most recent call last):
  File "/usr/local/lib/python3.6/site-packages/django/core/handlers/exception.py", line 34, in inner
    response = get_response(request)
  File "/usr/local/lib/python3.6/site-packages/django/core/handlers/base.py", line 126, in _get_response
    response = self.process_exception_by_middleware(e, request)
  File "/usr/local/lib/python3.6/site-packages/django/core/handlers/base.py", line 124, in _get_response
    response = wrapped_callback(request, *callback_args, **callback_kwargs)
  File "./twodj/views.py", line 311, in update_basic_info_by_path_name
    ip = va[0].__getattribute__('ip')
IndexError: list index out of range
[pid: 4075|app: 0|req: 71/539] 218.247.217.98 () {48 vars in 946 bytes} [Tue Dec  4 10:44:15 2018] POST /update/spider_basic_info/by_path_name/ => generated 12257 bytes in 50 msecs (HTTP/1.1 500) 4 headers in 145 bytes (1 switches on core 0)
[pid: 4071|app: 0|req: 71/540] 218.247.217.98 () {42 vars in 748 bytes} [Tue Dec  4 10:44:23 2018] GET /data/?page=3&limit=30 => generated 5460 bytes in 25 msecs (HTTP/1.1 200) 3 headers in 101 bytes (2 switches on core 0)
[pid: 4073|app: 0|req: 65/541] 218.247.217.98 () {42 vars in 808 bytes} [Tue Dec  4 10:44:30 2018] GET /demo/form?path_name=lyl_landtax => generated 9531 bytes in 1 msecs (HTTP/1.1 200) 3 headers in 110 bytes (1 switches on core 0)
[pid: 4074|app: 0|req: 70/542] 218.247.217.98 () {48 vars in 951 bytes} [Tue Dec  4 10:44:30 2018] POST /select/by_path_name/ => generated 769 bytes in 24 msecs (HTTP/1.1 200) 3 headers in 101 bytes (1 switches on core 0)
Internal Server Error: /update/spider_basic_info/by_path_name/
Traceback (most recent call last):
  File "/usr/local/lib/python3.6/site-packages/django/core/handlers/exception.py", line 34, in inner
    response = get_response(request)
  File "/usr/local/lib/python3.6/site-packages/django/core/handlers/base.py", line 126, in _get_response
    response = self.process_exception_by_middleware(e, request)
  File "/usr/local/lib/python3.6/site-packages/django/core/handlers/base.py", line 124, in _get_response
    response = wrapped_callback(request, *callback_args, **callback_kwargs)
  File "./twodj/views.py", line 301, in update_basic_info_by_path_name
    ip = va[0].__getattribute__('ip')
IndexError: list index out of range
[pid: 4072|app: 0|req: 66/543] 218.247.217.98 () {48 vars in 946 bytes} [Tue Dec  4 10:44:43 2018] POST /update/spider_basic_info/by_path_name/ => generated 12349 bytes in 66 msecs (HTTP/1.1 500) 4 headers in 145 bytes (1 switches on core 0)
[pid: 4075|app: 0|req: 72/544] 218.247.217.98 () {42 vars in 810 bytes} [Tue Dec  4 10:44:53 2018] GET /demo/form?path_name=lyl_markname => generated 9532 bytes in 1 msecs (HTTP/1.1 200) 3 headers in 110 bytes (1 switches on core 0)
[pid: 4071|app: 0|req: 72/545] 218.247.217.98 () {48 vars in 952 bytes} [Tue Dec  4 10:44:53 2018] POST /select/by_path_name/ => generated 746 bytes in 24 msecs (HTTP/1.1 200) 3 headers in 101 bytes (1 switches on core 0)
Internal Server Error: /update/spider_basic_info/by_path_name/
Traceback (most recent call last):
  File "/usr/local/lib/python3.6/site-packages/django/core/handlers/exception.py", line 34, in inner
    response = get_response(request)
  File "/usr/local/lib/python3.6/site-packages/django/core/handlers/base.py", line 126, in _get_response
    response = self.process_exception_by_middleware(e, request)
  File "/usr/local/lib/python3.6/site-packages/django/core/handlers/base.py", line 124, in _get_response
    response = wrapped_callback(request, *callback_args, **callback_kwargs)
  File "./twodj/views.py", line 301, in update_basic_info_by_path_name
    ip = va[0].__getattribute__('ip')
IndexError: list index out of range
[pid: 4073|app: 0|req: 66/546] 218.247.217.98 () {48 vars in 947 bytes} [Tue Dec  4 10:45:13 2018] POST /update/spider_basic_info/by_path_name/ => generated 12322 bytes in 47 msecs (HTTP/1.1 500) 4 headers in 145 bytes (1 switches on core 0)
[pid: 4074|app: 0|req: 71/547] 218.247.217.98 () {42 vars in 818 bytes} [Tue Dec  4 10:45:24 2018] GET /demo/form?path_name=lyl_neimenggu_ds => generated 9536 bytes in 1 msecs (HTTP/1.1 200) 3 headers in 110 bytes (1 switches on core 0)
[pid: 4072|app: 0|req: 67/548] 218.247.217.98 () {48 vars in 956 bytes} [Tue Dec  4 10:45:25 2018] POST /select/by_path_name/ => generated 744 bytes in 30 msecs (HTTP/1.1 200) 3 headers in 101 bytes (1 switches on core 0)
[pid: 4075|app: 0|req: 73/549] 218.247.217.98 () {48 vars in 951 bytes} [Tue Dec  4 10:45:34 2018] POST /update/spider_basic_info/by_path_name/ => generated 0 bytes in 49 msecs (HTTP/1.1 200) 3 headers in 107 bytes (1 switches on core 0)
[pid: 4071|app: 0|req: 73/550] 218.247.217.98 () {42 vars in 729 bytes} [Tue Dec  4 10:45:37 2018] GET /index => generated 7174 bytes in 1 msecs (HTTP/1.1 200) 3 headers in 110 bytes (1 switches on core 0)
[pid: 4073|app: 0|req: 67/551] 218.247.217.98 () {42 vars in 769 bytes} [Tue Dec  4 10:45:37 2018] GET /demo/welcome.html => generated 24253 bytes in 1 msecs (HTTP/1.1 200) 3 headers in 111 bytes (1 switches on core 0)
[pid: 4074|app: 0|req: 72/552] 218.247.217.98 () {40 vars in 652 bytes} [Tue Dec  4 10:45:37 2018] GET /js/index.js => generated 7174 bytes in 1 msecs (HTTP/1.1 200) 3 headers in 110 bytes (1 switches on core 0)
Not Found: /frame/static/js/vip_nav.js
[pid: 4072|app: 0|req: 68/553] 218.247.217.98 () {40 vars in 670 bytes} [Tue Dec  4 10:45:37 2018] GET /frame/static/js/vip_nav.js => generated 4584 bytes in 4 msecs (HTTP/1.1 404) 3 headers in 102 bytes (1 switches on core 0)
[pid: 4071|app: -1|req: -1/554] 218.247.217.98 () {44 vars in 769 bytes} [Tue Dec  4 10:45:38 2018] GET /src/frame/static/image/code.png => generated 2108 bytes in 0 msecs via sendfile() (HTTP/1.1 200) 3 headers in 112 bytes (0 switches on core 0)
Not Found: /demo/vip_tab.js
[pid: 4075|app: 0|req: 74/555] 218.247.217.98 () {40 vars in 660 bytes} [Tue Dec  4 10:45:38 2018] GET /demo/vip_tab.js => generated 4551 bytes in 5 msecs (HTTP/1.1 404) 3 headers in 102 bytes (1 switches on core 0)
[pid: 4073|app: 0|req: 68/556] 218.247.217.98 () {42 vars in 769 bytes} [Tue Dec  4 10:45:39 2018] GET /spider/basic.html => generated 12249 bytes in 1 msecs (HTTP/1.1 200) 3 headers in 111 bytes (1 switches on core 0)
[pid: 4074|app: 0|req: 73/557] 218.247.217.98 () {42 vars in 753 bytes} [Tue Dec  4 10:45:39 2018] GET /data/?page=1&limit=30 => generated 11502 bytes in 43 msecs (HTTP/1.1 200) 3 headers in 102 bytes (2 switches on core 0)
[pid: 4072|app: 0|req: 69/558] 218.247.217.98 () {42 vars in 753 bytes} [Tue Dec  4 10:45:43 2018] GET /data/?page=2&limit=30 => generated 11245 bytes in 24 msecs (HTTP/1.1 200) 3 headers in 102 bytes (2 switches on core 0)
[pid: 4071|app: 0|req: 74/559] 218.247.217.98 () {42 vars in 814 bytes} [Tue Dec  4 10:46:11 2018] GET /demo/form?path_name=lyl_ningxia_ds => generated 9534 bytes in 1 msecs (HTTP/1.1 200) 3 headers in 110 bytes (1 switches on core 0)
[pid: 4075|app: 0|req: 75/560] 218.247.217.98 () {48 vars in 954 bytes} [Tue Dec  4 10:46:12 2018] POST /select/by_path_name/ => generated 740 bytes in 25 msecs (HTTP/1.1 200) 3 headers in 101 bytes (1 switches on core 0)
[pid: 4073|app: 0|req: 69/561] 218.247.217.98 () {48 vars in 949 bytes} [Tue Dec  4 10:46:19 2018] POST /update/spider_basic_info/by_path_name/ => generated 0 bytes in 60 msecs (HTTP/1.1 200) 3 headers in 107 bytes (1 switches on core 0)
[pid: 4074|app: 0|req: 74/562] 218.247.217.98 () {42 vars in 814 bytes} [Tue Dec  4 10:46:23 2018] GET /demo/form?path_name=lyl_tianjin_ds => generated 9534 bytes in 1 msecs (HTTP/1.1 200) 3 headers in 110 bytes (1 switches on core 0)
[pid: 4072|app: 0|req: 70/563] 218.247.217.98 () {48 vars in 954 bytes} [Tue Dec  4 10:46:24 2018] POST /select/by_path_name/ => generated 740 bytes in 23 msecs (HTTP/1.1 200) 3 headers in 101 bytes (1 switches on core 0)
[pid: 4071|app: 0|req: 75/564] 218.247.217.98 () {48 vars in 949 bytes} [Tue Dec  4 10:46:32 2018] POST /update/spider_basic_info/by_path_name/ => generated 0 bytes in 36 msecs (HTTP/1.1 200) 3 headers in 107 bytes (1 switches on core 0)
[pid: 4075|app: 0|req: 76/565] 218.247.217.98 () {42 vars in 753 bytes} [Tue Dec  4 10:46:49 2018] GET /data/?page=3&limit=30 => generated 5460 bytes in 24 msecs (HTTP/1.1 200) 3 headers in 101 bytes (2 switches on core 0)
[pid: 4073|app: 0|req: 70/566] 218.247.217.98 () {42 vars in 729 bytes} [Tue Dec  4 10:46:54 2018] GET /index => generated 7174 bytes in 1 msecs (HTTP/1.1 200) 3 headers in 110 bytes (1 switches on core 0)
[pid: 4074|app: 0|req: 75/567] 218.247.217.98 () {42 vars in 769 bytes} [Tue Dec  4 10:46:54 2018] GET /demo/welcome.html => generated 24253 bytes in 1 msecs (HTTP/1.1 200) 3 headers in 111 bytes (1 switches on core 0)
[pid: 4072|app: 0|req: 71/568] 218.247.217.98 () {40 vars in 652 bytes} [Tue Dec  4 10:46:54 2018] GET /js/index.js => generated 7174 bytes in 1 msecs (HTTP/1.1 200) 3 headers in 110 bytes (1 switches on core 0)
Not Found: /frame/static/js/vip_nav.js
[pid: 4071|app: 0|req: 76/569] 218.247.217.98 () {40 vars in 670 bytes} [Tue Dec  4 10:46:55 2018] GET /frame/static/js/vip_nav.js => generated 4584 bytes in 23 msecs (HTTP/1.1 404) 3 headers in 102 bytes (1 switches on core 0)
[pid: 4075|app: -1|req: -1/570] 218.247.217.98 () {44 vars in 769 bytes} [Tue Dec  4 10:46:55 2018] GET /src/frame/static/image/code.png => generated 2108 bytes in 0 msecs via sendfile() (HTTP/1.1 200) 3 headers in 112 bytes (0 switches on core 0)
Not Found: /demo/vip_tab.js
[pid: 4073|app: 0|req: 71/571] 218.247.217.98 () {40 vars in 660 bytes} [Tue Dec  4 10:46:55 2018] GET /demo/vip_tab.js => generated 4551 bytes in 4 msecs (HTTP/1.1 404) 3 headers in 102 bytes (1 switches on core 0)
[pid: 4074|app: 0|req: 76/572] 218.247.217.98 () {42 vars in 769 bytes} [Tue Dec  4 10:46:55 2018] GET /spider/basic.html => generated 12249 bytes in 1 msecs (HTTP/1.1 200) 3 headers in 111 bytes (1 switches on core 0)
[pid: 4072|app: 0|req: 72/573] 218.247.217.98 () {42 vars in 753 bytes} [Tue Dec  4 10:46:56 2018] GET /data/?page=1&limit=30 => generated 11502 bytes in 25 msecs (HTTP/1.1 200) 3 headers in 102 bytes (2 switches on core 0)
[pid: 4071|app: 0|req: 77/574] 218.247.217.98 () {42 vars in 753 bytes} [Tue Dec  4 10:46:59 2018] GET /data/?page=2&limit=30 => generated 11351 bytes in 29 msecs (HTTP/1.1 200) 3 headers in 102 bytes (2 switches on core 0)
[pid: 4075|app: 0|req: 77/575] 218.247.217.98 () {42 vars in 814 bytes} [Tue Dec  4 10:47:14 2018] GET /demo/form?path_name=lyl_qinghai_ds => generated 9534 bytes in 1 msecs (HTTP/1.1 200) 3 headers in 110 bytes (1 switches on core 0)
[pid: 4073|app: 0|req: 72/576] 218.247.217.98 () {48 vars in 954 bytes} [Tue Dec  4 10:47:15 2018] POST /select/by_path_name/ => generated 740 bytes in 23 msecs (HTTP/1.1 200) 3 headers in 101 bytes (1 switches on core 0)
[pid: 4074|app: 0|req: 77/577] 218.247.217.98 () {48 vars in 949 bytes} [Tue Dec  4 10:47:24 2018] POST /update/spider_basic_info/by_path_name/ => generated 0 bytes in 60 msecs (HTTP/1.1 200) 3 headers in 107 bytes (1 switches on core 0)
[pid: 4072|app: 0|req: 73/578] 218.247.217.98 () {42 vars in 724 bytes} [Tue Dec  4 10:47:25 2018] GET /index => generated 7174 bytes in 1 msecs (HTTP/1.1 200) 3 headers in 110 bytes (1 switches on core 0)
[pid: 4071|app: 0|req: 78/579] 218.247.217.98 () {42 vars in 764 bytes} [Tue Dec  4 10:47:25 2018] GET /demo/welcome.html => generated 24253 bytes in 1 msecs (HTTP/1.1 200) 3 headers in 111 bytes (1 switches on core 0)
[pid: 4075|app: 0|req: 78/580] 218.247.217.98 () {40 vars in 647 bytes} [Tue Dec  4 10:47:25 2018] GET /js/index.js => generated 7174 bytes in 1 msecs (HTTP/1.1 200) 3 headers in 110 bytes (1 switches on core 0)
Not Found: /frame/static/js/vip_nav.js
[pid: 4073|app: 0|req: 73/581] 218.247.217.98 () {40 vars in 665 bytes} [Tue Dec  4 10:47:26 2018] GET /frame/static/js/vip_nav.js => generated 4584 bytes in 4 msecs (HTTP/1.1 404) 3 headers in 102 bytes (1 switches on core 0)
Not Found: /demo/vip_tab.js
[pid: 4074|app: 0|req: 78/582] 218.247.217.98 () {40 vars in 655 bytes} [Tue Dec  4 10:47:26 2018] GET /demo/vip_tab.js => generated 4551 bytes in 4 msecs (HTTP/1.1 404) 3 headers in 102 bytes (1 switches on core 0)
[pid: 4072|app: 0|req: 74/583] 218.247.217.98 () {42 vars in 764 bytes} [Tue Dec  4 10:47:26 2018] GET /spider/basic.html => generated 12176 bytes in 1 msecs (HTTP/1.1 200) 3 headers in 111 bytes (1 switches on core 0)
[pid: 4071|app: 0|req: 79/584] 218.247.217.98 () {42 vars in 748 bytes} [Tue Dec  4 10:47:26 2018] GET /data/?page=1&limit=30 => generated 11502 bytes in 17 msecs (HTTP/1.1 200) 3 headers in 102 bytes (2 switches on core 0)
[pid: 4075|app: 0|req: 79/585] 218.247.217.98 () {42 vars in 729 bytes} [Tue Dec  4 10:47:31 2018] GET /index => generated 7174 bytes in 1 msecs (HTTP/1.1 200) 3 headers in 110 bytes (1 switches on core 0)
[pid: 4073|app: 0|req: 74/586] 218.247.217.98 () {42 vars in 769 bytes} [Tue Dec  4 10:47:31 2018] GET /demo/welcome.html => generated 24253 bytes in 1 msecs (HTTP/1.1 200) 3 headers in 111 bytes (1 switches on core 0)
[pid: 4074|app: 0|req: 79/587] 218.247.217.98 () {40 vars in 652 bytes} [Tue Dec  4 10:47:32 2018] GET /js/index.js => generated 7174 bytes in 1 msecs (HTTP/1.1 200) 3 headers in 110 bytes (1 switches on core 0)
Not Found: /frame/static/js/vip_nav.js
[pid: 4072|app: 0|req: 75/588] 218.247.217.98 () {40 vars in 670 bytes} [Tue Dec  4 10:47:32 2018] GET /frame/static/js/vip_nav.js => generated 4584 bytes in 4 msecs (HTTP/1.1 404) 3 headers in 102 bytes (1 switches on core 0)
Not Found: /demo/vip_tab.js
[pid: 4071|app: 0|req: 80/589] 218.247.217.98 () {40 vars in 660 bytes} [Tue Dec  4 10:47:32 2018] GET /demo/vip_tab.js => generated 4551 bytes in 4 msecs (HTTP/1.1 404) 3 headers in 102 bytes (1 switches on core 0)
[pid: 4075|app: -1|req: -1/590] 218.247.217.98 () {44 vars in 769 bytes} [Tue Dec  4 10:47:32 2018] GET /src/frame/static/image/code.png => generated 2108 bytes in 0 msecs via sendfile() (HTTP/1.1 200) 3 headers in 112 bytes (0 switches on core 0)
[pid: 4073|app: 0|req: 75/591] 218.247.217.98 () {42 vars in 769 bytes} [Tue Dec  4 10:47:33 2018] GET /spider/basic.html => generated 12176 bytes in 1 msecs (HTTP/1.1 200) 3 headers in 111 bytes (1 switches on core 0)
[pid: 4074|app: 0|req: 80/592] 218.247.217.98 () {42 vars in 753 bytes} [Tue Dec  4 10:47:33 2018] GET /data/?page=1&limit=30 => generated 11502 bytes in 24 msecs (HTTP/1.1 200) 3 headers in 102 bytes (2 switches on core 0)
[pid: 4072|app: 0|req: 76/593] 218.247.217.98 () {42 vars in 779 bytes} [Tue Dec  4 10:47:36 2018] GET /spider/distribute.html => generated 3960 bytes in 1 msecs (HTTP/1.1 200) 3 headers in 110 bytes (1 switches on core 0)
[pid: 4071|app: 0|req: 81/594] 218.247.217.98 () {42 vars in 772 bytes} [Tue Dec  4 10:47:36 2018] GET /distribute_/?page=1&limit=20 => generated 6706 bytes in 30 msecs (HTTP/1.1 200) 3 headers in 101 bytes (2 switches on core 0)
[pid: 4075|app: 0|req: 80/595] 218.247.217.98 () {42 vars in 753 bytes} [Tue Dec  4 10:47:42 2018] GET /data/?page=2&limit=30 => generated 11404 bytes in 31 msecs (HTTP/1.1 200) 3 headers in 102 bytes (2 switches on core 0)
[pid: 4073|app: 0|req: 76/596] 218.247.217.98 () {42 vars in 818 bytes} [Tue Dec  4 10:47:53 2018] GET /demo/form?path_name=lyl_trademarking => generated 9536 bytes in 1 msecs (HTTP/1.1 200) 3 headers in 110 bytes (1 switches on core 0)
[pid: 4074|app: 0|req: 81/597] 218.247.217.98 () {48 vars in 956 bytes} [Tue Dec  4 10:47:54 2018] POST /select/by_path_name/ => generated 776 bytes in 30 msecs (HTTP/1.1 200) 3 headers in 101 bytes (1 switches on core 0)
Internal Server Error: /update/spider_basic_info/by_path_name/
Traceback (most recent call last):
  File "/usr/local/lib/python3.6/site-packages/django/core/handlers/exception.py", line 34, in inner
    response = get_response(request)
  File "/usr/local/lib/python3.6/site-packages/django/core/handlers/base.py", line 126, in _get_response
    response = self.process_exception_by_middleware(e, request)
  File "/usr/local/lib/python3.6/site-packages/django/core/handlers/base.py", line 124, in _get_response
    response = wrapped_callback(request, *callback_args, **callback_kwargs)
  File "./twodj/views.py", line 301, in update_basic_info_by_path_name
    ip = va[0].__getattribute__('ip')
IndexError: list index out of range
[pid: 4072|app: 0|req: 77/598] 218.247.217.98 () {48 vars in 951 bytes} [Tue Dec  4 10:48:08 2018] POST /update/spider_basic_info/by_path_name/ => generated 12362 bytes in 47 msecs (HTTP/1.1 500) 4 headers in 145 bytes (1 switches on core 0)
[pid: 4071|app: 0|req: 82/599] 218.247.217.98 () {42 vars in 724 bytes} [Tue Dec  4 10:48:37 2018] GET /index => generated 7174 bytes in 1 msecs (HTTP/1.1 200) 3 headers in 110 bytes (1 switches on core 0)
[pid: 4075|app: 0|req: 81/600] 218.247.217.98 () {42 vars in 764 bytes} [Tue Dec  4 10:48:37 2018] GET /demo/welcome.html => generated 24253 bytes in 1 msecs (HTTP/1.1 200) 3 headers in 111 bytes (1 switches on core 0)
[pid: 4073|app: 0|req: 77/601] 218.247.217.98 () {40 vars in 647 bytes} [Tue Dec  4 10:48:37 2018] GET /js/index.js => generated 7174 bytes in 1 msecs (HTTP/1.1 200) 3 headers in 110 bytes (1 switches on core 0)
Not Found: /frame/static/js/vip_nav.js
[pid: 4074|app: 0|req: 82/602] 218.247.217.98 () {40 vars in 665 bytes} [Tue Dec  4 10:48:37 2018] GET /frame/static/js/vip_nav.js => generated 4584 bytes in 4 msecs (HTTP/1.1 404) 3 headers in 102 bytes (1 switches on core 0)
Not Found: /demo/vip_tab.js
[pid: 4072|app: 0|req: 78/603] 218.247.217.98 () {40 vars in 655 bytes} [Tue Dec  4 10:48:37 2018] GET /demo/vip_tab.js => generated 4551 bytes in 4 msecs (HTTP/1.1 404) 3 headers in 102 bytes (1 switches on core 0)
[pid: 4071|app: 0|req: 83/604] 218.247.217.98 () {42 vars in 764 bytes} [Tue Dec  4 10:48:38 2018] GET /spider/basic.html => generated 12174 bytes in 1 msecs (HTTP/1.1 200) 3 headers in 111 bytes (1 switches on core 0)
[pid: 4075|app: 0|req: 82/605] 218.247.217.98 () {42 vars in 748 bytes} [Tue Dec  4 10:48:38 2018] GET /data/?page=1&limit=30 => generated 11502 bytes in 26 msecs (HTTP/1.1 200) 3 headers in 102 bytes (2 switches on core 0)
[pid: 4073|app: 0|req: 78/606] 218.247.217.98 () {42 vars in 803 bytes} [Tue Dec  4 10:49:31 2018] GET /demo/form?path_name=yf_icp_info => generated 9531 bytes in 1 msecs (HTTP/1.1 200) 3 headers in 110 bytes (1 switches on core 0)
[pid: 4074|app: 0|req: 83/607] 218.247.217.98 () {48 vars in 946 bytes} [Tue Dec  4 10:49:32 2018] POST /select/by_path_name/ => generated 806 bytes in 32 msecs (HTTP/1.1 200) 3 headers in 101 bytes (1 switches on core 0)
[pid: 4072|app: 0|req: 79/608] 218.247.217.98 () {42 vars in 797 bytes} [Tue Dec  4 10:49:35 2018] GET /demo/form?path_name=yf_demo2 => generated 9528 bytes in 1 msecs (HTTP/1.1 200) 3 headers in 110 bytes (1 switches on core 0)
[pid: 4071|app: 0|req: 84/609] 218.247.217.98 () {48 vars in 943 bytes} [Tue Dec  4 10:49:35 2018] POST /select/by_path_name/ => generated 740 bytes in 31 msecs (HTTP/1.1 200) 3 headers in 101 bytes (1 switches on core 0)
[pid: 4075|app: 0|req: 83/610] 218.247.217.98 () {42 vars in 819 bytes} [Tue Dec  4 10:49:37 2018] GET /demo/form?path_name=hyg_ald_app_gzhlogo => generated 9539 bytes in 1 msecs (HTTP/1.1 200) 3 headers in 110 bytes (1 switches on core 0)
[pid: 4073|app: 0|req: 79/611] 218.247.217.98 () {48 vars in 954 bytes} [Tue Dec  4 10:49:38 2018] POST /select/by_path_name/ => generated 733 bytes in 23 msecs (HTTP/1.1 200) 3 headers in 101 bytes (1 switches on core 0)
[pid: 4074|app: 0|req: 84/612] 218.247.217.98 () {42 vars in 831 bytes} [Tue Dec  4 10:49:40 2018] GET /demo/form?path_name=yf_C_research_report_rb_g => generated 9545 bytes in 1 msecs (HTTP/1.1 200) 3 headers in 110 bytes (1 switches on core 0)
[pid: 4072|app: 0|req: 80/613] 218.247.217.98 () {48 vars in 960 bytes} [Tue Dec  4 10:49:40 2018] POST /select/by_path_name/ => generated 738 bytes in 31 msecs (HTTP/1.1 200) 3 headers in 101 bytes (1 switches on core 0)
[pid: 4071|app: 0|req: 85/614] 218.247.217.98 () {42 vars in 724 bytes} [Tue Dec  4 10:55:02 2018] GET /index => generated 7174 bytes in 1 msecs (HTTP/1.1 200) 3 headers in 110 bytes (1 switches on core 0)
[pid: 4075|app: 0|req: 84/615] 218.247.217.98 () {42 vars in 764 bytes} [Tue Dec  4 10:55:02 2018] GET /demo/welcome.html => generated 24253 bytes in 1 msecs (HTTP/1.1 200) 3 headers in 111 bytes (1 switches on core 0)
[pid: 4073|app: 0|req: 80/616] 218.247.217.98 () {40 vars in 647 bytes} [Tue Dec  4 10:55:02 2018] GET /js/index.js => generated 7174 bytes in 1 msecs (HTTP/1.1 200) 3 headers in 110 bytes (1 switches on core 0)
Not Found: /frame/static/js/vip_nav.js
[pid: 4074|app: 0|req: 85/617] 218.247.217.98 () {40 vars in 665 bytes} [Tue Dec  4 10:55:02 2018] GET /frame/static/js/vip_nav.js => generated 4584 bytes in 4 msecs (HTTP/1.1 404) 3 headers in 102 bytes (1 switches on core 0)
Not Found: /demo/vip_tab.js
[pid: 4072|app: 0|req: 81/618] 218.247.217.98 () {40 vars in 655 bytes} [Tue Dec  4 10:55:02 2018] GET /demo/vip_tab.js => generated 4551 bytes in 4 msecs (HTTP/1.1 404) 3 headers in 102 bytes (1 switches on core 0)
[pid: 4071|app: 0|req: 86/619] 218.247.217.98 () {42 vars in 764 bytes} [Tue Dec  4 10:55:03 2018] GET /spider/basic.html => generated 12174 bytes in 1 msecs (HTTP/1.1 200) 3 headers in 111 bytes (1 switches on core 0)
[pid: 4075|app: 0|req: 85/620] 218.247.217.98 () {42 vars in 748 bytes} [Tue Dec  4 10:55:03 2018] GET /data/?page=1&limit=30 => generated 11502 bytes in 28 msecs (HTTP/1.1 200) 3 headers in 102 bytes (2 switches on core 0)
[pid: 4073|app: 0|req: 81/621] 218.247.217.98 () {42 vars in 724 bytes} [Tue Dec  4 10:55:12 2018] GET /index => generated 7174 bytes in 1 msecs (HTTP/1.1 200) 3 headers in 110 bytes (1 switches on core 0)
[pid: 4074|app: 0|req: 86/622] 218.247.217.98 () {42 vars in 764 bytes} [Tue Dec  4 10:55:12 2018] GET /demo/welcome.html => generated 24253 bytes in 1 msecs (HTTP/1.1 200) 3 headers in 111 bytes (1 switches on core 0)
[pid: 4072|app: 0|req: 82/623] 218.247.217.98 () {40 vars in 647 bytes} [Tue Dec  4 10:55:13 2018] GET /js/index.js => generated 7174 bytes in 1 msecs (HTTP/1.1 200) 3 headers in 110 bytes (1 switches on core 0)
Not Found: /frame/static/js/vip_nav.js
[pid: 4071|app: 0|req: 87/624] 218.247.217.98 () {40 vars in 665 bytes} [Tue Dec  4 10:55:13 2018] GET /frame/static/js/vip_nav.js => generated 4584 bytes in 4 msecs (HTTP/1.1 404) 3 headers in 102 bytes (1 switches on core 0)
Not Found: /demo/vip_tab.js
[pid: 4075|app: 0|req: 86/625] 218.247.217.98 () {40 vars in 655 bytes} [Tue Dec  4 10:55:13 2018] GET /demo/vip_tab.js => generated 4551 bytes in 4 msecs (HTTP/1.1 404) 3 headers in 102 bytes (1 switches on core 0)
[pid: 4073|app: 0|req: 82/626] 218.247.217.98 () {42 vars in 764 bytes} [Tue Dec  4 10:55:14 2018] GET /spider/basic.html => generated 12174 bytes in 1 msecs (HTTP/1.1 200) 3 headers in 111 bytes (1 switches on core 0)
[pid: 4074|app: 0|req: 87/627] 218.247.217.98 () {42 vars in 748 bytes} [Tue Dec  4 10:55:14 2018] GET /data/?page=1&limit=30 => generated 11502 bytes in 17 msecs (HTTP/1.1 200) 3 headers in 102 bytes (2 switches on core 0)
[pid: 4072|app: 0|req: 83/628] 218.247.217.98 () {42 vars in 797 bytes} [Tue Dec  4 10:55:18 2018] GET /demo/form?path_name=yf_demo2 => generated 9528 bytes in 1 msecs (HTTP/1.1 200) 3 headers in 110 bytes (1 switches on core 0)
[pid: 4071|app: 0|req: 88/629] 218.247.217.98 () {48 vars in 943 bytes} [Tue Dec  4 10:55:18 2018] POST /select/by_path_name/ => generated 740 bytes in 31 msecs (HTTP/1.1 200) 3 headers in 101 bytes (1 switches on core 0)
[pid: 4075|app: 0|req: 87/630] 218.247.217.98 () {42 vars in 729 bytes} [Tue Dec  4 10:59:09 2018] GET /index => generated 7174 bytes in 1 msecs (HTTP/1.1 200) 3 headers in 110 bytes (1 switches on core 0)
[pid: 4073|app: 0|req: 83/631] 218.247.217.98 () {42 vars in 769 bytes} [Tue Dec  4 10:59:09 2018] GET /demo/welcome.html => generated 24253 bytes in 1 msecs (HTTP/1.1 200) 3 headers in 111 bytes (1 switches on core 0)
[pid: 4074|app: 0|req: 88/632] 218.247.217.98 () {40 vars in 652 bytes} [Tue Dec  4 10:59:09 2018] GET /js/index.js => generated 7174 bytes in 1 msecs (HTTP/1.1 200) 3 headers in 110 bytes (1 switches on core 0)
Not Found: /frame/static/js/vip_nav.js
[pid: 4072|app: 0|req: 84/633] 218.247.217.98 () {40 vars in 670 bytes} [Tue Dec  4 10:59:09 2018] GET /frame/static/js/vip_nav.js => generated 4584 bytes in 4 msecs (HTTP/1.1 404) 3 headers in 102 bytes (1 switches on core 0)
[pid: 4071|app: -1|req: -1/634] 218.247.217.98 () {44 vars in 769 bytes} [Tue Dec  4 10:59:10 2018] GET /src/frame/static/image/code.png => generated 2108 bytes in 0 msecs via sendfile() (HTTP/1.1 200) 3 headers in 112 bytes (0 switches on core 0)
Not Found: /demo/vip_tab.js
[pid: 4075|app: 0|req: 88/635] 218.247.217.98 () {40 vars in 660 bytes} [Tue Dec  4 10:59:10 2018] GET /demo/vip_tab.js => generated 4551 bytes in 4 msecs (HTTP/1.1 404) 3 headers in 102 bytes (1 switches on core 0)
[pid: 4073|app: 0|req: 84/636] 218.247.217.98 () {42 vars in 769 bytes} [Tue Dec  4 10:59:11 2018] GET /spider/basic.html => generated 12174 bytes in 1 msecs (HTTP/1.1 200) 3 headers in 111 bytes (1 switches on core 0)
[pid: 4074|app: 0|req: 89/637] 218.247.217.98 () {42 vars in 753 bytes} [Tue Dec  4 10:59:11 2018] GET /data/?page=1&limit=30 => generated 11502 bytes in 24 msecs (HTTP/1.1 200) 3 headers in 102 bytes (2 switches on core 0)
[pid: 4072|app: 0|req: 85/638] 218.247.217.98 () {42 vars in 753 bytes} [Tue Dec  4 10:59:13 2018] GET /data/?page=3&limit=30 => generated 5460 bytes in 20 msecs (HTTP/1.1 200) 3 headers in 101 bytes (2 switches on core 0)
[pid: 4071|app: 0|req: 89/639] 218.247.217.98 () {42 vars in 724 bytes} [Tue Dec  4 11:00:09 2018] GET /index => generated 7174 bytes in 1 msecs (HTTP/1.1 200) 3 headers in 110 bytes (1 switches on core 0)
[pid: 4075|app: 0|req: 89/640] 218.247.217.98 () {42 vars in 764 bytes} [Tue Dec  4 11:00:09 2018] GET /demo/welcome.html => generated 24253 bytes in 1 msecs (HTTP/1.1 200) 3 headers in 111 bytes (1 switches on core 0)
[pid: 4073|app: 0|req: 85/641] 218.247.217.98 () {40 vars in 647 bytes} [Tue Dec  4 11:00:09 2018] GET /js/index.js => generated 7174 bytes in 1 msecs (HTTP/1.1 200) 3 headers in 110 bytes (1 switches on core 0)
Not Found: /frame/static/js/vip_nav.js
[pid: 4074|app: 0|req: 90/642] 218.247.217.98 () {40 vars in 665 bytes} [Tue Dec  4 11:00:09 2018] GET /frame/static/js/vip_nav.js => generated 4584 bytes in 4 msecs (HTTP/1.1 404) 3 headers in 102 bytes (1 switches on core 0)
Not Found: /demo/vip_tab.js
[pid: 4072|app: 0|req: 86/643] 218.247.217.98 () {40 vars in 655 bytes} [Tue Dec  4 11:00:09 2018] GET /demo/vip_tab.js => generated 4551 bytes in 4 msecs (HTTP/1.1 404) 3 headers in 102 bytes (1 switches on core 0)
[pid: 4071|app: 0|req: 90/644] 218.247.217.98 () {42 vars in 764 bytes} [Tue Dec  4 11:00:10 2018] GET /spider/basic.html => generated 12174 bytes in 1 msecs (HTTP/1.1 200) 3 headers in 111 bytes (1 switches on core 0)
[pid: 4075|app: 0|req: 90/645] 218.247.217.98 () {42 vars in 748 bytes} [Tue Dec  4 11:00:10 2018] GET /data/?page=1&limit=30 => generated 11502 bytes in 29 msecs (HTTP/1.1 200) 3 headers in 102 bytes (2 switches on core 0)
[pid: 4073|app: 0|req: 86/646] 218.247.217.98 () {42 vars in 724 bytes} [Tue Dec  4 11:01:15 2018] GET /index => generated 7174 bytes in 1 msecs (HTTP/1.1 200) 3 headers in 110 bytes (1 switches on core 0)
[pid: 4074|app: 0|req: 91/647] 218.247.217.98 () {42 vars in 764 bytes} [Tue Dec  4 11:01:16 2018] GET /demo/welcome.html => generated 24253 bytes in 1 msecs (HTTP/1.1 200) 3 headers in 111 bytes (1 switches on core 0)
[pid: 4072|app: 0|req: 87/648] 218.247.217.98 () {40 vars in 647 bytes} [Tue Dec  4 11:01:16 2018] GET /js/index.js => generated 7174 bytes in 1 msecs (HTTP/1.1 200) 3 headers in 110 bytes (1 switches on core 0)
Not Found: /frame/static/js/vip_nav.js
[pid: 4071|app: 0|req: 91/649] 218.247.217.98 () {40 vars in 665 bytes} [Tue Dec  4 11:01:16 2018] GET /frame/static/js/vip_nav.js => generated 4584 bytes in 4 msecs (HTTP/1.1 404) 3 headers in 102 bytes (1 switches on core 0)
Not Found: /demo/vip_tab.js
[pid: 4075|app: 0|req: 91/650] 218.247.217.98 () {40 vars in 655 bytes} [Tue Dec  4 11:01:16 2018] GET /demo/vip_tab.js => generated 4551 bytes in 4 msecs (HTTP/1.1 404) 3 headers in 102 bytes (1 switches on core 0)
[pid: 4073|app: 0|req: 87/651] 218.247.217.98 () {42 vars in 764 bytes} [Tue Dec  4 11:01:17 2018] GET /spider/basic.html => generated 12174 bytes in 1 msecs (HTTP/1.1 200) 3 headers in 111 bytes (1 switches on core 0)
[pid: 4074|app: 0|req: 92/652] 218.247.217.98 () {42 vars in 748 bytes} [Tue Dec  4 11:01:17 2018] GET /data/?page=1&limit=30 => generated 11502 bytes in 24 msecs (HTTP/1.1 200) 3 headers in 102 bytes (2 switches on core 0)
