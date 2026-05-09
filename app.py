import textwrap
from datetime import datetime

import pandas as pd
import streamlit as st

# =========================
# 0. 기본 설정
# =========================
st.set_page_config(
    page_title="KODEX CHECKPOINT",
    page_icon="📘",
    layout="centered",
    initial_sidebar_state="collapsed",
)

# =========================
# 1. CSS
# =========================
st.markdown(
    """
<style>
@import url('https://fonts.googleapis.com/css2?family=Noto+Sans+KR:wght@400;500;700;800;900&display=swap');

html, body, [class*="css"] {
    font-family: 'Noto Sans KR', sans-serif;
}

.stApp {
    background: linear-gradient(180deg, #EEF3FF 0%, #F7F9FC 100%);
}

.block-container {
    max-width: 440px;
    padding-top: 0.7rem;
    padding-bottom: 2rem;
}

#MainMenu, header, footer {
    visibility: hidden;
}

.phone-body {
    background:#F4F6FA;
    border:1px solid #DDE5F2;
    border-radius:28px;
    overflow:hidden;
    box-shadow:0 18px 45px rgba(15,23,42,0.16);
    margin-bottom:12px;
}

.phone-top {
    background:#243C9B;
    color:#fff;
    border-radius:28px 28px 0 0;
    padding:12px 20px 10px;
    display:flex;
    justify-content:space-between;
    font-size:14px;
    font-weight:900;
}

.phone-content {
    padding:18px;
}

.top-row {
    display:flex;
    align-items:center;
    justify-content:space-between;
    margin-bottom:18px;
}

.logo {
    font-size:18px;
    font-weight:900;
    color:#111827;
}

.logo span {
    color:#1155FF;
}

.search-box {
    background:#fff;
    border:3px solid #1155FF;
    border-radius:999px;
    padding:15px 18px;
    color:#8A8F98;
    font-size:16px;
    font-weight:800;
    margin-bottom:16px;
}

.hero-card {
    background:linear-gradient(135deg, #031342 0%, #071E68 55%, #0B318D 100%);
    border-radius:28px;
    padding:24px 22px;
    color:#fff;
    margin:16px 0;
    min-height:190px;
}

.hero-pill {
    background:#fff;
    color:#111827;
    padding:8px 14px;
    border-radius:999px;
    font-size:14px;
    font-weight:900;
    display:inline-block;
    margin-bottom:48px;
}

.hero-title {
    font-size:23px;
    font-weight:900;
    line-height:1.45;
    margin-bottom:12px;
}

.hero-link {
    border-top:1px solid rgba(255,255,255,0.25);
    padding-top:12px;
    font-size:16px;
    font-weight:900;
}

.check-card {
    background:linear-gradient(135deg, #EAF2FF 0%, #FFFFFF 100%);
    border:1.5px solid #C8DBFF;
    border-radius:26px;
    padding:20px;
    margin:16px 0;
    position:relative;
}

.check-card::after {
    content:"✓";
    position:absolute;
    right:22px;
    bottom:18px;
    color:#1155FF;
    font-size:52px;
    font-weight:900;
    opacity:0.16;
}

.badge {
    display:inline-block;
    background:#1155FF;
    color:#fff;
    border-radius:999px;
    padding:4px 9px;
    font-size:11px;
    font-weight:900;
    margin-bottom:8px;
}

.badge-soft {
    display:inline-block;
    background:#EAF2FF;
    color:#1155FF;
    border-radius:999px;
    padding:6px 11px;
    font-size:12px;
    font-weight:900;
    margin-bottom:8px;
}

.check-title {
    color:#1155FF;
    font-size:21px;
    font-weight:900;
    margin-bottom:8px;
    line-height:1.35;
}

.check-desc {
    color:#374151;
    font-size:14px;
    line-height:1.55;
    font-weight:700;
}

.section-title {
    font-size:22px;
    font-weight:900;
    margin:20px 0 10px;
    color:#111827;
}

.caption {
    color:#6B7280;
    font-size:13px;
    line-height:1.55;
    font-weight:700;
}

.note-text {
    color:#6B7280;
    font-size:12px;
    line-height:1.55;
    font-weight:600;
    margin-top:8px;
}

.product-card,
.info-card,
.product-list-card {
    background:#fff;
    border-radius:24px;
    padding:20px 18px;
    margin:12px 0;
    border:1px solid #E5E7EB;
    box-shadow:0 6px 18px rgba(15,23,42,0.05);
}

.product-name {
    font-size:21px;
    font-weight:900;
    color:#111827;
    margin-bottom:8px;
}

.product-code {
    color:#6B7280;
    font-size:13px;
    font-weight:700;
}

.product-meta {
    font-size:13px;
    color:#6B7280;
    font-weight:700;
    line-height:1.5;
}

.product-rate {
    color:#E11D48;
    font-size:28px;
    font-weight:900;
    text-align:right;
}

.blue-down {
    color:#2563EB;
    font-size:13px;
    font-weight:800;
    text-align:right;
}

.price-small {
    font-size:14px;
    font-weight:900;
    color:#111827;
    text-align:right;
}

.progress-big {
    font-size:36px;
    font-weight:900;
    color:#1155FF;
    margin-bottom:6px;
}

.progress-track {
    background:#E5E7EB;
    height:8px;
    border-radius:999px;
    overflow:hidden;
    margin-bottom:20px;
}

.progress-fill {
    background:#1155FF;
    height:8px;
    border-radius:999px;
}

.step-chip {
    display:inline-block;
    background:#EAF2FF;
    color:#1155FF;
    padding:6px 11px;
    border-radius:999px;
    font-size:12px;
    font-weight:900;
    margin-bottom:10px;
}

.question-title {
    font-size:24px;
    line-height:1.42;
    font-weight:900;
    color:#111827;
    margin-bottom:8px;
}

.question-guide {
    background:#F2F6FF;
    border:1px solid #D6E4FF;
    border-radius:18px;
    padding:14px 15px;
    color:#374151;
    font-size:13px;
    line-height:1.55;
    font-weight:700;
    margin:14px 0 18px;
}

.result-main {
    background:#fff;
    border-radius:26px;
    padding:24px 20px;
    text-align:center;
    border:1px solid #E5E7EB;
    box-shadow:0 8px 25px rgba(15,23,42,0.06);
    margin-bottom:16px;
}

.result-emoji {
    width:74px;
    height:74px;
    border-radius:50%;
    background:#EAF2FF;
    display:flex;
    align-items:center;
    justify-content:center;
    margin:0 auto 12px;
    font-size:35px;
}

.invest-code {
    display:inline-block;
    background:#EDEBFF;
    color:#3C3489;
    padding:13px 22px;
    border-radius:16px;
    font-size:25px;
    font-weight:900;
    letter-spacing:5px;
    margin:8px 0 10px;
}

.result-type {
    font-size:24px;
    font-weight:900;
    color:#1155FF;
    margin-bottom:8px;
    line-height:1.35;
}

.invest-type {
    font-size:21px;
    font-weight:900;
    color:#111827;
    margin-bottom:8px;
}

.result-desc {
    font-size:14px;
    color:#374151;
    line-height:1.6;
    font-weight:700;
}

.info-title {
    font-size:18px;
    font-weight:900;
    color:#111827;
    margin-bottom:12px;
}

.summary-list {
    margin:0;
    padding-left:20px;
    color:#374151;
    font-size:14px;
    line-height:1.75;
    font-weight:700;
}

.trait-grid {
    display:grid;
    grid-template-columns:1fr 1fr;
    gap:10px;
    margin-top:12px;
}

.trait-box {
    background:#F7FAFF;
    border:1px solid #D9E7FF;
    border-radius:18px;
    padding:14px;
    text-align:center;
}

.trait-main {
    font-size:19px;
    font-weight:900;
    color:#1155FF;
    margin-bottom:2px;
}

.trait-sub {
    font-size:12px;
    font-weight:700;
    color:#6B7280;
}

.score-row {
    margin-bottom:16px;
}

.score-head {
    display:flex;
    justify-content:space-between;
    font-size:13px;
    font-weight:900;
    color:#374151;
    margin-bottom:7px;
}

.score-bg {
    height:9px;
    background:#E5E7EB;
    border-radius:999px;
    overflow:hidden;
}

.score-fill {
    height:9px;
    background:#1155FF;
    border-radius:999px;
}

.status-row {
    display:flex;
    justify-content:space-between;
    align-items:center;
    padding:13px 0;
    border-bottom:1px solid #EEF2F7;
}

.status-row:last-child {
    border-bottom:none;
}

.status-label {
    font-size:14px;
    font-weight:900;
    color:#111827;
}

.status-badge {
    border-radius:999px;
    padding:6px 11px;
    font-size:12px;
    font-weight:900;
}

.status-good {
    background:#DCFCE7;
    color:#15803D;
}

.status-mid {
    background:#FEF3C7;
    color:#B45309;
}

.status-low {
    background:#EAF2FF;
    color:#1155FF;
}

.point-item {
    background:#F8FAFC;
    border:1px solid #E5E7EB;
    border-radius:17px;
    padding:14px 14px;
    margin-bottom:10px;
}

.point-name {
    font-size:15px;
    font-weight:900;
    color:#111827;
    margin-bottom:4px;
}

.point-desc {
    font-size:13px;
    color:#6B7280;
    line-height:1.45;
    font-weight:700;
}

.insight {
    background:#F0F7FF;
    border:1px solid #C8DBFF;
    border-radius:18px;
    padding:15px;
    color:#1E3A8A;
    font-size:13px;
    line-height:1.6;
    font-weight:800;
    margin:12px 0;
}

.tag-wrap {
    display:flex;
    flex-wrap:wrap;
    gap:6px;
    margin:10px 0;
}

.tag {
    display:inline-block;
    background:#F1F5F9;
    color:#334155;
    border-radius:999px;
    padding:5px 10px;
    font-size:12px;
    font-weight:800;
}

.compare-chip {
    display:inline-block;
    background:#EEF0F4;
    color:#6B7280;
    border-radius:999px;
    padding:6px 12px;
    font-size:12px;
    font-weight:900;
}

.similar-card {
    background:linear-gradient(180deg, #FFFFFF 0%, #F8FBFF 100%);
    border:1px solid #DDE8FF;
    border-radius:18px;
    padding:16px;
    margin-bottom:12px;
}

.similar-top {
    display:flex;
    justify-content:space-between;
    gap:10px;
    align-items:center;
    margin-bottom:8px;
}

.similar-name {
    font-size:16px;
    font-weight:900;
    color:#111827;
}

.match-badge {
    background:#EAF2FF;
    color:#1155FF;
    border-radius:999px;
    padding:5px 10px;
    font-size:12px;
    font-weight:900;
    white-space:nowrap;
}

.price-grid {
    display:grid;
    grid-template-columns:1fr 1fr;
    gap:10px;
    margin-bottom:14px;
}

.price-box {
    background:#fff;
    border-radius:22px;
    padding:16px 14px;
    border:1px solid #E5E7EB;
    box-shadow:0 6px 18px rgba(15,23,42,0.04);
}

.price-label {
    font-size:12px;
    font-weight:900;
    margin-bottom:12px;
    color:#374151;
}

.price-num {
    font-size:23px;
    font-weight:900;
    text-align:right;
}

.price-up {
    color:#EF233C;
    font-size:12px;
    font-weight:900;
    text-align:right;
}

.purple-hero {
    background:#3B007A;
    color:white;
    border-radius:28px;
    padding:26px 20px;
    margin-bottom:14px;
    position:relative;
    overflow:hidden;
}

.purple-title {
    font-size:26px;
    font-weight:900;
    line-height:1.35;
    margin:18px 0 8px;
}

.purple-desc {
    font-size:13px;
    line-height:1.55;
    font-weight:700;
    color:rgba(255,255,255,0.9);
}

.tab-row {
    display:flex;
    flex-wrap:wrap;
    gap:7px;
    background:#fff;
    border-radius:20px;
    padding:14px;
    border:1px solid #E5E7EB;
    margin-bottom:14px;
}

.tab-chip {
    background:#F8FAFC;
    border:1px solid #E5E7EB;
    border-radius:999px;
    padding:7px 10px;
    font-size:12px;
    font-weight:900;
    color:#111827;
}

.tab-active {
    background:#1155FF;
    color:white;
    border-color:#1155FF;
}

.nav-shell {
    background:#FFFFFF;
    border:1px solid #D9E2F1;
    border-radius:24px;
    padding:8px;
    box-shadow:0 8px 20px rgba(15,23,42,0.06);
    margin-top:10px;
    margin-bottom:4px;
}

.stButton > button {
    border-radius:16px !important;
    font-weight:900 !important;
    min-height:47px !important;
    border:1.3px solid #D6E4FF !important;
}

button[kind="primary"] {
    background-color:#1155FF !important;
    border:none !important;
}

div[data-testid="stRadio"] > label {
    display:none;
}

div[data-testid="stRadio"] label {
    background:#fff;
    border:1.5px solid #D9E2F1;
    border-radius:18px;
    padding:13px 14px;
    margin-bottom:8px;
    width:100%;
    font-weight:900;
}

div[data-testid="stRadio"] label:hover {
    border-color:#1155FF;
    background:#F2F6FF;
}
</style>
""",
    unsafe_allow_html=True,
)

# =========================
# 2. HTML helper
# =========================
def html(markup: str):
    cleaned = textwrap.dedent(markup).strip()
    cleaned = "\n".join(line.strip() for line in cleaned.splitlines() if line.strip())
    st.markdown(cleaned, unsafe_allow_html=True)


def br(text: str):
    return text.replace("\n", "<br>")


def now_text():
    return datetime.now().strftime("%Y.%m.%d %H:%M")


# =========================
# 3. ETF 데이터
# 실제 서비스에서는 공식/제휴 API로 대체
# =========================
ETF_PRODUCTS = [
    {
        "name": "KODEX 레버리지",
        "code": "122630",
        "category": "leveraged",
        "region": "국내",
        "kind": "파생",
        "price": 149855,
        "nav": 149720,
        "volume": 2154489,
        "return_1w": 33.3,
        "change": -2015,
        "change_pct": -1.32,
        "tags": ["레버리지", "변동성", "단기확인"],
        "desc": "국내 주식시장 일간 흐름을 레버리지 방식으로 추종하는 ETF입니다.",
    },
    {
        "name": "KODEX 반도체레버리지",
        "code": "494310",
        "category": "theme",
        "region": "국내",
        "kind": "테마",
        "price": 128910,
        "nav": 128640,
        "volume": 1802331,
        "return_1w": 31.4,
        "change": -905,
        "change_pct": -0.69,
        "tags": ["반도체", "레버리지", "테마"],
        "desc": "반도체 테마와 레버리지 특성이 결합된 ETF입니다.",
    },
    {
        "name": "KODEX KRX300 레버리지",
        "code": "306950",
        "category": "leveraged",
        "region": "국내",
        "kind": "시장지수",
        "price": 108840,
        "nav": 108520,
        "volume": 923810,
        "return_1w": 30.7,
        "change": -1415,
        "change_pct": -1.28,
        "tags": ["KRX300", "레버리지", "시장지수"],
        "desc": "KRX300 지수 흐름을 레버리지 방식으로 확인할 수 있는 ETF입니다.",
    },
    {
        "name": "KODEX 증권",
        "code": "102970",
        "category": "theme",
        "region": "국내",
        "kind": "섹터",
        "price": 31575,
        "nav": 31520,
        "volume": 551204,
        "return_1w": 19.5,
        "change": -675,
        "change_pct": -2.10,
        "tags": ["증권", "섹터", "국내"],
        "desc": "국내 증권업종 흐름을 확인할 수 있는 섹터형 ETF입니다.",
    },
    {
        "name": "KODEX 200IT TR",
        "code": "363580",
        "category": "domestic_index",
        "region": "국내",
        "kind": "시장지수",
        "price": 53240,
        "nav": 53190,
        "volume": 387610,
        "return_1w": 18.6,
        "change": -500,
        "change_pct": -0.93,
        "tags": ["IT", "TR", "국내"],
        "desc": "국내 IT 업종 중심의 지수 흐름을 확인할 수 있는 ETF입니다.",
    },
    {
        "name": "KODEX 200ESG",
        "code": "337160",
        "category": "domestic_index",
        "region": "국내",
        "kind": "시장지수",
        "price": 48015,
        "nav": 47980,
        "volume": 220914,
        "return_1w": 17.9,
        "change": -235,
        "change_pct": -0.49,
        "tags": ["ESG", "KOSPI200", "국내"],
        "desc": "ESG 관점의 국내 대표지수형 ETF입니다.",
    },
    {
        "name": "KODEX 미국S&P500",
        "code": "379800",
        "category": "global_index",
        "region": "해외",
        "kind": "시장지수",
        "price": 24375,
        "nav": 24325,
        "volume": 11523631,
        "return_1w": 3.8,
        "change": 175,
        "change_pct": 0.72,
        "tags": ["S&P500", "미국", "환율"],
        "desc": "미국 대표지수인 S&P500 흐름을 확인할 수 있는 ETF입니다.",
    },
    {
        "name": "KODEX 미국나스닥100",
        "code": "379810",
        "category": "global_index",
        "region": "해외",
        "kind": "시장지수",
        "price": 29750,
        "nav": 29712,
        "volume": 3208144,
        "return_1w": 4.6,
        "change": 260,
        "change_pct": 0.88,
        "tags": ["나스닥100", "미국", "기술주"],
        "desc": "미국 기술주 중심 지수 흐름을 확인할 수 있는 ETF입니다.",
    },
    {
        "name": "KODEX 배당성장",
        "code": "211900",
        "category": "dividend",
        "region": "국내",
        "kind": "배당",
        "price": 16210,
        "nav": 16185,
        "volume": 421880,
        "return_1w": 2.4,
        "change": 65,
        "change_pct": 0.40,
        "tags": ["배당", "분배금", "장기"],
        "desc": "배당 성장 관점에서 구성종목과 분배금 정보를 함께 확인하는 ETF입니다.",
    },
    {
        "name": "KODEX AI전력핵심설비",
        "code": "487230",
        "category": "theme",
        "region": "국내",
        "kind": "테마",
        "price": 14820,
        "nav": 14790,
        "volume": 1824501,
        "return_1w": 12.2,
        "change": 220,
        "change_pct": 1.51,
        "tags": ["AI전력", "테마", "변동성"],
        "desc": "AI 전력 인프라 관련 기업에 집중된 테마형 ETF입니다.",
    },
]

# =========================
# 4. 질문 데이터
# =========================
questions = [
    {
        "id": "q1",
        "step": "STEP 1. 내 돈 상태 점검",
        "title": "지금 ETF를 보려는 돈은\n어떤 돈인가요?",
        "options": [
            ("A", "생활비와 따로 구분하지 않은 돈이다", {"fund": 0}, "자금 상태 점검"),
            ("B", "이번 달 생활비를 제외하고 남은 돈이다", {"fund": 1}, None),
            ("C", "비상금은 따로 두고 남은 여유자금이다", {"fund": 2}, None),
            ("D", "생활비·비상금·단기 지출 예정금을 모두 제외한 투자 가능 금액이다", {"fund": 3}, None),
        ],
    },
    {
        "id": "q2",
        "step": "STEP 2. 투자 목적 점검",
        "title": "ETF를 보려는 목적에\n가장 가까운 것은?",
        "options": [
            ("A", "요즘 많이 오른다고 해서 궁금하다", {"goal": 0, "return": 2, "name": 1}, "목표 설정"),
            ("B", "단기 수익 기회를 보고 싶다", {"goal": 1, "return": 2}, None),
            ("C", "ETF 투자 공부를 해보고 싶다", {"goal": 2, "structure": 1}, None),
            ("D", "장기적으로 자산관리를 시작하고 싶다", {"goal": 3, "period": 1, "risk": 1}, None),
        ],
    },
    {
        "id": "q3",
        "step": "STEP 2. 투자 기간 점검",
        "title": "이 돈을 어느 정도 기간 동안\n투자할 수 있나요?",
        "options": [
            ("A", "1개월 안에도 쓸 수 있다", {"period": 0, "return": 2}, "투자 기간 설정"),
            ("B", "3~6개월 정도는 가능하다", {"period": 1}, None),
            ("C", "1년 이상은 가능하다", {"period": 2, "long": 1}, None),
            ("D", "장기적으로 꾸준히 가져갈 수 있다", {"period": 3, "long": 2}, None),
        ],
    },
    {
        "id": "q4",
        "step": "STEP 3. ETF 확인 습관 진단",
        "title": "ETF를 볼 때\n가장 먼저 확인하는 것은?",
        "options": [
            ("A", "최근 수익률", {"return": 2}, None),
            ("B", "현재가와 차트 흐름", {"return": 1, "chart": 2}, None),
            ("C", "기초지수와 구성종목", {"structure": 2}, None),
            ("D", "총보수와 유의사항", {"risk": 2}, None),
        ],
    },
    {
        "id": "q5",
        "step": "STEP 3. ETF 확인 습관 진단",
        "title": "ETF 상품명에\n익숙한 이름이 보이면?",
        "options": [
            ("A", "익숙한 이름이라 더 믿음이 간다", {"name": 2}, None),
            ("B", "사람들이 많이 보는 상품인지 먼저 본다", {"name": 1, "return": 1}, None),
            ("C", "어떤 지수를 따라가는지 확인한다", {"structure": 2}, None),
            ("D", "구성종목, 총보수, 유의사항을 함께 확인한다", {"structure": 1, "risk": 1}, None),
        ],
    },
    {
        "id": "q6",
        "step": "STEP 4. 상품정보 확인 행동",
        "title": "상품 상세에서\n가장 먼저 누르고 싶은 탭은?",
        "options": [
            ("A", "수익률", {"return": 2}, None),
            ("B", "기준가와 차트", {"return": 1, "chart": 2}, None),
            ("C", "구성종목", {"structure": 2}, None),
            ("D", "상품정보와 유의사항", {"risk": 2}, None),
        ],
    },
]

# =========================
# 5. 세션 상태
# =========================
defaults = {
    "page": "home",
    "q_idx": 0,
    "answers": {},
    "selected_etf_code": "379800",
    "sort_metric": "1주 수익률",
    "sort_order": "높은 순",
    "selected_region": "전체",
    "compare_codes": [],
    "saved": False,
    "product_tab": "투자포인트",
    "history": [],
}

for key, value in defaults.items():
    if key not in st.session_state:
        st.session_state[key] = value


# =========================
# 6. 기본 함수
# =========================
def go(page: str, add_history: bool = True):
    current_page = st.session_state.get("page", "home")

    if add_history and current_page != page:
        st.session_state.history.append(current_page)

        if len(st.session_state.history) > 20:
            st.session_state.history = st.session_state.history[-20:]

    st.session_state.page = page
    st.rerun()


def go_back(default_page: str = "home"):
    if st.session_state.history:
        previous_page = st.session_state.history.pop()
        st.session_state.page = previous_page
    else:
        st.session_state.page = default_page

    st.rerun()


def start():
    current_page = st.session_state.get("page", "home")

    st.session_state.page = "checklist"
    st.session_state.q_idx = 0
    st.session_state.answers = {}
    st.session_state.saved = False
    st.session_state.product_tab = "투자포인트"

    if current_page != "checklist":
        st.session_state.history.append(current_page)

    st.rerun()


def select_etf(code: str):
    st.session_state.selected_etf_code = code
    st.session_state.product_tab = "투자포인트"
    go("product_detail")


def get_etf_by_code(code: str):
    for item in ETF_PRODUCTS:
        if item["code"] == code:
            return item
    return ETF_PRODUCTS[0]


def phone_header():
    html("""
    <div class="phone-body">
    <div class="phone-top">
    <div>1:24</div>
    <div>▮▮▮ Wi-Fi 41%</div>
    </div>
    <div class="phone-content">
    """)


def phone_footer():
    html("</div></div>")


def page_title_bar(title: str, default_back: str = "home"):
    c1, c2, c3 = st.columns([0.5, 3, 0.5])

    with c1:
        if st.button("‹", key=f"back_{title}_{st.session_state.page}", use_container_width=True):
            go_back(default_back)

    with c2:
        st.markdown(
            f"""
            <div style="
                text-align:center;
                font-size:15px;
                font-weight:900;
                color:#111827;
                padding-top:8px;
                padding-bottom:12px;
            ">
                {title}
            </div>
            """,
            unsafe_allow_html=True,
        )

    with c3:
        st.markdown("<div style='height:38px;'></div>", unsafe_allow_html=True)


def bottom_nav(active="home"):
    html("""
    <div class="nav-shell">
    <div style="text-align:center; font-size:12px; font-weight:900; color:#6B7280;">
    KODEX CHECKPOINT
    </div>
    </div>
    """)

    cols = st.columns(5)

    nav_items = [
        ("홈", "home"),
        ("전체상품", "products"),
        ("체크", "checkpoint"),
        ("투자정보", "insight"),
        ("이벤트", "event"),
    ]

    for col, (label, page) in zip(cols, nav_items):
        with col:
            button_label = f"● {label}" if page == active else label

            if st.button(button_label, key=f"nav_{active}_{page}", use_container_width=True):
                if page == "checkpoint":
                    if len(st.session_state.answers) == len(questions):
                        go("report")
                    else:
                        start()
                else:
                    go(page)


def tag_html(tags):
    return "".join([f'<span class="tag">{tag}</span>' for tag in tags])


def score_bar(label, value):
    return f"""
    <div class="score-row">
    <div class="score-head"><span>{label}</span><span>{value}/100</span></div>
    <div class="score-bg"><div class="score-fill" style="width:{value}%;"></div></div>
    </div>
    """


def status_badge(value):
    if value >= 70:
        return '<span class="status-badge status-good">잘 점검됨</span>'
    if value >= 40:
        return '<span class="status-badge status-mid">조금 더 확인</span>'
    return '<span class="status-badge status-low">추가 확인</span>'


def status_row(label, value):
    return f"""
    <div class="status-row">
    <div class="status-label">{label}</div>
    {status_badge(value)}
    </div>
    """


def point_item(title, desc):
    return f"""
    <div class="point-item">
    <div class="point-name">✓ {title}</div>
    <div class="point-desc">{desc}</div>
    </div>
    """


def similar_card(etf, pct=None, weak=None):
    items = get_product_checkpoints(etf, pct, weak)

    return f"""
    <div class="similar-card">
    <div class="similar-top">
    <div class="similar-name">{etf["name"]}</div>
    <div class="match-badge">함께 비교</div>
    </div>
    <div class="point-desc">{etf["desc"]}</div>
    <div class="tag-wrap">{tag_html(items[:3])}</div>
    </div>
    """
# =========================
# 7. 분석 로직
# =========================
def get_selected_options():
    selected = []

    for q in questions:
        value = st.session_state.answers.get(q["id"])

        if not value:
            continue

        for opt in q["options"]:
            code, text, scores, weakness = opt

            if value == f"{code}. {text}":
                selected.append((q, opt))
                break

    return selected


def calculate_scores():
    axes = ["fund", "goal", "period", "return", "structure", "risk", "name", "chart", "long"]
    raw = {axis: 0 for axis in axes}
    max_scores = {axis: 0 for axis in axes}
    weaknesses = []

    for q in questions:
        for axis in axes:
            max_scores[axis] += max([opt[2].get(axis, 0) for opt in q["options"]])

    for q, opt in get_selected_options():
        _, _, scores, weakness = opt

        for axis, value in scores.items():
            raw[axis] += value

        if weakness:
            weaknesses.append(weakness)

    pct = {}

    for axis in axes:
        pct[axis] = round(raw[axis] / max_scores[axis] * 100) if max_scores[axis] else 0

    goal_period_raw = raw["goal"] + raw["period"]
    goal_period_max = max_scores["goal"] + max_scores["period"]
    pct["goal_period"] = round(goal_period_raw / goal_period_max * 100) if goal_period_max else 0

    return raw, pct, weaknesses


def safe_scores():
    if len(st.session_state.answers) < len(questions):
        return None, None, None

    return calculate_scores()


def classify_habit(pct, weaknesses):
    if pct["structure"] >= 65 and pct["risk"] >= 60 and pct["fund"] >= 50 and pct["goal_period"] >= 50:
        return {
            "mbti": "BL형",
            "type": "균형 점검형",
            "emoji": "🧭",
            "desc": "ETF를 보기 전 돈 상태와 상품 정보를 비교적 균형 있게 확인하는 유형입니다.",
            "priority": ["기초지수", "구성종목", "총보수·유의사항"],
        }

    if pct["name"] >= 50:
        return {
            "mbti": "BN형",
            "type": "익숙한 이름에 끌리는 타입",
            "emoji": "🏷️",
            "desc": "익숙한 브랜드명이나 상품명에 먼저 반응하는 유형입니다.",
            "priority": ["기초지수", "구성종목", "투자포인트"],
        }

    if pct["chart"] >= 60:
        return {
            "mbti": "CT형",
            "type": "차트 먼저 보는 타입",
            "emoji": "📈",
            "desc": "현재가와 단기 흐름을 먼저 보는 유형입니다.",
            "priority": ["현재가·기준가", "수익률 기간", "구성종목"],
        }

    if pct["return"] >= 60:
        return {
            "mbti": "SR형",
            "type": "수익률 먼저 보는 타입",
            "emoji": "🔥",
            "desc": "최근 수익률과 상승률에 빠르게 반응하는 유형입니다.",
            "priority": ["수익률 기간", "구성종목", "총보수·유의사항"],
        }

    if pct["risk"] < 50:
        return {
            "mbti": "FR형",
            "type": "비용·리스크 보완형",
            "emoji": "⚠️",
            "desc": "총보수와 유의사항을 한 번 더 확인하면 좋은 유형입니다.",
            "priority": ["총보수·유의사항", "상품정보", "기준가"],
        }

    return {
        "mbti": "CP형",
        "type": "구성종목 보완형",
        "emoji": "🧩",
        "desc": "ETF 안에 어떤 기업들이 들어있는지 한 번 더 확인하면 좋은 유형입니다.",
        "priority": ["구성종목", "기초지수", "총보수·유의사항"],
    }


def get_invest_mbti(pct):
    stable_base = pct["fund"] + pct["goal_period"] + pct["structure"] + pct["risk"]
    growth_base = pct["return"] + pct["chart"] + pct["name"]

    s_or_g = "S" if stable_base >= growth_base else "G"
    d_or_c = "D" if pct["structure"] >= 45 or pct["risk"] >= 55 else "C"
    l_or_q = "L" if pct["period"] >= 50 else "Q"
    p_or_i = "P" if stable_base >= growth_base else "I"

    code = s_or_g + d_or_c + l_or_q + p_or_i

    trait_map = {
        "S": ("안정형", "리스크 성향"),
        "G": ("성장형", "리스크 성향"),
        "D": ("분산형", "투자 방식"),
        "C": ("집중형", "투자 방식"),
        "L": ("장기형", "투자 기간"),
        "Q": ("단기형", "투자 기간"),
        "P": ("계획형", "판단 방식"),
        "I": ("직관형", "판단 방식"),
    }

    traits = [trait_map[ch] for ch in code]

    if code[0] == "S" and code[2] == "L":
        title = "안정 추구형 장기 투자자"
        desc = "수익률보다 자금 상태와 장기적인 자산관리 흐름을 중시하는 편이에요."
    elif code[0] == "G" and code[3] == "I":
        title = "트렌드 반응형 ETF 탐색자"
        desc = "성장 테마, 수익률, 익숙한 상품명에 빠르게 반응하는 편이에요."
    elif code[1] == "D":
        title = "분산 선호형 ETF 탐색자"
        desc = "단일 정보보다 지수, 구성종목, 분산 구조를 함께 보려는 편이에요."
    else:
        title = "ETF 기준 점검형 탐색자"
        desc = "ETF를 볼 때 상품의 구조와 확인 기준을 함께 살펴보려는 편이에요."

    return {
        "code": code,
        "traits": traits,
        "title": title,
        "desc": desc,
    }


def missed_items(pct, weaknesses):
    items = []

    for w in weaknesses:
        if w not in items:
            items.append(w)

    if pct["fund"] < 50 and "자금 상태 점검" not in items:
        items.append("자금 상태 점검")

    if pct["goal_period"] < 50:
        for x in ["목표 설정", "투자 기간 설정"]:
            if x not in items:
                items.append(x)

    if pct["structure"] < 50:
        for x in ["기초지수", "구성종목"]:
            if x not in items:
                items.append(x)

    if pct["risk"] < 50:
        for x in ["총보수", "유의사항"]:
            if x not in items:
                items.append(x)

    return items or ["전반적으로 균형 있게 확인 중"]


def behavior_summary(pct, habit, missed):
    lines = []

    if pct["fund"] >= 70:
        lines.append("생활비·비상금과 투자 가능 금액을 비교적 잘 구분하고 있어요.")
    elif pct["fund"] >= 40:
        lines.append("생활비와 투자 가능 금액은 어느 정도 구분하고 있어요.")
    else:
        lines.append("ETF를 보기 전, 이 돈이 생활비와 분리된 투자 가능 금액인지 먼저 확인해보면 좋아요.")

    if pct["goal_period"] >= 70:
        lines.append("투자 목적과 기간을 비교적 명확하게 생각하고 있어요.")
    elif pct["goal_period"] >= 40:
        lines.append("투자 목적은 어느 정도 있지만, 투자 가능 기간을 더 구체적으로 정리하면 좋아요.")
    else:
        lines.append("ETF를 보기 전, 왜 투자하려는지와 얼마나 오래 가져갈 수 있는지 먼저 정리해보면 좋아요.")

    lines.append(f"ETF 확인 습관은 ‘{habit['type']}’에 가까워요.")

    if "전반적으로 균형 있게 확인 중" in missed:
        lines.append("기초지수·구성종목·총보수·유의사항을 함께 확인하는 습관을 유지하면 좋아요.")
    else:
        lines.append(f"특히 {', '.join(missed[:3])} 항목은 다음에 ETF를 볼 때 한 번 더 확인하면 좋아요.")

    return lines


def category_priority(category):
    category_map = {
        "domestic_index": ["기초지수", "구성종목", "현재가·기준가"],
        "global_index": ["해외지수", "환율 영향", "수익률 기간", "구성종목"],
        "dividend": ["분배금", "분배 기준", "총보수", "유의사항"],
        "theme": ["테마 집중도", "상위 구성종목", "변동성", "수익률 기간"],
        "leveraged": ["일간 추종 구조", "변동성", "단기 수익률 기간", "유의사항"],
    }

    return category_map.get(category, ["기초지수", "구성종목", "총보수"])


def get_product_checkpoints(etf, pct=None, weak=None):
    if pct is None:
        user_items = ["기초지수", "구성종목", "총보수·유의사항"]
    else:
        habit = classify_habit(pct, weak)
        user_items = habit["priority"]

    product_items = category_priority(etf["category"])
    merged = []

    for item in user_items + product_items:
        if item not in merged:
            merged.append(item)

    return merged[:4]


def checkpoint_to_tab(item):
    mapping = {
        "기초지수": "투자포인트 / 상품정보",
        "해외지수": "투자포인트 / 상품정보",
        "구성종목": "구성종목(PDF)",
        "상위 구성종목": "구성종목(PDF)",
        "수익률 기간": "수익률",
        "단기 수익률 기간": "수익률",
        "총보수": "상품정보",
        "총보수·유의사항": "상품정보",
        "유의사항": "상품정보",
        "현재가·기준가": "상단 현재가 / 기준가 iNAV",
        "기준가": "기준가",
        "거래량": "상단 거래량",
        "환율 영향": "상품정보 / 관련콘텐츠",
        "분배금": "분배금 / 상품정보",
        "분배 기준": "분배금 / 상품정보",
        "테마 집중도": "투자포인트 / 구성종목(PDF)",
        "변동성": "수익률 / 기준가",
        "일간 추종 구조": "상품정보 / 유의사항",
        "투자포인트": "투자포인트",
        "상품정보": "상품정보",
    }

    return mapping.get(item, "상품정보")


def checkpoint_desc(item, etf):
    desc = {
        "기초지수": f"{etf['name']}가 어떤 지수를 따라가는지 확인합니다.",
        "해외지수": "해외 시장 지수를 기준으로 움직이는 상품인지 확인합니다.",
        "구성종목": "ETF 안에 어떤 기업과 산업이 포함되어 있는지 확인합니다.",
        "상위 구성종목": "상위 종목 비중이 특정 기업에 몰려 있는지 확인합니다.",
        "수익률 기간": "1주, 1개월, 1년 등 어느 기간 기준 수익률인지 확인합니다.",
        "단기 수익률 기간": "단기 수익률은 기간에 따라 크게 달라질 수 있으니 기준 기간을 확인합니다.",
        "총보수": "ETF를 보유할 때 반영되는 비용을 확인합니다.",
        "총보수·유의사항": "보유 비용과 가격 변동 가능성을 함께 확인합니다.",
        "유의사항": "시장 상황에 따른 가격 변동과 원금 손실 가능성을 확인합니다.",
        "현재가·기준가": "현재 거래 가격과 기준가 흐름을 함께 확인합니다.",
        "기준가": "ETF의 순자산가치 흐름을 확인합니다.",
        "거래량": "시장에서 얼마나 활발하게 거래되는지 확인합니다.",
        "환율 영향": "해외 ETF의 경우 환율 변화가 수익률에 영향을 줄 수 있습니다.",
        "분배금": "분배금 지급 여부와 지급 기준을 확인합니다.",
        "분배 기준": "분배금이 어떤 기준과 주기로 지급되는지 확인합니다.",
        "테마 집중도": "특정 테마나 산업에 집중된 정도를 확인합니다.",
        "변동성": "테마형·레버리지 상품은 가격 변동이 커질 수 있어 기간별 흐름을 확인합니다.",
        "일간 추종 구조": "레버리지 상품은 일간 수익률을 추종하는 구조인지 확인합니다.",
        "투자포인트": "상품의 핵심 특징과 투자 포인트를 먼저 확인합니다.",
        "상품정보": "상품 구조, 총보수, 유의사항을 확인합니다.",
    }

    return desc.get(item, "상품정보를 기준 있게 확인합니다.")


def get_similar_etfs(pct, weak):
    if pct is None:
        target_categories = ["domestic_index", "global_index", "dividend"]
    else:
        habit = classify_habit(pct, weak)

        if habit["type"] == "수익률 먼저 보는 타입":
            target_categories = ["global_index", "theme", "leveraged"]
        elif habit["type"] == "익숙한 이름에 끌리는 타입":
            target_categories = ["domestic_index", "global_index"]
        elif habit["type"] == "비용·리스크 보완형":
            target_categories = ["domestic_index", "dividend", "global_index"]
        elif habit["type"] == "구성종목 보완형":
            target_categories = ["theme", "global_index", "domestic_index"]
        else:
            target_categories = ["domestic_index", "global_index", "dividend"]

    result = []

    for cat in target_categories:
        for item in ETF_PRODUCTS:
            if item["category"] == cat and item not in result:
                result.append(item)

            if len(result) >= 3:
                return result

    return result[:3]


# =========================
# 8. 데이터 로딩 / 상품 상세 탭 함수
# =========================
@st.cache_data(ttl=60)
def load_etf_products():
    # 실제 서비스에서는 여기에서 공식/제휴 API를 호출하면 됩니다.
    return pd.DataFrame(ETF_PRODUCTS)


def filter_and_sort_products(df):
    region = st.session_state.selected_region

    if region != "전체":
        df = df[df["region"] == region]

    sort_metric = st.session_state.sort_metric
    sort_order = st.session_state.sort_order

    if sort_metric == "1주 수익률":
        sort_col = "return_1w"
    elif sort_metric == "현재가":
        sort_col = "price"
    elif sort_metric == "거래량":
        sort_col = "volume"
    else:
        sort_col = "return_1w"

    ascending = sort_order == "낮은 순"

    return df.sort_values(sort_col, ascending=ascending)


def get_sample_holdings(etf):
    name = etf["name"]

    if "미국S&P500" in name:
        return pd.DataFrame([
            {"종목명": "Apple", "비중(%)": 7.1},
            {"종목명": "Microsoft", "비중(%)": 6.5},
            {"종목명": "NVIDIA", "비중(%)": 5.8},
            {"종목명": "Amazon", "비중(%)": 3.7},
            {"종목명": "Meta", "비중(%)": 2.4},
        ])

    if "나스닥" in name:
        return pd.DataFrame([
            {"종목명": "Microsoft", "비중(%)": 8.3},
            {"종목명": "Apple", "비중(%)": 7.9},
            {"종목명": "NVIDIA", "비중(%)": 7.4},
            {"종목명": "Amazon", "비중(%)": 5.2},
            {"종목명": "Broadcom", "비중(%)": 4.1},
        ])

    if "반도체" in name:
        return pd.DataFrame([
            {"종목명": "삼성전자", "비중(%)": 24.2},
            {"종목명": "SK하이닉스", "비중(%)": 21.7},
            {"종목명": "한미반도체", "비중(%)": 8.4},
            {"종목명": "리노공업", "비중(%)": 5.2},
            {"종목명": "DB하이텍", "비중(%)": 4.8},
        ])

    if "200ESG" in name:
        return pd.DataFrame([
            {"종목명": "삼성전자", "비중(%)": 20.3},
            {"종목명": "SK하이닉스", "비중(%)": 8.1},
            {"종목명": "현대차", "비중(%)": 6.2},
            {"종목명": "KB금융", "비중(%)": 4.4},
            {"종목명": "기아", "비중(%)": 4.1},
        ])

    return pd.DataFrame([
        {"종목명": "삼성전자", "비중(%)": 18.4},
        {"종목명": "SK하이닉스", "비중(%)": 9.3},
        {"종목명": "현대차", "비중(%)": 6.1},
        {"종목명": "NAVER", "비중(%)": 4.8},
        {"종목명": "LG에너지솔루션", "비중(%)": 4.2},
    ])


def render_detail_tabs():
    tabs = ["투자포인트", "상품정보", "수익률", "기준가", "구성종목(PDF)", "관련콘텐츠"]

    cols = st.columns([1, 1, 1, 1, 1.25, 1.25])

    for col, tab in zip(cols, tabs):
        with col:
            is_active = st.session_state.product_tab == tab
            label = f"● {tab}" if is_active else tab

            if st.button(label, key=f"detail_tab_{tab}", use_container_width=True):
                st.session_state.product_tab = tab
                st.rerun()


def render_detail_tab_content(etf):
    tab = st.session_state.product_tab

    if tab == "투자포인트":
        html(f"""
        <div class="info-card">
        <div class="info-title">투자포인트</div>
        {point_item("이 ETF가 어떤 상품인지", etf["desc"])}
        {point_item("핵심 확인 포인트", f"{etf['name']}는 {etf['region']} · {etf['kind']} 유형 ETF입니다. 먼저 어떤 지수·테마를 추종하는지 확인해보세요.")}
        {point_item("이런 경우 더 확인", "최근 수익률이 좋아 보여도, 구성종목과 비용·유의사항을 함께 보면 더 기준 있게 볼 수 있어요.")}
        <div class="note-text">프로토타입 예시 화면입니다.</div>
        </div>
        """)

    elif tab == "상품정보":
        html(f"""
        <div class="info-card">
        <div class="info-title">상품정보</div>
        {point_item("상품 기본 정보", f"상품명: {etf['name']} / 종목코드: {etf['code']}")}
        {point_item("상품 분류", f"{etf['region']} · {etf['kind']} · 카테고리 {etf['category']}")}
        {point_item("총보수·유의사항", "실제 서비스에서는 총보수, 과세, 추적오차, 원금손실 가능성 등의 공식 데이터가 연결됩니다.")}
        </div>
        """)

    elif tab == "수익률":
        one_w = etf["return_1w"]
        one_m = round(one_w * 1.6, 1)
        one_y = round(one_w * 3.4, 1)

        html(f"""
        <div class="info-card">
        <div class="info-title">수익률</div>
        {point_item("1주 수익률", f"+{one_w:.1f}%")}
        {point_item("1개월 수익률", f"+{one_m:.1f}% (프로토타입 예시값)")}
        {point_item("1년 수익률", f"+{one_y:.1f}% (프로토타입 예시값)")}
        <div class="note-text">실제 서비스에서는 공식 수익률 데이터를 연결해 기간별로 보여줄 수 있습니다.</div>
        </div>
        """)

    elif tab == "기준가":
        gap = etf["price"] - etf["nav"]

        html(f"""
        <div class="info-card">
        <div class="info-title">기준가</div>
        {point_item("현재가", f"{etf['price']:,}원")}
        {point_item("기준가 iNAV", f"{etf['nav']:,}원")}
        {point_item("현재가-기준가 차이", f"{gap:+,}원")}
        {point_item("거래량", f"{etf['volume']:,}주")}
        </div>
        """)

    elif tab == "구성종목(PDF)":
        html("""
        <div class="info-card">
        <div class="info-title">구성종목(PDF)</div>
        <div class="point-desc">상위 종목과 비중을 예시로 보여주는 화면입니다.</div>
        </div>
        """)

        holdings = get_sample_holdings(etf)
        st.dataframe(holdings, use_container_width=True, hide_index=True)

    elif tab == "관련콘텐츠":
        html(f"""
        <div class="info-card">
        <div class="info-title">관련콘텐츠</div>
        {point_item("ETF 기초 설명", f"{etf['name']}를 처음 보는 사용자를 위한 기초 설명 콘텐츠")}
        {point_item("구성종목 쉽게 보기", "이 ETF 안에 어떤 기업이 담겨 있는지 카드형 콘텐츠로 설명")}
        {point_item("비용·유의사항 가이드", "총보수, 추적오차, 원금손실 가능성을 쉽게 설명하는 콘텐츠")}
        </div>
        """)

# =========================
# 9. 페이지: 홈
# =========================
def render_home():
    phone_header()

    html("""
    <div class="top-row">
    <div class="logo">🔵 삼성 <span>Kodex ETF</span></div>
    <div style="font-size:28px;font-weight:900;">☰</div>
    </div>

    <div class="hero-card">
    <div class="hero-pill">반도체 맛집</div>
    <div class="hero-title">전국민 반도체 투자,<br>반도체는 역시 삼성 KODEX</div>
    <div class="hero-link">반도체 맛집 ETF 확인하기 →</div>
    </div>

    <div class="search-box">🔍 &nbsp; 상품명 혹은 종목코드 검색</div>

    <div class="check-card">
    <div class="badge">NEW</div>
    <div class="check-title">KODEX CHECKPOINT</div>
    <div class="check-desc">
    ETF 보기 전 1분 점검<br>
    내 돈 상태, 투자 목적,<br>
    상품 확인 습관까지 먼저 체크해보세요.
    </div>
    </div>
    """)

    if st.button("KODEX CHECKPOINT 시작하기", type="primary", use_container_width=True):
        start()

    c1, c2 = st.columns(2)

    with c1:
        if st.button("전체상품 보기", use_container_width=True):
            go("products")

    with c2:
        if st.button("투자정보 보기", use_container_width=True):
            go("insight")

    df = load_etf_products()
    top = df.sort_values("return_1w", ascending=False).head(1).iloc[0]

    html(f"""
    <div class="section-title">오늘 많이 본 KODEX</div>
    <div class="product-card">
    <div class="product-name">{top['name']}</div>
    <div class="product-meta">{top['desc']}</div>
    <div class="product-rate">+{top['return_1w']:.1f}%</div>
    </div>
    """)

    if st.button(f"{top['name']} 상품 보기", use_container_width=True):
        select_etf(top["code"])

    phone_footer()
    bottom_nav("home")


# =========================
# 10. 페이지: 체크리스트
# =========================
def render_checklist():
    idx = st.session_state.q_idx
    q = questions[idx]
    progress = int(((idx + 1) / len(questions)) * 100)

    phone_header()

    st.markdown(
        """
        <style>
        /* 체크리스트 페이지 질문 글자 */
        .question-title {
            color: #111827 !important;
        }

        .question-guide {
            color: #111827 !important;
        }

        /* 체크리스트 라디오 선지 글자 */
        div[data-testid="stRadio"] label,
        div[data-testid="stRadio"] label *,
        div[data-testid="stRadio"] p,
        div[data-testid="stRadio"] span {
            color: #111827 !important;
        }

        /* 선택지 카드 배경은 흰색으로 고정 */
        div[data-testid="stRadio"] label {
            background: #FFFFFF !important;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )
    
    page_title_bar("KODEX CHECKPOINT", default_back="home")

    html(f"""
    <div class="progress-big">{idx + 1} <span style="font-size:24px;color:#111827;">/ {len(questions)}</span></div>
    <div class="progress-track"><div class="progress-fill" style="width:{progress}%;"></div></div>

    <div class="step-chip">{q["step"]}</div>
    <div class="question-title">{br(q["title"])}</div>
    <div class="question-guide">가장 가까운 항목을 선택해주세요.</div>
    """)

    labels = [f"{code}. {text}" for code, text, scores, weakness in q["options"]]
    current = st.session_state.answers.get(q["id"])
    index = labels.index(current) if current in labels else None

    selected = st.radio(
        "선택지",
        labels,
        index=index,
        key=f"radio_{idx}",
        label_visibility="collapsed",
    )

    c1, c2 = st.columns(2)

    with c1:
        if st.button("이전", use_container_width=True):
            if idx > 0:
                st.session_state.q_idx -= 1
                st.rerun()
            else:
                go_back("home")

    with c2:
        next_label = "다음 질문" if idx < len(questions) - 1 else "리포트 보기"

        if st.button(next_label, type="primary", use_container_width=True):
            st.session_state.answers[q["id"]] = selected

            if idx < len(questions) - 1:
                st.session_state.q_idx += 1
                st.rerun()
            else:
                go("report")

    phone_footer()
    bottom_nav("checkpoint")


# =========================
# 11. 페이지: 리포트
# =========================
def render_report():
    if len(st.session_state.answers) < len(questions):
        st.warning("체크리스트가 아직 완료되지 않았어요.")

        if st.button("체크리스트로 돌아가기"):
            go("checklist")

        return

    raw, pct, weak = calculate_scores()
    habit = classify_habit(pct, weak)
    invest = get_invest_mbti(pct)
    missed = missed_items(pct, weak)
    summary_lines = behavior_summary(pct, habit, missed)

    trait_html = "".join([
        f'<div class="trait-box"><div class="trait-main">{main}</div><div class="trait-sub">{sub}</div></div>'
        for main, sub in invest["traits"]
    ])

    summary_html = "".join([f"<li>{line}</li>" for line in summary_lines])
    missed_html = "".join([f"<li>{x}</li>" for x in missed])

    similar_html = "".join([
        similar_card(item, pct, weak)
        for item in get_similar_etfs(pct, weak)
    ])

    phone_header()

    page_title_bar("KODEX CHECKPOINT", default_back="home")

    html(f"""
    <div class="result-main">
    <div style="font-weight:900;margin-bottom:10px;">나의 ETF 체크포인트 리포트</div>
    <div class="result-emoji">📋</div>
    <div class="result-type">ETF 확인 습관 진단</div>
    <div class="result-desc">
    내 돈 상태, 투자 목적, 상품 확인 습관을 기준으로<br>
    ETF를 볼 때 먼저 확인하면 좋은 항목을 정리했어요.
    </div>
    </div>

    <div class="info-card">
    <div class="info-title">매수 전 점검 상태</div>
    {status_row("자금 상태 점검", pct["fund"])}
    {status_row("목표·기간 설정", pct["goal_period"])}
    {status_row("상품 구조 확인", pct["structure"])}
    {status_row("비용·리스크 확인", pct["risk"])}
    </div>

    <div class="result-main">
    <div style="font-weight:900;margin-bottom:8px;">투자 MBTI</div>
    <div class="invest-code">{invest["code"]}</div>
    <div class="invest-type">{invest["title"]}</div>
    <div class="result-desc">{invest["desc"]}</div>
    <div class="trait-grid">{trait_html}</div>
    </div>

    <div class="result-main">
    <div style="font-weight:900;margin-bottom:10px;">ETF 확인 습관 유형</div>
    <div class="result-emoji">{habit["emoji"]}</div>
    <div class="result-type">{habit["type"]}</div>
    <div class="badge">{habit["mbti"]}</div>
    <div class="result-desc">{habit["desc"]}</div>
    </div>

    <div class="info-card">
    <div class="info-title">나의 점검 행동 요약</div>
    <ul class="summary-list">{summary_html}</ul>
    </div>

    <div class="info-card">
    <div class="info-title">체크 결과 요약</div>
    {score_bar("자금 상태 점검", pct["fund"])}
    {score_bar("목표·기간 점검", pct["goal_period"])}
    {score_bar("수익률·트렌드 반응", pct["return"])}
    {score_bar("상품 구조 확인 습관", pct["structure"])}
    {score_bar("비용·리스크 확인 습관", pct["risk"])}
    <div class="note-text">이 점수는 투자 실력 평가가 아니라, ETF를 볼 때 어떤 정보를 먼저 보고 어떤 항목을 놓치기 쉬운지 확인하기 위한 점수입니다.</div>
    </div>

    <div class="info-card">
    <div class="info-title">한 번 더 확인하면 좋은 항목</div>
    <ul class="summary-list">{missed_html}</ul>
    </div>

    <div class="info-card">
    <div class="info-title">비슷한 확인 유형이 함께 비교한 ETF</div>
    <div class="insight">비슷한 ETF 확인 습관을 가진 사용자가 추가로 살펴본 상품과 정보입니다.</div>
    {similar_html}
    </div>
    """)

    if st.button("전체상품에서 ETF 확인하기", type="primary", use_container_width=True):
        go("products")

    c1, c2 = st.columns(2)

    with c1:
        if st.button("체크리스트 저장", use_container_width=True):
            st.session_state.saved = True
            st.success("체크리스트가 저장되었습니다.")

    with c2:
        if st.button("운영자 인사이트", use_container_width=True):
            go("insight")

    phone_footer()
    bottom_nav("checkpoint")


# =========================
# 12. 페이지: 전체상품
# =========================
def product_list_card(etf, pct=None, weak=None):
    items = get_product_checkpoints(etf, pct, weak)
    item_text = " · ".join(items[:3])
    tags = tag_html(etf["tags"])

    if etf["change"] >= 0:
        change_text = f"▲ {etf['change']:,} ({etf['change_pct']:.2f}%)"
    else:
        change_text = f"▼ {abs(etf['change']):,} ({abs(etf['change_pct']):.2f}%)"

    return f"""
    <div class="product-list-card">
    <div style="display:flex; justify-content:space-between; align-items:start; gap:10px;">
    <div>
    <div class="product-name">{etf["name"]}</div>
    <div class="product-code">{etf["code"]}</div>
    </div>
    <div class="compare-chip">비교</div>
    </div>

    <div class="tag-wrap">{tags}</div>

    <div class="product-rate">+{etf["return_1w"]:.1f}%</div>
    <div class="price-small">현재가 {etf["price"]:,} 원</div>
    <div class="blue-down">{change_text}</div>

    <div class="insight">
    <b>먼저 확인하면 좋은 항목</b><br>{item_text}
    </div>
    </div>
    """


def render_products():
    raw, pct, weak = safe_scores()
    df = load_etf_products()

    phone_header()

    page_title_bar("전체상품", default_back="home")

    html(f"""
    <div class="search-box">🔍 &nbsp; 상품명 혹은 종목코드 검색</div>
    <div class="caption">최근 갱신 {now_text()} · 프로토타입 샘플 데이터</div>
    """)

    c1, c2 = st.columns([1.5, 1])

    with c1:
        st.session_state.sort_metric = st.selectbox(
            "정렬 기준",
            ["1주 수익률", "현재가", "거래량"],
            index=["1주 수익률", "현재가", "거래량"].index(st.session_state.sort_metric),
            label_visibility="collapsed",
        )

    with c2:
        st.session_state.sort_order = st.radio(
            "정렬 순서",
            ["높은 순", "낮은 순"],
            index=0 if st.session_state.sort_order == "높은 순" else 1,
            horizontal=True,
            label_visibility="collapsed",
        )

    region_options = ["전체", "국내", "해외"]
    region_index = region_options.index(st.session_state.selected_region)

    st.session_state.selected_region = st.radio(
        "지역",
        region_options,
        index=region_index,
        horizontal=True,
        label_visibility="collapsed",
    )

    if pct is not None:
        habit = classify_habit(pct, weak)

        html(f"""
        <div class="check-card">
        <div class="badge">REPORT 기반</div>
        <div class="check-title">{habit["type"]}을 위한<br>상품 확인 순서</div>
        <div class="check-desc">
        각 ETF 카드에 표시된 ‘먼저 확인하면 좋은 항목’을 보고<br>
        상품 상세에서 필요한 정보를 바로 찾아볼 수 있어요.
        </div>
        </div>
        """)
    else:
        html("""
        <div class="check-card">
        <div class="badge">CHECK</div>
        <div class="check-title">ETF 보기 전,<br>확인 습관부터 체크해볼까요?</div>
        <div class="check-desc">체크리스트를 완료하면 상품별 확인 항목이 더 개인화됩니다.</div>
        </div>
        """)

        if st.button("CHECKPOINT 시작하기", type="primary", use_container_width=True):
            start()

    filtered = filter_and_sort_products(df)

    html("""
    <div class="section-title">ETF 한눈에 보기</div>
    <div class="caption">상품명을 클릭하면 상품상세정보 페이지로 이동합니다.</div>
    """)

    for _, row in filtered.iterrows():
        etf = row.to_dict()
        html(product_list_card(etf, pct, weak))

        c1, c2 = st.columns(2)

        with c1:
            if st.button(f"{etf['name']} 상품 확인", key=f"open_{etf['code']}", use_container_width=True):
                select_etf(etf["code"])

        with c2:
            is_compared = etf["code"] in st.session_state.compare_codes
            label = "비교 해제" if is_compared else "비교 담기"

            if st.button(label, key=f"compare_{etf['code']}", use_container_width=True):
                if is_compared:
                    st.session_state.compare_codes.remove(etf["code"])
                else:
                    st.session_state.compare_codes.append(etf["code"])

                st.rerun()

    if st.session_state.compare_codes:
        html('<div class="section-title">비교함</div>')

        rows = []

        for code in st.session_state.compare_codes:
            item = get_etf_by_code(code)
            rows.append({
                "상품명": item["name"],
                "현재가": f'{item["price"]:,}원',
                "1주 수익률": f'+{item["return_1w"]:.1f}%',
                "거래량": f'{item["volume"]:,}주',
            })

        st.dataframe(pd.DataFrame(rows), use_container_width=True, hide_index=True)

    phone_footer()
    bottom_nav("products")


# =========================
# 13. 페이지: 상품 상세
# =========================
def render_product_detail():
    raw, pct, weak = safe_scores()
    etf = get_etf_by_code(st.session_state.selected_etf_code)
    items = get_product_checkpoints(etf, pct, weak)
    item_text = " · ".join(items[:3])
    tags = tag_html(etf["tags"])

    checkpoint_html = "".join([
        point_item(
            f"{idx + 1}. {item}",
            f"{checkpoint_desc(item, etf)}<br><br><b>연결 위치</b> · {checkpoint_to_tab(item)}"
        )
        for idx, item in enumerate(items)
    ])

    phone_header()

    page_title_bar("ETF 상품정보", default_back="products")

    html(f"""
    <div class="purple-hero">
    <div class="badge-soft">{etf["region"]} · {etf["kind"]}</div>
    <div class="purple-title">{etf["name"]}</div>
    <div style="font-size:19px;font-weight:900;margin-bottom:12px;">{etf["code"]}</div>
    <div class="purple-desc">{etf["desc"]}</div>
    <div class="tag-wrap">{tags}</div>
    </div>

    <div class="price-grid">
    <div class="price-box">
    <div class="price-label">현재가(원)</div>
    <div class="price-num">{etf["price"]:,}</div>
    <div class="price-up">▲ {etf["change"]:,} ({etf["change_pct"]:.2f}%)</div>
    </div>

    <div class="price-box">
    <div class="price-label">기준가 iNAV(원)</div>
    <div class="price-num">{etf["nav"]:,}</div>
    <div class="note-text">거래량 {etf["volume"]:,}주</div>
    </div>
    </div>
    """)

    render_detail_tabs()

    html(f"""
    <div class="check-card">
    <div class="badge">KODEX CHECKPOINT</div>
    <div class="check-title">이 상품에서<br>먼저 확인하면 좋은 항목</div>
    <div class="check-desc">
    나의 리포트와 상품 유형을 함께 반영했어요.<br>
    <b>{item_text}</b>
    </div>
    </div>
    """)

    render_detail_tab_content(etf)

    html(f"""
    <div class="info-card">
    <div class="info-title">체크리스트와 상품정보 연결</div>
    {checkpoint_html}
    </div>

    <div class="info-card">
    <div class="info-title">기존 상품정보와 연결되는 방식</div>
    {point_item("현재가·기준가", "상단 현재가와 기준가 iNAV 영역에서 확인")}
    {point_item("수익률 기간", "수익률 탭에서 기간별 수익률 확인")}
    {point_item("구성종목", "구성종목(PDF) 탭에서 상위 종목과 비중 확인")}
    {point_item("총보수·유의사항", "상품정보 탭에서 비용과 유의사항 확인")}
    {point_item("관련콘텐츠", "상품 구조가 어렵다면 관련 콘텐츠에서 추가 설명 확인")}
    </div>
    """)

    c1, c2 = st.columns(2)

    with c1:
        if st.button("전체상품으로", use_container_width=True):
            go("products")

    with c2:
        if st.button("체크리스트 저장", type="primary", use_container_width=True):
            st.session_state.saved = True
            st.success("체크리스트가 저장되었습니다.")

    html("""
    <div class="info-card">
    <div class="info-title">함께 비교해볼 만한 KODEX 상품</div>
    <div class="point-desc">비슷한 확인 유형의 사용자가 추가로 살펴본 상품입니다.</div>
    </div>
    """)

    for item in get_similar_etfs(pct, weak):
        if item["code"] == etf["code"]:
            continue

        html(similar_card(item, pct, weak))

        if st.button(f"{item['name']} 비교해보기", key=f"detail_compare_{item['code']}", use_container_width=True):
            select_etf(item["code"])

    phone_footer()
    bottom_nav("products")


# =========================
# 14. 페이지: 운영자 인사이트
# =========================
def render_insight():
    raw, pct, weak = safe_scores()

    phone_header()

    page_title_bar("운영자 인사이트", default_back="home")

    html("""
    <div class="section-title">기업 활용 데이터 예시</div>
    <div class="caption">
    CHECKPOINT는 20대가 ETF를 보기 전 어떤 정보를 먼저 보고, 어떤 항목에서 이탈하는지 확인할 수 있는 데이터 접점이 될 수 있습니다.
    </div>

    <div class="info-card">
    <div class="info-title">수집 가능한 지표</div>
    <div class="point-desc">
    · 가장 많이 나온 ETF 확인 유형<br>
    · 가장 많이 놓친 정보 항목<br>
    · 전체상품 탭 진입률<br>
    · 상품 상세페이지 클릭률<br>
    · 수익률 탭 이동률<br>
    · 구성종목 탭 이동률<br>
    · 총보수 확인률<br>
    · 비교 담기 클릭률<br>
    · 체크리스트 저장률<br>
    · 관련콘텐츠 클릭률
    </div>
    </div>

    <div class="insight">
    예를 들어 구성종목 확인 단계에서 이탈이 높다면, 구성종목을 쉽게 설명하는 카드뉴스나 숏폼 콘텐츠를 제작할 수 있습니다.
    총보수 확인률이 낮다면, 총보수를 쉽게 설명하는 상품 상세 안내 카드를 강화할 수 있습니다.
    </div>
    """)

    if pct is not None:
        habit = classify_habit(pct, weak)
        invest = get_invest_mbti(pct)
        missed = ", ".join(missed_items(pct, weak))
        similar = ", ".join([item["name"] for item in get_similar_etfs(pct, weak)])

        html(f"""
        <div class="info-card">
        <div class="info-title">현재 사용자 예시</div>
        <div class="point-desc">
        투자 MBTI: {invest["code"]} · {invest["title"]}<br>
        확인 유형: {habit["type"]} · {habit["mbti"]}<br>
        보완 항목: {missed}<br>
        함께 비교한 ETF: {similar}
        </div>
        </div>
        """)

    phone_footer()
    bottom_nav("insight")


# =========================
# 15. 페이지: 이벤트
# =========================
def render_event():
    phone_header()

    page_title_bar("이벤트", default_back="home")

    html("""
    <div class="check-card">
    <div class="badge">EVENT</div>
    <div class="check-title">ETF 보기 전,<br>KODEX CHECKPOINT</div>
    <div class="check-desc">
    체크리스트 완료 후 공유 카드를 저장하면<br>
    ETF 확인 습관을 다시 볼 수 있어요.
    </div>
    </div>
    """)

    if st.button("체크포인트 시작하기", type="primary", use_container_width=True):
        start()

    phone_footer()
    bottom_nav("event")


# =========================
# 16. 라우팅
# =========================
if st.session_state.page == "home":
    render_home()
elif st.session_state.page == "checklist":
    render_checklist()
elif st.session_state.page == "report":
    render_report()
elif st.session_state.page == "products":
    render_products()
elif st.session_state.page == "product_detail":
    render_product_detail()
elif st.session_state.page == "insight":
    render_insight()
elif st.session_state.page == "event":
    render_event()
else:
    render_home()
