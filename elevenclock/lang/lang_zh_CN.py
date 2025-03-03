# INSTRUCTIONS

# Translate the text and write it between the "
# EXAMPLE:      original    ->  "This text is in english: value {0}" 
#               translation ->  "Aquest text està en anglès: valor {0}"
# If you see sth like {0}, {1}, maintain it on the translated sentence
# Meke special attention to elements like ":", etc.

lang_3_4_0 = {
    "Show calendar": "显示日历",
    "Disabled": "已禁用",
    "Open quick settings": "打开快速设置",
    "Show desktop": "显示桌面",
    "Open run dialog": "打开运行对话",
    "Open task manager": "打开任务管理器",
    "Open start menu": "打开开始菜单",
    "Open search menu": "打开搜索菜单",
    "Change task": "更改任务",
    "Change the action done when the clock is clicked": "更改单击时钟时完成的操作",
}

lang_3_3_2 = lang_3_4_0 | {
    "ElevenClock Updater": "ElevenClock 更新器",
    "ElevenClock is downloading updates": "ElevenClock 正在下载更新",
    "ElevenClock has updated to version {0} successfully\nPlease see GitHub for the changelog": "ElevenClock 已成功更新到版本 {0}\n请参阅 GitHub 获取更新日志",
    "Customize the clock on Windows 11": "在 Windows 11 上自定义时钟",
    "Disable the new instance checker method": "禁用新的实例检查器方法",
    "Import settings from a local file": "从本地文件导入设置",
    "Export settings to a local file": "将设置导出到本地文件",
    "Export": "导出",
    "Import": "导入",
}

lang_3_3_1 = lang_3_3_2 | {
    "Invalid time format\nPlease follow the\nC 1989 Standards": "时间格式无效\n请遵循 C 1989 标准",
    "Nothing to preview": "没有可预览的",
    "Invalid time format\nPlease modify it\nin the settings": "时间格式无效\n请在设置中修改",
    "Disable the tooltip shown when the clock is hovered": "禁用时钟悬停时显示的工具提示"
}
lang_3_3 = lang_3_3_1 | {
    "Custom format rules:": "自定义格式规则",
    "Any text can be placed here. To place items such as date and time, please use the 1989 C standard. More info on the following link": "任何文字都可以放在这里。 要放置日期和时间等项目，请使用 1989 C 标准。 以下链接有关更多信息",
    "Python date and time formats": "Python 日期和时间格式",
    "To disable the zero-padding effect, add a # in between the % and the code: non-zero-padded hours would be %#H, and zero-padded hours would be %H": "要禁用零填充效果，请在 % 和代码之间添加一个 #：非零填充小时数将是 %#H，零填充小时数将是 %H", # Here please don't modify the %H and %#H values
    "Click on Apply to apply and preview the format": "单击应用以应用和预览格式",
    "Apply": "应用",
    "If you don't understand what is happening, please uncheck the checkbox over the text area": "如果您不明白发生了什么，请取消选中文本区域上的复选框",
    "Set a custom date and time format": "设置自定义日期和时间格式",
    "(for advanced users only)": "（仅限高级用户）",
    "Move this clock to the left": "将此时钟移至左侧",
    "Move this clock to the top": "将此时钟移至顶部",
    "Move this clock to the right": "将此时钟移至右侧",
    "Move this clock to the bottom": "将此时钟移至底部",
    "Restore horizontal position": "恢复水平位置",
    "Restore vertical position": "恢复垂直位置",
}

lang_3_2_1 = lang_3_3 | {
    "Open online help to troubleshoot problems": "打开联机帮助以解决问题",
    "Reset ElevenClock preferences to defaults": "将 ElevenClock 首选项重置为默认值",
    "Specify a minimum width for the clock": "指定时钟的最小宽度",
    "Search on the settings": "搜索设置",
    "No results were found": "没有找到任何结果",
}

lang_3_2 = lang_3_2_1 | {
    "Use system accent color as background color": "使用系统强调色作为背景色",
    "Check only the focused window on the fullscreen check": "在全屏检查中只检查被关注的窗口",
    "Clock on monitor {0}": "监视器 {0} 上的时钟",
    "Move to the left": "向左移动",
    "Show this clock on the left": "在左侧显示这个时钟",
    "Show this clock on the right": "在右侧显示这个时钟",
    "Restore clock position": "恢复时钟位置",
}

lang_3_1 = lang_3_2 | {
    "W": "周", # The initial of the word week in your language: W for week, S for setmana, etc.
    "Disable the notification badge": "禁用通知标志",
    "Override clock default height": "覆盖时钟默认高度",
    "Adjust horizontal clock position": "调整水平时钟位置",
    "Adjust vertical clock position": "调整垂直时钟位置",
    "Export log as a file": "将日志导出为文件",
    "Copy log to clipboard": "将日志复制到剪贴板",
    "Announcements:": "公告：",
    "Fetching latest announcement, please wait...": "正在获取最新公告，请稍候……",
    "Couldn't load the announcements. Please try again later": "无法加载公告。 请稍后再试",
    "ElevenClock's log": "ElevenClock 的日志",
    "Pick a color": "取样一个颜色"
}

lang_3 = lang_3_1 | {
    "Hide the clock during 10 seconds when clicked": "单击时在 10 秒内隐藏时钟",
    "Enable low-cpu mode": "启用低 CPU 模式",
    "You might lose functionalities, like the notification counter or the dynamic background": "您可能会丢失通知计数器或动态背景等功能",
    "Clock position and size:": "时钟位置和大小",
    "Clock size preferences, position offset, clock at the left, etc.": "时钟大小首选项、位置偏移、左侧时钟等。",
    "Reset monitor blacklisting status": "重置监视器黑名单状态",
    "Reset": "重置",
    "Third party licenses": "第三方许可",
    "View": "视图",
    "ElevenClock": "",
    "Monitor tools": "监控工具",
    "Blacklist this monitor": "将此显示器列入黑名单",
    "Third Party Open-Source Software in Elevenclock {0} (And their licenses)": "Elevenclock {0} 中的第三方开源软件（及其许可证）",
    "ElevenClock is an Open-Source application made with the help of other libraries made by the community:": "ElevenClock 是在社区制作的其他库的帮助下制作的开源应用程序：",
    "Ok": "确认",
    "More Info": "更多信息",
    "About Qt": "关于 Qt",
    "Success": "成功",
    "The monitors were unblacklisted successfully.": "显示器已成功取消黑名单。",
    "Now you should see the clock everywhere": "现在你应该到处都能看到时钟",
    "Ok": "确认",
    "Blacklist Monitor": "黑名单监视器",
    "Blacklisting a monitor will hide the clock on this monitor permanently.": "将监视器列入黑名单将永久隐藏该监视器上的时钟。",
    "This action can be reverted from the settings window, under <b>Clock position and size</b>": "可以从设置窗口恢复此操作。 under <b>时钟位置和大小</b>",
    "Are you sure do you want to blacklist the monitor \"{0}\"?": "您确定要将监视器\"{0}\"列入黑名单吗？",
    "Yes": "是",
    "No": "否",
}

lang_2_9_2 = lang_3 | {
    "Reload log": "重新加载日志",
    "Do not show the clock on secondary monitors": "不要在辅助监视器上显示时钟",
    "Disable clock taskbar background color (make clock transparent)": "禁用时钟任务栏背景颜色（使时钟透明）",
    "Open the welcome wizard": "打开欢迎向导",
    " (ALPHA STAGE, MAY NOT WORK)": "（ALPHA 阶段，可能不起作用）",
    "Welcome to ElevenClock": "欢迎使用 ElevenClock",
    "Skip": "跳过",
    "Start": "开始",
    "Next": "下一个",
    "Finish": "完成",
}

lang_2_9 = lang_2_9_2 | {
    "Task Manager": "任务管理器",
    "Change date and time": "更改日期和时间",
    "Notification settings": "通知设置",
    "Updates, icon tray, language": "更新, 托盘图标, 语言",
    "Hide extended options from the clock right-click menu (needs a restart to be applied)": "隐藏时钟右键菜单中的扩展选项（需要重新启动才能应用）",
    "Fullscreen behaviour, clock position, 1st monitor clock, other miscellanious settings": "全屏行为, 时钟位置, 主监视器时钟, 其他杂项设置",
    'Add the "Show Desktop" button on the left corner of every clock': '在每个时钟的左上角添加“显示桌面”按钮',
    'You might need to set a custom background color for this to work.&nbsp;More info <a href="{0}" style="color:DodgerBlue">HERE</a>': '您可能需要为此设置自定义背景颜色。&nbsp;更多信息 <a href="{0}" style="color:DodgerBlue">HERE</a>',
    "Clock's font, font size, font color and background, text alignment": "时钟的字体, 字体大小, 字体颜色和背景, 文本对齐",
    "Date format, Time format, seconds,weekday, weeknumber, regional settings": "日期格式, 时间格式, 秒,工作日, 周数, 区域设置",
    "Testing features and error-fixing tools": "测试功能和错误修复工具",
    "Language pack author(s), help translating ElevenClock": "ElevenClock 语言包由 hlgsdx、jmlcoliveira、BoyceLig 帮助翻译",
    "Info, report a bug, submit a feature request, donate, about": "信息, 报告错误, 提交功能请求, 捐赠, 关于",
    "Log, debugging information": "日志, 调试信息",
}

lang_2_8 = lang_2_9 | {
    "Force the clock to be at the top of the screen": "强制时钟区位于屏幕顶部",
    "Show the clock on the primary screen": "在主屏幕上时钟区显示本程序的时钟样式",
    "Use a custom font color": "使用自定义字体颜色",
    "Use a custom background color": "使用自定义背景颜色",
    "Align the clock text to the center": "将时钟区文本与中心对齐",
    "Select custom color": "选择自定义颜色",
    "Hide the clock when a program occupies all screens": "当其它程序占据所有屏幕时隐藏时钟区",
}

lang2_7_bis = lang_2_8 | {
    "Use a custom font": "使用自定义字体",
    "Use a custom font size": "使用自定义字体大小",
    "Enable hide when multi-monitor fullscreen apps are running": "在多显示器全屏应用程序运行时启用隐藏",
    "<b>{0}</b> needs to be enabled to change this setting": "需要启用 <b>{0}</b> 才能更改此设置",
    "<b>{0}</b> needs to be disabled to change this setting": "需要禁用 <b>{0}</b> 才能更改此设置",
}

lang2_7 = lang2_7_bis | {
    " (This feature has been disabled because it should work by default. If it is not, please report a bug)": "此功能已被禁用，因为它应该在默认情况下工作。 如果不是，请报告错误",
    "ElevenClock's language": "ElevenClock 语言"
}

lang2_6 = lang2_7 | {
    "About Qt6 (PySide6)": "关于 Qt6 (PySide6)",
    "About": "关于",
    "Alternative non-SSL update server (This might help with SSL errors)": "使用替代的非SSL更新服务器(出现SSL错误时可尝试)",
    "Fixes and other experimental features: (Use ONLY if something is not working)": "启用试验性功能: (请仅在出问题时使用)",
    "Show week number on the clock": "在时钟区显示当前周序号",
    "This feature has been disabled because it should work by default. If it is not, please report a bug": "由于已开箱即用, 此选项被禁用。如有疑问, 请提交bug反馈",
}

lang2_5 = lang2_6 | {
    "Hide the clock when RDP Client or Citrix Workspace are running": "当使用远程桌面或运行 Citrix Workspace 时隐藏时钟区",
    "Clock Appearance:": "时钟区外观:",
    "Force the clock to have black text": "强制时钟区使用深色文本",
    " - It is required that the Dark Text checkbox is disabled": " - 当启用深色文本时不要使用",
    "Debbugging information:": "调试信息",
    "Open ElevenClock's log": "查看 ElevenClock 日志",
}

lang2_4 = lang2_5 | {
    # Added text in version 2.4
    "Show the clock on the primary screen (Useful if clock is set on the left)": "在主显示器上显示时钟区(在屏幕左侧显示时钟区时推荐开启)",
    "Show weekday on the clock"  :"在时钟区显示星期",
}

lang2_3 = lang2_4 | {
    #Context menu
    "ElevenClock Settings"      :"ElevenClock 选项", # Also settings title
    "Reload Clocks"             :"重载时钟区",
    "ElevenClock v{0}"          :"ElevenClock v{0}",
    "Restart ElevenClock"       :"重启 ElevenClock",
    "Hide ElevenClock"          :"隐藏 ElevenClock",
    "Quit ElevenClock"          :"退出 ElevenClock",
    
    #General settings section
    "General Settings:"                                                                 :"通用设置:",
    "Automatically check for updates"                                                   :"自动检测更新",
    "Automatically install available updates"                                           :"自动安装可用更新",
    "Enable really silent updates"                                                      :"开启静默更新",
    "Bypass update provider authenticity check (NOT RECOMMENDED, AT YOUR OWN RISK)"     :"跳过更新来源校验 (不推荐，自行承担风险)",
    "Show ElevenClock on system tray"                                                   :"在系统托盘显示 ElevenClock 图标",
    "Alternative clock alignment (may not work)"                                        :"使用替代的时钟对齐方式 (可能不起作用)",
    "Change startup behaviour"                                                          :"修改开机自启行为",
    "Change"                                                                            :"去修改",
    "<b>Update to the latest version!</b>"                                             :"<b>更新到最新版!</b>",
    "Install update"                                                                    :"安装更新",
    
    #Clock settings
    "Clock Settings:"                                              :"时钟区设置:",
    "Hide the clock in fullscreen mode"                            :"在全屏模式下隐藏时钟区",
    "Hide the clock when RDP client is active"                     :"当使用远程桌面时隐藏时钟区",
    "Force the clock to be at the bottom of the screen"            :"强制时钟区在屏幕底部显示",
    "Show the clock when the taskbar is set to hide automatically" :"当启用任务栏自动隐藏时显示时钟区",
    "Fix the hyphen/dash showing over the month"                   :"修复连字符会挡住月份的问题",
    "Force the clock to have white text"                           :"强制时钟区使用白色文本",
    "Show the clock at the left of the screen"                     :"在屏幕左侧显示时钟区",
    
    #Date & time settings
    "Date & Time Settings:"                             :"时间与日期设置",
    "Show seconds on the clock"                         :"显示秒数",
    "Show date on the clock"                            :"显示日期",
    "Show time on the clock"                            :"显示时间",
    "Change date and time format (Regional settings)"   :"修改日期与时间格式(区域设置)",
    "Regional settings"                                 :"区域设置",
    
    #About the language pack
    "About the language pack:"                  :"关于语言包",
    "Translated to English by martinet101"      :"简体中文翻译由 hlgsdx、jmlcoliveira、BoyceLig 贡献", # Here, make sute to give you some credits:  Translated to LANGUAGE by USER/NAME/PSEUDONYM/etc. 
    "Translate ElevenClock to your language"    :"把 ElevenClock 翻译成您的语言",
    "Get started"                               :"开始",
    
    #About ElevenClock
    "About ElevenClock version {0}:"            :"关于 ElevenClock {0}版:",
    "View ElevenClock's homepage"               :"查看 ElevenClock 的主页",
    "Open"                                      :"打开",
    "Report an issue/request a feature"         :"报告问题/建议新功能",
    "Report"                                    :"报告",
    "Support the dev: Give me a coffee☕"       :"打赏开发者：给我买杯咖啡☕",
    "Open page"                                 :"打开页面",
    "Icons by Icons8"                           :"程序图标由 Icons8 设计", # Here, the word "Icons8" should not be translated
    "Webpage"                                   :"网站",
    "Close settings"                            :"关闭设置",
    "Close"                                     :"关闭",
}

lang = lang2_3
