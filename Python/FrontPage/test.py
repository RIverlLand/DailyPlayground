
# 给定一个整数数组 temperatures ，表示每天的温度，返回一个数组 answer ，其中 answer[i] 是指在第 i 天之后，才会有更高的温度。如果气温在这之后都不会升高，请在该位置用 0 来代替。
# 示例 1:
# 输入: temperatures = [73,74,75,71,69,72,76,73]
# 输出: [1,1,4,2,1,1,0,0]
# 示例 2:
# 输入: temperatures = [30,40,50,60]
# 输出: [1,1,1,0]示例 3:
# 输入: temperatures = [30,60,90]
# 输出: [1,1,0]
# 提示：
# 1 <= temperatures.length <= 105
# 30 <= temperatures[i] <= 100

def test(temperatures:list):
    i = 0
    output = []
    while i < len(temperatures):
        j = i
        if i == len(temperatures) - 1:
            output.append(0)
            break
        while j < len(temperatures):
            if temperatures[j] <= temperatures[i]:
                pass
            elif temperatures[j] > temperatures[i]:
                output.append(j-i)
                break
            if j >= len(temperatures)-1:
                output.append(0)
                break
            j +=1
        i += 1
    return output

print(test([30,60,90]))
print(test([73,74,75,71,69,72,76,73]))