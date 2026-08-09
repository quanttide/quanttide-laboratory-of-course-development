# 创新原型 UI 设计系统

> 提取自 `innovation-prototype-latest.html`，量潮课堂 LMS 全平台原型。
> 喂给 AI 即可复刻整套 UI——包含所有色值、组件、布局、动效。
>
> 提取日期：2026-08-09

---

## 一、页面架构总览

原型包含 **5 个视图 + 1 个全屏表单页**：

| 视图 ID | 用途 | 视觉风格 |
|---------|------|---------|
| `#view-courses` | 课程列表首页 | 海平线 v5：海景图底 + 白渐变遮罩 + 衬线 Hero |
| `#view-front` | 生产实习课程内页 | 海景底 + 白雾遮罩 + 磨砂大白卡片 |
| `#view-generic` | 通用课程内页（课程1-4） | Hero 蓝渐变卡片 + 模块内容海平线风格 |
| `#view-back` | 后台 LMS 管理 | 纯色底 + 220px 侧边栏 + 卡片/表格 |
| `#form-page` | 立项申请表问卷预览 | 左右分栏：60%表单 + 40%装饰圆 |
| AppBar | 全局顶栏 | 透明底 + 潮汐线分隔 |

---

## 二、Design Tokens（CSS 变量）

### 2.1 全局 :root 变量（海岸主题 · 课程内页 & 后台）

```css
:root {
  --brand: #1677ff;
  --brand-soft: #e8f4ff;
  --brand-muted: #b8d8ff;
  --bg: #f8fafe;
  --surface: #f5f9fc;
  --text: #1a2332;
  --text-2: #556678;
  --text-3: #8899aa;
  --line: #e8ecf2;
  --line-light: #f2f5f8;
  --success: #22c55e;
  --success-soft: #f0fdf4;
  --radius: 14px;
  --radius-sm: 8px;
  --radius-lg: 18px;
  --radius-full: 9999px;
  --font: -apple-system, BlinkMacSystemFont, "PingFang SC", "Microsoft YaHei", "Noto Sans SC", sans-serif;
}
```

### 2.2 课程列表页局部变量（海平线 v5）

```css
#view-courses {
  --ocean-500: #4AA8E8;
  --ocean-400: #75BCEB;
  --ocean-300: #A8D4F0;
  --ocean-200: #CDE7F6;
  --ink-900: #10182B;
  --ink-700: #43516A;
  --ink-400: #94A0B3;
  --mist: #F7FBFE;
  --v3-line: rgba(148, 163, 184, 0.18);
  --font-serif: 'Noto Serif SC', 'STSong', 'Georgia', serif;
}
```

### 2.3 课程首页 v4 局部变量

```css
#view-front {
  --v4-btn: #2464BC;
  --v4-title: #3678D8;
  --v4-soft: #73B4F2;
}
```

---

## 三、完整色板速查

### 蓝色系（主品牌色）

| 色值 | 名称 | 用途 |
|------|------|------|
| `#1677ff` | brand | 默认按钮、链接、进度条 |
| `#e8f4ff` | brand-soft | hover 背景、选中态 |
| `#b8d8ff` | brand-muted | 淡化强调 |
| `#4AA8E8` | ocean-500 | 列表页主强调：激活文字、潮线起点、步骤按钮 |
| `#75BCEB` | ocean-400 | 潮线过渡段 |
| `#A8D4F0` | ocean-300 | 潮线中段 |
| `#CDE7F6` | ocean-200 | 淡蓝图标背景 |
| `#2464BC` | v4-btn | 课程首页按钮主色 |
| `#3678D8` | v4-title | 课程首页标题强调色 |
| `#73B4F2` | v4-soft | 课程首页柔和蓝 |

### 墨色系（文字）

| 色值 | 名称 | 用途 |
|------|------|------|
| `#10182B` | ink-900 | 主标题、Logo、Hero 标题 |
| `#1a2332` | text | 正文默认色 |
| `#43516A` | ink-700 | 副标题、描述 |
| `#556678` | text-2 | 次要文字 |
| `#64748B` | — | 课程首页 meta 文字 |
| `#94A0B3` | ink-400 | 辅助信息、placeholder |
| `#8899aa` | text-3 | 三级文字 |
| `#334155` | — | 模块内描述文字 |

### 底色系

| 色值 | 名称 | 用途 |
|------|------|------|
| `#f8fafe` | bg | 页面底色 |
| `#f5f9fc` | surface | 卡片/组件底色 |
| `#f7fbfe` | mist | 极淡蓝底（备用） |
| `#FFFFFF` | — | 课程首页 v4 卡片底色 |

### 状态色

| 色值 | 名称 | 用途 |
|------|------|------|
| `#22c55e` | success | 完成态圆点、badge、步骤对勾 |
| `#f0fdf4` | success-soft | 完成态背景 |
| `#F25F5C` | — | 驳回按钮色 |

### 分割线

| 色值 | 用途 |
|------|------|
| `#e8ecf2` | 标准分割线 |
| `#f2f5f8` | 浅分割线 |
| `rgba(148, 163, 184, 0.18)` | 海平线风格分割线 |

### Badge 配色

| class | 背景色 | 文字色 | 用途 |
|-------|--------|--------|------|
| `beginner` | `#e8f4ff` | `#1677ff` | 入门 |
| `intermediate` | `#ede9fe` | `#5b21b6` | 进阶 |
| `advanced` | `#fff3e0` | `#e65100` | 实战 |
| `capstone` | `#ffeaea` | `#c62828` | 微型创业 |
| `review` | `#e8f4ff` | `#1677ff` | 待审批 |
| `active-status` | `#f0fdf4` | `#22c55e` | 进行中/活跃 |
| `done` | `#f5f0ff` | `#6a1b9a` | 已完成/已验收 |
| `draft` | `#fff3e0` | `#e65100` | 草稿 |

---

## 四、字体系统

### 字体栈

```
系统无衬线（默认）:
  -apple-system, BlinkMacSystemFont, "PingFang SC", "Microsoft YaHei", "Noto Sans SC", sans-serif

衬线（Hero 专用）:
  'Noto Serif SC', 'STSong', 'Georgia', serif
```

### 字号 & 字重对照

| 场景 | 字号 | 字重 | 字体 |
|------|------|------|------|
| Hero 主标题（课程列表） | 42px | 500 | 衬线 |
| v4 Hero 标题 | 42px | 650 | 系统无衬线 |
| 页面标题（模块内） | 28px | 550-600 | 衬线 |
| 统计数字 | 30px | 700 | 系统无衬线 |
| 课程标题 h2 | 20px | 600 | 系统无衬线 |
| 步骤标题 | 15px | 550 | 系统无衬线 |
| 正文 | 14px | 400 | 系统无衬线 |
| 描述文字 | 13-14px | 400 | 系统无衬线 |
| Nav 链接 | 13px | 500 | 系统无衬线 |
| 表格文字 | 13px | 400 | 系统无衬线 |
| 辅助/元信息 | 10.5-13px | 400-600 | 系统无衬线 |
| Badge | 11-12px | 600 | 系统无衬线 |
| Eyebrow（小标签） | 10.5px | 550-600 | 系统无衬线 |
| Logo | 15px | 550 | 系统无衬线 |

### 字间距

| 场景 | letter-spacing |
|------|---------------|
| Hero 标题（衬线） | `-0.5px` |
| v4 Hero 标题 | `-0.035em` |
| Eyebrow | `2.5px` |
| 步骤编号 | `1.5px` |
| 侧边栏标签 | `1px` |
| Logo | `0.3px` |

---

## 五、间距 & 圆角

### 圆角

| Token | 值 | 用途 |
|-------|-----|------|
| `--radius-sm` | 8px | 按钮、输入框、表单元素 |
| `--radius` | 14px | 标准卡片、步骤条 |
| `--radius-lg` | 18px | Hero 卡片、表单 body 容器 |
| `--radius-full` | 9999px | Badge/Pill、进度条轨道 |
| 其他 | 4px | 步骤按钮（课程列表页） |
| 其他 | 6px | Nav 项、面包屑 |
| 其他 | 10px | v4 按钮、v4 表单输入框 |
| 其他 | 28px | v4 大白卡片 |

### 间距

| 场景 | 值 |
|------|-----|
| 页面水平内边距（桌面） | 24px |
| 页面水平内边距（移动） | 16px |
| 卡片内边距 | 36px 40px |
| v4 卡片内边距 | 44-52px 52-62px |
| 模块卡片内边距 | 20px |
| 课程卡片内边距 | 22px 28px |
| 统计卡片内边距 | 20px |
| 表格单元格内边距 | 12-13px 16px |
| 条目行内边距 | 14px 16px |
| 按钮内边距（标准） | 10px 28px |
| 按钮内边距（大） | 14px 32px |
| 按钮内边距（小） | 6px 14px |
| v4 按钮内边距 | 12px 28px |
| Nav 链接间距 | 32px |
| 卡片间距（grid gap） | 12-24px |

### 内容区最大宽度

| 页面 | max-width |
|------|----------|
| 课程列表 | 1100px |
| 课程内页（通用） | 860px |
| 课程内页（前台） | 860px |
| 后台 LMS | 无限制（flex:1） |
| 侧边栏 | 220px 固定 |

---

## 六、潮汐线（Horizon Line）—— 核心视觉符号

从左到右渐隐的水平分割线，模拟潮水进退，是量潮课堂最核心的品牌视觉元素。

### 完整潮汐线

```css
.horizon {
  height: 1px;
  border: 0;
  width: 100%;
  background: linear-gradient(90deg,
    #4AA8E8 0%,                    /* 左端：主海洋蓝，清晰 */
    #75BCEB 20%,                   /* 过渡 */
    #A8D4F0 45%,                   /* 中段：浅蓝 */
    rgba(168, 212, 240, 0.35) 68%, /* 开始消散 */
    rgba(168, 212, 240, 0.10) 88%, /* 几乎消失 */
    rgba(168, 212, 240, 0) 100%    /* 完全透明 */
  );
}
```

### 短潮汐线（模块内）

```css
.horizon-sm {
  height: 1px;
  border: 0;
  margin: 16px 0;
  width: 100%;
  background: linear-gradient(90deg,
    rgba(168, 212, 240, 0.25) 0%,
    rgba(168, 212, 240, 0.08) 50%,
    rgba(168, 212, 240, 0) 100%
  );
}
```

### 使用位置

- AppBar 下方（`#appbar-horizon`）
- Hero 与课程路径之间
- 模块卡片内（标题后、内容前、按钮前）
- 每个课程步骤内部（step-line）
- Outro 区域上方

---

## 七、背景系统

### 7.1 海浪装饰背景（全局）

固定在页面底层的装饰层，由两个部分组成：

**光晕：**
```css
position: absolute; top: -120px; left: 50%; transform: translateX(-50%);
width: 900px; height: 400px;
background: radial-gradient(ellipse 50% 50% at 50% 40%, rgba(22,119,255,.07) 0%, transparent 70%);
```

**海浪 SVG 波形：**
```html
<svg viewBox="0 0 1440 220" preserveAspectRatio="none">
  <path d="M0,70 C220,140 440,20 660,75 C880,130 1100,30 1320,70 C1380,85 1420,65 1440,55 L1440,0 L0,0 Z" fill="rgba(22,119,255,0.5)"/>
  <path d="M0,100 C280,160 560,40 840,90 C1060,130 1240,80 1440,65 L1440,0 L0,0 Z" fill="rgba(64,150,255,0.3)"/>
</svg>
```

### 7.2 课程列表页背景

**底层：** 海景摄影图 `抠图需求.webp`，`center 30% / cover no-repeat`

**上层：** 白渐变遮罩（控制海"露"多少）
```css
background: linear-gradient(180deg,
  rgba(255,255,255,0.28) 0%,   /* 顶部微透 → 看到海 */
  rgba(255,255,255,0.50) 28%,
  rgba(255,255,255,0.65) 55%,
  rgba(255,255,255,0.78) 100%   /* 底部几乎全白 */
);
```

### 7.3 课程首页 v4 背景

三层叠加：
1. **底层：** `首页.webp`，`62% center / cover no-repeat fixed`，滤镜 `saturate(0.72) hue-rotate(15deg) brightness(1.12) contrast(0.92)`
2. **中上层：** 顶部白渐变（`rgba(255,255,255,.92) → 0`，55%处完全透明）
3. **上层：** 左侧白渐变（135deg，`rgba(255,255,255,.82) → 0`，48%处完全透明）

### 7.4 模块内容页（前台 & 通用）

模块的 `module-panel` 内复用海景图 + 渐变遮罩（同 7.2），但模块卡片本身透明无边框：
```css
background: transparent; border: none; border-radius: 0;
padding: 0; box-shadow: none;
```

### 7.5 纯色底（后台 LMS）

- 页面底色：`#f8fafe`
- 卡片底色：`#f5f9fc`
- 无背景图

---

## 八、组件规范

### 8.1 AppBar（顶栏 · 海平线 v5）

```
[量潮课堂]                    [学习路径] [班级] [创新项目] [管理]
———————————————————————————————————————————————————————————————— (潮汐线)
```

- **定位：** `position: sticky; top: 0; z-index: 100`
- **背景：** 透明（`background: transparent`）
- **布局：** flex column，`padding: 16px 24px 0`
- **Logo：** 15px，weight 550，`#10182B`，letter-spacing 0.3px
- **Nav 链接：** 13px，weight 500，默认 `#94A0B3`，激活/hover `#4AA8E8`，间距 32px
- **潮汐线：** 1px 高，margin-top 15px

### 8.2 课程步骤卡片（Step Card · 列表页）

五步横向排列，`flex: 1` 等分。每步从顶部不同高度起始，形成海浪起伏：

| 步骤 | padding-top | 隐喻 |
|------|-------------|------|
| Step 1 | 80px | 海面下（深水区） |
| Step 2 | 60px | 上浮中 |
| Step 3 | 50px | 继续上浮 |
| Step 4 | 30px | 接近海面 |
| Step 5 | 10px | 海面（浅水区） |

**每步内部结构：**
```
[编号]    10.5px, weight 600, letter-spacing 1.5px
[标题]    15px, weight 550
[描述]    11.5px, ink-700, line-height 1.5
[元信息]  10.5px, ink-400
[按钮]    12px, 蓝底白字, 4px 圆角, padding 5px 14px
[潮线]    2px, 渐变, margin-top 2px
```

**交互状态：**
| 状态 | 效果 |
|------|------|
| 默认 | 编号 `#94A0B3`，标题 `#10182B`，潮线 2px 标准渐变 |
| hover | `translateY(-2px)`，编号+标题变 `#4AA8E8`，潮线 3px 更亮 |
| active | `scale(0.97)`，潮线 4px 全亮 |

### 8.3 v4 课程首页卡片（Hero Card）

大白卡片悬浮于海景背景之上：

```
┌──────────────────────────────────────────┐
│ 🏭 生产实习 · 微型创业        ← Badge   │
│                                          │
│ 量潮课堂 · 实训基地            ← 42px   │
│ 描述文字...                    ← 14px   │
│ 📚 5模块 ⏱ 2周 👤 38人        ← meta   │
│ ████░░░░░░░░░░ 20%             ← 进度条  │
│ [▶ 继续学习] [👥 组队广场]     ← 按钮   │
│                              ··点阵··    │
└──────────────────────────────────────────┘
```

**规格：**
- 宽度：`55vw`，最大 `1120px`，宽高比 `16/9`
- 背景：`#fff`
- 圆角：28px
- 阴影：`0 28px 90px rgba(35,80,120,.12)`
- 内边距：44-52px 52-62px
- 右下角点阵装饰：`radial-gradient(circle, rgba(115,180,242,.10) 1.5px, transparent 1.5px)`，10px 间距
- v4-badge：`padding: 4px 16px; border-radius: 9999px; background: rgba(54,120,216,.08); color: #3678D8; font-size: 12px; font-weight: 600`
- v4-title 强调色 `<em>`：`#3678D8`
- v4-desc strong：`#10213D`，weight 600
- v4-meta：13px，`#64748B`，flex gap 24pxwrap

### 8.4 课程 Hero 卡片（通用课程内页）

```
┌──────────────────────────────────────┐
│ 📝 知识工作 · 入门       ← Badge   │
│ 知识工作                  ← h2 28px│
│ 描述文字...               ← 14px   │
│ 📚 4阶段 ⏱ 1周 👤 56人   ← meta   │
│ ████░░░░░░░░ 50%          ← 进度条 │
│        [▶ 继续学习]                  │
└──────────────────────────────────────┘
```

**规格：**
- 背景渐变：`linear-gradient(135deg, #E3F2FD 0%, #BBDEFB 50%, #E8F5FF 100%)`
- 圆角：18px
- 内边距：40px 48px
- 右下角点阵：`radial-gradient(circle, rgba(22,119,255,.08) 1.6px, transparent 1.6px)`，10px 间距
- h2：28px，`#1a2332`
- 描述：14px，`#556678`，line-height 1.7，max-width 680px
- Meta：12px，`#8899aa`，flex gap 20px

### 8.5 模块面板（Module Panel · 海平线风格）

模块内页（#view-front 和 #view-generic 共用）：

```html
<div class="module-panel show" id="mod-m1">
  <!-- 海浪背景层 -->
  <div class="ocean-bg">
    <div class="ocean-img"></div>
    <div class="ocean-fade"></div>
  </div>
  <!-- 内容卡片：透明无边框 -->
  <div class="card">
    <h2>📖 一、模块标题</h2>
    <p class="subtitle">模块描述</p>
    <hr class="horizon">
    <!-- 课时列表 -->
    <div class="lesson-item"><span class="ldot"></span>课时名称<span class="duration">阅读 10 min</span></div>
    <hr class="horizon-sm">
    <!-- 操作按钮 -->
    <button class="btn btn-filled">→ 下一模块</button>
  </div>
</div>
```

**规则：**
- 卡片本身：透明底、无边框、无圆角、无阴影、无内边距
- h2：衬线体，28px，weight 550，`#10182B`，letter-spacing `-0.4px`
- subtitle：14px，`#64748B`，margin-bottom 34px
- 潮汐线间距：28px（horizon）/ 16px（horizon-sm）

### 8.6 课时条目行（Lesson Item）

```
[●]  课时名称                         阅读 10 min
───────────────────────────────────────────────── (浅潮线分隔)
```

- 布局：flex，`align-items: center`，gap 13px
- 内边距：16px 0
- 分隔线：`border-bottom: 1px solid rgba(148, 163, 184, 0.10)`
- 最后一项无分隔线
- hover：背景 `rgba(74, 168, 232, 0.03)`，左移 `padding-left: 10px`
- ldot（圆点）：8px，`#73B4F2`，opacity 0.7；完成态 `.done` → `#4AA8E8` opacity 1
- duration：12px，`#94A0B3`，weight 500，`margin-left: auto`

### 8.7 按钮系统

#### 海岸主题按钮（课程内页 & 后台）

| class | 背景 | 文字色 | 边框 | 阴影 |
|-------|------|--------|------|------|
| `.btn-filled` | `linear-gradient(135deg, #1677ff, #4096ff)` | `#fff` | 无 | `0 2px 8px rgba(22,119,255,.18)` |
| `.btn-outlined` | transparent | `#1677ff` | `1.5px solid #e8ecf2` | 无 |
| `.btn-text` | transparent | `#1677ff` | 无 | 无 |

- 标准：padding `10px 28px`，14px，weight 600，border-radius 8px
- 大：padding `14px 32px`，16px
- 小：padding `6px 14px`，12px
- hover filled：阴影加深 + `translateY(-1px)`
- hover outlined/text：背景 `#e8f4ff`

#### 海平线按钮（模块内页）

```css
.btn-filled {
  background: #2464BC;       /* 模块内覆写 */
  color: #fff;
  box-shadow: 0 6px 20px rgba(36, 100, 188, 0.16);
  border-radius: 10px;
  font-weight: 600;
}
.btn-filled:hover {
  background: #1A4F9A;
  transform: translateY(-1px);
  box-shadow: 0 10px 28px rgba(36, 100, 188, 0.24);
}
```

#### v4 课程首页按钮

```css
.v4-btn-primary {
  background: #2464BC; color: #fff;
  box-shadow: 0 8px 24px rgba(36,100,188,.20);
  border-radius: 10px; padding: 12px 28px;
  font-size: 15px; font-weight: 600;
}
.v4-btn-primary:hover { background: #1A4F9A; transform: translateY(-1px); }

.v4-btn-ghost {
  background: transparent; color: #2464BC;
  border: 1.5px solid rgba(36,100,188,.18);
  border-radius: 10px; padding: 12px 28px;
  font-size: 15px; font-weight: 600;
}
.v4-btn-ghost:hover { background: rgba(36,100,188,.04); }
```

#### 步骤按钮（课程列表页）

```css
.step-action {
  display: inline-flex; align-items: center; gap: 4px;
  padding: 5px 14px; border-radius: 4px;
  background: #4AA8E8; color: #fff;
  font-size: 12px; font-weight: 500;
  letter-spacing: 0.3px;
}
.step-action:hover { background: #3090d8; }
.step-action .arrow { transition: transform 0.2s; }
.step-action:hover .arrow { transform: translateX(2px); }
```

### 8.8 按钮 Ripple 涟漪效果

```css
.btn {
  position: relative; overflow: hidden;
}
.btn::after {
  content: ''; position: absolute; inset: 0;
  background: radial-gradient(circle, rgba(255,255,255,.3) 10%, transparent 10%);
  background-position: center; background-repeat: no-repeat;
  opacity: 0; transform: scale(10);
}
.btn:active::after {
  opacity: 1; transform: scale(0);
  transition: transform 0s, opacity .2s;
}
/* text 按钮用品牌色涟漪，outlined 用半透明品牌色 */
.btn-text::after { background: radial-gradient(circle, rgba(22,119,255,.2) 10%, transparent 10%); }
.btn-outlined::after { background: radial-gradient(circle, rgba(22,119,255,.15) 10%, transparent 10%); }
```

### 8.9 步骤条（Step Bar）

```
[← 课程首页]  [✓ 量潮是谁] — [2 业务与市场] — [3 工作方法论] — [4 最新方向] — [5 微型创业]
```

- 容器：`background: #f5f9fc`，border-radius 14px，border `1px solid #e8ecf2`，padding `18px 32px`
- 模块内页版本：透明底无边框（覆写为 `background: transparent; border: none; box-shadow: none; padding: 14px 0`）
- 返回链接：13px，`#1677ff`，weight 500

**圆点状态：**
| 状态 | 类名 | 背景色 | 文字色 | 特效 |
|------|------|--------|--------|------|
| 待完成 | `.dot` | `#f1f5f9` | `#b0bec5` | 无 |
| 已完成 | `.dot.ok` / `.dot.done` | `#f0fdf4` | `#22c55e` | `0 0 0 4px rgba(34,197,94,.08)` 光晕 |
| 当前 | `.dot.on` / `.dot.current` | `#1677ff` | `#fff` | `0 0 0 6px rgba(22,119,255,.10), 0 2px 8px rgba(22,119,255,.15)` 光晕 |

- 圆点尺寸：36px
- 连接线：24px 宽，2px 高，`#e8ecf2`；完成态 `#bbf7d0`

### 8.10 侧边栏（Sidenav）

```
┌─────────────────────┐
│ ▼ LMS · 学习管理    │  ← nav-label (11px, letter-spacing 1px)
│   📋 课题管理       │  ← nav-item (13px)
│   🔍 审批中心       │
│   🎓 双创项目管理   │
│   📁 成果仓库       │
│   👥 成员管理       │
│   📖 课程管理       │
│   👤 学员管理       │
│                     │
│ ▼ 表单配置          │  ← 可折叠
│   📝 立项申请表     │  ← sub (padding-left: 32px)
│   📋 阶段报告模板   │
│   ✅ 验收评审表     │
│                     │
│ ▼ 关联系统          │
│   📚 课程研发       │
│   💬 咨询/工单      │
└─────────────────────┘
```

- 宽度：220px，flex-shrink: 0
- 背景：`#f5f9fc`
- 右边框：`1px solid #e8ecf2`
- nav-label：11px，`#8899aa`，letter-spacing 1px，可折叠（箭头旋转 -90deg）
- nav-item：padding `9px 14px`，border-radius 6px，13px
- nav-item hover：背景 `#e8f4ff`
- nav-item active：背景 `#e8f4ff` + 文字 `#1677ff` + weight 600
- nav-item.sub：padding-left 32px
- nav-item.placeholder：opacity 0.6，不可点击

**折叠动画：**
- 箭头：`transform: rotate(-90deg)`，transition 0.15s
- 子列表：`max-height` transition 0.25s，folded 时 `max-height: 0 !important`

### 8.11 统计分析卡片（Stat Card）

```
┌──────────┐ ┌──────────┐ ┌──────────┐ ┌──────────┐
│    5     │ │    12    │ │    8     │ │    3     │
│  待审批  │ │  执行中  │ │  已完成  │ │  已否决  │
└──────────┘ └──────────┘ └──────────┘ └──────────┘
```

- 布局：`display: flex; gap: 16px`，等分（`flex: 1`）
- 背景：`#f5f9fc`
- 圆角：14px
- 边框：`1px solid #e8ecf2`
- 内边距：20px
- 数字：30px，weight 700，`#1a2332`
- 标签：13px，`#556678`，margin-top 2px
- hover：阴影浮起 + `translateY(-1px)`

### 8.12 数据表格（Data Table）

```
┌─────────────────────────────────────────────────┐
│ 课题名称 │ 申请人 │ 角色 │ 阶段 │ 状态 │ 操作  │
├─────────────────────────────────────────────────┤
│ AI ...  │ 李明   │ 技术 │ ...  │ 🟢   │ 详情  │
└─────────────────────────────────────────────────┘
```

- 表头：`text-align: left`，padding `12px 16px`，`#556678`，weight 500，底部 `2px solid #e8ecf2`
- 单元格：padding `13px 16px`，底部 `1px solid #f2f5f8`
- hover 行：背景 `#f8fafc`
- 字号：13px
- 容器卡片：padding: 0（表格撑满卡片）
- 表格底栏：padding `14px 16px`，顶部 `1px solid #f2f5f8`

### 8.13 流水线（Pipeline）

```
[💡]  →  [📝]  →  [🔍]  →  [🚀]  →  [🎤]
发现      提交      总部      2周       Sale
盲区      立项      审批      执行       总部
```

- 布局：`display: flex; gap: 0`，等分
- 箭头：`::after { content: '→' }`，18px，`#e8ecf2`，最后一项隐藏
- 图标：44px 圆形，`#f1f5f9` 底色，20px 字号，margin-bottom 8px
- 标题：13px，weight 600
- 提示：11px，`#8899aa`，line-height 1.5

### 8.14 时间线（Timeline）

```
│  ●  08-04 14:30  王芳 提交立项申请
│  ●  08-04 15:00  系统自动分配审阅人：张果
│  ●  当前节点 →   等待张果审批
│  ○  待触发        资源分配 · 进入执行
```

- 左边框：`2px solid #f2f5f8`，padding-left 20px
- 圆点：12px，`#1677ff`，border `3px solid #f5f9fc`，`box-shadow: 0 0 0 2px #e8ecf2`
- 圆点定位：`left: -28px; top: 4px`
- 时间戳：11px，`#8899aa`
- 事件：14px，margin-top 2px
- 间距：16px

### 8.15 表单元素

**标签：**
```css
display: block; font-size: 13px; font-weight: 600;
margin-bottom: 6px; color: #1a2332;  /* 或 #334155 */
```

**输入框/文本域/下拉框（标准）：**
```css
width: 100%; padding: 10px 14px;
border: 1.5px solid #e8ecf2;
border-radius: 8px; font-size: 14px;
background: #f5f9fc; color: #1a2332;
```
focus：边框变 `#1677ff`

**输入框（海平线模块内）：**
```css
width: 100%; padding: 11px 16px;
border: 1.5px solid rgba(148, 163, 184, 0.2);
border-radius: 10px; font-size: 14px;
background: #fafbfc; color: #10182B;
```
focus：边框变 `#4AA8E8`，背景变 `#fff`

**文本域：**
- 最小高度：90px
- `resize: vertical`

**表单行（并排）：**
```css
.form-row { display: flex; gap: 16px; }
.form-row > * { flex: 1; }
```

**表单组间距：** 标准 `margin-bottom: 16px`，模块内 `margin-bottom: 20px`

### 8.16 进度条

**标准版（课程 Hero）：**
- 轨道：`height: 5px; border-radius: 3px; background: rgba(22,119,255,.12); max-width: 400px`
- 填充：`height: 100%; border-radius: 3px; background: #1677ff`

**v4 版（课程首页）：**
- 轨道：`height: 5px; border-radius: 999px; background: linear-gradient(90deg, rgba(115,180,242,.18), rgba(115,180,242,.08) 70%, rgba(115,180,242,0))`
- 填充：`height: 100%; border-radius: inherit; background: linear-gradient(90deg, #3678D8, #73B4F2)`
- 标签：11px，`#64748B`，flex space-between

### 8.17 Badge / 标签

```css
.badge {
  display: inline-block;
  padding: 3px 12px;
  border-radius: 9999px;   /* pill */
  font-size: 11px;
  font-weight: 600;
  white-space: nowrap;
}
```

完整配色见第三章 Badge 配色表。

### 8.18 面包屑 / 返回链接

```css
.back-link {
  display: inline-flex; align-items: center; gap: 5px;
  color: #1677ff;         /* 或 #3678D8 */
  font-size: 13px; font-weight: 500;
  margin: 16px 0 12px;
  padding: 7px 14px; border-radius: 6px;
  cursor: pointer; transition: all .15s;
}
.back-link:hover { background: #e8f4ff; }
```

### 8.19 点阵装饰（右下角）

```css
.dots {
  position: absolute; right: 32px; bottom: 32px;
  width: 72px; height: 72px; pointer-events: none;
  background-image: radial-gradient(circle, rgba(22,119,255,.08) 1.6px, transparent 1.6px);
  background-size: 10px 10px;
}
```

v4 版：`rgba(115,180,242,.10) 1.5px`，right/bottom: 36px

### 8.20 成果仓库卡片

```html
<div style="flex:1; min-width:200px; padding:16px;
  background:#f8fafc; border-radius:8px;
  border:1px solid #f2f5f8;">
  <div style="font-size:24px; margin-bottom:8px">📊</div>
  <div style="font-weight:600; font-size:14px; margin-bottom:4px">项目名</div>
  <div style="font-size:12px; color:#8899aa; margin-bottom:8px">作者 · 日期</div>
  <span class="badge done">已验收</span>
</div>
```

### 8.21 全屏表单页（Form Page）

左右分栏布局：
```
┌─ form-header (50px) ──────────────────────────┐
│ 🟧 量潮课堂生产实习立项申请表    [结果分析][发布]│
├─ form-body (flex:1, 12px margin, 18px radius) ─┤
│ ┌─ form-left (60%) ─┐ ┌─ form-right (40%) ──┐ │
│ │ ← 返回后台         │ │    ○ ○ ○  装饰圆    │ │
│ │ h1: 表单标题       │ │         ★          │ │
│ │ 1 → 文本           │ │                     │ │
│ │ [问题描述]         │ │                     │ │
│ │ [textarea]         │ │                     │ │
│ │ 2 → 单选           │ │                     │ │
│ │ ○ 选项1            │ │                     │ │
│ │ ○ 选项2            │ │                     │ │
│ │ [✓ 提交]           │ │                     │ │
│ └────────────────────┘ └─────────────────────┘ │
└────────────────────────────────────────────────┘
```

**规格：**
- 全屏：`width: 100%; height: 100vh`
- 底色：`#f8fafe`
- 顶栏：50px，`#f5f9fc`，底部 `1px solid #e8ecf2`
- body 容器：`margin: 12px 24px`，border-radius 18px，背景渐变 `linear-gradient(135deg, #fdfaf6, #f0f4ff)`
- 左侧：60%宽度，padding `24px 0 0 80px`，overflow-y auto
- 标题：26px，weight 700
- 描述：13px，`#556678`
- 问题编号：17px，`#556678`
- 右侧装饰圆（3 个同心圆）：
  - 外圈：420px，`#e8f4ff`，opacity 0.5
  - 中圈：315px，`#1677ff`，opacity 0.3
  - 内圈：210px，`#f5f9fc`
  - 中心星号：56px，`#FFA726`
- 返回链接：`position: absolute; top: 14px; left: 80px`

---

## 九、布局工具类

### 9.1 Workspace

```css
.workspace { display: flex; height: calc(100vh - 56px); }
```

### 9.2 主内容区

```css
.main { flex: 1; overflow-y: auto; padding: 0 32px 60px; position: relative; z-index: 1; }
.main-inner { max-width: 860px; margin: 0 auto; }
```

### 9.3 视图切换

```css
.view { display: none; }
.view.show { display: flex; }
.module-panel { display: none; }
.module-panel.show { display: block; }
```

### 9.4 双栏

```css
.twocol { display: flex; gap: 24px; }
.twocol > * { flex: 1; }
.twocol .side { flex: 0 0 280px; }
```

### 9.5 Section

```css
.section { margin-bottom: 24px; }
.section-hd {
  display: flex; align-items: center; justify-content: space-between;
  margin-bottom: 16px;
}
.section-hd h3 { font-size: 16px; font-weight: 600; color: #1a2332; }
```

### 9.6 分割线

```css
hr.divider { border: none; border-top: 1px solid #f2f5f8; margin: 20px 0; }
```

---

## 十、动效系统

### 10.1 过渡时间速查

| 元素 | 属性 | 时长 | 缓动 |
|------|------|------|------|
| 卡片 hover 阴影 | box-shadow | 0.25s | ease |
| 课程卡片 hover | all | 0.25s | ease |
| 统计卡片 hover | all | 0.25s | ease |
| 模块卡片 hover | all | 0.25s | ease |
| 步骤卡片 hover | transform | 0.25s | — |
| 步骤卡片 active | transform | 0.06s | — |
| 潮线 hover | background, height | 0.25s | — |
| 按钮 hover | all | 0.2s | ease |
| 按钮 active ripple | transform, opacity | 0s / 0.2s | — |
| Nav 链接 hover | color | 0.2s | ease |
| 条目 hover 左移 | all | 0.15s | ease |
| 步骤圆点状态切换 | all | 0.25s | ease |
| 侧边栏状态层 | background | 0.2s | ease |
| 侧边栏箭头旋转 | transform | 0.15s | ease |
| 侧边栏折叠 | max-height | 0.25s | ease |
| 按钮箭头 hover | transform | 0.2s | ease |
| 面包屑 hover | all | 0.15s | ease |
| 表单输入 focus | border | 0.15s/0.2s | ease |

### 10.2 动效原则

1. 只用 `transform` 和 `opacity`，不动 `width/height/top/left`
2. 无自动播放动画，全部由用户交互触发
3. 默认贝塞尔曲线用 ease（`cubic-bezier(0.25, 0.1, 0.25, 1)`）

### 10.3 关键交互细节

**Card Elevation（hover 浮起）：**
- `.card:hover`：`box-shadow: 0 2px 8px rgba(0,0,0,.06), 0 4px 16px rgba(0,0,0,.04)`
- `.course-card:hover`：`box-shadow: 0 4px 12px rgba(22,119,255,.08), 0 2px 4px rgba(0,0,0,.06)` + `translateX(4px)`
- `.stat-card:hover`：`box-shadow: 0 2px 8px rgba(0,0,0,.06)` + `translateY(-1px)`
- `.module-card:hover`：`box-shadow: 0 2px 8px rgba(22,119,255,.08)`

**条目 hover 左移：**
```css
.lesson-item:hover, .lrow:hover { padding-left: 20px; }
```

**Focus 环：**
```css
input:focus-visible, textarea:focus-visible, select:focus-visible, button:focus-visible {
  outline: 2px solid rgba(22,119,255,.4); outline-offset: 2px;
}
```

**侧边栏 State Layer：**
```css
.nav-item::after { content: ''; position: absolute; inset: 0; pointer-events: none; transition: background .2s; }
.nav-item:hover::after { background: rgba(22,119,255,.04); }
.nav-item:active::after { background: rgba(22,119,255,.08); }
```

---

## 十一、全局规则

```css
* { box-sizing: border-box; margin: 0; padding: 0; }

body {
  font-family: var(--font);
  font-size: 14px;
  line-height: 1.6;
  background: #f8fafe;
  color: #1a2332;
  min-height: 100vh;
  overflow-x: hidden;
  -webkit-font-smoothing: antialiased;
}

/* 滚动条 */
::-webkit-scrollbar { width: 6px; }
::-webkit-scrollbar-track { background: transparent; }
::-webkit-scrollbar-thumb { background: #e8ecf2; border-radius: 3px; }
```

---

## 十二、响应式规则

**断点：800px（列表页）/ 900px（课程首页）**

### 列表页 ≤800px
- 页面内边距：16px
- Hero 标题：34px
- 步骤竖向排列（`flex-direction: column`），每步 `border-bottom: 1px solid rgba(148,163,184,0.18)`
- 所有步骤 padding-top 归零
- 按钮 transform 归零
- Outro：`flex-direction: column`

### 课程首页 ≤900px
- v4-card：宽度 90vw，`aspect-ratio: auto`，padding 32px 24px
- v4-title：30px

---

## 十三、页面层级关系

```
body
├── .bg-atmo (固定海浪装饰背景)
├── header.appbar (粘性顶栏)
│   ├── .top-bar (.top-logo + .top-links)
│   └── hr.appbar-horizon (潮汐线)
├── .workspace (flex row)
│   ├── #view-courses (课程列表 · show)
│   │   ├── .ocean-bg (.ocean-img + .ocean-fade)
│   │   └── .v3-page
│   │       ├── .v3-hero
│   │       ├── hr.horizon
│   │       ├── .course-path (5个 .step)
│   │       └── .outro
│   │
│   ├── #view-front (生产实习课程内页)
│   │   ├── 固定背景层 (海景图 + 雾遮罩 × 3)
│   │   └── .main > .main-inner
│   │       ├── .back-link
│   │       ├── .steps (步骤条)
│   │       ├── #mod-overview (.v4-shell > .v4-card)
│   │       ├── #mod-m1 ~ #mod-m5 (模块面板)
│   │       └── #mod-consult (咨询表单)
│   │
│   ├── #view-generic (通用课程内页)
│   │   └── .main > .main-inner
│   │       ├── .back-link
│   │       ├── .steps
│   │       ├── #gen-mod-overview (.course-hero)
│   │       └── #gen-panels (动态模块面板)
│   │
│   └── #view-back (后台 LMS)
│       ├── .sidenav (侧边栏 · 3组 nav-group)
│       │   ├── LMS · 学习管理 (7个 nav-item)
│       │   ├── 表单配置 (3个 nav-item.sub)
│       │   └── 关联系统 (2个 nav-item.sub)
│       └── .main
│           ├── 概览 (stat-row · 4个 stat-card)
│           ├── 课题管理 (datatable)
│           ├── 审批中心 (timeline + form)
│           ├── 双创项目管理 (pipeline)
│           ├── 成果仓库 (flex 卡片组)
│           ├── 成员管理 (datatable)
│           ├── 课程管理 (datatable)
│           ├── 学员管理 (datatable)
│           ├── 立项申请表 (form)
│           ├── 阶段报告模板 (form)
│           ├── 验收评审表 (form)
│           ├── 课程研发 (flex 双栏卡片)
│           └── 咨询/工单 (datatable)
│
└── #form-page (全屏表单 · 默认隐藏)
    ├── .form-header
    └── .form-body
        ├── .form-left (60%)
        └── .form-right (40% · 装饰圆)
```

---

## 十四、交付清单（新页面检查项）

- [ ] 颜色使用本系统 token，不硬编码新色值
- [ ] 潮汐线遵循渐变公式（`#4AA8E8 → #75BCEB → #A8D4F0 → 消隐`）
- [ ] 按钮有 hover（上浮 -1px + 阴影加深）+ active（ripple）反馈
- [ ] 卡片 hover 有浮起效果
- [ ] 条目行 hover 有左移反馈（padding-left 增加）
- [ ] 圆角在 4/6/8/10/14/18/28/9999 八个值中选择
- [ ] 响应式断点 800px / 900px 已覆盖
- [ ] 字体：列表 Hero 用衬线，其余用系统无衬线
- [ ] 背景：列表页用海景+遮罩，课程首页用大白卡片，模块内页用海平线透明卡片，后台用纯色
- [ ] 页面内容区 max-width 正确设置
- [ ] 模块内页步骤条为透明无边框样式
- [ ] Focus 环和滚动条样式已处理
