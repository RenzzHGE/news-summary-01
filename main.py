# news-summary-01 entry (Python 3.13, standard library only).
# Writes one summary of the world's news of Wednesday 11 November 2026
# to <output>/entry.txt. Runs twice with byte-identical output, no network.
# Outside the grader's container, MAKEFUN_OUTPUT_DIR stands in for /output:
#   mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py

import os
from pathlib import Path

SUMMARY = """World news, Wednesday 11 November 2026: Two days of US-mediated talks between Ukraine and Russia ended in Abu Dhabi with agreement on a large prisoner exchange but no ceasefire, and President Zelenskyy rejected proposals for Ukrainian troops to withdraw from Donbas (NPR). At the COP31 climate summit in Antalya, UN chief Antonio Guterres told 102 heads of state and government that slow action had put the world on a path to destruction, while Australia, Bangladesh, Kenya, Nigeria and Vanuatu backed a pledge to double homes with rooftop solar by 2030 (AFP). US Secretary of State Marco Rubio said the pressure campaign on Iran had worked and there was no need for major combat operations any longer (New York Times), as the Justice Department charged three Iran-backed operatives over about 20 plots in the US and Europe (Justice Department). Israeli strikes killed at least eight people in Gaza, including a father and his 13-year-old son, as the Gaza truce frayed (local health officials). The US House voted 211-204 to send impeachment articles against Defense Secretary Pete Hegseth to committee, ending the effort, and House Republicans elected Jim Jordan as minority leader (House). British counterterrorism police arrested a 41-year-old US Army officer near Gloucester, England, on suspicion of spying for Russia (British police). Four million workers joined Spain's first general strike since 2012 over a housing shortage of 750,000 homes (Reuters). Anthropic filed to list on Nasdaq seeking a $1.4 trillion valuation (filing), and a hot inflation report made a December Federal Reserve rate rise look near certain. Kenya, with no new Ebola infections since 19 October, began the 42-day countdown to being declared Ebola-free (health officials)."""

def main():
    outdir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    outdir.mkdir(parents=True, exist_ok=True)
    (outdir / "entry.txt").write_text(SUMMARY, encoding="utf-8")

if __name__ == "__main__":
    main()
