# Truth audit: Grokipedia, "Baruch Spinoza"

**Page audited:** grokipedia.com Baruch Spinoza article, using the saved page [`snapshots/2026-10-01.html`](../../snapshots/2026-10-01.html). A live re-fetch on Thu 1 Oct 2026 (PT) returned the same byte size (629,108) and the same 152-source list.
**Run:** first test run of the standing audit method. Tool: [`tools/grokaudit/grokaudit.py`](../../../../../../tools/grokaudit/README.md). Log: `spinoza_audit_log.csv`.

## 1. Summary

The article's prose gets the outline of Spinoza's life and the Ethics' main doctrines broadly right. Its citation apparatus, however, is badly broken. From about [90] onward every inline number points to the wrong source: the intended source is the listed one nine places earlier. Numbers [153]–[161] point to nothing at all. So 110 of the 389 citation markers (28%) lead a reader to an unrelated or missing source; 97 sentences are affected. The other bot's report of "153–161 missing" is correct but understates the problem.

Below the citation layer there are real factual errors, concentrated in the correspondence section and in several Ethics locators:
- misnumbered letters: Blyenbergh replies Epp. 19, 21, 23 and 27 (old Letter 38), Boxel Epp. 51–56, Ep. 69 to van Velthuysen, and Tschirnhaus correspondence; Letter 73 is not from June 1666;
- E2P7 labelled as Part I Prop 7;
- Spinoza buried "near Grotius" instead of near Johan de Witt;
- Leibniz's visit dated "4 November 1676" instead of c. 18–21 November;
- a "1678 papal condemnation" that was actually a Dutch civil ban (Wiltens: States of Holland and West Friesland; Spinoza Web: Supreme Court); the Court of Holland had banned the TTP in 1674;
- the PCP called "anonymous" when it carried Spinoza's name.

Framing is mostly even-handed on pantheism versus atheism, but leans on an unexplained house term, "causal realism", and on present-day labels such as "blueprints for secular governance".

## 2. Counts

All numbers below come from `grokaudit.py parse`/`linkcheck`/`soft404` (structure) and `grokaudit.py report spinoza_audit_log.csv` (verdicts). None are estimated.

**Structure** (`data/structure.json`, `data/linkcheck.csv`)

| item | count |
|---|---|
| paragraphs / sentences (claims) | 125 / 401 |
| cited sentences / uncited sentences | 325 / 76 |
| uncited with no later citation anywhere in the paragraph | 13 |
| citation markers / distinct numbers cited / sources listed | 389 / 161 / 152 |
| dangling numbers (cited, no source): [153]–[161] | 9 numbers, 9 markers, in 7 sentences (C393, C395–C397, C399–C401) |
| markers ≥ [90] (shifted by −9, see §4) | 110, of which 101 point to a wrong source and 9 dangle |
| markers in the ambiguous zone [81]–[89] | 11 |
| sentences with ≥1 shifted/dangling cite | 97 |
| duplicate source URLs / unused sources | 0 / 0 |
| malformed source URL | 1 (ref 80, Wikisource URL cut at `Ethics_(Spinoza`), plus 1 markup leak in the text (C213 `./Part_3#Proposition_6)`) |
| linkcheck: OK / OK but paywall-likely / bot-blocked / paywall 401 / unreachable (SSL) | 103 / 25 / 15 / 1 / 1 |
| dead links (404) | 7: refs 51, 52, 71, 80, 91, 107, 132 |
| soft-404 or bot-wall pages returning 200 | ref 53 ("Page not found"), refs 38 and 115 (bot wall), plus 11 near-empty fetches (see `soft404` output) |

**Claim verdicts** (`spinoza_audit_log.csv`, 401 rows)

The "verdict" column scores each citation as linked, which is what a reader clicking the number gets.

| verdict | count |
|---|---|
| SUPPORTED | 121 |
| MISCITED | 69 |
| UNSUPPORTED | 7 |
| UNCITED | 76 (42 priority sentences checked against sources/primary texts, plus 34 flagged by script only) |
| UNVERIFIABLE | 24 |
| NOT_CHECKED (outside priority set and sample) | 104 |
| sentences with a factual problem (`factual_issue = Y`, any verdict) | 41 |

For the shifted citations, each claim was also checked against the source it was evidently meant to cite (n − 9). That column, `verdict_vs_intended`, covers 54 claims: SUPPORTED 28, UNVERIFIABLE 16, MISCITED 8, UNSUPPORTED 2. The UNSUPPORTED cases are C324 and C368. So for about half of the shifted claims, the right source does exist in the list. It is just mis-numbered.

**Coverage.** 263 claims were judged by hand:
- all 181 priority cited claims (dates, places, people, quotes, publication history, cherem, every Ethics/TTP/TP/TIE/letter reference);
- all 42 priority uncited claims;
- a seeded random sample of 40 of the remaining 144 non-priority cited claims (seed 1656).

The remaining 104 cited non-priority claims are NOT_CHECKED. Hand checks were done at four depths: read the source passage (72), keyword plus best-passage skim (106), checked against the primary text (51), and title/abstract only (8). The remaining rows are script-only (34) or not checked (130).

## 3. Problem claims

The **systemic** problem comes first because it affects the most claims:

| claim | fragment | cited | verdict | reason | correct fact / citation |
|---|---|---|---|---|---|
| ~97 sentences, C223–C401 | e.g. TTP prophecy claims citing [98] | [90]–[152] | MISCITED (as linked) | The displayed source list was renumbered, apparently after 9 entries were dropped, but the inline numbers were not. Mean claim–source word overlap at n is 0.13; at n − 9 it is 0.63 (42 of 45 claims in 90–120 match better at n − 9). | Read [n] as source n − 9. Example: [98] = ref 89, the Bennett TTP (<https://www.earlymoderntexts.com/assets/pdfs/spinoza1669.pdf>), not ref 98 (Cambridge Lexicon, Short Treatise) |
| C393, C395–C397, C399–C401 | e.g. Melamed denied filming, 2021 | [153]–[161] | UNVERIFIABLE (as linked) | There are no sources 153–161 | Intended sources are refs 144–152. Example: [159] = ref 150, Times of Israel, 30 Nov 2021 (<https://www.timesofisrael.com/in-echo-of-excommunication-top-spinoza-scholar-banned-from-amsterdam-synagogue/>) |

Next, every claim with a factual problem or an UNSUPPORTED verdict (41 rows, generated from the log). Fragments are cut at 70 characters. "vs intended" is the verdict against source n − 9 where the shift applies.

| claim | fragment | cited | verdict | reason | correct fact / citation |
|---|---|---|---|---|---|
| C008 | Michael's first wife had died in 1627, leaving two daughters, Miriam a… | [8][9] | SUPPORTED | JE 1906 does say this, but its genealogy is outdated | Spinoza Web: Michael's first wife Rachel d. 1627. Miriam, Isaac, Rebecca, Gabriel and Baruch were most likely all Hanna Deborah's children — <https://spinozaweb.org/people/4> |
| C011 | Michael's father, Abraham Michael de Spinoza, had been a community lea… | [8] | SUPPORTED | JE does say this, but modern scholarship differs | Spinoza Web: Abraham de Spinoza (of Nantes) was Michael's uncle and father-in-law, not his father — <https://spinozaweb.org/people/4> |
| C031 | His father, Michael de Spinoza, managed the firm until his death on Ma… | [3][14] | MISCITED | NEH (ref 3) says "his brother Gabriel", not half-brother | Brother Gabriel (Spinoza Web treats both as Hanna's sons) — <https://www.neh.gov/article/why-spinoza-was-excommunicated> |
| C038 | The decree, pronounced publicly in Hebrew and Portuguese during servic… | [18] | UNSUPPORTED | Only a Portuguese text of the herem survives, in the community's record book. "Pronounced in Hebrew and Portuguese" is not supported | Extant text is Portuguese (Livro dos Acordos da Nação) — <https://www.neh.gov/article/why-spinoza-was-excommunicated> |
| C041 | Spinoza had reportedly rejected rabbinic interpretations of Scripture,… | [19][20] | UNSUPPORTED | Uriel da Costa was excommunicated in 1618 and 1623, readmitted, banned again, and died in 1640; there was no "expulsion in 1640". The rest is plausible | Da Costa bans 1618/1623; suicide 1640 — <https://plato.stanford.edu/entries/spinoza/> |
| C043 | A secondary factor was Spinoza's legal challenge to communal inheritan… | [3] | UNSUPPORTED | NEH: Spinoza had himself declared an orphan by Amsterdam authorities to escape his father's debts, not to claim an inheritance share | Orphan declaration (1656) to shed the estate's debts — <https://www.neh.gov/article/why-spinoza-was-excommunicated> |
| C053 | Jelles, a wealthy ship-owner, later funded Spinoza's publications and … | — | UNCITED | No citation. De Vries's 2,000 florins was a gift Spinoza refused; the annuity came later via his will (ref 24: 500 cut to 300/250). "Wealthy ship-owner" for Jelles is unverified (ref 17: he financed the PCP) | Colerus via ref 24 — <https://justinmurphy.studio/spinoza/> |
| C062 | This self-sufficiency was deliberate: Spinoza rejected a large annuity… | [32] | UNVERIFIABLE | Ref 32 is a paywalled OUP chapter (abstract only) | Colerus: de Vries offered 2,000 florins, which Spinoza refused. The annuity was from de Vries's will (500, reduced to 300 or 250) after his death in 1667, not "around 1661" (ref 24) — <https://justinmurphy.studio/spinoza/> |
| C064 | Supplemented sparingly by gifts from a small circle of supporters, suc… | [33] | MISCITED | No "Pieter Serrurier" in ref 33. Probably a garbled Petrus Serrarius, who was a friend and go-between rather than a known patron | Petrus Serrarius (Collegiant millenarian, intermediary for letters) — <https://academic.oup.com/> |
| C076 | Spinoza maintained scientific correspondences, exchanging 34 letters w… | [35] | SUPPORTED | Spinoza Web reports a different total, but the standard numbering has exactly 28 Spinoza–Oldenburg letters; 18 fall in 1661–65. This also corrects the article's C327 count. | Exactly 28 letters: Epp. 1–7, 11, 13, 14, 16, 25, 26, 29–33, 61, 62, 68, 71, 73–75, 77–79; 18 fall in 1661–65 — <https://www.earlymoderntexts.com/assets/pdfs/spinoza1661.pdf> |
| C101 | In Letter 32 (dated November 1665), Spinoza argued that every part of … | — | UNCITED | Letter 32 (20 Nov 1665) is about parts agreeing with the whole (the worm in the blood), but Spinoza does not "reject mechanistic alternatives like Descartes". He says Descartes' rules of motion are false | Ep. 32 — <https://www.earlymoderntexts.com/assets/pdfs/spinoza1661.pdf> |
| C102 | Oldenburg subsequently shared details of Christiaan Huygens's experime… | — | UNCITED | The nitre experiments were Boyle's (Ep. 6, 1662), not Huygens'. Letter 73 is from late 1675, not June 1666. It does contain the immanent-cause passage | Boyle nitre: Epp. 6, 11, 13. Ep. 73: late 1675 — <https://www.earlymoderntexts.com/assets/pdfs/spinoza1661.pdf> |
| C104 | Spinoza's exchanges with Leibniz occurred late in his life, around 167… | — | UNCITED | Epp. 45–46 (Oct and Nov 1671) are the surviving Leibniz–Spinoza letters and concern optics. Leibniz sought the Ethics through Schuller in Nov 1675 (Epp. 70 and 72), and the 1676 contact was an in-person visit, so “around 1676” is not baseless. | Epp. 45–46 (Oct–Nov 1671); Ethics sought through Schuller in Nov 1675 (Epp. 70, 72); visit c. 18–21 Nov 1676 — <https://www.earlymoderntexts.com/assets/pdfs/spinoza1661.pdf> |
| C105 | In Letter 69, Spinoza outlined how the infinite intellect comprehends … | [50] | UNSUPPORTED | Ep. 69 is to Lambert van Velthuysen and dates from Sep–Nov 1675, not 1671; the 1671 Velthuysen items are Epp. 42–43. It is not a Leibniz letter and does not make the article’s claim. | Ep. 69 to van Velthuysen, Sep–Nov 1675; the 1671 Velthuysen items are Epp. 42–43. Leibniz–Spinoza letters are Epp. 45–46 (1671, optics) — <https://www.earlymoderntexts.com/assets/pdfs/spinoza1661.pdf> |
| C106 | Theological debates featured prominently with Willem van Blyenbergh, a… | — | UNCITED | Blyenbergh (from 12 Dec 1664) questioned the PCP and its appendix (Cogitata Metaphysica), not the Short Treatise | Ep. 18 on the PCP/CM — <https://www.earlymoderntexts.com/assets/pdfs/spinoza1661.pdf> |
| C107 | Spinoza replied in Letters 27–29, insisting that evil arises from priv… | — | UNCITED | The replies to Blyenbergh are Epp. 19 (5 Jan 1665), 21 (28 Jan), 23 (13 Mar) and 27 (3 Jun); Ep. 28 is to Bouwmeester and Ep. 29 is from Oldenburg. | Epp. 19 (5 Jan 1665), 21 (28 Jan), 23 (13 Mar) and 27 (3 Jun 1665) — <https://www.earlymoderntexts.com/assets/pdfs/spinoza1661.pdf> |
| C108 | By Letter 38 (March 1665), Spinoza curtailed the dialogue, citing irre… | [53] | UNSUPPORTED | The Blyenbergh correspondence ended with Ep. 27 on 3 June 1665. “Letter 38” is the old Elwes numbering for Ep. 27 (ref 53’s title: “LETTER XXXVIII (XXVII)”); the article’s March date is wrong. Ref 53 is a soft-404. | Ep. 27, 3 June 1665; old Letter 38 numbering confirmed — <https://www.earlymoderntexts.com/assets/pdfs/spinoza1661.pdf> |
| C110 | Spinoza countered in Letters 56–58 that such reports stem from confuse… | — | UNCITED | The Boxel exchange is Epp. 51–56 (Sep–Nov 1674), with Spinoza’s replies in 52, 54 and 56. Ep. 57 is from Tschirnhaus, and Ep. 58 is via Schuller. | Epp. 52, 54, 56 (Spinoza to Boxel); Tschirnhaus correspondence: direct Epp. 57, 59, 60, 65, 66, 80–83, and via Schuller Epp. 58, 63, 64, 70, 72 — <https://www.earlymoderntexts.com/assets/pdfs/spinoza1661.pdf> |
| C112 | Later letters with mathematicians like Ehrenfried Walther von Tschirnh… | — | UNCITED | The direct Tschirnhaus letters are Epp. 57, 59, 60, 65, 66 and 80–83; letters via Schuller are Epp. 58, 63, 64, 70 and 72. The article’s topics fit Epp. 59–60 and 63–66 better than Epp. 81–82, which concern deriving bodies from extension. | Tschirnhaus direct: Epp. 57, 59, 60, 65, 66, 80–83; via Schuller: Epp. 58, 63, 64, 70, 72. Epp. 81–82 concern deriving bodies from extension — <https://www.earlymoderntexts.com/assets/pdfs/spinoza1661.pdf> |
| C114 | In May 1670, Spinoza established permanent residence in The Hague, ren… | [11] | MISCITED | IEP says only 1670; "May 1670" is not in the source. Spinoza Web gives the move as between Sep 1669 and Feb 1671 | Moved to The Hague between late 1669 and early Feb 1671 — <https://spinozaweb.org/locations/9> |
| C118 | He succumbed to this pulmonary ailment on 21 February 1677, at age 44,… | [8][17] | UNSUPPORTED | The physician is contested. Colerus gives only “L.M.”; W. Meijer (1897) and Steenbakkers (1994) argue for Schuller, while other early evidence points to Meyer. Do not attribute a position to Nadler. | Contested: Colerus gives only “L.M.”; W. Meijer (1897) and Steenbakkers (1994) argue for Schuller; early evidence points to Meyer — <https://www.jewishencyclopedia.com/articles/13964-Spinoza-baruch-benedict-de-spinoza> |
| C120 | He was interred on 25 February 1677 in a rented vault within the Nieuw… | [49] | UNSUPPORTED | Spinoza was buried on 25 February 1677 in rented vault no. 162 in the Nieuwe Kerk, The Hague, a shared grave near de Witt’s grave no. 77. The vault was cleared in 1738; the present stone is a 1927 memorial. Grotius is buried in Delft. | Nieuwe Kerk shared grave: rented vault no. 162, 25 Feb 1677, near Johan de Witt’s grave no. 77; vault cleared 1738, present stone 1927; Grotius is in Delft — <https://www.spinozaweb.org/locations/156> |
| C123 | Spinoza argues deductively that only one such substance can exist, as … | [59] | MISCITED | E1D6 defines God, not substance in general. The argument uses E1P5 (no shared attributes), E1P8 (every substance necessarily infinite) and E1P14 (only one substance). “Absolutely infinite” appears in E1D6, but applies to God; the error is applying it to substance in general. | E1P5, E1P8 and E1P14; E1D6’s “absolutely infinite” applies to God, not substance in general — <https://www.gutenberg.org/ebooks/3800> |
| C158 | While thought and extension are indeed conceived through themselves (E… | — | UNCITED | E1D4, which defines attribute, is a fair supporting citation, and “conceived through itself” is E1P10. Only E1D5 is wrong: it defines mode. The claim is therefore half right. | Half right: E1D4 supports the attribute definition; “conceived through itself” is E1P10; E1D5 defines mode — <https://www.gutenberg.org/ebooks/3800> |
| C199 | For instance, sensory experience may present the sun as proximate—appr… | [77] | MISCITED | The sun “about two hundred feet” example is in E2P35S, and is repeated at E4P1S. E2P35S points back to E2P17S for the theory, but the example itself is not in E2P17S. | E2P35S (also E4P1S); E2P35S points back to E2P17S for the theory, not the example — <https://www.gutenberg.org/ebooks/3800> |
| C201 | These limitations impede adequate understanding and perpetuate bondage… | [77] | MISCITED | E2P3 concerns God's idea of his essence. The mind's passivity from inadequate ideas is E3P1 and E3P3 | E3P1, E3P3 — <https://www.gutenberg.org/ebooks/3800> |
| C206 | Appetite denotes conatus in relation to mind and body conjointly, whil… | [78][79] | MISCITED | DefAff 1 Explanation restates E3P9S, so the article’s citation is a near miss rather than a fabrication. The quoted sentence is located in E3P9S (Curley), not in the definition proper. | E3P9S; DefAff 1 Explanation restates E3P9S, so the locator is a near miss — <https://www.gutenberg.org/ebooks/3800> |
| C209 | Ethically, unaided conatus yields bondage to passive affects from exte… | [79] | MISCITED | “Acting according to the laws of one’s own nature” is in E4P24 Dem and the underlying E4D8; E4P18S also bears on the rational redirection of striving. E4P37 is about wanting for others the good one wants for oneself. | E4D8, E4P18S and E4P24 Dem; E4P37 concerns wanting for others the good one wants for oneself — <https://www.gutenberg.org/ebooks/3800> |
| C232 | The result is not escape from determinism—since all things follow nece… | [70] | SUPPORTED | Partly supported, misleading. E5P23 leaves “something which is eternal” remaining, and E5P40C identifies it as the intellect. What Spinoza rejects is eternity read as duration or memory (E5P23S, E5P34S, E5P21). “Beyond bodily death” is misleading, but “its intellectual capacities” is supported. | Partly supported, misleading: E5P23, E5P40C, E5P23S, E5P34S and E5P21; intellectual capacities are supported, “beyond bodily death” is misleading — <https://www.gutenberg.org/ebooks/3800> |
| C276 | Spinoza's explicit aim was to demonstrate that "freedom of judgement i… | [98] | MISCITED (vs intended: SUPPORTED) | Shift [98] -> 89. The sentence paraphrases the TTP title page and Preface, not chapter 20, and should not be presented as a verbatim quotation without naming a translation. The paraphrase also weakens Spinoza’s claim: freedom cannot be removed without destroying piety and peace. | TTP title page and Preface (Elwes): freedom may be granted without prejudice to peace, while without it piety cannot flourish nor public peace be secure — <https://www.gutenberg.org/ebooks/989> |
| C291 | Propositions build sequentially; for instance, Proposition 7 in Part I… | [74] | MISCITED | "The order and connection of ideas is the same as the order and connection of things" is E2P7, not Part I Prop 7. The cited ref 74 (Bennett Ethics) has it under Part II. The article itself gives E1P7 correctly in C183 | E2P7 — <https://www.gutenberg.org/ebooks/3800> |
| C313 | Freedom of thought persists under any stable regime, but political lib… | [101] | MISCITED (vs intended: MISCITED) | Shift [101] -> 92 (IEP political). The TP has only 11 chapters, so “TP 16:204” cannot exist; it probably means TTP ch. 16 plus a page number. TTP 16 tells subjects to obey even absurd commands. The limits on sovereign power are TP 3.9, 4.4 and 4.6, where general indignation is decisive. | TP 3.9, 4.4 and 4.6 (sovereign loses right when it provokes general indignation); TTP 16 for natural right — <https://constitution.org/2-Authors/bs/poltr-02.htm> |
| C324 | Published anonymously to aid instruction, this work demonstrates Spino… | [110] | MISCITED (vs intended: UNSUPPORTED) | Shift [110] -> 101 (Hackett PCP page). “Published anonymously” is wrong: the 1663 PCP carried Spinoza’s name and was the only work published under his name in his lifetime, with Meyer's preface (IEP, ref 11). | PCP published under Spinoza’s name in 1663, the only work published under his name in his lifetime — <https://iep.utm.edu/spinoza/> |
| C327 | Notable exchanges include 13 letters with Henry Oldenburg (1661–1665),… | — | UNCITED | “13 letters with Oldenburg” and “four with Blyenbergh” are wrong. The standard numbering has exactly 28 Oldenburg letters, 18 in 1661–65, and 8 Blyenbergh letters (Epp. 18–24, 27). | Oldenburg exactly 28 (18 in 1661–65); Blyenbergh 8 (Epp. 18–24, 27) — <https://www.earlymoderntexts.com/assets/pdfs/spinoza1661.pdf> |
| C328 | Letters to Gottfried Wilhelm Leibniz (late 1670s) touch on infinite at… | — | UNCITED | The surviving Leibniz–Spinoza letters are Epp. 45–46 (Oct–Nov 1671, optics), not late-1670s letters. “Around 1676” is not baseless for the broader contact: Leibniz sought the Ethics through Schuller in Nov 1675 (Epp. 70, 72) and visited in c. 18–21 Nov 1676. | Epp. 45–46 (Oct–Nov 1671, optics); Ethics sought through Schuller Nov 1675 (Epp. 70, 72); visit c. 18–21 Nov 1676 — <https://www.earlymoderntexts.com/assets/pdfs/spinoza1661.pdf> |
| C348 | In Ethics Part II, Propositions 48 and 49, he argues that the human mi… | [117] | MISCITED (vs intended: UNVERIFIABLE) | Shift [117] -> 108 (bot-blocked). E2P49C says will and understanding are one. E2P48S says will is the faculty of affirming, “not the desire”; E3P9S calls striving related to the mind alone “will”. The article both mislocates the line and runs will together with desire. | E2P48S, E2P49C and E3P9S: will is affirmation/intellect, while desire is treated in E3P9S — <https://www.gutenberg.org/ebooks/3800> |
| C360 | Hume argued that Spinoza's assertion of necessary causal chains within… | [126] | MISCITED (vs intended: MISCITED) | Shift [126] -> 117 (Garrett interview), which does not say this. Hume's explicit discussion of Spinoza (Treatise 1.4.5) is about the simplicity and immateriality of substance and the soul, not about over-extending causal necessity | Hume, Treatise 1.4.5 — <https://www.gutenberg.org/ebooks/4705> |
| C364 | This monistic framework influenced Gottfried Wilhelm Leibniz, who visi… | [129][38] | MISCITED (vs intended: MISCITED) | Shift [129] -> 120 (no Leibniz content). Ref 38 is bot-walled. The visit should be written c. 18–21 Nov 1676: Academy edition A VI 3, 578 prints the date with a “(?)”. | Leibniz in The Hague c. 18–21 Nov 1676 (Academy Edition A VI 3, 578, with “(?)” ) — <https://www.leibniz-translations.com/perfectbeing> |
| C368 | Despite bans—such as the 1678 papal condemnation—Spinozism fueled unde… | [132][133][134] | MISCITED (vs intended: UNSUPPORTED) | Shift [132–134] -> 123–125. Diderot/Encyclopédie is supported, but none mentions a “1678 papal condemnation”. The Dutch civil ban is dated 25 June 1678: Wiltens names the States of Holland and West Friesland, while Spinoza Web credits the Supreme Court. The Court of Holland had already banned the TTP on 19 July 1674. | Dutch civil ban, 25 June 1678: Wiltens says States of Holland and West Friesland; Spinoza Web credits the Supreme Court. Court of Holland banned the TTP 19 July 1674 — <https://spinozaweb.org/works/date/asc> |
| C383 | Albert Einstein, in a 1929 interview, affirmed his belief in "Spinoza'… | [143][144] | MISCITED (vs intended: SUPPORTED) | Shift [143][144] -> 134/135. The intended source quotes Einstein's reply to Rabbi Goldstein. It was a 1929 cable reply, not an "interview"; the wording is a translation variant | April 1929 cable to Rabbi Herbert S. Goldstein: "I believe in Spinoza's God, who reveals himself in the harmony of all that exists…" — <https://philosophybreak.com/articles/pantheism-spinoza-and-the-god-that-einstein-believed-in/> |
| C398 | Additionally, while the cherem of 1656 was never formally rescinded, i… | — | UNCITED | Ref 126: in 2012 the community was asked to lift the ban and declined; ref 148 describes a 2015 review. "Concluded they lacked the authority" was not found in either | 2012 request declined; 2015 symposium/review — <https://www.sourcesjournal.org/articles/lifting-the-ban-spinoza-and-the-boundaries-of-belonging> |
## 4. Spinoza citations

**Standard and method.** Ethics references were checked against Elwes (Project Gutenberg #3800); Curley was consulted only through SEP entries and published papers. Ethics citations below use Part/Proposition/Definition/Scholium locators only, with no page numbers. TTP and TP were checked against Elwes; TIE against Elwes (PG #1016). Letters were checked by Gebhardt numbering against Spinoza Web and Bennett. The sacred-texts Elwes edition uses a different numbering, shown in brackets in its titles.

**The two items the other bot spotted:**
1. *[153]–[161] dangling.* **Confirmed** by the script: 9 numbers, 9 markers, 7 sentences. The cause is larger than missing entries. The source list was evidently renumbered, so citations from about [90] onward are off by nine (§3). The "missing" sources are actually refs 144–152.
2. *"The order and connection of ideas is the same as the order and connection of things" labelled Part I Prop 7.* **Confirmed wrong; it is E2P7.** The wording is confirmed in Elwes and through the permitted Curley sources. The cited source (ref 74, Bennett's Ethics) has it in Part II. The article contradicts itself: C183 gives E1P7 correctly ("it pertains to the nature of a substance to exist"). C155 also cites "Ethics 2p7" correctly for parallelism.

**Ethics locators: wrong**

| claim | article says | correct |
|---|---|---|
| C291 | "Proposition 7 in Part I": order and connection of ideas | **E2P7** |
| C123 | "Part I, Definition 6": substance "absolutely infinite"; one substance because shared attributes would limit each other | D6 defines *God*. The argument uses **E1P5**, **E1P8** and **E1P14**; “absolutely infinite” in E1D6 applies to God, not substance in general |
| C158 | attributes conceived through themselves "(Ethics 1d4, 1d5)" | 1D5 defines *mode*. Use **E1P10** (with E1D4) |
| C199 | sun "200 feet" away "(IIp17, note)" | **E2P35S** (repeated at E4P1S). Elwes: "about two hundred feet" |
| C201 | imaginative ideas make the mind passive "(IIp3)" | E2P3 is God's idea of his own essence. Use **E3P1**, **E3P3** |
| C206 | "Desire … appetite together with consciousness of the appetite" given as Definition of the Affects I | The quoted sentence is **E3P9S**; the DefAff 1 Explanation restates E3P9S, so this is a near miss. DefAff I is "Desire is man's very essence…" |
| C209 | virtue = "acting according to the laws of one's own nature" "(E4P37)" | **E4D8**, **E4P18S** and **E4P24** Dem. (Elwes: "to act according to the laws of one's own nature"). E4P37 is about wanting the good for others |
| C348 | E2P48–49 "will is merely an appetite" | The locator E2P48–49 is fine, but **E2P49C** says will and intellect are one and the same; **E2P48S** calls will the faculty of affirming, “not the desire”, and **E3P9S** calls mind-only striving “will”. “Appetite” belongs to E3P9S |
| C232 | mind will "persist immortally beyond bodily death" | **Partly supported, misleading**: E5P23 leaves “something which is eternal” remaining, E5P40C identifies it as the intellect; E5P23S, E5P34S and E5P21 reject eternity read as duration or memory |
| C173 / C177 / C165 | "2+2=4", "4's essence from unity", horse example as Spinoza's illustrations of intuition/reason | Not Spinoza's. His example is the fourth proportional (1:2 = 3:x) at **E2P40S2**. None of these are in the cited IEP article (ref 70). *(Non-priority sentences found while checking neighbours; logged as NOT_CHECKED, so they are not in the counts.)* |

**Ethics locators and quotes: correct**

- E1D3 (C121, Elwes verbatim); E1D5 (C140); E1D6 (C126, C138); E1P7 (C183); E1P14 (C124 — locator correct, but the quote mixes Elwes "Besides God…" with Curley "Except God…");
- E1P16 (C143); E1P29 (C134); E1 Appendix "all final causes are nothing but human fictions" (C133, Curley);
- E2P2 (C144); E2P7 (C155); E2P17 (C193, Elwes verbatim); E2P18 (C200); E2P25 (C195); E2P28 (C196);
- E2P40S2 three kinds of knowledge and "opinion or imagination" (C160, C191); E2P41 (C198: Curley "only cause of falsity", Elwes "only source");
- E3P6 (C203, Curley); E3P7 (C205); E3P11S (C208); E3P58–59 (C208); the 48 definitions of the affects (C223); "waves of the sea driven by contrary winds" = E3P59S;
- E4P22C "first and only foundation of virtue" (C210).

Part titles (C293–C297) mix Elwes and Curley wording. They are not wrong, but they should follow one translation.

**Possibly fabricated paraphrase in quotation marks**

- **C276**, TTP: "freedom of judgement is in itself most useful for piety and the peace of the State". This paraphrases the TTP title page and Preface, not chapter 20, and should not be presented as a verbatim quotation without naming a translation. It also weakens Spinoza's claim: freedom cannot be removed without destroying piety and peace. Elwes: "not only can such freedom be granted without prejudice to the public peace, but also, that without such freedom, piety cannot flourish nor the public peace be secure."
- **C333**: "open project" (Hebrew grammar) is in quotation marks with no source.
- **C367**: Voltaire 1772, "famous book so little read". Not found in the sources or by web search. **UNVERIFIABLE**; treat as unsourced until a Voltaire text is cited.
- **C383**, Einstein: the quote is genuine in substance. It was a 1929 *cable reply* to Rabbi Herbert S. Goldstein, not an "interview", and the wording is one of several translations.

**TTP / TP**

- **C313 "(TP 16:204)"**: no such locator exists, because the TP has 11 chapters (the last unfinished). It is probably TTP ch. 16 plus a page number. TTP 16 actually says subjects must obey even absurd commands, so the claim of "permitting resistance" is better supported, in a hedged form, by **TP 3.9, 4.4 and 4.6** (a sovereign that provokes general indignation loses right).
- Correct: TP 6.15ff on royal councils (C309); TP 8–9 on centralized and federal aristocracy (C310); TP 8.46, patricians of "that most simple and general religion" (C312); TP 11.3, exclusion of women and servants (C311); TTP ch. 1 definition of prophecy (C234); ch. 3 (C239); ch. 7 method (C242, C244); ch. 14 justice and charity (C252).

**Letters** (standard numbering). This is the weakest section of the article. Almost all of these sentences are uncited, and several are wrong:

| claim | article | correct |
|---|---|---|
| C102 | Huygens's nitre experiments → "Letter 73 (June 1666)" | Nitre was **Boyle's** (Ep. 6, 1662; also Epp. 11, 13). **Ep. 73** to Oldenburg is late 1675; it does contain "God is the immanent cause of all things" |
| C104, C105, C328 | Leibniz letters c. 1676 / "late 1670s"; "Letter 69" on infinite intellect | Leibniz–Spinoza letters are **Epp. 45–46 (Oct–Nov 1671), on optics**. Leibniz sought the Ethics through Schuller in Nov 1675 (**Epp. 70 and 72**), and the 1676 visit should be dated **c. 18–21 Nov 1676** (Academy edition A VI 3, 578 prints “(?)”). **Ep. 69** is to Lambert van Velthuysen, from Sep–Nov 1675; the 1671 Velthuysen items are Epp. 42–43 |
| C106–C108 | Blyenbergh questioned the Short Treatise; Spinoza replied in "Letters 27–29"; "Letter 38 (March 1665)" ended it | Blyenbergh's questions were on the **PCP / Cogitata Metaphysica** (Ep. 18, 12 Dec 1664). Replies were **Ep. 19 (5 Jan 1665), Ep. 21 (28 Jan), Ep. 23 (13 Mar) and Ep. 27 (3 Jun)**. “38” is the old Elwes number of Ep. 27 (ref 53's title: "LETTER XXXVIII (XXVII)") |
| C110 | Boxel replies "Letters 56–58" | Boxel exchange is **Epp. 51–56** (Sep–Nov 1674); Spinoza's replies are 52, 54, 56. Tschirnhaus's direct letters are **57, 59, 60, 65, 66 and 80–83**, and the letters via Schuller are **58, 63, 64, 70 and 72** |
| C112 | Tschirnhaus "Letters 81–82" on method and proofs of God | The article's topics fit **Epp. 59–60 and 63–66** better than 81–82; **Epp. 80–83 (May–Jul 1676)** concern deducing the variety of bodies from extension |
| C076 vs C327 | 34 Oldenburg letters (C076) and 13 (C327); "four" Blyenbergh letters | The article contradicts itself. The standard numbering has exactly **28** Oldenburg letters (**18 in 1661–65**) and **8** Blyenbergh letters |
| C101 | Ep. 32 "rejecting mechanistic alternatives like Descartes" | Ep. 32 (20 Nov 1665) is the worm-in-the-blood passage. Spinoza disputes Descartes' *rules of motion*; he does not reject mechanism |
| C097, C325 | 88 letters | **Correct** (EMLO: "just eighty-eight letters"). The 50/38 split was not verified |
| C094 | Heidelberg chair declined, 1673 | **Correct**: Epp. 47–48 |

## 5. Fallacy and framing pass (substance lens v0.5.9, `fallacyScanPass`)

**Honesty rules.**
- Every flag below is a **judgment** by the auditor. None was computed; no argument graph was built, and there are no scores.
- One mechanical sub-check was run, for F053: a term count over `claims.csv`. That count is reported as such.
- A flag *withdraws warrant* from the flagged sentence. It does **not** show the sentence is false.
- Per the dual-case rule, each issue was scanned from the article's side (Side A: does the article's own framing tilt?) and from a critic's counter-reading (Side B: would a reader of the opposite persuasion find the opposite bias?).
- Effort was equal on both sides, but evidence was not: several of the theist-reading sources (refs 103, 107, 112) and atheist-reading sources (105, 115, 116) were bot-blocked or unreadable.

### Side A: flags on the article as written

| # | id / name (check_type) | flagged span | why | repair or refusal |
|---|---|---|---|---|
| A1 | F040 Loaded Language + F050 Reification (judgment); F053 Repetition (partial: count run by code) | "causal realism" in **5 sentences** (C096, C342, C346, C381, C393). C342: "…which **causal realism suggests** renders divine personality causally inert and thus nonexistent in orthodox terms". C381: "the causal incompatibility between his causal realism… and doctrines of grace" | Spinoza never uses the term, and it is not standard in the cited Spinoza literature. It is treated as an authority that "suggests" conclusions, and repetition makes it seem established | Refuse as warrant. Replace with Spinoza's own terms (necessitarianism, E1P29 and E1P33; immanent causation, E1P18), and attribute the "personality is inert" conclusion to named interpreters |
| A2 | F057 Historian's Fallacy (judgment) | C036: van den Enden studies "intensified… a deterministic, substance-monist worldview, marking the onset of views later deemed heretical" | Projects the mature system of the 1660s–70s back onto 1654–56. C045 itself admits no document details the heresies | Restrict to what was documented then. The 1659 Inquisition informants' reports (Spinoza and Prado said the Law was not true, souls die with the body, and God exists only "philosophically") are the standard evidence in Nadler's biography. Mark the rest as hindsight |
| A3 | F013 False Dilemma (judgment); unsupported inference | C046: "indicating deeply entrenched heterodoxy **rather than mere youthful rebellion**". C047: "underscores Spinoza's perceived threat as an intellectually formidable figure" | Two framings are offered as exhaustive, and the cited NEH source supports neither the Morteira episode nor the inference | Present the motives as contested (NEH and Kasher/Biderman list several hypotheses) and drop the dichotomy |
| A4 | F004 Appeal to Authority (partial: citation-presence check) | C129: "**Scholars compare** natura naturans… to the Daoist concept of ziran" (uncited). The neighbouring support, C130 ref 61, is an undergraduate "comparative philosophy sample" essay on a business-services site | Anonymous scholarly consensus, backed by a non-scholarly source | Refuse. Name a comparative-philosophy publication, or cut |
| A5 | F058 Presentism (judgment) | C389 "underpin **modern liberal republicanism**"; C401 "**blueprints for secular governance**, relevant to contemporary struggles against illiberalism"; C386 "anticipated cognitive therapies"; C341 "effectively **secularizing** ontology" | Present-day categories are attributed to the texts rather than to their modern interpreters | Separate the historical claim (what TTP 20 / TP argue) from the reception claim ("X reads Spinoza as…"), each with its own source |
| A6 | F011 Hasty Generalization / F019 Composition (judgment) | C375 (uncited): "**Orthodox Judaism continues to regard him** as a heretic…" | Generalizes from one Amsterdam congregation's 2012 and 2021 positions (refs 126 and 150) to all of Orthodox Judaism | Narrow it to the Portuguese-Israelite community of Amsterdam, with dates and refs |
| A7 | F036 Suppressed Evidence (judgment) | C380–C381: "mainstream theology… equating it to atheism"; influence "**confined to liberal or deistic fringes** rather than confessional cores" | Leaves out well-known contrary reception: Schleiermacher's "holy and rejected Spinoza" (*Reden*, 1799); Novalis's "God-intoxicated man" (quoted in the article's own ref 106); Herder's *Gott* (1787); Goethe; Lessing (whom the article itself mentions in C339) | Do an evidence census and add the Romantic and idealist theological reception |
| A8 | F079 Shotgun Argumentation (judgment) | C327–C328: a rapid list of letter counts, dates and topics with no citations | Many specifics quickly, several wrong (see §4), so the claims are hard to check | Cite each exchange to EMLO or Bennett letter numbers |
| A9 | F040 Loaded Language (judgment) | C331: "Hebrew, **the language from which he was expelled** in 1656" | He was expelled from a congregation, not a language; the phrase adds pathos and is literally false | Rephrase: "the language of the community that expelled him" |
| A10 | F004 / F005 (judgment) | C365, C367: Israel's "Radical Enlightenment" causal story (Spinoza → Bayle → Revolution) stated as fact, uncited | A contested historiographical thesis presented as consensus | Attribute it to Israel and note its critics |

### Side B: the critic's counter-reading, checking for the opposite bias

| # | id / name (check_type) | flagged span | why a critic would flag it | repair or refusal |
|---|---|---|---|---|
| B1 | F040 Loaded Language / F004 (judgment) | C005: "accusations of atheism, **despite Spinoza's explicit identification of God with substance**"; C376: "interpreted… by Bayle as atheistic **despite** his explicit identification of God or Nature…" | A reader of Bayle, Jacobi, or modern "atheist-in-effect" interpretations would say "despite" quietly ruled the atheism reading a misreading and takes Spinoza's vocabulary as decisive. This is the *pro-theist* tilt, the opposite of A1 | Neutral form: "accused of atheism; defenders point to his identification of God with substance" |
| B2 | F002 Straw Man (partial: quote/paraphrase check) | C340: the theist reading described as "a rigorous theism stripped of superstition, **akin to non-theistic monotheism**" | "Non-theistic monotheism" is self-undermining and caricatures the pantheist and theist side. The cited sources are shifted (102/103), and neither uses the phrase | Restore the actual positions with named proponents (e.g., panentheist and pantheist readings in the SEP literature) |
| B3 | F041 False Equivalence / F048 Middle Ground (judgment) | C335–C343, C394: "This tension persists…", "without resolving the atheism charge" | Run both ways: the section gives each reading a paragraph, which is fair. But it ends each round on the atheist side ("effectively", "rhetorical concessions", "nonexistent in orthodox terms"), so balance is formal rather than substantive. A theist critic would see an atheist tilt; an atheist critic would see "remain divided" as false balance over a settled point about the denial of a personal God | Keep both readings, attribute each to sources, and say what *is* agreed: no personal, providential, miracle-working God (E1 App) |
| B4 | Anachronism check: label "modern secular atheist" (judgment) | Searched all 401 sentences | **Not found unqualified.** The article never calls Spinoza an atheist in its own voice; the atheist reading is always attributed ("Others contend", C341). The nearest anachronisms are the "secular" labels in A5 | No repair needed for the label itself; A5 covers the rest |
| B5 | F058 Presentism (reverse) (judgment) | C313 "permitting resistance"; C389 "liberal republicanism" | A critic who reads Spinoza as close to Hobbes (TTP 16: obey even absurd commands; TTP 19: sovereign controls public religion) would say the article over-liberalizes him. Partial balance: C311 does note TP 11.3's exclusion of women and servants | Add TTP 16 and 19 on sovereign authority over religion, alongside TTP 20 |
| B6 | F040 Loaded Language (judgment) | C047 "the community's survival strategy of **pious conformity**"; C372 "the community's **fear**…" | Against the community: a reader sympathetic to the Talmud Torah congregation's position (cf. Serfaty, ref 150) would flag these as pejorative. A Spinoza partisan would equally flag C046's "entrenched heterodoxy" (A3) as pathologizing Spinoza. Both directions were found | Describe the motives in the sources' terms: Kaplan's 40 bans, 1622–1683, and the converso context in NEH and ref 16 |

**Net judgment, not a score.** The framing problems are mostly *local*: an unexplained house term (A1), several presentist labels (A5), and a few unsupported inferences about the cherem (A2, A3). There is no systematic one-sided bias on the pantheism/atheism question. Side A and Side B flags roughly offset there (B1 against A1/B3). The larger reliability problem for a reader is the citation layer (§3), not the slant.

## 6. Methods and limits

- **Inputs.** The page saved as Markdown and HTML (in this repo: `topics/spinoza/articles/baruch-spinoza/snapshots/2026-10-01.md` and `.html`). The live page re-fetched on 1 Oct 2026 (PT) was the same size and had the same source count.
- **Parsing.** `grokaudit.py parse` splits `<span data-tts-block>` paragraphs into sentences and keeps inline citation numbers. Sources come from `<li id="ref-N">`.
- **Link checks.** `linkcheck` uses HEAD with a GET fallback, at least 2 s between hits on the same host. `fetch` caches source text; `soft404` flags 200-status error pages and bot walls. Everything was read-only: nothing was edited, posted or submitted, and no one was contacted.
- **Numbering shift.** Detected with `offset`: full-text word overlap of each claim against source n and n ± k. The −9 shift is statistically clear for [90]–[152]. **[81]–[89] are ambiguous** (11 markers), so I judged them as linked and noted the ambiguity. The likely mechanism (9 duplicate entries dropped from the displayed list without renumbering the text) is an inference; I did not see Grokipedia's build process.
- **Verdict rules.** Verdicts are judgments recorded in `data/verdicts_spinoza.psv` and merged by `grokaudit.py buildlog`. The `verdict` column scores the citation *as linked*. `verdict_vs_intended` re-scores shifted citations against source n − 9. For shifted cites, MISCITED reflects the established shift even where the linked page was itself unreadable.
- **Depth.** `check_depth` records how each verdict was reached: read / skim / primary / title / none / script. "Skim" means keyword search plus reading the best-matching passage in the cached source, not a full read. A skim-level SUPPORTED is weaker than a read-level one.
- **Not reachable.**
  - Paywalled or abstract-only: WSJ (34), OUP chapters and TOCs (32, 36, 40), Cambridge Lexicon entries. These were marked UNVERIFIABLE where they were the only support.
  - Bot-blocked: PhilArchive, ResearchGate, umich (14 refs), plus ref 138 (HTTP 500) and ref 68 (redirect loop). I did not try to get around these blocks.
  - Unreachable: ref 9 (SSL failure). This leaves the genealogy claims C012–C015 unverifiable.
- **Sampling.** The priority set (223 claims) was chosen by regex tags plus manual review. Non-priority cited claims were sampled at 40 of 144 (seed 1656), leaving **104 cited claims NOT_CHECKED**. The non-sampled claims C165/C173/C177, noted in §4, show that errors exist outside the sample. The sample error rate should not be extrapolated as a precise figure.
- **Primary texts.**
  - Elwes: Gutenberg Ethics, TTP, TP and TIE.
  - Curley: consulted only through SEP entries and published papers.
  - Bennett's Early Modern Texts versions: these are the article's own refs 50, 74 and 89.
- **Biographical facts.** Where the article follows the 1906 Jewish Encyclopedia (genealogy) and that has been superseded, I marked it "SUPPORTED by citation, factual issue Y" and gave the modern source (Spinoza Web). Contested points, such as Schuller vs Meyer at the deathbed and the TIE's date, are marked as contested rather than wrong.
- **No invented material.** Where I could not confirm a quote or fact, it is marked UNVERIFIABLE or "not verified". All corrections link to a public source or name the primary-text locator.
- **Re-running on another page.**

  ```
  python3 tools/grokaudit/grokaudit.py parse page.html -o out/
  python3 tools/grokaudit/grokaudit.py linkcheck out/sources.csv -o out/linkcheck.csv
  python3 tools/grokaudit/grokaudit.py fetch out/sources.csv --cache out/cache
  python3 tools/grokaudit/grokaudit.py soft404 --cache out/cache
  python3 tools/grokaudit/grokaudit.py offset out/claims.csv --cache out/cache
  python3 tools/grokaudit/grokaudit.py priority out/claims.csv -o out/worksheet.csv
  python3 tools/grokaudit/grokaudit.py evidence out/worksheet.csv --cache out/cache --only-priority
  ```

  Then write the verdicts file by hand and run:

  ```
  python3 tools/grokaudit/grokaudit.py buildlog out/worksheet.csv verdicts.psv out/sources.csv -o audit_log.csv
  python3 tools/grokaudit/grokaudit.py report audit_log.csv
  ```

## Peer cross-check (freedom_of_necessity, 2026-10-01)

**Confirmed.** The peer cross-check used Elwes for the Ethics, TTP and TP; Spinoza Web with Gebhardt numbering and Bennett for the letters; and Curley only through SEP entries and published papers. It confirmed the citation-shift diagnosis, E2P7, the Ethics locator corrections, the Oldenburg total of exactly 28 letters (18 in 1661–65), the PCP as the only lifetime publication under Spinoza’s name, and the TP’s 11-chapter limit.

**Changed.** The verdict file and merged log now correct Blyenbergh’s Ep. 27 date (3 June 1665), Ep. 69’s Sep–Nov 1675 date, the Tschirnhaus direct/via-Schuller lists and topic placement, and the Leibniz chronology (Epp. 45–46; Epp. 70 and 72; visit c. 18–21 Nov 1676). C232 is now **SUPPORTED** in the schema’s closest category, with a note that it is partly supported but misleading; C276’s intended-source assessment is now supported as a paraphrase of the TTP title page and Preface. The notes now distinguish E1D4/E1P10, E4P18S/E4P24/E4D8, E2P35S/E4P1S, E3P9S, E2P48S/E2P49C/E3P9S, and the E1P5/E1P8/E1P14 argument.

The audit also now records the contested deathbed physician attribution without attributing a view to Nadler; the shared burial vault and de Witt memorial details; the careful alternatives for the 1678 Dutch civil ban and the 1674 Court of Holland ban; TP 4.6 alongside TP 3.9 and 4.4; the replacement TP URL; and the removal of “or immortality” and any page-number references.
