'''
72410. 신규 아이디 추천
1단계 new_id의 모든 대문자를 대응되는 소문자로 치환합니다.
2단계 new_id에서 알파벳 소문자, 숫자, 빼기(-), 밑줄(_), 마침표(.)를 제외한 모든 문자를 제거합니다.
3단계 new_id에서 마침표(.)가 2번 이상 연속된 부분을 하나의 마침표(.)로 치환합니다.
4단계 new_id에서 마침표(.)가 처음이나 끝에 위치한다면 제거합니다.
5단계 new_id가 빈 문자열이라면, new_id에 "a"를 대입합니다.
6단계 new_id의 길이가 16자 이상이면, new_id의 첫 15개의 문자를 제외한 나머지 문자들을 모두 제거합니다.
     만약 제거 후 마침표(.)가 new_id의 끝에 위치한다면 끝에 위치한 마침표(.) 문자를 제거합니다.
7단계 new_id의 길이가 2자 이하라면, new_id의 마지막 문자를 new_id의 길이가 3이 될 때까지 반복해서 끝에 붙입니다.
'''

# 첫번째 풀이
def solution(new_id):
    answer = ''
    
    # 1 
    answer = new_id.lower()
    
    # 2
    filtered = []
    for c in answer:
        if c.isalpha() or c.isdigit() or c in ('-', '_', '.'):
            filtered.append(c)
    answer = ''.join(filtered)
    
    # 3
    while '..' in answer:
        answer = answer.replace('..', '.')
    
    # 4
    answer = answer.strip('.')
    
    # 5
    if answer == '': answer = 'a'
    
    # 6
    if len(answer) > 15: 
        answer = answer[:15]
    if answer[-1] == '.': answer = answer[:-1]
    
    # 7
    while len(answer) < 3:
        answer += answer[-1]
    
    
    return answer

'''
테스트 1 〉	    통과 (0.01ms, 10.3MB)
테스트 2 〉	    통과 (0.01ms, 10.2MB)
테스트 3 〉	    통과 (0.02ms, 10.2MB)
테스트 4 〉	    통과 (0.01ms, 10.3MB)
테스트 5 〉	    통과 (0.01ms, 10.2MB)
테스트 6 〉	    통과 (0.01ms, 10.3MB)
테스트 7 〉	    통과 (0.01ms, 10.3MB)
테스트 8 〉	    통과 (0.01ms, 10.3MB)
테스트 9 〉	    통과 (0.01ms, 10.3MB)
테스트 10 〉	통과 (0.01ms, 10.2MB)
테스트 11 〉	통과 (0.01ms, 10.2MB)
테스트 12 〉	통과 (0.04ms, 10.3MB)
테스트 13 〉	통과 (0.02ms, 10.2MB)
테스트 14 〉	통과 (0.02ms, 10.3MB)
테스트 15 〉	통과 (0.03ms, 10.1MB)
테스트 16 〉	통과 (0.05ms, 10.2MB)
테스트 17 〉	통과 (0.11ms, 10.4MB)
테스트 18 〉	통과 (0.10ms, 10.2MB)
테스트 19 〉	통과 (0.20ms, 10.3MB)
테스트 20 〉	통과 (0.15ms, 10.2MB)
테스트 21 〉	통과 (0.18ms, 10.2MB)
테스트 22 〉	통과 (0.15ms, 10.2MB)
테스트 23 〉	통과 (0.19ms, 10.2MB)
테스트 24 〉	통과 (0.28ms, 10.2MB)
테스트 25 〉	통과 (0.20ms, 10.1MB)
테스트 26 〉	통과 (0.25ms, 10.2MB)
'''