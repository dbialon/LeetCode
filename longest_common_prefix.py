def longestCommonPrefix(strs: [str]) -> str:
    if len(strs) == 0:
        return ""

    result = strs[0]
    max_len = float("inf")
    for word in strs:
        max_len = min(max_len, len(word))
        result = result[:max_len]
        while True:
            if result != word[:max_len]:
                max_len -= 1
                result = result[:-1]
            else:
                break

    return result


my_list = ["flower","flow","flight"]

print(longestCommonPrefix(my_list))
