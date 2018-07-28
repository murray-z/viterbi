# 维特比算法
> 主要解决根据观察状态求解隐含状态的问题

# 示例

### 问题假设
<pre>
天气有三种情况：'Sunny', 'Cloudy'， 'Rainy';
海水中海草状态有四种情况：'Dry', 'Dryish', 'Damp', 'Soggy'； 
</pre>

### 问题抽象
```python
# 初始状态，天气分布情况
start_stat = {'Sunny': 0.63, 'Cloudy': 0.17, 'Rainy': 0.20}

# 状态转移，即各种天气之间转移概率
transfer_stat = {'Sunny': {'Sunny': 0.5, 'Cloudy': 0.375, 'Rainy': 0.125},
                'Cloudy': {'Sunny': 0.25, 'Cloudy': 0.125, 'Rainy': 0.625},
                 'Rainy': {'Sunny': 0.25, 'Cloudy': 0.375, 'Rainy': 0.375}}

# 发射矩阵, 即根据天气情况观察到的海草状态
emitter_stat = {'Sunny': {'Dry': 0.6, 'Dryish': 0.2, 'Damp': 0.15, 'Soggy': 0.05},
                'Cloudy': {'Dry': 0.25, 'Dryish': 0.25, 'Damp': 0.25, 'Soggy': 0.25},
                'Rainy': {'Dry': 0.05, 'Dryish': 0.1, 'Damp': 0.35, 'Soggy': 0.5}}

# 假设连着三天我们观察到的海草状态为['Dry', 'Damp', 'Soggy']
# 那么如何根据以上条件求解天气状态？

# 观察状态
observation = ['Dry', 'Damp', 'Soggy']


# 求解
from viterbi import Viterbi


viterbi = Viterbi(start_stat=start_stat, transfer_stat=transfer_stat, emitter_stat=emitter_stat)
hidden_stat = viterbi.viterbi_decode(['Dry', 'Damp', 'Soggy'])

```


