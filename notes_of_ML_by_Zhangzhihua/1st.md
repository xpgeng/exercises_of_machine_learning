# 基本概念
- Machine Learning
    - Mike Jordon: 
    - ML = Matrix + Optimization + Algorithm + Statistics
- 尽量用矩阵, 范数去表达目标函数
- ridge regression
    - 对目标函数(最小二乘误差函数)加一个惩罚项 `+lamda*||a||`
        - 注意是二范数
        - 如果一范数, 则叫Lasso
    - 目的就是使得X_T*X变成正定阵, a是所优化参数, lamda是可调节参数.
- Data 分类
    - Training data
    - Validation data
    - Test data
- 二分类(0,1)问题
    - 使用最大似然估计, maximum likihood
    - 利用sigmoid函数,取log...
- Unsupervised learning
    - PCA
    - 降维
        - 线性
        - 非线性
    - 聚类
- Semi-supervised Learning
    - 标签数据少, 无标签数据多, 将测试数据也放进去, 循环训练.
        - Transtactive learning. 传导学习
    - Elastic Net
- Active Learning

## ML 分类
- Parametric Approach
    - 参数不随数据的个数变化.
    - Logistic regression
- Non-parametric Approach
    - 参数依赖训练数据的个数.
    - NN(每个数据都是参数)
- Discriminait Models
    - 数据
- Generation Models
    - 数据分布有假设
- *Bayesian*
    - 要估计的参数a是随机变量(random variable)
    - a给定一个先验分布
    - P(x|a)
    - 然后算x(数据)给定的情况下, 算a的后验.
    - 核心: **算积分**, 用MC(赌城).
    - 大数定理
- *Frequentist*
    - 给数据, 把参数(常数,未知)估计出来.
    - 核心:**优化问题**.

> 讲了Logistic regression 用极大似然估计与Bayesian 方法的等价关系.  
> G =  f(x) + penalty(a)  
> 1. 对数打分原理  
> 2. Dualty between penalty and Prior

> Regularition Framework