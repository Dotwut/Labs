```bash
whatweb --color=never --no-errors -a 3 -v http://192.168.217.194:80 2>&1
```

[/home/dotwut/Labs/dc-2/results/192.168.217.194/scans/tcp80/tcp_80_http_whatweb.txt](file:///home/dotwut/Labs/dc-2/results/192.168.217.194/scans/tcp80/tcp_80_http_whatweb.txt):

```
WhatWeb report for http://192.168.217.194:80
Status    : 301 Moved Permanently
Title     : <None>
IP        : 192.168.217.194
Country   : RESERVED, ZZ

Summary   : Apache[2.4.10], HTTPServer[Debian Linux][Apache/2.4.10 (Debian)], RedirectLocation[http://dc-2/]

Detected Plugins:
[ Apache ]
	The Apache HTTP Server Project is an effort to develop and
	maintain an open-source HTTP server for modern operating
	systems including UNIX and Windows NT. The goal of this
	project is to provide a secure, efficient and extensible
	server that provides HTTP services in sync with the current
	HTTP standards.

	Version      : 2.4.10 (from HTTP Server Header)
	Google Dorks: (3)
	Website     : http://httpd.apache.org/

[ HTTPServer ]
	HTTP server header string. This plugin also attempts to
	identify the operating system from the server header.

	OS           : Debian Linux
	String       : Apache/2.4.10 (Debian) (from server string)

[ RedirectLocation ]
	HTTP Server string location. used with http-status 301 and
	302

	String       : http://dc-2/ (from location)

HTTP Headers:
	HTTP/1.1 301 Moved Permanently
	Date: Tue, 02 May 2023 23:55:06 GMT
	Server: Apache/2.4.10 (Debian)
	Location: http://dc-2/
	Content-Length: 0
	Connection: close
	Content-Type: text/html; charset=UTF-8



```
