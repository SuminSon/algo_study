N = int(input())            # N+1개의 "I"와 N개의 "O"가 번갈아 들어가는 문자열이 대상이다.
s_length = int(input())     # 탐색하려는 문자열의 길이
S = input()                 # 탐색하려는 문자열
left = right = 0            # 투포인터를 설정해준다.


count = 0                   # 주어진 문자열에 탐색 문자열이 몇 번 들어가는지 체크할 변수.
while right < s_length:     # 오른쪽 포인터가 끝에 도달하기 전에
    if S[right:right+3] == "IOI":   # 오른쪽 포인터의 오른쪽이 IOI라면
        right += 2                  # 오른쪽 포인터를 두 칸 옮긴다.
        if right - left == 2*N:     # 만약 두 포인터의 차이가 찾으려는 문자열 크기와 같아지면 찾으려던 문자열과 같다는 뜻
            count += 1              # 결과값에 +1
            left += 2               # 왼쪽 포인터를 오른쪽으로 2칸 옮긴다.
    else:
        left = right = right+1      # 투포인터를 모두 오른쪽으로 한 칸 옮긴다.

print(count)

# 이 경우에는 투 포인터로 중복되는 슬라이싱 연산을 줄여서 O(N)이 소요된다.
# 계속해서 오른쪽으로 2칸씩 넘어가며 확인하기 때문이다.