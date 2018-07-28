# -*- coding: utf-8 -*-

"""
@Time    : 2018/7/28 19:41
@Author  : fazhanzhang
@Function :
"""


class Viterbi(object):
    """维特比算法"""
    def __init__(self, start_stat, transfer_stat, emitter_stat):
        """
        :param start_stat: 初始状态
        :param transfer_stat: 转移矩阵
        :param emitter_stat: 发射矩阵
        """
        self.start = start_stat
        self.transfer = transfer_stat
        self.emitter = emitter_stat
        self.hidden = self.start.keys()

    def viterbi_decode(self, observation):
        """
        维特比解码
        :param observation:
        :return:
        """
        high_stat, temp_prob = self.init_temp_stat(observation[0])

        hidden_stat = [high_stat]
        probability = [temp_prob]

        for obser in observation[1:]:
            high_stat, temp_prob = self.get_high_prob_stat(probability[-1], obser)
            hidden_stat.append(high_stat)
            probability.append(temp_prob)

        return hidden_stat

    def get_high_prob_stat(self, previous_prob, observation):
        """
        根据前一次记录结果，求解当前观察状态对应隐含值
        :param previous_prob:
        :param observation:
        :return:
        """
        stat_prob_now = {}
        high_hidden_now_stat = ''
        high_hidden_now_prob = 0.0

        for stat0 in self.hidden:
            temp_prob = 0.0
            for stat1 in self.hidden:
                trans_prob = previous_prob[stat1] * self.transfer[stat1][stat0]
                if trans_prob > temp_prob:
                    temp_prob = trans_prob
            prob_stat0 = temp_prob * self.emitter[stat0][observation]

            stat_prob_now[stat0] = prob_stat0
            if prob_stat0 > high_hidden_now_prob:
                high_hidden_now_prob = prob_stat0
                high_hidden_now_stat = stat0
        return high_hidden_now_stat, stat_prob_now

    def init_temp_stat(self, observation):
        """
        根据初始状态，求解第一次观察值对应隐含状态
        :param observation:
        :return:
        """
        temp_stat = {}
        high_pro = 0.0
        high_stat = ''
        for item in self.hidden:
            prob_hidden = self.start[item] * self.emitter[item][observation]
            if prob_hidden > high_pro:
                high_pro = prob_hidden
                high_stat = item
            temp_stat[item] = prob_hidden
        return high_stat, temp_stat


if __name__ == '__main__':
    start = {'Sunny': 0.63, 'Cloudy': 0.17, 'Rainy': 0.20}
    transfer_stat = {'Sunny': {'Sunny': 0.5, 'Cloudy': 0.375, 'Rainy': 0.125},
                     'Cloudy': {'Sunny': 0.25, 'Cloudy': 0.125, 'Rainy': 0.625},
                     'Rainy': {'Sunny': 0.25, 'Cloudy': 0.375, 'Rainy': 0.375}}

    emitter_stat = {'Sunny': {'Dry': 0.6, 'Dryish': 0.2, 'Damp': 0.15, 'Soggy': 0.05},
                    'Cloudy': {'Dry': 0.25, 'Dryish': 0.25, 'Damp': 0.25, 'Soggy': 0.25},
                    'Rainy': {'Dry': 0.05, 'Dryish': 0.1, 'Damp': 0.35, 'Soggy': 0.5}}
    viterbi = Viterbi(start_stat=start, transfer_stat=transfer_stat, emitter_stat=emitter_stat)
    print(viterbi.viterbi_decode(['Dry', 'Damp', 'Soggy']))
