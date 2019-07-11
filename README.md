# YunXunSDKPy
### 云讯科技通讯服务SDK

###### 本SDK由个人编写, 用以个人开发和个人工作使用, 与`北京云讯科技有限公司 京ICP备14002087号-7`无关

![GitHub](https://img.shields.io/github/license/kerbalwzy/YunXunSDKPy.svg?color=green&logo=python&logoColor=yellow&style=flat-square)

### [云讯官方API文档](http://console.ytx.net/FileDetails/FileAccessGuide)

----
### 使用说明:

- 使用Git命令将此SDK的源代码下载到本地

  ```
  git clone https://github.com/kerbalwzy/YunXunSDKPy.git
  ```

- 将克隆下来的仓库中的`yunxunSDK`模块文件夹复制到你的项目目录中, 作为自定工具模块使用

  ![image-20190711111819409](https://github.com/kerbalwzy/DailyEssay/blob/master/media/yunxunsdk/image-20190711111819409.png)

- 编辑`yunxunSDK`模块内的`config.py`文件, 将你的配置添加好

  | 变量名      | 类型   | 说明                                                         |
  | ----------- | ------ | ------------------------------------------------------------ |
  | ACCOUNT_SID | String | 云通信平台用户账户ID：对应管理控制台中的 ACCOUNT SID         |
  | AUTH_TOKEN  | String | 云通信平台用户账户授权令牌：对应管理控制台中的 AUTH TOKEN    |
  | VERSION     | String | 云通信API接口版本 目前可选版本：201512                       |
  | API_HOST    | String | 云通信APT接口host 正式环境http://api.ytx.net 沙箱环境http://sandbox.ytx.net |
  | APPS        | Dict   | 云通信应用表,字典键为应用名称,值为应用ID：对应控制台中的应用管理-应用列表 |

- 导入`yunxunSDK.sender`模块内的功能类创建实例对象, 使用你创建的实例对象去调用云讯科技的API接口

  以发送普通模版短信为例:

  ```python
  from yunxunSDK.config import APPS	# 导入应用配置信息, 主要是要用到应用ID
  from yunxunSDK.sender import TemplateTextMessageSender
  
  # 创建实例对象
  TTMS_instance = TemplateTextMessageSender(APPS["YourAppName"])
  
  # 发送参数: 接收方列表、模版占位数据、模版ID
  receiver = ["138XXXXXXXX", "131XXXXXXXX"]
  data = ["dataDemo0", "dataDemo1"]
  tid = 1
  
  # 调用方法, 给云讯科技API发送请求
  TTMS_instance.send_text_message(receiver, data, tid)
  ```

- 更多内容, 请自己看源代码中的注释






