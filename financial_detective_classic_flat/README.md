# 금융사기 수사대 · 클래식 기록실 버전

고풍스럽고 클래식한 탐정 기록실 콘셉트로 제작한 Streamlit 웹앱입니다.
귀여운 캐릭터 대신, 사건 파일과 수사 보고서 같은 서류형 UI를 중심으로 구성했습니다.

## 파일 구성
- `app.py` : 메인 실행 파일
- `questions.py` : 문제 데이터
- `requirements.txt` : 설치 패키지 목록
- `README.md` : 프로젝트 설명

## 실행 방법
```bash
pip install -r requirements.txt
streamlit run app.py
```

## 배포 팁
GitHub 저장소의 **최상위(root)** 에 아래 4개 파일만 올리면 됩니다.
- `app.py`
- `questions.py`
- `requirements.txt`
- `README.md`

그 다음 Streamlit Community Cloud에서 **Main file path** 를 `app.py`로 설정하면 됩니다.

## 콘셉트
- 빈티지 사건파일 디자인
- 고전적인 기록물/문서 UI
- 브라운, 베이지, 골드 중심 색상
- 금융사기 대응 판단 테스트

## 주의
교육용 개인 프로젝트이며, 특정 금융기관의 공식 서비스가 아닙니다.
