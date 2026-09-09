# Experiment No. 5
# Longest Common Subsequence using Dynamic Programming

def find_lcs(X, Y):
    m = len(X)
    n = len(Y)

    # Create DP table
    dp = [[0 for _ in range(n + 1)] for _ in range(m + 1)]

    # Fill the DP table
    for i in range(1, m + 1):
        for j in range(1, n + 1):

            if X[i - 1] == Y[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1

            else:
                dp[i][j] = max(dp[i - 1][j],
                               dp[i][j - 1])

    # Construct the LCS
    i = m
    j = n
    lcs = []

    while i > 0 and j > 0:

        if X[i - 1] == Y[j - 1]:
            lcs.append(X[i - 1])
            i -= 1
            j -= 1

        elif dp[i - 1][j] > dp[i][j - 1]:
            i -= 1

        else:
            j -= 1

    # Reverse because LCS was constructed backwards
    lcs.reverse()

    return ''.join(lcs), dp[m][n]


# Main Program
print("===== Longest Common Subsequence =====")

sequence1 = input("Enter first sequence: ")
sequence2 = input("Enter second sequence: ")

lcs, length = find_lcs(sequence1, sequence2)

print("\nFirst Sequence :", sequence1)
print("Second Sequence:", sequence2)
print("LCS            :", lcs)
print("LCS Length     :", length)