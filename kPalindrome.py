dp = {}

def is_palendrome(word, start, end, k):
    if k == -1:
        return False
    if start > end:
        return True
    
    key = "%s %s %s" % (start, end, k)
    if key in dp:
        return dp[key]

    result = None

    #print "start: %s end: %s" % (word[start], word[end])
    if word[start] == word[end]:
        result = is_palendrome(word, start + 1, end - 1, k)
    else:
        result = is_palendrome(word, start + 1, end, k - 1)
        if result == False:
            result = is_palendrome(word, start, end - 1, k - 1)

    dp[key] = result

    return result


string = "abdxa"
k = 1

print is_palendrome(string, 0, len(string)-1, k)

k = 2

print is_palendrome(string, 0, len(string)-1, k)

string = "oozyratinasanitaryzoo"
k = 0
print string
print is_palendrome(string, 0, len(string)-1, k)

string = "racecar111"
k = 2

print string
print is_palendrome(string, 0, len(string)-1, k)

string = "1ooz2yrat3inasani4tary56zo7o"
k = 7

print string
print is_palendrome(string, 0, len(string)-1, k)

k = 6

print string
print is_palendrome(string, 0, len(string)-1, k)


