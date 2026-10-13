import streamlit as st
from questions import QUESTIONS

st.set_page_config(
    page_title="금융사기 수사대 | 고전 기록실",
    page_icon="🕮",
    layout="centered",
    initial_sidebar_state="collapsed",
)

if "screen" not in st.session_state:
    st.session_state.screen = "intro"
if "current" not in st.session_state:
    st.session_state.current = 0
if "answers" not in st.session_state:
    st.session_state.answers = {}


def reset_app():
    st.session_state.screen = "intro"
    st.session_state.current = 0
    st.session_state.answers = {}


def get_grade(score: int):
    if score == 100:
        return "A", "수석 조사관", "모든 사건에서 위험 신호를 정확히 읽어냈습니다. 매우 침착하고 신중한 판단력을 보였습니다."
    if score >= 75:
        return "B", "선임 조사관", "전반적으로 우수한 대응력을 보였습니다. 다만 몇몇 유형에서는 한 번 더 확인하는 습관이 필요합니다."
    if score >= 50:
        return "C", "수습 조사관", "기본적인 감각은 있으나 긴급한 상황에서 흔들릴 수 있습니다. 공식 채널 확인 원칙을 더 익혀야 합니다."
    return "D", "기록 보조원", "즉각적인 판단보다 먼저 멈추고 확인하는 훈련이 필요합니다. 링크 클릭과 송금 전 재확인이 중요합니다."


def weak_tag():
    wrong = [q["tag"] for i, q in enumerate(QUESTIONS) if st.session_state.answers.get(i) != q["answer"]]
    if not wrong:
        return "취약 유형 없음"
    counts = {}
    for t in wrong:
        counts[t] = counts.get(t, 0) + 1
    return max(counts, key=counts.get)


st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Cormorant+Garamond:wght@500;600;700&family=Noto+Serif+KR:wght@400;500;600;700&display=swap');

    :root {
        --bg: #f3ede1;
        --paper: #f9f3e8;
        --paper-deep: #efe2c6;
        --ink: #2f2418;
        --sub: #6e5a43;
        --line: #bda98a;
        --gold: #8c6a2f;
        --navy: #203040;
        --seal: #7b332d;
        --good: #ece8d8;
        --bad: #f4e4df;
    }

    html, body, [class*="css"] {
        font-family: 'Noto Serif KR', serif;
        color: var(--ink);
    }

    .stApp {
        background:
            radial-gradient(circle at top right, rgba(140,106,47,.08), transparent 18%),
            linear-gradient(180deg, #f6f0e4 0%, #efe6d4 100%);
    }

    .block-container {
        max-width: 820px;
        padding-top: 1.3rem;
        padding-bottom: 3rem;
    }

    #MainMenu, footer {visibility:hidden;}
    header[data-testid="stHeader"] {background: transparent;}

    .cover-card {
        position: relative;
        background: linear-gradient(180deg, #f9f2e5 0%, #f1e4c8 100%);
        border: 1.6px solid var(--line);
        border-radius: 8px;
        padding: 34px 30px;
        box-shadow: 0 14px 28px rgba(48,36,24,0.10);
        margin-bottom: 18px;
        overflow: hidden;
    }

    .cover-card:before {
        content: "";
        position: absolute;
        inset: 14px;
        border: 1px solid rgba(123, 85, 45, .32);
        border-radius: 4px;
        pointer-events: none;
    }

    .archival-stamp {
        display:inline-block;
        border:1.4px solid var(--seal);
        color:var(--seal);
        padding:6px 12px;
        font-size:.82rem;
        font-weight:700;
        letter-spacing:.08em;
        margin-bottom:16px;
        transform: rotate(-2deg);
        background: rgba(123,51,45,.03);
    }

    .cover-title {
        font-family: 'Cormorant Garamond', serif;
        font-size: 3rem;
        font-weight: 700;
        line-height: 1.05;
        margin-bottom: 10px;
        letter-spacing: .02em;
        color: var(--navy);
    }

    .cover-subtitle {
        font-size: 1.02rem;
        color: var(--sub);
        line-height: 1.85;
        margin-bottom: 18px;
    }

    .divider-rule {
        height: 1px;
        background: linear-gradient(90deg, transparent, rgba(79,59,35,.44), transparent);
        margin: 18px 0;
    }

    .meta-row {
        display:flex;
        flex-wrap:wrap;
        gap:10px;
        margin-top:14px;
    }

    .meta-chip {
        display:inline-block;
        padding:8px 12px;
        border:1px solid var(--line);
        border-radius: 999px;
        font-size:.88rem;
        color: var(--sub);
        background:#fbf7ef;
    }

    .note-card, .case-card, .report-card {
        background: var(--paper);
        border: 1.4px solid var(--line);
        border-radius: 8px;
        padding: 22px;
        box-shadow: 0 10px 18px rgba(48,36,24,0.06);
        margin-bottom: 14px;
    }

    .section-title {
        font-family: 'Cormorant Garamond', serif;
        font-size: 1.7rem;
        font-weight: 700;
        color: var(--navy);
        margin-bottom: 10px;
    }

    .section-text {
        color: var(--sub);
        line-height: 1.8;
        font-size: .98rem;
    }

    .case-header {
        display:flex;
        justify-content:space-between;
        align-items:center;
        gap:10px;
        flex-wrap:wrap;
        margin-bottom: 10px;
    }

    .file-no {
        font-family:'Cormorant Garamond', serif;
        font-size: 1.4rem;
        color: var(--navy);
        font-weight: 700;
        letter-spacing: .04em;
    }

    .tag-box {
        border:1px solid var(--line);
        padding:6px 10px;
        background:#fcf7ee;
        font-size:.82rem;
        color: var(--sub);
        border-radius: 999px;
    }

    .case-title {
        font-size: 1.28rem;
        font-weight: 700;
        color: var(--ink);
        margin-bottom: 10px;
    }

    .scenario-box {
        background: rgba(255,255,255,.35);
        border: 1px solid #d4c4aa;
        border-radius: 6px;
        padding: 16px;
        line-height: 1.9;
        color: var(--ink);
    }

    .memo-box {
        margin-top:12px;
        border-left: 4px solid var(--gold);
        background: #f7efe0;
        padding: 12px 14px;
        color: var(--sub);
        line-height: 1.7;
    }

    .result-good {
        background: var(--good);
        border: 1px solid #c5b991;
        border-radius: 6px;
        padding: 14px;
        line-height: 1.8;
        color: var(--ink);
    }

    .result-bad {
        background: var(--bad);
        border: 1px solid #d5aea5;
        border-radius: 6px;
        padding: 14px;
        line-height: 1.8;
        color: var(--ink);
    }

    .stamp-title {
        display:inline-block;
        font-family:'Cormorant Garamond', serif;
        font-size: 2rem;
        font-weight: 700;
        letter-spacing:.03em;
        color: var(--navy);
        margin-bottom: 6px;
    }

    .grade-box {
        border: 1.5px solid var(--line);
        background: linear-gradient(180deg, #faf6ee 0%, #f2e6cf 100%);
        border-radius: 8px;
        padding: 18px;
        text-align:center;
    }

    .grade-code {
        font-family:'Cormorant Garamond', serif;
        font-size: 2.1rem;
        font-weight: 700;
        color: var(--navy);
        line-height:1;
    }

    .grade-name {
        font-size: 1.05rem;
        font-weight: 700;
        color: var(--ink);
        margin-top: 8px;
    }

    .small-label {
        font-size: .82rem;
        color: var(--sub);
        letter-spacing:.04em;
        text-transform: uppercase;
        margin-bottom: 6px;
    }

    .summary-item {
        border-top: 1px dashed #c9b79a;
        padding-top: 12px;
        margin-top: 12px;
    }

    div.stButton > button {
        width:100%;
        min-height:58px;
        border-radius: 6px;
        border:1.3px solid #7a6444;
        background: linear-gradient(180deg, #3d3123 0%, #261d14 100%);
        color: #f8f1e4;
        font-weight: 600;
        font-size: 1rem;
        box-shadow: 0 6px 14px rgba(34,26,18,.12);
    }

    div.stButton > button:hover {
        border-color: #8c6a2f;
        color: #fff9ed;
    }

    div.stButton > button[kind="secondary"] {
        background: #fbf6ee;
        color: var(--ink);
        border: 1.2px solid var(--line);
        box-shadow:none;
    }

    .stProgress > div > div > div > div {
        background: linear-gradient(90deg, #6a5131 0%, #b28a45 100%);
    }

    .final-note {
        margin-top: 16px;
        text-align:center;
        color: #7c6a54;
        font-size:.82rem;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

with st.sidebar:
    st.markdown("### 기록실 메뉴")
    st.write("- 금융사기 사례 8건")
    st.write("- 사건별 분석 메모")
    st.write("- 최종 수사 보고서")
    st.write("- 개인정보 미수집")
    st.divider()
    if st.button("처음으로", use_container_width=True):
        reset_app()
        st.rerun()

if st.session_state.screen == "intro":
    st.markdown(
        """
        <div class="cover-card">
            <div class="archival-stamp">CONFIDENTIAL · FRAUD INVESTIGATION ARCHIVE</div>
            <div class="cover-title">금융사기 수사대</div>
            <div class="cover-subtitle">
                고전 기록실 형식으로 구성한 금융사기 대응 테스트입니다.<br>
                사건 기록을 읽고 가장 안전한 대응을 고른 뒤,<br>
                최종 수사 보고서에서 당신의 판단 성향을 확인해보세요.
            </div>
            <div class="divider-rule"></div>
            <div class="meta-row">
                <div class="meta-chip">사건 수 8건</div>
                <div class="meta-chip">예상 소요 3분</div>
                <div class="meta-chip">금융소비자 보호 주제</div>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown(
        """
        <div class="note-card">
            <div class="section-title">기록실 안내</div>
            <div class="section-text">
                본 서비스는 실제 금융사기 사례에서 자주 등장하는 문구와 상황을 교육용으로 재구성한 것입니다.
                링크 클릭, 송금, 개인정보 제공 전에 한 번 더 확인하는 습관을 기르는 데 목적이 있습니다.
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown(
        """
        <div class="note-card">
            <div class="section-title">이용 원칙</div>
            <div class="section-text">
                본 페이지는 특정 금융기관의 공식 서비스가 아니며, 이름·계좌번호·연락처 등 민감한 개인정보를 입력받지 않습니다.
                판단 연습을 위한 탐구형 웹앱입니다.
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    c1, c2 = st.columns([2, 1])
    with c1:
        if st.button("사건 기록 열기", type="primary", use_container_width=True):
            st.session_state.screen = "quiz"
            st.session_state.current = 0
            st.rerun()
    with c2:
        st.button("개인정보 미수집", disabled=True, use_container_width=True)

elif st.session_state.screen == "quiz":
    idx = st.session_state.current
    q = QUESTIONS[idx]
    st.progress(idx / len(QUESTIONS), text=f"진행 기록 {idx} / {len(QUESTIONS)}")

    st.markdown(
        f"""
        <div class="case-card">
            <div class="case-header">
                <div class="file-no">CASE FILE {q['case_no']}</div>
                <div class="tag-box">{q['tag']}</div>
            </div>
            <div class="case-title">{q['title']}</div>
            <div class="scenario-box">{q['scenario']}</div>
            <div class="memo-box"><b>수사 메모</b><br>{q['memo']}</div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown("#### 다음 중 가장 안전한 대응을 고르세요.")
    selected = st.session_state.answers.get(idx)

    if selected is None:
        for i, choice in enumerate(q["choices"]):
            if st.button(f"{chr(65+i)}. {choice}", key=f"choice_{idx}_{i}", use_container_width=True):
                st.session_state.answers[idx] = i
                st.rerun()
    else:
        correct = selected == q["answer"]
        for i, choice in enumerate(q["choices"]):
            st.button(f"{chr(65+i)}. {choice}", key=f"locked_{idx}_{i}", disabled=True, use_container_width=True)

        st.markdown("#### 사건 분석")
        if correct:
            st.markdown(
                f'<div class="result-good"><b>판정: 적절한 대응</b><br>{q["analysis"]}</div>',
                unsafe_allow_html=True,
            )
        else:
            best = q["choices"][q["answer"]]
            st.markdown(
                f'<div class="result-bad"><b>판정: 추가 검토 필요</b><br>가장 안전한 대응은 <b>{best}</b>입니다.<br>{q["analysis"]}</div>',
                unsafe_allow_html=True,
            )

        next_label = "최종 수사 보고서 보기" if idx == len(QUESTIONS) - 1 else "다음 기록 보기"
        c1, c2 = st.columns([3, 1.3])
        with c1:
            if st.button(next_label, type="primary", use_container_width=True):
                if idx == len(QUESTIONS) - 1:
                    st.session_state.screen = "result"
                else:
                    st.session_state.current += 1
                st.rerun()
        with c2:
            if st.button("처음으로", type="secondary", use_container_width=True):
                reset_app()
                st.rerun()

else:
    correct_count = sum(1 for i, q in enumerate(QUESTIONS) if st.session_state.answers.get(i) == q["answer"])
    score = round(correct_count / len(QUESTIONS) * 100)
    grade_code, grade_name, grade_desc = get_grade(score)
    weak = weak_tag()

    st.markdown(
        """
        <div class="report-card">
            <div class="archival-stamp">FINAL INVESTIGATION REPORT</div>
            <div class="stamp-title">최종 수사 보고서</div>
            <div class="section-text">응답 기록을 바탕으로 당신의 금융사기 대응 성향을 정리했습니다.</div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    c1, c2, c3 = st.columns(3)
    with c1:
        st.markdown(
            f'<div class="grade-box"><div class="small-label">최종 점수</div><div class="grade-code">{score}</div><div class="grade-name">/ 100</div></div>',
            unsafe_allow_html=True,
        )
    with c2:
        st.markdown(
            f'<div class="grade-box"><div class="small-label">등급</div><div class="grade-code">{grade_code}</div><div class="grade-name">{grade_name}</div></div>',
            unsafe_allow_html=True,
        )
    with c3:
        st.markdown(
            f'<div class="grade-box"><div class="small-label">취약 유형</div><div class="grade-name" style="margin-top:18px;">{weak}</div></div>',
            unsafe_allow_html=True,
        )

    st.markdown(
        f"""
        <div class="note-card">
            <div class="section-title">평가 소견</div>
            <div class="section-text">{grade_desc}</div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    with st.expander("사건별 판정 기록 보기", expanded=True):
        for i, q in enumerate(QUESTIONS):
            ok = st.session_state.answers.get(i) == q["answer"]
            status = "적절한 대응" if ok else "추가 검토 필요"
            st.markdown(
                f"""
                <div class="summary-item">
                    <b>CASE FILE {q['case_no']} · {q['title']}</b><br>
                    판정: {status}<br>
                    안전한 대응: {q['choices'][q['answer']]}<br>
                    <span style="color:#6e5a43;">{q['analysis']}</span>
                </div>
                """,
                unsafe_allow_html=True,
            )

    st.markdown(
        """
        <div class="note-card">
            <div class="section-title">실제 피해가 의심된다면</div>
            <div class="section-text">
                1) 즉시 거래 금융회사 또는 112에 신고하기<br>
                2) 지급정지 가능 여부 문의하기<br>
                3) 문자·통화·이체 기록을 삭제하지 말고 보관하기<br>
                4) 의심 앱을 설치했다면 기기 점검 및 기관 안내 따르기
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    share_text = (
        f"금융사기 수사대 결과\n"
        f"점수: {score}점 ({correct_count}/8)\n"
        f"등급: {grade_name} ({grade_code})\n"
        f"취약 유형: {weak}"
    )
    st.code(share_text, language=None)

    c1, c2 = st.columns([2, 1])
    with c1:
        if st.button("다시 조사하기", type="primary", use_container_width=True):
            reset_app()
            st.rerun()
    with c2:
        st.button("기록 보존 완료", disabled=True, use_container_width=True)

st.markdown('<div class="final-note">ⓘ 금융소비자 교육용 개인 프로젝트 · 고전 기록실 콘셉트의 Streamlit 앱</div>', unsafe_allow_html=True)
