import sys
sys.stdin = open('test_input.txt', 'rt', encoding='UTF8')

for _ in range(1, 11):
    T = input()
    # 찾을 문자열
    finding = input()
    # 찾을 문자열의 길이
    finding_len = len(finding)
    # 검색할 문장
    sentence = input()
    # 검색할 문장의 길이
    sentence_len = len(sentence)

    # 찾은 문자열의 수
    count = 0

    # 검색할 문장의 길이에서 찾을 문자열 길이만큼 뺀 값까지 반복
    for i in range(sentence_len - finding_len + 1):
        # 만약 찾을 문자열 전체가 검색할 문장의 찾을 문자열 길이만큼 검색해서 있다면
        if finding[:finding_len] == sentence[i:i + finding_len]:
            # 카운트 + 1
            count += 1

    print(f'#{T} {count}')