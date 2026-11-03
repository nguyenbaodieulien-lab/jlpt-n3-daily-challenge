#!/usr/bin/env python3
"""Publish only pre-reviewed, complete lesson banks. No scraping or AI guessing."""
import argparse, datetime as dt, json, pathlib, sys
from zoneinfo import ZoneInfo
ROOT=pathlib.Path(__file__).resolve().parents[1]
START=dt.date(2026,11,4)

def target(day):
    offset=(day-START).days
    if offset<0: raise ValueError('Start date not reached')
    chapter=offset//6+1
    slot=offset%6+1
    if chapter>12: raise ValueError('All 12 chapters completed; schedule needs review')
    return chapter,slot

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--date',help='YYYY-MM-DD in JST; defaults to today in JST'); args=ap.parse_args()
    day=dt.date.fromisoformat(args.date) if args.date else dt.datetime.now(ZoneInfo('Asia/Tokyo')).date()
    ch,slot=target(day)
    name=f'chapter-{ch:02d}-'+(f'lesson-{slot:02d}' if slot<=5 else 'review')+'.json'
    path=ROOT/'data'/'banks'/name
    if not path.exists():
        print(f'MISSING REVIEWED BANK: {path.relative_to(ROOT)}. Publication stopped; no fake lesson created.',file=sys.stderr)
        return 2
    data=json.loads(path.read_text(encoding='utf-8'))
    if data.get('reviewed') is not True or data.get('chapter')!=ch or data.get('lesson')!=(slot if slot<=5 else 'review'):
        print('Lesson metadata not reviewed or mismatched',file=sys.stderr);return 2
    words=data.get('words')
    if not isinstance(words,list) or len(words)<10:
        print('Need at least 10 verified words for the existing game',file=sys.stderr);return 2
    required=('w','r','m','syn','note','ex','vi','blank','answer')
    if any(not isinstance(w,dict) or any(not isinstance(w.get(k),str) or not w[k].strip() for k in required) for w in words):
        print('Invalid vocabulary record',file=sys.stderr);return 2
    if len({w['w'] for w in words})!=len(words):
        print('Duplicate vocabulary terms',file=sys.stderr);return 2
    result={'dateJST':day.isoformat(),'chapter':ch,'lesson':slot if slot<=5 else 'review','title':f'Chương {ch} · '+(f'Bài {slot}' if slot<=5 else 'Tổng hợp'),'challengeId':f'N3-{day.isoformat()}-C{ch}L{slot}','words':words,'sourceBank':name}
    out=ROOT/'data'/'daily.json';out.write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    print(f'Published {out.relative_to(ROOT)}: {result["title"]} / {len(words)} words / {day}')
    return 0
if __name__=='__main__':sys.exit(main())
