//star
$(document).ready(init);
var user_id = null;
var last_head = null;
var last_yan = null;
var in_progress = false;
var timeid = null;
var star_has = false;
var is_pc = true;


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
    star_init();
    $('.mytooltip').tooltipster({trigger:"click", maxWidth:500});
    $('.type_selector').click(function() {
        if (in_progress)
            return;
        $('.type_selector').removeClass('checked');
        $("#jiju").attr('src', "images/jiju.png");
        $("#jueju").attr('src', "images/jueju.png");
        $("#cangtou").attr('src', "images/cangtou.png");
        $(this).addClass('checked');
        $(this).attr('src', "images/" + $(this).attr('id') + "_checked.png");
        var panel_name = $(this).attr('panel-toggle');
        $('.option-panel').hide();
        $('.option-panel.' + panel_name).show();
        $('.yan_selector').removeClass('checked');
        $('.action_selector').removeClass('checked');
        $('.action_selector.' + panel_name).addClass('checked');
        $('.action_selector.' + panel_name).attr('src', "images/yan7_checked.png");
        // console.log($('.action_selector'));
        // console.log($('img#yan7'));
        $('.yan5').attr('src', "images/yan5.png")

    });
    $('#button_yes').click(update);
    $('#button_yes2').click(update2);
    $('#button_yes3').click(update3);
    $('.yan_selector').click(yan_clicked);
    // $('#random_button').click(random_question);
    // $('#random_button2').click(random_question2);
    // $('#random_button3').click(random_question3);
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
    if (/Android|webOS|iPhone|iPod|BlackBerry/i.test(navigator.userAgent)) {
        is_pc = false;
    }
    console.log(is_pc);
}

function update() {
    if (!$('#user_input')[0].value)
        random_question();
    var this_head = $('#user_input')[0].value || $('#user_input').attr('placeholder');
    var this_yan = null;
    this_head = this_head.trim();
    if ($('#yan5_JJ').hasClass('checked')) this_yan = 5;
    if ($('#yan7_JJ').hasClass('checked')) this_yan = 7;
    var all_chinese = true;
    if (this_head.length > 7) {
        show_strings(['长度不能大于7']);
        return;
    }
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
        last_head = this_head;
        last_yan = this_yan;
    }

}

function update2() {
    if (!$('#user_input2')[0].value)
        random_question();
    var this_head = $('#user_input2')[0].value || $('#user_input2').attr('placeholder');
    var this_yan = null;
    this_head = this_head.trim();
    if ($('#yan5_JJJ').hasClass('checked')) this_yan = 5;
    if ($('#yan7_JJJ').hasClass('checked')) this_yan = 7;
    var all_chinese = true;
    if (this_head.length != this_yan) {
        if (this_yan == 5)
            show_strings(['五言诗长度需等于5']);
        else if (this_yan == 7)
            show_strings(['七言诗长度需等于7']);
        return;
    }
    for (var i = 0; i < this_head.length; i++) {
        if (encodeURI(this_head[i]).length != 9)
            all_chinese = false;
    }
    if (!all_chinese) {
        show_strings(['只能输入汉字']);
    } else if (in_progress) {
        check_poem("JJJ", this_yan, this_head);
    } else {
        send_poem("JJJ", this_yan, this_head);
        last_head = this_head;
        last_yan = this_yan;
    }

}

function update3() {
    if (!$('#user_input3')[0].value)
        random_question3();
    var this_head = $('#user_input3')[0].value || $('#user_input3').attr('placeholder');
    var this_yan = null;
    this_head = this_head.trim();
    if ($('#yan5_CT').hasClass('checked')) this_yan = 5;
    if ($('#yan7_CT').hasClass('checked')) this_yan = 7;
    var all_chinese = true;
    if (this_head.length != 4) {
        show_strings(['长度必须为4']);
        return;
    }
    for (var i = 0; i < this_head.length; i++) {
        if (encodeURI(this_head[i]).length != 9)
            all_chinese = false;
    }
    if (!all_chinese) {
        show_strings(['只能输入汉字']);
    } else if (in_progress) {
        check_poem("CT", this_yan, this_head);
    } else {
        send_poem("CT", this_yan, this_head);
        last_head = this_head;
        last_yan = this_yan;
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
    $("#kongbai").css("height", "30px");
    $.ajax({
        url: apiurl,
        method: 'POST',
        data: { type: this_type, yan: this_yan, keyword: this_head, user_id: user_id },
        success: function(data) {
            in_progress = true;
            var show = $('#poem_show');
            show.append($('<div>还有' + data + '首排队...</div>'));
            timeid = window.setInterval(function() {
                check_poem(this_type, this_yan, this_head);
            }, 1500);
        },
        error: function(e) {
            show_strings_chuchu(['服务器错误', '请稍候再试']);
            star_show();
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
            var ans = eval('(' + data + ')');
            var show = $('#poem_show');
            show.empty();
            if (ans.code == '0') {
                var div = $('<div><img/></div>');
                div.find('img').attr('src', 'images/waiting.gif');
                show.append(div);
                show.append($('<div>正在为您创作...</div>'));
                if (ans['content'] != '0') {
                    show.append($('<div>还有' + ans['content'] + '首排队...</div>'));
                }
            } else {
                last_poem = ans.content;
                // console.log(last_poem);
                if (this_type == "JJJ") {
                    show_strings_chuchu(last_poem, ans.source);
                } else {
                    show_strings(last_poem);
                }
                window.clearInterval(timeid);
                star_show();
                in_progress = false;
            }
        },
        error: function(e) {
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
    $('.yan5').attr('src', "images/yan5.png")
    $('.yan7').attr('src', "images/yan7.png")
    $(this).addClass('checked');
    $(this).attr('src', "images/yan" + $(this).attr('yan') + "_checked" + ".png");
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
        tr.append($('<td><img src="images/kongbai.png" width="40px"></img></td>'));
        // tr.append($('<td>&nbsp;</td>'));    
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
            // tr.append('<td class="hint--right hint--info" data-hint="'+vv[i]+'"><img src="images/chuchu.png" height="15px" weight="20px"></img></td>')    
            if (is_pc) {
                tr.append('<td class="hint--right hint--info" data-hint="123"><img src="images/chuchu.png" width="40px" style="margin-bottom: 10px;"></img></td>')
            } else {
                tr.append('<td><img class="mytooltip" title="123" src="images/chuchu.png" width="40px" style="margin-bottom: 10px;"></img></td>')
            }

        }
        show.append(tr);
    }
    $('.mytooltip').tooltipster({trigger:"click"});
}

function star_show() {
    $("#kongbai").css("height", "10px");
    $(".showb").css("width", 0);
    $(".description").text(" ");
    $("#star_title").text("请对本首诗打分");
    star_has = false;
    descriptionTemp = " ";
    $(".xzw_starSys").show();
    // console.log(123);
}

function star_init() {
    var stepW = 30;
    var description = new Array("胡言乱语", "差强人意", "上乘之作", "妙笔生花", "神来之笔");
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