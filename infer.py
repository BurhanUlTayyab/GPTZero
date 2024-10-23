"""
This code a slight modification of perplexity by hugging face
https://huggingface.co/docs/transformers/perplexity

Both this code and the orignal code are published under the MIT license.

by Burhan Ul tayyab and Nicholas Chua
"""

from model import GPT2PPL

# initialize the model
model = GPT2PPL()

sentence = """
这些术语通常与自然语言处理（NLP）中的文本分析有关。下面是对每个术语的解释：

Perplexity (困惑度)：
Perplexity 是衡量概率模型预测文本序列能力的一个指标。它实际上可以理解为模型对于未见数据的预测误差。Perplexity 越低，表示模型对数据的拟合越好。Perplexity 为 1 表示模型完美地预测了每一个词，这是一个理想的情况，在实际应用中很少见到这么低的困惑度。
Perplexity per line 142.7：
这个值表示每行文本的平均困惑度。如果是在评估一个模型对于文本的理解程度，那么 142.7 是一个相对较高的数值，意味着模型在预测该行文本中的词语时有较大的不确定性。
Burstiness (爆发性)：
Burstiness 是指文本中的信息量分布不均匀的现象。在自然语言处理中，它通常用来描述消息或邮件等通信中的非均匀模式。例如，在电子邮件交流中，burstiness 可能指的是发送邮件的时间间隔分布不均匀，或者消息长度的波动较大。在这个上下文中，642 可能是一个量化这种不均匀性的值。
这些指标可以帮助我们了解一个模型对文本的理解程度以及文本本身的特性。如果你正在使用某个工具来检测 AI 输出的质量，那么这些数值可以用来评估生成的文本是否自然、连贯，并且符合人类写作的习惯。
"""

model(sentence)
