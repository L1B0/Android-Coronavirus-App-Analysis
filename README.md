# 恶意程序分析

> 参考链接：
> https://securitynews.sonicwall.com/xmlpost/coronavirus-themed-android-rat-on-the-prowl/

> https://www.aqniu.com/threat-alert/64734.html

> https://www.freebuf.com/articles/terminal/227337.html

> 安卓动态调试-虚拟机：https://bbs.pediy.com/thread-217612.htm

> https://www.52pojie.cn/thread-508579-1-1.html

> https://blog.csdn.net/piracy5566/article/details/87859747

## 事件背景

随着新型冠状病毒在全世界范围内的传播，恶意软件的开发人员开始利用新冠病毒造成的恐慌作为一种传播恶意软件的手段。2020年2月初，SonicWall威胁研究小组发现了一个名为Coronavirus的Android apk。以下描述均用“Covirus”代指Coronavirus APP。

## 分析过程

### 动态执行

1. 将Covirus放入模拟器中，安装并执行。随着时间推移，观察到Covirus有以下行为：
* 弹窗提示启用Coronavirus服务，如图1；
* 反复弹窗提示是否忽略电池优化，并自动撤销，不给用户点击的时间，如图2；
* 当用户离开Covirus界面时，如返回桌面、执行其它app，Covirus会自动弹出；
* 关机或重启后，Covirus会自动启动；
* 执行后隐藏图标，用户无法通过长按图标卸载app。

### 静态分析
1. 使用安卓反编译工具apktool对apk文件进行反编译。
* 浏览生成的文件时发现src文件夹下的文件（夹）名称均为无意义的字母串，如hdjro、Isupplycountry.smali，并且通过反编译smali文件，查看其伪代码发现每个smali文件的内容都类似，没有找到有意义的代码；
* 查看AndroidManifest.xml文件，发现activity类型的android:name元素的内容中许多是src文件夹下不存在的文件，如iba.jkgmnr.nomttdnemcorujdfjfsfsmrb.Ahedgehogsay，故猜测Covirus通过动态加载代码的方式执行这些文件；
2. 在模拟器中执行Covirus之后，查看系统路径/data/data，可以看到如图3所示的文件，app_DynamicOptDex文件夹中的ZE.json实际是一个Dex文件，将其转jar后便能够通过Java 
Decompiler看到其伪代码，可以看到该文件内便包含有AndroidManifest.xml文件所描述的所有动态加载的文件。其中首字母为大写后面接两个单词的文件均为无意义的代码，如WcaptainShift；而文件名全为小写的文件包含关键代码，这些文件均位于iba.jkgmnr.nomttdnemcorujdfjfsfsmrb内，分析结果如下：
* 这些代码的函数中的参数内容均使用类base64的字符串，调用解密函数后传入。
* 解密的python代码如图4所示，原理：输入为12位小写字母拼接上一串base64加密的字符串；解密函数首先将字符串使用base64算法解密，得到一串字符串，其中每位均为16进制的数据范围内（0-9,a-f）,然后将解密得到的这串16进制串每两位为一个byte转为字符串作为密文；使用12位小写字母作为key生成密钥。
* 分析所有解密得到的明文可以发现Covirus的一些恶意行为，如http://kryll.ug表示其可能与该网站建立了连接，发送数据造成用户信息泄露；connect_teamviewer表示可能调用teamviewer进行远程控制，使得手机成为RAT；android.permission.READ_PHONE_STATE表示获取了读取手机状态的权限等。

### 防御和补救方法

* 进入系统文件路径/data/data和/data/app，删除与恶意app有关的文件夹；

### 使用的软件

* 模拟器：Android Studio - Pixel 2 Android 9.0，夜神模拟器
* 反编译工具：Apktool Box V1.6.4

### 反编译
java -jar .\baksmali-2.4.0.jar d .\malware.apk -o .\src

