import re

line = """






<!DOCTYPE html>
<html>
<head>
<meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
<title>行政处罚公示</title>
<link type="text/css" rel="stylesheet" href="/xxgs/ui/css/global.css"/>
<script type="text/javascript" src="/xxgs/ui/lib/jquery/jquery-1.8.3.min.js"></script>
<link type="text/css" rel="stylesheet" href="/xxgs/ui/widgets/hanweb/calendar/css/calendar.css"/>
<script type="text/javascript" src="/xxgs/ui/widgets/My97DatePicker/WdatePicker.js"></script>

<link href="/xxgs/resources/front/images/jnszf_sgs.css" rel="stylesheet" type="text/css"/>

<script type="text/javascript" src="/xxgs/resources/front/js/jpage/jquery.js"></script>

<script type="text/javascript" src="/xxgs/resources/front/js/jpage/jquery.jpage.js"></script>

<link href="/xxgs/resources/front/js/jpage/theme/default/css/jpage.css" rel="stylesheet" type="text/css"/>

</head>
<script type="text/javascript">  
	$(document).ready(
			function(){
				//demo2带初始数据
				var param = {
						/* jg:'',
						xdr:'',
						//sxq:'',
						bm:'' */
						encode_text:'lr0l3c8HD0HcYz9l19dVTPaC20ScVJtM+9NAyax1QDQ='
				};
				var InAllCount1 = '4204'; //总记录数
				if(InAllCount1 == '0'){
					alert("暂无双公示信息！");
				}
				/*dataBefore,dataAfter调用HTML样式、totalRecord当前数据的总记录数、perPage每页显示的条数、groupSize分组 showMode:normal列表页面工具栏显示的方式*/
				$('#ListBox').jpage(
					{
						openCookies:false,
						dataBefore:'<table width=\"100%\" border=\"0\" cellspacing=\"0\" cellpadding=\"0\"><tr class=\"ListTitle\"><td width=\"27%\" height=\"49\" align=\"center\">行政相对人名称</td><td width=\"26%\" align=\"center\">处罚机关</td><td width=\"36%\" align=\"center\">案件名称</td><td width=\"11%\" align=\"center\">处罚生效期</td></tr>',
						dataAfter:'</table>',
						totalRecord:InAllCount1,
						groupSize:5,
						perPage:10,
						allowChangePerPage:false,
						proxyUrl:'./xzcfmore_show.do',
						barPosition:'bottom',
						showMode:'full',
						ajaxParam:param
					}
				);
			} 
		) 
		
		function resetForm(){
		
		$("#xdr").val('');
	}
</script>
<body>
<div id="Container">
	<div id="Nav">
		<!--<div class="menu_xkB font_nav"><a href="/xxgs/front/xxgs/xk/xzxk_show.do?bm=">行政许可</a></div>
		<div class="menu_cfA font_nav"><a href="/xxgs/front/xxgs/cf/xzcf_show.do?bm=">行政处罚</a></div>
        <div class="menu_gsmlA font_nav"><a href="http://service.jinan.gov.cn/col/col9323/index.html" target="_blank">“双公示”目录</a></div>-->
		
	</div>
	<div id="PageBody">
		<div id="SearchBox">
			<div class="title">条件查询：</div>
			<table width="87%" border="0" cellspacing="0" cellpadding="0">
				<tr>
	    			<td height="40">
	    				<form id="form1" name="form1" method="post" action="xzcf_show.do?bm=">
	    					<span class="searchtext"></span><input name="xdr" type="text" class="input_xdr" id="xdr" style="width: 270px;" placeholder="请输入案件名称或行政相对人名称" value=""/>
	    					
	    					<input type="image" src="/xxgs/resources/front/images/jnszfsgs_menu_search.jpg" name="button" id="button" value="提交" class="searchmenu" />
	    				<input type="image" style="margin-left: 20px;" src="/xxgs/resources/front/images/jnszfsgs_menu_reset.jpg" name="reset" id="reset"  onclick="resetForm();return false;" value="重置" class="searchmenu" />
	    				</form>
	    			</td>
				</tr>
			</table>
		</div>
	    <div id="ListBox">
	    	
	    </div>
	</div>
</div>
</body>
</html>

"""

matchObj = re.search(r'encode_text(.*).*', line, re.M | re.I)
print(1)
