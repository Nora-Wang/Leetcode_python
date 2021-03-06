Given a collection of intervals, merge all overlapping intervals.

Example 1:

Input: [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].
Example 2:

Input: [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considered overlapping.
NOTE: input types have been changed on April 15, 2019. Please reset to default code definition to get new method signature.


思路：
直接合并，比如[1,3] [2,6] 合并成[1,6] ，不断合并，直到不能合并为止
区间左端点从小到大排个序，从左往右扫一遍:
– 不能合并 -> 直接下一个
– 能合并 -> 就合并


follow up: 057. Insert Interval

code:
Version 高频班
class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        #corner case
        if not intervals:
            return []
        
        result = []
        
        #使用lambda和sorted完成intervals的排序,时间复杂度为O(nlogn)(因为python中的sorted函数使用Timsort,参考https://github.com/qiwsir/algorithm/blob/master/python_sort.md)
        #sorted(iterable, cmp=None, key=None, reverse=False)
        #iterable:可迭代对象
        #cmp:比较的函数，这个具有两个参数，参数的值都是从可迭代对象中取出，此函数必须遵守的规则为，大于则返回1，小于则返回-1，等于则返回0
        #key:主要是用来进行比较的元素，只有一个参数，具体的函数的参数就是取自于可迭代对象中，指定可迭代对象中的一个元素来进行排序
        #reverse:排序规则，reverse = True 降序 ， reverse = False 升序（默认)
        intervals.sort(key = lambda x: x[0])
        
        for interval in intervals:
            #目前的interval的起始点<=前一个interval的终点，即result中的最后一个interval的终点时,则说明两个interval可以被合并
            #否则直接将该interval加入result中即可
            if len(result) and interval[0] <= result[-1][1]:
                result[-1][1] = max(result[-1][1], interval[1])
            else:
                result.append(interval)
                
        return result

    
Version 自写
class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        #注意点1:corner case
        if not intervals:
            return []
        if len(intervals) == 1:
            return intervals
        
        #知识点:sorted函数的应用
        #按照intervals中item排序的第一个值
        sorted_intervals = sorted(intervals, key = lambda item:item[0])
        
        result = []
        i = 0
        while i < len(sorted_intervals):
            #记录当前pair的起始值与终点值
            start = sorted_intervals[i][0]
            end = sorted_intervals[i][1]
            #当下一个pair的起始值>=当前pair的终点值,则将终点值更新
            #注意点2:while循环时用到了i+1,因此需要提前加个条件i < (len(sorted_intervals) - 1)
            while i < (len(sorted_intervals) - 1) and sorted_intervals[i + 1][0] <= end:
                #注意点3:可能会出现一个情况[[1,6],[2,3]],这样其实end还是为当前pair的终点值,因此需要加一个取max
                end = max(sorted_intervals[i + 1][1], end)
                i += 1
            
            #将该轮结果pair加入result
            result.append([start, end])
            
            i += 1

        return result
