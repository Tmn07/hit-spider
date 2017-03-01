<?php
ini_set('memory_limit', '-1');
    $dbhost = "localhost";
    $dbuser = "root";
    $dbpassword = "root";
    $dbdatabase = "jwts";
    $db = mysql_connect($dbhost,$dbuser,$dbpassword);

    mysql_select_db($dbdatabase,$db);
    $sql = "SELECT score,count(*) as f FROM `gay` where `status` = 0 group by `score` order by score asc";
    $res = mysql_query($sql);
    while ($row = mysql_fetch_assoc($res)) {
        $arr[] = $row;
    }
    $js = json_encode($arr);

    $arr = array();
    $sql = "SELECT AVG(score) as a,AVG(item1) as a1  ,AVG(item2) as a2 ,AVG(item3) as a3   FROM `gay` where status = 0 and rwh != '021'";
    $res = mysql_query($sql);
    while ($row = mysql_fetch_assoc($res)) {
        $arr[] = $row;
    }
    $a1 = $arr[0]['a'];
    $a2 = $arr[0]['a1'];
    $a3 = $arr[0]['a2'];
    $a4 = $arr[0]['a3'];

    $arr = array();
    $sql = "SELECT COUNT( * ) as t FROM  `gay`";
    $res = mysql_query($sql);
    while ($row = mysql_fetch_assoc($res)) {
        $arr[] = $row;
    }
    $len = $arr[0]['t'];


    $arr = array();
    $sql = "SELECT count(*) as t FROM `gay` WHERE `score` < 60";
    $res = mysql_query($sql);
    while ($row = mysql_fetch_assoc($res)) {
        $arr[] = $row;
    }
    $gua = $arr[0]['t'];
    $gg = $gua/$len;

    
    $arr = array();
    $sql = "SELECT status, count(*) as t FROM `gay` where status != 0 group by status order by status asc";
    $res = mysql_query($sql);
    while ($row = mysql_fetch_assoc($res)) {
        $arr[] = $row;
    }   
    $sdata1 = $arr[0]['t']; 
    $sdata2 = $arr[1]['t']; 

    $arr = array();
    $sql = "SELECT item1, COUNT( * ) AS f
        FROM  `gay` 
        WHERE  `status` =0 and `rwh` != '021'
        GROUP BY  `item1` 
        ORDER BY score ASC ";
    $res = mysql_query($sql);
    while ($row = mysql_fetch_assoc($res)) {
        $arr[] = array($row['item1'],intval($row['f']));
    }
    $item1 = json_encode($arr);

    $arr = array();
    $sql = "SELECT item2, COUNT( * ) AS f
        FROM  `gay` 
        WHERE  `status` =0 and `rwh` != '021'
        GROUP BY  `item2` 
        ORDER BY score ASC ";
    $res = mysql_query($sql);
    while ($row = mysql_fetch_assoc($res)) {
        $arr[] = array($row['item2'],intval($row['f']));
    }
    $item2 = json_encode($arr);

?>

<!DOCTYPE html>
<html>
<head>
	<title>概率论部分成绩分析</title>
	<meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=0">
</head>
<script src="//cdn.bootcss.com/jquery/3.1.1/jquery.min.js"></script>
<script src="http://cdn.hcharts.cn/highcharts/highcharts.js"></script>

<body>
<div id="container1" style="min-width:400px;height:400px"></div>
<div id="container2" style="min-width:400px;height:400px;"></div>
<div id="container3" style="width:400px;height:400px;display:inline-block;"></div>
<div id="container4" style="width:400px;height:400px;display:inline-block;"></div>
<div style="width:300px;height:400px;display:inline-block;">
    <p>其他（取自目前<?php echo $len;?>份数据）</p>
    <p>总平均分：<?php echo round($a1,2);?></p>
    <p>作业平均分：<?php echo round($a2,2);?></p>
    <p>论文平均分：<?php echo round($a3,2);?></p>
    <p>期末考平均分：<?php echo round($a4,2);?></p>
    <p>挂科率：<?php echo round($gg,4)*100;echo "%";?></p>
    <p>旷考人数：<?php echo $sdata2;?></p>
    <p>缓考人数：<?php echo $sdata1;?></p>
</div>
</body>


<script type="text/javascript">
var data = <?php echo $js;?>;
var data_item1 = <?php echo $item1;?>;
var data_item2 = <?php echo $item2;?>;
var len = <?php echo $len;?>;


var ddata = new Array();
var j = 0;

for (var i = 0;i<= 100; i+=0.5) {
	if (data[j]['score'] == i) {
		ddata.push( parseInt(data[j]['f']));
		j++;
	}
	else{
		ddata.push(null);
	}
}
var pdata = new Array();
var n=0;
var f=0;
j = 0;
for (var i = 0;i<= 100; i+=0.5) {
    if (data[j]['score'] == i) {
        f += parseInt(data[j]['f']);
        j ++;
    }
    else{
        f += 0;
    }

    if (i>=10*n && i<10*(n+1)){
        continue;
    }
    else{
        pdata.push(f);
        f = 0;
        n += 1;
    }

}


$(function () {

    $('#container1').highcharts({
        chart: {
            type: 'area'
        },
        title: {
            text: '2016年概率论成绩分布'
        },
        subtitle: {
            text: 'Source: <a href="http://github.com/qq519043202">' +
            'Tmn07</a> 数据取自真实的'+len+'份成绩'
        },
        xAxis: {

            labels: {
                formatter: function () {
                    return this.value/2; // clean, unformatted number for year
                }
            }
        },
        yAxis: {
            title: {
                text: '人数'
            },
            labels: {
                formatter: function () {
                    return this.value ;
                }
            }
        },
        tooltip: {
            formatter: function(){
            	return "分数："+this.x/2.0+"<br>"+"人数："+this.y;
            }
        },
        plotOptions: {
            area: {
                pointStart: 0,
                marker: {
                    enabled: false,
                    symbol: 'circle',
                    radius: 2,
                    states: {
                        hover: {
                            enabled: true
                        }
                    }
                }
            }
        },
        series: [{
            name: '概率论',
            data: ddata
        }]
    });
});
</script>
<script type="text/javascript">
$(function () {
    $('#container2').highcharts({
        chart: {
            plotBackgroundColor: null,
            plotBorderWidth: null,
            plotShadow: false
        },
        title: {
            text: '各分数段占比'
        },
        tooltip: {
            pointFormat: '{series.name}: <b>{point.percentage:.1f}%</b>'
        },
        plotOptions: {
            pie: {
                allowPointSelect: true,
                cursor: 'pointer',
                dataLabels: {
                    enabled: true,
                    format: '<b>{point.name}</b>: {point.percentage:.1f} %',
                    style: {
                        color: (Highcharts.theme && Highcharts.theme.contrastTextColor) || 'black'
                    }
                }
            }
        },
        series: [{
            type: 'pie',
            name: '占比',
            data: [
                ['0-10',   pdata[0]],
                ['10-20',       pdata[1]],
                ['20-30',       pdata[2]],
                ['30-40',       pdata[3]],
                ['40-50',       pdata[4]],
                ['50-60',       pdata[5]],
                ['60-70',       pdata[6]],
                ['70-80',       pdata[7]],
                ['80-90',       pdata[8]],
                ['90-100',       pdata[9]]
            ]
        }]
    });
});
$(function () {
    $('#container3').highcharts({
        chart: {
            plotBackgroundColor: null,
            plotBorderWidth: null,
            plotShadow: false
        },
        title: {
            text: '作业得分占比'
        },
        tooltip: {
            pointFormat: '{series.name}: <b>{point.percentage:.1f}%</b>'
        },
        plotOptions: {
            pie: {
                allowPointSelect: true,
                cursor: 'pointer',
                dataLabels: {
                    enabled: true,
                    format: '<b>{point.name}分</b>: {point.percentage:.1f} %',
                    style: {
                        color: (Highcharts.theme && Highcharts.theme.contrastTextColor) || 'black'
                    }
                }
            }
        },
        series: [{
            type: 'pie',
            name: '占比',
            data: data_item1,
        }]
    });
});
$(function () {
    $('#container4').highcharts({
        chart: {
            plotBackgroundColor: null,
            plotBorderWidth: null,
            plotShadow: false
        },
        title: {
            text: '论文得分占比'
        },
        tooltip: {
            pointFormat: '{series.name}: <b>{point.percentage:.1f}%</b>'
        },
        plotOptions: {
            pie: {
                allowPointSelect: true,
                cursor: 'pointer',
                dataLabels: {
                    enabled: true,
                    format: '<b>{point.name}分</b>: {point.percentage:.1f} %',
                    style: {
                        color: (Highcharts.theme && Highcharts.theme.contrastTextColor) || 'black'
                    }
                }
            }
        },
        series: [{
            type: 'pie',
            name: '占比',
            data: data_item2,
        }]
    });
});
</script>
</html>