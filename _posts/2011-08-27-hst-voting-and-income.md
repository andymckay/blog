---
layout: post
title: HST voting and income
categories: Canada
old: 2315
blog: andy-mckay
---
<p>Yesterday the vote came in and British Columbia voted to get rid of the HST. Which means we now owe the Federal Government <a href="http://www.vancouversun.com/business/Ottawa+says+respects+decision+wants+money+back/5313789/story.html">$1.6 billion or more</a>. The Sun showed the data on who voted on what, but I thought there was a correlation between income and who voted for what.</p>
<p>Perhaps there is:</p>
<script type="text/javascript" src="//ajax.googleapis.com/ajax/static/modules/gviz/1.0/chart.js"> {"dataSourceUrl":"//docs.google.com/spreadsheet/tq?key=0ApbiPdOYdv9IdDVhdHpRWkp5T21DZEFQY1AyUUVQamc&transpose=0&headers=-1&merge=COLS&range=C1%3AC86%2CI1%3AI86&gid=0&pub=1","options":{"series":{"1":{"color":"#cc0000"},"0":{"color":"#0000ff"}},"reverseCategories":false,"backgroundColor":"#FFFFFF","pointSize":0,"width":839,"vAxis":{},"logScale":false,"hasLabelsColumn":false,"hAxis":{"maxAlternation":1},"vAxes":[{"min":null,"title":null,"max":null}],"title":"","height":484,"legend":"right","reverseAxis":false,"isStacked":false},"state":{},"chartType":"AreaChart","chartName":"Chart 1"} </script>
<cite>Sources: <a href="http://www.vancouversun.com/news/Electoral+district+breakdown+voting/5313477/story.html">Vancouver Sun for HST data</a>, <a href="http://www.bcstats.gov.bc.ca/data/cen06/profiles/peds/ped_06.asp">StatsCan for income data</a> into a <a href="https://docs.google.com/spreadsheet/ccc?key=0ApbiPdOYdv9IdDVhdHpRWkp5T21DZEFQY1AyUUVQamc#gid=0">spreadsheet</a></cite>
<p>The red line represents average income per riding (from the poorest Vancouver-Mount Pleasant at 22% income to Vancouver-Quilchena at 100%). The blue line represents the % of yes votes, those that wanted to get rid of the HST.</p>
<p>As income rises, the number of people voting to get rid of the HST falls.</p>
<blockquote>Poorer ridings like North Coast were more likely to vote to scrap the tax while richer ridings, like Surrey-Cloverdale, were more likely to want to keep it.</blockquote>
<cite><a href="http://www.vancouversun.com/news/Interactive+graphic+vote+numbers/5313879/story.html">Vancouver Sun</a></cite>
<p>In my opinion, all the arguments about how the HST is superior tax from economists and the Fraser Institute and so on didn't matter. The HST hurt people every day when they paid for things and that's what mattered. The lower your income, the more that mattered.</p>
<p><b>Note:</b> my source data is all in the <a href="https://docs.google.com/spreadsheet/ccc?key=0ApbiPdOYdv9IdDVhdHpRWkp5T21DZEFQY1AyUUVQamc#gid=2">Google spreadsheet</a>. To get the average income data per riding I wrote a Python script, parsed the BC web page, downloaded all the 85 odd PDFs, converted them into text and then parsed that. Sigh.</p>
