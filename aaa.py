# # # dx = [-1, 1, 0, 0]
# # # dy = [0, 0, -1, 1]
# # # def is_valid(x, y):
# # #     return 0 <= x < N and 0 <= y < M
# # # N, M = map(int, input().split())
# # # heights = [list(map(int, input().split())) for _ in range(N)]
# # # x1, y1, x2, y2 = map(int, input().split())
# # # arr = []
# # # for i in range(N):
# # #     for j in range(M):
# # #        arr.append((heights[i][j],i,j))
# # # arr.sort()
# # # dp=[ [0 for i in range(M)] for j in range(N)]
# # # for h,i,j in arr:
# # #     if i==x1 and j==y1:
# # #         dp[i][j] = 1
# # #     for k in range(4):
# # #         tx=i+dx[k]
# # #         ty=j+dy[k]
# # #         if is_valid(tx,ty) and h > heights[tx][ty]:
# # #             dp[i][j] += dp[tx][ty]
# # #             dp[i][j] %= (10**9)
# # # print(dp[x2][y2])
# #
# # # M, N = map(int, input().split())
# # #
# # # chicks = list(map(int, input().split()))
# # # j = 0
# # # a = list(map(int,input().split()))
# # # for _ in range(N):
# # #     if len(chicks) <= 1:
# # #         break
# # #     attack, defend = a[j],a[j+1]
# # #     j+=2
# # #     if attack > len(chicks) :
# # #         continue
# # #     elif attack != defend or defend > len(chicks):
# # #         del chicks[attack-1]
# # # chicks.sort()
# # # if len(chicks) > 1:
# # #     print("Success!",end=' ')
# # #
# # #     print(" ".join(map(str, chicks)))
# # # else:
# # #     print("Fail!",end=' ')
# # #     if chicks:
# # #         print(chicks[0])
# # # def countNumbers(arr):
# # #     print(arr)
# # #     ans=[0]
# # #     for i in range(1,1000010):
# # #         cnt=[0 for j in range(10)]
# # #         t=i
# # #         flag=0
# # #         while t>0:
# # #             if cnt[t%10]>0:
# # #                 flag=1
# # #                 break
# # #             cnt[t%10]+=1
# # #             t//=10
# # #         ans.append(0)
# # #         if flag==1:
# # #             ans[i]=ans[i-1]
# # #         else:
# # #             ans[i]=ans[i-1]+1
# # #     res=[]
# # #     for x,y in arr:
# # #         res.append(ans[y]-ans[x-1])
# # #     for x in res:
# # #         print(x)
# # #     return res
# #
# # #
# # # print(solution([[1,20],[9,19]]))
# #
# # def areAlmostEquivalent(s,T):
# #     res=[]
# #     for i in range(len(s)):
# #         x=s[i]
# #         y=T[i]
# #         cnt=[0 for j in range(260)]
# #         for t in x:
# #             cnt[ord(t)-ord('a')] += 1
# #         for t in y:
# #             cnt[ord(t)-ord('a')] -= 1
# #         if min(cnt)>=-3 and max(cnt)<=3:
# #             res.append("YES")
# #         else:
# #             res.append("NO")
# #     return res
# # print(areAlmostEquivalent(["aaa",'t'],["aab",'t']))
# #
# # # 定义一个链表节点类
# # class ListNode:
# #     def __init__(self, val=0, next=None):
# #         self.val = val  # 节点的值
# #         self.next = next  # 指向下一个节点的指针
# #
# # # 定义一个函数来反转单链表
# # def reverseLinkedList(head):
# #     prev = None  # 前一个节点的指针，初始为None，因为第一个节点没有前一个节点
# #     current = head  # 当前节点的指针，初始为链表的头节点
# #
# #     # 开始迭代链表
# #     while current is not None:
# #         next_node = current.next  # 下一个节点的指针，用于保存当前节点的下一个节点
# #
# #         # 反转当前节点的指针，使其指向前一个节点
# #         current.next = prev
# #
# #         # 更新prev和current指针，为下一次迭代做准备
# #         prev = current
# #         current = next_node
# #
# #     return prev  # 返回反转后的链表的头节点
# #
# # # 示例用法
# # # 创建一个链表：1 -> 2 -> 3
# # node3 = ListNode(3)
# # node2 = ListNode(2, node3)
# # node1 = ListNode(1, node2)
# #
# # # 反转链表
# # new_head = reverseLinkedList(node1)
# #
# # # 打印反转后的链表
# # current = new_head
# # while current is not None:
# #     print(current.val, end=" -> ")
# #     current = current.next
# # # 输出：3 -> 2 -> 1 ->
# #
# # # 输出：3 -> 2 -> 1 ->
# #
# # def longestCommonPrefix(self, strs: List[str]) -> str:
# #     if not strs:
# #         return ""
# #
# #     length, count = len(strs[0]), len(strs)
# #     for i in range(length):
# #         c = strs[0][i]
# #         if any(i == len(strs[j]) or strs[j][i] != c for j in range(1, count)):
# #             return strs[0][:i]
# #
# #     return strs[0]
# #
# #
# # def longestCommonPrefix(self, strs: List[str]) -> str:
# #     # 检查输入列表是否为空，如果为空则返回空字符串
# #     if not strs:
# #         return ""
# #
# #     # 获取第一个字符串的长度和字符串列表的长度
# #     length, count = len(strs[0]), len(strs)
# #
# #     # 从第一个字符开始遍历
# #     for i in range(length):
# #         # 获取当前位置的字符
# #         c = strs[0][i]
# #
# #         # 使用 any() 函数检查除第一个字符串外的其他字符串在当前位置是否不等于 c
# #         # 如果有不等于 c 的字符串或者某个字符串已经到达末尾，返回第一个字符串的前 i 个字符作为最长公共前缀
# #         if any(i == len(strs[j]) or strs[j][i] != c for j in range(1, count)):
# #             return strs[0][:i]
# #
# #     # 如果循环结束都没有返回，说明第一个字符串本身就是最长公共前缀
# #     return strs[0]
# # time log(n) space o(1)
# # 二分
# # 二分找到这个数第一次出现的位置
# # 找到最后一次的出现位置
# # 两个相减就行
#
#
# # time log(n) space o(1)
# def countOccurrences(target, arr):
#     # 初始化左右边界
#     l, r = 0, len(arr) - 1
#
#     # 找到第一个大于或等于 target 的位置
#     while l < r:
#         mid = (l + r) // 2
#         if arr[mid] < target:
#             l = mid + 1
#         else:
#             r = mid
#
#     # 记录第一个大于或等于 target 的位置
#     ansl = l
#
#     # 检查目标值是否存在于数组中
#     if arr[ansl] != target:
#         return 0
#
#     # 重置左右边界
#     l, r = 0, len(arr) - 1
#
#     # 找到最后一个小于或等于 target 的位置
#     while l < r:
#         mid = (l + r + 1) // 2
#         if arr[mid] > target:
#             r = mid - 1
#         else:
#             l = mid
#
#     # 返回目标值在数组中的出现次数
#     return r - ansl + 1
#
#
# # 测试函数
# print(countOccurrences(20, [10,10,20]))  # 输出：2

def solution(s,t):
    for i in range(len(s)):
        x = ord(s[i]) - ord('a')
        y = ord(t[i]) - ord('a')
        if y != (x+1)%26:
            return False
    return True
print(solution("abyz","bcza"))
print(solution("abyz","bczb"))
def solution(numbers):
    arr1 = [numbers[0]]
    arr2 = [numbers[1]]
    for i in range(2,len(numbers)):
        cnt1 = 0
        for x in arr1:
            if x > numbers[i]:
                cnt1 += 1
        for x in arr2:
            if x > numbers[i]:
                cnt1 -= 1
        if cnt1!=0:
            if cnt1>0:
                arr1.append(numbers[i])
            else:
                arr2.append(numbers[i])
        else:
            if len(arr1) <= len(arr2):
                arr1.append(numbers[i])
            else:
                arr2.append(numbers[i])
    arr1.extend(arr2)
    return arr1

print(solution([5,7,6,9,2]))

def solution(firstArray,secondArray,target):
    d={}
    for i in range(len(firstArray)):
        s = 0
        for j in range(i,len(firstArray)):
            s += firstArray[j]
            if s not in d:
                d[s] = 0
            d[s] += 1
    firstArray = secondArray
    res = 0
    for i in range(len(firstArray)):
        s = 0
        for j in range(i,len(firstArray)):
            s += firstArray[j]
            if target - s in d:
                res += d[target - s]
    return res


print(solution([5,2,1,6,4],[3,5],10))


def solution(members,events):
    members.sort()
    active = {}
    inactive={}
    uc = {}
    for x in members:
        active[x] = 0
        uc[x] = 0
    for event in events:
        op = event[0]
        time = int(event[1])
        tt = event[2].split()
        for x in list(inactive.keys()):
            if inactive[x] <= time:
                del inactive[x]
                active[x]  = time
        if op=="MESSAGE":
            s = set()
            if "ALL" in tt:
                for x in members:
                    if x=="ALL" or x=="HERE":
                        continue
                    uc[x] += 1
            elif "HERE" in tt:
                for x in active.keys():
                    if x not in s:
                        s.add(x)
                        uc[x] += 1
                for x in tt:
                    if x=="HERE":
                        continue
                    if x not in s:
                        s.add(x)
                        uc[x] += 1
            else:
                for x in tt:
                    if x not in s:
                        s.add(x)
                        uc[x] += 1
        else:
            del active[tt[0]]
            inactive[tt[0]] = time + 60
    ans = []
    for x in members:
        ans.append(x+"="+str(uc.get(x,0)))
    return ans

print(solution(["id42","id158","id23"],[["MESSAGE","0","ALL id158 id42"],["OFFLINE","1","id158"],

        ["MESSAGE","2","id158 id158"],["OFFLINE","3","id23"],["MESSAGE","60","HERE id158 id42 id23"],
                                        ["MESSAGE","61","HERE"]]))
