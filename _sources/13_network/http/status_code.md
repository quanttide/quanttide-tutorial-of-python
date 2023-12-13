# http状态码

http状态码表示客户端http请求的返回结果、标记服务器端的处理是否正常或者出现错误，根据返回的状态码判断请求是否得到正确的处理。状态码有3位数和原因短语组成，三位数中第一位表示响应的类别。

## 1xx：信息状态码（接受的请求正在处理）

- 100 Continue：客户端继续发送请求，如果请求已经完成可忽略
- 101 Switching Protocols：服务器已经理解了客户端请求，将通过Upgrade消息头通知客户端采取不同的协议完成这个请求
- 102 Processing：处理将被继续执行

## 2xx：成功状态码（请求正常处理完毕）

- 200 OK：客户端发送到服务器的请求被正常处理并返回
- 201 Created：请求成功并创建了新的资源
- 204 No Content：客户端发送的请求服务端已成功处理，但没有资源可以返回
- 206 Patial Content：客户端进行了范围请求，服务器成功处理了部分GET请求

## 3xx：重定向（请求需要进行附加操作，APP登录流程页面比较常见）

- 301 Moved Permanently：永久重定向，表示请求的资源被分配到新的URL，之后应使用新的URL
- 301 Found：临时重定向：表示请求的资源被分配到新的UPL，本次访问使用新的URL，URL之后可能会更改

## 4xx：客户端错误（客户端请求出现错误，服务器无法处理请求）

- 400 Bad Request：语义出现错误，当前请求无法被服务器处理；请求参数有误
- 401 Unauthorized：当前请求用户未经许可，需要验证
- 403 Forbidden：控制权限，没有访问权限，服务器拒绝当前访问
- 404 Not Found：服务器没有找到请求的网页

## 5xx：服务器错误（服务器处理请求出错）

- 500 Inter Server Error：服务器执行请求时发生错误；web应用存在bug或者出现临时错误
- 501 Not Implemented：服务器不具备完成请求的功能
- 502 Bad Gateway：服务器作为网关或代理服务器，从上游服务器收到无效响应
- 503 Server Unavailable：服务器处于超负载状态或者正在维护，不能正常处理请求
- 504 Gateway Timeout：服务器作为网关或代理服务器，没有及时从上游服务器接收到请求
- 505 HTTP Version Not Supported：服务器不支持请求中所用的http协议版本