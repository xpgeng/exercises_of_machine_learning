# Precision and Recall
---
- 光用误差率(error rate)肯定是不行的, 因为你不知道细节: 正例的正确率是多少, 反例的正确率又多少. 所以有了`confusion matrix`

- confusion matrix
    - TP(True Positive)
    - FP
    - FN(False Negative)
    - TN
- Precision = TP / (TP + FP)
    - 只关注预测为正例的正确率
- Recall = TP/(TP + FN)
- Precision 和 Recall 不能同时保证很高. 极端一点, 全部预测为正例, recall就是100%, 可是此时 precision就会很低. 
- ROC curve (Receiver Operating Characteristic)
- AUC (area under the curve)
    - perfect: 1
    - randomly select: 0.5

