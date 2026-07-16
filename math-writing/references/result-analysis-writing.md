# Result Analysis Writing

## Purpose

Use this when result tables, sensitivity tables, validation rows, or figure evidence need to become paper-facing analysis.

## Core Pattern

Every result paragraph should contain conclusion, evidence, comparison, mechanism, and boundary or decision meaning. If one part is missing, the paragraph may be readable but not judge-useful.

## Result Paragraph

Recommended shape:

```text
由表X可见，[方案/场景]在[指标]上达到[数值][单位]，较[基准]变化[差值/比例]。这一变化说明[趋势或比较结论]，其原因在于[机制解释]。在[条件/边界]内，该结果支持[决策/回答分问]。
```

Avoid:

- dumping one bullet per scenario;
- listing parameters without a table or trend sentence;
- saying "效果较好" without a measurable baseline;
- citing a figure before it has been introduced;
- describing sensitivity values without the perturbation range.

## Sensitivity Paragraph

Use:

```text
为检验[参数]对[指标]的影响，将其在[范围]内扰动。结果显示，[指标]变化幅度为[数值]，且[排名/可行性/符号]保持不变，说明模型在该范围内对[参数]不敏感。当[参数]超出[阈值]时，[现象]开始出现，因此该阈值构成模型适用边界。
```
