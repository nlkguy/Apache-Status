# Apache-Status Monitor
Python Script for scraping Apache Server Status page if present , find directories , connected IPs and their geolocation .etc
## Apache-Server-Status

The Apache Server-Status module provides an instrumentation tool set to determine how well the Apache server instance is performing.
Apache web server exposes metrics through its status module, mod_status. If your server is running and mod_status is enabled, your server’s status page should be available at http://{host}/server-status. If that link does not work, it means you need to enable mod_status in your configuration file.
<p align="center">
<img width="1608" height="188" src="https://github.com/nlkguy/Apache-Status/blob/main/images/apache_stat_01.png">
</p>

```
Srv	- Child Server number - generation
PID -	OS process ID
Acc - Number of accesses this connection / this child / this slot
M - Mode of operation
CPU	- CPU usage, number of seconds
SS - Seconds since beginning of most recent request
Req - Milliseconds required to process most recent request
Dur - Sum of milliseconds required to process all requests
Conn - Kilobytes transferred this connection
Child	- Megabytes transferred this child
Slot - Total megabytes transferred this slot

```

- The number of children serving requests.
- The number of idle children.
- The status of each child, the number of requests that child has performed, and the total number of bytes served by the child.
- The total number of accesses and byte count served.
- The time the server was started or restarted and the amount of time the server has been running.
- An average of the number of requests per second, the number of bytes served per second, and the average number of bytes per request.
- The current percentage of the CPU used by each child and in total by Apache.
- The current hosts and requests being processed.

## IP Geolocation API

Apache Status Monitor Script uses Free [ip-api.com IP Geoplocation API](https://ip-api.com/).
Each client IP scraped from the server-status page are recorded in a local file.
Free API endpoints are limited to 45 HTTP requests per minute from an IP address.
If you go over this limit requests are throttled (HTTP 429) until your limit window is reset.
you can always get the [paid - pro version](https://members.ip-api.com/) to support them.

```
{
  "status": "success",
  "country": "United States",
  "countryCode": "US",
  "region": "VA",
  "regionName": "Virginia",
  "city": "Ashburn",
  "zip": "20149","lat": 39.03,
  "lon": -77.5",
  "timezone": "America/New_York",
  "isp": "Google LLC",
  "org": "Google Public DNS",
  "as": "AS15169 Google LLC","query": "8.8.8.8"
}

```
you can customize returned fields by passing GET parameter.you can add or avoid certain fields.
```
http://ip-api.com/json/{query}?fields=status,message,continent,continentCode,country,countryCode,region,regionName,city,district,zip,lat,lon,timezone,offset,currency,isp,org,as,asname,reverse,mobile,proxy,hosting,query
```
will give maximum number of fields.


### Useful Links

- [Apache Official Documentation](https://httpd.apache.org/docs/2.4/mod/mod_status.html)
- [Blackboard.com - Apache Server Status Module](https://help.blackboard.com/Learn/Administrator/Hosting/Performance_Optimization/Optimization_Apache/Server-Status_Module_Apache)
- [DataDogHQ.com - Apache Performance Metrics](https://www.datadoghq.com/blog/collect-apache-performance-metrics/)
- [IP-API Documentation](https://ip-api.com/docs)
- [Peko-Step.com - Online Image Editor](https://www.peko-step.com/)
