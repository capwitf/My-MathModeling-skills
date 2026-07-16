# Model Evaluation Writing

## Purpose

Use this when writing model advantages, limitations, improvements, and promotion boundaries.

## Advantages

Write advantages as structural value, not praise. Each advantage should point to a visible formula, table, figure, previous result, or support artifact.

Good structure:

```text
模型通过[变量/约束/判定函数]把[现实难点]转化为可计算结构，见式(X)和表Y。这使得[状态判断/方案比较/跨问传递]可以被回代检验，而不是依赖经验描述。
```

Do not write:

- "模型效果较好";
- "图像直观清晰";
- "具有广阔应用前景";
- "时间有限，仍需改进".

## Limitations And Promotion

Limitations should name the missing factor and affected conclusion. Promotion should name the same mathematical structure, required new data, and failure boundary.

Use:

```text
当前模型忽略[因素]，主要影响[指标/结论]。若推广到[同构场景]，需要重新标定[参数]并增加[约束/数据]；当[关键假设]不成立时，应引入[修正机制]后再使用。
```
