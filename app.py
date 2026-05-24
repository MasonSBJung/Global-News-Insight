import streamlit as st
import feedparser
import urllib.parse
from deep_translator import GoogleTranslator

st.set_page_config(page_title="Global News Insight", layout="wide")
st.title("🌐 Global News Insight_JSB")

# 언론사 설정
media_lineup = {
    "Right Media": ["Fox News", "The Wall Street Journal"],
    "Left Media": ["CNN", "The New York Times"],
    "Centrist Media": ["Reuters", "Bloomberg"]
}

keyword = st.text_input("검색 키워드 입력:", "M7 Stock")

if st.button("분석 시작"):
    encoded = urllib.parse.quote(keyword)
    rss_url = f"https://news.google.com/rss/search?q={encoded}&hl=en-US&gl=US&ceid=US:en"
    feed = feedparser.parse(rss_url)
    
    for category, publishers in media_lineup.items():
        st.subheader(f"🔷 {category}")
        for entry in feed.entries:
            source = entry.source.get('title', '')
            if any(p.lower() in source.lower() for p in publishers):
                st.write(f"[{source}] {entry.title}")
                st.link_button("기사 원문 보기", entry.link)