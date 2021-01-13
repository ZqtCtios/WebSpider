JST["04paper-edit"] = function(obj) {
	obj || (obj = {});
	var __t, __p = "",
	__e = _.escape,
	__j = Array.prototype.join;
	function print() {
		__p += __j.call(arguments, "")
	}
	with(obj) __p += '<div class="fixheader" style="display: none;">  <div class="g-cw cfx">  <div class="w fl">  <div class="g-mn2">  <h2 data-jedit="title" class="J_edit_tit">' + (null == (__t = data.title) ? "": __t) + '</h2>  </div>  </div>  <div class="g-sd2">  <div class="btn-group">  ',
	data.pid && 0 != data.pid && user.isAdmin ? __p += '  <a href="javascript:;" class="button-g J_submit_uncheck">保存到待审</a>  <a href="javascript:;" class="button-w J_submit_check">保存到已审</a>  ': __p += '  <a href="javascript:;" class="button-g J_submit_paper">完成组卷</a>  <a href="javascript:;" class="button-w J_show_analyze">试卷分析</a>  ',
	__p += '  </div>  </div>  </div> </div> <div class="m-wrap g-cw cfx" id="edit-wrap">  <div class="w fl">  <div class="g-mn2">  ',
	data.source_title && data.spid && (__p += '<div class="source-paper-row">试卷来源：<a href="' + (null == (__t = mURL("/paper/view/", data.spid)) ? "": __t) + '" target="_blank" >' + (null == (__t = data.source_title) ? "": __t) + "</a></div>"),
	__p += '  <div class="paper-wrap">  <div class="paper-sd" data-jset="1"></div>  <div class="paper-mc">  <div class="paper-hd">  \x3c!--考试科目标题--\x3e  <div class="test-title">  \x3c!--主标题--\x3e  <h1 data-jset="3">  <span class="edit-text contenteditable J_edit_tit" data-jedit="title">' + (null == (__t = data.title) ? "": __t) + '</span>  </h1>  \x3c!--副标题--\x3e  <h2 data-jset="5">  <span class="edit-text contenteditable" data-jedit="subtitle">' + (null == (__t = data.subtitle) ? "": __t) + '</span>  </h2>  </div>  \x3c!--考试时间--\x3e  <div class="test-time" data-jset="7">  <span>考试时间：<i class="edit-text contenteditable" data-jedit="examtime">' + (null == (__t = data.examtime) ? "": __t) + '</i>分钟</span>  <span>满分：<i class="edit-text contenteditable" data-jedit="score">' + (null == (__t = data.score) ? "": __t) + '</i>分</span>  </div>  \x3c!--学生信息--\x3e  <ul class="stu-info" data-jset="9">  <li>姓名：<span>____________</span></li>  <li>班级：<span>____________</span></li>  <li>学号：<span>____________</span></li>  </ul>  \x3c!--评分区--\x3e  <div class="mark-table J_mark_table" data-jset="11"></div>  \x3c!--注意事项--\x3e  <div class="rule" data-jset="4">  <p class="note">*注意事项：</p>  <div class="edit-text contenteditable" data-jedit="notes">' + (null == (__t = data.notes) ? "": __t) + '</div>  </div>  </div>  <div class="paper-bd J_paper f-usn" onselectstart="return false" onselect="return false" oncontextmenu="return false" ondragstart="return false"></div>  </div>  </div>    </div>  </div>  <div class="g-sd2">  <div class="btn-group">  ',
	data.pid && 0 != data.pid && user.isAdmin ? __p += '  <a href="javascript:;" class="button-g J_submit_uncheck">保存到待审</a>  <a href="javascript:;" class="button-w J_submit_check">保存到已审</a>  ': __p += '  <a href="javascript:;" class="button-g J_submit_paper">完成组卷</a>  <a href="javascript:;" class="button-w J_show_analyze">试卷分析</a>  ',
	__p += '  </div>  <div id="sd-fix">  <div class="edit-handle J_paper_style"></div>  <div class="edit-handle J_height">  <div class="J_edit_grids f-usn" onselectstart="return false" onselect="return false" oncontextmenu="return false" ondragstart="return false"></div>  <div class="edit-handle-ft">  <a href="/question?tree_type=category&xd=' + (null == (__t = data.xd) ? "": __t) + "&chid=" + (null == (__t = data.chid) ? "": __t) + '" class="handle-btn">继续选题</a>  <a href="javascript:;" class="handle-btn J_new_type">自定义题型</a>  </div>  </div>  </div>  </div> </div>';
	return __p
},
JST["04paper-report"] = function(obj) {
	obj || (obj = {});
	var __t, __p = "",
	__e = _.escape,
	__j = Array.prototype.join;
	function print() {
		__p += __j.call(arguments, "")
	}
	with(obj) __p += '<div class="report-data-wrap g-cw">  <div class="report-hdtit">  <strong class="report-title">  作答报告  <span class="b-tl"></span>  <span class="b-tr"></span>  <span class="b-br"></span>  <span class="b-bl"></span>  </strong>  </div>  <div class="report-data-bd">  <div class="c-circle-wrap">  <span class="c-circle-box">  <div class="cfx">  ' + (null == (__t = JST["report/report-circle"]({
		data: data
	})) ? "": __t) + '  </div>  </span>  </div>  <div class="report-data-con">  <div class="report-data-mt cfx">  <div class="report-data-tit fl">  <i class="iconw-what4"></i>未掌握知识点：  <div class="report-tip">  <i class="iconw-tri-t"></i>  <P>1、知识点得分率计算方式：包含该知识点的试题所得的总分/包含该知识点的试题总分</P>  <p>2、知识点掌握程度小于80%未掌握的知识点。</p>  <p>3、此处只加载未掌握的知识点。</p>  <p>4、点击查看详情，显示此次作答的全部知识点。</p>  </div>  </div>  <div class="fl report-data-item">  ',
	_.each(data.un_know,
	function(t, a) {
		__p += "  " + (null == (__t = 0 == a ? "": "、") ? "": __t) + "<span>" + (null == (__t = t.name ? t.name.name: "--") ? "": __t) + "</span>  "
	}),
	__p += "  </div>  </div>  ",
	_.size(data.errorRateByKnowledge) && (__p += '  <a href="javascript:;" class="report-detail-btn J_know_detail">查看详情</a>  '),
	__p += '  </div>  </div> </div>   <div class="b-wrap g-cw cfx" >  <div class="w fl">  <div class="g-mn2" id="report-warp">  <div class="do-wrap">  <div class="do-q-box">  <div class="do-q-hd">  <div class="do-q-tab J_tab">  <a href="javascript:;" class="current" data-rest="all">全部试题</a>  <a href="javascript:;" data-rest="wrong">做错的题</a>  <a href="javascript:;" data-rest="right">做对的题</a>  </div>  <div class="do-q-handle J_custom_radio">  <label class="checkbox checked">  <b class="iconw-checkbox"></b>  <input type="checkbox" name="answer" value="1" checked style="display: none;">  <span>答案</span>  </label>  <label class="checkbox checked">  <b class="iconw-checkbox"></b>  <input type="checkbox" name="know" value="1" checked style="display: none;">  <span>考点</span>  </label>  <label class="checkbox checked">  <b class="iconw-checkbox"></b>  <input type="checkbox" name="analyze" value="1" checked style="display: none;">  <span>解析</span>  </label>  </div>  </div>   </div>  <div class="do-q-bd J_reprot_con"></div>  </div>  </div>  </div>  <div class="g-sd2">  <div class="edit-handle paper-report-card J_side_card">  <div class="edit-mc">  ',
	head_t_collection.each(function(t) {
		__p += '  <div class="edit-handle-mt">  <strong title="' + (null == (__t = t.get("_t")) ? "": __t) + '"><span>' + (null == (__t = myUtils.chinesesn(t.get("_n"))) ? "": __t) + "、</span>" + (null == (__t = t.get("_t")) ? "": __t) + '</strong>  </div>  <div class="edit-handle-bd">  <ul class="item-num cfx">  ',
		t.collection.each(function(t) {
			__p += "  ",
			1 == t.get("myanswer").is_check ? (__p += "  ", 1 == t.get("myanswer").is_right ? __p += '  <li data-idz="' + (null == (__t = t.id) ? "": __t) + '"><a href="javascript:;" class="right">' + (null == (__t = t.get("_n") + 1) ? "": __t) + "</a></li>  ": __p += '  <li data-idz="' + (null == (__t = t.id) ? "": __t) + '"><a href="javascript:;" class="error">' + (null == (__t = t.get("_n") + 1) ? "": __t) + "</a></li>  ", __p += "  ") : __p += '  <li data-idz="' + (null == (__t = t.id) ? "": __t) + '"><a href="javascript:;">' + (null == (__t = t.get("_n") + 1) ? "": __t) + "</a></li>  ",
			__p += "  "
		}),
		__p += "  </ul>  </div>  "
	}),
	__p += "  </div>  </div>  </div> </div>";
	return __p
},
JST["vip-msg"] = function(obj) {
	obj || (obj = {});
	var __t, __p = "",
	__e = _.escape,
	__j = Array.prototype.join;
	function print() {
		__p += __j.call(arguments, "")
	}
	with(obj) __p += '<style> .top-vip-msg { width: 270px; padding: 0 15px; border: 1px solid #ddd; font-size: 14px; border-radius: 5px; position: absolute; right:0; top: 50px; background: #fff; z-index: 100; } .top-vip-msg .iconw-tri-t { display: inline-block; position: absolute; top: -6px; right: 30px; } .top-vip-msg .mt { height: 34px; line-height: 34px; border-bottom: 1px solid #ddd; } .top-vip-msg .btn-close-it { position: absolute; right: 15px; top: 7px; cursor: pointer; width:23px; height: 23px; display: block; } .top-vip-msg .btn-close-it i { display: block; margin: 5px 0 0 5px;} .top-vip-msg .mc { line-height: 34px; padding: 10px 0; } .top-vip-msg .mb { text-align: right; line-height: 40px; } .top-vip-msg .mb a { color: #2bbb61; } </style> <div class="top-vip-msg">  <b class="iconw-tri-t"></b>  <div class="mt">消息<span class="btn-close-it"><i class="iconw-close2"></i></span></div>  <div class="mc">  ',
	_.each(data,
	function(t) {
		__p += "  <p>" + (null == (__t = t) ? "": __t) + "</p>  "
	}),
	__p += "  </div>  ",
	"zujuan21" == window.Application.AppName ? __p += '  <div class="mb"><a href="//zujuan.21cnjy.com/payment/vip" target="_blank">我要续费</a></div>  ': __p += '  <div class="mb"><a href="/payment/vip-intro" target="_blank" style="color:#4498ee">我要续费</a></div>   ',
	__p += " </div>";
	return __p
},
JST["dialogs/Permission"] = function(obj) {
	obj || (obj = {});
	var __t, __p = "",
	__e = _.escape,
	__j = Array.prototype.join;
	function print() {
		__p += __j.call(arguments, "")
	}
	with(obj)"zujuan21" == window.Application.AppName ? __p += ' <div style="padding:45px 10px; text-align: center;">  <div class="vip-tips">  <p>抱歉，该功能仅限VIP与组卷通用户使用。</p>  <div class="enters">  <a href="/payment/vip" target="_blank">购买VIP</a>  <a href="/help/request" target="_blank">申请免费试用（组卷通）</a>  </div>  </div> </div> ': __p += '  <div style="padding:45px 10px; text-align: center;">  <div class="vip-tips">  <p>抱歉，该功能仅限VIP用户使用。</p>  <div class="enters">  <a href="/payment/vip-intro" target="_blank">购买VIP</a>  </div>  </div>  </div> ';
	return __p
},
JST["dialogs/paper-analyze"] = function(obj) {
	obj || (obj = {});
	var __t, __p = "",
	__e = _.escape,
	__j = Array.prototype.join;
	function print() {
		__p += __j.call(arguments, "")
	}
	with(obj) __p += '<div class="paper-analysis-fixed" data-modal-title="试卷分析">  <div class="paper-analysis">  <div class="analysis-block">  <h3 class="analysis-tit"><span>试卷总体分布分析</span></h3>  <table class="analysis-table">  <thead>  <tr>  <th colspan="3">总分：' + (null == (__t = grid1.score) ? "": __t) + '</th>  </tr>  </thead>  <tbody>  <tr>  <th rowspan="2">分值分布</th>  <th>客观题（占比）</th>  <td>' + (null == (__t = grid1.row1[0]) ? "": __t) + "（" + (null == (__t = grid1.row1[1]) ? "": __t) + "）</td>  </tr>  <tr>  <th>主观题（占比）</th>  <td>" + (null == (__t = grid1.row1[2]) ? "": __t) + "（" + (null == (__t = grid1.row1[3]) ? "": __t) + '）</td>  </tr>  <tr>  <th rowspan="2">题量分布</th>  <th>客观题（占比）</th>  <td>' + (null == (__t = grid1.row2[0]) ? "": __t) + "（" + (null == (__t = grid1.row2[1]) ? "": __t) + "）</td>  </tr>  <tr>  <th>主观题（占比）</th>  <td>" + (null == (__t = grid1.row2[2]) ? "": __t) + "（" + (null == (__t = grid1.row2[3]) ? "": __t) + '）</td>  </tr>  </tbody>  </table>  </div>  <div class="f-cb">  <div class="analysis-cell f-fl">  <div class="analysis-block">  <div class="analysis-tit"><span>试卷题量分布分析</span></div>  <table class="analysis-table">  <thead>  <tr>  <th>大题题型</th>  <th>题目量（占比）</th>  <th>分值（占比）</th>  </tr>  </thead>  <tbody>  ',
	_.each(grid2,
	function(t) {
		__p += "  <tr>  <th>" + (null == (__t = t.title) ? "": __t) + "</th>  <td>" + (null == (__t = t.q_num) ? "": __t) + "（" + (null == (__t = t.q_percent) ? "": __t) + "）</td>  <td>" + (null == (__t = t.s_num) ? "": __t) + "（" + (null == (__t = t.s_percent) ? "": __t) + "）</td>  </tr>  "
	}),
	__p += '\t  </tbody>  </table>  </div>  </div>  <div class="analysis-cell f-fr">  <div class="analysis-block">  <h3 class="analysis-tit"><span>试卷难度结构分析</span></h3>  <div class="analysis-chart" id="J_chart_container" style="min-height:160px; width: 360px"></div>  </div>  </div>  </div>  <div class="analysis-block">  <h3 class="analysis-tit"><span>试卷知识点分析</span></h3>  <table class="analysis-table">  <thead>  <tr>  <th>序号</th>  <th>知识点（认知水平）</th>  <th>分值（占比）</th>  <th>对应题号</th>  </tr>  </thead>  <tbody>  ',
	_.each(grid4,
	function(t) {
		__p += "  <tr>  <td>" + (null == (__t = t.sn) ? "": __t) + "</td>  <td>" + (null == (__t = t.knowledge) ? "": __t) + "</td>  <td>" + (null == (__t = t.s_num) ? "": __t) + "（" + (null == (__t = t.s_percent) ? "": __t) + '）</td>  <td><span class="pre-w">' + (null == (__t = t.id) ? "": __t) + "</span></td>  </tr>  "
	}),
	__p += "  </tbody>  </table>  </div>  </div>  </div>";
	return __p
},
JST["dialogs/paper-card"] = function(obj) {
	obj || (obj = {});
	var __t, __p = "",
	__e = _.escape,
	__j = Array.prototype.join;
	function print() {
		__p += __j.call(arguments, "")
	}
	with(obj) {
		if (__p += '<link rel="stylesheet" href="' + (null == (__t = CDN_LOCAL_DOMAIN) ? "": __t) + '/css/popup.min.css?v=8ce06c807d"> <link rel="stylesheet" href="' + (null == (__t = CDN_LOCAL_DOMAIN) ? "": __t) + '/css/spriter-a.min.css?v=c8a2fa51d7"> <link rel="stylesheet" href="' + (null == (__t = CDN_LOCAL_DOMAIN) ? "": __t) + '/css/spriter-mix.min.css?v=c8a2fa51d7"> <style>  .ui-dialog-content { width: 520px; }  .answersheet-con { padding: 20px 20px 20px 20px;}   </style> <div class="answersheet-con">  <div class="sheet-title">请选择需要下载的题卡类型，选中后点击“确定”按钮即可下载</div>  <div class="sheet-line2 f-cb">  <span>答题卡类型：</span>  <div class="sheet-tab">  <a href="javascript:;" data-sheet="1" class="sheet-item active">普通题卡</a>  <a href="javascript:;" data-sheet="2" class="sheet-item">标准题卡</a>  <a href="javascript:;" data-sheet="3" class="sheet-item">密集题卡</a>  \x3c!-- <a href="javascript:;" data-sheet="4" class="sheet-item">阅卷题卡</a> --\x3e  </div>  </div>  \x3c!-- <div class="sheet-line f-cb">  <label>答题卡样式：</label>  <div class="menu sheet-section">  <span class="s-title">普通表格型</span><i class="icona-tri"></i>  <ul class="sheet-list">  <li data-sheet="1">普通表格型</li>  <li data-sheet="2">标准题卡型</li>  <li data-sheet="3">选择密集型</li>  </ul>  </div>  </div> --\x3e  <div class="sheet">  <div>  <img src="' + (null == (__t = CDN_LOCAL_DOMAIN) ? "": __t) + '/images/putong.png">  <p class="sheet-tips">普通题卡适用于一般的普通考试及测评使用，如：周测、家庭作业答题使用</p>  </div>  <div style="display: none;">  <img src="' + (null == (__t = CDN_LOCAL_DOMAIN) ? "": __t) + '/images/biaozhun.png">  <p class="sheet-tips">标准题卡适用于普通考试及日常考试使用，如：周考、月考等使用</p>  </div>  <div style="display: none;">  <img src="' + (null == (__t = CDN_LOCAL_DOMAIN) ? "": __t) + '/images/miji.png">  <p class="sheet-tips">密集题卡适用于普通考试及日常考试使用,如：周考、月考、期中考、期末考等使用</p>  </div>  <div style="display: none;">  <img src="' + (null == (__t = CDN_LOCAL_DOMAIN) ? "": __t) + '/images/yuejuan.png">  <p class="sheet-tips">阅卷题卡适用于普通考试、日常考试及中/高考升学考试使用，如：周考、月考、期中考、期末考、中考、高考等使用。支持在线编辑题卡操作</p>  ', "zujuan21" == window.Application.AppName) {
			__p += "  ";
			var pred = _.size(User.vip) || User.school_permit_id;
			pred || (__p += '  <div class="sheet-limit">  <p>温馨提示：</p>  <p>阅卷题卡下载仅对VIP及组卷通用户使用，您如需使用，请选前往 <a href="/payment/vip" target="_blank">购买VIP</a> 或在线免费<a href="/help/request" target="_blank">申请组卷通</a></p>  </div>  '),
			__p += "  "
		}
		__p += "  ",
		"zujuanw" == window.Application.AppName && (__p += "  ", _.size(User.vip) || (__p += '  <div class="sheet-limit">  <p>温馨提示：</p>  <p>阅卷题卡下载仅对VIP用户使用，您如需使用，请选前往 <a href="/payment/vip-intro" target="_blank">购买VIP</a></p>  </div>  '), __p += "  "),
		__p += "  </div>  </div> </div>"
	}
	return __p
},
JST["dialogs/paper-download"] = function(obj) {
	obj || (obj = {});
	var __t, __p = "",
	__e = _.escape,
	__j = Array.prototype.join;
	function print() {
		__p += __j.call(arguments, "")
	}
	with(obj) __p += '<div> <link rel="stylesheet" href="' + (null == (__t = CDN_LOCAL_DOMAIN) ? "": __t) + '/css/spriter-a.min.css?v=c8a2fa51d7"> <link rel="stylesheet" href="' + (null == (__t = CDN_LOCAL_DOMAIN) ? "": __t) + '/css/spriter-mix.min.css?v=c8a2fa51d7"> <style>  .form-paper-download { width: 500px; height: 500px; overflow-y: auto; } .form-paper-download i { display: inline-block; } .download-msg { padding-left: 0; padding-right: 0; } .download-hint, .download-size, .download-type, .download-math, .download-beizu { padding-left: 10px; padding-right: 10px; border-bottom: 0px; zoom: 1; }  .download-type-content .checkbox, .download-type-con .radiobox { margin-right: 10px; } </style> <div class="form-paper-download">  <form class="P_download">  <input type="hidden" name="pid" value="' + (null == (__t = pid) ? "": __t) + '" >   <div class=" download-msg">  <div class="download-size">  <div class="download-text">纸张大小：</div>  <div class="size-con download-bd J_radio_group">  <div class="size-a4 radiobox checked">  <span>  <i class="icona-radio"></i>  <input type="radio" value="A4" name="size" checked style="display: none;">  </span>  <i class="icona-a4"></i>  <p>A4</p>  </div>  <div class="size-a3 radiobox">  <span>  <i class="icona-radio"></i>  <input type="radio" value="A3" name="size" style="display: none;">  </span>  <i class="icona-a3"></i>  <p>A3（双栏）</p>  </div>  <div class="size-a4 radiobox">  <span>  <i class="icona-radio"></i>  <input type="radio" value="B5" name="size" style="display: none;">  </span>  <i class="icona-a4"></i>  <p>B5</p>  </div>  <div class="size-a3 radiobox">  <span>  <i class="icona-radio"></i>  <input type="radio" value="B4" name="size" style="display: none;">  </span>  <i class="icona-a3"></i>  <p>B4（双栏）</p>  </div>  </div>   </div>  <div class="download-type">  <div class="download-text">试卷内容：</div>  <div class="download-type-content download-bd J_content">  <span class="checkbox checked">  <i class="icona-check"></i>  <input type="checkbox" style="display:none" value="an" checked name="content_type[]">  答案  </span>  <span class="checkbox">  <i class="icona-check"></i>  <input type="checkbox" style="display:none" value="kw" name="content_type[]">  考点  </span>  <span class="checkbox">  <i class="icona-check"></i>  <input type="checkbox" style="display:none" value="ex" name="content_type[]">  解析  </span>   <span class="checkbox">  <i class="icona-check"></i>  <input type="checkbox" style="display:none" value="sc" name="content_type[]">  小题分  </span>   <span class="checkbox">  <i class="icona-check"></i>  <input type="checkbox" style="display:none" value="fx" name="content_type[]">  分析  </span>   </div>  </div>  </div>  <div class="download-math">  <div class="download-text">公式形式：</div>  <div class="download-type-con download-bd J_radio_group">  <span class="radiobox checked">  <i class="icona-radio"></i>  <input type="radio" value="2" name="renderMathAsImg" checked style="display: none;">  图片公式（不可编辑）  </span>  <span class="radiobox" style="display:block">  <i class="icona-radio"></i>  <input type="radio" value="1" name="renderMathAsImg" style="display: none;">  文本公式（可编辑）<b style="font-size:12px; color:#f00;">请使用Word2010及以上版本打开编辑</b>  </span>  </div>  </div>  <div class="download-type">  <div class="download-text">试卷类型：</div>  <div class="download-type-con download-bd J_radio_group">  <span class="radiobox">  <i class="icona-radio"></i>  <input type="radio" value="teacher" name="type" style="display: none;">  教师用卷（答案在题后）  </span>  <span class="radiobox checked">  <i class="icona-radio"></i>  <input type="radio" value="student" name="type" checked style="display: none;">  学生用卷（答案在卷尾）  </span>  </div>  </div>  <div class="download-hint">  ',
	User.co_partner ? (__p += '  <div class="download-bd">  ', verifyCode && (__p += '  <div class="download-verifycode">  <label for="v-code">验证码：</label>  <input type="text" name=\'code\' id="v-code" placeholder="请输入验证码">  <span class="yzm">' + (null == (__t = verifyCode) ? "": __t) + '</span>  <span class="hint" style="display:none;"></span>  </div>  '), __p += '  <div class="recharge-btn-box"><button class="recharge-btn" type="submit">下 载</button></div>  </div>   ') : (__p += '  <div class="download-bd">  ', isUnit && !limitStatus[3] && (__p += '  <div class="hint-con">  ', isOnDue ? (__p += "  ", limitStatus[0] ? (isEnd = !0, __p += '  <p>您为“组卷通”用户，此次下载<b class="highlight strong">免费</b></p>  <p class="small"> “组卷通” 到期时间：<b class="highlight">' + (null == (__t = moment(1e3 * productInfo.etime).format("YYYY-MM-DD")) ? "": __t) + "</b></p>  ") : (isEnd = !1, isUnitOutLimit = !0, __p += '  <p><b class="highlight">' + (null == (__t = limitStatus[1]) ? "": __t) + "</b></p>  ")) : (isEnd = !1, isUnitOutDue = !0), __p += "  ", __p += "  </div>  "), __p += "   ", isUnitOutLimit || (__p += "  ", !isEnd && PaperCount.isfree && (isEnd = !0, __p += '  <div class="hint-con">  <p>你下载过这份试卷，15天内下载<b class="highlight strong">免费</b></p>  </div>  '), __p += "   ", !isEnd && newvip.deadline ? (__p += '  <div class="hint-con">  ', newvip.coin && (isEnd = !0, __p += '  <p>您为vip用户，此次下载<b class="highlight">免费</b></p>  <p class="small">剩余下载次数:<b class="highlight">' + (null == (__t = newvip.coin) ? "": __t) + "</b>, 到期时间:" + (null == (__t = moment(1e3 * newvip.deadline).format("YYYY-MM-DD")) ? "": __t) + "</p>  "), __p += "  </div>  ") : !isEnd && isUnitOutDue && (__p += '  <div class="hint-con">  <p><b class="highlight">非常抱歉，“组卷通”已到期！</b><a href="/help/request" target="_blank">立即申请</a></p>  </div>   '), __p += "   ", !isEnd && (xuebi.coin >= 3 * PaperCount.point || pu >= PaperCount.point) && (isEnd = !0, __p += '  <div class="hint-con">  ', vipLimitMsg && (__p += ' <p><b class="highlight">' + (null == (__t = vipLimitMsg) ? "": __t) + "</b></p> "), __p += '  <p>此次下载需扣除： 学币<b class="highlight">' + (null == (__t = PaperCount.xuebi) ? "": __t) + '</b>个  <span class="lowlight">（或普通点' + (null == (__t = PaperCount.point) ? "": __t) + '个）</span>  </p>  <p class="small">您当前剩余：<b>' + (null == (__t = xuebi.coin) ? "": __t) + "</b>个学币，<b>" + (null == (__t = pu) ? "": __t) + "</b>个普通点</p>  </div>  "), __p += "  "), __p += "   ", isEnd || hasWxpay || isUnitOutDue || isUnitOutLimit || (__p += "  ", vipLimitMsg && (__p += ' <div class="hint-con"> <p><b class="highlight">' + (null == (__t = vipLimitMsg) ? "": __t) + "</b></p> </div> "), __p += "  ", wxpayInfo && 1 == wxpayInfo.status ? __p += '  <div class="recharge-btn-box wxpay_info">  <p style="padding:5px 0;">  <strong style="color:#333;font-weight:bold">需付：</strong><font style="color:#3db06e;font-weight:bold">' + (null == (__t = wxpayInfo.paymoney) ? "": __t) + '</font><br>  </p>  <img src="' + (null == (__t = wxpayInfo.wxpayUrl) ? "": __t) + '" width="160" height="160"><br>  <div style="padding: 5px 0;">  <img src="' + (null == (__t = CDN_LOCAL_DOMAIN) ? "": __t) + '/s/images/wx.png" style="width:40px;height:40px; padding: 0 2px;">  <img src="' + (null == (__t = CDN_LOCAL_DOMAIN) ? "": __t) + '/s/images/alipay.png" style="width:40px;height:40px; padding: 0 2px;">  </div>  （使用微信/支付宝安全支付，支付成功自动下载）  </div>  \x3c!-- <div class="recharge-btn-box down_btn" style="display:none">  <font style="color:#3db06e;font-weight:bold">已通过微信支付，可以正常下载！</font><br>  <button class="recharge-btn" type="submit">下 载</button>  </div> --\x3e  ': __p += '   <div class="recharge-btn-box">  <font style="color:red;font-weight:bold">(error: ' + (null == (__t = wxpayInfo.error ? wxpayInfo.error: "") ? "": __t) + ")生成二维码失败！请联系客服QQ：81321902</font>  </div>  ", __p += "  "), __p += "   ", !isEnd && hasWxpay && (isEnd = !0, __p += '  <div class="recharge-btn-box">  <font style="color:#3db06e;font-weight:bold">已通过扫码支付，可以正常下载！</font>  </div>  '), __p += "  ", verifyCode && (__p += '  <div class="download-verifycode">  <label for="v-code">验证码：</label>  <input type="text" name=\'code\' id="v-code" placeholder="请输入验证码">  <span class="yzm">' + (null == (__t = verifyCode) ? "": __t) + '</span>  <span class="hint" style="display:none;"></span>  </div>  '), __p += "  ", isEnd && (__p += ' <div class="recharge-btn-box"><button class="recharge-btn" type="submit">下 载</button></div> '), __p += "    </div>  "),
	__p += "  </div>  </form>  ",
	User.co_partner || (__p += '  <div class="download-beizu" style="padding-bottom: 15px;">  <div class="download-text" style="padding-top:0;"> 温馨提示：</div>  <div class="download-bd">  <p class="small">1、VIP用户下载免费。 <a href="/payment/vip" target="_blank">开通VIP</a></p>  <p class="small">2、如有问题，请联系客服QQ：4006379991 </p>  </div>  ', pu && (__p += '  <div style="margin:5px 10px; padding:10px; background:#fff8f2; border:1px solid #eab180;" style="display:none;">  <div>网站将于<span style="color:#f00">2020年01月01日</span>起关闭普通点的下载通道，统一下载货币为“学币”，在此之前请将普通点兑换成学币。  </div>  <div class="cfx">  <p class="fl">当前账号剩余普通点：<span style="color:#f00">' + (null == (__t = pu) ? "": __t) + '个</span></p>  <a href="https://www.21cnjy.com/ucp.php?mod=change_coins" target="_blank" class="fr" style="color:#f00;">【立即兑换】</a>  </div>  </div>  '), __p += "  </div>  "),
	__p += "    </div> </div>";
	return __p
},
JST["dialogs/paper-download_old"] = function(obj) {
	obj || (obj = {});
	var __t, __p = "",
	__e = _.escape,
	__j = Array.prototype.join;
	function print() {
		__p += __j.call(arguments, "")
	}
	with(obj) __p += '<div class=" download-msg">  <div class="download-size">  <div class="download-text" style="height: 120px;">  纸张大小：  </div>  <div class="size-con">  <div class="size-a4 radiobox checked">  <span>  <i class="icona-radio"></i>  <input type="radio" value="A4" name="chooseSize" checked style="display: none;">  </span>  <i class="icona-a4"></i>  <p>A4</p>  </div>  <div class="size-a3 radiobox">  <span>  <i class="icona-radio"></i>  <input type="radio" value="A3" name="chooseSize" style="display: none;">  </span>  <i class="icona-a3"></i>  <p>A3（双栏）</p>  </div>  </div>   <div class="size-con">  <div class="size-a4 radiobox">  <span>  <i class="icona-radio"></i>  <input type="radio" value="B5" name="chooseSize" style="display: none;">  </span>  <i class="icona-a4"></i>  <p>B5</p>  </div>  <div class="size-a3 radiobox">  <span>  <i class="icona-radio"></i>  <input type="radio" value="B4" name="chooseSize" style="display: none;">  </span>  <i class="icona-a3"></i>  <p>B4（双栏）</p>  </div>  </div>   </div>  <div class="download-type">  <div class="download-text">  试卷类型：  </div>  <div class="download-type-con">  <div>  <span class="radiobox">  <i class="icona-radio"></i>  <input type="radio" value="teacher" name="chooseType" style="display: none;">  教师用卷（答案在题后）  </span>  <label></label>  </div>  <div>  <span class="radiobox checked">  <i class="icona-radio"></i>  <input type="radio" value="student" name="chooseType" checked style="display: none;">  学生用卷（答案在卷尾）  </span>  <label></label>  </div>  </div>  </div>  <div class="download-hint">  <div class="download-text">  扣费提示：  </div>  ',
	data.unitcount.isOnDue ? (__p += '  <div class="hint-con">  ', data.unitcount.limitStatus[0] ? __p += "  <p>此次下载需扣除您所属的单位账户额度1份</p>  ": __p += "  <p>您所属的单位账户下载受限</p>  <p>系统提示：" + (null == (__t = data.unitcount.limitStatus[1]) ? "": __t) + "</p>  ", __p += "  </div>  ") : data.paperinfo.isfree ? __p += '  <div class="hint-con">  <p>您已下载过这份试卷,15天内再次下载免费</p>  </div>  ': (__p += '  <div class="hint-con">  ', 0 < data.userinfo.newvip.coin ? __p += '  <p>您为vip用户，此次下载<b class="highlight">免费</b></p>  <p>剩余下载次数:<b class="highlight">' + (null == (__t = data.userinfo.newvip.coin) ? "": __t) + '</b>到期时间:<b class="highlight">' + (null == (__t = data.userinfo.newvip.deadline) ? "": __t) + "</b></p>  ": __p += "  <p>您当前剩余：<b>" + (null == (__t = data.userinfo.xuebi.coin) ? "": __t) + "</b>个学币，<b>" + (null == (__t = data.userinfo.pu) ? "": __t) + "</b>个普通点</p>  <p>本次下载含普通试题<b>" + (null == (__t = data.paperinfo.common) ? "": __t) + "</b>个，精品试题<b>" + (null == (__t = data.paperinfo.special) ? "": __t) + '</b>个</p>  <p>此次下载需扣除普通点：  <b class="highlight">' + (null == (__t = data.paperinfo.point) ? "": __t) + '</b>个  或学币<b class="highlight">' + (null == (__t = data.paperinfo.xuebi) ? "": __t) + "</b>个  </p>  ", __p += "  </div>  "),
	__p += '  <p></p>  <div class="hint-msg">  <div class="hint-tit">  温馨提示：  </div>  <div class="hint-text">  <p>1、组卷通用户下载免费。 <a href="/help/zujuan" target="blank" style="color:#17A3E0;">学校/培训机构申请免费试用</a></p>  <p>2、VIP用户下载免费。 <a href="/payment/vip" target="blank" style="color:#17A3E0;">开通VIP</a></p>  <p>3、如有问题，请联系客服QQ：81321902 </p>  </div>  </div>  </div>  </div>';
	return __p
},
JST["dialogs/paper-join"] = function(obj) {
	obj || (obj = {});
	var __t, __p = "",
	__e = _.escape,
	__j = Array.prototype.join;
	function print() {
		__p += __j.call(arguments, "")
	}
	with(obj) __p += '<div class=" download-msg">  <style type="text/css">  .mytest-data {margin:10px 0} .mytest-data select { margin-left: 10px;} .mytest-data td {text-align: left; padding:5px 0; } .mytest-data select {width: 140px; padding: 2px 0;} .mytest-data input {margin-left: 10px; padding: 2px 4px;}   </style>  <form id =\'share-form\'>  <input type="hidden" name="pid" value="' + (null == (__t = pid) ? "": __t) + '"/>  <input type="hidden" name="_csrf" value="' + (null == (__t = _csrf) ? "": __t) + '">  <table width="100%" class="mytest-data" id="sharedata">  <tbody>  <tr>  <td height="40" colspan="2">  试卷名称:<input type="text" class="papers papers-tit" value="' + (null == (__t = title) ? "": __t) + '" name="title" style="width:300px; color:#9a9a9a">  </td>  </tr>  <tr>  <td>  地区:  <select class="papers" name="province">  <option value="0">全国</option>  <option value="1">北京市</option>  <option value="2">天津市</option>  <option value="3">河北省</option>  <option value="4">山西省</option>  <option value="5">内蒙古自治区</option>  <option value="6">辽宁省</option>  <option value="7">吉林省</option>  <option value="8">黑龙江省</option>  <option value="9">上海市</option>  <option value="10">江苏省</option>  <option value="11">浙江省</option>  <option value="12">安徽省</option>  <option value="13">福建省</option>  <option value="14">江西省</option>  <option value="15">山东省</option>  <option value="16">河南省</option>  <option value="17">湖北省</option>  <option value="18">湖南省</option>  <option value="19">广东省</option>  <option value="20">广西壮族自治区</option>  <option value="21">海南省</option>  <option value="22">重庆市</option>  <option value="23">四川省</option>  <option value="24">贵州省</option>  <option value="25">云南省</option>  <option value="26">西藏自治区</option>  <option value="27">陕西省</option>  <option value="28">甘肃省</option>  <option value="29">青海省</option>  <option value="30">宁夏回族自治区</option>  <option value="31">新疆维吾尔自治区</option>  </select>  </td>   <td>  年级:  <select class="papers" name="gradeid">  ',
	_.each(nianji,
	function(t, a) {
		__p += '  <option value="' + (null == (__t = a) ? "": __t) + '">' + (null == (__t = t) ? "": __t) + "</option>  "
	}),
	__p += '  </select>  </td>  <td>  类型:  <select class="papers" name="papertype">  ',
	_.each(papertype,
	function(t, a) {
		__p += '  <option value="' + (null == (__t = a) ? "": __t) + '">' + (null == (__t = t) ? "": __t) + "</option>  "
	}),
	__p += "  </select>  </td>  </tr>  <tr>  </tr>  </tbody>  </table>  </form>  注：投稿成功后将由组委会对您的试卷进行评分，获奖名单将于活动结束后七天内进行公布 </div>";
	return __p
},
JST["dialogs/paper-newtype"] = function(obj) {
	obj || (obj = {});
	var __t, __p = "",
	__e = _.escape;
	with(obj) __p += '<div class="add-type-con custom-modal" data-modal-title="添加新题型">  <p>请输入新题型名称：<span class="error-msg"></span></p>  <input type="text" name="" value="" /> </div>';
	return __p
},
JST["dialogs/paper-share"] = function(obj) {
	obj || (obj = {});
	var __t, __p = "",
	__e = _.escape,
	__j = Array.prototype.join;
	function print() {
		__p += __j.call(arguments, "")
	}
	with(obj) __p += '<div class=" download-msg">  <style type="text/css">  .mytest-data {margin:10px 0} .mytest-data select { margin-left: 10px;} .mytest-data td {text-align: left; padding:5px 0; } .mytest-data select {width: 140px; padding: 2px 0;} .mytest-data input {margin-left: 10px; padding: 2px 4px;}   </style>  <form id =\'share-form\'>  <input type="hidden" name="pid" value="' + (null == (__t = pid) ? "": __t) + '"/>  <input type="hidden" name="_csrf" value="' + (null == (__t = _csrf) ? "": __t) + '">  <table width="100%" class="mytest-data" id="sharedata">  <tbody>  <tr>  <td height="40" colspan="2">  试卷名称:<input type="text" class="papers papers-tit" value="' + (null == (__t = title) ? "": __t) + '" name="title" style="width:300px; color:#9a9a9a">  </td>  </tr>  <tr>  <td>  地区:  <select class="papers" name="province">  <option value="0">全国</option>  <option value="1">北京市</option>  <option value="2">天津市</option>  <option value="3">河北省</option>  <option value="4">山西省</option>  <option value="5">内蒙古自治区</option>  <option value="6">辽宁省</option>  <option value="7">吉林省</option>  <option value="8">黑龙江省</option>  <option value="9">上海市</option>  <option value="10">江苏省</option>  <option value="11">浙江省</option>  <option value="12">安徽省</option>  <option value="13">福建省</option>  <option value="14">江西省</option>  <option value="15">山东省</option>  <option value="16">河南省</option>  <option value="17">湖北省</option>  <option value="18">湖南省</option>  <option value="19">广东省</option>  <option value="20">广西壮族自治区</option>  <option value="21">海南省</option>  <option value="22">重庆市</option>  <option value="23">四川省</option>  <option value="24">贵州省</option>  <option value="25">云南省</option>  <option value="26">西藏自治区</option>  <option value="27">陕西省</option>  <option value="28">甘肃省</option>  <option value="29">青海省</option>  <option value="30">宁夏回族自治区</option>  <option value="31">新疆维吾尔自治区</option>  </select>  </td>   <td>  年级:  <select class="papers" name="gradeid">  ',
	_.each(nianji,
	function(t, a) {
		__p += '  <option value="' + (null == (__t = a) ? "": __t) + '">' + (null == (__t = t) ? "": __t) + "</option>  "
	}),
	__p += '  </select>  </td>  <td>  类型:  <select class="papers" name="papertype">  ',
	_.each(papertype,
	function(t, a) {
		__p += '  <option value="' + (null == (__t = a) ? "": __t) + '">' + (null == (__t = t) ? "": __t) + "</option>  "
	}),
	__p += '  </select>  </td>  </tr>  <tr>  </tr>  </tbody>  </table>  </form>  注：共享试卷成功后，其他用户也可以看到您的组卷哦。同时，您也会得到一定的<label style="color:#FF9136;">积分</label>作为奖励。 </div>';
	return __p
},
JST["dialogs/paper-temp-test"] = function(obj) {
	obj || (obj = {});
	var __t, __p = "",
	__e = _.escape;
	with(obj) __p += '<style>  .temp-test-box { width: 460px; }  .temp-test-link { width: 328px; border: 1px solid #ddd; background: #fff; font-size: 12px; line-height: 1.6; padding: 5px; border-radius: 5px; }  .test-link-btn {  margin-left: 10px;  width: 100px;  height: 36px;  line-height: 36px;  text-align: center;  color: #fff;  font-size: 12px;  background: #2bbb61;  border-radius: 5px;  border: none;  outline: none;  }  .test-link-btn:hover { background: #5ecb87; }   .temp-test-tip { font-size: 12px; margin-top: 10px; color: #333; } </style> <div class="temp-test-box">  <input type="text" id="copyurl" value=\'https://' + (null == (__t = "zujuanw" == Application.AppName ? "www.zujuan.com": "zujuan.21cnjy.com") ? "": __t) + (null == (__t = mURL("/paper/view/", pid)) ? "": __t) + "?code=" + (null == (__t = code) ? "": __t) + '\' class="temp-test-link">  <button type="button" class="test-link-btn" onclick="copyUrl();">复制链接</button>  <P class="temp-test-tip">温馨提示：您可以通过此链接将试卷分享给用户进行下载或作答</P> </div>  <script>  function copyUrl(){  var Url=document.getElementById("copyurl");  Url.select();   document.execCommand("Copy");   } <\/script>';
	return __p
},
JST["dialogs/ques-error"] = function(obj) {
	obj || (obj = {});
	var __t, __p = "",
	__e = _.escape;
	with(obj) __p += '<div class="error-con custom-modal" data-modal-title="试题纠错"> \t<form> \t\t<input type="hidden" name="qid" value="' + (null == (__t = question_id) ? "": __t) + '"> \t\t<p>*请在下方输入框内输入纠错内容，纠错一经审核通过我们将给予您30 ~ 150 的积分奖励</p> \t\t\x3c!-- <textarea name="message"></textarea> --\x3e \t\t<div class="error-report-textarea J_messageInput" contenteditable></div> \t\t<div class="warn"></div> \t\t<div class="candy-words cfx"> \t\t\t<a href="/help/youjiangjiucuo" target="_blank">奖励说明</a>  \t\t\t<a href="/u/question/error" target="_blank">纠错统计</a> \t\t\t<span style="color:#999" ></span> \t\t</div> \t\t<input type="hidden" name="_csrf" value="' + (null == (__t = Application.dataState.csrf._csrf) ? "": __t) + '" > \t</form> </div';
	return __p
},
JST["dialogs/ques-migrate"] = function(obj) {
	obj || (obj = {});
	var __t, __p = "",
	__e = _.escape,
	__j = Array.prototype.join;
	function print() {
		__p += __j.call(arguments, "")
	}
	with(obj) __p += '<div class="transfer-con f-usn custom-modal" onselectstart="return false" data-modal-title="转移试题">  <div class="transfer-title">  将第' + (null == (__t = model.get("_n") + 1) ? "": __t) + '题转移至：  </div>  <div class="transfer-num">  <form>  <ul>  ',
	_.each(type_views,
	function(t, a) {
		__p += '  <li>  <span data-vid="' + (null == (__t = t.cid) ? "": __t) + '" class="custom-radio ' + (null == (__t = t.cid == t_view.cid ? "checked": "") ? "": __t) + '">  <i class="iconw-radio"></i>' + (null == (__t = myUtils.chinesesn(a)) ? "": __t) + "、" + (null == (__t = t.model.get("_t")) ? "": __t) + "  </span>  </li>  "
	}),
	__p += '  </ul>  <input type="hidden" name="_vid" value="' + (null == (__t = t_view.cid) ? "": __t) + '">  </form>  </div> </div>';
	return __p
},
JST["dialogs/ques-replace"] = function(obj) {
	obj || (obj = {});
	var __t, __p = "",
	__e = _.escape,
	__j = Array.prototype.join;
	function print() {
		__p += __j.call(arguments, "")
	}
	with(obj) null === data ? __p += ' <div class="shade-bg"></div> <div class="p-replace-wrap ">  <div class="loading">  \x3c!-- <img src="' + (null == (__t = CDN_LOCAL_DOMAIN) ? "": __t) + '/build/images/loading.gif">  <span>试题正在加载中...</span> --\x3e  </div>  <div class="p-body J_bd_replace"></div> </div> ': (__p += ' <div class="p-con-hd f-cb">  <ul class="p-con-num f-cb">  ', _.each(data.questions,
	function(t, a) {
		__p += '  <li><a href="javascript:;" data-n="' + (null == (__t = a) ? "": __t) + '" class="J_ques_tab ' + (null == (__t = 0 == a ? "active": "") ? "": __t) + '">' + (null == (__t = a + 1) ? "": __t) + "</a></li>  "
	}), __p += "  </ul>  ", 10 < data.count && (__p += '  <a href="javascript:;" class="change-btn J_reload_replace">换一批</a>  '), __p += ' </div> <div class="p-con-bd">  <div class="p-content">  ', 0 < _.size(data.questions) ? __p += '  <ul class="J_ques_list"></ul>  ': __p += '  <div class="empty-ffxi">  <img src="' + (null == (__t = CDN_LOCAL_DOMAIN) ? "": __t) + '/images/blank.png">  <p>暂无可替换的试题</p>  </div>  ', __p += '  </div>  <div class="p-q-ft">  ', _.size(data.questions) && (__p += '  <a href="javascript:;" class="replace-btn J_submit_replace">替换</a>  '), __p += '  <a href="javascript:;" class="p-close J_close_replace">关闭</a>  </div> </div> ');
	return __p
},
JST["dialogs/save-paper"] = function(obj) {
	obj || (obj = {});
	var __t, __p = "",
	__e = _.escape;
	with(obj) __p += '<div class="form-save-paper custom-modal">  <form action="">  <p class="field-tip" style="display:none">请输入标题。</p>  <div class="field-line">  <label for="field-paper-tit">标题：</label>  <input class="field-tit" type="text" id="field-paper-tit" name="title" value="' + (null == (__t = title) ? "": __t) + '" >  </div>  <div>注：保存后的试卷可在<a href="/u/zujuan" class="field-go">用户中心--组卷记录</a>中查看</div>  </form> </div>';
	return __p
},
JST["dialogs/save-test"] = function(obj) {
	obj || (obj = {});
	var __t, __p = "",
	__e = _.escape;
	with(obj) __p += '<div class="pop-tit"><span>作答保存成功</span></div> <P class="pop-txt mt10">您可以在<a href="/u/ceshi" target="_blank" class="field-go">个人中心--测试记录</a>进行查看</P> <button type="button" class="pop-btn doing">继续做题</button>';
	return __p
},
JST["dialogs/select-ximutype"] = function(obj) {
	obj || (obj = {});
	var __t, __p = "",
	__e = _.escape,
	__j = Array.prototype.join;
	function print() {
		__p += __j.call(arguments, "")
	}
	with(obj) __p += '<div class="select-ximutype">  <div class="ximutypt-tit">请选择细目表的类型：</div>  <div class="smart-set cfx">  ',
	_.each(res,
	function(t, a) {
		__p += '  <label class="radio ' + (null == (__t = ximutype == a ? "checked": "") ? "": __t) + ' ">  <i class="iconw-radio"></i>  <input type="radio" name="ximu_type" value="' + (null == (__t = a) ? "": __t) + '" ' + (null == (__t = ximutype == a ? "checked": "") ? "": __t) + ' style="display: none;">  <em>' + (null == (__t = t) ? "": __t) + "</em>  </label>  "
	}),
	__p += "  </div> </div>";
	return __p
},
JST["dialogs/setscore-one"] = function(obj) {
	obj || (obj = {});
	var __t, __p = "",
	__e = _.escape,
	__j = Array.prototype.join;
	function print() {
		__p += __j.call(arguments, "")
	}
	with(obj) {
		if (__p += '<div class="q-score-con" data-modal-title="设置分数">  <form action="javascript:;" id="dialog-score-form">  ', Number(model.get("question_type")) < 6) {
			if (__p += "  ", "4" == model.get("question_type")) {
				__p += "  ";
				var _NN = _.size(model.get("answer_json") || model.get("myanswer"));
				__p += '  <p><label for="">' + (null == (__t = qctypes[model.get("question_channel_type")]) ? "": __t) + '：</label><input type="text" name="score" value="' + (null == (__t = model.get("score").subScore || 1) ? "": __t) + '" data-n="' + (null == (__t = _NN) ? "": __t) + '"> 分 x ' + (null == (__t = _NN) ? "": __t) + "空</p>  "
			} else __p += '  <p><label for="">' + (null == (__t = qctypes[model.get("question_channel_type")]) ? "": __t) + '：</label><input type="text" value="' + (null == (__t = model.get("score").score) ? "": __t) + '" name="score"> 分</p>  ';
			__p += "  "
		} else {
			if (__p += "    <ul>  ", "7" == model.get("question_type") && (__p += "  ", model.collection.each(function(t, a) {
				if (__p += "  <li>  <label>（" + (null == (__t = Number(a) + 1) ? "": __t) + "）</label>  ", Number(t.get("question_type")) < 6) {
					if (__p += "  ", "4" == t.get("question_type")) {
						__p += "  ";
						var i = _.size(t.get("answer_json") || t.get("myanswer"));
						__p += '  <div><input type="text" name="score" value="' + (null == (__t = t.get("score").subScore || 1) ? "": __t) + '" data-n="' + (null == (__t = i) ? "": __t) + '"> 分 x ' + (null == (__t = i) ? "": __t) + "空</div>  "
					} else __p += '  <div><input type="text" value="' + (null == (__t = t.get("score").subScore || 0) ? "": __t) + '" name="score" /> 分</div>  ';
					__p += "  "
				}
				__p += "  ",
				"6" == t.get("question_type") && (__p += "  ", i = _.size(t.get("answer_json") || t.get("myanswer")), __p += '  <div><input type="text" name="score" value="' + (null == (__t = t.get("score").subScore || 1) ? "": __t) + '" data-n="' + (null == (__t = i) ? "": __t) + '"> 分 x ' + (null == (__t = i) ? "": __t) + "空</div>  "),
				__p += "  </li>  "
			}), __p += "  "), __p += "   ", "6" == model.get("question_type")) {
				__p += "  ";
				var _NN = _.size(model.get("answer_json") || model.get("myanswer"));
				__p += "  <li>  <div>  " + (null == (__t = qctypes[model.get("question_channel_type")]) ? "": __t) + '：  <input type="text" name="score" value="' + (null == (__t = model.get("score").subScore || 1) ? "": __t) + '" data-n="' + (null == (__t = _NN) ? "": __t) + '"> 分 x ' + (null == (__t = _NN) ? "": __t) + "空  </div>  </li>  "
			}
			__p += '   </ul>  <p>共计：<span class="s-total">0</span> 分</p>   '
		}
		__p += "  </form> </div>"
	}
	return __p
},
JST["dialogs/setscore-some"] = function(obj) {
	obj || (obj = {});
	var __t, __p = "",
	__e = _.escape,
	__j = Array.prototype.join;
	function print() {
		__p += __j.call(arguments, "")
	}
	with(obj) __p += '<div class="q-scorelist-con custom-modal" data-modal-title="根据题型批量设置分数：">  <ul>  ',
	_.each(data,
	function(t, i) {
		__p += "  ",
		"4" == i ? (__p += "  ", _.each(t,
		function(t, a) {
			__p += "  ",
			_NN = _.reduce(t,
			function(t, a) {
				return t + _.size(a.get("answer_json") || a.get("myanswer"))
			},
			0),
			__p += "  <li><em>" + (null == (__t = qctypes[a]) ? "": __t) + '：</em><input type="text" name="score" data-n="' + (null == (__t = _NN) ? "": __t) + '" value="0" data-ct="' + (null == (__t = [i, a].join(",")) ? "": __t) + '" /> 分 x ' + (null == (__t = _NN) ? "": __t) + "空</li>  "
		})) : -1 < _.indexOf(["6", "7"], i) ? (__p += "  ", _.each(t,
		function(t, a) {
			__p += "  <li><em>" + (null == (__t = qctypes[a]) ? "": __t) + '：</em><span class="words">该题型暂时不支持批量设置分数，请针对题单独设置分数！</span></li>  '
		})) : (__p += "  ", _.each(t,
		function(t, a) {
			__p += "  <li><em>" + (null == (__t = qctypes[a]) ? "": __t) + '：</em><input type="text" name="score" data-n="' + (null == (__t = t.length) ? "": __t) + '" value="0" data-ct="' + (null == (__t = [i, a].join(",")) ? "": __t) + '" /> 分 x ' + (null == (__t = t.length) ? "": __t) + "题</li>  "
		})),
		__p += "  ",
		__p += "  "
	}),
	__p += '  <li class="sum"><em>共计：</em><strong class="t-score">0</strong> 分</li>  </ul> </div>';
	return __p
},
JST["dialogs/sort-bytype"] = function(obj) {
	obj || (obj = {});
	var __t, __p = "",
	__e = _.escape,
	__j = Array.prototype.join;
	function print() {
		__p += __j.call(arguments, "")
	}
	with(obj) __p += '<div class="new-side-types custom-modal" data-modal-title="试题排序">  <form>  <div class="label">需要排序的大题</div>  <div class="custom-checbox-g f-cb">  ',
	models.each(function(t) {
		__p += '  <span class="custom-checkbox ' + __e(t.cid == cid ? "checked": "") + '" title="' + __e(t.get("_t").replace(/[。]+|<\/?[^>]*>/g, "")) + '">  <i class="iconw-checkbox"></i><input type="checkbox" name="type[]" value="' + __e(t.cid) + '" style="display:none" ' + __e(t.cid == cid ? "checked": "") + " >" + __e(t.get("_t").replace(/[。]+|<\/?[^>]*>/g, "")) + "  </span>  "
	}),
	__p += '  </div>  <div class="label">排序方式</div>  <div class="custom-radio-g">  <span class="checked custom-radio"><i class="iconw-radio"></i><input type="radio" name="orderby" value="1" style="display:none" checked>难度从低到高排序</span>  <span class="custom-radio"><i class="iconw-radio"></i><input type="radio" name="orderby" value="-1" style="display:none">难度从高到低排序</span>  </div>  </form> </div>';
	return __p
},
JST["dialogs/subject-download"] = function(obj) {
	obj || (obj = {});
	var __t, __p = "",
	__e = _.escape,
	__j = Array.prototype.join;
	function print() {
		__p += __j.call(arguments, "")
	}
	with(obj) __p += '<div>  <link rel="stylesheet" href="' + (null == (__t = CDN_LOCAL_DOMAIN) ? "": __t) + '/css/spriter-a.min.css?v=c8a2fa51d7">  <link rel="stylesheet" href="' + (null == (__t = CDN_LOCAL_DOMAIN) ? "": __t) + '/css/spriter-mix.min.css?v=c8a2fa51d7">  <style>   .form-paper-download { width: 500px; height: ' + (null == (__t = User.co_partner ? "500px": "660px") ? "": __t) + '; overflow-y: auto; }  .form-paper-download i { display: inline-block; }  .download-msg { padding-left: 0; padding-right: 0; }  .download-hint, .download-size, .download-type, .download-math, .download-beizu { padding-left: 10px; padding-right: 10px; padding-bottom: 13px; border-bottom: 0px; zoom: 1; }   .download-type-content .checkbox,  .download-type-con .radiobox { margin-right: 10px; }  </style>  <div class="form-paper-download">  <form class="P_download">   <input type="hidden" name="subject_id" value="' + (null == (__t = subject_id) ? "": __t) + '">   <div class=" download-msg">  <div class="download-size">  <div class="download-text">纸张大小：</div>  <div class="size-con download-bd J_radio_group">  <div class="size-a4 radiobox checked">  <span>  <i class="icona-radio"></i>  <input type="radio" value="A4" name="size" checked style="display: none;">  </span>  <i class="icona-a4"></i>  <p>A4</p>  </div>  <div class="size-a3 radiobox">  <span>  <i class="icona-radio"></i>  <input type="radio" value="A3" name="size" style="display: none;">  </span>  <i class="icona-a3"></i>  <p>A3（双栏）</p>  </div>  <div class="size-a4 radiobox">  <span>  <i class="icona-radio"></i>  <input type="radio" value="B5" name="size" style="display: none;">  </span>  <i class="icona-a4"></i>  <p>B5</p>  </div>  <div class="size-a3 radiobox">  <span>  <i class="icona-radio"></i>  <input type="radio" value="B4" name="size" style="display: none;">  </span>  <i class="icona-a3"></i>  <p>B4（双栏）</p>  </div>  </div>   </div>  <div class="download-type">  <div class="download-text">试卷内容：</div>  <div class="download-type-content download-bd J_content">  <span class="checkbox checked">  <i class="icona-check"></i>  <input type="checkbox" style="display:none" value="an" checked name="content_type[]">  答案  </span>  <span class="checkbox">  <i class="icona-check"></i>  <input type="checkbox" style="display:none" value="kw" name="content_type[]">  考点  </span>  <span class="checkbox">  <i class="icona-check"></i>  <input type="checkbox" style="display:none" value="ex" name="content_type[]">  解析  </span>   <span class="checkbox">  <i class="icona-check"></i>  <input type="checkbox" style="display:none" value="sc" name="content_type[]">  小题分  </span>   <span class="checkbox">  <i class="icona-check"></i>  <input type="checkbox" style="display:none" value="fx" name="content_type[]">  分析  </span>   </div>  </div>  </div>  <div class="download-math">  <div class="download-text">公式形式：</div>  <div class="download-type-con download-bd J_radio_group">  <span class="radiobox checked">  <i class="icona-radio"></i>  <input type="radio" value="2" name="renderMathAsImg" checked style="display: none;">  图片公式（不可编辑）  </span>  <span class="radiobox" style="display:block">  <i class="icona-radio"></i>  <input type="radio" value="1" name="renderMathAsImg" style="display: none;">  文本公式（可编辑）<b style="font-size:12px; color:#f00;">请使用Word2010及以上版本打开编辑</b>  </span>  </div>  </div>    <div class="download-type">  <div class="download-text">试卷类型：</div>  <div class="download-type-con download-bd J_radio_group">  <span class="radiobox">  <i class="icona-radio"></i>  <input type="radio" value="teacher" name="type" style="display: none;">  教师用卷（答案在题后）  </span>  <span class="radiobox checked">  <i class="icona-radio"></i>  <input type="radio" value="student" name="type" checked style="display: none;">  学生用卷（答案在卷尾）  </span>  </div>  </div>  <div class="download-hint">  ',
	User.co_partner ? __p += '  <div class="download-bd"><div class="recharge-btn-box"><button class="recharge-btn" type="submit">下 载</button></div></div>  ': (__p += '  <div class="download-bd">  ', isUnit && !limitStatus[3] && (__p += '  <div class="hint-con">  ', isOnDue ? (__p += "  ", limitStatus[0] ? (isEnd = !0, __p += '  <p>您为“组卷通”用户，此次下载<b class="highlight strong">免费</b></p>  <p class="small"> “组卷通” 到期时间：<b class="highlight">' + (null == (__t = moment(1e3 * productInfo.etime).format("YYYY-MM-DD")) ? "": __t) + "</b></p>  ") : (isEnd = !1, isUnitOutLimit = !0, __p += '  <p><b class="highlight">' + (null == (__t = limitStatus[1]) ? "": __t) + "</b></p>  ")) : (isEnd = !1, isUnitOutDue = !0), __p += "  ", __p += "  </div>  "), __p += "    ", isUnitOutLimit || (__p += "  ", !isEnd && PaperCount.isfree && (isEnd = !0, __p += '  <div class="hint-con">  <p>你下载过此专题，15天内下载<b class="highlight strong">免费</b></p>  </div>  '), __p += "    ", !isEnd && newvip.deadline ? (__p += '  <div class="hint-con">  ', newvip.coin >= paperNum ? (isEnd = !0, __p += '  <p>您为vip用户，此次下载<b class="highlight">免费</b></p>  <p class="small">剩余下载次数:<b class="highlight">' + (null == (__t = newvip.coin) ? "": __t) + "</b>, 到期时间:" + (null == (__t = moment(1e3 * newvip.deadline).format("YYYY-MM-DD")) ? "": __t) + "</p>  ") : isUnitOutDue || (isEnd = !1), __p += "  ", 0 == newvip.coin ? __p += '  <p><b class="highlight">非常抱歉，组卷VIP已经到期！</b><a href="/payment/vip" target="_blank">立即续费</a></p>  ': newvip.coin < paperNum && (__p += '  <p><b class="highlight">非常抱歉，组卷VIP权限的下载次数不足！</b><a href="/payment/vip" target="_blank">立即续费</a></p>  <p class="small">剩余试卷下载份数:<b class="highlight">' + (null == (__t = newvip.coin) ? "": __t) + "</b>,到期时间:" + (null == (__t = moment(1e3 * newvip.deadline).format("YYYY-MM-DD")) ? "": __t) + "</p>  "), __p += "  </div>  ") : !isEnd && isUnitOutDue && (__p += '  <div class="hint-con">  <p><b class="highlight">非常抱歉，“组卷通”已到期！</b></p>  </div>   '), __p += "     "), __p += "       ", isEnd && (__p += ' <div class="recharge-btn-box"><button class="recharge-btn" type="submit">下 载</button></div> '), __p += "    </div>  "),
	__p += "  </div>  </form>  ",
	User.co_partner || (__p += '  <div class="download-beizu">  <div class="download-text" style="padding-top:0;"> 温馨提示：</div>  <div class="download-bd">  <p class="small">1、VIP用户下载免费。 <a href="/payment/vip" target="_blank">开通VIP</a></p>  <p class="small">2、如有问题，请联系客服QQ：81321902 </p>  </div>  </div>  '),
	__p += "  </div>  </div>";
	return __p
},
JST["dialogs/update-notice-v3.3.1"] = function(obj) {
	obj || (obj = {});
	var __t, __p = "",
	__e = _.escape;
	with(obj) __p += '<div> <style>  .system-upgrade .system-upgrade-wall, .system-upgrade .pop-wrap { display: block; }  .system-upgrade-wall { position: fixed; top:0; right:0; left:0; bottom:0; background:#000; opacity: 0.3; filter:alpha(opacity=30); z-index: 10000; display: none; }  .pop-wrap { width: 600px; background-color: #fff; position: absolute; top: 60px; left: 50%; margin-left: -300px; z-index: 12000; font-size: 14px; display: none; }  .update span:first-child { margin-right: 30px; }  .pop-banner img { display: block; }  .pop-banner { position: relative; }  .produce { position: absolute; top: -54px; left: 87px; }  .pop-banner>span { cursor: pointer; display: block; width: 36px; height: 36px; position: absolute; background: url(/images/upgrade/close.png); right: -15px; top: -16px;}  .main-wrap { padding: 20px 24px; max-height: 350px; overflow: auto; }  .pop-icon { width: 4px; height: 16px; background-color: #52c684; float: left; margin-right: 10px; }  .pop-title>h1 { font-size: 16px; float: left; }  .pop-detail { clear: both; }  #J_NoticeModal .pop-content { margin-top: 20px; text-align: left; margin:0; }  .pop-detail li { line-height: 22px; margin-bottom: 5px; }  .pop-detail li a { color: #52c684; }  .pop-detail li a:hover { text-decoration:underline; }  .pop-detail { padding-top: 10px;}  .pop-title { overflow: hidden; margin-top: 15px; }  #J_NoticeModal .pop-content h1 { margin-bottom: 0; font-size: 16px; font-weight: bold; }  </style>  <div class="system-upgrade-wall"></div>  <div class="pop-wrap" id="J_NoticeModal">  <div class="pop-banner">  <img src="' + (null == (__t = CDN_LOCAL_DOMAIN) ? "": __t) + '/images/upgrade/pop-banner.png" alt="二一组卷v3.5更新公告">  <img src="' + (null == (__t = CDN_LOCAL_DOMAIN) ? "": __t) + '/images/upgrade/produce.png" alt="二一组卷v3.5更新公告" class="produce">  <span class="icon-close"></span>  </div>  <div class="main-wrap">  <div class="update">  <span>更新版本：V3.5</span>  <span>更新时间：2019年8月1日</span>  </div>  <div class="pop-content">  <div class="pop-title">  <div class="pop-icon"></div>  <h1>更新内容</h1>  </div>  <ul class="pop-detail">  <li>1、试题列表中新增“下载”功能，支持一键下载试题；</li>  <li>2、小额扫码支付新增“支付宝支付”方式，支持微信、支付宝扫码下载试卷；</li>  <li>3、智能组卷新增按“试题更新年份”进行筛选智能组卷；</li>  <li>4、试卷库模块下，对预览过的试卷做了优化处理，让您能快速查找出已预览使用过的试卷；</li>  <li>5、专题特供下，新增专题状态标识。让您能快速查找出已完结的完整专题；</li>  </ul>  </div>  \x3c!-- <div class="pop-content">  <div class="pop-title">  <div class="pop-icon"></div>  <h1>二、其他</h1>  </div>  <ul class="pop-detail">  <li>1、优化了网页与word的题号样式问题；</li>  <li>2、优化了下载下来的word，缺少阅卷人、分卷注释等信息的bug；</li>  <li>3、优化了系统不稳定，偶尔崩溃的现象；</li>  <li>4、优化了VIP购买机制，1个用户可购买多个学科的VIP。</li>  </ul>  </div> --\x3e  </div>  </div> </div>';
	return __p
},
JST["dialogs/update-notice"] = function(obj) {
	obj || (obj = {});
	var __t, __p = "",
	__e = _.escape;
	with(obj) __p += '<div> <style>  .system-upgrade .system-upgrade-wall, .system-upgrade .pop-wrap { display: block; }  .system-upgrade-wall { position: fixed; top:0; right:0; left:0; bottom:0; background:#000; opacity: 0.3; filter:alpha(opacity=30); z-index: 10000; display: none; }  .pop-wrap { width: 600px; background-color: #fff; position: absolute; top: 60px; left: 50%; margin-left: -300px; z-index: 12000; font-size: 14px; display: none; }  .update span:first-child { margin-right: 30px; }  .pop-banner img { display: block; }  .pop-banner { position: relative; }  .produce { position: absolute; top: -54px; left: 87px; }  .pop-banner>span { cursor: pointer; display: block; width: 36px; height: 36px; position: absolute; background: url(/images/upgrade/close.png); right: -15px; top: -16px;}  .main-wrap { padding: 20px 24px; max-height: 350px; overflow: auto; }  .pop-icon { width: 4px; height: 16px; background-color: #52c684; float: left; margin-right: 10px; }  .pop-title>h1 { font-size: 16px; float: left; }  .pop-detail { clear: both; }  #J_NoticeModal .pop-content { margin-top: 20px; text-align: left; margin:0; }  .pop-detail li { line-height: 22px; margin-bottom: 5px; }  .pop-detail li a { color: #52c684; }  .pop-detail li a:hover { text-decoration:underline; }  .pop-detail { padding-top: 10px;}  .pop-title { overflow: hidden; margin-top: 15px; }  #J_NoticeModal .pop-content h1 { margin-bottom: 0; font-size: 16px; font-weight: bold; }  </style>  <div class="system-upgrade-wall"></div>  <div class="pop-wrap" id="J_NoticeModal">  <div class="pop-banner">  <img src="' + (null == (__t = CDN_LOCAL_DOMAIN) ? "": __t) + '/images/upgrade/pop-banner.png" alt="二一组卷v3.0更新公告">  <img src="' + (null == (__t = CDN_LOCAL_DOMAIN) ? "": __t) + '/images/upgrade/produce.png" alt="二一组卷v3.0更新公告" class="produce">  <span class="icon-close"></span>  </div>  <div class="main-wrap">  <div class="update">  <span>更新版本：V3.2</span>  <span>更新时间：2018年10月9日</span>  </div>  <div class="pop-content">  <div class="pop-title">  <div class="pop-icon"></div>  <h1>更新内容</h1>  </div>  <ul class="pop-detail">  <li>1.在手动组卷下的章节同步选题中新增防超纲选题功能，筛选出来的试题更精准；</li>  <li>2.优化了智能组卷功能，新增支持为同一个题型同时设置不同的试题难度进行组卷，出卷方式更贴近老师的实际需求；</li>  <li>3.在使用智能组卷下的双向细目表组卷时，新增支持用户手动输入知识点关键字进行知识点的匹配绑定；</li>  <li>4.在下载试卷时的弹窗中新增文本公式可编辑的word版本提示，让用户拥有更好的使用体验；</li>  </ul>  </div>  \x3c!-- <div class="pop-content">  <div class="pop-title">  <div class="pop-icon"></div>  <h1>二、其他</h1>  </div>  <ul class="pop-detail">  <li>1、优化了网页与word的题号样式问题；</li>  <li>2、优化了下载下来的word，缺少阅卷人、分卷注释等信息的bug；</li>  <li>3、优化了系统不稳定，偶尔崩溃的现象；</li>  <li>4、优化了VIP购买机制，1个用户可购买多个学科的VIP。</li>  </ul>  </div> --\x3e  </div>  </div> </div>';
	return __p
},
JST["basket/basket-body"] = function(obj) {
	obj || (obj = {});
	var __t, __p = "",
	__e = _.escape,
	__j = Array.prototype.join;
	function print() {
		__p += __j.call(arguments, "")
	}
	with(obj) __p += '<div class="scorll">  ',
	0 == _.size(type_count) ? __p += '  <div class="basket-empty">您的试题篮还没有试题，马上添加试题吧！</div>  ': (__p += '  <div class="c-basket-hd"> 试题总量（<span class="c-num">' + (null == (__t = total) ? "": __t) + '</span>） </div>  <div class="c-basket-bd">  ', _.each(type_count,
	function(t) {
		__p += '  <div class="c-basket-line">  <div class="c-type">  <span class="c-type-tit fl" title="' + (null == (__t = t._t) ? "": __t) + '">' + (null == (__t = t._t) ? "": __t) + '</span>  <span class="c-type-sum fr"><em class="c-num">' + (null == (__t = t.count) ? "": __t) + '</em>题</span>  </div>  <a href="javascript:;" class="c-del J_del_type" data-name="' + (null == (__t = t._t) ? "": __t) + '"><i class="iconw-del2"></i></a>  </div>  '
	}), __p += '  <a href="javascript:;" class="c-clear J_emtpy_data">清空试题</a>  ', Number(pid) && user.isAdmin ? __p += '  <a href="/paper/edit/' + (null == (__t = pid || "") ? "": __t) + "?from=0&xd=" + (null == (__t = xd) ? "": __t) + "&chid=" + (null == (__t = chid) ? "": __t) + '" class="c-btn">编辑试卷</a>  <a href="javascript:;" class="c-btn J_cancel_data">取消编辑</a>  ': __p += '  <a href="javascript:;" class="c-btn J_redirect_to_edit">试卷预览</a>  ', __p += "  </div>  "),
	__p += " </div>";
	return __p
},
JST["basket/basket-handler"] = function(obj) {
	obj || (obj = {});
	var __t, __p = "",
	__e = _.escape;
	with(obj) __p += '<div class="c-basket-btn">  <div class="c-basket-mc">  <i class="iconw-box"></i>  <p>试题篮</p>  <span>' + (null == (__t = total) ? "": __t) + "</span>  </div> </div>";
	return __p
},
JST["papers/edit-grids"] = function(obj) {
	obj || (obj = {});
	var __t, __p = "",
	__e = _.escape,
	__j = Array.prototype.join;
	function print() {
		__p += __j.call(arguments, "")
	}
	with(obj) {
		__p += '<div class="club-summary f-cb">  <div class="t1">分数：<strong>' + (null == (__t = ques_score) ? "": __t) + '分</strong></div>  <div class="w"><span class="t2">题数：<strong>' + (null == (__t = ques_num) ? "": __t) + '</strong></span></div>  \x3c!-- <div class="t3">难度：<strong>' + (null == (__t = ques_difficulty) ? "": __t) + '</strong></div> --\x3e  <div class="t3">难度系数：<strong>' + (null == (__t = coefficient) ? "": __t) + "</strong></div> </div> ";
		var NN = 0;
		_.each(part_views,
		function(t, a) {
			__p += ' <div class="edit-handle-hd J_type_hd">  <span>' + (null == (__t = t.model.get("name")) ? "": __t) + '</span>  <div class="dash-line"></div> </div> <div class="edit-mc J_type_ques" data-cid="' + (null == (__t = t.model.cid) ? "": __t) + '">  ',
			_.each(type_group[t.cid],
			function(t, a) {
				__p += '  <div class="J_drag_type edit-mc-item" data-cid="' + (null == (__t = t.model.cid) ? "": __t) + '">  <div class="edit-handle-mt">  <strong title="' + (null == (__t = t.model.get("_t")) ? "": __t) + '"><span>' + (null == (__t = myUtils.chinesesn(NN++)) ? "": __t) + "、</span>" + (null == (__t = t.model.get("_t")) ? "": __t) + '</strong>  <div class="edit-act">  <a href="javascript:;" class="J_sortby_type J_dis_drag" data-cid="' + (null == (__t = t.model.cid) ? "": __t) + '">排序</a>  <a href="javascript:;" class="J_del_type J_dis_drag" data-cid="' + (null == (__t = t.model.cid) ? "": __t) + '">删除</a>  </div>  </div>  <div class="edit-handle-bd">  <ul class="item-num cfx">  ',
				_.each(ques_group[t.cid],
				function(t, a) {
					__p += '  <li class="J_drag_grid" data-cid="' + (null == (__t = t.model.cid) ? "": __t) + '"><span>' + (null == (__t = t.model.get("_n") + 1) ? "": __t) + "</span></li>  "
				}),
				__p += "  </ul>  </div>  </div>  "
			}),
			__p += " </div> "
		})
	}
	return __p
},
JST["papers/mark-table"] = function(obj) {
	obj || (obj = {});
	var __t, __p = "",
	__e = _.escape;
	with(obj) __p += "<table>  <tr><th>题号</th><th>" + (null == (__t = data.num.join("</th><th>")) ? "": __t) + "</th></tr>  <tr><th>评分</th><td>" + (null == (__t = data.blanks.join("</td><td>")) ? "": __t) + "</td></tr> </table>";
	return __p
},
JST["papers/paper-items"] = function(obj) {
	obj || (obj = {});
	var __t, __p = "",
	__e = _.escape,
	__j = Array.prototype.join;
	function print() {
		__p += __j.call(arguments, "")
	}
	with(obj) __p += '<div class="loading-wrap">  <div class="loading-bg"></div>  <div class="loading"></div> </div> ',
	_.size(list) ? (__p += " <ul>  ", _.each(list,
	function(t) {
		t.short_title = t.title.toString(),
		t.short_title = t.short_title.slice(0, 32) + (t.short_title.slice(32, 33) ? "...": ""),
		__p += '  <li>  <div class="item-wrap">  ',
		t.new_flag && (__p += '  <span class="icon-subject--new"></span>  '),
		__p += '  <div class="item-img">  <a href="' + (null == (__t = mURL("/paper/view/", t.pid)) ? "": __t) + '" target="_blank"><span class="icon iconf-' + (null == (__t = t.icon) ? "": __t) + '"></span></a>  </div>  <div class="w fl">  <div class="item-mc">  <h3 class="item-tit"><a href="' + (null == (__t = mURL("/paper/view/", t.pid)) ? "": __t) + '" target="_blank" title="' + (null == (__t = t.title) ? "": __t) + '" >' + (null == (__t = t.short_title) ? "": __t) + '</a></h3>  <div class="item-attr">  <span><i class="iconw-time"></i>修改时间：' + (null == (__t = myUtils.formatTimestamp(t.examine_time)) ? "": __t) + '</span>  <span><i class="iconw-eye1"></i>浏览次数：' + (null == (__t = t.look_num) ? "": __t) + '</span>  <span><i class="iconw-leixing"></i>类型：' + (null == (__t = t.typeName) ? "": __t) + '</span>  </div>  </div>  </div>  <div class="item-act">  <a class="download-btn" onclick="Application.popupPaperDownload(' + (null == (__t = t.pid) ? "": __t) + ')">下载</a>  <a class="fun-btn" onclick="Application.AnalyzeChart.show(' + (null == (__t = t.pid) ? "": __t) + ')"><span class="iconw-fenxi2"></span>试卷分析</a>  </div>  </div>  </li>  '
	}), __p += " </ul> ") : __p += ' <div class="empty-ffxi">  <img src="' + (null == (__t = CDN_LOCAL_DOMAIN) ? "": __t) + '/images/blank.png" >  <p>筛选无结果，去组个试卷试试吧<a href="/question?tree_type=knowledge" class="">【立即组卷】</a></p> </div> ';
	return __p
},
JST["papers/paper-part"] = function(obj) {
	obj || (obj = {});
	var __t, __p = "",
	__e = _.escape,
	__j = Array.prototype.join;
	function print() {
		__p += __j.call(arguments, "")
	}
	with(obj) null === data ? __p += ' <div class="paper-title" data-jset="6"></div> ': __p += ' <h2>  <span class="edit-text contenteditable-part" data-jedit="name">' + (null == (__t = data.name) ? "": __t) + '</span> </h2>  <p data-jset="8">  <span class="edit-text contenteditable-part" data-jedit="tip">' + (null == (__t = data.tip) ? "": __t) + "</span> </p> ";
	return __p
},
JST["papers/paper-style"] = function(obj) {
	obj || (obj = {});
	var __t, __p = "",
	__e = _.escape,
	__j = Array.prototype.join;
	function print() {
		__p += __j.call(arguments, "")
	}
	with(obj) __p += '<div class="edit-handle-mt cfx">  <strong>试卷结构调整</strong>  <div class="edit-act">  <div class="edit-sel-box J_selete_temp">  <a class="edit-sel-hd"><span>' + (null == (__t = templates[data.template].name) ? "": __t) + '</span><i class="iconw-filter-down"></i></a>  <ul class="edit-type">  ',
	_.each(templates,
	function(t, a) {
		__p += '  <li data-jtemp="' + (null == (__t = a) ? "": __t) + '">' + (null == (__t = t.name) ? "": __t) + "</li>  "
	}),
	__p += '  </ul>  </div>  </div> </div> <div class="edit-handle-bd">  <div class="edit-sel-tag cfx J_jsettings">  ',
	_.each(settings,
	function(t, a) {
		__p += '  <label style="' + (null == (__t = -1 < ",3,8,12,".indexOf("," + a + ",") ? "display:none": "") ? "": __t) + '" class=" ' + (null == (__t = 1 == data.style[a - 1] ? "checked": "") ? "": __t) + ' custom-checkbox" data-jsetcheck="' + (null == (__t = a) ? "": __t) + '">  <i class="iconw-checkbox"></i>  <span>' + (null == (__t = t) ? "": __t) + "</span>  </label>  "
	}),
	__p += "   </div> </div>";
	return __p
},
JST["papers/paper-type"] = function(obj) {
	obj || (obj = {});
	var __t, __p = "",
	__e = _.escape,
	__j = Array.prototype.join;
	function print() {
		__p += __j.call(arguments, "")
	}
	with(obj) null === data ? __p += ' <div class="paper-type" data-jset="10"></div> <ul></ul>  ': __p += ' \x3c!--答题评分区--\x3e <table data-jset="2" style="display:none">  <tr>  <th>阅卷人</th>  <td></td>  </tr>  <tr>  <th>得分</th>  <td></td>  </tr> </table> <h3>  <span class="order">' + (null == (__t = myUtils.chinesesn(data._n)) ? "": __t) + '</span>、  <span class="edit-text contenteditable-type" data-jedit="_t">' + (null == (__t = data.short_tit) ? "": __t) + '</span>  <span data-jset="12">(共<b class="t-num">' + (null == (__t = data.type_count.count) ? "": __t) + '</b>题；共<b class="t-score">' + (null == (__t = data.type_count.score) ? "": __t) + '</b>分)</span> </h3> <div class="paper-fun-list cfx">  <a href="javascript:;" class="paper-fun-item J_score_ques">  <i class="iconw-fenshu"></i>批量设定得分  </a>  <a href="javascript:;" class="paper-fun-item J_sort_ques">  <i class="iconw-sort"></i>排序  </a>  <a href="javascript:;" class="paper-fun-item J_del_ques">  <i class="iconw-del"></i>删除  </a> </div> ';
	return __p
},
JST["manualpage/filter-box"] = function(obj) {
	obj || (obj = {});
	var __t, __p = "",
	__e = _.escape,
	__j = Array.prototype.join;
	function print() {
		__p += __j.call(arguments, "")
	}
	with(obj) __p += '<span class="mt">  ' + (null == (__t = title) ? "": __t) + '： </span> <div class="w fl">  <div class="mc hide-mc">  <ul class="filter-item-wrap cfx ">  ',
	_.each(list,
	function(t) {
		__p += '  <li><a class="' + (null == (__t = t.value == selected ? "active": "") ? "": __t) + '" data-param="' + (null == (__t = [t.name, t.value].join("=")) ? "": __t) + '">' + (null == (__t = t.text) ? "": __t) + "</a></li>   "
	}),
	__p += '   </ul>  <div class="filter-more">   <span><i class="iconw-more-down-tiggle"></i>更多</span>  </div>  </div> </div>';
	return __p
},
JST["manualpage/filter-drop"] = function(obj) {
	obj || (obj = {});
	var __t, __p = "",
	__e = _.escape,
	__j = Array.prototype.join;
	function print() {
		__p += __j.call(arguments, "")
	}
	with(obj) __p += '<dd>  <a class="filter-sel-hd"><span class="J_filter_tit">' + (null == (__t = title) ? "": __t) + '</span><i class="iconw-filter-down"></i></a>  <ul class="' + (null == (__t = "short" == style ? "filter-type": "filter-item-wrap cfx") ? "": __t) + '">  ',
	_.each(list,
	function(t) {
		__p += '  <li><a class="' + (null == (__t = t.value == selected ? "active": "") ? "": __t) + '" data-param="' + (null == (__t = [t.name, t.value].join("=")) ? "": __t) + '">' + (null == (__t = t.text) ? "": __t) + "</a></li>  "
	}),
	__p += "  </ul> </dd>";
	return __p
},
JST["manualpage/manual-tree-mt"] = function(obj) {
	obj || (obj = {});
	var __t, __p = "",
	__e = _.escape,
	__j = Array.prototype.join;
	function print() {
		__p += __j.call(arguments, "")
	}
	with(obj) parital ? (__p += "  ", _.each(grades,
	function(t) {
		__p += '  <li class="' + (null == (__t = cur_grade && t.id == cur_grade.id ? "selected": "") ? "": __t) + '"   data-val="' + (null == (__t = t.id) ? "": __t) + '"   data-selected="' + (null == (__t = cur_grade && t.id == cur_grade.id ? "selected": "") ? "": __t) + '" >  <a href="javascript:;">' + (null == (__t = t.title) ? "": __t) + "</a>  </li>  "
	}), __p += " ") : (__p += ' <div class="mt-hd clearfix">  <div class="fl mt-tit" title="' + (null == (__t = cur_version.title) ? "": __t) + (null == (__t = cur_grade.title) ? "": __t) + '">  <span>' + (null == (__t = cur_version.title) ? "": __t) + "</span>  <em>·</em>  <span>" + (null == (__t = cur_grade.title) ? "": __t) + '</span>  </div>  <i class="iconw-nav-down"></i> </div> <div class="mt-bd" id="J_TreeVersionForm">  <form action="" class="version-filter-form">  <div class="ff clearfix">  <label>版本：</label>  <div class="ff-filter-box">  <ul class="J_version">  ', _.each(versions,
	function(t) {
		__p += '  <li class="' + (null == (__t = cur_version && t.id == cur_version.id ? "selected": "") ? "": __t) + '"   data-val="' + (null == (__t = t.id) ? "": __t) + '"   data-selected="' + (null == (__t = cur_version && t.id == cur_version.id ? "selected": "") ? "": __t) + '" >  <a href="javascript:;">' + (null == (__t = t.title) ? "": __t) + "</a>  </li>  "
	}), __p += '  </ul>  </div>  </div>  <div class="ff clearfix">  <label>年级：</label>  <div class="ff-filter-box">  <ul class="J_grade">  ', _.each(grades,
	function(t) {
		__p += '  <li class="' + (null == (__t = cur_grade && t.id == cur_grade.id ? "selected": "") ? "": __t) + '"   data-val="' + (null == (__t = t.id) ? "": __t) + '"   data-selected="' + (null == (__t = cur_grade && t.id == cur_grade.id ? "selected": "") ? "": __t) + '" >  <a href="javascript:;">' + (null == (__t = t.title) ? "": __t) + "</a>  </li>  "
	}), __p += "  </ul>  </div>  </div>  </form> </div> ");
	return __p
},
JST["manualpage/manual-tree-mt2"] = function(obj) {
	obj || (obj = {});
	var __t, __p = "",
	__e = _.escape,
	__j = Array.prototype.join;
	function print() {
		__p += __j.call(arguments, "")
	}
	with(obj) __p += '<div class="mt-hd clearfix">  <div class="fl mt-tit" title="' + (null == (__t = cur_version.title) ? "": __t) + (null == (__t = cur_grade.title) ? "": __t) + '">  <span>' + (null == (__t = cur_version.title) ? "": __t) + "</span>  <em>·</em>  <span>" + (null == (__t = cur_grade.title) ? "": __t) + '</span>  </div>  <i class="iconw-nav-down"></i> </div> <div class="mt-bd" id="J_TreeVersionForm">  <h3>教材选择</h3>  <form action="">  <div class="ff clearfix">  <label>版本：</label>  <select name="chid" class="J_version">  ',
	_.each(versions,
	function(t) {
		__p += '  <option value="' + (null == (__t = t.id) ? "": __t) + '" ' + (null == (__t = t.id == sel_version.id ? "selected": "") ? "": __t) + " >" + (null == (__t = t.title) ? "": __t) + "</option>  "
	}),
	__p += '  </select>  </div>  <div class="ff clearfix">  <label>年级：</label>  <select name="bookversionid" class="J_grade">  \x3c!-- <option value="">请选择年级</option> --\x3e  ',
	_.each(grades,
	function(t) {
		__p += '  <option value="' + (null == (__t = t.id) ? "": __t) + '" ' + (null == (__t = t.id == sel_grade.id ? "selected": "") ? "": __t) + " >" + (null == (__t = t.title) ? "": __t) + "</option>  "
	}),
	__p += '   </select>  </div>  <button type="submit">确定</button>  </form> </div>';
	return __p
},
JST["payment/active-dialog.201809"] = function(obj) {
	obj || (obj = {});
	var __t, __p = "",
	__e = _.escape;
	with(obj) __p += '<link href="' + (null == (__t = CDN_LOCAL_DOMAIN) ? "": __t) + '/s/css/active.min.css" rel="stylesheet"> <div class="pop-mask"></div> <div class="active-pop a-bounceinT">  <a href="javascript:;" class="pop-close">  <img src="' + (null == (__t = CDN_LOCAL_DOMAIN) ? "": __t) + '/s/images/active201809/pop-close.png">  </a>  <a href="/payment/advertise" class="pop-link">  <img src="' + (null == (__t = CDN_LOCAL_DOMAIN) ? "": __t) + '/s/images/active201809/pop-btn.png">  </a> </div>';
	return __p
},
JST["payment/active-dialog"] = function(obj) {
	obj || (obj = {});
	var __t, __p = "",
	__e = _.escape;
	with(obj) __p += '<link href="' + (null == (__t = CDN_LOCAL_DOMAIN) ? "": __t) + '/s/css/active.min.css" rel="stylesheet"> <div class="pop-mask"></div> <div class="active-pop a-bounceinT">  <a href="javascript:;" class="pop-close">  <img src="' + (null == (__t = CDN_LOCAL_DOMAIN) ? "": __t) + '/s/images/active201902/act-pop-close.png">  </a>  <div class="act-pop-bd">  <img src="' + (null == (__t = CDN_LOCAL_DOMAIN) ? "": __t) + '/s/images/active201902/act-pop.png">  </div>  <a href="/payment/advertise" class="pop-link">  <img src="' + (null == (__t = CDN_LOCAL_DOMAIN) ? "": __t) + '/s/images/active201902/act-pop-btn.png">  </a> </div>';
	return __p
},
JST["report/dialog-know-master"] = function(obj) {
	obj || (obj = {});
	var __t, __p = "",
	__e = _.escape,
	__j = Array.prototype.join;
	function print() {
		__p += __j.call(arguments, "")
	}
	with(obj) __p += '<div class="progress-wrap">  ',
	_.each(data,
	function(t) {
		__p += '  <div class="bar-item">  <p class="bar-tit">' + (null == (__t = t.name ? t.name.name: "--") ? "": __t) + '</p>  <div class="bar-bd">  <div class="bar-bg"><div class="bar" style="width:' + (null == (__t = 100 - 100 * t.err_rate) ? "": __t) + '%"></div></div>  <span class="bar-pp">' + (null == (__t = 100 - 100 * t.err_rate) ? "": __t) + "%</span>  </div>  </div>  "
	}),
	__p += " </div>";
	return __p
},
JST["report/head-title"] = function(obj) {
	obj || (obj = {});
	var __t, __p = "",
	__e = _.escape;
	with(obj) __p += '<div class="do-q-mt">  <strong class="do-q-tit">' + (null == (__t = myUtils.chinesesn(data._n)) ? "": __t) + "、" + (null == (__t = data.head_title) ? "": __t) + '<span class="q-score">(共' + (null == (__t = data.count) ? "": __t) + "题；共" + (null == (__t = data.score) ? "": __t) + '分)</span></strong>  </div>  <div class="do-q-mc"><ul class="J_ques_items"></ul></div> </div>';
	return __p
},
JST["report/report-circle"] = function(obj) {
	obj || (obj = {});
	var __t, __p = "",
	__e = _.escape;
	with(obj) __p += '\x3c!--环形进度条 ie8 ie7 全挂orz--\x3e  \x3c!--作答成绩--\x3e <div class="c-circle">  <div class="circle-wrap">  <div class="circle">  \x3c!--左半边圆--\x3e  <div class="circle-left">  <div class="clip_left"></div>  </div>  \x3c!--右半边圆--\x3e  <div class="circle-right">  <div class="clip_right"></div>  </div>  <div class="mask">  <div class="mask-con">  <span class="per">' + (null == (__t = data.score) ? "": __t) + "</span>分   </div>   </div>  </div>  </div>  <h3>作答成绩</h3>  <p>（平均分：" + (null == (__t = Math.floor(data.scoreRank.total_score / data.scoreRank.total)) ? "": __t) + '分）</p> </div>  \x3c!--排名--\x3e <div class="c-circle c2">  <div class="circle-wrap">  <div class="circle">  \x3c!--左半边圆--\x3e  <div class="circle-left">  <div class="clip_left"></div>  </div>  \x3c!--右半边圆--\x3e  <div class="circle-right">  <div class="clip_right"></div>  </div>  <div class="mask">  <div class="mask-con">  第' + (null == (__t = Number(data.scoreRank.myrank) + 1) ? "": __t) + '名   <span class="per" style="display: none">100</span>  </div>   </div>  </div>  </div>  <h3>排名</h3>  <p>（总共' + (null == (__t = data.scoreRank.total) ? "": __t) + '人作答）</p> </div>  \x3c!--作答时长--\x3e <div class="c-circle c3">  <div class="circle-wrap">  <div class="circle">  \x3c!--左半边圆--\x3e  <div class="circle-left">  <div class="clip_left"></div>  </div>  \x3c!--右半边圆--\x3e  <div class="circle-right">  <div class="clip_right"></div>  </div>  <div class="mask">  <div class="mask-con">  ' + (null == (__t = Math.floor(data.use_time / 60)) ? "": __t) + "'" + (null == (__t = data.use_time % 60) ? "": __t) + '"  <span class="per" style="display: none">100</span>   </div>   </div>  </div>  </div>  <h3>作答时长</h3>  <p>平均时长' + (null == (__t = data.avgmin) ? "": __t) + "'" + (null == (__t = data.avgsec) ? "": __t) + '"</p> </div>';
	return __p
},
JST["partial/function-line"] = function(obj) {
	obj || (obj = {});
	var __t, __p = "",
	__e = _.escape,
	__j = Array.prototype.join;
	function print() {
		__p += __j.call(arguments, "")
	}
	with(obj) __p += '<div class="c-fun-bd">  <div class="c-fun-box">  <div class="basket__handler"></div>  ',
	user.co_partner || (__p += '  <div class="c-fun-blcok">  <div class="c-fun-item">  <a href="javascript:;" onclick="window.open(\'http://wpa.b.qq.com/cgi/wpa.php?ln=1&key=XzkzODE4MjQ4OF80NjM1NzhfNDAwNjM3OTk5MV8yXw&uin=\', \'_blank\', \'height=544, width=644,toolbar=no,scrollbars=no,menubar=no,status=no\')" class="jBizQQWPA">  <i class="iconw-kf"></i>  </a>  <div class="c-fun-tip" onclick="window.open(\'http://wpa.b.qq.com/cgi/wpa.php?ln=1&key=XzkzODE4MjQ4OF80NjM1NzhfNDAwNjM3OTk5MV8yXw&uin=\', \'_blank\', \'height=544, width=644,toolbar=no,scrollbars=no,menubar=no,status=no\')">  <b class="iconw-tri-r"></b>  QQ客服  </div>  </div>  <div class="c-fun-item">  <a href="javascript:;">  <i class="iconw-gn"></i>  </a>  <div class="c-fun-tip c-ewm">  <b class="iconw-tri-r"></b>  <div class="c-ewm-item">  <img src="/build/images/ewm1.png">  <p>二一教育</p>  </div>  <div class="c-ewm-item">  <img src="/build/images/ewm2.png">  <p>二一组卷官方交流群1<br>(142401456)</p>  </div>  </div>  </div>  <div class="c-fun-item">  <a href="/help/feedback">  <i class="iconw-fk"></i>  </a>  <div class="c-fun-tip">  <b class="iconw-tri-r"></b>  意见反馈  </div>  </div>  <div class="c-fun-item">  <a href="javascript:;" class="J_gotop">  <i class="iconw-top"></i>  </a>  <div class="c-fun-tip">  <b class="iconw-tri-r"></b>  返回顶部  </div>  </div>  </div>  '),
	__p += '  </div>  </div> <div class="c-basket basket__body"></div>';
	return __p
},
JST["partial/list-loading"] = function(obj) {
	obj || (obj = {});
	var __t, __p = "",
	__e = _.escape;
	with(obj) __p += '<div class="loading-wrap">  <div class="loading-bg"></div>  <div class="loading"></div> </div>';
	return __p
},
JST["partial/login"] = function(obj) {
	obj || (obj = {});
	var __t, __p = "",
	__e = _.escape,
	__j = Array.prototype.join;
	function print() {
		__p += __j.call(arguments, "")
	}
	with(obj) __p += '<link rel="stylesheet" href="' + (null == (__t = CDN_LOCAL_DOMAIN) ? "": __t) + '/css/spriter-a.min.css?v=c8a2fa51d7"> <link rel="stylesheet" href="' + (null == (__t = CDN_LOCAL_DOMAIN) ? "": __t) + '/css/spriter-mix.min.css?v=c8a2fa51d7"> <link rel="stylesheet" href="' + (null == (__t = CDN_LOCAL_DOMAIN) ? "": __t) + '/css/reg.min.css?v=c8a2fa51d7"> <style>  .reg-form { z-index: 11100; left: 50%; margin-left: -180px; top: 0; }  .reg-form i { display: inline-block; vertical-align: middle; }  .reg-mask { position: fixed; left: 0; top: 0; bottom: 0; right: 0; background: #000; opacity: 0.5; filter: alpha(opacity=50); z-index: 10000; }  .reg-form .btn-close { position: absolute; right: 16px; top: 16px; display: block; text-indent: -9999px; width: 24px; height: 24px; background: url(/images/close_24.png) no-repeat center center; }  .reg-form .btn-close:hover { opacity: 0.8; } </style> <div class="reg-mask"></div> <div class="reg-form" style="top: 182px;">  <ul>  <li> <a href="javascript:;" class="reg-active">登录</a> </li>  </ul>  <a class="btn-close J_CloseForm">x</a>  <form id="J_LoginForm" class="reg-form-detail" action="/login" method="post">  <input type="hidden" name="_csrf" value="' + (null == (__t = csrf._csrf) ? "": __t) + '">  <div class="reg-form-input">  <label for="account" class="placeholder">请输入网站账号/手机号码/邮箱</label>  <input type="text" name="LoginForm[username]" class="validate" id="account" placeholder="请输入网站账号/手机号码/邮箱">  <div class="fm-warn"> <p>账号不能为空！</p> <i></i> </div>   </div>  <div class="reg-form-input">  <label for="password" class="placeholder">请输入密码</label>  <input type="password" name="LoginForm[password]" class="validate" id="password" placeholder="请输入密码">  <div class="fm-warn"> <p>密码不能为空！</p> <i></i> </div>   </div>  <div class="login-line">  <div class="login-auto">  <span class="checkbox checked f-usn" onselectstart="return false">  <i class="icona-check"></i>  <input type="checkbox" checked="" value="1" class="f-dn" name="LoginForm[rememberMe]">自动登录</span>  </div>  <div class="login-pwd">  <a href="http://passport.21cnjy.com/site/password-find?jump_url=http://zujuan.21cnjy.com/paper/new-index?tree_type=exam"  target="_blank">忘记密码</a>  </div>  </div>  <div class="reg-btn">  <button type="submit">登录</button>  </div>  </form>  ',
	co_partner || (__p += '  <div class="login-others">  <div class="login-others-method">其它登录方式：  <a href="http://passport.21cnjy.com/site/show-qr-code?jump_url=http://zujuan.21cnjy.com">  <i class="icona-wxloginbtn"> </i>  </a>  <a href="http://21cnjy.com/qqconnect?jump_url=http://zujuan.21cnjy.com">  <i class="icona-qqloginbtn"> </i>  </a>  </div>  <div class="login-reg">  <a target="_blank" href="http://passport.21cnjy.com/site/register?jump_url=http://zujuan.21cnjy.com">免费注册  <i class="icona-right-arrow"></i>  </a>  </div>   </div>  '),
	__p += " </div>";
	return __p
},
JST["partial/not-allowed"] = function(obj) {
	obj || (obj = {});
	var __t, __p = "",
	__e = _.escape;
	with(obj) __p += '<div class="bridge-bd" style="padding-top: 44px;">  <h2 class="bridge-title"> (#error) 页面出错。</h2>   <h2 class="bridge-title">sorry！ 系统出错了，码农正在抢修中！</h2>  <div> 请稍候再试，或<a href="/">【返回首页】</a> </div> </div>';
	return __p
},
JST["partial/not-found"] = function(obj) {
	obj || (obj = {});
	var __t, __p = "",
	__e = _.escape;
	with(obj) __p += '<div class="bridge-bd" style="padding-top: 44px;">  <h2 class="bridge-title"> (#404) 页面未找到。</h2>   <h2 class="bridge-title">sorry！ 系统出错了，码农正在抢修中！</h2>  <div> 请稍候再试，或<a href="/">【返回首页】</a> </div> </div>';
	return __p
},
JST["partial/paper-undefind"] = function(obj) {
	obj || (obj = {});
	var __t, __p = "",
	__e = _.escape,
	__j = Array.prototype.join;
	function print() {
		__p += __j.call(arguments, "")
	}
	with(obj) __p += '<div class="undefind-data">  <img src="' + (null == (__t = CDN_LOCAL_DOMAIN) ? "": __t) + '/images/blank.png" class="undefind-img">  <div class="undefind-tit">筛选无结果，去组个试卷试试吧</div>  <div class="back-line">  <a href="/" class="gohome"><span>←</span>返回首页</a>  ',
	"categories" == goto ? __p += '  <a href="/question" class="other">【立即组卷】</a>  ': __p += '  <a href="/question?tree_type=knowledge" class="other">【立即组卷】</a>  ',
	__p += "  </div> </div>";
	return __p
},
JST["partial/undefind-know"] = function(obj) {
	obj || (obj = {});
	var __t, __p = "",
	__e = _.escape,
	__j = Array.prototype.join;
	function print() {
		__p += __j.call(arguments, "")
	}
	with(obj) __p += '<div class="undefind-data">  <img src="' + (null == (__t = CDN_LOCAL_DOMAIN) ? "": __t) + '/images/blank.png" class="undefind-img">  <div class="undefind-tit">当前学科下暂不支持' + (null == (__t = text) ? "": __t) + "</div>  ",
	"知识点选题" == text && (__p += '  <div class="back-line">  <a href="/" class="gohome"><span>←</span>返回首页</a>  <a href="/question" class="other">章节同步选题<span>→</span></a>  </div>  '),
	__p += " </div>";
	return __p
},
JST["partial/undefind"] = function(obj) {
	obj || (obj = {});
	var __t, __p = "",
	__e = _.escape,
	__j = Array.prototype.join;
	function print() {
		__p += __j.call(arguments, "")
	}
	with(obj) __p += '<div class="undefind-data">  <img src="' + (null == (__t = CDN_LOCAL_DOMAIN) ? "": __t) + '/images/blank.png" class="undefind-img">  <div class="undefind-tit">当前学科下暂不支持' + (null == (__t = text) ? "": __t) + "</div>  ",
	"章节同步选题" == text && (__p += '  <div class="back-line">  <a href="/" class="gohome"><span>←</span>返回首页</a>  <a href="/question?tree_type=knowledge" class="other">知识点选题<span>→</span></a>  </div>  '),
	__p += " </div>";
	return __p
},
JST["question/analyze"] = function(obj) {
	obj || (obj = {});
	var __t, __p = "",
	__e = _.escape,
	__j = Array.prototype.join;
	function print() {
		__p += __j.call(arguments, "")
	}
	with(obj) data.current_user.uid ? (__p += "  ", 0 == data.parent_id ? (__p += '  <div class="q-analyize">  ', data.knowledge && (__p += '  <div class="q-analyize-item J_ana_knw cfx">  <strong class="q-analyize-mt">【考点】</strong>  <div class="q-analyize-mc"><img _src="' + (null == (__t = String(data.knowledge).replace(/http(s)?:/gi, "")) ? "": __t) + '"></div>  </div>  '), __p += "  ", 7 != data.question_type && (__p += '  <div class="q-analyize-item J_ana_ans cfx">  <strong class="q-analyize-mt">【答案】</strong>  <div class="q-analyize-mc"><img _src="' + (null == (__t = String(data.answer).replace(/http(s)?:/gi, "")) ? "": __t) + '" ></div>  </div>  '), __p += "  ", data.explanation.toString().length && (__p += '  <div class="q-analyize-item J_ana_exp cfx">  <strong class="q-analyize-mt">【解析】</strong>  <div class="q-analyize-mc"><img _src="' + (null == (__t = String(data.explanation).replace(/http(s)?:/gi, "")) ? "": __t) + '"></div>  </div>  '), __p += "  </div>  ") : __p += '  <div class="q-analyize">  <div class="q-analyize-item J_ana_ans cfx">  <strong class="q-analyize-mt">【答案】</strong>  <div class="q-analyize-mc"><img _src="' + (null == (__t = String(data.answer).replace(/http(s)?:/gi, "")) ? "": __t) + '" ></div>  </div>  </div>  ') : (__p += "  ", 0 == data.parent_id && (__p += '  <div class="q-analyize">  <div class="q-nologin-tips">抱歉，您未登录！暂时无法查看答案与解析，<a href="javascript:;" onclick="Application.popupLogin() ">点击登录</a></div>  </div>  ')),
	__p += " ";
	return __p
},
JST["question/btn-handler"] = function(obj) {
	obj || (obj = {});
	var __t, __p = "",
	__e = _.escape,
	__j = Array.prototype.join;
	function print() {
		__p += __j.call(arguments, "")
	}
	with(obj) __p += '<div class="paper-fun-list cfx J_acts">  ',
	data.current_user.isSuperAdmin && (__p += '  <a href="//zbadmin.21cnjy.com/examQuestions/setExam?id=' + (null == (__t = data.question_id) ? "": __t) + "&type=1&url=https%2F%2Fwww.21cnjy.com%2Fquestion%2Fdetail%2F" + (null == (__t = data.question_id) ? "": __t) + '" class="paper-fun-item J_edit_it" target="_blank"><i class="iconw-edit2"></i>编辑</a>  '),
	__p += '  <a href="' + (null == (__t = mURL("/question/detail/", data.question_id)) ? "": __t) + '" target="_blank" class="paper-fun-item">  <i class="iconw-jiexi"></i>答案解析  </a>  <a href="javascript:;" class="paper-fun-item J_set_score">  <i class="iconw-fenshu"></i>设定得分  </a>  <a href="javascript:;" class="paper-fun-item J_reload">  <i class="iconw-exchange"></i>换题  </a>  <a href="javascript:;" class="paper-fun-item J_migrate">  <i class="iconw-zhuanyi"></i>转移  </a>  ',
	data.is_collect ? __p += '  <a href="javascript:;" class="paper-fun-item J_collect">  <i class="iconw-ucollect"></i>取消收藏  </a>  ': __p += '  <a href="javascript:;" class="paper-fun-item J_collect">  <i class="iconw-collect"></i>收藏  </a>  ',
	__p += '  <a href="javascript:;" onclick="Application.popupErrorReport(' + (null == (__t = data.question_id) ? "": __t) + ')" class="paper-fun-item J_correct">  <i class="iconw-error"></i>' + (null == (__t = HtmText.report) ? "": __t) + '  </a>  <a href="javascript:;" class="paper-fun-item J_remove">  <i class="iconw-del"></i>删除  </a> </div>';
	return __p
},
JST["question/btn-handler2"] = function(obj) {
	obj || (obj = {});
	var __t, __p = "",
	__e = _.escape,
	__j = Array.prototype.join;
	function print() {
		__p += __j.call(arguments, "")
	}
	with(obj) __p += '<div class="paper-fun-list cfx J_acts">  ',
	data.current_user.isSuperAdmin && (__p += '  <a href="//zbadmin.21cnjy.com/examQuestions/setExam?id=' + (null == (__t = data.question_id) ? "": __t) + "&type=1&url=https%2F%2Fwww.21cnjy.com%2Fquestion%2Fdetail%2F" + (null == (__t = data.question_id) ? "": __t) + '" class="paper-fun-item J_edit_it" target="_blank"><i class="iconw-edit2"></i>编辑</a>  '),
	__p += '  <a href="' + (null == (__t = mURL("/question/detail/", data.question_id)) ? "": __t) + '" target="_blank" class="paper-fun-item">  <i class="iconw-jiexi"></i>答案解析  </a>   ',
	data.is_collect ? __p += '  <a href="javascript:;" class="paper-fun-item J_collect">  <i class="iconw-ucollect"></i>取消收藏  </a>  ': __p += '  <a href="javascript:;" class="paper-fun-item J_collect">  <i class="iconw-collect"></i>收藏  </a>  ',
	__p += '  <a href="javascript:;" onclick="Application.popupErrorReport(' + (null == (__t = data.question_id) ? "": __t) + ')" class="paper-fun-item J_correct">  <i class="iconw-error"></i>' + (null == (__t = HtmText.report) ? "": __t) + "  </a>  ",
	data.exists_in_basket ? __p += '  <a href="javascript:;" class="paper-fun-item J_add_it ">  - 移除  </a>  ': __p += '  <a href="javascript:;" class="paper-fun-item J_add_it ">  + 选题  </a>  ',
	__p += " </div>";
	return __p
},
JST["question/login-btn"] = function(obj) {
	obj || (obj = {});
	var __t, __p = "",
	__e = _.escape;
	with(obj) __p += '<div class="q-login">  <P class="q-login-txt">抱歉，您未登录！暂时无法查看答案与解析！</P>  <a class="q-login-btn">登录查看答案解析<div class="qline"></div></a> </div>';
	return __p
},
JST["question/options-answer"] = function(obj) {
	obj || (obj = {});
	var __t, __p = "",
	__e = _.escape,
	__j = Array.prototype.join;
	function print() {
		__p += __j.call(arguments, "")
	}
	with(obj) - 1 < "123".indexOf(data.question_type) && (__p += ' <div class="q-res J_answer_input">  <ol class="op-items ' + (null == (__t = 3 == data.question_type ? "op-items-xv": "") ? "": __t) + ' ">  ', _.each(data.options,
	function(t, a) {
		__p += '  <li class="op-item">  ',
		2 == data.question_type ? __p += '  <span class="checkbox J_inputbox ' + (null == (__t = data.myanswer && _.contains(data.myanswer, a) ? "checked": "") ? "": __t) + ' ">  <span class="op-item-nut">  <i class="iconw-checkbox"></i>  <input type="checkbox" name="" value="' + (null == (__t = a) ? "": __t) + '" ' + (null == (__t = data.myanswer && _.contains(data.myanswer, a) ? "checked": "") ? "": __t) + ' style="display:none" />' + (null == (__t = a) ? "": __t) + ' .   </span>  <span class="op-item-meat">' + (null == (__t = String(t).replace(/http(s)?:/gi, "")) ? "": __t) + "</span>  </span>  ": (__p += '  <span class="radiobox J_inputbox ', data.myanswer == a && (__p += "checked"), __p += '">  <span class="op-item-nut">  <i class="iconw-radio"></i>  <input type="radio" name="" value="' + (null == (__t = a) ? "": __t) + '" ' + (null == (__t = self.myanswer == a ? "checked": "") ? "": __t) + ' style="display:none" />' + (null == (__t = 3 != data.question_type ? a + ".": "") ? "": __t) + '  </span>  <span class="op-item-meat">' + (null == (__t = String(t).replace(/http(s)?:/gi, "")) ? "": __t) + "</span>  </span>  "),
		__p += "  </li>  "
	}), __p += "  </ol> </div> "),
	__p += "   ",
	4 == data.question_type && (__p += ' <div class="q-res J_answer_input">  ', _.each(data.answer_json,
	function(t, a) {
		__p += '  <div class="line-field">  <span>【第' + (null == (__t = a + 1) ? "": __t) + '空】</span>  <div class="edit-wrap">  <div contenteditable="true" data-idx="' + (null == (__t = a + 1) ? "": __t) + '" class="fill-edit edit-line ' + (null == (__t = data.myanswer && data.myanswer[a + 1] ? "done-textarea": "") ? "": __t) + '" >' + (null == (__t = data.myanswer && data.myanswer[a + 1] ? data.myanswer[a + 1] : "") ? "": __t) + "</div>  </div>  </div>\t  "
	}), __p += " </div> "),
	__p += "   ",
	5 == data.question_type && (__p += ' <div class="q-res J_answer_input">  <div class="edit-wrap2">  <div contenteditable="true" class="fill-edit txt-field edit-line ' + (null == (__t = data.myanswer ? "done-textarea": "") ? "": __t) + '">' + (null == (__t = data.myanswer ? data.myanswer: "") ? "": __t) + "</div>  </div> </div> "),
	__p += "   ",
	6 == data.question_type && (__p += ' <div class="q-res"> ', _.each(data.options,
	function(t, i) {
		__p += '  <div class="q-subitem J_answer_input" data-idx="' + (null == (__t = i + 1) ? "": __t) + '">  <span class="op-order">（' + (null == (__t = i + 1) ? "": __t) + '）</span>  <div class="w">  <ol class="op-items">  ',
		_.each(t,
		function(t, a) {
			__p += '  <li class="op-item">  <span class="radiobox J_inputbox ' + (null == (__t = data.myanswer && data.myanswer[i + 1] == a ? "checked": "") ? "": __t) + '">  <span class="op-item-nut">  <i class="iconw-radio"></i>  <input type="radio" name="" value="' + (null == (__t = a) ? "": __t) + '" style="display:none" ' + (null == (__t = data.myanswer && data.myanswer[i + 1] == a ? "checked": "") ? "": __t) + ' />  <span class="op-ordersn">' + (null == (__t = a) ? "": __t) + ' . </span>  </span>  <span class="op-item-meat">' + (null == (__t = String(t).replace(/http(s)?:/gi, "")) ? "": __t) + "</span>  </span>  </li>  "
		}),
		__p += "  </ol>  </div>  </div>\t "
	}), __p += " </div> ");
	return __p
},
JST["question/options-report"] = function(obj) {
	obj || (obj = {});
	var __t, __p = "",
	__e = _.escape,
	__j = Array.prototype.join;
	function print() {
		__p += __j.call(arguments, "")
	}
	with(obj) - 1 < "123".indexOf(data.question_type) && (__p += '  <div class="q-res">  <ol class="op-items ' + (null == (__t = 3 == data.question_type ? "op-items-xv": "") ? "": __t) + ' ">  ', _.each(data.options,
	function(t, a) {
		__p += '  <li class="op-item">  ',
		2 == data.question_type ? __p += '  <span class="checkbox ' + (null == (__t = data.myanswer.myanswer && _.contains(data.myanswer.myanswer, a) ? "checked": "") ? "": __t) + ' ">  <span class="op-item-nut">  <i class="iconw-checkbox"></i>' + (null == (__t = a) ? "": __t) + ' .   </span>  <span class="op-item-meat">' + (null == (__t = String(t).replace(/http(s)?:/gi, "")) ? "": __t) + "</span>  </span>  ": __p += '  <span class="radiobox ' + (null == (__t = data.myanswer.myanswer == a ? "checked": "") ? "": __t) + '">  <span class="op-item-nut">  <i class="iconw-radio"></i>' + (null == (__t = a) ? "": __t) + ' .  </span>  <span class="op-item-meat">' + (null == (__t = String(t).replace(/http(s)?:/gi, "")) ? "": __t) + "</span>  </span>  ",
		__p += "  </li>  "
	}), __p += '  </ol>  <div class="judeg"><i class="' + (null == (__t = 1 == data.myanswer.is_right ? "qright": data.myanswer.is_check ? "qwrong": "qunknow") ? "": __t) + '"></i></div>  </div>  '),
	__p += "     ",
	4 == data.question_type && data.myanswer && (__p += ' <div class="q-res">  <ul class="fill-items">  ', _.each(data.myanswer.list,
	function(t, a) {
		__p += '  <li class="fill-item cfx">  <span class="fill-hint">【第' + (null == (__t = a + 1) ? "": __t) + '空】</span>  <div class="w"><div class="fill-blank">' + (null == (__t = t.myanswer) ? "": __t) + '</div></div>  <span class="judeg">  <i class="' + (null == (__t = 0 == t.is_check ? "qunknow": 1 == t.is_right ? "qright": "qwrong") ? "": __t) + ' "></i>  </span>  </li>  '
	}), __p += "  </ul> </div> "),
	__p += "     ",
	5 == data.question_type && (__p += ' <div class="q-res">  <div class="fill-myanswer f-cb">  <span class="fill-hint">答：</span>  <div class="w">  <div class="fill-blank">  ' + (null == (__t = data.myanswer.myanswer) ? "": __t) + '  </div>  </div>  <div class="judeg"><i class="' + (null == (__t = 1 == data.myanswer.is_right ? "qright": data.myanswer.is_check ? "qwrong": "qunknow") ? "": __t) + '"></i></div>  </div> </div>  '),
	__p += "      ",
	6 == data.question_type && (__p += '  <div class="q-res">  ', _.each(data.options,
	function(t, i) {
		__p += '  <div class="q-subitem" data-idx="' + (null == (__t = i + 1) ? "": __t) + '">  <span class="op-order">（' + (null == (__t = i + 1) ? "": __t) + '）</span>  <div class="w">  <ol class="op-items">  ',
		_.each(t,
		function(t, a) {
			__p += '  <li class="op-item">  <span class="radiobox ' + (null == (__t = data.myanswer && data.myanswer.list[i].myanswer == a ? "checked": "") ? "": __t) + '">  <span class="op-item-nut">  <i class="iconw-radio"></i>  <span class="op-ordersn">' + (null == (__t = a) ? "": __t) + ' . </span>  </span>  <span class="op-item-meat">' + (null == (__t = String(t).replace(/http(s)?:/gi, "")) ? "": __t) + "</span>  </span>  </li>  "
		}),
		__p += '  </ol>  </div>  <div class="judeg"><i class="' + (null == (__t = 1 == data.myanswer.list[i].is_right ? "qright": "qwrong") ? "": __t) + '"></i></div>\t  </div>  '
	}), __p += "  </div>  ");
	return __p
},
JST["question/options"] = function(obj) {
	obj || (obj = {});
	var __t, __p = "",
	__e = _.escape,
	__j = Array.prototype.join;
	function print() {
		__p += __j.call(arguments, "")
	}
	with(obj) - 1 < "12".indexOf(data.question_type) && (__p += ' <div class="exam-s">  ', _.each(data.options,
	function(t, a) {
		__p += '  <span class="op-item"><span class="op-item-nut">' + (null == (__t = a) ? "": __t) + ' . </span><span class="op-item-meat">' + (null == (__t = String(t).replace(/http(s)?:/gi, "")) ? "": __t) + "</span></span>  "
	}), __p += " </div> "),
	__p += "   ",
	6 == data.question_type && (__p += "  ", _.each(data.options,
	function(t, a) {
		__p += '  <div class="f-cb">  <div class="exam-mynum">（' + (null == (__t = a + 1) ? "": __t) + '）</div>  <div class="w">  <div class="exam-s exam-sw">  ',
		_.each(t,
		function(t, a) {
			__p += '  <span class="op-item">  <span class="op-item-nut">' + (null == (__t = a) ? "": __t) + ' . </span>  <span class="op-item-meat">' + (null == (__t = String(t).replace(/http(s)?:/gi, "")) ? "": __t) + "</span>  </span>  "
		}),
		__p += "  </div>  </div>  </div>  "
	}), __p += " ");
	return __p
},
JST["question/origin-handler-nobtn"] = function(obj) {
	obj || (obj = {});
	var __t, __p = "",
	__e = _.escape;
	with(obj) __p += '<div class="q-msg cfx">  <div class="q-attr fl">  <span>题型：' + (null == (__t = data.question_channel_type_name) ? "": __t) + "</span>  <em>|</em>  <span>题类：" + (null == (__t = data.exam_name) ? "": __t) + "</span>  <em>|</em>  <span>难度：" + (null == (__t = data.difficult_name) ? "": __t) + "</span>  <em>|</em>  <span>组卷次数：" + (null == (__t = data.save_num) ? "": __t) + "</span>  </div> </div>";
	return __p
},
JST["question/origin-handler"] = function(obj) {
	obj || (obj = {});
	var __t, __p = "",
	__e = _.escape,
	__j = Array.prototype.join;
	function print() {
		__p += __j.call(arguments, "")
	}
	with(obj) data.paperid && data.question_source && (__p += ' <div class="q-origin">  <a href="' + (null == (__t = mURL("/paper/view/", data.paperid)) ? "": __t) + '" target="_blank">试题来源：' + (null == (__t = data.question_source) ? "": __t) + "</a> </div> "),
	__p += ' <div class="q-msg cfx">  <div class="q-attr fl">  <span>题型：' + (null == (__t = data.question_channel_type_name) ? "": __t) + "</span>  ",
	"zujuanw" == window.Application.AppName && (__p += "  <em>|</em>  <span>题类：" + (null == (__t = data.exam_name) ? "": __t) + "</span>  "),
	__p += "  <em>|</em>  <span>难度：" + (null == (__t = data.difficult_name) ? "": __t) + "</span>  <em>|</em>  <span>组卷次数：" + (null == (__t = data.save_num) ? "": __t) + "</span>  ",
	0 < data.is_use && (__p += '  <em>|</em>  <span style="color:#ff9a18">您最近3个月使用：' + (null == (__t = data.is_use) ? "": __t) + "次</span>  "),
	__p += '  </div>  <div class="q-handle fr">  ',
	"zujuan21" == window.Application.AppName && (__p += '  <a href="javascript:;" class="q-handle-item" onclick="Application.popupQuestionDownload(' + (null == (__t = data.question_id) ? "": __t) + ')"><i class="iconw-download4" style="margin-top:-2px;"></i>下载</a>  '),
	__p += "  ",
	data.current_user.isSuperAdmin && (__p += '  <a href="//zbadmin.21cnjy.com/examQuestions/setExam?id=' + (null == (__t = data.question_id) ? "": __t) + "&type=1&url=https%2F%2Fwww.21cnjy.com%2Fquestion%2Fdetail%2F" + (null == (__t = data.question_id) ? "": __t) + '" class="q-handle-item J_edit_it" target="_blank"><i class="iconw-edit2"></i>编辑</a>  '),
	__p += '  <a href="' + (null == (__t = mURL("/question/detail/", data.question_id)) ? "": __t) + '" target="_blank" class="q-handle-item J_analyize"><i class="iconw-jiexi"></i>查看解析</a>  ',
	data.is_collect ? __p += '  <a href="javascript:;" class="q-handle-item J_collect">  <i class="iconw-ucollect"></i>取消收藏  </a>  ': __p += '  <a href="javascript:;" class="q-handle-item J_collect">  <i class="iconw-collect"></i>收藏  </a>  ',
	__p += '  <a class="q-handle-item J_report_error"><i class="iconw-error"></i>' + (null == (__t = HtmText.report) ? "": __t) + "</a>  ",
	data.exists_in_basket ? __p += '  <a class="q-add-btn active J_add_remove">- 移除</a>  ': __p += '  <a class="q-add-btn J_add_remove">+ 选题</a>  ',
	__p += "  </div> </div>";
	return __p
},
JST["question/origin-handler2"] = function(obj) {
	obj || (obj = {});
	var __t, __p = "",
	__e = _.escape,
	__j = Array.prototype.join;
	function print() {
		__p += __j.call(arguments, "")
	}
	with(obj) data.paperid && data.question_source && (__p += ' <div class="q-origin">  <a href="' + (null == (__t = mURL("/paper/view/", data.paperid)) ? "": __t) + '" target="_blank">试题来源：' + (null == (__t = data.question_source) ? "": __t) + "</a> </div> "),
	__p += ' <div class="q-msg cfx">  <div class="q-attr fl">  <span>题型：' + (null == (__t = data.question_channel_type_name) ? "": __t) + "</span>  <em>|</em>  <span>题类：" + (null == (__t = data.exam_name) ? "": __t) + "</span>  <em>|</em>  <span>难度：" + (null == (__t = data.difficult_name) ? "": __t) + "</span>  <em>|</em>  <span>组卷次数：" + (null == (__t = data.save_num) ? "": __t) + '</span>  </div>  <div class="q-handle fr">  ',
	data.current_user.isSuperAdmin && (__p += '  <a href="//zbadmin.21cnjy.com/examQuestions/setExam?id=' + (null == (__t = data.question_id) ? "": __t) + "&type=1&url=https%2F%2Fwww.21cnjy.com%2Fquestion%2Fdetail%2F" + (null == (__t = data.question_id) ? "": __t) + '" class="q-handle-item J_edit_it" target="_blank"><i class="iconw-edit2"></i>编辑</a>  '),
	__p += '  <a href="' + (null == (__t = mURL("/question/detail/", data.question_id)) ? "": __t) + '" target="_blank" class="q-handle-item J_analyize"><i class="iconw-jiexi"></i>查看解析</a>  ',
	data.is_collect ? __p += '  <a href="javascript:;" class="q-handle-item J_collect">  <i class="iconw-ucollect"></i>取消收藏  </a>  ': __p += '  <a href="javascript:;" class="q-handle-item J_collect">  <i class="iconw-collect"></i>收藏  </a>  ',
	__p += '  <a class="q-handle-item J_report_error"><i class="iconw-error"></i>' + (null == (__t = HtmText.report) ? "": __t) + "</a>  </div> </div>";
	return __p
},
JST["question/select-ques-type"] = function(obj) {
	obj || (obj = {});
	var __t, __p = "",
	__e = _.escape,
	__j = Array.prototype.join;
	function print() {
		__p += __j.call(arguments, "")
	}
	with(obj) __p += "<ul>  ",
	_.each(types,
	function(t) {
		__p += "  ";
		var a = t && 5 < t.toString().length ? t.toString().slice(0, 4) + "...": t;
		__p += '  <li class="J_add_remove" data-t="' + (null == (__t = t) ? "": __t) + '"><a href="javascript:;" title="' + (null == (__t = t) ? "": __t) + '">' + (null == (__t = a) ? "": __t) + "</a></li>  "
	}),
	__p += " </ul>";
	return __p
},
JST["question/text-score"] = function(obj) {
	obj || (obj = {});
	var __t, __p = "",
	__e = _.escape,
	__j = Array.prototype.join;
	function print() {
		__p += __j.call(arguments, "")
	}
	with(obj) __p += '<div class="q-tit">' + (null == (__t = 0 != data.parent_id ? "（" + (data._n + 1) + "）": data._n + 1 + ". ") ? "": __t),
	0 == data.parent_id && (__p += '<span class="t-score">（' + (null == (__t = data.score.score) ? "": __t) + "分）</span>"),
	__p += (null == (__t = String(data.question_text).replace(/http(s)?:/gi, "")) ? "": __t) + " ",
	data.extra_file && (__p += ' <div class="q-audio" style="margin-bottom:10px;cursor:pointer;"> <audio controls>  <source src="' + (null == (__t = data.extra_file) ? "": __t) + '" />  <embed src="' + (null == (__t = data.extra_file) ? "": __t) + '"></embed> </audio> </div> '),
	__p += " </div>";
	return __p
},
JST["question/text"] = function(obj) {
	obj || (obj = {});
	var __t, __p = "",
	__e = _.escape,
	__j = Array.prototype.join;
	function print() {
		__p += __j.call(arguments, "")
	}
	with(obj) __p += '<div class="q-tit">' + (null == (__t = 0 != data.parent_id ? "（" + (data._n + 1) + "）": data._n + 1 + ". ") ? "": __t) + (null == (__t = String(data.question_text).replace(/http(s)?:/gi, "")) ? "": __t) + " ",
	data.extra_file && (__p += ' <div class="q-audio" style="margin-bottom:10px;cursor:pointer;"> <audio controls>  <source src="' + (null == (__t = data.extra_file) ? "": __t) + '" /> </audio> </div> '),
	__p += " </div>";
	return __p
},
JST["question/type-show"] = function(obj) {
	obj || (obj = {});
	var __t, __p = "",
	__e = _.escape;
	with(obj) __p += '<div class="do-q-mt">  <strong class="do-q-tit">' + (null == (__t = myUtils.chinesesn(data._n)) ? "": __t) + "、" + (null == (__t = data._t) ? "": __t) + '<span class="q-score">(共' + (null == (__t = type_count.count) ? "": __t) + "题；共" + (null == (__t = type_count.score) ? "": __t) + '分)</span></strong> </div> <ul class="do-q-mc"></ul>';
	return __p
},
JST["searchpage/search-qblock"] = function(obj) {
	obj || (obj = {});
	var __t, __p = "",
	__e = _.escape,
	__j = Array.prototype.join;
	function print() {
		__p += __j.call(arguments, "")
	}
	with(obj) __p += '<div class="loading-wrap">  <div class="loading-bg"></div>  <div class="loading"></div> </div>  ',
	data.total ? __p += " <ul> </ul> ": __p += ' <div class="empty-ffxi">  <img src="' + (null == (__t = CDN_LOCAL_DOMAIN) ? "": __t) + '/images/blank.png">  <p>没有相关试题，换个条件试试吧。</p> </div> ';
	return __p
},
JST["searchpage/search-tblock"] = function(obj) {
	obj || (obj = {});
	var __t, __p = "",
	__e = _.escape,
	__j = Array.prototype.join;
	function print() {
		__p += __j.call(arguments, "")
	}
	with(obj) __p += '<div class="loading-wrap">  <div class="loading-bg"></div>  <div class="loading"></div> </div> ',
	_.size(data.list) ? (__p += "  <ul>  ", _.each(data.list,
	function(t) {
		__p += '  <li>  <div class="item-wrap">  <div class="item-img">  <a href="' + (null == (__t = mURL("/paper/view/", t.pid)) ? "": __t) + '" traget="_blank"><img src="' + (null == (__t = CDN_LOCAL_DOMAIN) ? "": __t) + '/build/images/shijuan.png"></a>  </div>  <div class="w fl">  <div class="item-mc">  <h3 class="item-tit"><a href="' + (null == (__t = mURL("/paper/view/", t.pid)) ? "": __t) + '" traget="_blank" title="' + (null == (__t = t.origin_title) ? "": __t) + '">' + (null == (__t = t.title) ? "": __t) + '</a></h3>  <div class="item-attr">  <span><i class="iconw-time"></i>修改时间：' + (null == (__t = myUtils.formatTimestamp(t.examine_time)) ? "": __t) + '</span>  <span><i class="iconw-download"></i>下载次数：' + (null == (__t = t.use_num) ? "": __t) + '</span>  <span><i class="iconw-leixing"></i>类型：' + (null == (__t = t.typeName) ? "": __t) + '</span>  </div>  </div>  </div>  <div class="item-act">  <a class="download-btn" onclick="Application.popupPaperDownload(' + (null == (__t = t.pid) ? "": __t) + ')">下载</a>  <a class="fun-btn J_analyze" data-pid="' + (null == (__t = t.pid) ? "": __t) + '" onclick="Application.AnalyzeChart.show(' + (null == (__t = t.pid) ? "": __t) + ')" ><span class="iconw-fenxi2"></span>试卷分析</a>  </div>  </div>  </li>  '
	}), __p += " </ul> ") : __p += ' <div class="empty-ffxi">  <img src="' + (null == (__t = CDN_LOCAL_DOMAIN) ? "": __t) + '/images/blank.png">  <p>筛选无结果，换个条件试试吧。</p> </div> ';
	return __p
},
JST["smartpage/node-results"] = function(obj) {
	obj || (obj = {});
	var __t, __p = "",
	__e = _.escape,
	__j = Array.prototype.join;
	function print() {
		__p += __j.call(arguments, "")
	}
	with(obj) __p += '<div class="smart-mt cfx">  <strong>已选' + (null == (__t = "categories" == tree_type ? "章节": "知识点") ? "": __t) + "（<span>" + (null == (__t = _.size(list)) ? "": __t) + '</span>个）</strong>  <a href="javascript:;" class="J_clear_all"><i class="iconw-del2"></i>清空</a> </div> <div class="smart-mc">  <div class="smart-sel-list cfx">  ',
	_.size(list) ? (__p += "  ", _.each(list,
	function(t) {
		__p += '  <div class="smart-sel-item" data-id="' + (null == (__t = t.id) ? "": __t) + '">  ' + (null == (__t = t.title) ? "": __t) + '<span class="smart-del"><i class="iconw-close"></i></span>  <input type="checkbox" checked name="' + (null == (__t = "categories" == tree_type ? "categories[]": "knowledges[]") ? "": __t) + '" value="' + (null == (__t = t.id) ? "": __t) + '" style="display:none">  </div>  '
	}), __p += "  ") : __p += "  <p>您未选择" + (null == (__t = "categories" == tree_type ? "章节": "知识点") ? "": __t) + "！</p>  ",
	__p += "  </div> </div>";
	return __p
},
JST["smartpage/paper-items"] = function(obj) {
	obj || (obj = {});
	var __t, __p = "",
	__e = _.escape,
	__j = Array.prototype.join;
	function print() {
		__p += __j.call(arguments, "")
	}
	with(obj)"2" == addtype ? (__p += '  <div class="handle-line cfx">  <div class="sort-item fl">  <span class="' + (null == (__t = "edit_time" == order ? "sort-current": "") ? "": __t) + '" data-param="order=edit_time">时间<i class="iconw-sort-desc"></i></span>  <span class="' + (null == (__t = "makenum" == order ? "sort-current": "") ? "": __t) + '" data-param="order=makenum">使用次数<i class="iconw-sort-desc"></i></span>  ', "zujuan21" == window.Application.AppName ? __p += '  <a href="/help/notice?id=41" target="_blank"><i class="iconw-what3"></i>如何使用双向细目表</a>  ': __p += '  <a href="/help/article?id=44" target="_blank"><i class="iconw-what3"></i>如何使用双向细目表</a>  ', __p += '  </div>  <div class="act-item fr">  <span>共计：<b class="J_total">' + (null == (__t = count) ? "": __t) + "</b>份</span>  </div>  </div>  ") : __p += '  <div class="handle-line cfx">  <div class="sort-item fl">  <span>共计：<b >' + (null == (__t = count) ? "": __t) + '</b>份</span>  </div>  <div class="act-item fr">  <a class="selall-btn J_build">新建细目表</a>  </div>  </div>  ',
	__p += " " + (null == (__t = JST["partial/list-loading"]()) ? "": __t) + " ",
	_.size(list) ? (__p += ' <ul class="' + (null == (__t = "2" == addtype ? "smart-detail-list": "smart-mydetail-list") ? "": __t) + '">  ', _.each(list,
	function(t) {
		__p += '  <li>  <div class="item-wrap">  <div class="item-img J_islogin">  <a href="' + (null == (__t = user.get("uid") ? "/smart/spec-edit/" + t.id: "javascript:;") ? "": __t) + ' "><img src="' + (null == (__t = CDN_LOCAL_DOMAIN) ? "": __t) + '/build/images/xmb.png"></a>  </div>  <div class="w fl">  <div class="item-mc">  <h3 class="item-tit J_islogin"><a href="' + (null == (__t = user.get("uid") ? "/smart/spec-edit/" + t.id: "javascript:;") ? "": __t) + ' " title="' + __e(t.title) + '">' + (null == (__t = t.title) ? "": __t) + '</a></h3>  <div class="item-attr">  <span><i class="iconw-time"></i>上传时间：' + (null == (__t = t.format_date) ? "": __t) + '</span>  <span><i class="iconw-leixing"></i>类型：' + (null == (__t = t.ximutype_name) ? "": __t) + '</span>  <span><i class="iconw-use"></i>使用人数：' + (null == (__t = t.makenum) ? "": __t) + '人</span>  </div>  </div>  </div>  <div class="item-act">  <a href="' + (null == (__t = user.get("uid") ? "/smart/spec-edit/" + t.id: "javascript:;") ? "": __t) + ' " class="download-btn J_islogin">使用</a>  </div>  </div>  ',
		1 == addtype && (__p += '  <a href="javascript:;" data-xid="' + (null == (__t = t.id) ? "": __t) + '" class="del iconw-del J_del_ximu"></a>  '),
		__p += "   </li>  "
	}), __p += " </ul> ") : __p += ' <div class="empty-ffxi">  <img src="' + (null == (__t = CDN_LOCAL_DOMAIN) ? "": __t) + '/images/blank.png">  <p>当前条件下没有找到细目表。</p> </div> ';
	return __p
},
JST["smartpage/setting-input"] = function(obj) {
	obj || (obj = {});
	var __t, __p = "",
	__e = _.escape,
	__j = Array.prototype.join;
	function print() {
		__p += __j.call(arguments, "")
	}
	with(obj) data.selected && (__p += ' <div class="fl cfx">  <span class="setting-tit fl" title="' + (null == (__t = data.question_channel_type_name) ? "": __t) + '">' + (null == (__t = data.question_channel_type_name) ? "": __t) + "：</span>  ", _.each(data.difficulty_items,
	function(t) {
		__p += '  <div class="fl difficult-type">  <span>' + (null == (__t = t.name) ? "": __t) + '</span>  <input type="text"   placeholder="0"  ' + (null == (__t = t.is_disabled) ? "": __t) + '   data-difficulty="' + (null == (__t = t.id) ? "": __t) + '"  name="' + (null == (__t = t.field_name) ? "": __t) + '"   class="' + (null == (__t = t.style) ? "": __t) + '"   value="' + (null == (__t = t.value) ? "": __t) + '"   >  <em><b>' + (null == (__t = t.enabled_num) ? "": __t) + "</b>道试题可用</em>  </div>  "
	}), __p += ' </div> <div class="setting-fun fr">  <span>难度系数：' + (null == (__t = data.difficulty_coefficient) ? "": __t) + '</span>  <i class="del iconw-del2"></i> </div> ');
	return __p
},
JST["specpage/add-new-head"] = function(obj) {
	obj || (obj = {});
	var __t, __p = "",
	__e = _.escape,
	__j = Array.prototype.join;
	function print() {
		__p += __j.call(arguments, "")
	}
	with(obj) __p += '<form action="" class="save-question-form"> \x3c!--   <div class="type-name">  <label for="">大题名称：</label>  <input type="text" name="head_title" placeholder="请输入大题名称">  </div> --\x3e  <div class="f-cb">  <div class="select-item">  <label for="x-num">试题数量：</label>  <input type="text" name="num" class="x-num" value="1" >  </div>  <div class="select-item">  <label for="">选择题型：</label>  <select name="question_channel_type" id="">  ',
	_.each(params.question_channel_types,
	function(t, a) {
		__p += '  <option value="' + (null == (__t = a) ? "": __t) + '">' + (null == (__t = t) ? "": __t) + "</option>  "
	}),
	__p += '  </select>  </div>  <div class="select-item">  <label for="">试题难度：</label>  <select name="difficult_index" id="">  ',
	_.each(params.difficult_indexs,
	function(t, a) {
		__p += '  <option value="' + (null == (__t = a) ? "": __t) + '">' + (null == (__t = t) ? "": __t) + "</option>  "
	}),
	__p += "  </select>  </div>  </div> </form>";
	return __p
},
JST["specpage/add-new-ques"] = function(obj) {
	obj || (obj = {});
	var __t, __p = "",
	__e = _.escape,
	__j = Array.prototype.join;
	function print() {
		__p += __j.call(arguments, "")
	}
	with(obj) __p += '<form action="" class="save-question-form f-cb">  <div class="select-item">  <label for="x-num">试题数量：</label>  <input type="text" name="num" class="x-num" value="1" >  </div>  <div class="select-item">  <label for="">选择题型：</label>  <select name="question_channel_type" id="">  ',
	_.each(params.question_channel_types,
	function(t, a) {
		__p += '  <option value="' + (null == (__t = a) ? "": __t) + '">' + (null == (__t = t) ? "": __t) + "</option>  "
	}),
	__p += '  </select>  </div>  <div class="select-item">  <label for="">试题难度：</label>  <select name="difficult_index" id="">  ',
	_.each(params.difficult_indexs,
	function(t, a) {
		__p += '  <option value="' + (null == (__t = a) ? "": __t) + '">' + (null == (__t = t) ? "": __t) + "</option>  "
	}),
	__p += "  </select>  </div> </form>";
	return __p
},
JST["specpage/dia-kn-item"] = function(obj) {
	obj || (obj = {});
	var __t, __p = "",
	__e = _.escape;
	with(obj) __p += '<div class="kn-item">' + (null == (__t = name) ? "": __t) + '<span class="del-it" data-id="' + (null == (__t = kid) ? "": __t) + '"><i class="icone-del"></i></span></div>';
	return __p
},
JST["specpage/dia-know-tree"] = function(obj) {
	obj || (obj = {});
	var __t, __p = "",
	__e = _.escape,
	__j = Array.prototype.join;
	function print() {
		__p += __j.call(arguments, "")
	}
	with(obj) data ? (__p += '  <div class="hd">已选知识点<span>（最多选5个）</span></div> <div class="kn-list">  ', _.each(data.knowledge,
	function(t, a) {
		__p += '  <div class="kn-item">' + (null == (__t = t.name) ? "": __t) + '<span class="del-it" data-id="' + (null == (__t = t.kid) ? "": __t) + '"><i class="icone-del"></i></span></div>  '
	}), __p += " </div>  ") : __p += ' <div class="f-cb dialog-know-tree">  <div class="kn-tree t-tree"></div>  <div class="w f-fl">  <div class="kn-selected-box">    </div>  </div>  <div class="search-kn-items">  <form class="search-kn-items-form">  <input type="text" class="search-kn-items-input" placeholder="关键字搜索" name="search_words">  <button type="submit" >搜索</button>  </form>  <div class="search-kn-items-result J_SearchResult">    </div>  </div> </div> ';
	return __p
},
JST["specpage/dia-select-spec"] = function(obj) {
	obj || (obj = {});
	var __t, __p = "",
	__e = _.escape;
	with(obj) __p += '<form class="dialog-temp-form">  <div class="name-wave" style="font-size: 12px;">*请选择细目表的类型：</div>  <div class="f-cb type-wave">  <span class="custom-radio ' + (null == (__t = 1 == ximutype ? "checked": "") ? "": __t) + '"><i class="iconw-radio"></i>' + (null == (__t = nj) ? "": __t) + '模拟<input type="radio" name="paper_type" value="1" class="f-dn" ' + (null == (__t = 1 == ximutype ? "checked": "") ? "": __t) + ' ></span>  <span class="custom-radio ' + (null == (__t = 2 == ximutype ? "checked": "") ? "": __t) + '"><i class="iconw-radio"></i>期中试卷<input type="radio" name="paper_type" value="2" class="f-dn" ' + (null == (__t = 2 == ximutype ? "checked": "") ? "": __t) + ' ></span>  <span class="custom-radio ' + (null == (__t = 3 == ximutype ? "checked": "") ? "": __t) + '"><i class="iconw-radio"></i>期末试卷<input type="radio" name="paper_type" value="3" class="f-dn" ' + (null == (__t = 3 == ximutype ? "checked": "") ? "": __t) + ' ></span>  <span class="custom-radio ' + (null == (__t = 4 == ximutype ? "checked": "") ? "": __t) + '"><i class="iconw-radio"></i>其他<input type="radio" name="paper_type" value="3" class="f-dn" ' + (null == (__t = 3 == ximutype ? "checked": "") ? "": __t) + " ></span>  </div> </form> <script>    var g = [];  $('.dialog-temp-form').find('.custom-radio').each(function () {  new OT2.Element.radio(this, g).bindEvent();  });   <\/script>";
	return __p
},
JST["specpage/item-head"] = function(obj) {
	obj || (obj = {});
	var __t, __p = "",
	__e = _.escape;
	with(obj) __p += '<div class="diy-tixy-hd">  <div class="big-tixy-tit">  <span class="tixy-sort">' + (null == (__t = myUtils.chinesesn(data._n)) ? "": __t) + '</span>、<span class="editable J_Edit">' + __e(data.head_title.replace(/&\w+?;|<\/?[^>]*>/g, "")) + '</span>  </div>  <div class="act">  <a href="javascript:;" class="del btn J_DelQ"><i class="iconw-del3"></i>删除</a>  <a href="javascript:;" class="add btn J_AddQ">+ 添加小题</a>  </div> </div> <div class="diy-tixy-grid">  <table>  <thead>  <tr>  <td>题序</td>  <td>题型</td>  <td>关联知识点<span class="kn-tit-tips">（最多选5个）</span></td>  <td>难度</td>  <td>操作</td>  </tr>  </thead>  <tbody></tbody>  </table> </div>';
	return __p
},
JST["specpage/item-ques"] = function(obj) {
	obj || (obj = {});
	var __t, __p = "",
	__e = _.escape,
	__j = Array.prototype.join;
	function print() {
		__p += __j.call(arguments, "")
	}
	with(obj) {
		__p += '<td class="cell-1"><span>' + (null == (__t = data._n + 1) ? "": __t) + '</span></td> <td class="cell-2">  <dl class="drop-list">  <dt>  ';
		var x1 = params.question_channel_types[data.question_channel_type];
		__p += '  <span title="' + (null == (__t = x1) ? "": __t) + '" >' + (null == (__t = x1 ? x1.slice(0, 6) : x1) ? "": __t) + '</span>  <i class="icone-sjjc"></i></dt>  <dd>  ',
		_.each(params.question_channel_types,
		function(t, a) {
			__p += '  <div data-val="' + (null == (__t = [data.cid, "question_channel_type", a].join(",")) ? "": __t) + '" title="' + (null == (__t = t) ? "": __t) + '" >' + (null == (__t = t) ? "": __t) + "</div>  "
		}),
		__p += '  </dd>  </dl> </td> <td class="cell-3">  <div class="kn-items J_kn_items">  ',
		_.each(data.knowledge,
		function(t, a) {
			__p += '  <span class="kn-item">' + (null == (__t = t.name) ? "": __t) + '<span class="del-it J_del_kn" data-kid="' + (null == (__t = t.kid) ? "": __t) + '"><i class="icone-del"></i></span></span>  '
		}),
		__p += "  ",
		_.size(data.knowledge) < 5 && (__p += '  <span class="kn-add-item J_add_kn">+ 添加知识点</span>  '),
		__p += '  </div> </td> <td class="cell-4">  <dl class="drop-list">  <dt><span>' + (null == (__t = params.difficult_indexs[data.difficult_index]) ? "": __t) + '</span><i class="icone-sjjc"></i></dt>  <dd>  ',
		_.each(params.difficult_indexs,
		function(t, a) {
			__p += '  <div data-val="' + (null == (__t = [data.cid, "difficult_index", a].join(",")) ? "": __t) + '" >' + (null == (__t = t) ? "": __t) + "</div>  "
		}),
		__p += '  </dd>  </dl> </td> <td class="cell-6"><a href="javascript:;" class="del-uiti J_del_q"><i class="iconw-del2"></i></a></td>'
	}
	return __p
},
JST["specpage/report-analyze"] = function(obj) {
	obj || (obj = {});
	var __t, __p = "",
	__e = _.escape,
	__j = Array.prototype.join;
	function print() {
		__p += __j.call(arguments, "")
	}
	with(obj) data.len ? (__p += '  <h4>大题题量分析</h4>  <div id="J_ChartQNum" class="xc"></div>  <h4>难度分析</h4>  <div id="J_ChartDifficulty" class="xc"></div>  ', 0 < _.size(data.knowledge) && (__p += '  <h4>知识点分析</h4>  <div id="J_ChartKnowlist" class="xc"></div>  '), __p += " ") : __p += '  <div class="empty-ffxi">  <img src="' + (null == (__t = CDN_LOCAL_DOMAIN) ? "": __t) + '/images/blank.png">  <p>未检测到相关数据！</p>  </div> ';
	return __p
},
JST["specpage/save-spec"] = function(obj) {
	obj || (obj = {});
	var __t, __p = "",
	__e = _.escape;
	with(obj) __p += '<form class="dialog-temp-form">  <div class="name-wave"><label for="">细目表名称：</label><input type="text" name="title" value="' + (null == (__t = name) ? "": __t) + '" class="ximu-name" placeholder="请输入细目表名称"></div>  <div class="f-cb type-wave">  <label>细目表类型：</label>  <span class="custom-radio ' + (null == (__t = 1 == ximutype ? "checked": "") ? "": __t) + '"><i class="iconw-radio"></i>' + (null == (__t = nj) ? "": __t) + '模拟<input type="radio" name="paper_type" value="1" class="f-dn" ' + (null == (__t = 1 == ximutype ? "checked": "") ? "": __t) + ' ></span>  <span class="custom-radio ' + (null == (__t = 2 == ximutype ? "checked": "") ? "": __t) + '"><i class="iconw-radio"></i>期中试卷<input type="radio" name="paper_type" value="2" class="f-dn" ' + (null == (__t = 2 == ximutype ? "checked": "") ? "": __t) + ' ></span>  <span class="custom-radio ' + (null == (__t = 3 == ximutype ? "checked": "") ? "": __t) + '"><i class="iconw-radio"></i>期末试卷<input type="radio" name="paper_type" value="3" class="f-dn" ' + (null == (__t = 3 == ximutype ? "checked": "") ? "": __t) + ' ></span>  <span class="custom-radio ' + (null == (__t = 4 == ximutype ? "checked": "") ? "": __t) + '"><i class="iconw-radio"></i>其他<input type="radio" name="paper_type" value="4" class="f-dn" ' + (null == (__t = 4 == ximutype ? "checked": "") ? "": __t) + " ></span>  </div> </form>";
	return __p
},
JST["specpage/search-kn-items-result"] = function(obj) {
	obj || (obj = {});
	var __t, __p = "",
	__e = _.escape,
	__j = Array.prototype.join;
	function print() {
		__p += __j.call(arguments, "")
	}
	with(obj) _.size(data) ? (__p += " ", _.each(data,
	function(t) {
		__p += " <dl>  <dt>" + (null == (__t = t.name) ? "": __t) + "</dt>  ",
		_.each(t.list,
		function(t) {
			__p += '  <dd data-kid="' + (null == (__t = t.kid) ? "": __t) + '">' + (null == (__t = t.name) ? "": __t) + "</dd>  "
		}),
		__p += " </dl> "
	}), __p += " ") : __p += "  <p>搜索结果：暂无相关知识点可选...</p> ";
	return __p
},
JST["specpage/tbl-kn-item"] = function(obj) {
	obj || (obj = {});
	var __t, __p = "",
	__e = _.escape,
	__j = Array.prototype.join;
	function print() {
		__p += __j.call(arguments, "")
	}
	with(obj) _.each(data.knowledge,
	function(t, a) {
		__p += ' <span class="kn-item">' + (null == (__t = t.name) ? "": __t) + '<span class="del-it J_del_kn" data-kid="' + (null == (__t = t.kid) ? "": __t) + '"><i class="icone-del"></i></span></span> '
	}),
	__p += " ",
	_.size(data.knowledge) < 5 && (__p += ' <span class="kn-add-item J_add_kn">+ 添加知识点</span> '),
	__p += " ",
	"knowledge" == errcode && (__p += '<span class="none-kn-item">（请添加知识点）</span>'),
	__p += " ",
	"none" == errcode && (__p += '<p class="none-kn-question">（没有找到符合当前条件的试题）</p>');
	return __p
},
JST["specpage/ximu-type"] = function(obj) {
	obj || (obj = {});
	var __t, __p = "",
	__e = _.escape,
	__j = Array.prototype.join;
	function print() {
		__p += __j.call(arguments, "")
	}
	with(obj) __p += '<div class="item-attr-mt">  <span class="item-attr-tit">类型：' + (null == (__t = data[cur_type] || "--") ? "": __t) + '<i class="iconw-down2"></i></span>  <div class="item-attr-mc">  ',
	_.each(data,
	function(t, a) {
		__p += '  <a href="javascript:;" data-ximutype="' + (null == (__t = a) ? "": __t) + '" >' + (null == (__t = t) ? "": __t) + "</a>  "
	}),
	__p += "  </div> </div>";
	return __p
},
JST["subjectpage/paper-item"] = function(obj) {
	obj || (obj = {});
	var __t, __p = "",
	__e = _.escape,
	__j = Array.prototype.join;
	function print() {
		__p += __j.call(arguments, "")
	}
	with(obj) if ("chapter" == data.type) __p += ' <dl class="subject-list cfx">  <dt>  <div class="w fl">  <div class="subject-cn">  <label class="iconw-checkbox custom-checkbox">  <input type="checkbox" value="' + (null == (__t = data.pid) ? "": __t) + '" name="chapter[]">  </label>  <a href="javascript:;" class="subject-tit" title="' + (null == (__t = data.name) ? "": __t) + '">' + (null == (__t = data.name) ? "": __t) + "</a>  ",
	current_user.co_partner || (__p += "  <span>该专题只对<em>VIP</em>与<em>组卷通</em>用户开放</span>  "),
	__p += "  </div>  </div>  ",
	current_user.co_partner || (__p += '  <div class="subject-fun">  <a href="/help/request" class="link">还没有组卷通？点此申请</a>  </div>  '),
	__p += "    </dt> </dl> ";
	else {
		__p += ' <dd>  <div class="w fl">  <div class="subject-cn">  <label class="iconw-checkbox custom-checkbox ' + (null == (__t = data.checked ? "checked": "") ? "": __t) + ' ">  <input type="checkbox" value="' + (null == (__t = data.pid) ? "": __t) + '" name="paper[]">  </label>  ';
		var short_title = data.name.toString();
		short_title = short_title.slice(0, 48) + (short_title.slice(48, 49) ? "...": ""),
		__p += '  <a href="' + (null == (__t = mURL("/paper/view/", data.pid)) ? "": __t) + '" target="_blank" class="subject-tit" title="' + (null == (__t = data.name) ? "": __t) + '">' + (null == (__t = short_title) ? "": __t) + "<span>(" + (null == (__t = data.paper_data && data.paper_data.qcount) ? "": __t) + '道题)</span></a>   </div>  </div>  <div class="subject-fun __aa">  <a href="/paper/test/' + (null == (__t = data.pid) ? "": __t) + '" target="_blank" class="test-btn J_islogin"><i class="iconw-ceshi2"></i>在线测试</a>  ',
		data.test ? __p += '  <span class="msg"> 平均分：<span class="numc">' + (null == (__t = data.test.avg) ? "": __t) + "分</span></span>  ": __p += '  <span class="msg"> 平均分：<span>暂无测试</span></span>  ',
		__p += "  </div> </dd> "
	}
	return __p
},
JST["subjectpage/subject-items"] = function(obj) {
	obj || (obj = {});
	var __t, __p = "",
	__e = _.escape,
	__j = Array.prototype.join;
	function print() {
		__p += __j.call(arguments, "")
	}
	with(obj) __p += '<div class="loading-wrap">  <div class="loading-bg"></div>  <div class="loading"></div> </div> ',
	_.size(list) ? (__p += ' <ul class=" cfx">  ', _.each(list,
	function(t) {
		t.short_title = t.title.toString(),
		t.short_title = t.short_title.slice(0, 52) + (t.short_title.slice(52, 53) ? "...": ""),
		__p += '  <li>  <div class="subject bg1 subject-item--type' + (null == (__t = t.type) ? "": __t) + '">  <div class="subject-bd cfx">  <div class="subject-pic">  <i class="iconc-zt"></i>  </div>  <div class="subject-mc">  <p>' + (null == (__t = t.type_name) ? "": __t) + '</p>  <h3><a href="' + (null == (__t = mURL("/subject/detail/", t.id)) ? "": __t) + '" target="_blank" title="' + (null == (__t = t.title) ? "": __t) + '">' + (null == (__t = t.short_title) ? "": __t) + "</a></h3>  </div>  ",
		t.new_flag && (__p += '  <span class="icon-subject--new"></span>  '),
		__p += '  </div>  <div class="subject-ft">  <span><i class="iconw-time3"></i>时间：' + (null == (__t = t.format_date) ? "": __t) + '</span>  <span><i class="iconw-download2"></i>下载：' + (null == (__t = t.downcount) ? "": __t) + '</span>  <span><i class="iconw-eye"></i>浏览量：' + (null == (__t = t.hits) ? "": __t) + "次</span>  </div>  </div>  </li>  "
	}), __p += " </ul> ") : __p += ' <div class="empty-ffxi">  <img src="' + (null == (__t = CDN_LOCAL_DOMAIN) ? "": __t) + '/images/blank.png">  <p>筛选无结果，换个条件试试吧。</p> </div> ';
	return __p
},
JST["test/head-title"] = function(obj) {
	obj || (obj = {});
	var __t, __p = "",
	__e = _.escape;
	with(obj) __p += '<div class="do-q-mt">  <strong class="do-q-tit">' + (null == (__t = myUtils.chinesesn(data._n)) ? "": __t) + "、" + (null == (__t = data._t) ? "": __t) + '</strong> </div> <div class="do-q-mc J_ques_items">  </div>';
	return __p
},
JST["test/side-card"] = function(obj) {
	obj || (obj = {});
	var __t, __p = "",
	__e = _.escape,
	__j = Array.prototype.join;
	function print() {
		__p += __j.call(arguments, "")
	}
	with(obj) head_t_collection.each(function(t) {
		__p += ' <div class="edit-handle-mt" title="' + (null == (__t = t.bareTitle()) ? "": __t) + '">  <strong><span>' + (null == (__t = myUtils.chinesesn(t.get("_n"))) ? "": __t) + "、</span>" + (null == (__t = t.get("_t")) ? "": __t) + '</strong> </div> <div class="edit-handle-bd">  <ul class="item-num cfx">  ',
		t.collection.each(function(i) {
			__p += "  ",
			6 == i.get("question_type") ? (__p += "  ", _.each(i.get("options"),
			function(t, a) {
				__p += '  <li data-idz="' + (null == (__t = i.id) ? "": __t) + "." + (null == (__t = a) ? "": __t) + '">  <a href="javascript:;" class="' + (null == (__t = i.hasDone(a + 1) ? "done": "") ? "": __t) + '" >' + (null == (__t = i.get("_n") + 1) ? "": __t) + "." + (null == (__t = a + 1) ? "": __t) + "</a>  </li>  "
			}), __p += "  ") : 7 == i.get("question_type") ? (__p += "  ", i.collection.each(function(t, a) {
				__p += '  <li data-idz="' + (null == (__t = i.id) ? "": __t) + "." + (null == (__t = a) ? "": __t) + '">  <a href="javascript:;" class="' + (null == (__t = t.hasDone() ? "done done1": "") ? "": __t) + '" >' + (null == (__t = i.get("_n") + 1) ? "": __t) + "." + (null == (__t = a + 1) ? "": __t) + "</a>  </li>  "
			}), __p += "  ") : __p += '  <li data-idz="' + (null == (__t = i.id) ? "": __t) + '">  <a href="javascript:;" class="' + (null == (__t = i.hasDone() ? "done": "") ? "": __t) + '" >' + (null == (__t = i.get("_n") + 1) ? "": __t) + "</a>  </li>  ",
			__p += "  "
		}),
		__p += "  </ul> </div> "
	});
	return __p
},
JST["test/used-time"] = function(obj) {
	obj || (obj = {});
	var __t, __p = "",
	__e = _.escape;
	with(obj) __p += '<div class="timer-item">  <h3>00</h3>  <p>小时</p> </div> <div class="timer-item">  <h3>00</h3>  <p>分钟</p> </div> <div class="timer-item">  <h3>00</h3>  <p>秒</p> </div>';
	return __p
};