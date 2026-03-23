import sys
input = sys.stdin.readline

def solve():
    t = int(input())
    for _ in range(t):
        n = int(input())
        a = list(map(int, input().split()))
        
        max_elem = a[-1]
        ans = 0
        
        for k in range(2, n):
            need = max(a[k], max_elem - a[k])
            
            i, j = 0, k - 1
            while i < j:
                if a[i] + a[j] > need:
                    ans += (j - i)
                    j -= 1
                else:
                    i += 1
        
        print(ans)

if __name__ == "__main__":
    solve()