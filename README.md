<a id="top"></a>

# Academic Paper Forensic & Research Integrity Auditor

**Author:** 𝓐.𝓒.𝓑  
**License:** MIT  
**Documentation:** 12 languages  
**Version:** v.0.0.1

An evidence-first master prompt for AI-assisted screening of academic papers, figures, statistics, references, metadata, provenance, and research-integrity signals.

> **Important:** This project is an investigative screening aid, not a forensic verdict. AI can be wrong, miss problems, or flag benign material. Findings should be independently verified before they are used for public allegations, editorial sanctions, disciplinary action, or formal misconduct determinations.

---

## 🌐 Language navigation

| | | |
|---|---|---|
| [English](#lang-en) | [Türkçe](#lang-tr) | [Deutsch](#lang-de) |
| [Français](#lang-fr) | [Español](#lang-es) | [Italiano](#lang-it) |
| [Português](#lang-pt) | [العربية](#lang-ar) | [简体中文](#lang-zh-cn) |
| [繁體中文](#lang-zh-tw) | [한국어](#lang-ko) | [日本語](#lang-ja) |

---

<a id="lang-en"></a>
## English

### What this project is

This repository contains a reusable master prompt designed to turn a capable AI system into an **Academic Paper Forensic & Research Integrity Auditor**. It is intended for researchers, editors, peer reviewers, journalists, students, and research-integrity professionals who need a structured first-pass examination of scientific papers and related files.

The prompt is deliberately evidence-first. It prioritizes **observable evidence, reproducibility, uncertainty, alternative explanations, external verification, and human review**. It does not treat suspicious patterns as proof of fraud, falsification, fabrication, plagiarism, or intentional misconduct.

### What it can examine

Depending on the files and tools available to the AI system, the prompt can examine:

- internal contradictions and methods/results inconsistencies;
- sample-size, percentage, p-value, confidence-interval, and other statistical inconsistencies;
- suspicious figure, panel, or image-region reuse;
- possible cloning, splicing, copy-move, resampling, patching, or other digital-editing signals;
- possible AI-generated or AI-modified scientific imagery;
- PDF and original-image metadata, including EXIF/XMP when available;
- DOI, citation, reference, correction, retraction, and publisher-notice information;
- ethics approval, study registration, timeline, affiliation, and provenance inconsistencies;
- paper-mill or systematic publication-manipulation patterns;
- cross-paper similarities in images, text, tables, graphs, or numerical sequences when several papers are supplied.

The prompt also requires the AI to identify evidence **against** a misconduct interpretation and to challenge its strongest findings before presenting them.

### What it cannot guarantee

The prompt does not make an AI system omniscient or equivalent to a laboratory, journal investigation, or forensic expert. A PDF may contain compressed images, stripped metadata, incomplete tables, or no raw data. A model without web access cannot externally verify DOI records, retractions, citations, or publisher notices. A model without image-forensics tools cannot honestly claim to have performed pixel-level tests.

An anomaly is not proof of intent. Photoshop metadata is not proof of falsification. Missing metadata is not proof of manipulation. An AI-detector score is not proof that an image was AI-generated. Failure to detect a problem is not proof that the paper is authentic, error-free, or free from misconduct.

### Repository structure

```text
academic-paper-forensic-auditor/
├── README.md
├── master_prompt.md
└── LICENSE
```

- **README.md** — complete project documentation in 12 languages.
- **master_prompt.md** — the full master prompt. In normal use, only the `USER INPUT — EDIT ONLY THIS SECTION` block at the bottom should be changed.
- **LICENSE** — MIT License.

### Quick start

1. Open `master_prompt.md`.
2. Copy the entire prompt into the AI system you want to use.
3. Go to the `USER INPUT — EDIT ONLY THIS SECTION` block at the bottom.
4. Set the output language, audience level, report length, analysis depth, priority focus, output format, and any special instructions.
5. Upload the paper PDF. If available, also provide supplementary files, original figures, raw data, uncropped blots, microscopy source files, or related papers.
6. Start the analysis.

Recommended general-purpose configuration:

```text
OUTPUT_LANGUAGE = [English]
AUDIENCE = [Professional]
OUTPUT_LENGTH = [Detailed]
ANALYSIS_DEPTH = [Deep]
PRIORITY_FOCUS = [All areas]
OUTPUT_FORMAT = [Structured forensic report]
SPECIAL_INSTRUCTIONS = [None]
MATERIALS = [Analyze the uploaded paper and all accompanying files. Use DOI/URL and external sources when available.]
```

### For stronger image and metadata analysis

A journal PDF is sufficient for broad screening, but it is not ideal for high-confidence image forensics. For stronger analysis, provide the highest-quality source files available, such as:

- original TIFF/PNG/JPEG figures;
- uncropped western blots or gels;
- raw microscopy exports or instrument-native image files;
- supplementary figures and acquisition metadata;
- raw datasets and analysis outputs;
- related papers when cross-paper comparison is relevant.

If only a PDF is available, the report should explicitly limit its conclusions to what can be supported from that PDF.

### Understanding the report

Findings are classified from **Level 0** to **Level 4**:

- **Level 0:** no meaningful concern detected;
- **Level 1:** weak signal with plausible benign explanations;
- **Level 2:** reproducible material inconsistency;
- **Level 3:** strong forensic concern requiring expert review;
- **Level 4:** integrity issue corroborated by an authoritative external source.

Level 2 or Level 3 does **not** mean that misconduct occurred. Confidence labels refer to confidence in the observation itself, not confidence about an author's intent.

### Recommended use

Use this project for triage, peer-review preparation, integrity screening, source verification, and prioritizing what a qualified human should inspect next. For consequential decisions, verify important findings independently and obtain original source material whenever possible.

<p align="right"><a href="#top">↑ Back to language menu</a></p>

---

<a id="lang-tr"></a>
## Türkçe

### Bu proje nedir?

Bu depo, gelişmiş bir yapay zekâ sistemini **Akademik Makale Forensik ve Araştırma Bütünlüğü Denetçisi** olarak kullanmaya yönelik yeniden kullanılabilir bir ana prompt içerir. Araştırmacılar, editörler, hakemler, gazeteciler, öğrenciler ve araştırma bütünlüğü uzmanlarının bilimsel makaleleri ve ilişkili dosyaları sistematik biçimde ön incelemesine yardımcı olmak için tasarlanmıştır.

Prompt bilinçli biçimde kanıt odaklıdır. **Gözlemlenebilir kanıtı, yeniden üretilebilirliği, belirsizliğin açıkça belirtilmesini, alternatif açıklamaları, harici doğrulamayı ve insan incelemesini** önceliklendirir. Şüpheli bir örüntüyü doğrudan sahtekârlık, falsifikasyon, fabrikasyon, intihal veya kasıtlı suistimal kanıtı olarak kabul etmez.

### Neleri inceleyebilir?

Kullanılan yapay zekâ sisteminin erişebildiği dosya ve araçlara bağlı olarak şunları inceleyebilir:

- metin içi çelişkiler ve yöntem-sonuç uyumsuzlukları;
- örneklem sayısı, yüzde, p-değeri, güven aralığı ve diğer istatistiksel tutarsızlıklar;
- şüpheli figür, panel veya görüntü bölgesi tekrarları;
- olası klonlama, splice, copy-move, resampling, patching ve diğer dijital düzenleme sinyalleri;
- yapay zekâ ile üretilmiş veya değiştirilmiş olabilecek bilimsel görseller;
- mevcutsa PDF ve orijinal görsellerin EXIF/XMP dahil metadata bilgileri;
- DOI, atıf, kaynakça, düzeltme, geri çekme ve yayıncı bildirimleri;
- etik kurul, çalışma kaydı, zaman çizelgesi, kurum ve provenance tutarsızlıkları;
- paper-mill veya sistematik yayın manipülasyonu örüntüleri;
- birden fazla makale sağlandığında makaleler arası görsel, metin, tablo, grafik veya sayısal dizi benzerlikleri.

Prompt ayrıca yapay zekânın suistimal yorumuna **karşı olan kanıtları** da aramasını ve en güçlü bulgularını raporlamadan önce yeniden sorgulamasını zorunlu kılar.

### Neyi garanti etmez?

Bu prompt, yapay zekâyı hatasız bir laboratuvar, yayın kurulu soruşturması veya adli uzman haline getirmez. PDF içindeki görseller sıkıştırılmış olabilir, metadata silinmiş olabilir, tablolar eksik olabilir veya ham veri hiç sağlanmamış olabilir. İnternet erişimi olmayan bir model DOI, retraction, atıf veya yayıncı bildirimlerini dışarıdan doğrulayamaz. Görsel forensik araçları olmayan bir model piksel düzeyinde test yapmış gibi davranmamalıdır.

Bir anomali kasıt kanıtı değildir. Photoshop metadata'sı falsifikasyon kanıtı değildir. Metadata'nın olmaması manipülasyon kanıtı değildir. Bir AI-detector skoru görselin yapay zekâ ile üretildiğini kanıtlamaz. Hiçbir sorun bulunmaması da makalenin özgün, hatasız veya araştırma bütünlüğü açısından sorunsuz olduğunu kanıtlamaz.

### Dosya yapısı

```text
academic-paper-forensic-auditor/
├── README.md
├── master_prompt.md
└── LICENSE
```

- **README.md** — 12 dilde tam proje dokümantasyonu.
- **master_prompt.md** — ana promptun tamamı. Normal kullanımda yalnızca en alttaki `USER INPUT — EDIT ONLY THIS SECTION` bölümü değiştirilir.
- **LICENSE** — MIT Lisansı.

### Hızlı kullanım

1. `master_prompt.md` dosyasını açın.
2. Promptun tamamını kullanacağınız yapay zekâ sistemine kopyalayın.
3. En alttaki `USER INPUT — EDIT ONLY THIS SECTION` bölümüne gidin.
4. Çıktı dili, hedef okuyucu seviyesi, rapor uzunluğu, analiz derinliği, öncelik alanı, çıktı biçimi ve özel talimatları ayarlayın.
5. Makalenin PDF'sini yükleyin. Varsa supplementary dosyaları, orijinal figürleri, ham veriyi, uncropped blotları, microscopy kaynak dosyalarını veya ilişkili makaleleri de ekleyin.
6. Analizi başlatın.

Önerilen genel ayar:

```text
OUTPUT_LANGUAGE = [Turkish]
AUDIENCE = [Professional]
OUTPUT_LENGTH = [Detailed]
ANALYSIS_DEPTH = [Deep]
PRIORITY_FOCUS = [All areas]
OUTPUT_FORMAT = [Structured forensic report]
SPECIAL_INSTRUCTIONS = [None]
MATERIALS = [Analyze the uploaded paper and all accompanying files. Use DOI/URL and external sources when available.]
```

### Daha güçlü görsel ve metadata analizi için

Dergi PDF'si geniş kapsamlı ön tarama için yeterlidir; ancak yüksek güvenli görsel forensik inceleme için ideal değildir. Mümkünse şu kaynak dosyaları da sağlayın:

- orijinal TIFF/PNG/JPEG figürleri;
- uncropped western blot veya gel görüntüleri;
- ham microscopy çıktıları veya cihazın native görüntü dosyaları;
- supplementary figürler ve acquisition metadata;
- ham veri setleri ve analiz çıktıları;
- cross-paper karşılaştırma gerekiyorsa ilişkili makaleler.

Yalnızca PDF mevcutsa rapor, sonuçlarını açıkça o PDF'den desteklenebilen kanıtlarla sınırlandırmalıdır.

### Rapor nasıl okunur?

Bulgular **Level 0** ile **Level 4** arasında sınıflandırılır:

- **Level 0:** anlamlı bir sorun tespit edilmedi;
- **Level 1:** makul masum açıklamaları bulunan zayıf sinyal;
- **Level 2:** yeniden üretilebilir maddi tutarsızlık;
- **Level 3:** uzman incelemesi gerektiren güçlü forensik bulgu;
- **Level 4:** yetkili harici bir kaynakla doğrulanmış araştırma bütünlüğü sorunu.

Level 2 veya Level 3, suistimalin gerçekleştiği anlamına **gelmez**. Güven etiketi, yazarın niyetine değil, gözlemin kendisinin doğru olduğuna ilişkin güveni ifade eder.

### Önerilen kullanım

Bu projeyi ön eleme, hakemlik hazırlığı, araştırma bütünlüğü taraması, kaynak doğrulama ve hangi konuların uzman tarafından incelenmesi gerektiğini önceliklendirmek için kullanın. Sonuç doğurabilecek kararlar için önemli bulguları bağımsız biçimde doğrulayın ve mümkün olduğunda orijinal kaynak dosyalarını inceleyin.

<p align="right"><a href="#top">↑ Dil menüsüne dön</a></p>

---

<a id="lang-de"></a>
## Deutsch

### Was ist dieses Projekt?

Dieses Repository enthält einen wiederverwendbaren Master-Prompt, der ein leistungsfähiges KI-System als **forensischen Prüfer für wissenschaftliche Publikationen und Forschungsintegrität** einsetzt. Er richtet sich an Forschende, Herausgebende, Peer-Reviewer, Journalistinnen und Journalisten, Studierende sowie Fachleute für Forschungsintegrität, die wissenschaftliche Arbeiten und zugehörige Dateien strukturiert vorprüfen möchten.

Der Prompt ist bewusst evidenzorientiert. Er priorisiert **beobachtbare Belege, Reproduzierbarkeit, transparente Unsicherheit, alternative Erklärungen, externe Verifikation und menschliche Prüfung**. Auffällige Muster werden nicht automatisch als Beweis für Betrug, Fälschung, Fabrikation, Plagiat oder vorsätzliches Fehlverhalten behandelt.

### Was kann untersucht werden?

Abhängig von den verfügbaren Dateien und Werkzeugen kann der Prompt unter anderem prüfen:

- interne Widersprüche sowie Inkonsistenzen zwischen Methoden und Ergebnissen;
- Unstimmigkeiten bei Stichprobengrößen, Prozentwerten, p-Werten, Konfidenzintervallen und weiteren Statistiken;
- verdächtige Wiederverwendung von Abbildungen, Panels oder Bildbereichen;
- mögliche Hinweise auf Cloning, Splicing, Copy-Move, Resampling, Patching oder andere digitale Bearbeitung;
- mögliche KI-generierte oder KI-modifizierte wissenschaftliche Bilder;
- PDF- und Originalbild-Metadaten einschließlich EXIF/XMP, sofern verfügbar;
- DOI-, Zitations-, Literatur-, Korrektur-, Retraction- und Publisher-Hinweise;
- Inkonsistenzen bei Ethikvoten, Studienregistrierung, Zeitabläufen, Institutionen und Provenienz;
- Muster von Paper Mills oder systematischer Publikationsmanipulation;
- bildliche, textliche, tabellarische, grafische oder numerische Ähnlichkeiten zwischen mehreren Arbeiten.

Der Prompt verlangt außerdem, dass die KI aktiv nach Belegen **gegen** eine Fehlverhaltensinterpretation sucht und ihre stärksten Befunde vor der Ausgabe kritisch hinterfragt.

### Was kann nicht garantiert werden?

Der Prompt macht ein KI-System weder allwissend noch zu einem Ersatz für ein Labor, eine Verlagsermittlung oder eine forensische Fachperson. PDF-Abbildungen können komprimiert sein, Metadaten können fehlen, Tabellen unvollständig sein und Rohdaten können gar nicht vorliegen. Ohne Webzugriff können DOI-Daten, Retractions, Zitationen und Publisher-Hinweise nicht extern verifiziert werden. Ohne geeignete Bildforensik-Werkzeuge darf das System keine Pixelanalysen vortäuschen.

Eine Anomalie beweist keine Absicht. Photoshop-Metadaten beweisen keine Fälschung. Fehlende Metadaten beweisen keine Manipulation. Ein KI-Detektorwert beweist keine KI-Erzeugung. Umgekehrt beweist ein unauffälliges Ergebnis nicht, dass eine Publikation authentisch, fehlerfrei oder frei von Integritätsproblemen ist.

### Repository-Struktur

```text
academic-paper-forensic-auditor/
├── README.md
├── master_prompt.md
└── LICENSE
```

- **README.md** — vollständige Projektdokumentation in 12 Sprachen.
- **master_prompt.md** — vollständiger Master-Prompt. Im Normalfall wird nur der Block `USER INPUT — EDIT ONLY THIS SECTION` am Ende geändert.
- **LICENSE** — MIT-Lizenz.

### Schnellstart

1. `master_prompt.md` öffnen.
2. Den gesamten Prompt in das gewünschte KI-System kopieren.
3. Zum Abschnitt `USER INPUT — EDIT ONLY THIS SECTION` am Ende gehen.
4. Ausgabesprache, Zielpublikum, Berichtslänge, Analysetiefe, Schwerpunkt, Ausgabeformat und Sonderanweisungen festlegen.
5. Das PDF hochladen. Falls vorhanden, Supplemente, Originalabbildungen, Rohdaten, ungekürzte Blots, Mikroskopie-Quelldateien oder verwandte Arbeiten ergänzen.
6. Analyse starten.

Empfohlene allgemeine Konfiguration:

```text
OUTPUT_LANGUAGE = [German]
AUDIENCE = [Professional]
OUTPUT_LENGTH = [Detailed]
ANALYSIS_DEPTH = [Deep]
PRIORITY_FOCUS = [All areas]
OUTPUT_FORMAT = [Structured forensic report]
SPECIAL_INSTRUCTIONS = [None]
MATERIALS = [Analyze the uploaded paper and all accompanying files. Use DOI/URL and external sources when available.]
```

### Für eine stärkere Bild- und Metadatenanalyse

Ein Journal-PDF reicht für ein breites Screening, ist aber für hochzuverlässige Bildforensik nicht ideal. Wenn möglich, sollten zusätzlich bereitgestellt werden:

- originale TIFF/PNG/JPEG-Abbildungen;
- unbeschnittene Western Blots oder Gele;
- Roh-Exporte aus der Mikroskopie oder instrumentnative Bilddateien;
- Supplement-Abbildungen und Aufnahmemetadaten;
- Rohdatensätze und Analyseergebnisse;
- verwandte Publikationen für Cross-Paper-Vergleiche.

Wenn nur ein PDF vorliegt, sollte der Bericht seine Schlussfolgerungen ausdrücklich auf die daraus belegbaren Informationen begrenzen.

### Wie ist der Bericht zu lesen?

Befunde werden von **Level 0** bis **Level 4** eingestuft:

- **Level 0:** kein relevanter Befund erkannt;
- **Level 1:** schwaches Signal mit plausiblen harmlosen Erklärungen;
- **Level 2:** reproduzierbare materielle Inkonsistenz;
- **Level 3:** starker forensischer Befund, der eine Expertenprüfung erfordert;
- **Level 4:** durch eine autoritative externe Quelle bestätigtes Integritätsproblem.

Level 2 oder Level 3 bedeutet **nicht**, dass wissenschaftliches Fehlverhalten stattgefunden hat. Konfidenzangaben beziehen sich auf die Zuverlässigkeit der Beobachtung, nicht auf die Absicht einer Autorin oder eines Autors.

### Empfohlene Verwendung

Nutzen Sie das Projekt für Triage, Vorbereitung von Peer Reviews, Integritätsscreening, Quellenprüfung und die Priorisierung weiterer Expertenprüfung. Vor folgenreichen Entscheidungen sollten wichtige Befunde unabhängig bestätigt und nach Möglichkeit Originalmaterialien beschafft werden.

<p align="right"><a href="#top">↑ Zurück zum Sprachmenü</a></p>

---

<a id="lang-fr"></a>
## Français

### Qu'est-ce que ce projet ?

Ce dépôt contient un prompt principal réutilisable conçu pour transformer un système d'IA performant en **auditeur forensique d'articles scientifiques et d'intégrité de la recherche**. Il s'adresse aux chercheurs, éditeurs, évaluateurs, journalistes, étudiants et professionnels de l'intégrité scientifique souhaitant effectuer un premier examen structuré d'un article et de ses fichiers associés.

Le prompt suit une approche volontairement fondée sur les preuves. Il donne la priorité aux **éléments observables, à la reproductibilité, à l'incertitude explicite, aux explications alternatives, à la vérification externe et à l'examen humain**. Un signal suspect n'est jamais traité automatiquement comme une preuve de fraude, falsification, fabrication, plagiat ou faute intentionnelle.

### Que peut-il examiner ?

Selon les fichiers et outils accessibles au système d'IA, il peut notamment analyser :

- les contradictions internes et les incohérences entre méthodes et résultats ;
- les incohérences de taille d'échantillon, pourcentages, valeurs p, intervalles de confiance et autres statistiques ;
- la réutilisation suspecte de figures, panneaux ou zones d'image ;
- des indices possibles de clonage, montage, copy-move, rééchantillonnage, retouche locale ou autre édition numérique ;
- des images scientifiques potentiellement générées ou modifiées par IA ;
- les métadonnées PDF et image, y compris EXIF/XMP lorsqu'elles sont disponibles ;
- les DOI, citations, références, corrections, rétractations et avis des éditeurs ;
- les incohérences relatives à l'éthique, l'enregistrement de l'étude, la chronologie, les affiliations et la provenance ;
- des schémas de paper mill ou de manipulation systématique de publication ;
- les similitudes entre plusieurs articles au niveau des images, textes, tableaux, graphiques ou séquences numériques.

Le prompt impose également de rechercher les éléments **contraires** à une interprétation de faute scientifique et de soumettre les résultats les plus forts à une vérification critique avant de les présenter.

### Ce qu'il ne peut pas garantir

Ce prompt ne transforme pas une IA en système infaillible ni en substitut d'un laboratoire, d'une enquête éditoriale ou d'un expert forensique. Les images d'un PDF peuvent être compressées, les métadonnées supprimées, les tableaux incomplets et les données brutes absentes. Sans accès au web, l'IA ne peut pas vérifier de manière externe les DOI, rétractations, citations ou avis d'éditeur. Sans outils d'analyse d'image adaptés, elle ne doit pas prétendre avoir effectué une analyse au niveau du pixel.

Une anomalie ne prouve pas l'intention. La présence de métadonnées Photoshop ne prouve pas une falsification. L'absence de métadonnées ne prouve pas une manipulation. Un score de détecteur d'IA ne prouve pas qu'une image a été générée par IA. Inversement, l'absence de problème détecté ne prouve pas qu'un article est authentique, exempt d'erreur ou exempt de problème d'intégrité.

### Structure du dépôt

```text
academic-paper-forensic-auditor/
├── README.md
├── master_prompt.md
└── LICENSE
```

- **README.md** — documentation complète du projet en 12 langues.
- **master_prompt.md** — prompt principal complet. En usage normal, seul le bloc `USER INPUT — EDIT ONLY THIS SECTION` situé à la fin doit être modifié.
- **LICENSE** — licence MIT.

### Démarrage rapide

1. Ouvrez `master_prompt.md`.
2. Copiez l'intégralité du prompt dans le système d'IA choisi.
3. Allez au bloc `USER INPUT — EDIT ONLY THIS SECTION` situé à la fin.
4. Définissez la langue de sortie, le niveau du public, la longueur du rapport, la profondeur d'analyse, les priorités, le format de sortie et les instructions particulières.
5. Téléversez le PDF de l'article. Si disponibles, ajoutez les suppléments, figures originales, données brutes, blots non recadrés, fichiers source de microscopie ou articles associés.
6. Lancez l'analyse.

Configuration générale recommandée :

```text
OUTPUT_LANGUAGE = [French]
AUDIENCE = [Professional]
OUTPUT_LENGTH = [Detailed]
ANALYSIS_DEPTH = [Deep]
PRIORITY_FOCUS = [All areas]
OUTPUT_FORMAT = [Structured forensic report]
SPECIAL_INSTRUCTIONS = [None]
MATERIALS = [Analyze the uploaded paper and all accompanying files. Use DOI/URL and external sources when available.]
```

### Pour une analyse d'image et de métadonnées plus robuste

Un PDF de revue suffit pour un dépistage général, mais il n'est pas idéal pour une analyse forensique d'image à forte confiance. Lorsque possible, fournissez également :

- les figures originales en TIFF/PNG/JPEG ;
- les western blots ou gels non recadrés ;
- les exports bruts de microscopie ou les fichiers natifs de l'instrument ;
- les figures supplémentaires et métadonnées d'acquisition ;
- les jeux de données bruts et résultats d'analyse ;
- les articles liés lorsqu'une comparaison inter-publications est utile.

Si seul un PDF est disponible, le rapport doit limiter explicitement ses conclusions aux éléments réellement démontrables à partir de ce PDF.

### Comprendre le rapport

Les résultats sont classés de **Level 0** à **Level 4** :

- **Level 0 :** aucune anomalie significative détectée ;
- **Level 1 :** signal faible avec explications bénignes plausibles ;
- **Level 2 :** incohérence matérielle reproductible ;
- **Level 3 :** préoccupation forensique forte nécessitant un examen expert ;
- **Level 4 :** problème d'intégrité corroboré par une source externe faisant autorité.

Un Level 2 ou Level 3 ne signifie **pas** qu'une faute scientifique a été commise. Le niveau de confiance concerne la fiabilité de l'observation, et non l'intention des auteurs.

### Utilisation recommandée

Utilisez ce projet pour le triage, la préparation d'une évaluation par les pairs, le contrôle d'intégrité, la vérification des sources et la priorisation des points nécessitant une expertise humaine. Avant toute décision importante, vérifiez indépendamment les résultats clés et obtenez les fichiers sources originaux lorsque cela est possible.

<p align="right"><a href="#top">↑ Retour au menu des langues</a></p>

---

<a id="lang-es"></a>
## Español

### ¿Qué es este proyecto?

Este repositorio contiene un prompt maestro reutilizable diseñado para convertir un sistema de IA avanzado en un **auditor forense de artículos académicos e integridad de la investigación**. Está pensado para investigadores, editores, revisores, periodistas, estudiantes y profesionales de integridad científica que necesiten una revisión inicial estructurada de artículos y archivos relacionados.

El prompt sigue un enfoque deliberadamente basado en evidencia. Prioriza **evidencia observable, reproducibilidad, incertidumbre explícita, explicaciones alternativas, verificación externa y revisión humana**. Un patrón sospechoso nunca se trata automáticamente como prueba de fraude, falsificación, fabricación, plagio o mala conducta intencional.

### ¿Qué puede examinar?

Según los archivos y herramientas disponibles para el sistema de IA, puede analizar:

- contradicciones internas e inconsistencias entre métodos y resultados;
- inconsistencias en tamaños de muestra, porcentajes, valores p, intervalos de confianza y otras estadísticas;
- reutilización sospechosa de figuras, paneles o regiones de imagen;
- posibles señales de clonación, empalme, copy-move, remuestreo, parcheado u otra edición digital;
- imágenes científicas potencialmente generadas o modificadas con IA;
- metadatos de PDF e imágenes originales, incluidos EXIF/XMP cuando estén disponibles;
- DOI, citas, referencias, correcciones, retractaciones y avisos editoriales;
- inconsistencias en ética, registro del estudio, cronología, afiliaciones y procedencia;
- patrones de paper mills o manipulación sistemática de publicaciones;
- similitudes entre varios artículos en imágenes, texto, tablas, gráficos o secuencias numéricas.

El prompt también exige buscar evidencia **en contra** de una interpretación de mala conducta y someter los hallazgos más fuertes a una revisión crítica antes de presentarlos.

### ¿Qué no puede garantizar?

El prompt no convierte a la IA en un sistema infalible ni sustituye a un laboratorio, una investigación editorial o un experto forense. Las imágenes de un PDF pueden estar comprimidas, los metadatos pueden haber sido eliminados, las tablas pueden estar incompletas y puede no existir acceso a datos brutos. Sin acceso web, el sistema no puede verificar externamente DOI, retractaciones, citas o avisos editoriales. Sin herramientas forenses de imagen, no debe afirmar que realizó pruebas a nivel de píxel.

Una anomalía no demuestra intención. Los metadatos de Photoshop no demuestran falsificación. La ausencia de metadatos no demuestra manipulación. Un porcentaje de un detector de IA no demuestra generación por IA. Del mismo modo, no detectar problemas no demuestra que el artículo sea auténtico, esté libre de errores o carezca de problemas de integridad.

### Estructura del repositorio

```text
academic-paper-forensic-auditor/
├── README.md
├── master_prompt.md
└── LICENSE
```

- **README.md** — documentación completa del proyecto en 12 idiomas.
- **master_prompt.md** — prompt maestro completo. En uso normal, solo se modifica el bloque `USER INPUT — EDIT ONLY THIS SECTION` del final.
- **LICENSE** — licencia MIT.

### Inicio rápido

1. Abre `master_prompt.md`.
2. Copia el prompt completo en el sistema de IA que quieras utilizar.
3. Ve al bloque `USER INPUT — EDIT ONLY THIS SECTION` del final.
4. Configura idioma de salida, nivel de audiencia, longitud del informe, profundidad de análisis, prioridad, formato e instrucciones especiales.
5. Sube el PDF. Si están disponibles, añade suplementos, figuras originales, datos brutos, blots sin recortar, archivos fuente de microscopía o artículos relacionados.
6. Inicia el análisis.

Configuración general recomendada:

```text
OUTPUT_LANGUAGE = [Spanish]
AUDIENCE = [Professional]
OUTPUT_LENGTH = [Detailed]
ANALYSIS_DEPTH = [Deep]
PRIORITY_FOCUS = [All areas]
OUTPUT_FORMAT = [Structured forensic report]
SPECIAL_INSTRUCTIONS = [None]
MATERIALS = [Analyze the uploaded paper and all accompanying files. Use DOI/URL and external sources when available.]
```

### Para un análisis de imágenes y metadatos más sólido

Un PDF de revista sirve para una revisión general, pero no es ideal para análisis forense de imágenes de alta confianza. Cuando sea posible, aporta:

- figuras originales en TIFF/PNG/JPEG;
- western blots o geles sin recortar;
- exportaciones brutas de microscopía o archivos nativos del instrumento;
- figuras suplementarias y metadatos de adquisición;
- conjuntos de datos brutos y resultados de análisis;
- artículos relacionados cuando sea útil la comparación entre publicaciones.

Si solo existe el PDF, el informe debe limitar explícitamente sus conclusiones a la evidencia que realmente puede sostenerse a partir de ese archivo.

### Cómo interpretar el informe

Los hallazgos se clasifican de **Level 0** a **Level 4**:

- **Level 0:** no se detecta una preocupación significativa;
- **Level 1:** señal débil con explicaciones benignas plausibles;
- **Level 2:** inconsistencia material reproducible;
- **Level 3:** preocupación forense fuerte que requiere revisión experta;
- **Level 4:** problema de integridad corroborado por una fuente externa autorizada.

Un Level 2 o Level 3 **no** significa que haya ocurrido mala conducta. La etiqueta de confianza indica confianza en la observación, no en la intención del autor.

### Uso recomendado

Utiliza este proyecto para triage, preparación de revisiones por pares, controles de integridad, verificación de fuentes y priorización de aspectos que deba revisar una persona cualificada. Antes de decisiones con consecuencias, verifica de forma independiente los hallazgos importantes y consigue material fuente original siempre que sea posible.

<p align="right"><a href="#top">↑ Volver al menú de idiomas</a></p>

---

<a id="lang-it"></a>
## Italiano

### Che cos'è questo progetto?

Questo repository contiene un master prompt riutilizzabile progettato per trasformare un sistema di IA avanzato in un **auditor forense di articoli accademici e integrità della ricerca**. È pensato per ricercatori, editor, revisori, giornalisti, studenti e professionisti dell'integrità scientifica che necessitano di una prima analisi strutturata di articoli e file correlati.

Il prompt adotta intenzionalmente un approccio basato sulle prove. Dà priorità a **evidenze osservabili, riproducibilità, incertezza esplicita, spiegazioni alternative, verifica esterna e revisione umana**. Un pattern sospetto non viene mai trattato automaticamente come prova di frode, falsificazione, fabbricazione, plagio o condotta intenzionalmente scorretta.

### Che cosa può esaminare?

In base ai file e agli strumenti disponibili al sistema di IA, può analizzare:

- contraddizioni interne e incoerenze tra metodi e risultati;
- incoerenze in dimensione del campione, percentuali, p-value, intervalli di confidenza e altre statistiche;
- riutilizzo sospetto di figure, pannelli o regioni d'immagine;
- possibili segnali di clonazione, splicing, copy-move, ricampionamento, patching o altre modifiche digitali;
- immagini scientifiche potenzialmente generate o modificate tramite IA;
- metadati PDF e delle immagini originali, inclusi EXIF/XMP quando disponibili;
- DOI, citazioni, riferimenti, correzioni, ritrattazioni e comunicazioni dell'editore;
- incoerenze relative a etica, registrazione dello studio, cronologia, affiliazioni e provenienza;
- pattern di paper mill o manipolazione sistematica delle pubblicazioni;
- somiglianze tra più articoli in immagini, testo, tabelle, grafici o sequenze numeriche.

Il prompt richiede inoltre di cercare evidenze **contrarie** a un'interpretazione di cattiva condotta e di sottoporre i risultati più forti a una verifica critica prima di presentarli.

### Che cosa non può garantire?

Il prompt non rende l'IA infallibile e non sostituisce un laboratorio, un'indagine editoriale o un esperto forense. Le immagini nei PDF possono essere compresse, i metadati rimossi, le tabelle incomplete e i dati grezzi assenti. Senza accesso al web non è possibile verificare esternamente DOI, ritrattazioni, citazioni o avvisi editoriali. Senza strumenti di image forensics il sistema non deve dichiarare di aver eseguito analisi a livello di pixel.

Un'anomalia non dimostra l'intenzione. La presenza di metadati Photoshop non dimostra falsificazione. L'assenza di metadati non dimostra manipolazione. Un punteggio di un AI detector non dimostra che un'immagine sia stata generata dall'IA. Allo stesso modo, non rilevare problemi non dimostra che un articolo sia autentico, privo di errori o privo di problemi di integrità.

### Struttura del repository

```text
academic-paper-forensic-auditor/
├── README.md
├── master_prompt.md
└── LICENSE
```

- **README.md** — documentazione completa del progetto in 12 lingue.
- **master_prompt.md** — master prompt completo. Nell'uso normale si modifica solo il blocco `USER INPUT — EDIT ONLY THIS SECTION` in fondo.
- **LICENSE** — licenza MIT.

### Avvio rapido

1. Apri `master_prompt.md`.
2. Copia l'intero prompt nel sistema di IA che vuoi utilizzare.
3. Vai al blocco `USER INPUT — EDIT ONLY THIS SECTION` in fondo.
4. Imposta lingua di output, livello del pubblico, lunghezza del report, profondità dell'analisi, priorità, formato e istruzioni speciali.
5. Carica il PDF dell'articolo. Se disponibili, aggiungi supplementi, figure originali, dati grezzi, blot non ritagliati, file sorgente di microscopia o articoli correlati.
6. Avvia l'analisi.

Configurazione generale consigliata:

```text
OUTPUT_LANGUAGE = [Italian]
AUDIENCE = [Professional]
OUTPUT_LENGTH = [Detailed]
ANALYSIS_DEPTH = [Deep]
PRIORITY_FOCUS = [All areas]
OUTPUT_FORMAT = [Structured forensic report]
SPECIAL_INSTRUCTIONS = [None]
MATERIALS = [Analyze the uploaded paper and all accompanying files. Use DOI/URL and external sources when available.]
```

### Per un'analisi più solida di immagini e metadati

Un PDF della rivista è sufficiente per uno screening generale, ma non è ideale per image forensics ad alta affidabilità. Quando possibile, fornisci anche:

- figure originali TIFF/PNG/JPEG;
- western blot o gel non ritagliati;
- esportazioni grezze di microscopia o file nativi dello strumento;
- figure supplementari e metadati di acquisizione;
- dataset grezzi e risultati di analisi;
- articoli correlati quando è utile un confronto tra pubblicazioni.

Se è disponibile solo il PDF, il report deve limitare esplicitamente le conclusioni alle evidenze realmente supportate da quel file.

### Come interpretare il report

I risultati sono classificati da **Level 0** a **Level 4**:

- **Level 0:** nessuna preoccupazione significativa rilevata;
- **Level 1:** segnale debole con spiegazioni benigne plausibili;
- **Level 2:** incoerenza materiale riproducibile;
- **Level 3:** forte preoccupazione forense che richiede revisione esperta;
- **Level 4:** problema di integrità corroborato da una fonte esterna autorevole.

Un Level 2 o Level 3 **non** significa che si sia verificata cattiva condotta. Il livello di confidenza riguarda la correttezza dell'osservazione, non l'intenzione dell'autore.

### Uso consigliato

Usa questo progetto per triage, preparazione della peer review, screening di integrità, verifica delle fonti e prioritizzazione degli aspetti che richiedono controllo umano qualificato. Prima di decisioni con conseguenze, verifica indipendentemente i risultati importanti e ottieni i file sorgente originali quando possibile.

<p align="right"><a href="#top">↑ Torna al menu delle lingue</a></p>

---

<a id="lang-pt"></a>
## Português

### O que é este projeto?

Este repositório contém um prompt mestre reutilizável criado para transformar um sistema de IA avançado em um **auditor forense de artigos acadêmicos e integridade da pesquisa**. Ele foi pensado para pesquisadores, editores, revisores, jornalistas, estudantes e profissionais de integridade científica que precisam de uma análise inicial estruturada de artigos e arquivos relacionados.

O prompt adota deliberadamente uma abordagem baseada em evidências. Ele prioriza **evidência observável, reprodutibilidade, incerteza explícita, explicações alternativas, verificação externa e revisão humana**. Um padrão suspeito nunca é tratado automaticamente como prova de fraude, falsificação, fabricação, plágio ou má conduta intencional.

### O que ele pode examinar?

Dependendo dos arquivos e ferramentas disponíveis para o sistema de IA, o prompt pode analisar:

- contradições internas e inconsistências entre métodos e resultados;
- inconsistências em tamanho de amostra, porcentagens, valores de p, intervalos de confiança e outras estatísticas;
- reutilização suspeita de figuras, painéis ou regiões de imagem;
- possíveis sinais de clonagem, splicing, copy-move, reamostragem, patching ou outras edições digitais;
- imagens científicas potencialmente geradas ou modificadas por IA;
- metadados de PDF e imagens originais, incluindo EXIF/XMP quando disponíveis;
- DOI, citações, referências, correções, retratações e avisos de editoras;
- inconsistências em ética, registro do estudo, cronologia, afiliações e proveniência;
- padrões de paper mills ou manipulação sistemática de publicações;
- semelhanças entre vários artigos em imagens, texto, tabelas, gráficos ou sequências numéricas.

O prompt também exige que a IA procure evidências **contrárias** a uma interpretação de má conduta e questione criticamente seus achados mais fortes antes de apresentá-los.

### O que ele não pode garantir?

O prompt não torna a IA infalível nem substitui um laboratório, uma investigação editorial ou um especialista forense. Imagens de PDF podem estar comprimidas, metadados podem ter sido removidos, tabelas podem estar incompletas e os dados brutos podem não estar disponíveis. Sem acesso à web, o sistema não pode verificar externamente DOI, retratações, citações ou avisos editoriais. Sem ferramentas de análise forense de imagem, não deve alegar que realizou testes em nível de pixel.

Uma anomalia não prova intenção. Metadados do Photoshop não provam falsificação. A ausência de metadados não prova manipulação. Uma pontuação de detector de IA não prova que uma imagem foi gerada por IA. Da mesma forma, não detectar problemas não prova que o artigo seja autêntico, isento de erros ou livre de problemas de integridade.

### Estrutura do repositório

```text
academic-paper-forensic-auditor/
├── README.md
├── master_prompt.md
└── LICENSE
```

- **README.md** — documentação completa do projeto em 12 idiomas.
- **master_prompt.md** — prompt mestre completo. No uso normal, apenas o bloco `USER INPUT — EDIT ONLY THIS SECTION` no final deve ser alterado.
- **LICENSE** — licença MIT.

### Início rápido

1. Abra `master_prompt.md`.
2. Copie o prompt inteiro para o sistema de IA que deseja usar.
3. Vá até o bloco `USER INPUT — EDIT ONLY THIS SECTION` no final.
4. Defina idioma de saída, nível do público, tamanho do relatório, profundidade da análise, foco prioritário, formato e instruções especiais.
5. Envie o PDF do artigo. Se disponíveis, adicione suplementos, figuras originais, dados brutos, blots sem corte, arquivos-fonte de microscopia ou artigos relacionados.
6. Inicie a análise.

Configuração geral recomendada:

```text
OUTPUT_LANGUAGE = [Portuguese]
AUDIENCE = [Professional]
OUTPUT_LENGTH = [Detailed]
ANALYSIS_DEPTH = [Deep]
PRIORITY_FOCUS = [All areas]
OUTPUT_FORMAT = [Structured forensic report]
SPECIAL_INSTRUCTIONS = [None]
MATERIALS = [Analyze the uploaded paper and all accompanying files. Use DOI/URL and external sources when available.]
```

### Para uma análise mais forte de imagens e metadados

Um PDF de revista é suficiente para triagem geral, mas não é ideal para análise forense de imagem de alta confiança. Sempre que possível, forneça também:

- figuras originais em TIFF/PNG/JPEG;
- western blots ou géis sem corte;
- exportações brutas de microscopia ou arquivos nativos do instrumento;
- figuras suplementares e metadados de aquisição;
- conjuntos de dados brutos e saídas de análise;
- artigos relacionados quando a comparação entre publicações for relevante.

Se apenas o PDF estiver disponível, o relatório deve limitar explicitamente suas conclusões às evidências realmente suportadas por esse arquivo.

### Como interpretar o relatório

Os achados são classificados de **Level 0** a **Level 4**:

- **Level 0:** nenhuma preocupação significativa detectada;
- **Level 1:** sinal fraco com explicações benignas plausíveis;
- **Level 2:** inconsistência material reproduzível;
- **Level 3:** preocupação forense forte que requer revisão especializada;
- **Level 4:** problema de integridade corroborado por uma fonte externa autorizada.

Level 2 ou Level 3 **não** significa que houve má conduta. O nível de confiança se refere à confiabilidade da observação, não à intenção do autor.

### Uso recomendado

Use este projeto para triagem, preparação de revisão por pares, análise de integridade, verificação de fontes e priorização do que deve ser revisado por uma pessoa qualificada. Antes de decisões com consequências, confirme independentemente os achados importantes e obtenha materiais-fonte originais sempre que possível.

<p align="right"><a href="#top">↑ Voltar ao menu de idiomas</a></p>

---

<a id="lang-ar"></a>
## العربية

### ما هذا المشروع؟

يحتوي هذا المستودع على موجّه رئيسي قابل لإعادة الاستخدام، صُمّم لتحويل نظام ذكاء اصطناعي متقدم إلى **مدقق جنائي للأوراق الأكاديمية ونزاهة البحث العلمي**. وهو موجه للباحثين والمحررين والمحكّمين والصحفيين والطلاب والمتخصصين في نزاهة البحث الذين يحتاجون إلى فحص أولي منظم للأبحاث والملفات المرتبطة بها.

يعتمد الموجّه على منهج يضع الأدلة أولاً. فهو يعطي الأولوية لـ **الأدلة القابلة للملاحظة، وإمكانية إعادة الفحص، والتصريح بعدم اليقين، والبحث عن تفسيرات بديلة، والتحقق الخارجي، والمراجعة البشرية**. ولا يتعامل مع أي نمط مريب تلقائياً على أنه دليل على الاحتيال أو التزوير أو اختلاق البيانات أو الانتحال أو سوء السلوك المتعمد.

### ما الذي يمكنه فحصه؟

بحسب الملفات والأدوات المتاحة لنظام الذكاء الاصطناعي، يمكن للموجّه تحليل:

- التناقضات الداخلية وعدم الاتساق بين المنهج والنتائج؛
- التناقضات في أحجام العينات والنسب المئوية وقيم p وفترات الثقة وغيرها من الإحصاءات؛
- إعادة الاستخدام المريبة للأشكال أو اللوحات أو أجزاء الصور؛
- مؤشرات محتملة على الاستنساخ أو الدمج أو copy-move أو إعادة أخذ العينات أو الترقيع أو غيرها من التعديلات الرقمية؛
- الصور العلمية التي قد تكون مولّدة أو معدّلة بالذكاء الاصطناعي؛
- بيانات PDF الوصفية وبيانات الصور الأصلية، بما في ذلك EXIF/XMP عند توفرها؛
- DOI والمراجع والاستشهادات والتصحيحات وسحب الأبحاث وإشعارات الناشرين؛
- عدم الاتساق في الموافقات الأخلاقية وتسجيل الدراسة والتسلسل الزمني والانتماءات ومصدر البيانات؛
- أنماط مصانع الأوراق العلمية أو التلاعب المنهجي بالنشر؛
- أوجه التشابه بين عدة أبحاث في الصور أو النصوص أو الجداول أو الرسوم أو التسلسلات الرقمية.

كما يفرض الموجّه على النظام البحث عن أدلة **تعارض** تفسير سوء السلوك، واختبار أقوى النتائج نقدياً قبل عرضها.

### ما الذي لا يستطيع ضمانه؟

هذا الموجّه لا يجعل الذكاء الاصطناعي معصوماً من الخطأ ولا يحل محل المختبر أو التحقيق التحريري أو الخبير الجنائي. قد تكون صور PDF مضغوطة، وقد تكون البيانات الوصفية محذوفة، وقد تكون الجداول ناقصة، وقد لا تتوفر البيانات الخام أصلاً. ومن دون الوصول إلى الويب لا يمكن التحقق خارجياً من DOI أو السحب أو الاستشهادات أو إشعارات الناشرين. ومن دون أدوات جنائية للصور لا يجوز للنظام الادعاء بأنه أجرى تحليلاً على مستوى البكسل.

وجود شذوذ لا يثبت القصد. وجود بيانات Photoshop الوصفية لا يثبت التزوير. غياب البيانات الوصفية لا يثبت التلاعب. نتيجة كاشف الذكاء الاصطناعي لا تثبت أن الصورة مولّدة بالذكاء الاصطناعي. وبالمثل، عدم اكتشاف مشكلة لا يثبت أن البحث أصيل أو خالٍ من الأخطاء أو من مشكلات النزاهة.

### بنية المستودع

```text
academic-paper-forensic-auditor/
├── README.md
├── master_prompt.md
└── LICENSE
```

- **README.md** — توثيق كامل للمشروع بـ 12 لغة.
- **master_prompt.md** — الموجّه الرئيسي الكامل. في الاستخدام العادي لا يلزم تعديل سوى قسم `USER INPUT — EDIT ONLY THIS SECTION` في النهاية.
- **LICENSE** — رخصة MIT.

### البدء السريع

1. افتح `master_prompt.md`.
2. انسخ الموجّه بالكامل إلى نظام الذكاء الاصطناعي الذي تريد استخدامه.
3. انتقل إلى قسم `USER INPUT — EDIT ONLY THIS SECTION` في الأسفل.
4. حدّد لغة الإخراج ومستوى الجمهور وطول التقرير وعمق التحليل والأولوية وتنسيق الإخراج والتعليمات الخاصة.
5. ارفع ملف PDF. وإن توفرت، أضف الملفات التكميلية والصور الأصلية والبيانات الخام وblots غير المقصوصة وملفات المجهر الأصلية أو الأبحاث ذات الصلة.
6. ابدأ التحليل.

إعداد عام مقترح:

```text
OUTPUT_LANGUAGE = [Arabic]
AUDIENCE = [Professional]
OUTPUT_LENGTH = [Detailed]
ANALYSIS_DEPTH = [Deep]
PRIORITY_FOCUS = [All areas]
OUTPUT_FORMAT = [Structured forensic report]
SPECIAL_INSTRUCTIONS = [None]
MATERIALS = [Analyze the uploaded paper and all accompanying files. Use DOI/URL and external sources when available.]
```

### للحصول على تحليل أقوى للصور والبيانات الوصفية

يكفي ملف PDF المنشور لإجراء فحص عام، لكنه ليس مثالياً لتحليل جنائي عالي الثقة للصور. كلما أمكن، وفّر أيضاً:

- ملفات TIFF/PNG/JPEG الأصلية للأشكال؛
- western blots أو gels غير المقصوصة؛
- مخرجات المجهر الخام أو الملفات الأصلية للجهاز؛
- الأشكال التكميلية وبيانات الالتقاط الوصفية؛
- مجموعات البيانات الخام ومخرجات التحليل؛
- الأبحاث المرتبطة إذا كانت المقارنة بين الأوراق مطلوبة.

إذا كان المتاح هو PDF فقط، فيجب أن يقيّد التقرير استنتاجاته صراحة بما يمكن دعمه فعلاً من هذا الملف.

### كيف تُقرأ النتائج؟

تُصنّف النتائج من **Level 0** إلى **Level 4**:

- **Level 0:** لم تُكتشف مشكلة ذات معنى؛
- **Level 1:** إشارة ضعيفة مع تفسيرات سليمة محتملة؛
- **Level 2:** تناقض جوهري يمكن إعادة التحقق منه؛
- **Level 3:** قلق جنائي قوي يتطلب مراجعة خبير؛
- **Level 4:** مشكلة نزاهة تؤكدها جهة خارجية موثوقة.

لا يعني Level 2 أو Level 3 أن سوء السلوك قد وقع. مستوى الثقة يتعلق بصحة الملاحظة نفسها، وليس بنية المؤلف.

### الاستخدام الموصى به

استخدم هذا المشروع للفرز الأولي، والتحضير للتحكيم، وفحص نزاهة البحث، والتحقق من المصادر، وتحديد ما ينبغي أن يراجعه خبير بشري بعد ذلك. وقبل اتخاذ قرارات ذات عواقب، تحقّق من النتائج المهمة بشكل مستقل واحصل على الملفات الأصلية كلما أمكن.

<p align="right"><a href="#top">↑ العودة إلى قائمة اللغات</a></p>

---

<a id="lang-zh-cn"></a>
## 简体中文

### 这个项目是什么？

本仓库包含一个可重复使用的主提示词，用于将具备较强能力的 AI 系统配置为 **学术论文取证与科研诚信审查助手**。它面向研究人员、编辑、同行评审者、记者、学生以及科研诚信专业人员，用于对论文及其相关文件进行结构化的初步审查。

该提示词坚持“证据优先”。它优先考虑 **可观察证据、可复现性、不确定性的明确说明、替代性解释、外部核验以及人工复核**。任何可疑模式都不会被自动视为欺诈、伪造、捏造、抄袭或故意科研不端的证明。

### 它可以检查什么？

具体能力取决于 AI 系统可访问的文件和工具，可能包括：

- 论文内部矛盾以及方法与结果之间的不一致；
- 样本量、百分比、p 值、置信区间及其他统计数据的不一致；
- 图、分面或局部图像的可疑重复使用；
- 可能的克隆、拼接、copy-move、重采样、局部修补或其他数字编辑痕迹；
- 可能由 AI 生成或经 AI 修改的科学图像；
- PDF 和原始图像的元数据，包括可用时的 EXIF/XMP；
- DOI、引用、参考文献、更正、撤稿及出版方公告；
- 伦理审批、研究注册、时间线、机构归属和来源信息的不一致；
- 论文工厂或系统性出版操纵模式；
- 在提供多篇论文时，比较图像、文本、表格、图形或数字序列之间的相似性。

提示词还要求 AI 主动寻找**不支持科研不端解释的证据**，并在输出前对最强的异常发现进行反向质疑。

### 它不能保证什么？

该提示词不会让 AI 变得绝对可靠，也不能替代实验室、期刊调查或专业取证人员。PDF 中的图片可能已经压缩，元数据可能被移除，表格可能不完整，也可能根本没有原始数据。没有网络访问时，AI 无法从外部核验 DOI、撤稿、引用或出版方公告。没有图像取证工具时，AI 不应声称自己完成了像素级取证分析。

异常并不等于主观故意。Photoshop 元数据并不证明伪造。缺少元数据并不证明图像被操纵。AI 检测器的分数并不能证明图像由 AI 生成。同样，未检测出问题也不能证明论文一定真实、无错误或不存在科研诚信问题。

### 仓库结构

```text
academic-paper-forensic-auditor/
├── README.md
├── master_prompt.md
└── LICENSE
```

- **README.md** — 12 种语言的完整项目文档。
- **master_prompt.md** — 完整主提示词。通常只需修改末尾的 `USER INPUT — EDIT ONLY THIS SECTION` 区域。
- **LICENSE** — MIT 许可证。

### 快速开始

1. 打开 `master_prompt.md`。
2. 将完整提示词复制到你要使用的 AI 系统中。
3. 找到文件底部的 `USER INPUT — EDIT ONLY THIS SECTION` 区域。
4. 设置输出语言、读者水平、报告长度、分析深度、优先关注领域、输出格式以及特殊要求。
5. 上传论文 PDF。若有条件，也请提供补充材料、原始图像、原始数据、未裁剪的 blot、显微镜源文件或相关论文。
6. 开始分析。

推荐的通用配置：

```text
OUTPUT_LANGUAGE = [Simplified Chinese]
AUDIENCE = [Professional]
OUTPUT_LENGTH = [Detailed]
ANALYSIS_DEPTH = [Deep]
PRIORITY_FOCUS = [All areas]
OUTPUT_FORMAT = [Structured forensic report]
SPECIAL_INSTRUCTIONS = [None]
MATERIALS = [Analyze the uploaded paper and all accompanying files. Use DOI/URL and external sources when available.]
```

### 如何获得更强的图像和元数据分析？

期刊 PDF 足以进行广泛筛查，但并不适合高置信度的图像取证。若可能，请同时提供：

- 原始 TIFF/PNG/JPEG 图像；
- 未裁剪的 western blot 或 gel；
- 原始显微镜导出文件或仪器原生图像文件；
- 补充图和采集元数据；
- 原始数据集和分析输出；
- 在需要跨论文比较时提供相关论文。

如果只有 PDF，报告应明确把结论限制在该 PDF 能够支持的证据范围内。

### 如何理解报告？

发现项按 **Level 0** 到 **Level 4** 分类：

- **Level 0：** 未发现有意义的异常；
- **Level 1：** 弱信号，存在合理的无害解释；
- **Level 2：** 可复现的实质性不一致；
- **Level 3：** 较强的取证关注点，需要专家复核；
- **Level 4：** 已被权威外部来源证实的科研诚信问题。

Level 2 或 Level 3 **不等于**已经发生科研不端。置信度标签表示对“观察本身是否正确”的信心，而不是对作者主观意图的判断。

### 推荐用途

建议将本项目用于初步筛查、同行评审准备、科研诚信审查、来源核验以及确定后续人工复核优先级。对于可能产生重要后果的决定，应独立核验关键发现，并尽可能取得原始源文件。

<p align="right"><a href="#top">↑ 返回语言菜单</a></p>

---

<a id="lang-zh-tw"></a>
## 繁體中文

### 這個專案是什麼？

本儲存庫包含一個可重複使用的主提示詞，用於將具備較強能力的 AI 系統設定為 **學術論文鑑識與研究誠信審查助手**。它適用於研究人員、編輯、同儕審查者、記者、學生以及研究誠信專業人士，用來對論文及相關檔案進行結構化的初步檢視。

此提示詞採取明確的「證據優先」原則。它優先考慮 **可觀察證據、可重現性、不確定性的明確說明、替代性解釋、外部核驗與人工複核**。任何可疑模式都不會被自動視為詐欺、偽造、捏造、抄襲或故意研究不端的證明。

### 它可以檢查什麼？

實際能力取決於 AI 系統可取得的檔案與工具，可能包括：

- 論文內部矛盾，以及方法與結果之間的不一致；
- 樣本數、百分比、p 值、信賴區間與其他統計數據的不一致；
- 圖、分圖或局部影像的可疑重複使用；
- 可能的複製、拼接、copy-move、重新取樣、局部修補或其他數位編輯痕跡；
- 可能由 AI 產生或經 AI 修改的科學影像；
- PDF 與原始影像的 metadata，包括可取得時的 EXIF/XMP；
- DOI、引用、參考文獻、更正、撤稿與出版商公告；
- 倫理審查、研究註冊、時間線、機構隸屬與來源資訊的不一致；
- 論文工廠或系統性出版操縱模式；
- 在提供多篇論文時，比較影像、文字、表格、圖表或數值序列的相似性。

提示詞也要求 AI 主動尋找**不支持研究不端解釋的證據**，並在輸出前對最強的異常發現進行反向檢驗。

### 它不能保證什麼？

此提示詞不會讓 AI 變得絕對可靠，也不能取代實驗室、期刊調查或專業鑑識人員。PDF 內的圖片可能已被壓縮，metadata 可能被移除，表格可能不完整，也可能根本沒有原始資料。沒有網路存取時，AI 無法從外部核驗 DOI、撤稿、引用或出版商公告。沒有影像鑑識工具時，AI 不應聲稱自己做過像素層級的鑑識分析。

異常不等於故意。Photoshop metadata 不代表影像被偽造。缺少 metadata 不代表影像遭操縱。AI 偵測器的分數不能證明影像由 AI 產生。同樣地，沒有偵測到問題也不能證明論文必然真實、完全無誤或不存在研究誠信問題。

### 儲存庫結構

```text
academic-paper-forensic-auditor/
├── README.md
├── master_prompt.md
└── LICENSE
```

- **README.md** — 12 種語言的完整專案文件。
- **master_prompt.md** — 完整主提示詞。一般情況下只需要修改最下方的 `USER INPUT — EDIT ONLY THIS SECTION` 區塊。
- **LICENSE** — MIT 授權條款。

### 快速開始

1. 開啟 `master_prompt.md`。
2. 將完整提示詞複製到你要使用的 AI 系統中。
3. 前往檔案底部的 `USER INPUT — EDIT ONLY THIS SECTION` 區塊。
4. 設定輸出語言、讀者程度、報告長度、分析深度、優先關注項目、輸出格式與特殊指示。
5. 上傳論文 PDF。若可取得，也請提供補充材料、原始圖像、原始資料、未裁切 blot、顯微鏡來源檔或相關論文。
6. 開始分析。

建議的通用設定：

```text
OUTPUT_LANGUAGE = [Traditional Chinese]
AUDIENCE = [Professional]
OUTPUT_LENGTH = [Detailed]
ANALYSIS_DEPTH = [Deep]
PRIORITY_FOCUS = [All areas]
OUTPUT_FORMAT = [Structured forensic report]
SPECIAL_INSTRUCTIONS = [None]
MATERIALS = [Analyze the uploaded paper and all accompanying files. Use DOI/URL and external sources when available.]
```

### 如何取得更強的影像與 metadata 分析？

期刊 PDF 足以進行廣泛篩查，但不適合高可信度的影像鑑識。若可能，建議一併提供：

- 原始 TIFF/PNG/JPEG 圖像；
- 未裁切的 western blot 或 gel；
- 原始顯微鏡匯出檔或儀器原生影像檔；
- 補充圖與影像取得 metadata；
- 原始資料集與分析輸出；
- 在需要跨論文比較時提供相關論文。

若只有 PDF，報告應明確把結論限制在該 PDF 可支持的證據範圍內。

### 如何理解報告？

發現項目依 **Level 0** 到 **Level 4** 分類：

- **Level 0：** 未發現有意義的異常；
- **Level 1：** 弱訊號，存在合理的無害解釋；
- **Level 2：** 可重現的實質性不一致；
- **Level 3：** 較強的鑑識疑點，需要專家複核；
- **Level 4：** 已由具權威性的外部來源證實之研究誠信問題。

Level 2 或 Level 3 **不代表**已經發生研究不端。信心標籤表示對「觀察本身是否正確」的信心，而不是對作者主觀意圖的判斷。

### 建議用途

建議將此專案用於初步篩查、同儕審查準備、研究誠信檢視、來源核驗以及安排後續人工複核的優先順序。對於可能產生重大後果的決定，應獨立核驗重要發現，並盡可能取得原始來源檔案。

<p align="right"><a href="#top">↑ 返回語言選單</a></p>

---

<a id="lang-ko"></a>
## 한국어

### 이 프로젝트는 무엇인가요?

이 저장소에는 고성능 AI 시스템을 **학술 논문 포렌식 및 연구진실성 감사 도구**처럼 활용할 수 있도록 설계된 재사용 가능한 마스터 프롬프트가 들어 있습니다. 연구자, 편집자, 동료심사자, 기자, 학생, 연구진실성 담당자가 논문과 관련 파일을 구조적으로 1차 검토할 때 사용할 수 있습니다.

이 프롬프트는 의도적으로 증거 우선 원칙을 따릅니다. **관찰 가능한 증거, 재현 가능성, 불확실성의 명시, 대안적 설명, 외부 검증, 인간 전문가의 재검토**를 우선합니다. 의심스러운 패턴을 자동으로 사기, 위조, 조작, 표절 또는 고의적 연구부정의 증거로 간주하지 않습니다.

### 무엇을 분석할 수 있나요?

AI 시스템이 사용할 수 있는 파일과 도구에 따라 다음 항목을 점검할 수 있습니다.

- 논문 내부의 모순과 방법-결과 간 불일치;
- 표본 수, 백분율, p값, 신뢰구간 및 기타 통계의 불일치;
- 그림, 패널 또는 이미지 영역의 의심스러운 재사용;
- 복제, 스플라이싱, copy-move, 리샘플링, 패칭 등 디지털 편집 가능성;
- AI로 생성되었거나 AI로 수정되었을 가능성이 있는 과학 이미지;
- 가능한 경우 EXIF/XMP를 포함한 PDF 및 원본 이미지 메타데이터;
- DOI, 인용, 참고문헌, 정정, 철회 및 출판사 공지;
- 윤리 승인, 연구 등록, 일정, 소속 및 provenance의 불일치;
- paper mill 또는 체계적 출판 조작 패턴;
- 여러 논문이 제공된 경우 이미지, 텍스트, 표, 그래프 또는 숫자 배열의 논문 간 유사성.

또한 프롬프트는 연구부정이라는 해석에 **반대되는 증거**도 적극적으로 찾고, 가장 강한 이상 징후를 최종 보고 전에 반박 관점에서 다시 검토하도록 요구합니다.

### 무엇을 보장하지 못하나요?

이 프롬프트가 AI를 무오류 시스템으로 만들거나 실험실, 학술지 조사, 포렌식 전문가를 대체하는 것은 아닙니다. PDF 이미지가 압축되어 있을 수 있고, 메타데이터가 제거되어 있을 수 있으며, 표가 불완전하거나 원시 데이터가 전혀 제공되지 않을 수 있습니다. 웹 접근이 없으면 DOI, 철회, 인용 또는 출판사 공지를 외부에서 검증할 수 없습니다. 이미지 포렌식 도구가 없다면 픽셀 수준 분석을 수행했다고 주장해서는 안 됩니다.

이상 징후는 의도를 증명하지 않습니다. Photoshop 메타데이터는 위조의 증거가 아닙니다. 메타데이터가 없다는 사실도 조작의 증거가 아닙니다. AI 탐지기 점수는 이미지가 AI로 생성되었다는 증거가 아닙니다. 반대로 문제가 발견되지 않았다고 해서 논문이 진짜이거나 오류가 없거나 연구진실성 문제가 없다는 뜻도 아닙니다.

### 저장소 구조

```text
academic-paper-forensic-auditor/
├── README.md
├── master_prompt.md
└── LICENSE
```

- **README.md** — 12개 언어로 제공되는 전체 프로젝트 문서.
- **master_prompt.md** — 전체 마스터 프롬프트. 일반적으로 마지막의 `USER INPUT — EDIT ONLY THIS SECTION` 블록만 수정하면 됩니다.
- **LICENSE** — MIT License.

### 빠른 시작

1. `master_prompt.md`를 엽니다.
2. 전체 프롬프트를 사용할 AI 시스템에 복사합니다.
3. 문서 하단의 `USER INPUT — EDIT ONLY THIS SECTION` 블록으로 이동합니다.
4. 출력 언어, 대상 독자 수준, 보고서 길이, 분석 깊이, 우선 분야, 출력 형식, 추가 지시사항을 설정합니다.
5. 논문 PDF를 업로드합니다. 가능하면 보충자료, 원본 그림, 원시 데이터, 자르지 않은 blot, 현미경 원본 파일 또는 관련 논문도 함께 제공합니다.
6. 분석을 시작합니다.

권장 일반 설정:

```text
OUTPUT_LANGUAGE = [Korean]
AUDIENCE = [Professional]
OUTPUT_LENGTH = [Detailed]
ANALYSIS_DEPTH = [Deep]
PRIORITY_FOCUS = [All areas]
OUTPUT_FORMAT = [Structured forensic report]
SPECIAL_INSTRUCTIONS = [None]
MATERIALS = [Analyze the uploaded paper and all accompanying files. Use DOI/URL and external sources when available.]
```

### 이미지 및 메타데이터 분석을 더 강하게 하려면

학술지 PDF만으로도 전반적인 스크리닝은 가능하지만, 높은 신뢰도의 이미지 포렌식에는 충분하지 않을 수 있습니다. 가능하면 다음 자료를 함께 제공하는 것이 좋습니다.

- 원본 TIFF/PNG/JPEG 그림;
- 자르지 않은 western blot 또는 gel;
- 원시 현미경 출력 또는 장비 고유 형식의 이미지 파일;
- 보충 그림과 획득 메타데이터;
- 원시 데이터셋과 분석 출력;
- 논문 간 비교가 필요한 경우 관련 논문.

PDF만 사용할 수 있는 경우 보고서는 반드시 해당 PDF에서 실제로 뒷받침할 수 있는 범위로 결론을 제한해야 합니다.

### 보고서 해석 방법

발견 사항은 **Level 0**부터 **Level 4**까지 분류됩니다.

- **Level 0:** 의미 있는 우려 사항 없음;
- **Level 1:** 합리적인 정상 설명이 가능한 약한 신호;
- **Level 2:** 재현 가능한 실질적 불일치;
- **Level 3:** 전문가 검토가 필요한 강한 포렌식 우려;
- **Level 4:** 권위 있는 외부 출처로 확인된 연구진실성 문제.

Level 2 또는 Level 3은 연구부정이 실제로 발생했다는 뜻이 **아닙니다**. 신뢰도 표시는 관찰 자체가 정확하다는 확신을 의미하며, 저자의 의도에 대한 판단을 뜻하지 않습니다.

### 권장 사용 방식

이 프로젝트는 초기 분류, 동료심사 준비, 연구진실성 스크리닝, 출처 검증, 그리고 어떤 항목을 인간 전문가가 우선 확인해야 하는지 정하는 데 활용할 수 있습니다. 중요한 결정에 사용하기 전에는 핵심 발견을 독립적으로 검증하고 가능하면 원본 자료를 확보하십시오.

<p align="right"><a href="#top">↑ 언어 메뉴로 돌아가기</a></p>

---

<a id="lang-ja"></a>
## 日本語

### このプロジェクトとは？

このリポジトリには、高性能な AI システムを **学術論文フォレンジックおよび研究公正監査アシスタント** として利用するための再利用可能なマスタープロンプトが含まれています。研究者、編集者、査読者、ジャーナリスト、学生、研究公正の専門家が、論文および関連ファイルを体系的に一次確認するために設計されています。

このプロンプトは意図的に「証拠優先」の方針を採用しています。**観察可能な証拠、再現可能性、不確実性の明示、代替説明、外部検証、人間による確認**を優先します。疑わしいパターンを自動的に、不正、改ざん、捏造、盗用、または意図的な研究不正の証拠として扱うことはありません。

### 何を調べられますか？

利用できるファイルやツールに応じて、以下のような項目を分析できます。

- 論文内部の矛盾や方法と結果の不一致；
- サンプル数、割合、p値、信頼区間、その他の統計値の不整合；
- 図、パネル、画像領域の不自然な再利用；
- クローン、スプライス、copy-move、リサンプリング、パッチ処理などのデジタル編集の可能性；
- AI により生成または変更された可能性のある科学画像；
- 利用可能な場合の EXIF/XMP を含む PDF・元画像のメタデータ；
- DOI、引用、参考文献、訂正、撤回、出版社からの告知；
- 倫理審査、研究登録、時系列、所属、provenance の不整合；
- paper mill や体系的な出版操作のパターン；
- 複数論文が提供された場合の画像、文章、表、グラフ、数値列の類似性。

また、研究不正という解釈に**反する証拠**も積極的に探し、最も強い所見については最終出力前に反証的な再検討を行うよう求めます。

### 何を保証できませんか？

このプロンプトによって AI が無謬になるわけではなく、研究室、出版社による調査、あるいは専門的なフォレンジック鑑定を代替するものでもありません。PDF 内の画像は圧縮されている場合があり、メタデータが削除されていることもあります。表が不完全だったり、生データが提供されていない場合もあります。ウェブアクセスがなければ DOI、撤回、引用、出版社の告知を外部検証できません。画像フォレンジック用のツールがなければ、ピクセルレベルの解析を実施したと主張してはいけません。

異常は意図を証明しません。Photoshop のメタデータは改ざんの証拠ではありません。メタデータがないことも操作の証拠ではありません。AI 検出器のスコアは AI 生成の証拠ではありません。同様に、問題が検出されなかったからといって、論文が真正・無誤・研究公正上問題なしと証明されたわけではありません。

### リポジトリ構成

```text
academic-paper-forensic-auditor/
├── README.md
├── master_prompt.md
└── LICENSE
```

- **README.md** — 12言語で提供される完全なプロジェクト文書。
- **master_prompt.md** — 完全版のマスタープロンプト。通常は末尾の `USER INPUT — EDIT ONLY THIS SECTION` ブロックのみ編集します。
- **LICENSE** — MIT License。

### クイックスタート

1. `master_prompt.md` を開きます。
2. プロンプト全体を使用する AI システムにコピーします。
3. 末尾の `USER INPUT — EDIT ONLY THIS SECTION` ブロックへ移動します。
4. 出力言語、対象読者、レポート長、分析深度、重点項目、出力形式、特別指示を設定します。
5. 論文 PDF をアップロードします。可能であれば、補足資料、元画像、生データ、未切り抜き blot、顕微鏡の元ファイル、関連論文も提供します。
6. 分析を開始します。

推奨される一般設定：

```text
OUTPUT_LANGUAGE = [Japanese]
AUDIENCE = [Professional]
OUTPUT_LENGTH = [Detailed]
ANALYSIS_DEPTH = [Deep]
PRIORITY_FOCUS = [All areas]
OUTPUT_FORMAT = [Structured forensic report]
SPECIAL_INSTRUCTIONS = [None]
MATERIALS = [Analyze the uploaded paper and all accompanying files. Use DOI/URL and external sources when available.]
```

### 画像・メタデータ分析を強化するには

学術誌の PDF だけでも広いスクリーニングは可能ですが、高信頼度の画像フォレンジックには理想的ではありません。可能であれば、次の資料も提供してください。

- 元の TIFF/PNG/JPEG 画像；
- 未切り抜きの western blot または gel；
- 顕微鏡の生出力または装置固有形式の画像ファイル；
- 補足図と取得メタデータ；
- 生データセットと解析出力；
- 論文間比較が必要な場合は関連論文。

PDF しかない場合、レポートはその PDF から実際に裏付けられる範囲に結論を明示的に限定する必要があります。

### レポートの読み方

所見は **Level 0** から **Level 4** に分類されます。

- **Level 0：** 意味のある懸念なし；
- **Level 1：** 妥当な無害な説明があり得る弱いシグナル；
- **Level 2：** 再現可能な実質的不整合；
- **Level 3：** 専門家による確認が必要な強いフォレンジック上の懸念；
- **Level 4：** 権威ある外部情報によって裏付けられた研究公正上の問題。

Level 2 または Level 3 は研究不正が発生したことを意味しません。信頼度ラベルは観察そのものの確からしさを表し、著者の意図を示すものではありません。

### 推奨用途

本プロジェクトは、初期トリアージ、査読準備、研究公正スクリーニング、情報源の確認、人間の専門家が次に確認すべき項目の優先順位付けに利用してください。重要な判断に用いる前には主要所見を独立に検証し、可能な限り元データや元ファイルを入手してください。

<p align="right"><a href="#top">↑ 言語メニューに戻る</a></p>

---

## License

Released under the **MIT License**. See [`LICENSE`](LICENSE) for the full text.

**Author:** 𝓐.𝓒.𝓑
