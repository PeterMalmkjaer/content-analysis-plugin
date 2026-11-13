# Kvalitetsrapport 1 — TU Delft-interviews

> **AI-skrevet rapport.** Denne rapport er skrevet af en AI-assistent som led i en ekstern evaluering den 9. september 2026. Den kan indeholde fejl, også fejl der ser overbevisende ud. Hovedtallene er efterregnet fra de kodede data den 13. november 2026; [README.md](../README.md) siger, hvad der er kontrolleret, og hvad der ikke er.
>
> **AI-written report.** Written by an AI assistant in an external evaluation on 9 September 2026. It may contain errors, including plausible-looking ones. The headline figures were recomputed from the coded data on 13 November 2026; see [README.md](../README.md) for what was and was not checked.

**Resultat: 60,1/100 i kodningsscore (micro-F1).** Content Analysis beta.3 leverede fuld dækning og kildefaste citater, men reproducerede kun delvist de publicerede forskerkodninger. Testen støtter brug som et efterprøvbart analyseudkast med faglig gennemgang; den dokumenterer ikke, at kodningen kan erstatte forskernes vurderinger.

## Hvad blev testet?

Alle syv tilgængelige interviews om institutionelle og infrastrukturelle vilkår for deling og genbrug af forskningsdata: fire interviews med policy-/supportpersoner og tre med forskere. Materialet blev opdelt i 262 spørgsmål/svar-enheder. Den oprindelige kodebog med 54 koder blev anvendt deduktivt og holdt fast. Indledende metadata blev bevaret som kontekst; kildens anonymisering og markerede udeladelser blev ikke udfyldt.

Testspørgsmålet var: Hvor godt kan en blind AI-kørsel med skillen anvende denne kodebog i forhold til de publicerede kodninger, og er output dækkende og efterprøvbart? Den konkrete indholdsanalyse spurgte til arrangementer, erfaringer, motivationer og støtte til datadeling/-genbrug.

En separat kodeagent modtog rå tekst og kodebog uden forskernes kodninger eller kodefrekvenser. Piloten omfattede 50 enheder fra tre interviews. Hele materialet blev derefter kodet i batches. En anden, blind agent genkodede interview I1. Referencekodninger blev kun behandlet af evaluator. Resultaterne måler denne AI+skill-kørsel; der er ikke udført en kontrol uden skillen.

## Målt kvalitet

| Mål | Resultat | Betydning |
|---|---:|---|
| Kodningsscore, micro-F1 × 100 | **60,1** | Samlet balance mellem manglende og ekstra koder |
| Præcision | 64,6 % | Andel af AI’ens kodetildelinger, som også findes i den tilpassede reference |
| Recall | 56,1 % | Andel af referencekodningerne, AI’en genfinder |
| Macro-F1 × 100 | 57,9 | Hver kode vægter lige meget |
| Helt samme kodesæt pr. tekstenhed | 26,3 % | Enheder hvor alle koder stemmer, også eventuelt tomt kodesæt |
| Dækning | **100 %** | 262 af 262 enheder behandlet |
| Ordrette evidenscitater | **100 %** | Samtlige evidenscitater genfundet i den tilhørende tekstenhed |

Der var 306 fælles, 168 AI-ekstra og 239 reference-ekstra kodetildelinger efter konvertering til fælles enheder. “Ekstra” betyder uenighed med referencen, ikke automatisk en forkert fortolkning. Gennemsnitlig kappa pr. kode var 0,565; interval −0,006 til 1,000.

| Interview | Micro-F1 × 100 |
|---|---:|
| I1 | 61,7 |
| I2 | 63,8 |
| I3 | 56,4 |
| I4 | 45,7 |
| I5 | 62,7 |
| I6 | 63,9 |
| I7 | 59,2 |

## Hvad fungerer, og hvad fejler?

**Validatorresultat: `RESULT: PASS`.** De endelige data indeholder 474 kodetildelinger og 26 `UNCODED`-rækker. En dobbelt registrering af samme kode på samme enhed blev fjernet ved den blinde koders strukturkontrol; dette ændrede ingen enheders kodesæt eller sammenligningsscore. Alle 500 tabelrækker bestod citatkontrollen. Validatoren håndterede desuden seks små kontrolscenarier som forventet: gyldigt eksempel, manglende kilder, opdigtet citat, ukendt kode, dublet og forkert frekvens. Dette er afgrænsede kontroltests, ikke bevis for fejlfri validering generelt.

**Styrken er sporbarhed.** Skillen behandlede hele materialet og knyttede sine koder til eksisterende citater. Den blinde koder noterede også uklarheder som forskellen mellem publicering af artikler og deling af data.

**Den største svaghed er kodevalg og abstraktionsniveau.** Eksempelvis gav koden “Experience with sharing research data [R]” kun 35,9 i F1: AI’en genfandt 7 af 31 referenceforekomster. “Support implementation tips” gav 32,4. En gennemgang af uenigheder viser både brede referencekoder, som AI’en undlader, og mere konkrete AI-koder, som ikke er registreret af forskerne. I I4/enhed 1 bruger AI’en eksempelvis en data-steward-kode, mens referencen omfatter støtteimplementering. Passagen indeholder både udvikling af støtteprogrammer og ansættelse af data stewards; forskellen er derfor ikke alene tekstforståelse.

**Gentageligheden er bedre end referenceoverensstemmelsen, men ikke fuldstændig.** De to blinde I1-kørsler havde F1 83,4 og præcis samme kodesæt i 30,8 % af enhederne. Gennemsnitlig kappa pr. kode var 0,774, med interval 0–1 blandt definerede værdier. Det er AI-konsistens, ikke menneskelig interkoderreliabilitet. Gentagelsen blev kørt separat og samtidig, ikke som en tidsmæssig driftmåling efter afslutningen. Førstekørslen bevares som benchmark; den er ikke genkodet for at forbedre scoren.

## Hvor sikkert kan scoren fortolkes?

Forskerne kodede 224 tekstpassager med 377 kodetildelinger. Flere passager dækker flere spørgsmål/svar. Til hovedmålet blev en referencekode knyttet til hver enhed med mindst 20 tegns overlap efter fjernelse af whitespace. Det gav 545 referencekodninger på enhedsniveau. Rå og kodet tekst blev matchet for samtlige 262 enheder; alle 224 citatpositioner blev kontrolleret. Kun whitespace og to indlejrede objektmarkører blev ignoreret ved denne tekstsammenligning.

Hvis hver referencepassage i stedet kun knyttes til den enhed, den overlapper mest, bliver F1 **53,0**. Intervallet 53,0–60,1 er en følsomhedsanalyse af opdelingen, ikke et statistisk konfidensinterval. Derfor skal 60,1 læses som benchmarkscore under en oplyst regel, ikke som “60,1 % af analysen er sand”.

Kodebogen indeholder forklaringer, men ikke udførlige grænsetilfælde for alle koder. Referencen er en publiceret forskerkodning, ikke et fejlfrit facit eller et datasæt med flere uafhængige menneskelige kodninger. Syv interviews fra ét emne kan ikke dokumentere generel kvalitet på andre fagområder. Offentlige data kan desuden have indgået i modellens træningsmateriale; dette kan ikke kontrolleres her.

## Vurdering og næste forbedring

**Teknisk solidt i denne kørsel; kodningskvaliteten kræver menneskelig kontrol.** Prioritér bedre afgrænsning mellem brede erfaringskoder og konkrete støtte-/infrastrukturkoder, tydelige regler for samtidige koder og kontrol af oversete brede temaer. Afprøv en forbedret kodebog på nyt materiale, så den aktuelle reference ikke bliver facit, som systemet tilpasses efter.

## Dokumentation

Originaldata, kodninger, frekvenser, uenigheder, målinger, metodeprotokol og validatorlog ligger i samme mappe. Se `SOURCE.md` for kreditering og licens. Instrument: Content Analysis Skill by Peter Malmkjaer, 5.0.0-beta.3. De metodiske henvisninger i skillen er ikke genverificeret som selvstændig litteraturundersøgelse i denne test.

Datakilde: [TU Delft / 4TU.ResearchData](https://doi.org/10.4121/19635147), hentet 9. september 2026.
