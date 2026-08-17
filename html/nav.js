document.write(`
<script src="https://code.jquery.com/jquery-3.7.1.min.js"></script>
<style>
.shared-nav {
    background: white;
    padding: 15px 20px;
    border-radius: 50px;
    box-shadow: 0 8px 15px rgba(139, 35, 35, 0.12);
    margin: 20px auto 40px;
    max-width: 1000px;
    display: flex;
    flex-wrap: wrap;
    justify-content: center;
    gap: 15px;
    border: 1px solid rgba(205, 168, 95, 0.3);
    z-index: 1000;
    position: relative;
}
.shared-nav a {
    text-decoration: none;
    color: #333;
    padding: 8px 16px;
    border-radius: 30px;
    font-weight: bold;
    transition: all 0.3s ease;
    font-size: 0.95em;
}
.shared-nav span.divider {
    display: none;
}
.shared-nav a:hover, .shared-nav a.active {
    background-color: #8b2323;
    color: white;
    transform: translateY(-2px);
    box-shadow: 0 4px 8px rgba(139, 35, 35, 0.3);
}

/* 顶部附加工具栏样式 */
#top-toolbar {
    text-align: right;
    font-size: 14px;
    margin-bottom: 10px;
    color: #8b2323;
    font-weight: bold;
}
#back-to-top {
    position: fixed;
    bottom: 30px;
    right: 30px;
    background: #8b2323;
    color: #fff;
    padding: 10px 15px;
    border-radius: 5px;
    cursor: pointer;
    display: none;
    z-index: 9999;
}
</style>
<div id="top-toolbar">
    <span id="countdown-timer"></span>
</div>
<nav class="shared-nav" id="shared-nav-container">
    <a href="index.html">首页</a> <span class="divider">|</span>
    <a href="intro.html">非遗概述</a> <span class="divider">|</span>
    <a href="craft.html">传统工艺</a> <span class="divider">|</span>
    <a href="music.html">传统音乐</a> <span class="divider">|</span>
    <a href="dance.html">传统舞蹈</a> <span class="divider">|</span>
    <a href="opera.html">传统戏曲</a> <span class="divider">|</span>
    <a href="food.html">美食技艺</a> <span class="divider">|</span>
    <a href="festival.html">传统节日</a> <span class="divider">|</span>
    <a href="inherit.html">传承保护</a> <span class="divider">|</span>
    <a href="form.html">意见反馈</a>
</nav>
<div id="back-to-top">返回顶部 ▲</div>
`);

// 仅使用jQuery代码，禁止原生JavaScript逻辑操作
$(document).ready(function() {
    // 动态高亮当前页面的导航项
    var currentHtml = location.pathname.split('/').pop() || 'index.html';
    $('.shared-nav a').each(function() {
        if ($(this).attr('href') === currentHtml) {
            $(this).addClass('active');
        } else {
            $(this).removeClass('active');
        }
    });

    // 功能1：系统时间展示（已被移除以避免页面多处重复显示时间）

    // 功能2：倒计时功能（到下一个文化遗产日，每年6月第二个星期六，为演示简化为2026农历端午节 倒计时）
    var targetDate = new Date("2026/06/19 00:00:00").getTime();
    setInterval(function() {
        var now = new Date().getTime();
        var distance = targetDate - now;
        if(distance > 0) {
            var days = Math.floor(distance / (1000 * 60 * 60 * 24));
            var hours = Math.floor((distance % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
            var mins = Math.floor((distance % (1000 * 60 * 60)) / (1000 * 60));
            $('#countdown-timer').text("距离2026端午节还有：" + days + "天" + hours + "时" + mins + "分");
        } else {
            $('#countdown-timer').text("端午佳节，安康！");
        }
    }, 60000); // 每分钟更新

    // 功能3：各类动态页面特效 - 页面加载动画、滚动特效及返回顶部
    $('body').hide().fadeIn(800);
    
    $(window).scroll(function() {
        if ($(this).scrollTop() > 300) {
            $('#back-to-top').fadeIn();
        } else {
            $('#back-to-top').fadeOut();
        }
    });
    
    $('#back-to-top').click(function() {
        $('html, body').animate({scrollTop: 0}, 600);
        return false;
    });
    
    // 图片悬停抖动特效
    $('img').hover(function(){
        $(this).stop().animate({opacity: 0.8}, 200);
    }, function(){
        $(this).stop().animate({opacity: 1}, 200);
    });

    // 功能4：AJAX交互 - 随机获取名言并在页脚展示
    var $footer = $('footer');
    if ($footer.length > 0) {
        $footer.append('<p id="ajax-quote" style="color:var(--primary-color);font-weight:bold;margin-top:10px;">正在加载每日格言...</p>');
        $.ajax({
            url: "https://v1.hitokoto.cn/?c=i", // 诗词类
            type: "GET",
            dataType: "json",
            success: function(data) {
                $('#ajax-quote').text("『 " + data.hitokoto + " 』 —— " + (data.from || "佚名")).hide().fadeIn(1500);
            },
            error: function() {
                $('#ajax-quote').text("传承不息，薪火相传。");
            }
        });
    }
});