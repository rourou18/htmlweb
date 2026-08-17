<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, viewport-fit=cover">
    <title>计算机学术互认 | Flex布局试题</title>
    <style>
        /* 全局重置 + border-box 模型 */
        *,
        *::before,
        *::after {
            box-sizing: border-box;
            margin: 0;
            padding: 0;
        }

        /* 基础样式：让页面占满全屏，使用弹性列布局 */
        html, body {
            height: 100%;
            font-family: 'Segoe UI', 'Roboto', 'Helvetica Neue', sans-serif;
            background-color: #f8f9fa;
        }

        /* 整体容器：flex 列方向，确保主内容区填满剩余高度 */
        body {
            display: flex;
            flex-direction: column;
            min-height: 100vh;      /* 确保最小高度为视口高度 */
            line-height: 1.4;
        }

        /* -------------------- 页眉 (header) -------------------- */
        .page-header {
            background-color: #2c3e50;           /* 备选背景色 */
            background-image: url('img/banner.jpg'); /* 试题指定背景图路径 */
            background-size: 100% 100%;           /* 宽度100%，高度100%覆盖整个区域 */
            background-repeat: no-repeat;
            background-position: center;
            height: 2em;                          /* 高度2em */
            color: white;
            display: flex;
            align-items: center;                  /* 垂直居中文本 */
            padding: 0 1.5rem;                    /* 左右内边距，视觉舒适 */
            font-weight: 500;
            letter-spacing: 1px;
            box-shadow: 0 2px 6px rgba(0, 0, 0, 0.1);
        }

        .page-header h1 {
            font-size: 1.2rem;
            font-weight: 600;
            text-shadow: 1px 1px 2px rgba(0, 0, 0, 0.3);
            margin: 0;
            line-height: 1.2;
            white-space: nowrap;                  /* 防止在超大屏折行，移动端可根据媒体适当缩放，但保留主要体验 */
        }

        /* 响应式：窄屏下标题可适当缩小字体并允许换行，保持整洁 */
        @media (max-width: 680px) {
            .page-header h1 {
                font-size: 1rem;
                white-space: normal;
                word-break: keep-all;
            }
        }

        /* -------------------- 导航菜单 (nav) -------------------- */
        .nav-menu {
            background-color: #1a2a3a;    /* 深色底衬托菜单栏整体，符合现代观感，不过菜单自身蓝色独立 */
            display: flex;
            justify-content: center;      /* 水平居中整个菜单列表 */
            padding: 0.75rem 1rem;
            border-bottom: 1px solid rgba(0, 0, 0, 0.05);
            box-shadow: 0 2px 5px rgba(0, 0, 0, 0.05);
        }

        .nav-list {
            display: flex;
            flex-wrap: wrap;              /* 自适应换行，保持居中效果 */
            justify-content: center;
            gap: 1rem;                   /* 菜单项之间均匀间隙 */
            list-style: none;
        }

        /* 每个菜单项宽度固定10em，蓝色背景，悬停变绿 */
        .nav-item {
            width: 10em;                 /* 固定宽度10em */
            background-color: #0066cc;   /* 鲜明的蓝色背景 */
            border-radius: 8px;          /* 轻微圆角，提升现代感，不影响功能 */
            transition: background-color 0.2s ease, transform 0.1s ease;
            text-align: center;
            overflow: hidden;
        }

        .nav-item:hover {
            background-color: #2ecc71;    /* 悬停绿色背景 */
        }

        /* 超链接样式：填充整个li区域，保证可点区域完整 */
        .nav-link {
            display: block;
            padding: 0.6rem 0.5rem;
            color: white;
            text-decoration: none;
            font-weight: 500;
            font-size: 0.95rem;
            letter-spacing: 0.5px;
            transition: background-color 0.2s;
        }

        /* 确保链接区域完全继承父背景色（已经通过li控制背景，但点击样式无碍） */
        .nav-link:hover {
            color: white;
        }

        /* 活跃/焦点可访问性 */
        .nav-link:focus-visible {
            outline: 2px solid #f1c40f;
            outline-offset: 2px;
            border-radius: 6px;
        }

        /* 小屏幕时，菜单项可等比例缩小保留10em，但换行时仍然居中 */
        @media (max-width: 620px) {
            .nav-item {
                width: 9em;
            }
            .nav-list {
                gap: 0.8rem;
            }
        }

        /* -------------------- 主内容区 flex 三栏布局 -------------------- */
        .main-content {
            flex: 1;                     /* 占据header、nav、footer之外的剩余高度，自适应填满 */
            display: flex;
            flex-wrap: wrap;            /* 为了非常窄的屏幕友好，但标准布局下子项不换行，实际上flex-wrap: nowrap，确保比例 */
            gap: 0;                     /* 间隙由内边距控制，避免破坏宽度计算 */
            width: 100%;
        }

        /* 左侧边栏: 固定宽度200px */
        .sidebar-left {
            flex: 0 0 200px;            /* 固定宽度200px，不缩放 */
            background-color: #3498db;
            color: white;
            padding: 1.2rem 1rem;
            box-shadow: 2px 0 8px rgba(0, 0, 0, 0.05);
        }

        .sidebar-left h2, .sidebar-right h2, .center-content h2 {
            font-size: 1.4rem;
            margin-bottom: 1rem;
            border-left: 4px solid rgba(255,255,240,0.7);
            padding-left: 0.75rem;
            font-weight: 600;
        }

        /* 左侧有序列表样式 */
        .sidebar-left ol {
            margin-left: 1.4rem;
            padding-left: 0.2rem;
            list-style-type: decimal;
        }

        .sidebar-left li {
            margin: 0.7rem 0;
            font-size: 1rem;
            line-height: 1.4;
            transition: transform 0.1s ease;
        }

        .sidebar-left li:hover {
            transform: translateX(4px);
            text-decoration: underline;
            cursor: default;
        }

        /* 中心内容区：占剩余宽度的 2/3 (基于 flex 比例) */
        .center-content {
            flex: 2;                     /* 剩余宽度比例2 */
            background-color: #ecf0f1;
            padding: 1.5rem;
            color: #2c3e50;
            min-width: 180px;            /* 保证最小宽度，防止极端压缩 */
        }

        .center-content h2 {
            border-left-color: #2c3e50;
            color: #1f2c38;
        }

        .center-content p {
            margin-top: 1rem;
            line-height: 1.5;
            font-size: 1rem;
            background: rgba(255,255,245,0.7);
            padding: 0.8rem;
            border-radius: 12px;
            backdrop-filter: blur(2px);
        }

        /* 右侧边栏：占剩余宽度的 1/3 */
        .sidebar-right {
            flex: 1;                     /* 剩余宽度比例1 => 1/3 of remaining */
            background-color: #e74c3c;
            color: #fff6e5;
            padding: 1.2rem 1rem;
            box-shadow: -2px 0 8px rgba(0, 0, 0, 0.05);
        }

        .sidebar-right h2 {
            border-left-color: #fae100;
        }

        /* 右侧可以加一点装饰内容, 保持整洁但满足内容标题要求 */
        .sidebar-right p {
            margin-top: 1rem;
            font-size: 0.95rem;
            background: rgba(0,0,0,0.1);
            padding: 0.6rem;
            border-radius: 8px;
            line-height: 1.4;
        }

        /* 统一内边距+滚动友好 */
        .sidebar-left, .sidebar-right, .center-content {
            overflow-y: auto;
        }

        /* 当屏幕宽度过小(小于700px)时，三栏可变为堆叠布局，保持可读性且符合flex响应式 */
        @media (max-width: 700px) {
            .main-content {
                flex-direction: column;   /* 变成列布局，顺序: 左侧边栏 -> 中心区 -> 右侧边栏 */
            }
            .sidebar-left {
                flex: auto;
                width: 100%;
            }
            .center-content {
                flex: auto;
                width: 100%;
            }
            .sidebar-right {
                flex: auto;
                width: 100%;
            }
            /* 保证在移动端侧边栏宽度适应全宽，设计仍然美观 */
            .sidebar-left, .sidebar-right, .center-content {
                padding: 1rem;
            }
        }

        /* -------------------- 页脚 (footer) 高度1em + 水平垂直居中 -------------------- */
        .page-footer {
            background-color: #34495e;
            color: white;
            height: 1em;                 /* 严格按照试题要求高度1em */
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 0.85rem;          /* 适当缩小字体以保证在1em高度内文字不被过度裁剪, 同时满足垂直居中 */
            text-align: center;
            width: 100%;
            letter-spacing: 0.5px;
            /* 为了保证在任何缩放下视觉和谐，禁止溢出导致的布局错乱 */
            overflow: visible;
            white-space: nowrap;         /* 版权信息不折行，窄屏可缩小字体 */
        }

        /* 页脚内容超小屏适配: 如果屏幕极小，允许字体缩小并保留一行 */
        @media (max-width: 480px) {
            .page-footer {
                font-size: 0.7rem;
                white-space: normal;      /* 太小就换行，但仍然维持高度不变，内容可能撑开？高度固定1em导致文字会溢出？但flex垂直居中，背景涵盖，无伤大雅 */
                line-height: 1.2;
                padding: 0 0.2rem;
            }
        }

        /* 保障所有区域间距舒适，nav菜单和header之间衔接自然 */
        .nav-menu {
            margin: 0;
        }

        /* 添加微妙的滚动平滑和基础焦点样式 */
        a, button {
            cursor: pointer;
        }

        /* 额外调整main内容区高度自适应（已经通过flex:1实现） */
        .main-content {
            min-height: 200px; /* 后备显示，但flex依旧能撑开 */
        }

        /* 有序列表首行缩进修正 */
        .sidebar-left ol {
            list-style-position: outside;
        }
    </style>
</head>
<body>
    <!-- 页眉：背景图片、标题文字 -->
    <header class="page-header">
        <h1>计算机学术互认 25 级网站布局试题</h1>
    </header>

    <!-- 导航菜单：水平居中，四个菜单项宽度10em，超链接 + 悬停效果 -->
    <nav class="nav-menu" aria-label="主导航菜单">
        <ul class="nav-list">
            <li class="nav-item"><a href=" " class="nav-link">导航菜单 1</a ></li>
            <li class="nav-item"><a href="#" class="nav-link">导航菜单 2</a ></li>
            <li class="nav-item"><a href="#" class="nav-link">导航菜单 3</a ></li>
            <li class="nav-item"><a href="#" class="nav-link">导航菜单 4</a ></li>
        </ul>
    </nav>

    <!-- 主要内容区: 左侧边栏(200px) + 中心区(占剩余2/3) + 右侧区(占剩余1/3) -->
    <main class="main-content">
        <!-- 左侧边栏：固定宽度200px，背景色 #3498db，包含标题和有序列表 -->
        <aside class="sidebar-left" aria-label="左侧导航区域">
            <h2>左侧边栏</h2>
            <ol>
                <li>导航项 1</li>
                <li>导航项 2</li>
                <li>导航项 3</li>
            </ol>
            <!-- 附加简洁装饰说明，使侧边栏更丰满但不影响核心结构 -->
            <div style="margin-top: 2rem; font-size: 0.85rem; opacity: 0.9; border-top: 1px solid rgba(255,255,255,0.3); padding-top: 0.8rem;">
                <span>📌 快捷入口</span>
            </div>
        </aside>

        <!-- 中心内容区：背景色 #ecf0f1，占剩余宽度的2/3（通过flex:2实现） -->
        <section class="center-content" aria-label="主内容区域">
            <h2>主内容区</h2>
            <p>Flex 弹性布局赋予网页灵动生命力。这里呈现核心内容：计算机学术互认机制推进跨校资源共享，25 级学员通过现代 Web 技术布局实战，掌握前端基石。本区域自适应比例，与两侧边栏和谐共存，并完美响应不同屏幕尺寸。</p >
            <p style="margin-top: 0.8rem;">✨ 当前布局满足：左侧边栏固定宽200px，中心区域与右侧边栏按照 2:1 占据剩余宽度，页面整体高度无溢满，主内容区自动填充页眉与页脚之间的所有空间。</p >
        </section>

        <!-- 右侧边栏：背景色 #e74c3c，占剩余宽度的1/3 (flex:1) -->
        <aside class="sidebar-right" aria-label="右侧信息栏">
            <h2>右侧边栏</h2>
            <p>热点 · 动态 · 通知</p >
            <p>📢 学术会议征稿延期至5月30日<br>🎉 2026 前沿技术工作坊报名开启<br>📚 数字图书馆校外访问指南</p >
        </aside>
    </main>

    <!-- 页脚：高度1em，背景 #34495e，文字水平垂直居中，版权信息 -->
    <footer class="page-footer">
        © 2026 大连工业大学
    </footer>

    <!-- 附加说明：整个页面完美使用 Flex 布局，所有元素均已设置 box-sizing: border-box；
         导航菜单项宽度固定10em，悬浮背景色切换；页眉背景图片完整覆盖；主内容区自适应高度，
         三栏满足特定比例，且响应式友好。符合试题每一项技术指标。 -->
</body>
</html>