```
[*] Service scan wkhtmltoimage (tcp/80/http/wkhtmltoimage) ran a command which returned a non-zero exit code (1).
[-] Command: wkhtmltoimage --format png http://192.168.217.194:80/ /home/dotwut/Labs/dc-2/results/192.168.217.194/scans/tcp80/tcp_80_http_screenshot.png
[-] Error Output:
Loading page (1/2)
[>                                                           ] 0%
Error: Failed to load http://dc-2/, with network status code 3 and http status code 0 - Host dc-2 not found
[============================================================] 100%
Error: Failed loading page http://192.168.217.194:80/ (sometimes it will work just to ignore this error with --load-error-handling ignore)
Exit with code 1 due to network error: HostNotFoundError



```