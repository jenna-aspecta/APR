'''
计算 APR
'''
import math
class APRCalculator:
    def __init__(self, staking, building_progress):
        self.staking = staking
        self.building_progress = building_progress
    def calculate_y(self):
        # y = staking * 0.02 * [(2 * (1 / (1 + e^{-building_progress / 25}))) - 1]
        y = ( self.staking + 500 ) * 0.02 * ((2 * (1 / (1 + math.exp(-self.building_progress / 25)))) - 1)
        return y
    def calculate_z(self):

        return 0
    def calculate_apr(self):
        # apy = [(0.3 * 52) / 500] * y * (z - 1) / z
        y = self.calculate_y()
        apr = ((0.3 * 52) / 500) * y  # staking = 0  时的公式,使用时注意把所有关于 z 的计算部分注释掉
        return apr

staking = 0
building_progress = 8
calculator = APRCalculator(staking, building_progress)
a = calculator.calculate_y()
b= calculator.calculate_z()
apr = calculator.calculate_apr()
print(f"APR: {apr}\ny: {a}\nz: {b}")
# print(f"APR2: {apr_2}\ny: {a}\nz: {b}")