```bash
nikto -ask=no -Tuning=x4567890ac -nointeractive -host http://192.168.217.194:80 2>&1 | tee "/home/dotwut/Labs/dc-2/results/192.168.217.194/scans/tcp80/tcp_80_http_nikto.txt"
```

[/home/dotwut/Labs/dc-2/results/192.168.217.194/scans/tcp80/tcp_80_http_nikto.txt](file:///home/dotwut/Labs/dc-2/results/192.168.217.194/scans/tcp80/tcp_80_http_nikto.txt):

```
- Nikto v2.5.0
---------------------------------------------------------------------------
+ Target IP:          192.168.217.194
+ Target Hostname:    192.168.217.194
+ Target Port:        80
+ Start Time:         2023-05-02 17:55:05 (GMT-6)
---------------------------------------------------------------------------
+ Server: Apache/2.4.10 (Debian)
+ /: The anti-clickjacking X-Frame-Options header is not present. See: https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/X-Frame-Options
+ /: The X-Content-Type-Options header is not set. This could allow the user agent to render the content of the site in a different fashion to the MIME type. See: https://www.netsparker.com/web-vulnerability-scanner/vulnerabilities/missing-content-type-header/
+ Root page / redirects to: http://dc-2/
+ /index.php?: Drupal Link header found with value: ARRAY(0x557b952bd9e8). See: https://www.drupal.org/
+ No CGI Directories found (use '-C all' to force check all possible dirs)
+ Apache/2.4.10 appears to be outdated (current is at least Apache/2.4.54). Apache 2.2.34 is the EOL for the 2.x branch.
+ /: Web Server returns a valid response with junk HTTP methods which may cause false positives.
+ /icons/README: Apache default file found. See: https://www.vntweb.co.uk/apache-restricting-access-to-iconsreadme/
+ /wp-content/plugins/akismet/readme.txt: The WordPress Akismet plugin 'Tested up to' version usually matches the WordPress version.
+ /wp-links-opml.php: This WordPress script reveals the installed version.
+ /license.txt: License file found may identify site software.
+ /wp-login.php?action=register: Cookie wordpress_test_cookie created without the httponly flag. See: https://developer.mozilla.org/en-US/docs/Web/HTTP/Cookies
+ /wp-login.php: Wordpress login found.
+ 7729 requests: 0 error(s) and 11 item(s) reported on remote host
+ End Time:           2023-05-02 18:05:34 (GMT-6) (629 seconds)
---------------------------------------------------------------------------
+ 1 host(s) tested

```
