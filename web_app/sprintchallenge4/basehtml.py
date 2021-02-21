<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>AirQuality</title>
</head>
<body>

<h1 style="color: maroon">AirQuality</h1>
<p>AirQuality in Los Angeles over time</p>
<a href="https://api.openaq.org/v1/measurements?city=Los%20Angeles&parameter=pm25">Source</a>
<hr>
<b><a href="/cities">More Cities</a></b>

<ul>
{% for datum in data %}
    <li>Date {{ datum.datetime }}  - Value {{datum.value}}</li>
{% endfor %}
</ul>

</ul>
</body>
