# Kvalitetsrapport 2 — TU Delft / AC-ICT

> **AI-skrevet rapport.** Denne rapport er skrevet af en AI-assistent som led i en ekstern evaluering den 9. september 2026. Den kan indeholde fejl, også fejl der ser overbevisende ud. Hovedtallene er efterregnet fra de kodede data den 13. november 2026; [README.md](../README.md) siger, hvad der er kontrolleret, og hvad der ikke er.
>
> **AI-written report.** Written by an AI assistant in an external evaluation on 9 September 2026. It may contain errors, including plausible-looking ones. The headline figures were recomputed from the coded data on 13 November 2026; see [README.md](../README.md) for what was and was not checked.

**Resultat: 63,1/100 i F1-overensstemmelse med den publicerede analyse.** Det er et mål for lighed med et andet AI-analyseforløb, ikke en verificeret procent for korrekthed. Skillen leverer kildefast evidens, men er mere tilbøjelig end referencen til at betragte anbefalinger som governance-relevante.

## Opgave og afgrænsning

Hele datapakken blev downloadet: 155 PDF-rapporter fra AC-ICT, udtrukne anbefalingsafsnit og filer fra det oprindelige analyseforløb. Den blinde kodning brugte **hele det medfølgende testrun_8: seks rapporter, 184 anbefalingsuddrag**. Dette er en fokuseret kodningstest, ikke en ny gennemførelse af alle fem oprindelige analysetrin på 155 rapporter.

Testspørgsmålet var: Hvilke anbefalinger vedrører governance, og hvordan kodes deres projektfase, myndighedskrav, primære governance-funktion og interesseorientering? Fem centrale felter blev testet: GOV_RELEVANT, PHASE, AUTH_REQ, GC_PRIMARY og INTEREST_ORIENTATION. Øvrige felter, eksempelvis aktør og domæne, indgår ikke i kvalitetsmålingen.

En separat blind koder modtog de 184 nederlandske tekstuddrag i rapportorden, kodebog_v21 og reglerne for governance-relevans. Tidligere kodninger og evalueringer var skjult. Piloten omfattede 50 enheder fra tre rapporter; kodebogen forblev fast. En anden blind koder gentog D02’s 26 enheder.

## Resultater

| Mål | Resultat | Grundlag |
|---|---:|---|
| F1-overensstemmelse ×100 | **63,1** | Sammenligning af felt/værdi-tildelinger på 184 enheder |
| Præcision mod referencen |58,6 %|Andel af AI-tildelinger, som findes i referencen|
| Recall mod referencen |68,3 %|Andel af referencens tildelinger, som genfindes|
| Alle fem felter identiske |40,2 %|74 af 184 enheder; omfatter også ikke-relevante enheder|
| Dækning af testsættet |**100 %**|184 af 184 enheder|
| Ordret evidens i inputuddrag |**100 %**|481 ikke-tomme evidenscitater|

Der var 396 fælles, 280 AI-ekstra og 184 reference-ekstra felt/værdi-tildelinger. Felter efter GOV_RELEVANT er tomme, når koderen vælger N. Ekstra eller manglende positive governance-vurderinger påvirker derfor også det samlede F1-mål.

| Felt | Enighed | Sammenlignede rækker |
|---|---:|---:|
| Governance-relevans: MECH/RESP/N |66,8 %|123/184|
| Projektfase |64,6 %|64/99|
| Myndighedskrav |67,7 %|67/99|
| Primær governance-kategori |67,7 %|67/99|
| Interesseorientering |75,8 %|75/99|

De fire sidste felter er målt på de 99 enheder, som referencen betegner som governance-relevante. Et tomt AI-felt tæller som uenighed. Ikke-relevante enheders tomme felter bruges således ikke til at oppuste disse procenter.

## Hvor opstår forskellene?

**Afgrænsningen af governance er den centrale udfordring.** Blandt referencens 85 N-enheder klassificerede skillen 34 som relevante: 23 RESP og 11 MECH. Omvendt blev 10 af referencens 99 relevante enheder kodet N. Hertil kommer forskelle mellem ansvar (RESP) og institutionaliseret mekanisme (MECH). Dette er forskelle mod referencen; de er ikke automatisk bevist fejlagtige fortolkninger.

Den blinde koder fremhævede især grænserne mellem teknisk test og institutionaliseret kvalitetssikring på tværs af organisationer samt mellem almindelig projektleverance og governance-aftaler. Det er netop grænser, som den detaljerede kodebog forsøger at fastlægge, men som stadig giver forskellige resultater.

**Den separate gentagelse var mere ensartet:** F1-overensstemmelse 87,5 og helt identiske felter i 61,5 % af D02’s 26 enheder. Gennemsnitlig kappa på felt/værdi-indikatorer var 0,691; interval 0–1 for definerede værdier. Det måler AI-konsistens, ikke menneskelig interkoderreliabilitet. Gentagelsen er en uafhængig kørsel, ikke en tidsmæssig driftmåling. Førstekørslen er bevaret uden efterfølgende tilpasning til referenceværdierne.

## Kilde- og datakontrol

Alle 155 PDF’er kunne åbnes. Der blev registreret 1.100 sider, hvoraf 14 ikke gav tekst ved udtræk. “Kunne åbnes” dokumenterer derfor ikke komplet tekstudtræk.

159/184 testuddrag (**86,4 %**) kunne genfindes automatisk i PDF-teksten efter normalisering af whitespace, orddeling og store/små bogstaver. Når indledende Markdown-listepunkter også fjernes, stiger tallet til 167/184 (**90,8 %**). De 17 resterende uddrag er ikke automatisk verificeret mod PDF-kilden. De må ikke kaldes opdigtede alene på dette grundlag; OCR, typografi og mellemproduktets tekstbehandling kan være årsager.

Skillens evidenscitater er kontrolleret mod de leverede 184 inputuddrag. Denne 100 %-kontrol må ikke forveksles med 90,8 %-kontrollen mod de oprindelige PDF’er. **Validatorstatus: `RESULT: PASS`** for de 676 kodetildelinger i den endelige tabel. Validatorens kildetabeller består af disse inputuddrag; original-PDF-kontrollen ligger separat i pdf_audit.json.

## Begrænsninger og vurdering

Referencefilerne indeholder resultater fra det oprindelige AI-forløb med forskernes evalueringsnoter. Pakken leverer ikke komplette uafhængige menneskelige kodninger, som kan bruges som et entydigt facit. Evalueringsnoten angiver 85 relevante enheder, mens det leverede testrun_8 indeholder 99; testens beregninger anvender de faktiske rækker. Forfatternes publicerede fejlprocent overtages ikke.

**Skillen er anvendelig til efterprøvelig kodning, men kan ikke betragtes som automatisk reproduktion af denne specialiserede governance-analyse.** Den vigtigste forbedring er skarpere pilotafprøvning af N/RESP/MECH-grænser med tydelige positive og negative eksempler. Nye regler bør testes på nye rapporter, så denne test ikke bruges til at optimere mod kendte svar.

Der findes ingen kontrolkørsel uden skillen. Resultatet gælder denne AI+skill-kørsel på det erklærede testsæt og de fem felter, ikke hele 155-rapporters analyse eller alle skillens funktioner.

## Dokumentation og kilde

Se audit_workbook.xlsx for kodninger og sammenligninger, validation.txt for validatorstatus samt SOURCE.md for licens, ændringer og kreditering. De metodiske litteraturhenvisninger i skillen er ikke genverificeret i denne benchmark.

Instrument: Content Analysis Skill by Peter Malmkjaer, 5.0.0-beta.3. [Originaldata — TU Delft / 4TU.ResearchData](https://doi.org/10.4121/ea45e84e-d128-4950-9d7a-0338fd7e064e.v1), hentet 9. september 2026.
