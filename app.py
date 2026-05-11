import textwrap
import random
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

/* =========================
   모바일 앱 프레임
========================= */
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

/* =========================
   공통 카드 / 텍스트
========================= */
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

.badge-event {
    display:inline-block;
    background:#233BFF;
    color:#fff;
    border-radius:999px;
    padding:6px 12px;
    font-size:12px;
    font-weight:900;
    margin-bottom:8px;
}

.badge-red {
    display:inline-block;
    background:#FFF1F2;
    color:#E11D48;
    border-radius:999px;
    padding:6px 12px;
    font-size:12px;
    font-weight:900;
    margin-bottom:8px;
}

.badge-green {
    display:inline-block;
    background:#DCFCE7;
    color:#15803D;
    border-radius:999px;
    padding:6px 12px;
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

/* =========================
   체크리스트
========================= */
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

/* =========================
   결과 / MBTI
========================= */
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

/* =========================
   같은 MBTI 추천 ETF
========================= */
.peer-card {
    background:#FFFFFF;
    border:1.5px solid #D9E7FF;
    border-radius:24px;
    padding:17px 16px;
    margin:10px 0;
    box-shadow:0 6px 18px rgba(15,23,42,0.04);
}

.peer-rank {
    display:inline-block;
    background:#1155FF;
    color:#fff;
    border-radius:999px;
    padding:4px 9px;
    font-size:11px;
    font-weight:900;
    margin-bottom:7px;
}

.peer-name {
    font-size:16px;
    font-weight:900;
    color:#111827;
    line-height:1.35;
    margin-bottom:5px;
}

.peer-desc {
    font-size:12px;
    color:#6B7280;
    font-weight:700;
    line-height:1.5;
}

/* =========================
   이벤트 / 응모권 / 뽑기
========================= */
.event-banner {
    background:linear-gradient(135deg, #173BFF 0%, #0B1E68 100%);
    border-radius:26px;
    padding:21px 18px;
    color:white;
    margin:14px 0;
    box-shadow:0 10px 26px rgba(17,85,255,0.22);
    position:relative;
    overflow:hidden;
}

.event-banner::after {
    content:"🎟️";
    position:absolute;
    right:18px;
    bottom:8px;
    font-size:60px;
    opacity:0.18;
}

.event-title {
    font-size:22px;
    line-height:1.35;
    font-weight:900;
    margin:8px 0 8px;
}

.event-desc {
    font-size:13px;
    line-height:1.55;
    font-weight:700;
    color:rgba(255,255,255,0.92);
}

.draw-hero {
    background:#FFFFFF;
    border-radius:30px;
    padding:24px 18px 22px;
    text-align:center;
    border:1px solid #D9E7FF;
    box-shadow:0 10px 28px rgba(15,23,42,0.06);
    margin:12px 0 16px;
    position:relative;
    overflow:hidden;
}

.draw-hero::before {
    content:"🪙";
    position:absolute;
    left:22px;
    top:60px;
    font-size:28px;
    opacity:0.75;
}

.draw-hero::after {
    content:"🪙";
    position:absolute;
    right:26px;
    top:105px;
    font-size:27px;
    opacity:0.75;
}

.draw-event-label {
    display:inline-block;
    background:#2844C7;
    color:#fff;
    border-radius:999px;
    padding:8px 14px;
    font-size:13px;
    font-weight:900;
    margin-bottom:18px;
}

.draw-kodex {
    font-size:43px;
    line-height:1;
    font-weight:900;
    color:#2145FF;
    letter-spacing:-1px;
    margin-bottom:12px;
}

.draw-product-name {
    font-size:26px;
    line-height:1.25;
    font-weight:900;
    color:#2145FF;
    letter-spacing:-1px;
    margin-bottom:9px;
}

.draw-product-code {
    color:#2145FF;
    font-size:16px;
    font-weight:900;
    margin-bottom:20px;
}

.draw-copy {
    color:#111827;
    font-size:17px;
    font-weight:800;
    line-height:1.55;
    margin-bottom:18px;
}

.draw-period {
    color:#2145FF;
    font-size:17px;
    font-weight:900;
    margin-bottom:14px;
}

.winner-ticker {
    background:#EAF2FF;
    border-radius:14px;
    padding:11px 12px;
    font-size:13px;
    color:#1E3A8A;
    font-weight:900;
    display:inline-block;
    margin:4px auto 6px;
}

.draw-machine {
    background:linear-gradient(180deg, #8AB7FF 0%, #2E63FF 100%);
    border-radius:28px 28px 14px 14px;
    padding:18px;
    color:white;
    margin:12px 0 0;
    border:3px solid #63A2FF;
    box-shadow:inset 0 0 0 2px rgba(255,255,255,0.12);
}

.draw-machine-window {
    background:#1E3A8A;
    border-radius:22px;
    padding:24px 14px;
    font-size:18px;
    font-weight:900;
    line-height:1.5;
}

.ticket-grid {
    display:grid;
    grid-template-columns:1fr;
    gap:10px;
    margin:12px 0;
}

.ticket-card {
    background:#FFFFFF;
    border:1.5px solid #D9E7FF;
    border-radius:22px;
    padding:16px 13px;
    text-align:center;
    box-shadow:0 6px 18px rgba(15,23,42,0.04);
}

.ticket-num {
    font-size:36px;
    font-weight:900;
    color:#1155FF;
    line-height:1;
}

.ticket-label {
    font-size:14px;
    color:#111827;
    font-weight:900;
    margin-top:8px;
}

.ticket-sub {
    font-size:12px;
    color:#6B7280;
    font-weight:700;
    line-height:1.45;
    margin-top:5px;
}

.mbti-share-card {
    background:linear-gradient(135deg, #F7F4FF 0%, #FFFFFF 100%);
    border:1.5px solid #D8CCFF;
    border-radius:26px;
    padding:20px 18px;
    margin:14px 0;
    text-align:center;
}

.share-code {
    display:inline-block;
    background:#EDEBFF;
    color:#3C3489;
    padding:12px 20px;
    border-radius:16px;
    font-size:25px;
    font-weight:900;
    letter-spacing:5px;
    margin:8px 0 10px;
}

.share-link-box {
    background:#F8FAFC;
    border:1.5px dashed #9DBBFF;
    border-radius:18px;
    padding:13px;
    font-size:12px;
    color:#1E3A8A;
    line-height:1.55;
    font-weight:800;
    word-break:break-all;
    margin:12px 0;
    text-align:left;
}

.share-complete {
    background:linear-gradient(135deg, #ECFDF5 0%, #FFFFFF 100%);
    border:1.5px solid #BBF7D0;
    border-radius:24px;
    padding:18px;
    margin:12px 0;
}

.share-complete-title {
    color:#15803D;
    font-size:19px;
    font-weight:900;
    margin-bottom:8px;
}

.draw-result {
    background:#fff;
    border:1.5px solid #D9E7FF;
    border-radius:26px;
    padding:22px 18px;
    margin:14px 0;
    text-align:center;
    box-shadow:0 8px 24px rgba(15,23,42,0.06);
}

.draw-result-emoji {
    font-size:42px;
    margin-bottom:8px;
}

.draw-result-title {
    font-size:21px;
    color:#111827;
    font-weight:900;
    margin-bottom:8px;
}

.draw-result-desc {
    font-size:13px;
    color:#6B7280;
    font-weight:700;
    line-height:1.55;
}

.event-product-card {
    background:#fff;
    border:1.5px solid #C8DBFF;
    border-radius:26px;
    padding:19px 18px;
    margin:14px 0;
    box-shadow:0 8px 22px rgba(15,23,42,0.05);
}

.event-product-title {
    font-size:20px;
    color:#2145FF;
    font-weight:900;
    line-height:1.3;
    margin-bottom:7px;
}

.event-rule-card {
    background:#F8FAFC;
    border:1px solid #E5E7EB;
    border-radius:20px;
    padding:15px;
    margin:10px 0;
}

.event-rule-title {
    font-size:14px;
    color:#111827;
    font-weight:900;
    margin-bottom:7px;
}

.event-rule-desc {
    font-size:12px;
    color:#6B7280;
    line-height:1.55;
    font-weight:700;
}

.referral-card {
    background:linear-gradient(135deg, #EFF6FF 0%, #FFFFFF 100%);
    border:1.5px solid #BFDBFE;
    border-radius:24px;
    padding:18px;
    margin:14px 0;
}

.referral-title {
    color:#1D4ED8;
    font-size:18px;
    font-weight:900;
    margin-bottom:7px;
}

.friend-status-grid {
    display:grid;
    grid-template-columns:1fr 1fr;
    gap:9px;
    margin-top:12px;
}

.friend-status-box {
    background:#FFFFFF;
    border:1px solid #D9E7FF;
    border-radius:17px;
    padding:12px;
    text-align:center;
}

.friend-status-num {
    font-size:22px;
    color:#1155FF;
    font-weight:900;
}

.friend-status-label {
    font-size:11px;
    color:#6B7280;
    font-weight:800;
    line-height:1.35;
}

/* =========================
   찜 / 하트
========================= */
.heart-pill {
    display:inline-flex;
    align-items:center;
    gap:5px;
    background:#FFF1F2;
    color:#E11D48;
    border-radius:999px;
    padding:6px 10px;
    font-size:12px;
    font-weight:900;
    white-space:nowrap;
}

.heart-empty {
    display:inline-flex;
    align-items:center;
    gap:5px;
    background:#F8FAFC;
    color:#64748B;
    border-radius:999px;
    padding:6px 10px;
    font-size:12px;
    font-weight:900;
    white-space:nowrap;
}

.like-count {
    font-size:12px;
    color:#6B7280;
    font-weight:800;
    text-align:right;
    margin-top:4px;
}

/* =========================
   전체 참여자 MBTI 비율
========================= */
.stat-card {
    background:#fff;
    border:1px solid #E5E7EB;
    border-radius:22px;
    padding:16px;
    margin:10px 0;
    box-shadow:0 6px 18px rgba(15,23,42,0.04);
}

.stat-head {
    display:flex;
    justify-content:space-between;
    align-items:center;
    gap:10px;
    margin-bottom:8px;
}

.stat-name {
    font-size:14px;
    font-weight:900;
    color:#111827;
}

.stat-pct {
    font-size:14px;
    font-weight:900;
    color:#1155FF;
}

.stat-bg {
    height:9px;
    background:#E5E7EB;
    border-radius:999px;
    overflow:hidden;
}

.stat-fill {
    height:9px;
    background:#1155FF;
    border-radius:999px;
}

.stat-desc {
    font-size:12px;
    color:#6B7280;
    font-weight:700;
    line-height:1.45;
    margin-top:7px;
}

.mini-kpi-grid {
    display:grid;
    grid-template-columns:1fr 1fr;
    gap:10px;
    margin:12px 0;
}

.mini-kpi {
    background:#F8FAFC;
    border:1px solid #E5E7EB;
    border-radius:18px;
    padding:13px;
    text-align:center;
}

.mini-kpi-num {
    font-size:22px;
    color:#1155FF;
    font-weight:900;
}

.mini-kpi-label {
    font-size:12px;
    color:#6B7280;
    font-weight:800;
}

/* =========================
   하단 네비게이션
========================= */
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
EVENT_INFO = {
    "title": "Kodex 신규상장 ETF 뽑기 이벤트",
    "product_name": "KODEX 반도체타겟위클리커버드콜 ETF",
    "product_code": "0190G0",
    "period": "2026.05.11 ~ 2026.06.30",
    "copy_1": "월말배당에 옵션 프리미엄 비과세까지 추구",
    "copy_2": "반도체는 역시 삼성 Kodex ETF",
    "official_url": "https://www.samsungfund.com/etf/lounge/draw-game-view.do?seq=68511719",
    "share_limit": 5,
    "daily_ticket_limit": 5,
}

DRAW_PRIZES_NORMAL = [
    {"title": "아쉽지만 꽝이에요", "desc": "일반 응모권은 꽝이 포함될 수 있어요. 내일 다시 참여해보세요.", "emoji": "😢", "is_win": False},
    {"title": "커피 쿠폰 응모 완료", "desc": "베가MGC커피 쿠폰 경품 응모가 완료되었어요.", "emoji": "☕", "is_win": True},
    {"title": "편의점 상품권 응모 완료", "desc": "편의점 모바일 상품권 경품 응모가 완료되었어요.", "emoji": "🎁", "is_win": True},
    {"title": "KODEX 굿즈 응모 완료", "desc": "KODEX 브랜드 굿즈 경품 응모가 완료되었어요.", "emoji": "📘", "is_win": True},
]


ETF_PRODUCTS = [
    {
        "name": "KODEX 반도체타겟위클리커버드콜 ETF",
        "code": "0190G0",
        "category": "covered_call",
        "region": "국내",
        "kind": "월배당·커버드콜",
        "price": 10075,
        "nav": 10062,
        "volume": 812340,
        "return_1w": 1.9,
        "change": 55,
        "change_pct": 0.55,
        "tags": ["신규상장", "반도체", "커버드콜", "월말배당"],
        "desc": "반도체 테마에 커버드콜 전략을 결합해 월말배당과 옵션 프리미엄을 추구하는 신규상장 ETF입니다.",
        "default_likes": 3521,
        "event_target": True,
    },
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
        "default_likes": 1284,
        "event_target": False,
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
        "default_likes": 1732,
        "event_target": False,
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
        "default_likes": 812,
        "event_target": False,
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
        "default_likes": 604,
        "event_target": False,
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
        "default_likes": 945,
        "event_target": False,
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
        "default_likes": 721,
        "event_target": False,
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
        "default_likes": 2310,
        "event_target": False,
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
        "default_likes": 2487,
        "event_target": False,
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
        "default_likes": 1588,
        "event_target": False,
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
        "default_likes": 1944,
        "event_target": False,
    },
]


# =========================
# 3-1. 투자 MBTI 16유형 카탈로그
# =========================
INVEST_MBTI_CATALOG = {
    "SDLP": {
        "name": "안정 설계형 장기 투자자",
        "short": "안정·분산·장기·계획",
        "desc": "자금 상태와 투자 기간을 먼저 정리하고, ETF 구조를 차분히 확인하는 유형입니다.",
    },
    "SDLI": {
        "name": "안정 분산형 직관 투자자",
        "short": "안정·분산·장기·직관",
        "desc": "큰 방향은 안정적으로 보지만, 최종 판단은 직관에 의존하는 편입니다.",
    },
    "SDQP": {
        "name": "안정 점검형 단기 투자자",
        "short": "안정·분산·단기·계획",
        "desc": "단기 흐름을 보더라도 자금 상태와 리스크를 함께 점검하려는 유형입니다.",
    },
    "SDQI": {
        "name": "안정 관찰형 ETF 탐색자",
        "short": "안정·분산·단기·직관",
        "desc": "안정성을 중시하지만, 단기 시장 분위기에도 영향을 받는 유형입니다.",
    },
    "SCLP": {
        "name": "안정 집중형 장기 투자자",
        "short": "안정·집중·장기·계획",
        "desc": "관심 있는 상품을 오래 보되, 계획과 기준을 세우고 접근하는 유형입니다.",
    },
    "SCLI": {
        "name": "안정 집중형 직관 투자자",
        "short": "안정·집중·장기·직관",
        "desc": "안정적인 방향을 선호하지만 익숙한 상품명이나 테마에 반응하기도 합니다.",
    },
    "SCQP": {
        "name": "신중한 단기 점검자",
        "short": "안정·집중·단기·계획",
        "desc": "단기 확인을 하더라도 비용과 유의사항을 챙기려는 유형입니다.",
    },
    "SCQI": {
        "name": "신중한 직관형 탐색자",
        "short": "안정·집중·단기·직관",
        "desc": "상품을 빠르게 탐색하지만, 기본적인 리스크는 의식하는 유형입니다.",
    },
    "GDLP": {
        "name": "성장 분산형 장기 투자자",
        "short": "성장·분산·장기·계획",
        "desc": "성장 가능성을 보되, 장기 관점에서 분산 구조를 함께 확인하는 유형입니다.",
    },
    "GDLI": {
        "name": "성장 분산형 직관 투자자",
        "short": "성장·분산·장기·직관",
        "desc": "성장 테마에 관심이 크지만, 여러 상품을 함께 살펴보려는 유형입니다.",
    },
    "GDQP": {
        "name": "성장 점검형 단기 투자자",
        "short": "성장·분산·단기·계획",
        "desc": "단기 수익 기회를 보면서도, 비교 기준을 세워 확인하려는 유형입니다.",
    },
    "GDQI": {
        "name": "트렌드 분산형 ETF 탐색자",
        "short": "성장·분산·단기·직관",
        "desc": "시장 트렌드에 빠르게 반응하면서도 여러 ETF를 비교하려는 유형입니다.",
    },
    "GCLP": {
        "name": "성장 집중형 장기 투자자",
        "short": "성장·집중·장기·계획",
        "desc": "관심 테마에 집중하되 장기적인 투자 이유를 정리하려는 유형입니다.",
    },
    "GCLI": {
        "name": "트렌드 반응형 ETF 탐색자",
        "short": "성장·집중·장기·직관",
        "desc": "성장 테마, 수익률, 익숙한 상품명에 빠르게 반응하는 편입니다.",
    },
    "GCQP": {
        "name": "수익률 추적형 단기 투자자",
        "short": "성장·집중·단기·계획",
        "desc": "단기 수익률을 빠르게 확인하지만, 비교 기준도 함께 세우려는 유형입니다.",
    },
    "GCQI": {
        "name": "핫테마 직진형 ETF 탐색자",
        "short": "성장·집중·단기·직관",
        "desc": "최근 오른 테마와 익숙한 상품명에 가장 빠르게 반응하는 유형입니다.",
    },
}


# =========================
# 3-2. 같은 투자 MBTI 유형이 많이 확인한 ETF 예시
# 실제 서비스에서는 MBTI 유형별 상품 상세 진입/찜/매수 데이터를 기반으로 집계
# =========================
PEER_ETF_BY_MBTI = {
    "SCLP": ["0190G0", "211900", "379800"],
    "SDLP": ["379800", "211900", "337160"],
    "SDLI": ["379800", "337160", "211900"],
    "SDQP": ["379800", "337160", "363580"],
    "SDQI": ["379800", "363580", "337160"],
    "SCLI": ["0190G0", "211900", "379800"],
    "SCQP": ["363580", "211900", "0190G0"],
    "SCQI": ["0190G0", "363580", "379800"],
    "GDLP": ["379810", "487230", "0190G0"],
    "GDLI": ["379810", "487230", "494310"],
    "GDQP": ["487230", "379810", "494310"],
    "GDQI": ["487230", "494310", "0190G0"],
    "GCLP": ["0190G0", "487230", "379810"],
    "GCLI": ["0190G0", "487230", "494310"],
    "GCQP": ["494310", "122630", "0190G0"],
    "GCQI": ["494310", "122630", "487230"],
}


# =========================
# 3-3. 전체 참여자 투자 MBTI 비율 예시
# 실제 서비스에서는 사용자 응답 로그 기반으로 집계
# =========================
PARTICIPANT_MBTI_STATS = [
    {"code": "GCLI", "name": "트렌드 반응형 ETF 탐색자", "pct": 17, "count": 214},
    {"code": "GCQI", "name": "핫테마 직진형 ETF 탐색자", "pct": 13, "count": 164},
    {"code": "SDLP", "name": "안정 설계형 장기 투자자", "pct": 12, "count": 151},
    {"code": "GDLP", "name": "성장 분산형 장기 투자자", "pct": 10, "count": 126},
    {"code": "SCLP", "name": "안정 집중형 장기 투자자", "pct": 8, "count": 101},
    {"code": "GDQI", "name": "트렌드 분산형 ETF 탐색자", "pct": 7, "count": 88},
    {"code": "SCQP", "name": "신중한 단기 점검자", "pct": 6, "count": 76},
    {"code": "GCQP", "name": "수익률 추적형 단기 투자자", "pct": 6, "count": 76},
    {"code": "SCLI", "name": "안정 집중형 직관 투자자", "pct": 5, "count": 63},
    {"code": "GDQP", "name": "성장 점검형 단기 투자자", "pct": 4, "count": 50},
    {"code": "SDQP", "name": "안정 점검형 단기 투자자", "pct": 3, "count": 38},
    {"code": "SDLI", "name": "안정 분산형 직관 투자자", "pct": 3, "count": 38},
    {"code": "GCLP", "name": "성장 집중형 장기 투자자", "pct": 2, "count": 25},
    {"code": "SCQI", "name": "신중한 직관형 탐색자", "pct": 2, "count": 25},
    {"code": "SDQI", "name": "안정 관찰형 ETF 탐색자", "pct": 1, "count": 13},
    {"code": "GDLI", "name": "성장 분산형 직관 투자자", "pct": 1, "count": 13},
]


# =========================
# 3-4. 이벤트 성과 예시 데이터
# 실제 서비스에서는 이벤트 로그 / 공유 링크 / 인증 데이터를 기반으로 집계
# =========================
EVENT_MBTI_STATS = [
    {"code": "GCLI", "share_rate": 24, "friend_check_rate": 31, "event_view_rate": 41, "buy_confirm_rate": 7},
    {"code": "GCQI", "share_rate": 21, "friend_check_rate": 28, "event_view_rate": 38, "buy_confirm_rate": 6},
    {"code": "SDLP", "share_rate": 12, "friend_check_rate": 18, "event_view_rate": 29, "buy_confirm_rate": 5},
    {"code": "GDLP", "share_rate": 16, "friend_check_rate": 22, "event_view_rate": 33, "buy_confirm_rate": 6},
    {"code": "SCLP", "share_rate": 11, "friend_check_rate": 17, "event_view_rate": 27, "buy_confirm_rate": 4},
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
    "selected_etf_code": "0190G0",
    "sort_metric": "1주 수익률",
    "sort_order": "높은 순",
    "selected_region": "전체",
    "compare_codes": [],
    "favorite_codes": [],
    "saved": False,
    "product_tab": "투자포인트",
    "history": [],

    # 이벤트 / 응모권 상태
    "shared_mbti": False,
    "share_count": 0,
    "normal_tickets": 0,
    "used_normal_tickets": 0,
    "last_draw_result": None,
    "draw_history": [],
    "share_link_copied": False,
    "daily_tickets_issued": 0,
    "friend_checklist_reward_count": 0,
    "friend_buy_reward_count": 0,

    # 친구 유입 상태 예시
    "mock_friend_link_visits": 4,
    "mock_friend_checklist_completed": 2,
    "mock_friend_event_product_views": 1,
    "mock_friend_buy_confirmed": 1,

    # 운영자 인사이트용 프로토타입 지표
    "mock_total_participants": 1260,
    "mock_save_clicks": 301,
    "mock_favorite_clicks": 512,
    "mock_product_clicks": 684,
    "mock_event_page_visits": 418,
    "mock_share_link_created": 176,
    "mock_share_clicks": 176,
    "mock_general_tickets_issued": 176,
    "mock_draw_plays": 121,
    "mock_referral_visits": 94,
    "mock_referral_checklist_complete": 51,
    "mock_referral_buy_confirm": 18,
    "mock_event_product_clicks": 147,
    "mock_daily_limit_users": 12,
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


def open_event_page():
    st.session_state.mock_event_page_visits += 1
    go("event_draw")


def select_etf(code: str):
    st.session_state.selected_etf_code = code
    st.session_state.product_tab = "투자포인트"
    st.session_state.mock_product_clicks += 1

    etf = get_etf_by_code(code)

    if etf.get("event_target"):
        st.session_state.mock_event_product_clicks += 1

    go("product_detail")


def get_etf_by_code(code: str):
    for item in ETF_PRODUCTS:
        if item["code"] == code:
            return item
    return ETF_PRODUCTS[0]


def get_event_etf():
    for item in ETF_PRODUCTS:
        if item.get("event_target"):
            return item
    return ETF_PRODUCTS[0]


def can_issue_daily_ticket():
    return st.session_state.daily_tickets_issued < EVENT_INFO["daily_ticket_limit"]


def issue_normal_ticket(reason: str):
    """
    모든 보상은 일반 응모권으로 통일.
    하루 최대 지급 한도 안에서만 응모권 지급.
    """
    if not can_issue_daily_ticket():
        return False, f"오늘 받을 수 있는 응모권 한도({EVENT_INFO['daily_ticket_limit']}장)에 도달했어요."

    st.session_state.normal_tickets += 1
    st.session_state.daily_tickets_issued += 1
    st.session_state.mock_general_tickets_issued += 1

    return True, f"{reason} 일반 응모권 1장이 지급되었습니다."


def make_share_link(invest_code: str):
    """
    실제 서비스에서는 사용자 ID, 추천인 ID, 캠페인 ID, 만료시간 등을 포함한 추적 링크로 생성.
    프로토타입에서는 투자 MBTI 코드와 날짜를 넣어 공유 링크처럼 보여줌.
    """
    today = datetime.now().strftime("%Y%m%d")
    return f"https://kodex-checkpoint.streamlit.app/?ref={invest_code}-{today}"


def issue_share_ticket():
    """
    프로토타입용 공유 완료 처리.
    실제 서비스에서는 링크 복사, 카카오톡 공유, 인스타 공유, 공유 콜백 등과 연결 가능.
    """
    if len(st.session_state.answers) < len(questions):
        return False, "투자 MBTI 결과가 아직 없어요. 먼저 CHECKPOINT를 완료해주세요."

    if st.session_state.share_count >= EVENT_INFO["share_limit"]:
        return False, f"이벤트 기간 내 결과 공유 응모권은 최대 {EVENT_INFO['share_limit']}장까지 받을 수 있어요."

    ok, msg = issue_normal_ticket("투자 MBTI 결과 공유가 완료되어")

    if not ok:
        return False, msg

    st.session_state.shared_mbti = True
    st.session_state.share_count += 1
    st.session_state.mock_share_clicks += 1
    st.session_state.mock_share_link_created += 1

    return True, msg


def copy_share_link():
    """
    Streamlit 프로토타입에서는 실제 클립보드 복사 대신 복사 완료 상태만 표시.
    실제 서비스에서는 navigator.clipboard 또는 모바일 공유 API와 연결.
    """
    if len(st.session_state.answers) < len(questions):
        return False, "투자 MBTI 결과가 있어야 공유 링크를 만들 수 있어요."

    st.session_state.share_link_copied = True
    st.session_state.mock_share_link_created += 1
    return True, "공유 링크가 생성되었습니다. 이 링크를 친구에게 공유할 수 있어요."


def auto_issue_friend_rewards():
    """
    친구가 공유 링크를 통해 들어와 체크리스트를 완료하거나,
    신규상장 ETF 매수 확인까지 이어졌을 때 일반 응모권을 자동 지급하는 구조.

    실제 서비스에서는:
    - 공유 링크 ref 추적
    - 친구 계정/휴대폰 중복 방지
    - 체크리스트 완료 로그
    - 신규상장 ETF 매수 확인 또는 이벤트 인증 API
    를 기반으로 자동 지급.
    """
    if not st.session_state.shared_mbti:
        return []

    messages = []

    # 친구 체크리스트 완료 보상
    completed_count = int(st.session_state.mock_friend_checklist_completed)
    already_rewarded_check = int(st.session_state.friend_checklist_reward_count)
    pending_check_rewards = max(0, completed_count - already_rewarded_check)

    for _ in range(pending_check_rewards):
        ok, msg = issue_normal_ticket("공유받은 친구가 체크리스트를 완료하여")

        if ok:
            st.session_state.friend_checklist_reward_count += 1
            st.session_state.mock_referral_checklist_complete += 1
            messages.append(msg)
        else:
            messages.append(msg)
            break

    # 친구 매수 확인 보상
    buy_count = int(st.session_state.mock_friend_buy_confirmed)
    already_rewarded_buy = int(st.session_state.friend_buy_reward_count)
    pending_buy_rewards = max(0, buy_count - already_rewarded_buy)

    for _ in range(pending_buy_rewards):
        ok, msg = issue_normal_ticket("공유받은 친구의 신규상장 ETF 매수 확인이 완료되어")

        if ok:
            st.session_state.friend_buy_reward_count += 1
            st.session_state.mock_referral_buy_confirm += 1
            messages.append(msg)
        else:
            messages.append(msg)
            break

    return messages


def draw_with_ticket():
    """
    일반 응모권으로만 뽑기 참여.
    꽝 없는 응모권/프리미엄 응모권은 제거.
    """
    if st.session_state.normal_tickets <= 0:
        return False, None

    st.session_state.normal_tickets -= 1
    st.session_state.used_normal_tickets += 1

    result = random.choice(DRAW_PRIZES_NORMAL)

    st.session_state.mock_draw_plays += 1
    st.session_state.last_draw_result = result
    st.session_state.draw_history.append({
        "type": "normal",
        "title": result["title"],
        "time": now_text(),
    })

    return True, result


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
        ("상품", "products"),
        ("체크", "checkpoint"),
        ("이벤트", "event_draw"),
        ("인사이트", "insight"),
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
                elif page == "event_draw":
                    open_event_page()
                else:
                    go(page)


def tag_html(tags):
    return "".join([f'<span class="tag">{tag}</span>' for tag in tags])


def event_target_badge_html(etf):
    if etf.get("event_target"):
        return '<span class="badge-red">신규상장 이벤트 대상</span>'
    return ""


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


def get_default_like_count(code: str):
    etf = get_etf_by_code(code)
    return int(etf.get("default_likes", 0))


def is_favorite(code: str):
    return code in st.session_state.favorite_codes


def toggle_favorite(code: str):
    if code in st.session_state.favorite_codes:
        st.session_state.favorite_codes.remove(code)
    else:
        st.session_state.favorite_codes.append(code)
        st.session_state.mock_favorite_clicks += 1


def favorite_badge_html(code: str):
    liked = is_favorite(code)
    total_likes = get_default_like_count(code) + (1 if liked else 0)

    if liked:
        return f"""
        <div class="heart-pill">♥ 찜한 ETF</div>
        <div class="like-count">관심 {total_likes:,}</div>
        """

    return f"""
    <div class="heart-empty">♡ 관심 ETF</div>
    <div class="like-count">관심 {total_likes:,}</div>
    """


def stat_bar_html(code, name, pct, desc=None):
    desc_html = f'<div class="stat-desc">{desc}</div>' if desc else ""
    return f"""
    <div class="stat-card">
    <div class="stat-head">
    <div class="stat-name">{code} · {name}</div>
    <div class="stat-pct">{pct}%</div>
    </div>
    <div class="stat-bg"><div class="stat-fill" style="width:{pct}%;"></div></div>
    {desc_html}
    </div>
    """


def event_metric_bar_html(label, value, desc=None):
    desc_html = f'<div class="stat-desc">{desc}</div>' if desc else ""
    return f"""
    <div class="stat-card">
    <div class="stat-head">
    <div class="stat-name">{label}</div>
    <div class="stat-pct">{value}%</div>
    </div>
    <div class="stat-bg"><div class="stat-fill" style="width:{value}%;"></div></div>
    {desc_html}
    </div>
    """


def ticket_summary_html():
    return f"""
    <div class="ticket-grid">
    <div class="ticket-card">
    <div class="ticket-num">{st.session_state.normal_tickets}</div>
    <div class="ticket-label">일반 응모권</div>
    <div class="ticket-sub">
    결과 공유, 친구 체크리스트 완료, 친구 매수 확인 시 지급<br>
    하루 최대 {EVENT_INFO["daily_ticket_limit"]}장
    </div>
    </div>
    </div>
    """


def friend_status_html():
    return f"""
    <div class="friend-status-grid">
    <div class="friend-status-box">
    <div class="friend-status-num">{st.session_state.mock_friend_link_visits}</div>
    <div class="friend-status-label">공유 링크<br>접속</div>
    </div>
    <div class="friend-status-box">
    <div class="friend-status-num">{st.session_state.mock_friend_checklist_completed}</div>
    <div class="friend-status-label">친구 체크리스트<br>완료</div>
    </div>
    <div class="friend-status-box">
    <div class="friend-status-num">{st.session_state.mock_friend_event_product_views}</div>
    <div class="friend-status-label">신규상장 ETF<br>정보 확인</div>
    </div>
    <div class="friend-status-box">
    <div class="friend-status-num">{st.session_state.mock_friend_buy_confirmed}</div>
    <div class="friend-status-label">매수 확인<br>완료</div>
    </div>
    </div>
    """


def peer_etf_card_html(rank, etf, invest_code):
    return f"""
    <div class="peer-card">
    <div class="peer-rank">{rank}위 · {invest_code} 유형</div>
    <div class="peer-name">{etf["name"]}</div>
    <div class="peer-desc">
    비슷한 투자 MBTI 유형의 사용자가 많이 확인한 ETF입니다.<br>
    {etf["desc"]}
    </div>
    </div>
    """


def get_peer_etf_codes(invest_code: str):
    return PEER_ETF_BY_MBTI.get(invest_code, ["0190G0", "379800", "211900"])


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
    catalog = INVEST_MBTI_CATALOG.get(code, {})

    title = catalog.get("name", "ETF 기준 점검형 탐색자")
    desc = catalog.get("desc", "ETF를 볼 때 상품의 구조와 확인 기준을 함께 살펴보려는 편이에요.")

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
        "covered_call": ["커버드콜 전략", "분배금", "상위 구성종목", "유의사항"],
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
        "분배금": "상품정보 / 관련콘텐츠",
        "분배 기준": "상품정보 / 관련콘텐츠",
        "테마 집중도": "투자포인트 / 구성종목(PDF)",
        "변동성": "수익률 / 기준가",
        "일간 추종 구조": "상품정보 / 유의사항",
        "커버드콜 전략": "상품정보 / 관련콘텐츠",
        "옵션 프리미엄": "상품정보 / 관련콘텐츠",
        "월말배당": "상품정보 / 관련콘텐츠",
        "투자포인트": "투자포인트",
        "상품정보": "상품정보",
    }

    return mapping.get(item, "상품정보")


def checkpoint_desc(item, etf):
    desc = {
        "기초지수": f"{etf['name']}가 어떤 지수나 전략을 따라가는지 확인합니다.",
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
        "커버드콜 전략": "커버드콜 구조가 수익과 손실 가능성에 어떤 영향을 주는지 확인합니다.",
        "옵션 프리미엄": "옵션 프리미엄이 분배 재원과 수익 구조에 어떤 역할을 하는지 확인합니다.",
        "월말배당": "월말배당의 지급 기준과 지속 가능성을 확인합니다.",
        "투자포인트": "상품의 핵심 특징과 투자 포인트를 먼저 확인합니다.",
        "상품정보": "상품 구조, 총보수, 유의사항을 확인합니다.",
    }

    return desc.get(item, "상품정보를 기준 있게 확인합니다.")


def checkpoint_reason(item, etf, pct=None):
    official_reason = {
        "기초지수": "ETF는 특정 지수나 전략을 따라가므로, 기초지수를 알아야 이 상품이 무엇에 투자하는지 이해할 수 있습니다.",
        "해외지수": "해외지수형 ETF는 해외 시장 흐름과 환율 영향을 함께 받을 수 있어 기준 지수를 확인해야 합니다.",
        "구성종목": "ETF 이름만으로는 실제 편입 종목과 비중을 알기 어렵기 때문에 구성종목 확인이 필요합니다.",
        "상위 구성종목": "상위 종목 비중이 높으면 특정 기업이나 산업의 영향을 크게 받을 수 있습니다.",
        "수익률 기간": "최근 수익률은 기간에 따라 다르게 보일 수 있어 1주·1개월·1년 기준을 구분해야 합니다.",
        "단기 수익률 기간": "단기 수익률만 보면 일시적 상승인지 장기 흐름인지 판단하기 어렵습니다.",
        "총보수": "ETF는 보유 기간 동안 비용이 반영되므로 장기 보유 시 총보수 확인이 중요합니다.",
        "총보수·유의사항": "비용과 투자위험은 수익률 화면에서 잘 보이지 않지만 실제 투자 판단에 영향을 줍니다.",
        "유의사항": "ETF도 원금 손실 가능성이 있으므로 상품 구조와 투자위험을 확인해야 합니다.",
        "현재가·기준가": "현재가와 기준가 차이를 보면 시장 가격이 순자산가치와 얼마나 차이 나는지 감을 잡을 수 있습니다.",
        "기준가": "기준가는 ETF의 순자산가치 흐름을 보여주는 지표입니다.",
        "거래량": "거래량이 적으면 매수·매도 시 원하는 가격에 거래하기 어려울 수 있습니다.",
        "환율 영향": "해외형 ETF는 기초자산 수익률 외에도 환율 변화가 성과에 영향을 줄 수 있습니다.",
        "분배금": "분배금이 있는 ETF는 지급 기준과 지속 가능성을 함께 확인해야 합니다.",
        "분배 기준": "분배금은 상품마다 지급 기준과 주기가 다르므로 확인이 필요합니다.",
        "테마 집중도": "테마형 ETF는 특정 산업이나 이슈에 집중되어 변동성이 커질 수 있습니다.",
        "변동성": "변동성이 큰 상품은 단기 수익률만 보고 판단하면 위험을 과소평가할 수 있습니다.",
        "일간 추종 구조": "레버리지 ETF는 장기 누적 수익률이 단순 배수로 움직이지 않을 수 있어 구조 확인이 필요합니다.",
        "커버드콜 전략": "커버드콜 ETF는 상승장에서 수익이 제한될 수 있고, 시장 하락 위험은 남을 수 있어 구조 확인이 필요합니다.",
        "옵션 프리미엄": "옵션 프리미엄은 분배 재원으로 활용될 수 있지만, 상품의 전체 수익 구조와 함께 이해해야 합니다.",
        "월말배당": "월말배당은 매력적으로 보일 수 있지만, 분배금 지급 기준과 지속 가능성을 함께 확인해야 합니다.",
        "투자포인트": "투자포인트는 상품의 핵심 특징을 빠르게 파악하는 출발점입니다.",
        "상품정보": "상품정보는 총보수, 과세, 유의사항 등 기본 확인 항목이 모이는 영역입니다.",
    }

    user_reason = ""

    if pct is not None:
        if item in ["총보수", "총보수·유의사항", "유의사항"] and pct["risk"] < 50:
            user_reason = " 특히 이번 체크리스트에서 비용·리스크 확인 점수가 낮게 나타나 이 항목을 우선 제시했습니다."
        elif item in ["기초지수", "구성종목", "상위 구성종목"] and pct["structure"] < 50:
            user_reason = " 특히 이번 체크리스트에서 상품 구조 확인 습관이 낮게 나타나 이 항목을 우선 제시했습니다."
        elif item in ["수익률 기간", "단기 수익률 기간", "변동성"] and pct["return"] >= 60:
            user_reason = " 최근 수익률에 빠르게 반응하는 편으로 나타나, 수익률의 기준 기간과 변동성을 함께 확인하도록 제시했습니다."
        elif item in ["기초지수", "투자포인트"] and pct["name"] >= 50:
            user_reason = " 익숙한 상품명에 반응하는 편으로 나타나, 이름보다 실제 추종 지수와 상품 구조를 먼저 확인하도록 제시했습니다."

    product_reason = ""

    if etf["category"] == "leveraged":
        product_reason = " 또한 이 상품은 레버리지 성격이 있어 일반 지수형 ETF보다 구조와 유의사항 확인이 더 중요합니다."
    elif etf["category"] == "theme":
        product_reason = " 또한 이 상품은 테마형 ETF라 특정 산업·이슈에 집중될 수 있어 구성종목과 변동성을 함께 봐야 합니다."
    elif etf["category"] == "global_index":
        product_reason = " 또한 해외지수형 ETF는 해외 시장과 환율 영향을 함께 받을 수 있습니다."
    elif etf["category"] == "dividend":
        product_reason = " 또한 배당형 ETF는 분배금뿐 아니라 구성종목과 분배 기준을 함께 확인해야 합니다."
    elif etf["category"] == "covered_call":
        product_reason = " 또한 이 상품은 신규상장 커버드콜 ETF이므로 반도체 테마, 분배 구조, 옵션 전략, 유의사항을 함께 확인해야 합니다."

    return official_reason.get(item, "ETF 확인을 위해 필요한 기본 항목입니다.") + user_reason + product_reason


# =========================
# 8. 데이터 로딩 / 상품 상세 탭 함수
# =========================
@st.cache_data(ttl=60)
def load_etf_products():
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

    if "반도체타겟" in name:
        return pd.DataFrame([
            {"종목명": "삼성전자", "비중(%)": 25.4},
            {"종목명": "SK하이닉스", "비중(%)": 22.8},
            {"종목명": "한미반도체", "비중(%)": 8.9},
            {"종목명": "리노공업", "비중(%)": 5.6},
            {"종목명": "DB하이텍", "비중(%)": 4.7},
        ])

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
        {point_item("이런 경우 더 확인", "최근 수익률이나 이벤트 문구만 보고 판단하기보다, 구성종목·분배금·비용·유의사항을 함께 보면 더 기준 있게 볼 수 있어요.")}
        <div class="note-text">프로토타입 예시 화면입니다.</div>
        </div>
        """)

    elif tab == "상품정보":
        extra = ""

        if etf.get("event_target"):
            extra = point_item(
                "신규상장 이벤트 연결",
                "이 상품은 KODEX 신규상장 ETF 뽑기 이벤트 대상 상품으로 설정한 프로토타입 예시입니다. 실제 서비스에서는 공식 이벤트 조건과 상품정보가 연결됩니다."
            )

        html(f"""
        <div class="info-card">
        <div class="info-title">상품정보</div>
        {point_item("상품 기본 정보", f"상품명: {etf['name']} / 종목코드: {etf['code']}")}
        {point_item("상품 분류", f"{etf['region']} · {etf['kind']} · 카테고리 {etf['category']}")}
        {point_item("총보수·유의사항", "실제 서비스에서는 총보수, 과세, 추적오차, 원금손실 가능성 등의 공식 데이터가 연결됩니다.")}
        {extra}
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
        {point_item("이벤트 참여 가이드", "투자 MBTI 결과를 이벤트 페이지에서 공유하면 일반 응모권을 받을 수 있다는 흐름을 안내")}
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
    <div class="hero-pill">CHECKPOINT</div>
    <div class="hero-title">ETF 보기 전,<br>내가 놓치기 쉬운 항목부터 체크</div>
    <div class="hero-link">투자 MBTI 확인하고 ETF 체크하기 →</div>
    </div>

    <div class="event-banner">
    <div class="badge-soft">EVENT</div>
    <div class="event-title">투자 MBTI 공유하고<br>응모권 받는 새로운 참여 방법</div>
    <div class="event-desc">
    KODEX 신규상장 ETF 뽑기 이벤트에<br>
    내 투자 MBTI 결과 공유 기능을 연결했어요.<br><br>
    결과 공유, 친구 체크리스트 완료, 친구 매수 확인 시<br>
    일반 응모권을 받을 수 있어요.
    </div>
    </div>
    """)

    c1, c2 = st.columns(2)

    with c1:
        if st.button("투자 MBTI 확인하기", type="primary", use_container_width=True):
            start()

    with c2:
        if st.button("이벤트 보러가기", use_container_width=True):
            open_event_page()

    html("""
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

    c1, c2 = st.columns(2)

    with c1:
        if st.button("전체상품 보기", use_container_width=True):
            go("products")

    with c2:
        if st.button("운영자 인사이트", use_container_width=True):
            go("insight")

    event_etf = get_event_etf()

    html(f"""
    <div class="section-title">진행 중인 이벤트</div>
    <div class="event-product-card">
    <div class="badge-event">Kodex 신규상장 ETF 뽑기 이벤트</div>
    <div class="event-product-title">{event_etf["name"]}</div>
    <div class="product-code">{event_etf["code"]}</div>
    <div class="product-meta" style="margin-top:8px;">
    {EVENT_INFO["copy_1"]}<br>
    {EVENT_INFO["copy_2"]}<br>
    기간: {EVENT_INFO["period"]}
    </div>
    <div class="insight">
    CHECKPOINT 완료 후 이벤트 페이지에서 투자 MBTI 공유 링크를 만들고,
    결과를 공유하면 일반 응모권을 받을 수 있어요.
    </div>
    </div>
    """)

    c1, c2 = st.columns(2)

    with c1:
        if st.button("이벤트 페이지로 이동", type="primary", use_container_width=True):
            open_event_page()

    with c2:
        if st.button("이벤트 ETF 확인", use_container_width=True):
            select_etf(event_etf["code"])

    df = load_etf_products()
    top = df.sort_values("return_1w", ascending=False).head(1).iloc[0]

    html(f"""
    <div class="section-title">오늘 많이 본 KODEX</div>
    <div class="product-card">
    <div style="display:flex; justify-content:space-between; gap:10px; align-items:flex-start;">
    <div>
    {event_target_badge_html(top)}
    <div class="product-name">{top['name']}</div>
    <div class="product-meta">{top['desc']}</div>
    </div>
    <div>{favorite_badge_html(top['code'])}</div>
    </div>
    <div class="product-rate">+{top['return_1w']:.1f}%</div>
    </div>
    """)

    c1, c2 = st.columns(2)

    with c1:
        if st.button(f"{top['name']} 상품 보기", use_container_width=True):
            select_etf(top["code"])

    with c2:
        fav_label = "♥ 찜 해제" if is_favorite(top["code"]) else "♡ 찜하기"

        if st.button(fav_label, key=f"home_fav_{top['code']}", use_container_width=True):
            toggle_favorite(top["code"])
            st.rerun()

    if st.session_state.favorite_codes:
        html("""
        <div class="info-card">
        <div class="info-title">내가 찜한 KODEX</div>
        <div class="point-desc">관심 있는 ETF를 하트로 모아두고 나중에 다시 확인할 수 있어요.</div>
        </div>
        """)

        for code in st.session_state.favorite_codes[:3]:
            item = get_etf_by_code(code)
            html(f"""
            <div class="product-card">
            <div class="product-name" style="font-size:17px;">♥ {item['name']}</div>
            <div class="product-meta">{item['desc']}</div>
            </div>
            """)

    html("""
    <div class="info-card">
    <div class="info-title">이벤트 참여 방식</div>
    <div class="point-desc">
    1. 투자 MBTI 체크리스트 완료<br>
    2. 이벤트 페이지에서 내 결과 공유 링크 생성<br>
    3. 결과 공유 시 일반 응모권 1장 지급<br>
    4. 친구가 링크로 들어와 체크리스트를 완료하면 일반 응모권 1장 추가 지급<br>
    5. 친구가 본인 판단으로 신규상장 ETF 매수까지 이어지면 일반 응모권 1장 추가 지급<br><br>
    ※ 응모권은 하루 최대 5장까지 받을 수 있도록 제한됩니다.
    </div>
    </div>
    """)

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
        .question-title {
            color: #111827 !important;
        }

        .question-guide {
            color: #111827 !important;
        }

        div[data-testid="stRadio"] label,
        div[data-testid="stRadio"] label *,
        div[data-testid="stRadio"] p,
        div[data-testid="stRadio"] span {
            color: #111827 !important;
        }

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
    <div class="question-guide">
    ETF 보기 전 나의 투자 성향을 확인해보세요.<br>
    체크리스트 완료 후 이벤트 페이지에서 결과를 공유하면<br>
    KODEX 뽑기 응모권을 받을 수 있어요.
    </div>
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

    peer_codes = get_peer_etf_codes(invest["code"])
    peer_cards_html = ""

    for idx, code in enumerate(peer_codes[:3], start=1):
        peer_etf = get_etf_by_code(code)
        peer_cards_html += peer_etf_card_html(idx, peer_etf, invest["code"])

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

    <div class="info-card">
    <div class="info-title">같은 {invest["code"]} 유형이 많이 확인한 ETF</div>
    <div class="point-desc">
    같은 투자 MBTI 유형의 사용자가 많이 확인한 KODEX 상품 예시입니다.<br>
    실제 서비스에서는 상품 상세 진입, 찜, 저장, 매수 확인 데이터를 기반으로 자동 집계할 수 있습니다.
    </div>
    {peer_cards_html}
    </div>
    """)

    c1, c2 = st.columns(2)

    with c1:
        first_peer = get_etf_by_code(peer_codes[0])
        if st.button("같은 유형 ETF 확인", type="primary", use_container_width=True):
            select_etf(first_peer["code"])

    with c2:
        if st.button("전체상품 보기", use_container_width=True):
            go("products")

    html(f"""
    <div class="event-banner">
    <div class="badge-soft">EVENT 연결</div>
    <div class="event-title">내 투자 MBTI 결과로<br>KODEX 뽑기 이벤트 참여하기</div>
    <div class="event-desc">
    결과 공유 버튼은 리포트가 아니라<br>
    KODEX 신규상장 ETF 뽑기 이벤트 페이지 안에서 제공됩니다.<br><br>
    이벤트 페이지에서 공유 링크를 만들고 결과를 공유하면<br>
    일반 응모권을 받을 수 있어요.
    </div>
    </div>
    """)

    if st.button("내 결과로 이벤트 참여하기", type="primary", use_container_width=True):
        open_event_page()

    html(f"""
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
    <div class="note-text">
    이 점수는 투자 실력 평가가 아니라, ETF를 볼 때 어떤 정보를 먼저 보고 어떤 항목을 놓치기 쉬운지 확인하기 위한 점수입니다.
    </div>
    </div>

    <div class="info-card">
    <div class="info-title">한 번 더 확인하면 좋은 항목</div>
    <ul class="summary-list">{missed_html}</ul>
    <div class="insight">
    이 항목은 ETF의 공식 확인 요소와 사용자의 체크리스트 응답을 함께 반영해 도출됩니다.
    즉, 단순 추천이 아니라 사용자가 놓치기 쉬운 확인 항목을 먼저 보여주는 구조입니다.
    </div>
    </div>

    <div class="info-card">
    <div class="info-title">투자 MBTI 결과 활용</div>
    <div class="point-desc">
    투자 MBTI는 사용자가 ETF를 볼 때 어떤 판단 기준에 더 민감한지 보여주는 요약 지표입니다.<br>
    기업은 전체 참여자의 투자 MBTI 분포, 같은 유형이 많이 확인한 ETF, 이벤트 공유 데이터를 통해
    20대가 어떤 성향으로 신규상장 ETF에 반응하는지 확인할 수 있습니다.
    </div>
    </div>
    """)

    c1, c2 = st.columns(2)

    with c1:
        if st.button("운영자 인사이트", use_container_width=True):
            go("insight")

    with c2:
        if st.button("다시 체크하기", use_container_width=True):
            start()

    if st.button("체크리스트 저장", use_container_width=True):
        st.session_state.saved = True
        st.session_state.mock_save_clicks += 1
        st.success("체크리스트가 저장되었습니다.")

    phone_footer()
    bottom_nav("checkpoint")


# =========================
# 11-1. 페이지: KODEX 신규상장 ETF 뽑기 이벤트
# =========================
def render_event_draw():
    raw, pct, weak = safe_scores()
    event_etf = get_event_etf()

    phone_header()

    page_title_bar("KODEX 뽑기 이벤트", default_back="home")

    html(f"""
    <div class="draw-hero">
    <div class="draw-event-label">{EVENT_INFO["title"]}</div>
    <div class="draw-kodex">KODEX</div>
    <div class="draw-product-name">반도체타겟위클리<br>커버드콜 ETF</div>
    <div class="draw-product-code">(종목코드 {EVENT_INFO["product_code"]})</div>
    <div class="draw-copy">
    {EVENT_INFO["copy_1"]}<br>
    {EVENT_INFO["copy_2"]}
    </div>
    <div class="draw-period">{EVENT_INFO["period"]}</div>
    <div class="winner-ticker">박**님 🪙 메가MGC커피 당첨 · 5시간 전</div>
    <div class="draw-machine">
    <div class="draw-machine-window">
    당첨 아이템이 든<br>인형을 뽑아보세요!
    </div>
    </div>
    </div>

    <div class="info-card">
    <div class="info-title">내 응모권</div>
    <div class="point-desc">
    모든 보상은 일반 응모권으로 통일됩니다.<br>
    투자 MBTI 결과 공유, 친구 체크리스트 완료, 친구 매수 확인 시 일반 응모권을 받을 수 있어요.
    </div>
    {ticket_summary_html()}
    <div class="note-text">
    오늘 지급된 응모권: {st.session_state.daily_tickets_issued}장 / 하루 최대 {EVENT_INFO["daily_ticket_limit"]}장
    </div>
    </div>
    """)

    if pct is None:
        html("""
        <div class="mbti-share-card">
        <div class="badge-event">CHECKPOINT 필요</div>
        <div class="info-title">아직 투자 MBTI 결과가 없어요</div>
        <div class="point-desc">
        응모권을 받으려면 먼저 KODEX CHECKPOINT를 완료하고 투자 MBTI 결과를 확인해주세요.
        </div>
        </div>
        """)

        if st.button("투자 MBTI 먼저 확인하기", type="primary", use_container_width=True):
            start()

    else:
        invest = get_invest_mbti(pct)
        habit = classify_habit(pct, weak)
        share_link = make_share_link(invest["code"])

        html(f"""
        <div class="mbti-share-card">
        <div class="badge-event">내 투자 MBTI 결과</div>
        <div class="share-code">{invest["code"]}</div>
        <div class="invest-type">{invest["title"]}</div>
        <div class="result-desc">
        {invest["desc"]}<br><br>
        ETF 확인 습관은 <b>{habit["type"]}</b>에 가까워요.
        </div>
        </div>

        <div class="info-card">
        <div class="info-title">결과 공유하고 응모권 받기</div>
        <div class="point-desc">
        아래 공유 링크를 친구에게 전달할 수 있어요.<br>
        내 투자 MBTI 결과를 공유하면 일반 응모권 1장을 받을 수 있습니다.
        </div>
        <div class="share-link-box">
        {share_link}
        </div>
        <div class="note-text">
        실제 서비스에서는 이 링크에 사용자 ID, 추천인 ID, 캠페인 ID가 연결되어
        친구의 체크리스트 완료와 매수 확인이 자동으로 추적됩니다.
        </div>
        </div>
        """)

        c1, c2 = st.columns(2)

        with c1:
            if st.button("링크 생성하기", use_container_width=True):
                ok, msg = copy_share_link()

                if ok:
                    st.success(msg)
                else:
                    st.warning(msg)

        with c2:
            if st.button("결과 공유하고 응모권 받기", type="primary", use_container_width=True):
                ok, msg = issue_share_ticket()

                if ok:
                    st.success(msg)
                else:
                    st.warning(msg)

        if st.session_state.share_link_copied:
            html("""
            <div class="share-complete">
            <div class="share-complete-title">공유 링크 생성 완료</div>
            <div class="point-desc">
            이 링크를 카카오톡, 문자, 인스타그램 프로필/스토리 링크 등으로 공유할 수 있어요.
            </div>
            </div>
            """)

        if st.session_state.shared_mbti:
            reward_messages = auto_issue_friend_rewards()

            html(f"""
            <div class="share-complete">
            <div class="share-complete-title">공유 완료!</div>
            <div class="point-desc">
            투자 MBTI 결과를 공유했어요.<br>
            현재까지 결과 공유로 받은 응모권: {st.session_state.share_count}장<br>
            친구 체크리스트 완료 보상: {st.session_state.friend_checklist_reward_count}장<br>
            친구 매수 확인 보상: {st.session_state.friend_buy_reward_count}장
            </div>
            </div>
            """)

            for msg in reward_messages:
                st.info(msg)

    html("""
    <div class="info-card">
    <div class="info-title">응모권으로 뽑기 참여</div>
    <div class="point-desc">
    보유한 일반 응모권으로 KODEX 신규상장 ETF 뽑기 이벤트에 참여할 수 있어요.<br>
    일반 응모권에는 꽝이 포함될 수 있습니다.
    </div>
    </div>
    """)

    if st.button("응모권으로 뽑기", type="primary", use_container_width=True):
        ok, result = draw_with_ticket()

        if ok:
            st.session_state.last_draw_result = result
        else:
            st.warning("사용 가능한 일반 응모권이 없습니다.")

    if st.session_state.last_draw_result:
        result = st.session_state.last_draw_result

        html(f"""
        <div class="draw-result">
        <div class="draw-result-emoji">{result["emoji"]}</div>
        <div class="draw-result-title">{result["title"]}</div>
        <div class="draw-result-desc">{result["desc"]}</div>
        </div>
        """)

    html(f"""
    <div class="referral-card">
    <div class="referral-title">친구 참여 현황</div>
    <div class="point-desc">
    공유 링크를 받은 친구가 체크리스트를 완료하거나 신규상장 ETF 매수 확인까지 이어지면
    공유자에게 일반 응모권이 자동 지급됩니다.<br><br>
    사용자가 직접 인증 버튼을 누르는 구조가 아니라, 실제 서비스에서는 공유 링크 추적과 매수 확인 데이터로 자동 처리됩니다.
    </div>
    {friend_status_html()}
    <div class="note-text">
    프로토타입 예시 상태입니다. 실제 서비스에서는 계정 중복 방지, 동일 친구 중복 인정 제한, 하루 지급 한도 제한이 필요합니다.
    </div>
    </div>

    <div class="event-product-card">
    <div class="badge-red">신규상장 이벤트 대상</div>
    <div class="event-product-title">{event_etf["name"]}</div>
    <div class="product-code">{event_etf["code"]}</div>
    <div class="product-meta">
    {event_etf["desc"]}
    </div>
    <div class="insight">
    CHECKPOINT는 이벤트 참여 이후에도 사용자가 상품을 바로 판단하지 않고,
    기초지수·구성종목·분배금·유의사항을 먼저 확인하도록 연결합니다.
    </div>
    </div>
    """)

    c1, c2 = st.columns(2)

    with c1:
        if st.button("신규상장 ETF 정보 확인", type="primary", use_container_width=True):
            select_etf(event_etf["code"])

    with c2:
        if st.button("전체상품 보기", use_container_width=True):
            go("products")

    html(f"""
    <div class="info-card">
    <div class="info-title">응모권 지급 기준</div>
    <div class="event-rule-card">
    <div class="event-rule-title">1. 내 투자 MBTI 결과 공유</div>
    <div class="event-rule-desc">
    이벤트 페이지에서 공유 링크를 생성하고 결과를 공유하면 일반 응모권 1장 지급
    </div>
    </div>
    <div class="event-rule-card">
    <div class="event-rule-title">2. 친구 체크리스트 완료</div>
    <div class="event-rule-desc">
    공유받은 친구가 링크로 접속해 KODEX CHECKPOINT를 완료하면 일반 응모권 1장 지급
    </div>
    </div>
    <div class="event-rule-card">
    <div class="event-rule-title">3. 친구 신규상장 ETF 매수 확인</div>
    <div class="event-rule-desc">
    친구가 신규상장 ETF 정보를 확인한 뒤 본인 판단으로 매수까지 이어지고, 시스템에서 매수 확인이 완료되면 일반 응모권 1장 지급
    </div>
    </div>
    <div class="event-rule-card">
    <div class="event-rule-title">지급 제한</div>
    <div class="event-rule-desc">
    모든 경로 합산 하루 최대 {EVENT_INFO["daily_ticket_limit"]}장까지 지급 · 동일 친구 중복 인정 불가 · 본인 계정 간 공유 인정 불가
    </div>
    </div>
    <div class="note-text">
    실제 서비스에서는 공유 링크 추적, 동일 계정 중복 방지, 매수 확인 API 또는 이벤트 인증 절차가 필요합니다.
    </div>
    </div>
    """)

    phone_footer()
    bottom_nav("event_draw")


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

    event_badge = event_target_badge_html(etf)

    return f"""
    <div class="product-list-card">
    <div style="display:flex; justify-content:space-between; align-items:start; gap:10px;">
    <div>
    {event_badge}
    <div class="product-name">{etf["name"]}</div>
    <div class="product-code">{etf["code"]}</div>
    </div>
    <div>{favorite_badge_html(etf["code"])}</div>
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
    event_etf = get_event_etf()

    phone_header()

    page_title_bar("전체상품", default_back="home")

    html(f"""
    <div class="search-box">🔍 &nbsp; 상품명 혹은 종목코드 검색</div>
    <div class="caption">최근 갱신 {now_text()} · 프로토타입 샘플 데이터</div>

    <div class="event-product-card">
    <div class="badge-red">EVENT 대상 신규상장 ETF</div>
    <div class="event-product-title">{event_etf["name"]}</div>
    <div class="product-code">{event_etf["code"]}</div>
    <div class="product-meta">{event_etf["desc"]}</div>
    <div class="insight">
    이벤트 페이지에서 투자 MBTI 결과를 공유하면 일반 응모권을 받을 수 있고,
    이 상품의 구조와 유의사항까지 이어서 확인할 수 있어요.
    </div>
    </div>
    """)

    c1, c2 = st.columns(2)

    with c1:
        if st.button("이벤트 페이지", type="primary", use_container_width=True):
            open_event_page()

    with c2:
        if st.button("이벤트 ETF 확인", use_container_width=True):
            select_etf(event_etf["code"])

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
        invest = get_invest_mbti(pct)

        html(f"""
        <div class="check-card">
        <div class="badge">REPORT 기반</div>
        <div class="check-title">{habit["type"]}을 위한<br>상품 확인 순서</div>
        <div class="check-desc">
        투자 MBTI {invest["code"]} 유형의 리포트와 상품 유형을 함께 반영했어요.<br>
        각 ETF 카드에 표시된 ‘먼저 확인하면 좋은 항목’을 보고
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

        c1, c2, c3 = st.columns([1.4, 1, 1])

        with c1:
            if st.button(f"{etf['name']} 상품 확인", key=f"open_{etf['code']}", use_container_width=True):
                select_etf(etf["code"])

        with c2:
            fav_label = "♥ 찜 해제" if is_favorite(etf["code"]) else "♡ 찜"

            if st.button(fav_label, key=f"fav_{etf['code']}", use_container_width=True):
                toggle_favorite(etf["code"])
                st.rerun()

        with c3:
            is_compared = etf["code"] in st.session_state.compare_codes
            label = "비교 해제" if is_compared else "비교"

            if st.button(label, key=f"compare_{etf['code']}", use_container_width=True):
                if is_compared:
                    st.session_state.compare_codes.remove(etf["code"])
                else:
                    st.session_state.compare_codes.append(etf["code"])

                st.rerun()

    if st.session_state.favorite_codes:
        html('<div class="section-title">내가 찜한 ETF</div>')

        favorite_rows = []

        for code in st.session_state.favorite_codes:
            item = get_etf_by_code(code)
            favorite_rows.append({
                "상품명": item["name"],
                "현재가": f'{item["price"]:,}원',
                "1주 수익률": f'+{item["return_1w"]:.1f}%',
                "확인 포인트": " · ".join(get_product_checkpoints(item, pct, weak)[:3]),
            })

        st.dataframe(pd.DataFrame(favorite_rows), use_container_width=True, hide_index=True)

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
            f"{checkpoint_desc(item, etf)}<br><br>"
            f"<b>왜 확인해야 하나요?</b><br>{checkpoint_reason(item, etf, pct)}<br><br>"
            f"<b>연결 위치</b> · {checkpoint_to_tab(item)}"
        )
        for idx, item in enumerate(items)
    ])

    if etf["change"] >= 0:
        detail_change = f"▲ {etf['change']:,} ({etf['change_pct']:.2f}%)"
    else:
        detail_change = f"▼ {abs(etf['change']):,} ({abs(etf['change_pct']):.2f}%)"

    phone_header()

    page_title_bar("ETF 상품정보", default_back="products")

    html(f"""
    <div class="purple-hero">
    <div style="display:flex; justify-content:space-between; gap:10px; align-items:flex-start;">
    <div>
    {event_target_badge_html(etf)}
    <div class="badge-soft">{etf["region"]} · {etf["kind"]}</div>
    <div class="purple-title">{etf["name"]}</div>
    <div style="font-size:19px;font-weight:900;margin-bottom:12px;">{etf["code"]}</div>
    </div>
    <div>{favorite_badge_html(etf["code"])}</div>
    </div>
    <div class="purple-desc">{etf["desc"]}</div>
    <div class="tag-wrap">{tags}</div>
    </div>

    <div class="price-grid">
    <div class="price-box">
    <div class="price-label">현재가(원)</div>
    <div class="price-num">{etf["price"]:,}</div>
    <div class="price-up">{detail_change}</div>
    </div>

    <div class="price-box">
    <div class="price-label">기준가 iNAV(원)</div>
    <div class="price-num">{etf["nav"]:,}</div>
    <div class="note-text">거래량 {etf["volume"]:,}주</div>
    </div>
    </div>
    """)

    if etf.get("event_target"):
        html("""
        <div class="event-banner">
        <div class="badge-soft">EVENT 대상</div>
        <div class="event-title">이 상품은 신규상장 ETF<br>뽑기 이벤트 대상입니다</div>
        <div class="event-desc">
        투자 MBTI 결과를 이벤트 페이지에서 공유하고 응모권을 받은 뒤,
        상품정보를 기준 있게 확인해보세요.
        </div>
        </div>
        """)

        if st.button("KODEX 뽑기 이벤트로 이동", type="primary", use_container_width=True):
            open_event_page()

    fav_label = "♥ 찜 해제하기" if is_favorite(etf["code"]) else "♡ 관심 ETF 찜하기"

    if st.button(fav_label, key=f"detail_fav_{etf['code']}", use_container_width=True):
        toggle_favorite(etf["code"])
        st.rerun()

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
            st.session_state.mock_save_clicks += 1
            st.success("체크리스트가 저장되었습니다.")

    phone_footer()
    bottom_nav("products")


# =========================
# 14. 페이지: 운영자 인사이트
# =========================
def render_insight():
    raw, pct, weak = safe_scores()

    phone_header()

    page_title_bar("운영자 인사이트", default_back="home")

    total = st.session_state.mock_total_participants
    save_rate = round(st.session_state.mock_save_clicks / total * 100, 1)
    fav_rate = round(st.session_state.mock_favorite_clicks / total * 100, 1)
    product_rate = round(st.session_state.mock_product_clicks / total * 100, 1)
    event_view_rate = round(st.session_state.mock_event_page_visits / total * 100, 1)
    share_rate = round(st.session_state.mock_share_clicks / total * 100, 1)
    draw_rate = round(st.session_state.mock_draw_plays / max(st.session_state.mock_general_tickets_issued, 1) * 100, 1)
    friend_check_rate = round(st.session_state.mock_referral_checklist_complete / max(st.session_state.mock_referral_visits, 1) * 100, 1)
    buy_confirm_rate = round(st.session_state.mock_referral_buy_confirm / max(st.session_state.mock_referral_visits, 1) * 100, 1)

    top_mbti = PARTICIPANT_MBTI_STATS[0]
    top_three = PARTICIPANT_MBTI_STATS[:3]

    html(f"""
    <div class="section-title">기업 활용 데이터 예시</div>
    <div class="caption">
    CHECKPOINT는 20대가 ETF를 보기 전 어떤 정보를 먼저 보고,
    어떤 성향의 사용자가 이벤트 공유와 신규상장 ETF 확인까지 이어지는지 확인할 수 있는 데이터 접점이 될 수 있습니다.
    </div>

    <div class="mini-kpi-grid">
    <div class="mini-kpi">
    <div class="mini-kpi-num">{total:,}</div>
    <div class="mini-kpi-label">누적 참여자</div>
    </div>
    <div class="mini-kpi">
    <div class="mini-kpi-num">{top_mbti["pct"]}%</div>
    <div class="mini-kpi-label">최다 MBTI 비율</div>
    </div>
    <div class="mini-kpi">
    <div class="mini-kpi-num">{share_rate}%</div>
    <div class="mini-kpi-label">결과 공유율</div>
    </div>
    <div class="mini-kpi">
    <div class="mini-kpi-num">{buy_confirm_rate}%</div>
    <div class="mini-kpi-label">매수 확인율</div>
    </div>
    </div>

    <div class="info-card">
    <div class="info-title">수집 가능한 지표</div>
    <div class="point-desc">
    · 전체 참여자 중 투자 MBTI 비율<br>
    · 같은 투자 MBTI 유형이 많이 확인한 ETF<br>
    · 이벤트 페이지 진입률<br>
    · 공유 링크 생성 수<br>
    · 결과 공유 클릭률<br>
    · 공유 링크 유입 수<br>
    · 친구 체크리스트 완료 수<br>
    · 친구 체크리스트 완료율<br>
    · 신규상장 ETF 상품정보 진입률<br>
    · 친구 매수 확인 수<br>
    · 일반 응모권 총 지급 수<br>
    · 하루 지급 한도 도달 사용자 수<br>
    · MBTI 유형별 공유율<br>
    · MBTI 유형별 친구 유입률<br>
    · MBTI 유형별 신규상장 ETF 관심도
    </div>
    </div>

    <div class="insight">
    기업은 전체 참여자 중 어떤 투자 MBTI가 많은지뿐 아니라,
    어떤 유형이 자신의 결과를 공유하고, 친구 유입과 체크리스트 완료,
    신규상장 ETF 정보 확인과 매수 확인까지 이어지는지 파악할 수 있습니다.
    </div>
    """)

    html("""
    <div class="info-card">
    <div class="info-title">이벤트 성과 지표</div>
    <div class="point-desc">
    프로토타입 예시 데이터입니다. 실제 서비스에서는 이벤트 로그와 공유 링크, 인증 데이터를 기반으로 자동 집계됩니다.
    </div>
    </div>
    """)

    html(event_metric_bar_html(
        "이벤트 페이지 진입률",
        min(event_view_rate, 100),
        f"이벤트 페이지 방문 {st.session_state.mock_event_page_visits:,}회"
    ))

    html(event_metric_bar_html(
        "투자 MBTI 결과 공유율",
        min(share_rate, 100),
        f"공유 클릭 {st.session_state.mock_share_clicks:,}회 · 공유 링크 생성 {st.session_state.mock_share_link_created:,}회"
    ))

    html(event_metric_bar_html(
        "친구 체크리스트 완료율",
        min(friend_check_rate, 100),
        f"공유 링크 유입 {st.session_state.mock_referral_visits:,}회 · 체크리스트 완료 {st.session_state.mock_referral_checklist_complete:,}회"
    ))

    html(event_metric_bar_html(
        "친구 매수 확인율",
        min(buy_confirm_rate, 100),
        f"공유 링크 유입 {st.session_state.mock_referral_visits:,}회 · 매수 확인 {st.session_state.mock_referral_buy_confirm:,}회"
    ))

    html(event_metric_bar_html(
        "뽑기 참여율",
        min(draw_rate, 100),
        f"뽑기 참여 {st.session_state.mock_draw_plays:,}회"
    ))

    html(f"""
    <div class="info-card">
    <div class="info-title">응모권 지급 현황</div>
    <div class="point-desc">
    일반 응모권 총 지급 수: {st.session_state.mock_general_tickets_issued:,}장<br>
    친구 체크리스트 완료 보상 수: {st.session_state.mock_referral_checklist_complete:,}장<br>
    친구 매수 확인 보상 수: {st.session_state.mock_referral_buy_confirm:,}장<br>
    하루 지급 한도 도달 사용자 수: {st.session_state.mock_daily_limit_users:,}명<br>
    신규상장 ETF 상품정보 진입 수: {st.session_state.mock_event_product_clicks:,}회
    </div>
    </div>
    """)

    html("""
    <div class="info-card">
    <div class="info-title">전체 참여자 투자 MBTI 비율</div>
    <div class="point-desc">
    프로토타입 예시 데이터입니다. 실제 서비스에서는 체크리스트 응답 로그를 기반으로 자동 집계됩니다.
    </div>
    </div>
    """)

    for item in PARTICIPANT_MBTI_STATS:
        html(stat_bar_html(
            item["code"],
            item["name"],
            item["pct"],
            f"참여자 {item['count']}명 · {INVEST_MBTI_CATALOG.get(item['code'], {}).get('short', '')}"
        ))

    stats_df = pd.DataFrame(PARTICIPANT_MBTI_STATS)
    chart_df = stats_df[["code", "pct"]].set_index("code")

    st.bar_chart(chart_df)

    html("""
    <div class="info-card">
    <div class="info-title">MBTI 유형별 이벤트 반응</div>
    <div class="point-desc">
    어떤 투자 성향이 공유를 많이 하고, 어떤 유형이 친구 체크리스트 완료와 신규상장 ETF 확인, 매수 확인까지 이어지는지 비교할 수 있습니다.
    </div>
    </div>
    """)

    event_stats_df = pd.DataFrame(EVENT_MBTI_STATS)
    st.dataframe(
        event_stats_df.rename(columns={
            "code": "투자 MBTI",
            "share_rate": "공유율(%)",
            "friend_check_rate": "친구 체크리스트 완료율(%)",
            "event_view_rate": "이벤트 진입률(%)",
            "buy_confirm_rate": "매수 확인율(%)",
        }),
        use_container_width=True,
        hide_index=True,
    )

    html(f"""
    <div class="info-card">
    <div class="info-title">기업 활용 해석 예시</div>
    {point_item("트렌드 반응형 비중 확인", f"{top_three[0]['code']}형이 {top_three[0]['pct']}%로 가장 높게 나타나면, 20대가 성장 테마와 수익률에 빠르게 반응한다는 인사이트를 얻을 수 있습니다.")}
    {point_item("같은 유형이 많이 확인한 ETF 확인", "투자 MBTI별로 많이 확인한 ETF를 보면, 성향별 관심 상품과 콘텐츠 연결 방향을 파악할 수 있습니다.")}
    {point_item("공유율과 친구 유입률 확인", "투자 MBTI 결과 공유율과 친구 체크리스트 완료율을 함께 보면, 어떤 유형의 결과가 자발적 확산으로 이어지는지 확인할 수 있습니다.")}
    {point_item("신규상장 ETF 관심도 확인", "이벤트 대상 ETF의 상품정보 진입률을 보면 이벤트가 단순 참여에서 상품 확인 행동으로 이어졌는지 판단할 수 있습니다.")}
    {point_item("응모권 구조 효과 확인", "결과 공유, 친구 체크리스트 완료, 친구 매수 확인이라는 단계별 응모권 지급 구조가 실제 행동 전환에 얼마나 기여하는지 분석할 수 있습니다.")}
    </div>
    """)

    if pct is not None:
        habit = classify_habit(pct, weak)
        invest = get_invest_mbti(pct)
        missed = ", ".join(missed_items(pct, weak))
        favorites = ", ".join([get_etf_by_code(code)["name"] for code in st.session_state.favorite_codes]) or "없음"
        peer_names = ", ".join([get_etf_by_code(code)["name"] for code in get_peer_etf_codes(invest["code"])])

        html(f"""
        <div class="info-card">
        <div class="info-title">현재 사용자 예시</div>
        <div class="point-desc">
        투자 MBTI: {invest["code"]} · {invest["title"]}<br>
        확인 유형: {habit["type"]} · {habit["mbti"]}<br>
        보완 항목: {missed}<br>
        같은 유형이 많이 확인한 ETF: {peer_names}<br>
        찜한 ETF: {favorites}<br>
        보유 일반 응모권: {st.session_state.normal_tickets}장<br>
        오늘 지급된 응모권: {st.session_state.daily_tickets_issued}장
        </div>
        </div>
        """)

    phone_footer()
    bottom_nav("insight")


# =========================
# 15. 라우팅
# =========================
if st.session_state.page == "home":
    render_home()
elif st.session_state.page == "checklist":
    render_checklist()
elif st.session_state.page == "report":
    render_report()
elif st.session_state.page == "event_draw":
    render_event_draw()
elif st.session_state.page == "products":
    render_products()
elif st.session_state.page == "product_detail":
    render_product_detail()
elif st.session_state.page == "insight":
    render_insight()
else:
    render_home()
