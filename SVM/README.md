# Support Vector Machine

## Introduction
- Linearly sparable
- separating hyperplane(分离超平面)
    - hyperplane: 可以简单的理解为, 维数较高的平面.都是线性组合而已.
- margin
    - SVM的目的就是**find the maximum margin**.
- support vectors
    - 距离分离超平面最近的点.
- 之前我们在做二分类的时候会选用{0, 1}作为labels, 在SVM中, 为了通过数学更好的描述问题, 选用{-1, 1}作为labels.
    - 这样做的目的是通过`label\*(w_t*x+b)`就可以表示出例子的标签以及其函数距离(函数距离的定义参看李航老师的**统计学习方法**)
- 问题:
    - max min{label\*(w_t*x+b)\*(1/||w||) }
- 使用Lagrange multipliers 转化为dual problem.
- 有时候数据并不是100%线性可分的, 所以这是引如slack varialbes(松弛变量)
    - 其目的是给一些距离分离超平面过近的点加上一个大于等于零的值, 使得其满足原约束.

## General approach to SVMs
1. Collect
2. Prepare: Numeric values are needed.
3. Analyze
4. Train
5. Test
6. Use

> 直接从ML in Acion上抄了下来.


## SMO(sequential minimal optimization)

### Why
- 当数据量较大的时候求解优化问题是非常慢的, 所以Platt在1999年发表了SMO.

### Idea


## Kernel Methods




## References
- [Machine Learning in Action](https://book.douban.com/subject/6962285/)
- [统计学习方法--李航](https://book.douban.com/subject/10590856/)