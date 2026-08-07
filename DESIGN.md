---
version: alpha
name: 量潮课堂 · 海岸设计系统
description: >
  面向培训机构的情景式互动教学平台。品牌以"海岸"为意象——清晨海面的冷静与正午浪花的生命力交融。
  大面积白色+浅蓝灰底色模拟海面反光，品牌蓝 #1677ff 如灯塔信号般精准出现在关键交互点。
  课程卡片采用微暖底色唤起"沙滩/书页"的联想。整体气质：理性但不冰冷、亲和但不幼稚。
  适用于：课堂前台、LMS 管理后台、课程展示页、创新项目管理。

colors:
  brand: "#1677ff"
  brand-deep: "#0958d9"
  brand-soft: "#e8f4ff"
  brand-muted: "#b8d8ff"
  canvas: "#ffffff"
  bg: "#f8fafe"
  surface: "#f5f9fc"
  surface-warm: "#fefaf5"
  surface-success: "#f0fdf4"
  surface-warning: "#fffbeb"
  ink: "#1a2332"
  ink-secondary: "#556678"
  ink-muted: "#8899aa"
  hairline: "#e8ecf2"
  hairline-light: "#f2f5f8"
  hairline-strong: "#d0d5dd"
  success: "#22c55e"
  warning: "#f59e0b"
  danger: "#ef4444"
  on-brand: "#ffffff"
  link: "#1677ff"

typography:
  display-xl:
    fontFamily: '"PingFang SC", "Microsoft YaHei", "Noto Sans SC", -apple-system, BlinkMacSystemFont, sans-serif'
    fontSize: 48px
    fontWeight: 600
    lineHeight: 1.15
    letterSpacing: -1px
  display-lg:
    fontFamily: '"PingFang SC", "Microsoft YaHei", "Noto Sans SC", -apple-system, BlinkMacSystemFont, sans-serif'
    fontSize: 36px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: -0.5px
  display-md:
    fontFamily: '"PingFang SC", "Microsoft YaHei", "Noto Sans SC", -apple-system, BlinkMacSystemFont, sans-serif'
    fontSize: 28px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: -0.3px
  title-lg:
    fontFamily: '"PingFang SC", "Microsoft YaHei", "Noto Sans SC", -apple-system, BlinkMacSystemFont, sans-serif'
    fontSize: 22px
    fontWeight: 600
    lineHeight: 1.35
  title-md:
    fontFamily: '"PingFang SC", "Microsoft YaHei", "Noto Sans SC", -apple-system, BlinkMacSystemFont, sans-serif'
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.4
  title-sm:
    fontFamily: '"PingFang SC", "Microsoft YaHei", "Noto Sans SC", -apple-system, BlinkMacSystemFont, sans-serif'
    fontSize: 16px
    fontWeight: 500
    lineHeight: 1.4
  body-lg:
    fontFamily: '"PingFang SC", "Microsoft YaHei", "Noto Sans SC", -apple-system, BlinkMacSystemFont, sans-serif'
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
  body-md:
    fontFamily: '"PingFang SC", "Microsoft YaHei", "Noto Sans SC", -apple-system, BlinkMacSystemFont, sans-serif'
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.55
  caption:
    fontFamily: '"PingFang SC", "Microsoft YaHei", "Noto Sans SC", -apple-system, BlinkMacSystemFont, sans-serif'
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.4
  button:
    fontFamily: '"PingFang SC", "Microsoft YaHei", "Noto Sans SC", -apple-system, BlinkMacSystemFont, sans-serif'
    fontSize: 15px
    fontWeight: 500
    lineHeight: 1.2
  label:
    fontFamily: '"PingFang SC", "Microsoft YaHei", "Noto Sans SC", -apple-system, BlinkMacSystemFont, sans-serif'
    fontSize: 12px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0.5px

rounded:
  xs: 6px
  sm: 8px
  md: 14px
  lg: 18px
  xl: 24px
  pill: 9999px
  full: 9999px

spacing:
  xxs: 4px
  xs: 8px
  sm: 12px
  md: 16px
  lg: 24px
  xl: 32px
  xxl: 48px
  section: 80px
  section-lg: 120px

shadows:
  card: "0 1px 3px rgba(26,35,50,0.04)"
  card-hover: "0 4px 16px rgba(26,35,50,0.08)"
  dropdown: "0 8px 24px rgba(26,35,50,0.10)"
  modal: "0 16px 48px rgba(26,35,50,0.12)"

components:
  button-primary:
    backgroundColor: "{colors.brand}"
    textColor: "{colors.on-brand}"
    typography: "{typography.button}"
    rounded: "{rounded.md}"
    padding: 12px 24px
    shadow: none
  button-primary-hover:
    backgroundColor: "{colors.brand-deep}"
    textColor: "{colors.on-brand}"
  button-secondary:
    backgroundColor: transparent
    textColor: "{colors.brand}"
    typography: "{typography.button}"
    rounded: "{rounded.md}"
    padding: 12px 24px
    border: "1px solid {colors.brand}"
  button-ghost:
    backgroundColor: transparent
    textColor: "{colors.ink-secondary}"
    typography: "{typography.button}"
    rounded: "{rounded.md}"
    padding: 8px 16px
  text-link:
    backgroundColor: transparent
    textColor: "{colors.link}"
    typography: "{typography.body-md}"
    textDecoration: none
    hover-textDecoration: underline
  top-nav:
    backgroundColor: rgba(255,255,255,0.85)
    backdropFilter: blur(12px)
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    height: 60px
    borderBottom: "1px solid {colors.hairline}"
  hero-band:
    backgroundColor: "{colors.bg}"
    textColor: "{colors.ink}"
    typography: "{typography.display-xl}"
    padding: "{spacing.section-lg} {spacing.xl}"
  card-default:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    rounded: "{rounded.md}"
    padding: "{spacing.lg}"
    shadow: "{shadows.card}"
    hover-shadow: "{shadows.card-hover}"
  card-course:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    rounded: "{rounded.lg}"
    padding: "{spacing.xl}"
    shadow: "{shadows.card}"
    borderLeft: "4px solid {colors.brand}"
  card-warm:
    backgroundColor: "{colors.surface-warm}"
    textColor: "{colors.ink}"
    rounded: "{rounded.md}"
    padding: "{spacing.lg}"
  card-success:
    backgroundColor: "{colors.surface-success}"
    textColor: "{colors.ink}"
    rounded: "{rounded.md}"
    padding: "{spacing.lg}"
    border: "1px solid {colors.success}"
  badge:
    backgroundColor: "{colors.brand-soft}"
    textColor: "{colors.brand}"
    typography: "{typography.label}"
    rounded: "{rounded.pill}"
    padding: 2px 10px
  badge-success:
    backgroundColor: "{colors.surface-success}"
    textColor: "{colors.success}"
    typography: "{typography.label}"
    rounded: "{rounded.pill}"
    padding: 2px 10px
  badge-warning:
    backgroundColor: "{colors.surface-warning}"
    textColor: "{colors.warning}"
    typography: "{typography.label}"
    rounded: "{rounded.pill}"
    padding: 2px 10px
  step-bar:
    backgroundColor: "{colors.surface}"
    activeColor: "{colors.brand}"
    inactiveColor: "{colors.hairline-strong}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
  side-nav:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink-secondary}"
    activeTextColor: "{colors.brand}"
    activeBgColor: "{colors.brand-soft}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    width: 240px
  side-nav-item:
    padding: 10px 16px
    rounded: "{rounded.sm}"
    hover-bg: "{colors.hairline-light}"
  input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 10px 14px
    border: "1px solid {colors.hairline-strong}"
    focus-border: "1px solid {colors.brand}"
    focus-shadow: "0 0 0 3px {colors.brand-soft}"
  divider:
    color: "{colors.hairline}"
    thickness: 1px
  progress-bar:
    backgroundColor: "{colors.hairline}"
    fillColor: "{colors.brand}"
    rounded: "{rounded.full}"
    height: 6px
  tooltip:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    typography: "{typography.caption}"
    rounded: "{rounded.xs}"
    padding: 6px 10px
  empty-state:
    textColor: "{colors.ink-muted}"
    typography: "{typography.body-lg}"
    iconColor: "{colors.hairline-strong}"
  modal-overlay:
    backgroundColor: "rgba(26,35,50,0.4)"
    backdropFilter: blur(4px)

animation:
  transition-fast: 0.15s ease
  transition-base: 0.25s ease
  transition-slow: 0.4s ease
  card-hover-lift: -4px

breakpoints:
  mobile: 640px
  tablet: 1024px
  desktop: 1280px
  wide: 1536px
