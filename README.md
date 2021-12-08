# Apache-Status Monitor
Python Script for scraping Apache Server Status page if present , find directories , connected IPs and their geolocation .etc
## Apache-Server-Status
The Apache Server-Status module provides an instrumentation tool set to determine how well the Apache server instance is performing.
Apache web server exposes metrics through its status module, mod_status. If your server is running and mod_status is enabled, your server’s status page should be available at http://{host}/server-status. If that link does not work, it means you need to enable mod_status in your configuration file.

- The number of children serving requests.
- The number of idle children.
- The status of each child, the number of requests that child has performed, and the total number of bytes served by the child.
- The total number of accesses and byte count served.
- The time the server was started or restarted and the amount of time the server has been running.
- An average of the number of requests per second, the number of bytes served per second, and the average number of bytes per request.
- The current percentage of the CPU used by each child and in total by Apache.
- The current hosts and requests being processed.

## IP Geolocation API

Apache Status Monitor Script uses Free ip-api.com IP Geoplocation API 
https://ip-api.com/


### Useful Links

https://httpd.apache.org/docs/2.4/mod/mod_status.html
https://help.blackboard.com/Learn/Administrator/Hosting/Performance_Optimization/Optimization_Apache/Server-Status_Module_Apache
https://www.datadoghq.com/blog/collect-apache-performance-metrics/
https://ip-api.com/docs
