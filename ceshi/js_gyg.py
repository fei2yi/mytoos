import jsbeautifier, re


script = '''

var x="if@745@captcha@@g@length@@@0xFF@setTimeout@href@parseInt@@innerHTML@1553769666@@@@@@pathname@@challenge@WhKM@@XC@@Thu@firstChild@11@RegExp@zXQkT@1@a@@return@charCodeAt@@chars@window@@@@@false@createElement@var@charAt@@@@@@@@@while@06@new@split@@k@@@@function@@@@@location@catch@attachEvent@GMT@D@1500@DOMContentLoaded@JgSe0upZ@try@36@28@join@for@rOm9XFMtA3QKV7nYsPGT4lifyWwkq5vcjH2IdxUoCbhERLaz81DNB6@eval@0@Path@Mar@f@substr@div@__jsl_clearance@@41@@onreadystatechange@cookie@d@search@19@J@fromCharCode@e@@X@gC@String@reverse@8@@replace@@toString@@0xEDB88320@@Expires@document@addEventListener@https@@Array@toLowerCase@3@match@@LWhx@else".replace(/@*$/,"").split("@"),y="21 14=2k(){a('32.b=32.l+32.47.4j(/[\\?|&]3-10/,\\'\\')',37);53.45='40=f.2|3h|'+(2k(){1d ['19',[{}+[[]][3h]][3h].22(4h),'4d',[!!{}+[]+[[]][3h]][3h].22(-~[]),'5c',({}+[]+[[]][3h]).22(-~[]),'4e',[-~(+!{})/(+[])+[]+[[]][3h]][3h].22(-~{}),'49',[59+59],'13',(!![][[]]+[]).22(-~-~(+!{})),'2g',[+[-~[], ~~'']+[[]][3h]][3h].22((-~!{}<<-~!{})),'11%',[(-~[]|-~!{}-~!{})],'36'].3d('')})()+';52=15, 3c-3j-48 17:42:2c 35;3i=/;'};1((2k(){3a{1d !!1h.54;}33(4b){1d 1m;}})()){53.54('38',14,1m)}5d{53.34('44',14)}",f=function(x,y){var a=0,b=0,c=0;x=x.split("");y=y||99;while((a=x.shift())&&(b=a.charCodeAt(0)-77.5))c=(Math.abs(b)<13?(b+48.5):parseInt(a,36))+y*c;return c},z=f(y.match(/\w/g).sort(function(x,y){return f(x)-f(y)}).pop());while(z++)try{eval(y.replace(/\b\w+\b/g, function(y){return x[f(y,z)-1]||("_"+y)}));break}catch(_){}

'''
script = script.replace('\r\n', '')
# 在美化之前，去掉\r\n之类的字符才有更好的效果
res = jsbeautifier.beautify(script)
jscode_list = res.split('function')
