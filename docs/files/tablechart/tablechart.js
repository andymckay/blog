/*
	Table Graph
	by Andy McKay, http://www.clearwind.ca
	based on http://www.wait-till-i.com/2008/01/08/generating-charts-from-accessible-data-tables-using-the-google-charts-api/


	Licensed under the Creative Commons Attribution 2.5 License - http://creativecommons.org/licenses/by/2.5/
*/
function insertAfter(parent, node, referenceNode) {
  parent.insertBefore(node, referenceNode.nextSibling);
}
function tablechart() {
  /* variables */
  var triggerClass = 'tograph';
  var chartClass = 'tablechart';
  var chartColour = '0000ff';
  var chartSize = '750x250';
  var labelTriggerClass = 'labelchartcolumn';
  var valueTriggerClass = 'valuechartcolumn';  
  var toTableClass = 'totable';
  var tableClass = 'generatedfromchart';
  var chartType = 'p3'
  /* end variables */

  var tables = document.getElementsByTagName('table');
  for (var i = 0; tables[i]; i++){
    var t = tables[i];
    var c = t.className;
    if(c.indexOf(triggerClass) !== -1){
      var charturl = 'http://chart.apis.google.com/chart?cht=' + 
        chartType + '&chco=' + chartColour + '&chs=' + chartSize + 
        '&chd=t:';
        
      /* So loop through all the head elements, finding the ones labelled 
         valuechartcolumn and labelchartcolumn, so that we can find the 
         corresponding table cells
         */
      var ths = t.getElementsByTagName('thead')[0].getElementsByTagName('th');
      var labelTriggerClassMap = 0;
      var valueTriggerClassMap = 0;  
      for (var j = 0; j < ths.length; j++) {
          var c = ths[j].className;
          if(c.indexOf(labelTriggerClass) !== -1) {
              labelTriggerClassMap = j;
          } 
          if(c.indexOf(valueTriggerClass) !== -1) {
              valueTriggerClassMap = j;
          }
      }
      /* now we know say what col 4 and col 5 are, so loop through and find them 
         note here we are summing together the values so if foo=1 and foo=2, foo will = 3 in
         the result
      */
      var trs = t.getElementsByTagName('tbody')[0].getElementsByTagName('tr');
      var temp = []
      for (var j=0; j < trs.length; j++) {
          var tds = trs[j].getElementsByTagName('td');
          var lbl = tds[labelTriggerClassMap].innerHTML;
          var val = tds[valueTriggerClassMap].innerHTML;      
          if (!temp[lbl]) {
              temp[lbl] = parseFloat(val);
          } else {
              temp[lbl] = temp[lbl] + parseFloat(val);
          }
      }
      /* build up urls, should avoid doing another loop here */
      var chart = document.createElement('a');
      var data = [];
      var labels = [];
      for (var x in temp) {
          data.push(temp[x]);
          labels.push(x);
      }
      /* finally write out link */
      chart.innerHTML = "Show as chart"
      chart.setAttribute('href',charturl+data.join(',') + '&chl=' + labels.join('|'));
      chart.setAttribute('rel', 'lightbox');
      chart.className = chartClass;
      insertAfter(t.parentNode,chart,t);
    };
  };
};

