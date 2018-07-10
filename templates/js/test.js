//star
$(document).ready(init);
var user_id = null;
var last_head = null;
var last_yan = null;
var in_progress = false;
var timeid = null;
var star_has = false;
var is_pc = true;
var last_poem = null;
var last_type = null;

function randomString(len) {　　
    len = len || 32;　　
    var $chars = 'ABCDEFGHJKMNPQRSTWXYZabcdefhijkmnprstwxyz2345678'; /****默认去掉了容易混淆的字符oOLl,9gq,Vv,Uu,I1****/ 　　
    var maxPos = $chars.length;　　
    var pwd = '';　　
    for (i = 0; i < len; i++) {
        pwd += $chars.charAt(Math.floor(Math.random() * maxPos));
    }
    return pwd;
}

function init() {
    $('#button_yes').click(update);
    $("#user_input").bind("keydown", function(e) {
        var event = e || window.event;
        var code = event.keyCode || event.which || event.charCode;
        if (code == '\n'.charCodeAt(0) || code == '\r'.charCodeAt(0)) {
            e.preventDefault();
            $('#button_yes').click();
        }
    }).focus();
    user_id = randomString(30);
    console.log(user_id);
}

function update() {
    var this_head = $('#keyword')[0].value;
    this_head = this_head.trim();


    for (var i = 0; i < this_head.length; i++) {
        if (encodeURI(this_head[i]).length != 9)
            all_chinese = false;
    }
    if (!all_chinese) {
        show_strings(['只能输入汉字']);
    } else if (in_progress) {
        check_poem("JJ", this_yan, this_head);
    } else {
        send_poem("JJ", this_yan, this_head);
        last_yan = this_yan;
        last_head = this_head;
        last_type = "JJ";
    }

}

function send_poem(this_type, this_yan, this_head) {
    var show = $('#poem_show');
    show.empty();
    var div = $('<div><img/></div>');
    div.find('img').attr('src', 'images/waiting.gif');
    show.append(div);
    show.append($('<div>正在为您创作...</div>'));
    var apiurl = 'sendPoem';
    $(".xzw_starSys").hide();
    $("#div_share").hide();
    $("#kongbai").css("height", "30px");
    $.ajax({
        url: apiurl,
        method: 'POST',
        data: { type: this_type, yan: this_yan, keyword: this_head, user_id: user_id },
        success: function(data) {
            if (data == "mgc") {
                show_strings(['该主题词无法成诗', '请重新选择主题词']);
                return;
            }
            in_progress = true;
            var show = $('#poem_show');
            if (Number(data) < 0) {
                data = '0';
            }
            show.append($('<div>还有' + data + '首排队...</div>'));
            timeid = window.setInterval(function() {
                check_poem(this_type, this_yan, this_head);
            }, 1500);
        },
        error: function(e) {
            show_strings(['服务器错误', '请稍候再试']);
            // star_show();
        },
    });
}


function check_poem(this_type, this_yan, this_head) {
    apiurl = "getPoem"
    $.ajax({
        url: apiurl,
        method: 'POST',
        data: { type: this_type, yan: this_yan, keyword: this_head, user_id: user_id },
        success: function(data) {
            last_poem = data;
            var ans = eval('(' + data + ')');
            var show = $('#poem_show');
            show.empty();
            if (ans.code == '0') {
                var div = $('<div><img/></div>');
                div.find('img').attr('src', '/images/waiting.gif');
                show.append(div);
                show.append($('<div>正在为您创作...</div>'));
                if (ans['content'] != '0') {
                    show.append($('<div>还有' + ans['content'] + '首排队...</div>'));
                }
            } else {
                var tmp_poem = ans.content;
                // console.log(ans);
                if (this_type == "JJJ") {
                    show_strings_chuchu(tmp_poem, ans.source);
                } else {
                    show_strings(tmp_poem);
                }
                if (this_type == "JJ") {
                    this_type = ans.type
                    if (ans.type == 0) {
                        if (is_pc) {
                            $("#test").attr('title', 'yxy ' + ans.state);
                            // $('.mytooltip1').tooltipster('content', 'yxy');
                        } else {
                            $('.mytooltip1').tooltipster('content', 'yxy ' + ans.state);
                        }

                    } else if (ans.type == 1) {
                        if (is_pc) {
                            $("#test").attr('title', 'yc ' + ans.state);
                            // $('.mytooltip1').tooltipster('content', 'yc '+ ans.state);
                        } else {
                            $('.mytooltip1').tooltipster('content', 'yc ' + ans.state);
                        }
                    } else {
                        if (is_pc) {
                            $("#test").attr('title', 'yizhi');
                            // $('.mytooltip1').tooltipster('content', 'yc '+ ans.state);
                        } else {
                            $('.mytooltip1').tooltipster('content', 'yizhi');
                        }
                    }
                }
                window.clearInterval(timeid);
                star_show();
                in_progress = false;
            }
        },
        error: function(e) {
            window.clearInterval(timeid);
            show_strings(['服务器错误', '请稍候再试']);

        },
    });
}

function yan_clicked() {
    if ($(this).hasClass('checked'))
        return;
    if (in_progress) {
        // show_strings(['不要着急，', '您的上一首诗马上就好']);
        return;
    }
    $('.yan_selector').removeClass('checked');
    // console.log($('#yan5').src);
    $('.yan5').attr('src', "/images/yan5.png")
    $('.yan7').attr('src', "/images/yan7.png")
    $(this).addClass('checked');
    $(this).attr('src', "/images/yan" + $(this).attr('yan') + "_checked" + ".png");
}

function random_question() {
    var all_questions = ['清华大学', '自强不息', '天地人', '月光', '新春', '荷塘', '友人', '离别'];
    while (1) {
        var r = Math.floor(Math.random() * all_questions.length);
        if ($('#user_input')[0].value != all_questions[r]) {
            $('#user_input')[0].value = all_questions[r];
            break;
        }
    }
    $('#user_input').focus();
}

function random_question2() {
    var all_questions = ['清华大学', '自强不息', '天地人', '月光', '新春', '荷塘', '友人', '离别'];
    while (1) {
        var r = Math.floor(Math.random() * all_questions.length);
        if ($('#user_input2')[0].value != all_questions[r]) {
            $('#user_input2')[0].value = all_questions[r];
            break;
        }
    }
    $('#user_input2').focus();
}

function random_question3() {
    var all_questions = ['清华大学', '自强不息'];
    while (1) {
        var r = Math.floor(Math.random() * all_questions.length);
        if ($('#user_input3')[0].value != all_questions[r]) {
            $('#user_input3')[0].value = all_questions[r];
            break;
        }
    }
    $('#user_input3').focus();
}

function show_strings(v) {
    var show = $('#poem_show');
    show.css("width", "260px");
    show.css("left", "245px");
    show.empty();
    var max_length = 0;
    for (var i = 0; i < v.length; i++) {
        if (v[i].length > max_length)
            max_length = length;
    }
    for (var i = 0; i < v.length; i++) {
        var tr = $('<tr></tr>');
        var s = v[i];
        for (var j = 0; j < s.length; j++) {
            var td = $('<td></td>');
            td.text(s[j]);
            tr.append(td);
        }
        show.append(tr);
    }
}

function show_strings_chuchu(v, vv) {
    var show = $('#poem_show');
    show.empty();
    show.css("width", "310px");
    show.css("left", "220px");
    var max_length = 0;
    for (var i = 0; i < v.length; i++) {
        if (v[i].length > max_length)
            max_length = length;
    }
    for (var i = 0; i < v.length; i++) {
        var tr = $('<tr></tr>');
        var s = v[i];
        // tr.append($('<td>&nbsp;</td>'));
        // tr.append($('<td>&nbsp;</td>'));
        tr.append($('<td><img src="images/kongbai.png" width="40px"></img></td>'));
        for (var j = 0; j < s.length; j++) {
            var td = $('<td></td>');
            td.text(s[j]);
            tr.append(td);
        }
        if (i == 0) {
            // tr.append($('<td>&nbsp;</td>'));
            // tr.append($('<td>&nbsp;</td>'));
            tr.append($('<td><img src="images/kongbai.png" width="40px"></img></td>'));
        } else {
            if (is_pc) {
                tr.append('<td class="hint--right hint--info" data-hint="' + vv[i] + '"><img src="images/chuchu.png" width="40px" style="margin-bottom: 10px;"></img></td>')
            } else {
                tr.append('<td><img class="mytooltip" title="' + vv[i] + '" src="images/chuchu.png" width="40px" style="margin-bottom: 10px;"></img></td>')
            }
        }
        show.append(tr);
        $('.mytooltip').tooltipster({ trigger: "click" });
    }
}

function star_show() {
    $("#kongbai").css("height", "10px");
    $(".showb").css("width", 0);
    $(".description").text(" ");
    $("#star_title").text("请对本首诗打分");
    star_has = false;
    descriptionTemp = " ";
    $(".xzw_starSys").show();
    $("#div_share").show();
    // console.log(123);
}

function star_init() {
    var stepW = 30;
    var description = new Array("不堪卒读", "初识文墨", "差强人意", "文从字顺", "妙笔生花");
    // var description = new Array("写的什么鬼！","还能看吧。。。","唉哟不错哦～","神作神作！","给大佬递茶(>_<)");
    // var description = new Array("写得太差","水平一般","质量不错","堪称好诗","千古绝句");
    var stars = $(".stars > li");
    var descriptionTemp;
    var option = $(".option");
    $(".showb").css("width", 0);
    stars.each(function(i) {
        $(stars[i]).click(function(e) {
            var n = i + 1;
            if (star_has) {
                $("#star_title").text("已完成打分，请不要重复打分！");
                return;
            }
            $(".showb").css({ "width": stepW * n });
            descriptionTemp = description[i];
            $(this).find('a').blur();
            $.DialogByZ.Confirm({
                Title: "",
                Content: "您对本首诗的评价是</br>" + n + "星</br>" + descriptionTemp,
                FunL: function() {
                    $.DialogByZ.Close();
                    $.ajax({
                        url: "/sendstar",
                        method: 'POST',
                        data: { star: n, user_id: user_id },
                        success: function(data) {
                            if (data == "1") {
                                $("#star_title").text("已完成打分，非常感谢！");
                                star_has = true;
                            } else {
                                $("#star_title").text("打分失败，请重新打分！");
                                $(".showb").css("width", 0);
                                $(".description").text(" ");
                                descriptionTemp = " ";
                            }
                        },
                        error: function(e) {
                            $("#star_title").text("打分失败，请重新打分！");
                            $(".showb").css("width", 0);
                            $(".description").text(" ");
                            descriptionTemp = " ";
                        },
                    });
                },
                FunR: function() {
                    $.DialogByZ.Close();
                    $("#star_title").text("请重新打分！");
                }
            });
            return stopDefault(e);
            return descriptionTemp;
        });
    });
    stars.each(function(i) {
        $(stars[i]).hover(
            function() {
                $(".description").text(description[i]);
                // option.find(".option-con:eq(" + $(this).index() + ")").show().siblings().hide();
            },
            function() {
                if (descriptionTemp != null) {
                    $(".description").text(descriptionTemp);
                } else {
                    $(".description").text(" ");
                    // option.find(".option-con").hide();
                    // $(".prompt").show();
                }


            }
        );
    });
}

function stopDefault(e) {
    if (e && e.preventDefault)
        e.preventDefault();
    else
        window.event.returnValue = false;
    return false;
};
