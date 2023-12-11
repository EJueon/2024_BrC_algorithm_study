def solution(new_id):
    answer = ''
    
    # 1. 대문자 소문자 치환
    answer = new_id.lower()
    
    # 2. 알파벳 소문자, 숫자, 빼기, 밑줄, 마침표 제외 모든 문자 제거
    from re import sub
    answer = sub(r'[^a-z0-9\-\_\.]', '', answer)
    
    # 3. dot이 두번 이상 연속될 경우 dot 1개로 치환
    answer = sub(r'\.+', '.', answer)

    # 4. 앞뒤 마침표 제거
    answer = answer.strip('.')
    
    # 5. 빈 문자열일 경우 문자열 a 추가
    answer = 'a' if not answer else answer
    
    # 6. 길이가 16자 이상일 경우 나머지 문자 제거. / 마지막 마침표 제거
    answer = answer[:15].rstrip('.') if len(answer) >= 16 else answer
    
    # 7. 길이가 2자 이하일 경우, 길이가 3이 될때까지 마지막 문자를 반복하여 추가
    if len(answer) < 3:
        answer += answer[-1] * (3 - len(answer))
    
    return answer
'''
결과
테스트 1 〉	    통과 (0.17ms, 10.2MB)
테스트 2 〉	    통과 (0.24ms, 10.4MB)
테스트 3 〉	    통과 (0.17ms, 10.4MB)
테스트 4 〉	    통과 (0.14ms, 10.2MB)
테스트 5 〉	    통과 (0.15ms, 10.2MB)
테스트 6 〉	    통과 (0.13ms, 10.2MB)
테스트 7 〉	    통과 (0.14ms, 10.3MB)
테스트 8 〉	    통과 (0.15ms, 10.3MB)
테스트 9 〉	    통과 (0.14ms, 10.3MB)
테스트 10 〉	통과 (0.14ms, 10.2MB)
테스트 11 〉	통과 (0.14ms, 10.4MB)
테스트 12 〉	통과 (0.14ms, 10.3MB)
테스트 13 〉	통과 (0.15ms, 10.2MB)
테스트 14 〉	통과 (0.13ms, 10.3MB)
테스트 15 〉	통과 (0.14ms, 10.3MB)
테스트 16 〉	통과 (0.21ms, 10.2MB)
테스트 17 〉	통과 (0.16ms, 10.2MB)
테스트 18 〉	통과 (0.17ms, 10.2MB)
테스트 19 〉	통과 (0.23ms, 10.2MB)
테스트 20 〉	통과 (0.42ms, 10.3MB)
테스트 21 〉	통과 (0.22ms, 10.4MB)
테스트 22 〉	통과 (0.23ms, 10.2MB)
테스트 23 〉	통과 (0.15ms, 10.3MB)
테스트 24 〉	통과 (0.16ms, 10.2MB)
테스트 25 〉	통과 (0.16ms, 10.3MB)
테스트 26 〉	통과 (0.15ms, 10.2MB)
'''