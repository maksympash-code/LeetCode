# def sliding_window(arr, k):
#     n = len(arr)
#
#     left = 0
#     curr = 0
#     answer = 0
#
#     for right in range(n):
#         curr += arr[right]
#
#         while curr > k:
#             curr -= arr[left]
#             left += 1
#
#         answer = max(answer, right - left + 1)
#
#     return answer

def sliding_window(s):

    left = 0
    curr = 0
    ans = 0

    for right in range(len(s)):
        if s[right] == '0':
            curr += 1

        while curr > 1:
            if s[left] == '0':
                curr -= 1
            left += 1

        ans = max(ans, right - left + 1)

    return ans



if __name__ == '__main__':
    # arr = [3, 1, 2, 7, 4, 2, 1, 1, 5]
    # k = 8

    s = '1101100111'

    print(sliding_window(s))