```bash
nmap -vv --reason -Pn -T4 -sV -p 80 --script="banner,(http* or ssl*) and not (brute or broadcast or dos or external or http-slowloris* or fuzzer)" -oN "/home/dotwut/Labs/dc-2/results/192.168.217.194/scans/tcp80/tcp_80_http_nmap.txt" -oX "/home/dotwut/Labs/dc-2/results/192.168.217.194/scans/tcp80/xml/tcp_80_http_nmap.xml" 192.168.217.194
```

[/home/dotwut/Labs/dc-2/results/192.168.217.194/scans/tcp80/tcp_80_http_nmap.txt](file:///home/dotwut/Labs/dc-2/results/192.168.217.194/scans/tcp80/tcp_80_http_nmap.txt):

```
# Nmap 7.93 scan initiated Tue May  2 17:55:04 2023 as: nmap -vv --reason -Pn -T4 -sV -p 80 "--script=banner,(http* or ssl*) and not (brute or broadcast or dos or external or http-slowloris* or fuzzer)" -oN /home/dotwut/Labs/dc-2/results/192.168.217.194/scans/tcp80/tcp_80_http_nmap.txt -oX /home/dotwut/Labs/dc-2/results/192.168.217.194/scans/tcp80/xml/tcp_80_http_nmap.xml 192.168.217.194
Nmap scan report for 192.168.217.194
Host is up, received user-set (0.069s latency).
Scanned at 2023-05-02 17:55:05 MDT for 241s

Bug in http-security-headers: no string output.
PORT   STATE SERVICE REASON  VERSION
80/tcp open  http    syn-ack Apache httpd 2.4.10 ((Debian))
|_http-title: Did not follow redirect to http://dc-2/
|_http-feed: Couldn't find any feeds.
| http-sitemap-generator: 
|   Directory structure:
|   Longest directory structure:
|     Depth: 0
|     Dir: /
|   Total files found (by extension):
|_    
|_http-date: Tue, 02 May 2023 23:55:27 GMT; 0s from local time.
|_http-drupal-enum: Nothing found amongst the top 100 resources,use --script-args number=<number|all> for deeper analysis)
|_http-server-header: Apache/2.4.10 (Debian)
|_http-comments-displayer: Couldn't find any comments.
| http-useragent-tester: 
|   Status for browser useragent: false
|   Redirected To: http://dc-2/
|   Allowed User Agents: 
|     Mozilla/5.0 (compatible; Nmap Scripting Engine; https://nmap.org/book/nse.html)
|     libwww
|     lwp-trivial
|     libcurl-agent/1.0
|     PHP/
|     Python-urllib/2.5
|     GT::WWW
|   Change in Status Code: 
|     Wget/1.13.4 (linux-gnu): 200
|     HTTP::Lite: 200
|     Snoopy: 200
|     PHPCrawl: 200
|     WWW-Mechanize/1.34: 200
|     http client: 200
|     Zend_Http_Client: 200
|     MFC_Tear_Sample: 200
|     PECL::HTTP: 200
|_    URI::Fetch: 200
| http-methods: 
|_  Supported Methods: GET HEAD POST OPTIONS
|_http-devframework: Couldn't determine the underlying framework or CMS. Try increasing 'httpspider.maxpagecount' value to spider more pages.
|_http-litespeed-sourcecode-download: Request with null byte did not work. This web server might not be vulnerable
|_http-config-backup: ERROR: Script execution failed (use -d to debug)
|_http-csrf: Couldn't find any CSRF vulnerabilities.
| http-waf-detect: IDS/IPS/WAF detected:
|_192.168.217.194:80/?p4yl04d3=<script>alert(document.cookie)</script>
|_http-jsonp-detection: Couldn't find any JSONP endpoints.
| http-wordpress-users: 
| Username found: admin
| Username found: tom
| Username found: jerry
|_Search stopped at ID #25. Increase the upper limit if necessary with 'http-wordpress-users.limit'
|_http-mobileversion-checker: No mobile version detected.
|_http-referer-checker: Couldn't find any cross-domain scripts.
| http-wordpress-enum: 
| Search limited to top 100 themes/plugins
|   themes
|     twentyfifteen 1.7
|     twentysixteen 1.3
|   plugins
|_    akismet 3.3.2
|_http-malware-host: Host appears to be clean
|_http-chrono: Request times for /; avg: 20029.71ms; min: 20024.74ms; max: 20031.69ms
| http-enum: 
|   /wp-login.php: Possible admin folder
|   /readme.html: Wordpress version: 2 
|   /wp-includes/images/rss.png: Wordpress version 2.2 found.
|   /wp-includes/js/jquery/suggest.js: Wordpress version 2.5 found.
|   /wp-includes/images/blank.gif: Wordpress version 2.6 found.
|   /wp-includes/js/comment-reply.js: Wordpress version 2.7 found.
|   /wp-login.php: Wordpress login page.
|   /wp-admin/upgrade.php: Wordpress login page.
|_  /readme.html: Interesting, a readme.
| http-headers: 
|   Date: Tue, 02 May 2023 23:55:34 GMT
|   Server: Apache/2.4.10 (Debian)
|   Location: http://dc-2/
|   Content-Length: 0
|   Connection: close
|   Content-Type: text/html; charset=UTF-8
|   
|_  (Request type: GET)
|_http-stored-xss: Couldn't find any stored XSS vulnerabilities.
|_http-errors: Couldn't find any error pages.
|_http-fetch: Please enter the complete path of the directory to save data in.
| http-vhosts: 
| 124 names had status 301
| crs
| mail2
| ftp0
|_internal
|_http-dombased-xss: Couldn't find any DOM based XSS.
| http-php-version: Logo query returned unknown hash a844ab26acfa9c805e60158ff7db3818
|_Credits query returned unknown hash a844ab26acfa9c805e60158ff7db3818

Read data files from: /usr/bin/../share/nmap
Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
# Nmap done at Tue May  2 17:59:06 2023 -- 1 IP address (1 host up) scanned in 241.98 seconds

```
