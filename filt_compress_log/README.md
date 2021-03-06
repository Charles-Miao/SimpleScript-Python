# 相关说明

## 版本V1.0

### log_filt_compress_1.0.py
- 实现功能：单进程实现log筛选和log压缩
- 问题一：测试log达到亿数量级时，处理效率极低，可能需要几个月才能把log处理完

## 版本V1.1

### log_filt_compress_1.1.py
- 实现功能：引入多进程编程，处理效率提高，亿数量级的log只需一个星期即可筛选完毕
- 问题一：压缩log未实现多进程
- 问题二：各个进程结束时间不确定，导致主进程无法继续运行后面脚本
- 问题三：进程数量未进行控制，导致部分CPU性能比较低的服务器会超频，特别是Windows Server 2008基本不可以正常工作

## 版本V1.2

### log_compress.py

- 压缩log多进程处理，瓶颈会在内存

### log_filt.py

- log筛选多进程处理，可以控制进程数量，瓶颈会在CPU

### log_filt_compress_1.2.py

- 引入进程池的概念，方便限制进程数量
- 主进程可以正常结束

## 版本V1.3

- 修复了1.2版本中的配置困难的问题，所有变量全部从ini获取
- 筛选log时自动获取机种名，无需人为设定
- log_filt.py，设定筛选某一天的log
- log_filt_1.py，透过数组设定筛选几天的log
- log_filt_2.py，透过scv设定筛选多天的log，方便手动筛选调试
- 问题点：子进程异常终止时无法记录和确认