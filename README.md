# Academic Paper Forensic & Research Integrity Auditor

<a id="languages"></a>
<a id="top"></a>

[English](#lang-en) · [Türkçe](#lang-tr) · [Deutsch](#lang-de) · [Français](#lang-fr) · [Español](#lang-es) · [Italiano](#lang-it) · [Português](#lang-pt) · [العربية](#lang-ar) · [简体中文](#lang-zh-cn) · [繁體中文](#lang-zh-tw) · [한국어](#lang-ko) · [日本語](#lang-ja)

<p align="center">
  <a href="https://github.com/IACBI/academic-paper-forensic-auditor/releases/tag/v.0.0.3"><img alt="Version: v.0.0.3" src="https://img.shields.io/badge/version-v.0.0.3-2563eb?style=flat"></a>
  <a href="LICENSE"><img alt="License: MIT" src="https://img.shields.io/badge/license-MIT-16a34a?style=flat"></a>
  <a href="https://github.com/IACBI/academic-paper-forensic-auditor/actions/workflows/validate.yml"><img alt="CI status" src="https://img.shields.io/github/actions/workflow/status/IACBI/academic-paper-forensic-auditor/validate.yml?branch=main&amp;event=push&amp;label=checks&amp;style=flat"></a>
</p>

---

<a id="lang-en"></a>
## English

### Purpose and scope

Academic Paper Forensic & Research Integrity Auditor helps researchers, reviewers, editors, students and research-integrity professionals conduct a structured first examination of scholarly work. Its central resource is a reusable protocol that you give to your preferred AI assistant. The review follows the claims, methods and evidence in the material, so it can support work across disciplines rather than impose one experimental checklist on every field.

Depending on the evidence and tools available, a review can examine arguments and proofs, methods/results consistency, numerical claims, computational evaluation, source attribution, figures, provenance, references, notices and comparisons between papers. The agent must distinguish a reporting gap, a methodological limitation, scholarly disagreement and a specific integrity concern. For a material finding, it identifies the exact location, shows how to reproduce the observation, tests a plausible benign explanation and explains what a human should verify next.

This is AI-assisted screening. Consequential decisions require independent human review. An anomaly does not establish misconduct or intent, and an absence of findings does not establish authenticity. The protocol supports judgment; it does not replace a domain expert, a forensic laboratory or an institutional investigation.

### Start with the assistant you already use

1. Download the [prompt package][download-prompt] or open [master_prompt.md](master_prompt.md). Give the assistant the full protocol by pasting it or attaching a readable copy. For a smaller first pass, use the request in [QUICKSTART.md](QUICKSTART.md).
2. Supply the paper or relevant excerpts and any supporting material you are authorized to share. Identify the version and the pages, figures, arguments or questions you want examined. If attachments cannot be read, paste targeted excerpts and ask for an explicitly excerpt-only review.
3. Set the output language, audience, length and focus. In the full prompt, edit the bracketed values in `USER INPUT — EDIT ONLY THIS SECTION`; leave the review policy intact. The example below is a starting configuration, not evidence that files or tools are available.

```text
OUTPUT_LANGUAGE = [English]
RESEARCH_CONTEXT = [Identify the disciplines, methods and evidence in the supplied material.]
CAPABILITY_MODE = [Use observed capabilities; disclose unavailable checks.]
AUDIENCE = [Professional]
OUTPUT_LENGTH = [Detailed]
ANALYSIS_DEPTH = [Deep]
PRIORITY_FOCUS = [All applicable areas]
OUTPUT_FORMAT = [Structured forensic report]
SPECIAL_INSTRUCTIONS = [Give exact evidence locations, test benign explanations and identify the next human checks.]
MATERIALS = [List the supplied files or excerpts, their versions and the requested review scope.]
```

Choose `Short`, `Standard`, `Detailed` or `Exhaustive` for length, and `Beginner`, `General`, `Researcher`, `Professional` or `Expert` for audience. A focused request such as “check the proof assumptions” or “reconcile Table 2 with the Methods” is often more useful than an unbounded audit. If nothing assessable was supplied, the appropriate result is a request for material and insufficient evidence, not a clean bill of health.

`ANALYSIS_DEPTH` accepts `Standard`, `Deep` or `Maximum`: use them for the applicable core checks, a closer examination, or the broadest useful review supported by the available evidence and tools. More depth does not add unavailable capabilities. The remaining descriptive fields accept your own instructions: explain the research context, priorities, special requests and supplied materials, and set `OUTPUT_FORMAT` to the report style you need, such as an executive summary or technical report.

### Choose a delivery format and appropriate evidence

| Format | When to use it | What you need |
| --- | --- | --- |
| [Full prompt][download-prompt] | A thorough review in a text-capable assistant | The master protocol and readable research material |
| [Quick request](QUICKSTART.md) | Initial triage or a small context window | The copyable request and a bounded scope |
| [Standalone skill][download-skill] | Your host supports the open Agent Skills folder format | The complete `academic-paper-audit` folder, including linked resources |
| [Optional plugin][download-plugin] | Your host supports the packaged plugin format | A compatible loader; installation and discovery depend on the host |

Use one format per review. Plain-text use requires no Python, API key or provider integration. The [release page][release] includes all three archives and [SHA-256 checksums][checksums]. A matching checksum confirms downloaded bytes; it does not authenticate a research source.

Checks follow the actual method. Quantitative work may need denominator, sampling and uncertainty checks; qualitative work may need contextual quotations and an analytic trail; computational work may need data-split and execution checks. Formal work calls for assumptions, quantifiers and counterexamples; engineering for units, calibration and boundary conditions; archival work for editions, dates and transcription. Mixed methods, synthesis, conceptual and practice-based research need criteria suited to their claims. These are examples, not a closed list. P-values, preregistration, public raw data and a DOI are not universal requirements.

Supply original figures or source records when a question depends on them. A compressed PDF can support a bounded textual review without supporting pixel-level or metadata conclusions. Vision, web access and specialist tools extend what can be inspected, but their presence must be verified. The helpers supplied here do not perform OCR, image forensics, proof checking or automatic AI-image detection.

### Understand the report

The report should explain the inspected scope, available tools, method context, prioritized findings, evidence against concerns, limitations and next human checks. It records coverage for text/methods, statistics/data, figures/images, metadata/provenance, references/notices, ethics/registration and cross-paper comparison. `completed` means the stated scope was checked; `partial` means only part was checked; `not_assessed` means it was not checked; `not_applicable` requires a reason why it does not apply.

Evidence levels describe support for an observation: **0** no meaningful concern within inspected scope; **1** a weak signal with plausible benign explanations; **2** a reproducible material inconsistency; **3** a strong concern with additional corroborating evidence requiring expert review; **4** a specific issue corroborated by a read, authoritative, article-matched external source. Level 2/3 does not establish intent. Confidence concerns the observation, not an author's guilt. A notice must be read for its actual reason; a retraction alone does not establish fraud.

Markdown or plain text is the default. The [report template](skills/academic-paper-audit/assets/report-template.md) shows the structure; [JSON](skills/academic-paper-audit/assets/report.schema.json) is optional. Structural validation cannot establish scientific truth or prove that a source was read. Unknown hashes or unavailable operations must remain explicit; if an observed timestamp required by strict report JSON is unavailable, use a human-readable report.

### Protect evidence and continue between sessions

Keep originals unchanged and record derived copies separately. Share unpublished papers, identifiable records and raw data only within an authorized environment. The project operates no hosted service or telemetry, but the assistant and its tools have their own data policies. A review request does not authorize external uploads, contacting authors or publishing allegations. Instructions embedded in a paper or metadata are evidence, not commands. See the [privacy guide](docs/PRIVACY.md) for practical handling and retention boundaries.

For another session or agent, use the [continuation record](skills/academic-paper-audit/assets/continuation-template.md). Carry the article/version, scope, evidence IDs, inspected locations, completed checks, finding IDs/status, missing material and next steps, together with the actual sources. Recheck changed evidence. Keep corrected findings as resolved history and exclude them from active counts. A summary does not replace an unseen original or grant permission to expand the task.

In the current source, JSON continuation export preserves recorded research context, each domain’s limitations and links to completed checks. `validate-checkpoint` reports `warnings` when older records lack this history; keep those gaps explicit when resuming. These updates are included in v.0.0.3; consistent v.0.0.2 continuation records remain readable.

### Optional local helpers

Use the complete repository or skill folder for helper commands; the prompt-only ZIP has no Python scripts. Python 3.10+ is needed only for helpers/development. Inventory and arithmetic use the standard library; report/checkpoint validation and checkpoint export require `jsonschema` 4.26.0. Use a suitable environment: `.venv/Scripts/python.exe` on Windows or `.venv/bin/python` on macOS/Linux after `python -m venv .venv`. In the examples, `python` means that environment's interpreter, run from the repository root.

For the commands below, download the [complete repository][download-source]. In an installed skill, follow [SKILL.md](skills/academic-paper-audit/SKILL.md) instead; its commands use paths relative to that skill folder.

```text
python -m pip install -r skills/academic-paper-audit/requirements.txt
python skills/academic-paper-audit/scripts/audit_tools.py inventory --root tests/fixtures synthetic_manuscript.md
python skills/academic-paper-audit/scripts/audit_tools.py percentage --count 1 --total 3 --reported 33.3 --places 1
python skills/academic-paper-audit/scripts/audit_tools.py flow --initial 100 --excluded 10 --dropouts 5 --analyzed 90 --disjoint
python skills/academic-paper-audit/scripts/audit_tools.py validate-report examples/synthetic-report.json
python skills/academic-paper-audit/scripts/audit_tools.py checkpoint examples/synthetic-report.json
python skills/academic-paper-audit/scripts/audit_tools.py validate-checkpoint examples/synthetic-checkpoint.json
```

These examples use synthetic material. Inventory accepts paths relative to `--root` and reports byte sizes and SHA-256. The percentage check assumes ordinary unweighted counts and nearest rounding; flow assumes disjoint losses in the same population/timepoint. Neither calculation assigns an evidence level. Checkpoint export prints JSON to stdout; save it as UTF-8 when needed. Exit codes are 0 for successful computation/valid records, 1 for an invalid report/checkpoint, and 2 for input or dependency errors. An arithmetic mismatch is a successful calculation, not a software failure.

### Verification, support and license

The project has 81 behavior tests and a Windows/Ubuntu CI matrix for Python 3.10 and 3.14. Version v.0.0.2 corrects the Windows inventory timestamp comparison while preserving file-identity and change-detection checks. Quick, master and skill routes each passed 16 synthetic cases and 48 model-judged checks, including legitimate controls, insufficient evidence and a resolved finding. These are acceptance results, not measured scientific accuracy. Observed native-host tests and their failures are recorded in the validation guide; results apply only to those runs. macOS execution and expert performance across languages, modalities and disciplines remain unverified. The [validation guide](docs/VALIDATION.md) documents evidence, limits and reproduction steps.

For a reproducible problem, use the [bug form][issues] with a minimal synthetic or authorized shareable example. [Contributing](CONTRIBUTING.md) covers development and releases; [CHANGELOG.md](CHANGELOG.md) records changes. The project is available under the [MIT license](LICENSE). This language section is a complete user guide; the additional technical documents are maintained in English.

[↑ Back to top](#top)

---

<a id="lang-tr"></a>
## Türkçe

### Amaç ve kapsam

Academic Paper Forensic & Research Integrity Auditor; araştırmacıların, hakemlerin, editörlerin, öğrencilerin ve araştırma bütünlüğü uzmanlarının akademik çalışmaları sistemli biçimde ön incelemesine yardımcı olur. Temel kaynak, tercih ettiğiniz yapay zekâ ajanına verebileceğiniz bir inceleme protokolüdür. İnceleme, çalışmanın iddialarına, yöntemine ve kanıtlarına göre şekillenir; her araştırma alanına aynı deneysel kontrol listesini uygulamaz.

Sağlanan materyale ve mevcut araçlara bağlı olarak argümanlar, ispatlar, yöntem–sonuç uyumu, sayısal iddialar, hesaplamalı değerlendirmeler, kaynak aktarımı, görseller, köken bilgisi, atıflar, yayıncı bildirimleri ve çalışmalar arası benzerlikler incelenebilir. Raporlama eksiği, yöntemsel sınırlılık, akademik görüş ayrılığı ve somut bütünlük kaygısı ayrı ele alınır. Önemli bir bulguda tam konum gösterilir, gözlemin nasıl yeniden üretileceği açıklanır, makul bir zararsız açıklama sınanır ve insan incelemesinin sonraki adımı belirtilir.

Bu çalışma yapay zekâ destekli ön incelemedir. Önemli sonuçlara dayalı kararlar bağımsız insan doğrulaması gerektirir. Bir tutarsızlık suistimali veya kastı kanıtlamaz; bulgu çıkmaması da özgünlük belgesi değildir. Protokol uzman değerlendirmesini destekler; alan uzmanının, adli laboratuvarın veya kurumsal soruşturmanın yerini almaz.

### Kullandığınız ajanla başlayın

1. [Prompt paketini][download-prompt] indirin veya [master_prompt.md](master_prompt.md) dosyasını açın. Tam protokolü ajana yapıştırın ya da okunabilir dosya olarak ekleyin. Daha dar bir ilk inceleme için [QUICKSTART.md](QUICKSTART.md) içindeki isteği kullanabilirsiniz.
2. Makaleyi veya ilgili alıntıları ve paylaşmaya yetkili olduğunuz destekleyici materyali sağlayın. Sürümü, incelenecek sayfaları, görselleri, argümanları veya soruları belirtin. Ek dosya okunamıyorsa ilgili bölümleri yapıştırıp incelemeyi açıkça bu alıntılarla sınırlandırın.
3. Çıktı dilini, okuyucu düzeyini, uzunluğu ve odağı seçin. Tam promptun sonundaki `USER INPUT — EDIT ONLY THIS SECTION` bölümünde yalnız köşeli parantezlerin içini düzenleyin. Aşağıdaki örnek bir başlangıç ayarıdır; dosyaların veya araçların gerçekten mevcut olduğunu varsaymaz.

```text
OUTPUT_LANGUAGE = [Türkçe]
RESEARCH_CONTEXT = [Sağlanan materyalin alanlarını, yöntemlerini ve kanıt türlerini belirle.]
CAPABILITY_MODE = [Yalnız gözlemlenen yetenekleri kullan; yapılamayan kontrolleri açıkla.]
AUDIENCE = [Professional]
OUTPUT_LENGTH = [Detailed]
ANALYSIS_DEPTH = [Deep]
PRIORITY_FOCUS = [All applicable areas]
OUTPUT_FORMAT = [Structured forensic report]
SPECIAL_INSTRUCTIONS = [Kanıtın tam konumunu göster, zararsız açıklamaları sına ve sonraki insan kontrollerini belirt.]
MATERIALS = [Sağlanan dosyaları veya alıntıları, sürümlerini ve istenen inceleme kapsamını yaz.]
```

Uzunluk için `Short`, `Standard`, `Detailed`, `Exhaustive`; okuyucu için `Beginner`, `General`, `Researcher`, `Professional`, `Expert` seçenekleri vardır. “İspatın varsayımlarını kontrol et” veya “Tablo 2’yi yöntem bölümüyle karşılaştır” gibi somut bir kapsam incelemeyi daha kullanışlı kılar. Değerlendirilebilir materyal yoksa uygun sonuç, materyal istemek ve kanıtın yetersiz olduğunu belirtmektir.

`ANALYSIS_DEPTH` için `Standard`, `Deep` veya `Maximum` seçebilirsiniz: sırasıyla uygulanabilir temel kontrolleri, daha ayrıntılı incelemeyi veya mevcut kanıt ve araçların desteklediği en geniş yararlı incelemeyi isteyin. Derinliği artırmak, ajana yeni araç kazandırmaz. Diğer açıklama alanlarını kendi ihtiyacınıza göre yazabilirsiniz: araştırma bağlamını, öncelikleri, özel istekleri ve sağlanan materyali belirtin; `OUTPUT_FORMAT` alanına yönetici özeti veya teknik rapor gibi istediğiniz çıktı biçimini yazın.

### Biçimi ve kanıtı ihtiyacınıza göre seçin

| Biçim | Ne zaman kullanılır? | Gerekenler |
| --- | --- | --- |
| [Tam prompt][download-prompt] | Metin okuyabilen bir ajanla ayrıntılı inceleme | Ana protokol ve okunabilir araştırma materyali |
| [Kısa istek](QUICKSTART.md) | İlk eleme veya sınırlı bağlam | Kopyalanabilir istek ve belirli bir kapsam |
| [Bağımsız skill][download-skill] | Ajan açık Agent Skills klasör biçimini destekliyorsa | Bağlı kaynaklarıyla birlikte `academic-paper-audit` klasörü |
| [İsteğe bağlı plugin][download-plugin] | Ajan paketlenmiş plugin biçimini destekliyorsa | Uyumlu bir yükleyici; kurulum ve keşif ajana bağlıdır |

Bir incelemede tek dağıtım biçimi kullanın. Düz metinle başlamak için Python, API anahtarı veya sağlayıcı entegrasyonu gerekmez. [Sürüm sayfasında][release] üç paket ve [SHA-256 değerleri][checksums] bulunur. Eşleşen hash, indirilen baytları doğrular; araştırma kaynağının özgünlüğünü kanıtlamaz.

Kontroller yönteme göre seçilir. Nicel çalışmada payda, örnekleme ve belirsizlik; nitel çalışmada alıntının bağlamı ve analiz izi; hesaplamalı çalışmada veri ayrımı ve gerçekten çalıştırılan süreç önemlidir. Formal çalışmada varsayımlar, niceleyiciler ve karşıörnekler; mühendislikte birimler, kalibrasyon ve sınır koşulları; arşiv araştırmasında baskı, tarih ve transkripsiyon incelenir. Karma yöntem, sentez, kavramsal ve uygulama temelli araştırmalar kendi iddialarına uygun ölçütlerle ele alınır. Bunlar kapalı bir alan listesi değildir. P-değeri, ön kayıt, açık ham veri veya DOI her çalışma için zorunlu değildir.

Soru görsele veya kaynak kaydına dayanıyorsa mümkün olan en iyi özgün dosyayı sağlayın. Sıkıştırılmış bir PDF, metin incelemesine elverişli olsa da piksel veya metadata düzeyinde sonuç çıkarmaya yetmeyebilir. Görme, web ve uzman araçları ancak gerçekten kullanılabiliyorsa kapsama katkı sağlar. Bu projenin yardımcı kodu OCR, görsel adli inceleme, ispat doğrulama veya otomatik yapay zekâ görsel tespiti motoru değildir.

### Raporu nasıl yorumlamalısınız?

Rapor; kapsamı, kullanılan araçları, yöntem bağlamını, öncelikli bulguları, kaygılara karşı kanıtları, sınırlılıkları ve sonraki insan kontrollerini açıklar. Metin/yöntem, istatistik/veri, görsel, metadata/köken, kaynakça/bildirim, etik/kayıt ve çalışmalar arası karşılaştırma için kapsam kaydı tutulur. `completed` belirtilen kapsamın incelendiğini, `partial` kısmen incelendiğini, `not_assessed` incelenmediğini belirtir. `not_applicable` ancak uygulanamazlığın gerekçesi varsa kullanılır.

Kanıt düzeyleri gözlemin dayanağını anlatır: **0** incelenen kapsamda anlamlı kaygı yok; **1** makul zararsız açıklamaları olan zayıf sinyal; **2** yeniden üretilebilir önemli tutarsızlık; **3** ek doğrulayıcı kanıtla desteklenen ve uzman incelemesi gerektiren güçlü kaygı; **4** okunmuş, yetkili ve ilgili çalışmayla eşleşen dış kaynağın doğruladığı somut sorun. Düzey 2/3 kastı göstermez. Güven ifadesi gözleme ilişkindir; yazarın suçluluğuna değil. Geri çekme bildiriminin gerçek gerekçesi okunmalıdır; geri çekme tek başına sahtekârlık demek değildir.

Varsayılan çıktı Markdown veya düz metindir. [Rapor şablonu](skills/academic-paper-audit/assets/report-template.md) düzeni gösterir; [JSON](skills/academic-paper-audit/assets/report.schema.json) isteğe bağlıdır. Yapısal doğrulama bilimsel doğruluğu veya kaynağın gerçekten okunduğunu kanıtlamaz. Hesaplanmamış hash ve yapılmamış işlemler açıkça belirtilir. Katı rapor JSON’unun istediği gözlemlenmiş zaman damgası yoksa insan-okunur rapor kullanılır.

### Kanıtı koruyun, oturumlar arasında devam edin

Özgün dosyaları değiştirmeyin; türetilen kopyaları ayrı kaydedin. Yayımlanmamış makaleleri, kimlik belirleyici kayıtları ve ham veriyi yalnız yetkili ortamda paylaşın. Proje sunucu hizmeti veya telemetri çalıştırmaz; kullandığınız ajan ve araçlarının veri politikaları ayrıca geçerlidir. İnceleme talebi, üçüncü tarafa yükleme, yazarlarla iletişim veya suçlama yayımlama izni değildir. Belgenin içindeki yönlendirici talimatlar komut olarak uygulanmaz. Ayrıntılı işleme ve saklama sınırları [gizlilik rehberinde](docs/PRIVACY.md) açıklanır.

Başka oturuma veya ajana geçerken [devam kaydını](skills/academic-paper-audit/assets/continuation-template.md) kullanın. Makale/sürüm, kapsam, kanıt kimlikleri, incelenen konumlar, tamamlanan kontroller, bulgu kimliği/durumu, eksik materyal ve sonraki adımları gerçek kaynaklarla birlikte taşıyın. Değişen kanıtı yeniden inceleyin. Düzeltilen bulguyu geçmişte saklayıp aktif sayıma katmayın. Özet, görülmemiş kaynağın veya yeni işlem izninin yerini tutmaz.

Güncel kaynak kodunda JSON devam kaydı, kaydedilmiş araştırma bağlamını, her alanın sınırlamalarını ve tamamlanan kontrollere bağlantılarını korur. Eski kayıtlarda bu bilgiler yoksa `validate-checkpoint`, `warnings` alanında uyarı verir; devam ederken eksikleri açıkça belirtin. Bu güncellemeler v.0.0.3 paketlerine dahildir; tutarlı v.0.0.2 devam kayıtları okunabilir.

### İsteğe bağlı yerel yardımcılar

Komutlar için tam depo veya skill klasörü gerekir; yalnız prompt içeren ZIP’te Python betikleri bulunmaz. Python 3.10+ sadece yardımcılar/geliştirme içindir. Envanter ve aritmetik standart kütüphaneyle çalışır; rapor/devam kaydı doğrulaması ve aktarımı `jsonschema` 4.26.0 gerektirir. `python -m venv .venv` sonrasında Windows’ta `.venv/Scripts/python.exe`, macOS/Linux’ta `.venv/bin/python` kullanılabilir. Aşağıdaki `python`, seçtiğiniz ortamın yorumlayıcısını ifade eder; komutlar depo kökünden çalıştırılır.

Aşağıdaki komutlar için [tam depo kaynağını][download-source] indirin. Kurulu skill içinden çalışıyorsanız klasörüne göre yollar kullanan [SKILL.md](skills/academic-paper-audit/SKILL.md) yönergelerini izleyin.

```text
python -m pip install -r skills/academic-paper-audit/requirements.txt
python skills/academic-paper-audit/scripts/audit_tools.py inventory --root tests/fixtures synthetic_manuscript.md
python skills/academic-paper-audit/scripts/audit_tools.py percentage --count 1 --total 3 --reported 33.3 --places 1
python skills/academic-paper-audit/scripts/audit_tools.py flow --initial 100 --excluded 10 --dropouts 5 --analyzed 90 --disjoint
python skills/academic-paper-audit/scripts/audit_tools.py validate-report examples/synthetic-report.json
python skills/academic-paper-audit/scripts/audit_tools.py checkpoint examples/synthetic-report.json
python skills/academic-paper-audit/scripts/audit_tools.py validate-checkpoint examples/synthetic-checkpoint.json
```

Örnekler sentetiktir. Envanter, `--root` köküne göre yolları kabul edip bayt boyutu ve SHA-256 üretir. Yüzde kontrolü ağırlıksız sayım ve en yakına yuvarlama; akış kontrolü aynı nüfus/zamandaki ayrık kayıplar varsayar. Hesaplama kanıt düzeyi atamaz. Devam kaydı komutu JSON’u standart çıktıya yazar; kaydederken UTF-8 kullanın. Çıkış kodları başarılı hesaplama/geçerli kayıt için 0, geçersiz rapor/devam kaydı için 1, girdi veya bağımlılık hatası için 2’dir. Sayısal uyumsuzluk, hesaplamanın başarısız olduğu anlamına gelmez.

### Doğrulama, destek ve lisans

Projede 81 davranış testi ve Windows/Ubuntu üzerinde Python 3.10 ve 3.14 ile çalışan bir CI matrisi bulunur. v.0.0.2, Windows envanterindeki zaman alanı karşılaştırmasını düzeltir; dosya kimliği ve gerçek değişiklik kontrollerini korur. Kısa istek, tam prompt ve skill yollarının her biri 16 sentetik vaka ve 48 model-yargıç ölçütünü geçmiştir; sorunsuz kontroller, yetersiz kanıt ve çözülen bulgu da sınanmıştır. Bunlar bilimsel doğruluk oranı değildir. Gerçek ajan testleri ve başarısızlıkları doğrulama rehberinde kayıtlıdır; sonuçlar yalnız sınanan çalıştırmalar için geçerlidir. macOS ve tüm dil, materyal ve disiplinlerde uzman performansı doğrulanmış değildir. [Doğrulama rehberi](docs/VALIDATION.md) kanıtları, sınırları ve tekrar adımlarını içerir.

Tekrarlanabilir bir sorun için [hata formuna][issues] küçük bir sentetik veya paylaşılabilir örnek ekleyin. Geliştirme ve yayın süreci [katkı rehberinde](CONTRIBUTING.md), sürüm değişiklikleri [CHANGELOG.md](CHANGELOG.md) içinde açıklanır. Proje [MIT lisanslıdır](LICENSE). Bu bölüm tam kullanıcı rehberidir; ek teknik belgeler İngilizce tutulur.

[↑ Başa dön](#top)

---

<a id="lang-de"></a>
## Deutsch

### Zweck und Anwendungsbereich

Academic Paper Forensic & Research Integrity Auditor unterstützt Forschende, Gutachtende, Redaktionen, Studierende und Fachleute für Forschungsintegrität bei einer nachvollziehbaren Erstprüfung wissenschaftlicher Arbeiten. Die Grundlage ist ein wiederverwendbares Prüfprotokoll für den KI-Assistenten Ihrer Wahl. Maßgeblich sind die Aussagen, Methoden und Belege der jeweiligen Arbeit; eine einheitliche experimentelle Checkliste wird nicht allen Disziplinen vorgeschrieben.

Je nach Material und tatsächlich verfügbaren Werkzeugen lassen sich Argumente und Beweise, Methoden-Ergebnis-Widersprüche, Zahlenangaben, rechnergestützte Auswertungen, Quellenzuordnungen, Abbildungen, Herkunftsangaben, Literaturverweise, Mitteilungen und mehrere Arbeiten vergleichend prüfen. Berichtslücken, methodische Grenzen, wissenschaftliche Meinungsverschiedenheiten und konkrete Integritätsbedenken werden getrennt behandelt. Ein wesentlicher Befund braucht eine genaue Fundstelle, einen reproduzierbaren Prüfschritt, eine plausible harmlose Erklärung und einen Vorschlag zur menschlichen Überprüfung.

Das Verfahren ist eine KI-gestützte Vorprüfung. Folgenschwere Entscheidungen erfordern eine unabhängige menschliche Prüfung. Auffälligkeiten belegen weder Fehlverhalten noch Absicht; fehlende Befunde bestätigen keine Echtheit. Das Protokoll unterstützt Fachurteile, ersetzt jedoch keine fachliche Begutachtung, Laboranalyse oder institutionelle Untersuchung.

### Mit dem vorhandenen Assistenten beginnen

1. Laden Sie das [Prompt-Paket][download-prompt] herunter oder öffnen Sie [master_prompt.md](master_prompt.md). Fügen Sie das vollständige Protokoll als Text oder lesbare Datei hinzu. Für eine eng begrenzte Erstprüfung steht die Anfrage in [QUICKSTART.md](QUICKSTART.md) bereit.
2. Stellen Sie die Arbeit oder gezielte Auszüge sowie ergänzende Materialien bereit, die Sie weitergeben dürfen. Benennen Sie Fassung, Seiten, Abbildungen, Argumente und Fragestellung. Kann der Assistent einen Anhang nicht lesen, fügen Sie die betreffenden Passagen ein und begrenzen Sie den Prüfauftrag ausdrücklich darauf.
3. Legen Sie Sprache, Zielgruppe, Umfang und Schwerpunkt fest. Im vollständigen Prompt ändern Sie nur die Werte in eckigen Klammern unter `USER INPUT — EDIT ONLY THIS SECTION`. Das folgende Beispiel beschreibt den Auftrag, bestätigt aber keine Datei- oder Werkzeugverfügbarkeit.

```text
OUTPUT_LANGUAGE = [Deutsch]
RESEARCH_CONTEXT = [Fachgebiete, Methoden und Belegarten des bereitgestellten Materials bestimmen.]
CAPABILITY_MODE = [Nur beobachtete Fähigkeiten nutzen und nicht mögliche Prüfungen offenlegen.]
AUDIENCE = [Professional]
OUTPUT_LENGTH = [Detailed]
ANALYSIS_DEPTH = [Deep]
PRIORITY_FOCUS = [All applicable areas]
OUTPUT_FORMAT = [Structured forensic report]
SPECIAL_INSTRUCTIONS = [Genaue Fundstellen nennen, harmlose Erklärungen prüfen und nächste menschliche Prüfschritte angeben.]
MATERIALS = [Bereitgestellte Dateien oder Auszüge, Fassungen und gewünschten Prüfbereich aufführen.]
```

Für die Länge stehen `Short`, `Standard`, `Detailed`, `Exhaustive`, für die Zielgruppe `Beginner`, `General`, `Researcher`, `Professional`, `Expert` zur Verfügung. Ein Auftrag wie „Annahmen des Beweises prüfen“ oder „Tabelle 2 mit dem Methodenteil abgleichen“ schafft einen klaren Rahmen. Fehlt prüfbares Material, soll der Assistent dieses anfordern und die Beweislage als unzureichend kennzeichnen.

`ANALYSIS_DEPTH` erlaubt `Standard`, `Deep` oder `Maximum`: die anwendbaren Kernprüfungen, eine vertiefte Untersuchung oder die umfassendste sinnvolle Prüfung mit den vorhandenen Belegen und Werkzeugen. Größere Tiefe schafft keine fehlenden Fähigkeiten. Die übrigen beschreibenden Felder nehmen eigene Anweisungen auf: Forschungskontext, Prioritäten, Sonderwünsche und Materialien. Unter `OUTPUT_FORMAT` können Sie etwa eine Zusammenfassung für Entscheidungsträger oder einen technischen Bericht anfordern.

### Format und Belege auswählen

| Format | Geeignet für | Voraussetzung |
| --- | --- | --- |
| [Vollständiger Prompt][download-prompt] | Eingehende Prüfung mit einem textfähigen Assistenten | Hauptprotokoll und lesbares Forschungsmaterial |
| [Kurzanfrage](QUICKSTART.md) | Erste Einordnung oder kleines Kontextfenster | Kopierbare Anfrage und begrenzter Prüfbereich |
| [Eigenständiger Skill][download-skill] | Hosts mit Unterstützung des offenen Agent-Skills-Ordnerformats | Vollständiger Ordner `academic-paper-audit` mit verknüpften Ressourcen |
| [Optionales Plugin][download-plugin] | Hosts mit Unterstützung des Plugin-Pakets | Kompatibler Loader; Installation und Erkennung hängen vom Host ab |

Verwenden Sie pro Prüfung ein Format. Für den Textweg sind weder Python noch API-Schlüssel oder Anbieterintegration nötig. Die [Release-Seite][release] bietet drei Archive und [SHA-256-Prüfsummen][checksums]. Eine passende Prüfsumme bestätigt die heruntergeladenen Bytes, nicht die Echtheit einer Forschungsquelle.

Die Prüfung richtet sich nach der Methode: bei quantitativen Arbeiten etwa nach Nennern, Stichproben und Unsicherheit; bei qualitativen nach Zitatkontext und Analyseschritten; bei rechnergestützten Arbeiten nach Datenaufteilung und tatsächlicher Ausführung. Formale Arbeiten erfordern Annahmen, Quantoren und Gegenbeispiele, technische Arbeiten Einheiten, Kalibrierung und Randbedingungen, Archivstudien Ausgaben, Daten und Transkriptionen. Mixed Methods, Synthesen sowie konzeptionelle und praxisbasierte Forschung werden anhand ihrer eigenen Aussagen beurteilt. Die Beispiele begrenzen den Anwendungsbereich nicht. P-Werte, Vorregistrierung, offene Rohdaten und DOI sind keine allgemeinen Pflichtkriterien.

Wenn eine Frage Originalbilder oder Quellenunterlagen voraussetzt, stellen Sie möglichst diese bereit. Eine komprimierte PDF kann eine Textprüfung ermöglichen, aber keine belastbare Pixel- oder Metadatenanalyse. Bild-, Web- und Spezialwerkzeuge zählen nur, wenn sie tatsächlich genutzt werden können. Die mitgelieferten Hilfsskripte sind keine OCR-, Bildforensik-, Beweisprüfungs- oder KI-Bilderkennungssysteme.

### Den Bericht verstehen

Ein Bericht erläutert Prüfbereich, eingesetzte Werkzeuge, Methodenkontext, priorisierte Befunde, entlastende Belege, Grenzen und nächste menschliche Schritte. Er dokumentiert Text/Methoden, Statistik/Daten, Abbildungen, Metadaten/Herkunft, Literatur/Mitteilungen, Ethik/Registrierung und arbeitsübergreifende Vergleiche. `completed` bedeutet im angegebenen Umfang geprüft, `partial` teilweise geprüft, `not_assessed` nicht geprüft. `not_applicable` verlangt eine Begründung der Nichtanwendbarkeit.

Die Evidenzstufen betreffen die Beobachtung: **0** keine relevante Auffälligkeit im geprüften Bereich; **1** schwaches Signal mit plausiblen harmlosen Erklärungen; **2** reproduzierbarer wesentlicher Widerspruch; **3** starkes, zusätzlich belegtes Bedenken mit Bedarf an fachlicher Prüfung; **4** ein konkretes Problem, das eine gelesene, maßgebliche und zur Arbeit passende externe Quelle bestätigt. Stufe 2/3 belegt keine Absicht. Vertrauensangaben beziehen sich auf den Befund, nicht auf persönliche Schuld. Ein Rückzug muss anhand seiner tatsächlichen Begründung gelesen werden; er allein belegt keinen Betrug.

Markdown oder Klartext ist der Standard. Die [Berichtsvorlage](skills/academic-paper-audit/assets/report-template.md) zeigt den Aufbau; [JSON](skills/academic-paper-audit/assets/report.schema.json) ist optional. Strukturprüfung beweist weder wissenschaftliche Wahrheit noch tatsächliches Quellenlesen. Nicht berechnete Hashes und nicht ausgeführte Prüfungen müssen erkennbar bleiben. Fehlt ein beobachteter Zeitstempel für das strikte Berichts-JSON, verwenden Sie einen menschenlesbaren Bericht.

### Belege schützen und später weiterarbeiten

Verändern Sie Originale nicht und kennzeichnen Sie abgeleitete Kopien. Unveröffentlichte Arbeiten, personenbezogene Unterlagen und Rohdaten gehören in eine autorisierte Umgebung. Das Projekt betreibt keinen gehosteten Dienst und keine Telemetrie; für Assistent und Werkzeuge gelten jedoch eigene Datenrichtlinien. Ein Prüfauftrag erlaubt weder externe Uploads noch die Kontaktaufnahme mit Autorinnen und Autoren oder die Veröffentlichung von Vorwürfen. Eingebettete Anweisungen im Material sind Inhalt, keine Befehle. Der [Datenschutzleitfaden](docs/PRIVACY.md) erläutert Verarbeitung und Aufbewahrung.

Für einen neuen Chat oder Assistenten nutzen Sie den [Fortsetzungsnachweis](skills/academic-paper-audit/assets/continuation-template.md). Übergeben Sie Arbeit/Fassung, Umfang, Beleg-IDs, Fundstellen, erledigte Prüfungen, Befund-IDs/Status, fehlendes Material und nächste Schritte zusammen mit den tatsächlichen Quellen. Geänderte Belege werden neu geprüft. Erledigte Bedenken bleiben als gelöste Historie erhalten und zählen nicht als aktive Befunde. Eine Zusammenfassung ersetzt keine ungelesene Quelle und erweitert keine Berechtigung.

Im aktuellen Quellstand bewahrt der JSON-Fortsetzungsexport den erfassten Forschungskontext, die Einschränkungen jedes Bereichs und Verweise auf abgeschlossene Prüfungen. Fehlen diese Angaben in älteren Datensätzen, meldet `validate-checkpoint` dies unter `warnings`; halten Sie die Lücken beim Fortsetzen ausdrücklich fest. Diese Änderungen sind in v.0.0.3 enthalten; konsistente Fortsetzungsdatensätze aus v.0.0.2 bleiben lesbar.

### Optionale lokale Hilfsskripte

Die Befehle benötigen das vollständige Repository oder den Skill-Ordner; das reine Prompt-ZIP enthält keine Python-Skripte. Python 3.10+ ist nur für Hilfsskripte/Entwicklung nötig. Inventarisierung und Arithmetik nutzen die Standardbibliothek; Berichts-/Fortsetzungsvalidierung und Export benötigen `jsonschema` 4.26.0. Nach `python -m venv .venv` lautet der Interpreter unter Windows `.venv/Scripts/python.exe`, unter macOS/Linux `.venv/bin/python`. `python` steht unten für diesen Interpreter; Ausgangspunkt ist das Repository-Hauptverzeichnis.

Laden Sie für die folgenden Befehle das [vollständige Repository][download-source] herunter. In einem installierten Skill folgen Sie [SKILL.md](skills/academic-paper-audit/SKILL.md); dort sind die Pfade relativ zum Skill-Ordner.

```text
python -m pip install -r skills/academic-paper-audit/requirements.txt
python skills/academic-paper-audit/scripts/audit_tools.py inventory --root tests/fixtures synthetic_manuscript.md
python skills/academic-paper-audit/scripts/audit_tools.py percentage --count 1 --total 3 --reported 33.3 --places 1
python skills/academic-paper-audit/scripts/audit_tools.py flow --initial 100 --excluded 10 --dropouts 5 --analyzed 90 --disjoint
python skills/academic-paper-audit/scripts/audit_tools.py validate-report examples/synthetic-report.json
python skills/academic-paper-audit/scripts/audit_tools.py checkpoint examples/synthetic-report.json
python skills/academic-paper-audit/scripts/audit_tools.py validate-checkpoint examples/synthetic-checkpoint.json
```

Die Beispiele sind synthetisch. Das Inventar erwartet Pfade relativ zu `--root` und liefert Bytezahl und SHA-256. Der Prozenttest setzt ungewichtete Zählwerte und übliche Rundung voraus; die Flussprüfung getrennte Verluste derselben Population zum selben Zeitpunkt. Rechenhilfen vergeben keine Evidenzstufe. Der Fortsetzungsexport schreibt JSON auf stdout; speichern Sie es bei Bedarf als UTF-8. Rückgabecodes: 0 für erfolgreiche Berechnung/gültige Datensätze, 1 für ungültigen Bericht/Fortsetzungsdatensatz, 2 für Eingabe- oder Abhängigkeitsfehler. Eine Zahlenabweichung ist ein Berechnungsergebnis, kein Programmfehler.

### Prüfung, Hilfe und Lizenz

Das Projekt enthält 81 Verhaltenstests und eine CI-Matrix für Windows/Ubuntu mit Python 3.10 und 3.14. Version v.0.0.2 korrigiert den Zeitstempelvergleich im Windows-Inventar und bewahrt die Prüfung von Dateiidentität und tatsächlichen Änderungen. Kurzanfrage, Hauptprotokoll und Skill bestanden jeweils 16 synthetische Fälle und 48 modellbewertete Kriterien, darunter unauffällige Kontrollen, unzureichende Evidenz und ein gelöster Befund. Das sind Abnahmeresultate, keine wissenschaftlichen Genauigkeitsmessungen. Beobachtete native Hosttests und ihre Fehlschläge sind im Validierungsleitfaden dokumentiert; die Ergebnisse gelten nur für diese Durchläufe. macOS sowie fachliche Leistung über alle Sprachen, Medien und Disziplinen sind nicht nachgewiesen. Der [Validierungsleitfaden](docs/VALIDATION.md) enthält Belege, Grenzen und Wiederholungsschritte.

Melden Sie reproduzierbare Probleme im [Fehlerformular][issues] mit einem kleinen synthetischen oder freigegebenen Beispiel. [Contributing](CONTRIBUTING.md) beschreibt Entwicklung und Releases, [CHANGELOG.md](CHANGELOG.md) die Änderungen. Es gilt die [MIT-Lizenz](LICENSE). Dieser Abschnitt ist ein vollständiger Benutzerleitfaden; ergänzende technische Dokumente werden auf Englisch gepflegt.

[↑ Nach oben](#top)

---

<a id="lang-fr"></a>
## Français

### Objectif et périmètre

Academic Paper Forensic & Research Integrity Auditor accompagne les chercheurs, évaluateurs, éditeurs, étudiants et spécialistes de l’intégrité scientifique dans un premier examen structuré des travaux de recherche. Son élément central est un protocole réutilisable à transmettre à l’assistant d’IA de votre choix. Les vérifications découlent des affirmations, méthodes et preuves disponibles ; une même grille expérimentale n’est pas imposée à toutes les disciplines.

Selon les documents et les outils accessibles, l’examen peut porter sur les arguments et démonstrations, la cohérence méthodes–résultats, les valeurs numériques, l’évaluation informatique, l’attribution des sources, les figures, la provenance, les références, les avis et les comparaisons entre publications. Le rapport distingue lacune de présentation, limite méthodologique, désaccord scientifique et préoccupation d’intégrité précise. Toute observation importante doit être localisée, reproductible, confrontée à une explication bénigne et accompagnée de la prochaine vérification humaine utile.

Il s’agit d’un examen préliminaire assisté par IA. Les décisions ayant des conséquences exigent une vérification humaine indépendante. Une anomalie ne démontre ni faute ni intention ; l’absence d’anomalies ne certifie pas l’authenticité. Le protocole soutient le jugement sans remplacer une expertise disciplinaire, un laboratoire ou une enquête institutionnelle.

### Commencer avec votre assistant habituel

1. Téléchargez le [paquet de prompts][download-prompt] ou ouvrez [master_prompt.md](master_prompt.md). Collez le protocole complet dans l’assistant ou joignez-le sous une forme lisible. Pour un premier examen limité, utilisez la demande de [QUICKSTART.md](QUICKSTART.md).
2. Fournissez l’article ou les extraits pertinents ainsi que les pièces complémentaires que vous êtes autorisé à partager. Précisez la version, les pages, figures, arguments ou questions concernés. Si une pièce jointe reste illisible, collez des passages ciblés et limitez explicitement l’examen à ces passages.
3. Choisissez la langue, le public, la longueur et la priorité. Dans le prompt complet, modifiez uniquement les valeurs entre crochets de `USER INPUT — EDIT ONLY THIS SECTION`. L’exemple suivant configure une demande ; il ne prouve pas que les fichiers ou outils sont disponibles.

```text
OUTPUT_LANGUAGE = [Français]
RESEARCH_CONTEXT = [Identifier les disciplines, méthodes et types de preuves du matériel fourni.]
CAPABILITY_MODE = [Utiliser les capacités observées et signaler les vérifications indisponibles.]
AUDIENCE = [Professional]
OUTPUT_LENGTH = [Detailed]
ANALYSIS_DEPTH = [Deep]
PRIORITY_FOCUS = [All applicable areas]
OUTPUT_FORMAT = [Structured forensic report]
SPECIAL_INSTRUCTIONS = [Indiquer les emplacements exacts, tester les explications bénignes et proposer les prochaines vérifications humaines.]
MATERIALS = [Énumérer les fichiers ou extraits fournis, leurs versions et le périmètre demandé.]
```

La longueur peut être `Short`, `Standard`, `Detailed` ou `Exhaustive` ; le public, `Beginner`, `General`, `Researcher`, `Professional` ou `Expert`. Une demande comme « vérifier les hypothèses de la preuve » ou « rapprocher le tableau 2 des méthodes » facilite un résultat exploitable. Sans élément évaluable, l’assistant doit demander du matériel et conclure à une insuffisance de preuves.

`ANALYSIS_DEPTH` accepte `Standard`, `Deep` ou `Maximum` : vérifications essentielles applicables, examen approfondi ou revue aussi complète que le permettent les preuves et outils disponibles. Une profondeur accrue ne crée pas de capacités absentes. Les autres champs descriptifs accueillent vos instructions : contexte de recherche, priorités, demandes particulières et pièces fournies. `OUTPUT_FORMAT` peut demander, par exemple, une synthèse pour décideurs ou un rapport technique.

### Choisir le format et les pièces utiles

| Format | Usage | Conditions |
| --- | --- | --- |
| [Prompt complet][download-prompt] | Examen approfondi avec un assistant lisant le texte | Protocole principal et documents lisibles |
| [Demande courte](QUICKSTART.md) | Premier tri ou contexte limité | Demande à copier et périmètre défini |
| [Skill autonome][download-skill] | Hôte compatible avec le format ouvert Agent Skills | Dossier `academic-paper-audit` complet et ressources liées |
| [Plugin facultatif][download-plugin] | Hôte compatible avec le paquet de plugin | Chargeur adapté ; installation et découverte propres à l’hôte |

Utilisez un seul format par examen. Le parcours textuel ne nécessite ni Python, ni clé API, ni intégration à un fournisseur. La [page de version][release] propose trois archives et les [sommes SHA-256][checksums]. Une somme correspondante vérifie les octets téléchargés, pas l’authenticité d’une source de recherche.

Les critères suivent la méthode : dénominateurs, échantillonnage et incertitude en quantitatif ; contexte des citations et trace analytique en qualitatif ; séparation des données et exécution réelle en informatique. Les travaux formels demandent hypothèses, quantificateurs et contre-exemples ; l’ingénierie, unités, étalonnage et conditions limites ; les archives, éditions, dates et transcriptions. Méthodes mixtes, synthèses et recherches conceptuelles ou fondées sur la pratique exigent des critères adaptés à leurs affirmations. Cette liste reste ouverte. Valeurs p, préenregistrement, données brutes publiques et DOI ne sont pas des obligations universelles.

Lorsqu’une question dépend d’une figure originale ou d’un document source, fournissez-le si possible. Un PDF compressé peut permettre un examen textuel sans justifier des conclusions sur les pixels ou métadonnées. Vision, accès web et outils spécialisés élargissent le périmètre seulement s’ils sont réellement disponibles. Les scripts du projet ne réalisent ni OCR, ni analyse forensique d’images, ni vérification formelle de preuves, ni détection automatique d’images générées par IA.

### Lire le rapport

Le rapport présente le périmètre, les outils employés, le contexte méthodologique, les observations prioritaires, les éléments qui réduisent les soupçons, les limites et les prochaines vérifications humaines. Il couvre texte/méthodes, statistiques/données, figures, métadonnées/provenance, références/avis, éthique/enregistrement et comparaisons entre publications. `completed` signifie vérifié dans le périmètre indiqué, `partial` partiellement vérifié, `not_assessed` non examiné. `not_applicable` nécessite une justification de non-pertinence.

Les niveaux décrivent l’appui d’une observation : **0**, aucune anomalie notable dans le périmètre examiné ; **1**, signal faible avec explications bénignes plausibles ; **2**, incohérence importante reproductible ; **3**, préoccupation forte étayée par des éléments supplémentaires et nécessitant une expertise ; **4**, problème précis corroboré par une source externe faisant autorité, effectivement lue et correspondant à l’article. Les niveaux 2/3 n’établissent pas l’intention. La confiance concerne l’observation, pas la culpabilité. Un avis de rétractation doit être lu pour son motif réel ; son existence seule ne prouve pas une fraude.

Markdown ou texte brut convient par défaut. Le [modèle de rapport](skills/academic-paper-audit/assets/report-template.md) précise l’organisation ; le [JSON](skills/academic-paper-audit/assets/report.schema.json) est facultatif. La validation structurelle ne prouve ni la vérité scientifique ni la consultation effective d’une source. Les empreintes non calculées et opérations non effectuées doivent rester visibles. Si l’horodatage observé exigé par le JSON strict manque, utilisez un rapport lisible par une personne.

### Protéger les preuves et reprendre une session

Conservez les originaux et identifiez séparément les copies dérivées. Partagez manuscrits inédits, données identifiantes et données brutes uniquement dans un environnement autorisé. Le projet n’exploite ni service hébergé ni télémétrie ; l’assistant et ses outils suivent néanmoins leurs propres politiques. Une demande d’examen n’autorise pas les dépôts externes, le contact des auteurs ou la publication d’accusations. Les instructions intégrées aux documents restent du contenu à examiner, pas des commandes. Le [guide de confidentialité](docs/PRIVACY.md) détaille traitement et conservation.

Pour changer de session ou d’agent, utilisez la [fiche de reprise](skills/academic-paper-audit/assets/continuation-template.md). Transmettez article/version, périmètre, identifiants de preuves, emplacements examinés, contrôles effectués, identifiants/statuts des observations, pièces manquantes et prochaines étapes avec les vraies sources. Réexaminez les éléments modifiés. Gardez les observations corrigées dans l’historique comme résolues, hors des comptes actifs. Un résumé ne remplace pas une source non consultée et n’élargit aucune autorisation.

Dans le code source actuel, l’export JSON de reprise conserve le contexte de recherche enregistré, les limites de chaque domaine et les liens vers les contrôles terminés. Si ces informations manquent dans un ancien enregistrement, `validate-checkpoint` les signale dans `warnings` ; gardez ces lacunes explicites lors de la reprise. Ces mises à jour sont incluses dans v.0.0.3 ; les enregistrements de reprise cohérents de v.0.0.2 restent lisibles.

### Outils locaux facultatifs

Les commandes demandent le dépôt complet ou le dossier du skill ; le ZIP de prompts ne contient pas de scripts Python. Python 3.10+ sert uniquement aux outils et au développement. Inventaire et calculs utilisent la bibliothèque standard ; validation des rapports/fiches de reprise et export exigent `jsonschema` 4.26.0. Après `python -m venv .venv`, utilisez `.venv/Scripts/python.exe` sous Windows ou `.venv/bin/python` sous macOS/Linux. Ci-dessous, `python` désigne cet interpréteur ; lancez les commandes depuis la racine du dépôt.

Pour ces commandes, téléchargez le [dépôt complet][download-source]. Dans un skill installé, suivez [SKILL.md](skills/academic-paper-audit/SKILL.md), dont les chemins sont relatifs au dossier du skill.

```text
python -m pip install -r skills/academic-paper-audit/requirements.txt
python skills/academic-paper-audit/scripts/audit_tools.py inventory --root tests/fixtures synthetic_manuscript.md
python skills/academic-paper-audit/scripts/audit_tools.py percentage --count 1 --total 3 --reported 33.3 --places 1
python skills/academic-paper-audit/scripts/audit_tools.py flow --initial 100 --excluded 10 --dropouts 5 --analyzed 90 --disjoint
python skills/academic-paper-audit/scripts/audit_tools.py validate-report examples/synthetic-report.json
python skills/academic-paper-audit/scripts/audit_tools.py checkpoint examples/synthetic-report.json
python skills/academic-paper-audit/scripts/audit_tools.py validate-checkpoint examples/synthetic-checkpoint.json
```

Les exemples sont synthétiques. L’inventaire accepte des chemins relatifs à `--root` et produit tailles en octets et SHA-256. Le contrôle de pourcentage suppose des effectifs non pondérés et un arrondi usuel ; le flux suppose des pertes disjointes dans la même population au même moment. Les calculs n’attribuent aucun niveau de preuve. L’export de reprise écrit du JSON sur stdout, à enregistrer en UTF-8. Codes de sortie : 0 pour calcul réussi/enregistrement valide, 1 pour rapport ou fiche invalide, 2 pour erreur d’entrée ou de dépendance. Une incohérence arithmétique reste un résultat de calcul valide.

### Vérification, aide et licence

Le projet comprend 81 tests de comportement et une matrice CI Windows/Ubuntu avec Python 3.10 et 3.14. La version v.0.0.2 corrige la comparaison temporelle de l’inventaire Windows tout en conservant les contrôles d’identité et de modification des fichiers. Demande courte, protocole complet et skill ont chacun passé 16 cas synthétiques et 48 critères évalués par un modèle, dont des contrôles sans anomalie, des preuves insuffisantes et une observation résolue. Ces résultats ne mesurent pas la précision scientifique. Les essais réels dans les environnements hôtes et leurs échecs sont consignés dans le guide de validation ; les résultats ne valent que pour ces exécutions. L’exécution macOS et l’expertise dans toutes les langues, modalités et disciplines restent non établies. Le [guide de validation](docs/VALIDATION.md) fournit preuves, limites et procédure de reproduction.

Signalez un problème reproductible dans le [formulaire][issues] avec un petit exemple synthétique ou partageable. [Contributing](CONTRIBUTING.md) décrit développement et versions, [CHANGELOG.md](CHANGELOG.md) les changements. Le projet est sous [licence MIT](LICENSE). Cette section constitue un guide utilisateur complet ; les documents techniques complémentaires sont maintenus en anglais.

[↑ Retour en haut](#top)

---

<a id="lang-es"></a>
## Español

### Propósito y alcance

Academic Paper Forensic & Research Integrity Auditor ayuda a investigadores, revisores, editores, estudiantes y especialistas en integridad científica a realizar una primera revisión estructurada de trabajos académicos. Su recurso principal es un protocolo reutilizable para el asistente de IA que prefiera. Los criterios se eligen a partir de las afirmaciones, métodos y pruebas del trabajo; no se impone la misma lista experimental a todas las disciplinas.

Según los materiales y las herramientas disponibles, pueden examinarse argumentos y demostraciones, coherencia entre métodos y resultados, cifras, evaluaciones computacionales, atribución de fuentes, imágenes, procedencia, referencias, avisos y comparaciones entre publicaciones. El informe distingue carencias de presentación, limitaciones metodológicas, desacuerdos académicos y preocupaciones concretas de integridad. Cada hallazgo relevante necesita una ubicación exacta, una comprobación reproducible, una explicación benigna plausible y un siguiente paso de verificación humana.

Se trata de una revisión preliminar asistida por IA. Las decisiones con consecuencias requieren revisión humana independiente. Una anomalía no demuestra mala conducta ni intención, y la ausencia de hallazgos no acredita autenticidad. El protocolo apoya el juicio profesional sin sustituir a un experto del área, un laboratorio o una investigación institucional.

### Empezar con su asistente habitual

1. Descargue el [paquete de prompts][download-prompt] o abra [master_prompt.md](master_prompt.md). Pegue el protocolo completo o adjúntelo como archivo legible. Para una revisión inicial acotada puede usar la solicitud de [QUICKSTART.md](QUICKSTART.md).
2. Proporcione el artículo o fragmentos pertinentes y los materiales complementarios que tenga autorización para compartir. Identifique versión, páginas, figuras, argumentos y pregunta de revisión. Si el asistente no puede leer un adjunto, pegue pasajes concretos y limite expresamente el alcance a ellos.
3. Elija idioma, público, extensión y prioridad. En el prompt completo, cambie solo los valores entre corchetes de `USER INPUT — EDIT ONLY THIS SECTION`. Esta configuración de ejemplo no confirma que existan archivos o herramientas accesibles.

```text
OUTPUT_LANGUAGE = [Español]
RESEARCH_CONTEXT = [Identificar disciplinas, métodos y tipos de pruebas del material proporcionado.]
CAPABILITY_MODE = [Usar capacidades observadas y declarar las comprobaciones no disponibles.]
AUDIENCE = [Professional]
OUTPUT_LENGTH = [Detailed]
ANALYSIS_DEPTH = [Deep]
PRIORITY_FOCUS = [All applicable areas]
OUTPUT_FORMAT = [Structured forensic report]
SPECIAL_INSTRUCTIONS = [Indicar ubicaciones exactas, contrastar explicaciones benignas y señalar las siguientes verificaciones humanas.]
MATERIALS = [Enumerar archivos o fragmentos, versiones y alcance solicitado.]
```

La extensión puede ser `Short`, `Standard`, `Detailed` o `Exhaustive`; el público, `Beginner`, `General`, `Researcher`, `Professional` o `Expert`. Una petición como «revisar los supuestos de la demostración» o «comparar la tabla 2 con los métodos» facilita un resultado útil. Sin material evaluable, corresponde solicitarlo y declarar pruebas insuficientes, no emitir un visto bueno.

`ANALYSIS_DEPTH` admite `Standard`, `Deep` o `Maximum`: comprobaciones esenciales aplicables, examen más detallado o revisión más amplia que permitan las pruebas y herramientas disponibles. Una mayor profundidad no añade capacidades ausentes. Los demás campos descriptivos aceptan sus instrucciones sobre contexto, prioridades, peticiones especiales y materiales. En `OUTPUT_FORMAT` puede pedir, por ejemplo, un resumen ejecutivo o un informe técnico.

### Elegir formato y pruebas

| Formato | Cuándo conviene | Requisitos |
| --- | --- | --- |
| [Prompt completo][download-prompt] | Revisión detallada con un asistente que lea texto | Protocolo principal y material legible |
| [Solicitud breve](QUICKSTART.md) | Primera evaluación o contexto limitado | Solicitud copiable y alcance definido |
| [Skill independiente][download-skill] | El entorno admite carpetas del formato abierto Agent Skills | Carpeta completa `academic-paper-audit` con sus recursos |
| [Plugin opcional][download-plugin] | El entorno admite el paquete de plugin | Cargador compatible; instalación y descubrimiento dependen del entorno |

Use un formato por revisión. La vía textual no exige Python, clave API ni integración con un proveedor. La [página de la versión][release] ofrece tres archivos y [sumas SHA-256][checksums]. Una suma coincidente verifica los bytes descargados, no la autenticidad de una fuente científica.

Los criterios dependen del método: denominadores, muestreo e incertidumbre en investigación cuantitativa; contexto de citas y trazabilidad analítica en cualitativa; separación de datos y ejecución real en computacional. El trabajo formal requiere supuestos, cuantificadores y contraejemplos; la ingeniería, unidades, calibración y condiciones de contorno; los archivos, ediciones, fechas y transcripciones. Métodos mixtos, síntesis y estudios conceptuales o basados en la práctica se evalúan según sus afirmaciones. La lista permanece abierta. Valores p, prerregistro, datos brutos públicos y DOI no son requisitos universales.

Si una pregunta depende de figuras originales o documentos fuente, proporciónelos cuando sea posible. Un PDF comprimido puede permitir revisión textual sin justificar conclusiones sobre píxeles o metadatos. Visión, web y herramientas especializadas amplían el alcance solo si están realmente disponibles. Los scripts incluidos no realizan OCR, análisis forense de imágenes, verificación formal de pruebas ni detección automática de imágenes generadas por IA.

### Interpretar el informe

El informe explica alcance, herramientas utilizadas, contexto metodológico, hallazgos prioritarios, pruebas que reducen las sospechas, limitaciones y próximos controles humanos. Registra texto/métodos, estadísticas/datos, figuras, metadatos/procedencia, referencias/avisos, ética/registro y comparación entre trabajos. `completed` significa revisado dentro del alcance indicado; `partial`, parcialmente revisado; `not_assessed`, no revisado. `not_applicable` exige justificar por qué no corresponde.

Los niveles describen el respaldo de una observación: **0**, sin preocupación significativa en el alcance revisado; **1**, señal débil con explicaciones benignas plausibles; **2**, inconsistencia material reproducible; **3**, preocupación fuerte respaldada por pruebas adicionales que requiere expertos; **4**, problema concreto corroborado por una fuente externa autorizada, leída y correspondiente al artículo. Los niveles 2/3 no establecen intención. La confianza se refiere a la observación, no a la culpabilidad del autor. Un aviso de retractación debe leerse por su motivo real; por sí solo no demuestra fraude.

Markdown o texto es la salida habitual. La [plantilla](skills/academic-paper-audit/assets/report-template.md) muestra la estructura y el [JSON](skills/academic-paper-audit/assets/report.schema.json) es opcional. Validar la estructura no demuestra verdad científica ni consulta efectiva de fuentes. Los hashes no calculados y las operaciones no realizadas deben quedar claros. Si falta una marca temporal observada necesaria para el JSON estricto, utilice un informe legible.

### Proteger las pruebas y continuar después

Conserve los originales y registre las copias derivadas por separado. Comparta manuscritos inéditos, registros identificables y datos brutos únicamente en un entorno autorizado. El proyecto no opera un servicio alojado ni telemetría; el asistente y sus herramientas tienen políticas propias. Una revisión no autoriza cargas externas, contacto con autores ni publicación de acusaciones. Las instrucciones dentro de documentos son contenido, no órdenes. La [guía de privacidad](docs/PRIVACY.md) explica tratamiento y conservación.

Para cambiar de sesión o agente, use el [registro de continuación](skills/academic-paper-audit/assets/continuation-template.md). Traslade artículo/versión, alcance, identificadores de pruebas, ubicaciones revisadas, controles terminados, identificadores/estados de hallazgos, material faltante y próximos pasos junto con las fuentes reales. Revise las pruebas modificadas. Mantenga los hallazgos corregidos como historial resuelto y exclúyalos del recuento activo. Un resumen no sustituye una fuente no vista ni amplía permisos.

En el código fuente actual, la exportación JSON de continuación conserva el contexto de investigación registrado, las limitaciones de cada área y los enlaces a las comprobaciones terminadas. Si un registro antiguo carece de esos datos, `validate-checkpoint` lo indica en `warnings`; mantenga explícitas las lagunas al continuar. Estas actualizaciones están incluidas en v.0.0.3; los registros de continuación coherentes de v.0.0.2 siguen siendo legibles.

### Herramientas locales opcionales

Los comandos requieren el repositorio completo o la carpeta del skill; el ZIP de prompts no incluye scripts Python. Python 3.10+ solo se necesita para herramientas/desarrollo. Inventario y aritmética usan la biblioteca estándar; validación de informes/registros y exportación requieren `jsonschema` 4.26.0. Después de `python -m venv .venv`, use `.venv/Scripts/python.exe` en Windows o `.venv/bin/python` en macOS/Linux. Aquí `python` representa ese intérprete; ejecute desde la raíz del repositorio.

Para estos comandos, descargue el [repositorio completo][download-source]. En un skill instalado, siga [SKILL.md](skills/academic-paper-audit/SKILL.md), que usa rutas relativas a su carpeta.

```text
python -m pip install -r skills/academic-paper-audit/requirements.txt
python skills/academic-paper-audit/scripts/audit_tools.py inventory --root tests/fixtures synthetic_manuscript.md
python skills/academic-paper-audit/scripts/audit_tools.py percentage --count 1 --total 3 --reported 33.3 --places 1
python skills/academic-paper-audit/scripts/audit_tools.py flow --initial 100 --excluded 10 --dropouts 5 --analyzed 90 --disjoint
python skills/academic-paper-audit/scripts/audit_tools.py validate-report examples/synthetic-report.json
python skills/academic-paper-audit/scripts/audit_tools.py checkpoint examples/synthetic-report.json
python skills/academic-paper-audit/scripts/audit_tools.py validate-checkpoint examples/synthetic-checkpoint.json
```

Los ejemplos son sintéticos. El inventario acepta rutas relativas a `--root` y devuelve tamaños en bytes y SHA-256. El porcentaje supone recuentos sin ponderación y redondeo ordinario; el flujo, pérdidas disjuntas en la misma población y momento. Estos cálculos no asignan niveles de prueba. La exportación escribe JSON en stdout; guárdelo en UTF-8 si hace falta. Códigos: 0 para cálculo correcto/registros válidos, 1 para informe o registro inválido, 2 para errores de entrada o dependencias. Una diferencia aritmética es un resultado válido del cálculo.

### Verificación, ayuda y licencia

El proyecto incluye 81 tests de comportamiento y una matriz CI para Windows/Ubuntu con Python 3.10 y 3.14. La versión v.0.0.2 corrige la comparación temporal del inventario en Windows y conserva los controles de identidad y cambios reales de los archivos. Solicitud breve, protocolo completo y skill superaron cada uno 16 casos sintéticos y 48 criterios juzgados por un modelo, incluidos controles legítimos, pruebas insuficientes y un hallazgo resuelto. No son medidas de precisión científica. Las pruebas reales en los entornos anfitriones y sus fallos constan en la guía de validación; los resultados se limitan a esas ejecuciones. La ejecución en macOS y el rendimiento experto en todos los idiomas, modalidades y disciplinas siguen sin verificarse. La [guía de validación](docs/VALIDATION.md) documenta pruebas, límites y reproducción.

Para problemas reproducibles, utilice el [formulario][issues] con un ejemplo mínimo sintético o compartible. [Contributing](CONTRIBUTING.md) explica desarrollo y publicaciones; [CHANGELOG.md](CHANGELOG.md), los cambios. El proyecto tiene [licencia MIT](LICENSE). Esta sección es una guía de uso completa; la documentación técnica adicional se mantiene en inglés.

[↑ Volver al principio](#top)

---

<a id="lang-it"></a>
## Italiano

### Scopo e ambito

Academic Paper Forensic & Research Integrity Auditor aiuta ricercatori, revisori, redazioni, studenti e specialisti dell’integrità della ricerca a svolgere un primo esame strutturato di lavori accademici. La risorsa centrale è un protocollo riutilizzabile da fornire all’assistente di IA preferito. Le verifiche dipendono dalle affermazioni, dai metodi e dalle prove del lavoro: non applicano un’unica lista sperimentale a ogni disciplina.

In base ai materiali e agli strumenti disponibili, si possono esaminare argomenti e dimostrazioni, coerenza fra metodi e risultati, dati numerici, valutazioni computazionali, attribuzioni delle fonti, immagini, provenienza, riferimenti, avvisi e confronti fra pubblicazioni. Il rapporto distingue lacune espositive, limiti metodologici, divergenze scientifiche e problemi specifici d’integrità. Un rilievo importante deve indicare la posizione esatta, una verifica riproducibile, una spiegazione innocua plausibile e il successivo controllo umano.

È uno screening preliminare assistito da IA. Le decisioni con conseguenze richiedono verifica umana indipendente. Un’anomalia non dimostra una condotta scorretta o l’intenzione; l’assenza di rilievi non certifica l’autenticità. Il protocollo sostiene il giudizio senza sostituire un esperto della disciplina, un laboratorio o un’indagine istituzionale.

### Iniziare con l’assistente che usi già

1. Scarica il [pacchetto prompt][download-prompt] oppure apri [master_prompt.md](master_prompt.md). Incolla il protocollo completo o allegalo come file leggibile. Per un primo esame circoscritto puoi usare la richiesta in [QUICKSTART.md](QUICKSTART.md).
2. Fornisci l’articolo o gli estratti pertinenti e i materiali che sei autorizzato a condividere. Specifica versione, pagine, figure, argomenti e domanda di revisione. Se un allegato non è leggibile, incolla i passaggi interessati e limita espressamente l’esame a essi.
3. Scegli lingua, destinatari, lunghezza e priorità. Nel prompt completo modifica soltanto i valori tra parentesi quadre in `USER INPUT — EDIT ONLY THIS SECTION`. Questo esempio configura la richiesta senza presumere che file o strumenti siano accessibili.

```text
OUTPUT_LANGUAGE = [Italiano]
RESEARCH_CONTEXT = [Identificare discipline, metodi e tipi di prova nel materiale fornito.]
CAPABILITY_MODE = [Usare capacità osservate e dichiarare le verifiche non disponibili.]
AUDIENCE = [Professional]
OUTPUT_LENGTH = [Detailed]
ANALYSIS_DEPTH = [Deep]
PRIORITY_FOCUS = [All applicable areas]
OUTPUT_FORMAT = [Structured forensic report]
SPECIAL_INSTRUCTIONS = [Indicare posizioni esatte, verificare spiegazioni innocue e proporre i successivi controlli umani.]
MATERIALS = [Elencare file o estratti forniti, versioni e ambito richiesto.]
```

La lunghezza può essere `Short`, `Standard`, `Detailed` o `Exhaustive`; i destinatari `Beginner`, `General`, `Researcher`, `Professional` o `Expert`. Richieste come «controlla le ipotesi della dimostrazione» o «confronta la tabella 2 con i metodi» rendono l’esame più utile. Se manca materiale valutabile, l’assistente deve richiederlo e dichiarare l’insufficienza delle prove.

`ANALYSIS_DEPTH` accetta `Standard`, `Deep` o `Maximum`: controlli essenziali applicabili, esame più approfondito o revisione più ampia consentita dalle prove e dagli strumenti disponibili. Aumentare la profondità non crea capacità mancanti. Gli altri campi descrittivi accolgono le tue istruzioni su contesto, priorità, richieste particolari e materiali forniti. In `OUTPUT_FORMAT` puoi chiedere, per esempio, una sintesi per i decisori o un rapporto tecnico.

### Scegliere formato e materiali

| Formato | Quando usarlo | Requisiti |
| --- | --- | --- |
| [Prompt completo][download-prompt] | Esame approfondito con un assistente capace di leggere testo | Protocollo principale e materiale leggibile |
| [Richiesta breve](QUICKSTART.md) | Prima selezione o contesto ridotto | Richiesta copiabile e ambito definito |
| [Skill autonomo][download-skill] | Host compatibile con il formato aperto Agent Skills | Cartella completa `academic-paper-audit` con risorse collegate |
| [Plugin facoltativo][download-plugin] | Host compatibile con il pacchetto plugin | Loader adatto; installazione e individuazione dipendono dall’host |

Usa un formato per esame. Il percorso testuale non richiede Python, chiavi API o integrazioni con fornitori. La [pagina della versione][release] offre tre archivi e [checksum SHA-256][checksums]. La corrispondenza verifica i byte scaricati, non l’autenticità della fonte scientifica.

I controlli seguono il metodo: denominatori, campionamento e incertezza nel quantitativo; contesto delle citazioni e percorso analitico nel qualitativo; separazione dei dati ed esecuzione reale nel computazionale. I lavori formali richiedono ipotesi, quantificatori e controesempi; l’ingegneria, unità, calibrazione e condizioni al contorno; gli archivi, edizioni, date e trascrizioni. Metodi misti, sintesi e ricerca concettuale o basata sulla pratica richiedono criteri coerenti con le proprie affermazioni. L’elenco rimane aperto. Valori p, preregistrazione, dati grezzi pubblici e DOI non sono obblighi universali.

Quando una domanda dipende da figure originali o documenti fonte, fornisci quelli disponibili. Un PDF compresso può consentire una lettura testuale senza sostenere conclusioni su pixel o metadati. Visione, web e strumenti specialistici ampliano l’ambito solo se sono realmente utilizzabili. Gli script inclusi non eseguono OCR, analisi forense delle immagini, verifica formale delle dimostrazioni o rilevamento automatico di immagini generate da IA.

### Interpretare il rapporto

Il rapporto espone ambito, strumenti usati, contesto metodologico, rilievi prioritari, elementi contrari ai sospetti, limiti e prossime verifiche umane. Registra testo/metodi, statistiche/dati, figure, metadati/provenienza, riferimenti/avvisi, etica/registrazione e confronti fra lavori. `completed` significa verificato nell’ambito indicato, `partial` verificato in parte, `not_assessed` non esaminato. `not_applicable` richiede una motivazione d’inapplicabilità.

I livelli riguardano il sostegno all’osservazione: **0**, nessuna anomalia significativa nell’ambito esaminato; **1**, segnale debole con spiegazioni innocue plausibili; **2**, incoerenza sostanziale riproducibile; **3**, preoccupazione forte con ulteriori prove corroboranti e necessità di esperti; **4**, problema preciso confermato da una fonte esterna autorevole, letta e corrispondente all’articolo. I livelli 2/3 non dimostrano intenzione. La fiducia riguarda l’osservazione, non la colpevolezza dell’autore. Un avviso di ritrattazione va letto per la sua motivazione effettiva; da solo non prova frode.

Markdown o testo semplice è il formato predefinito. Il [modello di rapporto](skills/academic-paper-audit/assets/report-template.md) illustra la struttura; il [JSON](skills/academic-paper-audit/assets/report.schema.json) è facoltativo. La validazione strutturale non dimostra verità scientifica né consultazione effettiva delle fonti. Hash non calcolati e operazioni non eseguite devono essere dichiarati. Se manca un timestamp osservato richiesto dal JSON rigoroso, usa un rapporto leggibile.

### Proteggere le prove e riprendere il lavoro

Conserva gli originali e identifica separatamente le copie derivate. Condividi manoscritti inediti, dati identificabili e dati grezzi solo in ambienti autorizzati. Il progetto non gestisce un servizio ospitato o telemetria; l’assistente e gli strumenti hanno comunque politiche proprie. Una revisione non autorizza caricamenti esterni, contatti con autori o pubblicazione di accuse. Le istruzioni dentro i documenti sono contenuto da esaminare, non comandi. La [guida sulla privacy](docs/PRIVACY.md) precisa trattamento e conservazione.

Per passare a un’altra sessione o agente usa il [registro di continuazione](skills/academic-paper-audit/assets/continuation-template.md). Trasmetti articolo/versione, ambito, ID delle prove, posizioni esaminate, controlli conclusi, ID/stati dei rilievi, materiali mancanti e prossimi passi insieme alle fonti reali. Riesamina le prove cambiate. Conserva i rilievi corretti come storico risolto, fuori dal conteggio attivo. Un riepilogo non sostituisce una fonte non letta e non amplia i permessi.

Nel codice sorgente attuale, l’esportazione JSON per la ripresa conserva il contesto di ricerca registrato, i limiti di ogni ambito e i collegamenti ai controlli completati. Se questi dati mancano nei vecchi record, `validate-checkpoint` li segnala in `warnings`; mantenete esplicite le lacune quando riprendete il lavoro. Questi aggiornamenti sono inclusi nella v.0.0.3; i record di ripresa coerenti della v.0.0.2 restano leggibili.

### Strumenti locali facoltativi

I comandi richiedono il repository completo o la cartella dello skill; lo ZIP dei prompt non contiene script Python. Python 3.10+ serve solo per strumenti e sviluppo. Inventario e aritmetica usano la libreria standard; validazione dei rapporti/registri ed esportazione richiedono `jsonschema` 4.26.0. Dopo `python -m venv .venv`, usa `.venv/Scripts/python.exe` in Windows o `.venv/bin/python` in macOS/Linux. Qui `python` indica quell’interprete; esegui dalla radice del repository.

Per questi comandi scarica il [repository completo][download-source]. In uno skill installato segui [SKILL.md](skills/academic-paper-audit/SKILL.md), che usa percorsi relativi alla sua cartella.

```text
python -m pip install -r skills/academic-paper-audit/requirements.txt
python skills/academic-paper-audit/scripts/audit_tools.py inventory --root tests/fixtures synthetic_manuscript.md
python skills/academic-paper-audit/scripts/audit_tools.py percentage --count 1 --total 3 --reported 33.3 --places 1
python skills/academic-paper-audit/scripts/audit_tools.py flow --initial 100 --excluded 10 --dropouts 5 --analyzed 90 --disjoint
python skills/academic-paper-audit/scripts/audit_tools.py validate-report examples/synthetic-report.json
python skills/academic-paper-audit/scripts/audit_tools.py checkpoint examples/synthetic-report.json
python skills/academic-paper-audit/scripts/audit_tools.py validate-checkpoint examples/synthetic-checkpoint.json
```

Gli esempi sono sintetici. L’inventario accetta percorsi relativi a `--root` e restituisce dimensioni in byte e SHA-256. La percentuale presuppone conteggi non ponderati e arrotondamento ordinario; il flusso, perdite distinte nella stessa popolazione e nello stesso momento. I calcoli non assegnano livelli di prova. L’esportazione scrive JSON su stdout, da salvare in UTF-8. Codici d’uscita: 0 per calcolo riuscito/record validi, 1 per rapporto o registro non valido, 2 per errori d’ingresso o dipendenze. Una discrepanza aritmetica è un risultato valido del calcolo.

### Verifica, assistenza e licenza

Il progetto comprende 81 test comportamentali e una matrice CI Windows/Ubuntu con Python 3.10 e 3.14. La versione v.0.0.2 corregge il confronto temporale dell’inventario Windows, mantenendo i controlli sull’identità e sulle modifiche effettive dei file. Richiesta breve, protocollo completo e skill hanno superato ciascuno 16 casi sintetici e 48 criteri valutati da un modello, inclusi controlli senza problemi, prove insufficienti e un rilievo risolto. Non sono misure di accuratezza scientifica. Le prove effettive negli ambienti host e i relativi insuccessi sono documentati nella guida di validazione; i risultati valgono solo per tali esecuzioni. L’esecuzione macOS e le prestazioni esperte in ogni lingua, modalità e disciplina restano non verificate. La [guida di validazione](docs/VALIDATION.md) documenta prove, limiti e riproduzione.

Per problemi riproducibili usa il [modulo][issues] con un esempio minimo sintetico o condivisibile. [Contributing](CONTRIBUTING.md) descrive sviluppo e pubblicazioni, [CHANGELOG.md](CHANGELOG.md) le modifiche. Il progetto è sotto [licenza MIT](LICENSE). Questa sezione è una guida utente completa; i documenti tecnici aggiuntivi sono mantenuti in inglese.

[↑ Torna in cima](#top)

---

<a id="lang-pt"></a>
## Português

### Objetivo e alcance

Academic Paper Forensic & Research Integrity Auditor ajuda pesquisadores, pareceristas, editores, estudantes e profissionais de integridade científica a fazer uma primeira análise estruturada de trabalhos acadêmicos. O recurso central é um protocolo reutilizável para o assistente de IA de sua preferência. A revisão acompanha as afirmações, os métodos e as evidências do trabalho, sem impor a mesma lista experimental a todas as disciplinas.

Conforme os materiais e as ferramentas disponíveis, a análise pode examinar argumentos e demonstrações, coerência entre métodos e resultados, números, avaliações computacionais, atribuição de fontes, figuras, procedência, referências, avisos e comparações entre publicações. Lacunas de relato, limitações metodológicas, divergências acadêmicas e preocupações específicas de integridade são tratadas separadamente. Um achado relevante deve indicar a localização exata, uma verificação reproduzível, uma explicação benigna plausível e o próximo passo de conferência humana.

É uma triagem assistida por IA. Decisões com consequências exigem revisão humana independente. Uma anomalia não demonstra má conduta ou intenção, e a ausência de achados não comprova autenticidade. O protocolo apoia o julgamento, sem substituir um especialista da área, um laboratório ou uma investigação institucional.

### Começar com o assistente que você já usa

1. Baixe o [pacote de prompts][download-prompt] ou abra [master_prompt.md](master_prompt.md). Cole o protocolo completo ou anexe uma cópia legível. Para uma primeira análise delimitada, use a solicitação de [QUICKSTART.md](QUICKSTART.md).
2. Forneça o artigo ou trechos pertinentes e os materiais complementares que você pode compartilhar. Identifique a versão, as páginas, figuras, argumentos e perguntas de interesse. Se o assistente não conseguir ler um anexo, cole passagens específicas e limite expressamente a revisão a elas.
3. Defina idioma, público, extensão e prioridade. No prompt completo, altere apenas os valores entre colchetes de `USER INPUT — EDIT ONLY THIS SECTION`. O exemplo configura a solicitação; não pressupõe que arquivos ou ferramentas estejam acessíveis.

```text
OUTPUT_LANGUAGE = [Português]
RESEARCH_CONTEXT = [Identificar disciplinas, métodos e tipos de evidência do material fornecido.]
CAPABILITY_MODE = [Usar capacidades observadas e informar as verificações indisponíveis.]
AUDIENCE = [Professional]
OUTPUT_LENGTH = [Detailed]
ANALYSIS_DEPTH = [Deep]
PRIORITY_FOCUS = [All applicable areas]
OUTPUT_FORMAT = [Structured forensic report]
SPECIAL_INSTRUCTIONS = [Indicar locais exatos, testar explicações benignas e apontar as próximas verificações humanas.]
MATERIALS = [Listar arquivos ou trechos fornecidos, versões e alcance solicitado.]
```

Para extensão, escolha `Short`, `Standard`, `Detailed` ou `Exhaustive`; para público, `Beginner`, `General`, `Researcher`, `Professional` ou `Expert`. Pedidos como “verificar as hipóteses da demonstração” ou “comparar a tabela 2 com os métodos” tornam o resultado mais útil. Sem material avaliável, o assistente deve solicitá-lo e registrar evidência insuficiente.

`ANALYSIS_DEPTH` aceita `Standard`, `Deep` ou `Maximum`: verificações essenciais aplicáveis, exame mais detalhado ou revisão mais ampla permitida pelas evidências e ferramentas disponíveis. Maior profundidade não cria capacidades ausentes. Os outros campos descritivos aceitam suas instruções sobre contexto, prioridades, pedidos específicos e materiais fornecidos. Em `OUTPUT_FORMAT`, você pode solicitar um resumo executivo ou relatório técnico, por exemplo.

### Escolher o formato e as evidências

| Formato | Quando usar | Requisitos |
| --- | --- | --- |
| [Prompt completo][download-prompt] | Revisão aprofundada em um assistente que leia texto | Protocolo principal e material legível |
| [Solicitação curta](QUICKSTART.md) | Triagem inicial ou contexto reduzido | Pedido copiável e alcance definido |
| [Skill independente][download-skill] | Ambiente compatível com pastas do formato aberto Agent Skills | Pasta completa `academic-paper-audit` com recursos vinculados |
| [Plugin opcional][download-plugin] | Ambiente compatível com o pacote de plugin | Carregador adequado; instalação e descoberta dependem do ambiente |

Use um formato por revisão. O caminho textual dispensa Python, chave de API e integração com um fornecedor. A [página da versão][release] oferece três arquivos e [somas SHA-256][checksums]. Uma soma correspondente verifica os bytes baixados, não a autenticidade da fonte científica.

Os critérios seguem o método: denominadores, amostragem e incerteza em estudos quantitativos; contexto das citações e percurso analítico em qualitativos; separação de dados e execução efetiva em computacionais. Trabalhos formais exigem hipóteses, quantificadores e contraexemplos; engenharia, unidades, calibração e condições de contorno; arquivos, edições, datas e transcrições. Métodos mistos, sínteses e pesquisas conceituais ou baseadas na prática precisam de critérios coerentes com suas afirmações. A lista é aberta. Valores p, pré-registro, dados brutos públicos e DOI não são exigências universais.

Quando a pergunta depender de figuras originais ou documentos-fonte, forneça-os se possível. Um PDF comprimido pode permitir análise textual sem sustentar conclusões sobre pixels ou metadados. Visão, web e ferramentas especializadas ampliam o alcance apenas quando realmente disponíveis. Os scripts incluídos não fazem OCR, perícia de imagens, verificação formal de demonstrações ou detecção automática de imagens geradas por IA.

### Entender o relatório

O relatório explica alcance, ferramentas usadas, contexto metodológico, achados prioritários, evidências que enfraquecem suspeitas, limitações e próximos controles humanos. Registra texto/métodos, estatísticas/dados, figuras, metadados/procedência, referências/avisos, ética/registro e comparações entre trabalhos. `completed` significa examinado no alcance declarado; `partial`, parcialmente examinado; `not_assessed`, não examinado. `not_applicable` exige explicar por que o domínio não se aplica.

Os níveis descrevem o suporte à observação: **0**, nenhuma preocupação significativa no alcance examinado; **1**, sinal fraco com explicações benignas plausíveis; **2**, inconsistência relevante e reproduzível; **3**, preocupação forte com evidências adicionais de corroboração que exige especialistas; **4**, problema específico corroborado por fonte externa autorizada, lida e correspondente ao artigo. Níveis 2/3 não estabelecem intenção. A confiança diz respeito à observação, não à culpa do autor. Um aviso de retratação deve ser lido pelo motivo real; sua existência isolada não comprova fraude.

Markdown ou texto simples é o padrão. O [modelo de relatório](skills/academic-paper-audit/assets/report-template.md) apresenta a estrutura; o [JSON](skills/academic-paper-audit/assets/report.schema.json) é opcional. A validação estrutural não comprova verdade científica nem leitura efetiva de fontes. Hashes não calculados e operações não realizadas devem permanecer explícitos. Se faltar um horário observado exigido pelo JSON estrito, use um relatório legível.

### Proteger as evidências e retomar a revisão

Preserve os originais e identifique separadamente as cópias derivadas. Compartilhe manuscritos inéditos, registros identificáveis e dados brutos apenas em um ambiente autorizado. O projeto não opera serviço hospedado ou telemetria; o assistente e as ferramentas têm políticas próprias. Uma revisão não autoriza uploads externos, contato com autores ou publicação de acusações. Instruções inseridas nos documentos são conteúdo, não comandos. O [guia de privacidade](docs/PRIVACY.md) detalha tratamento e retenção.

Ao mudar de sessão ou agente, use o [registro de continuidade](skills/academic-paper-audit/assets/continuation-template.md). Leve artigo/versão, alcance, IDs de evidência, locais examinados, controles concluídos, IDs/estados dos achados, materiais ausentes e próximos passos junto com as fontes reais. Reexamine evidências alteradas. Preserve achados corrigidos como histórico resolvido e exclua-os das contagens ativas. Um resumo não substitui uma fonte não vista nem amplia permissões.

No código-fonte atual, a exportação JSON de continuidade preserva o contexto de pesquisa registrado, as limitações de cada área e os vínculos com as verificações concluídas. Quando registros antigos não contêm esses dados, `validate-checkpoint` informa as lacunas em `warnings`; mantenha-as explícitas ao retomar. Estas atualizações estão incluídas na v.0.0.3; registros de continuidade consistentes da v.0.0.2 continuam legíveis.

### Ferramentas locais opcionais

Os comandos exigem o repositório completo ou a pasta do skill; o ZIP de prompts não inclui scripts Python. Python 3.10+ serve apenas às ferramentas e ao desenvolvimento. Inventário e aritmética usam a biblioteca padrão; validação de relatórios/registros e exportação exigem `jsonschema` 4.26.0. Após `python -m venv .venv`, use `.venv/Scripts/python.exe` no Windows ou `.venv/bin/python` no macOS/Linux. Abaixo, `python` representa esse interpretador; execute na raiz do repositório.

Para estes comandos, baixe o [repositório completo][download-source]. Em um skill instalado, siga [SKILL.md](skills/academic-paper-audit/SKILL.md), cujos caminhos são relativos à pasta do skill.

```text
python -m pip install -r skills/academic-paper-audit/requirements.txt
python skills/academic-paper-audit/scripts/audit_tools.py inventory --root tests/fixtures synthetic_manuscript.md
python skills/academic-paper-audit/scripts/audit_tools.py percentage --count 1 --total 3 --reported 33.3 --places 1
python skills/academic-paper-audit/scripts/audit_tools.py flow --initial 100 --excluded 10 --dropouts 5 --analyzed 90 --disjoint
python skills/academic-paper-audit/scripts/audit_tools.py validate-report examples/synthetic-report.json
python skills/academic-paper-audit/scripts/audit_tools.py checkpoint examples/synthetic-report.json
python skills/academic-paper-audit/scripts/audit_tools.py validate-checkpoint examples/synthetic-checkpoint.json
```

Os exemplos são sintéticos. O inventário aceita caminhos relativos a `--root` e informa tamanhos em bytes e SHA-256. A porcentagem supõe contagens sem ponderação e arredondamento usual; o fluxo, perdas distintas na mesma população e momento. Os cálculos não atribuem nível de evidência. A exportação escreve JSON em stdout, para salvar como UTF-8. Códigos: 0 para cálculo concluído/registros válidos, 1 para relatório ou registro inválido, 2 para erro de entrada ou dependência. Uma divergência aritmética é um resultado válido do cálculo.

### Validação, ajuda e licença

O projeto inclui 81 testes de comportamento e uma matriz CI Windows/Ubuntu com Python 3.10 e 3.14. A versão v.0.0.2 corrige a comparação temporal do inventário Windows e mantém as verificações de identidade e alterações reais dos arquivos. Solicitação curta, protocolo completo e skill passaram, cada um, por 16 casos sintéticos e 48 critérios julgados por um modelo, incluindo controles legítimos, evidência insuficiente e um achado resolvido. Esses resultados não medem precisão científica. Os testes reais nos ambientes hospedeiros e suas falhas estão registrados no guia de validação; os resultados se limitam àquelas execuções. A execução em macOS e o desempenho especializado em todos os idiomas, modalidades e disciplinas continuam sem comprovação. O [guia de validação](docs/VALIDATION.md) apresenta evidências, limites e reprodução.

Relate problemas reproduzíveis no [formulário][issues] com um exemplo mínimo sintético ou compartilhável. [Contributing](CONTRIBUTING.md) explica desenvolvimento e publicações; [CHANGELOG.md](CHANGELOG.md), as mudanças. O projeto usa a [licença MIT](LICENSE). Esta seção é um guia completo de uso; os documentos técnicos adicionais são mantidos em inglês.

[↑ Voltar ao início](#top)

---

<a id="lang-ar"></a>
## العربية

### الهدف ونطاق الاستخدام

يساعد مشروع Academic Paper Forensic & Research Integrity Auditor الباحثين والمحكّمين والمحررين والطلاب والمتخصصين في نزاهة البحث على إجراء مراجعة أولية منظمة للأعمال الأكاديمية. أساسه بروتوكول قابل لإعادة الاستخدام تقدّمه إلى مساعد الذكاء الاصطناعي الذي تختاره. تُختار الفحوص وفق ادعاءات العمل ومنهجه وأدلته، بدلاً من فرض قائمة تجريبية واحدة على جميع التخصصات.

يمكن، بحسب المواد والأدوات المتاحة فعلياً، مراجعة الحجج والبراهين، واتساق المنهج والنتائج، والأرقام، والتقييم الحاسوبي، ونسبة الأقوال إلى مصادرها، والأشكال، والمنشأ، والمراجع، والإشعارات، والمقارنة بين المنشورات. يميّز التقرير بين نقص العرض، والقصور المنهجي، والخلاف العلمي، ومشكلة نزاهة محددة. ويحتاج كل استنتاج مهم إلى موضع دقيق، وطريقة لإعادة التحقق، وتفسير سليم محتمل، وخطوة تالية للمراجعة البشرية.

هذه مراجعة أولية بمساعدة الذكاء الاصطناعي. القرارات ذات العواقب تتطلب تحققاً بشرياً مستقلاً. الشذوذ لا يثبت سوء السلوك أو القصد، وغياب الملاحظات لا يثبت الأصالة. يدعم البروتوكول الحكم المتخصص، لكنه لا يحل محل خبير المجال أو المختبر أو التحقيق المؤسسي.

### البدء بالمساعد الذي تستخدمه

1. نزّل [حزمة الموجّه][download-prompt] أو افتح [master_prompt.md](master_prompt.md). الصق البروتوكول كاملاً أو أرفقه في ملف مقروء. للمراجعة الأولية المحدودة، استخدم الطلب الموجود في [QUICKSTART.md](QUICKSTART.md).
2. قدّم الورقة أو المقاطع ذات الصلة والمواد الداعمة المسموح لك بمشاركتها. حدّد النسخة والصفحات والأشكال والحجج وأسئلة المراجعة. إذا تعذرت قراءة المرفق، الصق مقاطع محددة واطلب صراحةً حصر المراجعة فيها.
3. اختر لغة التقرير وجمهوره وطوله وأولوياته. في الموجّه الكامل، غيّر القيم بين الأقواس المربعة فقط في `USER INPUT — EDIT ONLY THIS SECTION`. المثال التالي يحدد الطلب ولا يؤكد توفر ملفات أو أدوات.

```text
OUTPUT_LANGUAGE = [العربية]
RESEARCH_CONTEXT = [حدّد التخصصات والمناهج وأنواع الأدلة في المادة المقدمة.]
CAPABILITY_MODE = [استخدم القدرات المتحقق من توفرها واذكر الفحوص غير المتاحة.]
AUDIENCE = [Professional]
OUTPUT_LENGTH = [Detailed]
ANALYSIS_DEPTH = [Deep]
PRIORITY_FOCUS = [All applicable areas]
OUTPUT_FORMAT = [Structured forensic report]
SPECIAL_INSTRUCTIONS = [اذكر مواضع الأدلة بدقة، واختبر التفسيرات السليمة، وحدّد خطوات التحقق البشري التالية.]
MATERIALS = [اذكر الملفات أو المقاطع المقدمة ونسخها ونطاق المراجعة المطلوب.]
```

خيارات الطول هي `Short` و`Standard` و`Detailed` و`Exhaustive`، وخيارات الجمهور `Beginner` و`General` و`Researcher` و`Professional` و`Expert`. طلب محدد، مثل فحص فرضيات برهان أو مطابقة الجدول 2 مع المنهج، يجعل النتيجة أكثر فائدة. إن لم توجد مادة قابلة للتقييم، فالنتيجة المناسبة طلبها وبيان عدم كفاية الأدلة.

يقبل `ANALYSIS_DEPTH` الخيارات `Standard` أو `Deep` أو `Maximum`: الفحوص الأساسية المنطبقة، أو فحصاً أعمق، أو أوسع مراجعة مفيدة تسمح بها الأدلة والأدوات المتاحة. زيادة العمق لا توفر قدرات غير موجودة. تقبل الحقول الوصفية الأخرى تعليماتك عن سياق البحث والأولويات والطلبات الخاصة والمواد المقدمة. ويمكن أن تطلب في `OUTPUT_FORMAT` ملخصاً تنفيذياً أو تقريراً تقنياً، مثلاً.

### اختيار الصيغة والأدلة المناسبة

| الصيغة | الاستخدام | المتطلبات |
| --- | --- | --- |
| [الموجّه الكامل][download-prompt] | مراجعة مفصلة بمساعد يستطيع قراءة النص | البروتوكول الرئيسي ومادة بحثية مقروءة |
| [الطلب المختصر](QUICKSTART.md) | الفرز الأولي أو نافذة سياق صغيرة | الطلب القابل للنسخ ونطاق محدد |
| [Skill مستقل][download-skill] | بيئة تدعم صيغة مجلدات Agent Skills المفتوحة | مجلد `academic-paper-audit` كاملاً مع موارده المرتبطة |
| [Plugin اختياري][download-plugin] | بيئة تدعم حزمة الإضافة | أداة تحميل متوافقة؛ التثبيت والاكتشاف يعتمدان على البيئة |

استخدم صيغة واحدة لكل مراجعة. لا يتطلب المسار النصي Python أو مفتاح API أو تكاملاً مع مزود بعينه. تتضمن [صفحة الإصدار][release] الحزم الثلاث و[قيم SHA-256][checksums]. تطابق القيمة يتحقق من بايتات التنزيل، لا من أصالة المصدر البحثي.

تتبع المعايير المنهج الفعلي: المقامات وأخذ العينات وعدم اليقين في البحوث الكمية؛ سياق الاقتباسات ومسار التحليل في النوعية؛ وتقسيم البيانات والتنفيذ الفعلي في الحاسوبية. تحتاج الأعمال الصورية إلى الفرضيات والمكممات والأمثلة المضادة، والهندسة إلى الوحدات والمعايرة والشروط الحدّية، والبحوث الأرشيفية إلى الطبعات والتواريخ والنسخ النصي. وتُراجع المناهج المختلطة وتوليف الأدلة والأعمال المفاهيمية والقائمة على الممارسة وفق ادعاءاتها. هذه أمثلة وليست قائمة مغلقة. قيم p والتسجيل المسبق والبيانات الخام العلنية وDOI ليست شروطاً عامة لكل بحث.

قدّم الأشكال الأصلية أو سجلات المصدر عندما تعتمد المسألة عليها. قد يسمح PDF مضغوط بمراجعة نصية، لكنه لا يبرر بالضرورة استنتاجات عن البكسلات أو البيانات الوصفية. توسّع أدوات الرؤية والويب والأدوات المتخصصة النطاق فقط إن كانت متاحة فعلياً. البرامج المساعدة هنا ليست محركات OCR أو تحليل جنائي للصور أو تحقق صوري من البراهين أو كشف آلي للصور المولدة بالذكاء الاصطناعي.

### فهم التقرير

يوضح التقرير النطاق المفحوص، والأدوات المستخدمة، والسياق المنهجي، والملاحظات ذات الأولوية، والأدلة التي تضعف الشبهات، والقيود، وخطوات التحقق البشرية التالية. ويسجل تغطية النص والمنهج، والإحصاء والبيانات، والأشكال، والبيانات الوصفية والمنشأ، والمراجع والإشعارات، والأخلاقيات والتسجيل، والمقارنة بين الأعمال. تعني `completed` فحص النطاق المحدد، و`partial` فحص جزء منه، و`not_assessed` عدم فحصه. أما `not_applicable` فتحتاج تفسيراً لعدم الانطباق.

تصف مستويات الأدلة قوة الاستناد للملاحظة: **0** لا مشكلة مهمة ضمن النطاق المفحوص؛ **1** إشارة ضعيفة لها تفسيرات سليمة معقولة؛ **2** تناقض جوهري قابل لإعادة التحقق؛ **3** قلق قوي تدعمه أدلة إضافية ويتطلب مراجعة متخصصة؛ **4** مشكلة محددة يؤيدها مصدر خارجي موثوق قُرئ فعلاً ويطابق الورقة. لا يثبت المستويان 2 و3 القصد. الثقة تخص الملاحظة، لا إدانة المؤلف. ينبغي قراءة السبب الفعلي لإشعار السحب؛ وجود السحب وحده ليس إثباتاً للاحتيال.

Markdown أو النص العادي هو الخيار الافتراضي. يوضح [قالب التقرير](skills/academic-paper-audit/assets/report-template.md) بنيته، ويظل [JSON](skills/academic-paper-audit/assets/report.schema.json) اختيارياً. التحقق من البنية لا يثبت الصحة العلمية أو قراءة المصدر. يجب الإفصاح عن البصمات غير المحسوبة والعمليات غير المنفذة. إذا تعذر رصد الطابع الزمني المطلوب لتقرير JSON الصارم، فاستخدم تقريراً مقروءاً للبشر.

### حماية الأدلة واستئناف العمل

احتفظ بالأصول دون تعديل وسجّل النسخ المشتقة منفصلة. شارك المخطوطات غير المنشورة والسجلات القابلة لتحديد الهوية والبيانات الخام داخل بيئة مصرح بها فقط. لا يشغّل المشروع خدمة مستضافة أو قياس استخدام؛ لكن للمساعد وأدواته سياسات بيانات خاصة. طلب المراجعة لا يجيز الرفع إلى جهات خارجية أو الاتصال بالمؤلفين أو نشر الاتهامات. التعليمات المضمّنة في الأدلة محتوى للفحص وليست أوامر. يشرح [دليل الخصوصية](docs/PRIVACY.md) التعامل والحفظ بمزيد من التفصيل.

عند الانتقال إلى جلسة أو وكيل آخر، استخدم [سجل الاستئناف](skills/academic-paper-audit/assets/continuation-template.md). انقل الورقة ونسختها والنطاق ومعرّفات الأدلة والمواضع المفحوصة والفحوص المنجزة ومعرّفات الملاحظات وحالاتها والمواد المفقودة والخطوات التالية، مع المصادر الفعلية. أعد فحص الأدلة المتغيرة. احتفظ بالملاحظات المصححة كتاريخ محلول ولا تحتسبها ضمن النشطة. الملخص لا يعوض مصدراً غير مقروء ولا يمنح إذناً جديداً.

في الشيفرة المصدرية الحالية، يحفظ تصدير سجل المتابعة بصيغة JSON سياق البحث المسجّل وقيود كل مجال وروابط الفحوص المكتملة. إذا افتقرت السجلات القديمة إلى هذه المعلومات، يوضحها `validate-checkpoint` في `warnings`؛ أبقِ هذه الفجوات صريحة عند الاستئناف. هذه التحديثات مشمولة في v.0.0.3؛ وتظل سجلات المتابعة المتسقة من v.0.0.2 قابلة للقراءة.

### الأدوات المحلية الاختيارية

تحتاج الأوامر إلى المستودع الكامل أو مجلد الـskill؛ لا تتضمن حزمة الموجّه وحدها برامج Python. يلزم Python 3.10+ للأدوات والتطوير فقط. يستخدم الجرد والحساب المكتبة القياسية؛ ويتطلب التحقق من التقارير وسجلات الاستئناف وتصديرها `jsonschema` 4.26.0. بعد `python -m venv .venv` يكون المفسّر `.venv/Scripts/python.exe` في Windows أو `.venv/bin/python` في macOS/Linux. تشير `python` أدناه إلى مفسّر بيئتك؛ نفّذ من جذر المستودع.

لهذه الأوامر، نزّل [المستودع الكامل][download-source]. داخل skill مثبّت، اتبع [SKILL.md](skills/academic-paper-audit/SKILL.md)، إذ تُكتب مسارات أوامره نسبةً إلى مجلده.

```text
python -m pip install -r skills/academic-paper-audit/requirements.txt
python skills/academic-paper-audit/scripts/audit_tools.py inventory --root tests/fixtures synthetic_manuscript.md
python skills/academic-paper-audit/scripts/audit_tools.py percentage --count 1 --total 3 --reported 33.3 --places 1
python skills/academic-paper-audit/scripts/audit_tools.py flow --initial 100 --excluded 10 --dropouts 5 --analyzed 90 --disjoint
python skills/academic-paper-audit/scripts/audit_tools.py validate-report examples/synthetic-report.json
python skills/academic-paper-audit/scripts/audit_tools.py checkpoint examples/synthetic-report.json
python skills/academic-paper-audit/scripts/audit_tools.py validate-checkpoint examples/synthetic-checkpoint.json
```

الأمثلة اصطناعية. يقبل الجرد مسارات نسبةً إلى `--root` ويُخرج الأحجام بالبايت وSHA-256. يفترض فحص النسبة أعداداً غير موزونة وتقريباً معتاداً، ويفترض فحص التدفق استبعادات غير متداخلة من السكان والفترة نفسيهما. لا تمنح الحسابات مستوى أدلة. يكتب التصدير JSON إلى stdout؛ احفظه بترميز UTF-8 عند الحاجة. رموز الخروج: 0 للحساب الناجح أو السجل الصحيح، و1 لتقرير أو سجل غير صالح، و2 لخطأ مدخلات أو اعتماديات. عدم تطابق الأرقام نتيجة حساب صحيحة وليس فشلاً برمجياً.

### التحقق والمساعدة والترخيص

يتضمن المشروع 81 اختباراً سلوكياً ومصفوفة CI على Windows وUbuntu مع Python 3.10 و3.14. يصحح الإصدار v.0.0.2 مقارنة الحقول الزمنية في جرد Windows مع الحفاظ على فحوص هوية الملف والتغييرات الفعلية. اجتاز كل من الطلب المختصر والموجّه الكامل والـskill ست عشرة حالة اصطناعية و48 معياراً بتقييم نموذج، تشمل حالات سليمة وأدلة غير كافية وملاحظة حُلّت بتصحيح. هذه نتائج قبول وليست قياسات للدقة العلمية. يوثّق دليل التحقق اختبارات البيئات الفعلية وإخفاقاتها؛ وتنطبق النتائج على تلك التشغيلات فقط. لم يُثبت تشغيل macOS أو الأداء المتخصص في جميع اللغات والوسائط والتخصصات. يوثّق [دليل التحقق](docs/VALIDATION.md) الأدلة والقيود وإعادة التنفيذ.

للأخطاء القابلة للتكرار، استخدم [النموذج][issues] مع مثال اصطناعي صغير أو مأذون بمشاركته. يشرح [دليل المساهمة](CONTRIBUTING.md) التطوير والإصدارات، ويسجل [CHANGELOG.md](CHANGELOG.md) التغييرات. يتاح المشروع وفق [ترخيص MIT](LICENSE). هذا القسم دليل استخدام كامل؛ تُصان الوثائق التقنية الإضافية بالإنجليزية.

[↑ العودة إلى الأعلى](#top)

---

<a id="lang-zh-cn"></a>
## 简体中文

### 项目用途与适用范围

Academic Paper Forensic & Research Integrity Auditor 面向研究人员、审稿人、编辑、学生及研究诚信工作者，帮助他们对学术作品进行有据可查的初步审查。项目的核心是一份可重复使用的审查协议，可以交给你惯用的 AI 助手。检查项目依据材料中的主张、方法和证据选择，不会把同一套实验研究清单强加给所有学科。

根据实际提供的材料和工具，可以检查论证与证明、方法和结果的一致性、数值主张、计算评估、来源归属、图像、溯源信息、参考文献、出版通知以及论文之间的对应关系。报告会区分报告不充分、方法局限、学术分歧与具体的研究诚信问题。重要发现应有准确位置、可重复的核查步骤、合理的无过错解释，以及下一步人工核查建议。

这是 AI 辅助初筛。涉及重要后果的决定必须经过独立人工核查。异常不能证明不端或主观意图；没有发现异常也不能证明真实性。协议用于支持判断，不能替代领域专家、鉴证实验室或机构调查。

### 使用现有助手开始审查

1. 下载[提示词包][download-prompt]，或打开 [master_prompt.md](master_prompt.md)。将完整协议粘贴给助手，或作为可读取的文件附上。如果只需要范围较小的初筛，可以使用 [QUICKSTART.md](QUICKSTART.md) 中的请求。
2. 提供论文、相关摘录及获准分享的辅助材料，说明版本、页码、图表、论证及希望回答的问题。若附件无法读取，就粘贴具体段落，并明确要求只对这些摘录作出判断。
3. 设置输出语言、读者、篇幅和重点。在完整提示词末尾的 `USER INPUT — EDIT ONLY THIS SECTION` 中，只修改方括号内的值。下面是请求配置示例，并不表示相关文件或工具已经可用。

```text
OUTPUT_LANGUAGE = [简体中文]
RESEARCH_CONTEXT = [识别所提供材料的学科、研究方法和证据类型。]
CAPABILITY_MODE = [仅使用实际确认的能力，并说明无法完成的检查。]
AUDIENCE = [Professional]
OUTPUT_LENGTH = [Detailed]
ANALYSIS_DEPTH = [Deep]
PRIORITY_FOCUS = [All applicable areas]
OUTPUT_FORMAT = [Structured forensic report]
SPECIAL_INSTRUCTIONS = [给出证据的准确位置，检验合理的无过错解释，并说明下一步人工核查。]
MATERIALS = [列出提供的文件或摘录、版本及本次审查范围。]
```

篇幅可选 `Short`、`Standard`、`Detailed`、`Exhaustive`；读者可选 `Beginner`、`General`、`Researcher`、`Professional`、`Expert`。“检查证明的假设”或“核对表 2 与方法部分”比没有边界的审查要求更容易产生可用结果。没有可评估材料时，助手应请求补充材料并说明证据不足，而不是宣布没有问题。

`ANALYSIS_DEPTH` 可选 `Standard`、`Deep` 或 `Maximum`，分别用于适用的核心检查、更深入的审查，或现有证据和工具所能支持的最全面且有用的审查。提高深度不会增加原本不存在的能力。其余描述字段可以填写自己的要求，包括研究背景、优先事项、特殊请求和提供的材料；在 `OUTPUT_FORMAT` 中可指定执行摘要、技术报告等输出形式。

### 选择交付形式与证据

| 形式 | 使用场景 | 所需条件 |
| --- | --- | --- |
| [完整提示词][download-prompt] | 在可读文本的助手中进行详细审查 | 主协议及可读取的研究材料 |
| [简短请求](QUICKSTART.md) | 初筛或上下文容量较小 | 可复制的请求及明确范围 |
| [独立 skill][download-skill] | 宿主支持开放的 Agent Skills 文件夹格式 | 完整的 `academic-paper-audit` 文件夹及关联资源 |
| [可选 plugin][download-plugin] | 宿主支持该插件包格式 | 兼容的加载器；安装与发现机制由宿主决定 |

每次审查使用一种形式即可。纯文本方式不要求 Python、API 密钥或特定供应商集成。[版本页面][release] 提供三种压缩包和 [SHA-256 校验值][checksums]。校验值一致说明下载的字节相同，不代表研究来源真实。

检查应匹配研究方法：定量研究可能涉及分母、抽样和不确定性；定性研究关注引文语境与分析轨迹；计算研究关注数据划分及实际执行。形式研究需要检查假设、量词与反例；工程研究需要检查单位、校准与边界条件；档案研究需要核对版本、日期和转录。混合方法、证据综合、概念性和实践性研究也应依据自身主张选择标准。这些只是开放的示例，不是学科限制。p 值、预注册、公开原始数据及 DOI 都不是普遍要求。

当问题依赖原始图像或来源记录时，应尽可能提供这些材料。压缩 PDF 可能支持有限的文字审查，却不足以支持像素或元数据层面的结论。视觉、网页与专业工具只有在实际可用时才能扩大审查范围。项目附带脚本不提供 OCR、图像鉴证、形式化证明检查或自动 AI 图像检测引擎。

### 理解审查报告

报告应交代检查范围、实际使用的工具、方法背景、优先发现、削弱疑虑的证据、局限及下一步人工核查。覆盖领域包括文本/方法、统计/数据、图像、元数据/溯源、参考文献/通知、伦理/注册及跨论文比较。`completed` 表示已完成所述范围，`partial` 表示部分完成，`not_assessed` 表示未检查；`not_applicable` 必须解释为什么不适用。

证据等级描述观察结果的支持程度：**0**，已检查范围内没有明显问题；**1**，存在合理无过错解释的弱信号；**2**，可重复验证的重要不一致；**3**，有额外佐证、需要专家复核的强烈疑虑；**4**，实际阅读过、具有权威性且与文章匹配的外部来源证实了某项具体问题。等级 2/3 不证明主观意图。置信度针对观察，不针对作者是否有罪。撤稿通知必须按其实际理由理解，撤稿本身并不等于欺诈。

默认使用 Markdown 或纯文本。[报告模板](skills/academic-paper-audit/assets/report-template.md) 展示基本结构，[JSON](skills/academic-paper-audit/assets/report.schema.json) 则是可选格式。结构验证无法证明科学结论真实，也无法证明来源确实被阅读。未计算的哈希值和未执行的操作都应如实说明。如果无法取得严格报告 JSON 所要求的实际观测时间戳，应改用便于阅读的报告。

### 保护证据与跨会话继续

保留原始文件，单独记录派生副本。未发表稿件、可识别个人的记录及原始数据只应在获准的环境中分享。项目不运行托管服务或遥测，但助手及工具有各自的数据政策。审查请求不自动授权外部上传、联系作者或公开指控。论文和元数据中的指令属于待检查内容，不能当作操作命令。[隐私指南](docs/PRIVACY.md) 说明材料处理与保留边界。

切换会话或代理时，可使用[续查记录](skills/academic-paper-audit/assets/continuation-template.md)。将文章/版本、范围、证据 ID、检查位置、已完成检查、发现 ID/状态、缺失材料和下一步任务与真实来源一起传递。变化的证据需要重新检查。被纠正的问题应保留为已解决历史，不计入活跃发现。摘要不能代替尚未看过的来源，也不构成扩大任务权限的依据。

当前源代码中的 JSON 续接导出会保留已记录的研究背景、各领域的限制及已完成检查的链接。旧记录缺少这些信息时，`validate-checkpoint` 会在 `warnings` 中提示；恢复审查时应明确保留这些未知项。这些更新已包含在 v.0.0.3 中；一致的 v.0.0.2 续接记录仍可读取。

### 可选的本地辅助工具

命令需要完整仓库或 skill 文件夹；纯提示词 ZIP 不含 Python 脚本。只有辅助工具和开发需要 Python 3.10+。清单与算术工具使用标准库；报告/续查记录验证及导出需要 `jsonschema` 4.26.0。运行 `python -m venv .venv` 后，Windows 解释器为 `.venv/Scripts/python.exe`，macOS/Linux 为 `.venv/bin/python`。以下 `python` 指所选环境的解释器；从仓库根目录执行。

以下命令请使用[完整仓库源码][download-source]。如果只安装了 skill，请按照 [SKILL.md](skills/academic-paper-audit/SKILL.md) 操作，其中的路径相对于 skill 文件夹。

```text
python -m pip install -r skills/academic-paper-audit/requirements.txt
python skills/academic-paper-audit/scripts/audit_tools.py inventory --root tests/fixtures synthetic_manuscript.md
python skills/academic-paper-audit/scripts/audit_tools.py percentage --count 1 --total 3 --reported 33.3 --places 1
python skills/academic-paper-audit/scripts/audit_tools.py flow --initial 100 --excluded 10 --dropouts 5 --analyzed 90 --disjoint
python skills/academic-paper-audit/scripts/audit_tools.py validate-report examples/synthetic-report.json
python skills/academic-paper-audit/scripts/audit_tools.py checkpoint examples/synthetic-report.json
python skills/academic-paper-audit/scripts/audit_tools.py validate-checkpoint examples/synthetic-checkpoint.json
```

示例使用合成材料。清单接受相对于 `--root` 的路径并输出字节大小和 SHA-256。百分比检查假设普通未加权计数及通常的四舍五入；流程检查假设同一总体、同一时间点的损失互不重叠。计算工具不会指定证据等级。续查导出将 JSON 写入 stdout，需要保存时使用 UTF-8。退出码：0 为计算成功或记录有效，1 为报告/续查记录无效，2 为输入或依赖错误。算术不一致是有效的计算结果，不是软件运行失败。

### 验证、反馈与许可

项目包含 81 项行为测试，以及覆盖 Windows/Ubuntu 和 Python 3.10、3.14 的 CI 矩阵。v.0.0.2 修正了 Windows 清单工具的时间字段比较，同时保留文件身份和实际变更检查。简短请求、完整提示词和 skill 各通过 16 个合成案例与 48 项模型评判标准，包括正常对照、证据不足和已解决发现。这些是验收结果，不是科学准确率。验证指南记录了实际宿主测试及其失败情况，结果仅适用于这些运行。macOS 运行以及跨语言、媒介和学科的专家表现仍未验证。[验证指南](docs/VALIDATION.md) 提供证据、边界及复现步骤。

如遇可复现问题，请通过[问题表单][issues] 提供最小合成示例或获准公开的材料。[贡献指南](CONTRIBUTING.md) 介绍开发与发布，[CHANGELOG.md](CHANGELOG.md) 记录变更，项目采用 [MIT 许可](LICENSE)。本节是完整用户指南；补充技术文档以英语维护。

[↑ 返回顶部](#top)

---

<a id="lang-zh-tw"></a>
## 繁體中文

### 專案目的與適用範圍

Academic Paper Forensic & Research Integrity Auditor 協助研究人員、審稿人、編輯、學生與研究誠信工作者，對學術作品進行可追溯的初步檢視。核心資源是一份可重複使用的審查協議，可交給您慣用的 AI 助理。檢查項目依作品的主張、方法與證據選擇，不會將同一套實驗研究清單套用於所有學科。

依實際提供的資料及工具，可以檢視論證與證明、方法和結果的一致性、數值主張、運算評估、來源歸屬、圖像、溯源資訊、參考文獻、出版通知及論文間的對應關係。報告會區分報告不足、方法限制、學術歧見與具體研究誠信問題。重要發現應附上精確位置、可重現的查核步驟、合理的非不當行為解釋，以及下一步人工查核建議。

這是 AI 輔助初篩。涉及重要後果的決定，需要獨立人工查核。異常不能證明不當行為或意圖；沒有發現問題也不能證明真實性。協議用於支持判斷，不能取代領域專家、鑑識實驗室或機構調查。

### 使用現有助理開始

1. 下載[提示詞套件][download-prompt]，或開啟 [master_prompt.md](master_prompt.md)。將完整協議貼給助理，或附上可讀取的檔案。若只需範圍較小的初篩，可使用 [QUICKSTART.md](QUICKSTART.md) 的請求。
2. 提供論文、相關摘錄及獲准分享的輔助資料，說明版本、頁碼、圖表、論證與審查問題。附件無法讀取時，貼上具體段落，並明確限制僅就這些摘錄判斷。
3. 設定輸出語言、讀者、篇幅與重點。在完整提示詞末尾的 `USER INPUT — EDIT ONLY THIS SECTION` 中，只修改方括號內的值。以下是請求設定示例，並不表示檔案或工具已經可用。

```text
OUTPUT_LANGUAGE = [繁體中文]
RESEARCH_CONTEXT = [辨識所提供資料的學科、研究方法與證據類型。]
CAPABILITY_MODE = [只使用實際確認的能力，並說明無法完成的檢查。]
AUDIENCE = [Professional]
OUTPUT_LENGTH = [Detailed]
ANALYSIS_DEPTH = [Deep]
PRIORITY_FOCUS = [All applicable areas]
OUTPUT_FORMAT = [Structured forensic report]
SPECIAL_INSTRUCTIONS = [指出證據的精確位置，檢驗合理的非不當行為解釋，並說明下一步人工查核。]
MATERIALS = [列出提供的檔案或摘錄、版本與本次審查範圍。]
```

篇幅可選 `Short`、`Standard`、`Detailed`、`Exhaustive`；讀者可選 `Beginner`、`General`、`Researcher`、`Professional`、`Expert`。「檢查證明的假設」或「核對表 2 與方法段落」比沒有邊界的要求更容易產生實用結果。若沒有可評估資料，助理應要求補充，並註明證據不足，而不是宣告沒有問題。

`ANALYSIS_DEPTH` 可選 `Standard`、`Deep` 或 `Maximum`，分別用於適用的核心檢查、更深入的審查，或現有證據與工具所能支持的最完整且有用的審查。提高深度不會增加原本不存在的能力。其餘描述欄位可以填寫自己的要求，包括研究背景、優先事項、特殊請求及提供的資料；在 `OUTPUT_FORMAT` 中可指定決策摘要、技術報告等輸出形式。

### 選擇交付形式與證據

| 形式 | 適用情境 | 所需條件 |
| --- | --- | --- |
| [完整提示詞][download-prompt] | 在可讀文字的助理中詳細審查 | 主協議及可讀取的研究資料 |
| [簡短請求](QUICKSTART.md) | 初篩或較小的上下文容量 | 可複製的請求與明確範圍 |
| [獨立 skill][download-skill] | 宿主支援開放的 Agent Skills 資料夾格式 | 完整 `academic-paper-audit` 資料夾及關聯資源 |
| [選用 plugin][download-plugin] | 宿主支援該外掛套件格式 | 相容的載入器；安裝與探索機制由宿主決定 |

每次審查選擇一種形式即可。純文字使用不要求 Python、API 金鑰或特定供應商整合。[版本頁面][release] 提供三種壓縮檔及 [SHA-256 校驗值][checksums]。相符的值代表下載位元組一致，不代表研究來源真實。

查核標準必須配合方法：量化研究可能涉及分母、抽樣與不確定性；質性研究重視引文脈絡及分析軌跡；運算研究重視資料切分與實際執行。形式研究應檢查假設、量詞及反例；工程研究應檢查單位、校正與邊界條件；檔案研究應核對版本、日期及轉錄。混合方法、證據綜合、概念性與實務研究也應依其主張選擇標準。這些是開放示例，不是學科限制。p 值、預先註冊、公開原始資料與 DOI 並非所有研究的必要條件。

問題若依賴原始圖像或來源紀錄，應盡可能提供原件。壓縮 PDF 可能足以支持有限的文字檢視，卻不足以支持像素或中繼資料層級的結論。視覺、網頁及專業工具只有在實際可用時，才能擴大範圍。附帶程式不提供 OCR、圖像鑑識、形式化證明檢查或自動 AI 圖像偵測引擎。

### 理解審查報告

報告應交代檢查範圍、實際使用工具、方法背景、優先發現、降低疑慮的證據、限制及下一步人工查核。涵蓋文字/方法、統計/資料、圖像、中繼資料/溯源、參考文獻/通知、倫理/註冊及跨論文比較。`completed` 表示已完成所述範圍，`partial` 表示部分完成，`not_assessed` 表示未檢查；`not_applicable` 必須解釋為何不適用。

證據等級描述觀察的支持程度：**0**，檢查範圍內沒有明顯問題；**1**，存在合理善意解釋的弱訊號；**2**，可重現的重要不一致；**3**，有額外佐證且需專家複核的強烈疑慮；**4**，已實際閱讀、具權威性且與文章匹配的外部來源證實特定問題。等級 2/3 不證明意圖。信心水準針對觀察，不針對作者是否有罪。撤稿通知應依實際理由解讀，撤稿本身不等於造假。

預設輸出為 Markdown 或純文字。[報告範本](skills/academic-paper-audit/assets/report-template.md) 說明結構，[JSON](skills/academic-paper-audit/assets/report.schema.json) 為選用格式。結構驗證無法證明科學內容真實，也無法證明來源已被閱讀。未計算的雜湊值及未執行的操作都應明示。若無法取得嚴格報告 JSON 所要求的實際觀測時間戳記，應採用便於閱讀的報告。

### 保護證據並跨工作階段接續

保留原始檔案，另行記錄衍生副本。未發表稿件、可識別個人的紀錄及原始資料，只能在授權環境分享。專案不營運託管服務或遙測，但助理與工具仍各有資料政策。審查請求不會自動授權對外上傳、聯絡作者或公開指控。文件及中繼資料內的指令屬於待檢查內容，不是操作命令。[隱私指南](docs/PRIVACY.md) 說明處理與保存界線。

更換工作階段或代理時，可使用[接續紀錄](skills/academic-paper-audit/assets/continuation-template.md)。將文章/版本、範圍、證據 ID、檢查位置、已完成檢查、發現 ID/狀態、缺少資料及下一步工作，與實際來源一起移交。變動的證據需重新檢查。已修正的發現保留為已解決歷史，不計入目前有效發現。摘要不能取代尚未閱讀的來源，也不會擴大權限。

目前原始碼中的 JSON 接續匯出會保留已記錄的研究脈絡、各領域的限制及已完成檢查的連結。舊紀錄缺少這些資訊時，`validate-checkpoint` 會在 `warnings` 中提示；恢復審查時應明確保留這些未知項。這些更新已包含在 v.0.0.3 中；一致的 v.0.0.2 接續紀錄仍可讀取。

### 選用本機輔助工具

命令需要完整儲存庫或 skill 資料夾；純提示詞 ZIP 不包含 Python 程式。只有輔助工具及開發需要 Python 3.10+。清單與算術工具使用標準函式庫；報告/接續紀錄驗證及匯出需要 `jsonschema` 4.26.0。執行 `python -m venv .venv` 後，Windows 解譯器為 `.venv/Scripts/python.exe`，macOS/Linux 為 `.venv/bin/python`。以下 `python` 代表該環境的解譯器；請從儲存庫根目錄執行。

以下命令請使用[完整儲存庫原始碼][download-source]。若只安裝 skill，請依照 [SKILL.md](skills/academic-paper-audit/SKILL.md) 操作，其中的路徑相對於 skill 資料夾。

```text
python -m pip install -r skills/academic-paper-audit/requirements.txt
python skills/academic-paper-audit/scripts/audit_tools.py inventory --root tests/fixtures synthetic_manuscript.md
python skills/academic-paper-audit/scripts/audit_tools.py percentage --count 1 --total 3 --reported 33.3 --places 1
python skills/academic-paper-audit/scripts/audit_tools.py flow --initial 100 --excluded 10 --dropouts 5 --analyzed 90 --disjoint
python skills/academic-paper-audit/scripts/audit_tools.py validate-report examples/synthetic-report.json
python skills/academic-paper-audit/scripts/audit_tools.py checkpoint examples/synthetic-report.json
python skills/academic-paper-audit/scripts/audit_tools.py validate-checkpoint examples/synthetic-checkpoint.json
```

示例均為合成資料。清單接受相對於 `--root` 的路徑，輸出位元組大小及 SHA-256。百分比檢查假設一般未加權計數及通常四捨五入；流程檢查假設相同母體、相同時間點的損失互不重疊。計算工具不指定證據等級。接續匯出將 JSON 寫入 stdout，需要保存時使用 UTF-8。結束代碼：0 為計算成功或紀錄有效，1 為報告/接續紀錄無效，2 為輸入或相依套件錯誤。數字不一致是有效計算結果，不是程式執行失敗。

### 驗證、回饋與授權

專案包含 81 項行為測試，以及涵蓋 Windows/Ubuntu 和 Python 3.10、3.14 的 CI 矩陣。v.0.0.2 修正了 Windows 清單工具的時間欄位比較，同時保留檔案識別及實際變更檢查。簡短請求、完整提示詞與 skill 各通過 16 個合成案例及 48 項模型評判標準，包括正常對照、證據不足及已解決發現。這些是驗收結果，不是科學準確率。驗證指南記錄了實際宿主測試及其失敗情況，結果僅適用於這些執行。macOS 執行，以及跨語言、媒介與學科的專家表現仍未驗證。[驗證指南](docs/VALIDATION.md) 提供證據、界線及重現步驟。

遇到可重現問題，請透過[問題表單][issues] 提供最小合成示例或獲准公開的資料。[貢獻指南](CONTRIBUTING.md) 說明開發與發布，[CHANGELOG.md](CHANGELOG.md) 記錄變更，專案採用 [MIT 授權](LICENSE)。本節為完整使用指南；補充技術文件以英文維護。

[↑ 回到頂端](#top)

---

<a id="lang-ko"></a>
## 한국어

### 목적과 적용 범위

Academic Paper Forensic & Research Integrity Auditor는 연구자, 심사자, 편집자, 학생, 연구진실성 담당자가 학술 연구를 체계적으로 예비 검토하도록 돕습니다. 핵심 자료는 원하는 AI 도우미에게 전달할 수 있는 재사용 가능한 검토 지침입니다. 확인할 항목은 연구의 주장, 방법, 근거에 따라 선택하며, 모든 분야에 같은 실험 연구 체크리스트를 적용하지 않습니다.

실제 자료와 도구에 따라 논증과 증명, 방법과 결과의 일관성, 수치 주장, 계산 연구 평가, 출처 인용, 그림, 자료의 출처와 이력, 참고문헌, 공지, 논문 간 비교를 검토할 수 있습니다. 보고 부족, 방법론적 한계, 학술적 견해 차이, 구체적인 연구진실성 우려는 구분합니다. 중요한 발견에는 정확한 위치, 재현 가능한 확인 방법, 합리적인 정상적 설명, 다음에 사람이 확인할 사항이 필요합니다.

이는 AI를 활용한 예비 검토입니다. 중대한 영향을 미치는 결정에는 독립적인 검토자의 확인이 필요합니다. 이상 징후가 부정행위나 고의를 입증하지 않으며, 발견된 문제가 없다고 진위를 보증할 수도 없습니다. 지침은 판단을 지원하지만 분야 전문가, 포렌식 실험실, 기관 조사를 대신하지 않습니다.

### 평소 사용하는 도우미로 시작하기

1. [프롬프트 패키지][download-prompt]를 내려받거나 [master_prompt.md](master_prompt.md)를 엽니다. 전체 지침을 붙여 넣거나 읽을 수 있는 파일로 첨부합니다. 범위가 작은 첫 검토에는 [QUICKSTART.md](QUICKSTART.md)의 요청문을 사용할 수 있습니다.
2. 논문이나 관련 발췌문, 공유 권한이 있는 보조 자료를 제공합니다. 버전, 페이지, 그림, 논증, 검토 질문을 명시하세요. 첨부 파일을 읽지 못하면 필요한 문단을 붙여 넣고 검토 범위를 해당 발췌문으로 한정합니다.
3. 출력 언어, 독자, 분량, 우선순위를 정합니다. 전체 프롬프트에서는 `USER INPUT — EDIT ONLY THIS SECTION`의 대괄호 안 값만 수정하세요. 다음 예시는 요청 설정이며 파일이나 도구의 이용 가능성을 확인한 기록이 아닙니다.

```text
OUTPUT_LANGUAGE = [한국어]
RESEARCH_CONTEXT = [제공된 자료의 학문 분야, 연구 방법, 근거 유형을 확인하세요.]
CAPABILITY_MODE = [실제로 확인한 기능만 사용하고 수행할 수 없는 검사를 밝히세요.]
AUDIENCE = [Professional]
OUTPUT_LENGTH = [Detailed]
ANALYSIS_DEPTH = [Deep]
PRIORITY_FOCUS = [All applicable areas]
OUTPUT_FORMAT = [Structured forensic report]
SPECIAL_INSTRUCTIONS = [근거의 정확한 위치를 제시하고 정상적 설명을 검토하며 다음 사람이 확인할 사항을 적으세요.]
MATERIALS = [제공한 파일이나 발췌문, 버전, 요청하는 검토 범위를 적으세요.]
```

분량은 `Short`, `Standard`, `Detailed`, `Exhaustive`, 독자는 `Beginner`, `General`, `Researcher`, `Professional`, `Expert` 중에서 선택할 수 있습니다. “증명의 가정을 확인해 주세요” 또는 “표 2와 방법 절을 대조해 주세요”처럼 구체적으로 요청하면 결과를 활용하기 쉽습니다. 평가 가능한 자료가 없다면 자료를 요청하고 근거 부족으로 표시해야 합니다.

`ANALYSIS_DEPTH`는 `Standard`, `Deep`, `Maximum` 중에서 선택합니다. 각각 적용 가능한 핵심 검사, 더 자세한 검토, 현재 근거와 도구가 뒷받침하는 가장 폭넓고 유용한 검토를 요청합니다. 깊이를 높여도 없는 기능이 생기지는 않습니다. 나머지 설명 필드에는 연구 맥락, 우선순위, 특별 요청, 제공 자료를 직접 적을 수 있습니다. `OUTPUT_FORMAT`에는 의사결정자용 요약이나 기술 보고서처럼 원하는 형식을 지정하세요.

### 배포 형식과 근거 선택하기

| 형식 | 적합한 경우 | 필요한 것 |
| --- | --- | --- |
| [전체 프롬프트][download-prompt] | 텍스트를 읽는 도우미로 상세 검토 | 주 지침과 읽을 수 있는 연구 자료 |
| [짧은 요청문](QUICKSTART.md) | 초기 선별 또는 작은 컨텍스트 | 복사할 요청문과 제한된 범위 |
| [독립 skill][download-skill] | 호스트가 개방형 Agent Skills 폴더 형식을 지원 | 연결된 리소스를 포함한 전체 `academic-paper-audit` 폴더 |
| [선택적 plugin][download-plugin] | 호스트가 해당 플러그인 패키지를 지원 | 호환 로더; 설치 및 검색 방식은 호스트에 따라 다름 |

한 번의 검토에는 한 형식을 사용하세요. 텍스트 방식에는 Python, API 키, 특정 제공업체 연동이 필요하지 않습니다. [릴리스 페이지][release]에서 세 압축 파일과 [SHA-256 체크섬][checksums]을 제공합니다. 체크섬이 일치하면 내려받은 바이트를 확인한 것이며 연구 출처의 진위를 입증한 것은 아닙니다.

검토 기준은 연구 방법에 맞춥니다. 양적 연구에서는 분모, 표집, 불확실성을, 질적 연구에서는 인용 맥락과 분석 과정을, 계산 연구에서는 데이터 분할과 실제 실행 여부를 살필 수 있습니다. 형식 연구에서는 가정·양화사·반례, 공학에서는 단위·교정·경계조건, 기록물 연구에서는 판본·날짜·전사를 확인합니다. 혼합 방법, 근거 종합, 개념 및 실천 기반 연구도 자체 주장에 맞는 기준이 필요합니다. 이는 열린 예시 목록입니다. p값, 사전등록, 원자료 공개, DOI가 모든 연구의 필수 요건은 아닙니다.

질문이 원본 그림이나 출처 기록에 의존한다면 가능한 원본을 제공하세요. 압축 PDF로 제한된 텍스트 검토는 가능해도 픽셀이나 메타데이터에 관한 결론은 뒷받침하지 못할 수 있습니다. 시각·웹·전문 도구는 실제 사용 가능할 때만 범위를 넓힙니다. 부속 스크립트는 OCR, 이미지 포렌식, 형식적 증명 검증, 자동 AI 이미지 탐지 엔진이 아닙니다.

### 보고서 해석하기

보고서는 확인 범위, 사용한 도구, 방법 맥락, 우선 발견, 우려를 약화하는 근거, 한계, 다음 사람의 확인 사항을 설명합니다. 텍스트/방법, 통계/데이터, 그림, 메타데이터/출처, 참고문헌/공지, 윤리/등록, 논문 간 비교를 기록합니다. `completed`는 명시한 범위를 검토했다는 뜻이고, `partial`은 일부 검토, `not_assessed`는 미검토입니다. `not_applicable`에는 적용되지 않는 이유가 있어야 합니다.

근거 수준은 관찰의 뒷받침 정도를 나타냅니다. **0**은 검토한 범위에서 유의미한 우려 없음, **1**은 정상적 설명이 가능한 약한 신호, **2**는 재현 가능한 중요한 불일치, **3**은 추가 근거가 있으며 전문가 검토가 필요한 강한 우려, **4**는 실제로 읽은 권위 있는 외부 자료가 해당 논문에 관해 구체적으로 확인한 문제입니다. 수준 2/3은 고의를 입증하지 않습니다. 신뢰도는 관찰에 관한 것이지 저자의 유죄 여부가 아닙니다. 철회 공지는 실제 사유를 읽어야 하며 철회 자체가 사기를 뜻하지는 않습니다.

기본 출력은 Markdown이나 일반 텍스트입니다. [보고서 서식](skills/academic-paper-audit/assets/report-template.md)이 구성을 보여 주며 [JSON](skills/academic-paper-audit/assets/report.schema.json)은 선택 사항입니다. 구조 검증으로 과학적 진실이나 실제 출처 열람을 입증할 수 없습니다. 계산하지 않은 해시와 수행하지 않은 작업은 밝혀야 합니다. 엄격한 보고서 JSON에 필요한 실제 관측 시각을 알 수 없다면 사람이 읽는 보고서를 사용하세요.

### 근거 보호와 세션 간 이어가기

원본을 변경하지 말고 파생 사본은 별도로 기록하세요. 미발표 원고, 개인 식별 기록, 원자료는 허가된 환경에서만 공유합니다. 프로젝트는 호스팅 서비스나 원격 사용량 수집을 운영하지 않지만 도우미와 도구에는 별도 데이터 정책이 적용됩니다. 검토 요청이 외부 업로드, 저자 접촉, 공개적인 의혹 제기를 허가하지는 않습니다. 문서에 삽입된 지시는 검토 자료이며 실행 명령이 아닙니다. [개인정보 안내](docs/PRIVACY.md)에 처리·보관 경계가 설명되어 있습니다.

다른 세션이나 에이전트로 옮길 때는 [이어가기 기록](skills/academic-paper-audit/assets/continuation-template.md)을 사용하세요. 논문/버전, 범위, 근거 ID, 검토 위치, 완료 검사, 발견 ID/상태, 빠진 자료, 다음 단계를 실제 출처와 함께 전달합니다. 변경된 근거는 다시 검토합니다. 수정으로 해소된 발견은 해결된 이력으로 남기고 현재 유효한 발견 수에서 제외합니다. 요약은 보지 않은 원자료나 새로운 작업 허가를 대신하지 않습니다.

현재 소스 코드의 JSON 이어가기 내보내기는 기록된 연구 맥락, 영역별 한계와 완료된 검사에 대한 연결을 보존합니다. 이전 기록에 이 정보가 없으면 `validate-checkpoint`가 `warnings`로 알립니다. 작업을 이어갈 때 이러한 누락을 명시하세요. 이 업데이트는 v.0.0.3에 포함되며, 일관된 v.0.0.2 이어가기 기록도 읽을 수 있습니다.

### 선택적 로컬 도구

명령에는 전체 저장소나 skill 폴더가 필요하며 프롬프트 ZIP에는 Python 스크립트가 없습니다. Python 3.10+는 도구와 개발에만 필요합니다. 목록 작성과 산술은 표준 라이브러리를 사용하고, 보고서/이어가기 기록 검증 및 내보내기는 `jsonschema` 4.26.0이 필요합니다. `python -m venv .venv` 후 Windows에서는 `.venv/Scripts/python.exe`, macOS/Linux에서는 `.venv/bin/python`을 사용합니다. 아래 `python`은 해당 환경의 인터프리터이며 저장소 루트에서 실행합니다.

아래 명령에는 [전체 저장소 소스][download-source]를 사용하세요. 설치된 skill에서는 폴더 기준 경로를 안내하는 [SKILL.md](skills/academic-paper-audit/SKILL.md)를 따르세요.

```text
python -m pip install -r skills/academic-paper-audit/requirements.txt
python skills/academic-paper-audit/scripts/audit_tools.py inventory --root tests/fixtures synthetic_manuscript.md
python skills/academic-paper-audit/scripts/audit_tools.py percentage --count 1 --total 3 --reported 33.3 --places 1
python skills/academic-paper-audit/scripts/audit_tools.py flow --initial 100 --excluded 10 --dropouts 5 --analyzed 90 --disjoint
python skills/academic-paper-audit/scripts/audit_tools.py validate-report examples/synthetic-report.json
python skills/academic-paper-audit/scripts/audit_tools.py checkpoint examples/synthetic-report.json
python skills/academic-paper-audit/scripts/audit_tools.py validate-checkpoint examples/synthetic-checkpoint.json
```

예시는 합성 자료를 사용합니다. 목록 도구는 `--root` 기준 상대 경로를 받아 바이트 크기와 SHA-256을 출력합니다. 백분율 검사는 가중치 없는 빈도와 일반적인 반올림을, 흐름 검사는 같은 모집단·시점에서 서로 겹치지 않는 제외 인원을 가정합니다. 계산은 근거 수준을 부여하지 않습니다. 이어가기 내보내기는 stdout에 JSON을 쓰므로 필요하면 UTF-8로 저장하세요. 종료 코드는 계산 성공/유효한 기록 0, 잘못된 보고서/이어가기 기록 1, 입력·의존성 오류 2입니다. 수치 불일치는 유효한 계산 결과입니다.

### 검증, 문의와 라이선스

프로젝트에는 행동 테스트 81개와 Windows·Ubuntu 및 Python 3.10·3.14를 대상으로 하는 CI 조합이 있습니다. v.0.0.2는 Windows 목록 도구의 시간 필드 비교를 수정하면서 파일 식별과 실제 변경 감지를 유지합니다. 짧은 요청문, 전체 프롬프트, skill은 각각 합성 사례 16개와 별도 모델이 평가한 기준 48개를 통과했으며, 정상 대조, 근거 부족, 해결된 발견도 포함합니다. 이는 수용 검사 결과이지 과학적 정확도 측정이 아닙니다. 실제 호스트 검사와 실패 사례는 검증 안내에 기록되어 있으며 결과는 해당 실행에만 적용됩니다. macOS 실행과 모든 언어·매체·분야에서의 전문가 성능은 검증되지 않았습니다. [검증 안내](docs/VALIDATION.md)에 근거, 한계, 재현 절차가 있습니다.

재현 가능한 문제는 [버그 양식][issues]에 작은 합성 예시나 공유 허가를 받은 자료와 함께 제출하세요. [기여 안내](CONTRIBUTING.md)는 개발·배포를, [CHANGELOG.md](CHANGELOG.md)는 변경 사항을 설명합니다. [MIT 라이선스](LICENSE)를 사용합니다. 이 절은 완전한 사용자 안내이며 추가 기술 문서는 영어로 유지됩니다.

[↑ 맨 위로](#top)

---

<a id="lang-ja"></a>
## 日本語

### 目的と対象範囲

Academic Paper Forensic & Research Integrity Auditor は、研究者、査読者、編集者、学生、研究公正の担当者が学術的な研究を体系的に予備確認するためのプロジェクトです。中心となるのは、普段使っている AI アシスタントに渡せる再利用可能な審査手順です。確認項目は研究の主張、方法、証拠に合わせて選び、すべての分野に同じ実験研究のチェックリストを当てはめません。

提供された資料と実際に使えるツールに応じて、論証や証明、方法と結果の整合性、数値、計算研究の評価、出典の扱い、図、来歴情報、参考文献、通知、論文間の対応を確認できます。記述不足、方法上の限界、学術的見解の相違、具体的な研究公正上の懸念は区別します。重要な指摘には正確な位置、再現可能な確認手順、問題のない合理的な説明、次に人が確認すべき事項が必要です。

本手順は AI 支援による予備審査です。重大な影響を伴う判断には独立した人による確認が必要です。異常は不正行為や意図の証明ではなく、指摘がないことも真正性の保証ではありません。専門家の判断を支えるもので、分野の専門家、鑑識機関、所属機関の調査を代替しません。

### 普段のアシスタントで始める

1. [プロンプトパッケージ][download-prompt]を取得するか、[master_prompt.md](master_prompt.md) を開きます。手順全体を貼り付けるか、読み取り可能なファイルとして添付してください。範囲を絞った初期確認には [QUICKSTART.md](QUICKSTART.md) の依頼文も使えます。
2. 論文、関連箇所の抜粋、共有を許可された補足資料を提供します。版、ページ、図、論証、確認したい問いを指定してください。添付を読み取れない場合は対象部分を貼り付け、その抜粋だけを審査するよう明示します。
3. 出力言語、読者、分量、重点を設定します。完全版では末尾の `USER INPUT — EDIT ONLY THIS SECTION` にある角括弧内の値だけを変更します。以下は依頼の設定例であり、ファイルやツールの利用可能性を確認した記録ではありません。

```text
OUTPUT_LANGUAGE = [日本語]
RESEARCH_CONTEXT = [提供資料の分野、研究方法、証拠の種類を特定してください。]
CAPABILITY_MODE = [実際に確認できた能力だけを使い、実施できない確認を明示してください。]
AUDIENCE = [Professional]
OUTPUT_LENGTH = [Detailed]
ANALYSIS_DEPTH = [Deep]
PRIORITY_FOCUS = [All applicable areas]
OUTPUT_FORMAT = [Structured forensic report]
SPECIAL_INSTRUCTIONS = [証拠の正確な位置を示し、問題のない説明を検討し、次の人的確認を提案してください。]
MATERIALS = [提供ファイルや抜粋、版、今回の確認範囲を記入してください。]
```

分量は `Short`、`Standard`、`Detailed`、`Exhaustive`、読者は `Beginner`、`General`、`Researcher`、`Professional`、`Expert` から選べます。「証明の仮定を確認する」「表 2 を方法節と照合する」といった具体的な依頼は、結果を活用しやすくします。評価できる資料がない場合は、資料を求め、証拠不十分とするのが適切です。

`ANALYSIS_DEPTH` は `Standard`、`Deep`、`Maximum` から選びます。それぞれ、該当する基本確認、より詳しい審査、利用可能な証拠とツールで支えられる最も広く有用な審査を依頼します。深度を上げても、利用できない機能は増えません。他の説明欄には、研究背景、優先事項、特別な依頼、提供資料を自分の言葉で記入できます。`OUTPUT_FORMAT` には、意思決定者向けの要約や技術報告など、必要な形式を指定してください。

### 形式と資料を選ぶ

| 形式 | 適した用途 | 必要なもの |
| --- | --- | --- |
| [完全版プロンプト][download-prompt] | 文章を読めるアシスタントで詳しく確認 | 主手順と読み取り可能な研究資料 |
| [短い依頼文](QUICKSTART.md) | 初期選別や小さなコンテキスト | コピーする依頼文と限定した範囲 |
| [単体 skill][download-skill] | ホストが公開 Agent Skills フォルダー形式に対応 | 関連リソースを含む `academic-paper-audit` フォルダー全体 |
| [任意の plugin][download-plugin] | ホストがプラグインパッケージに対応 | 互換ローダー。導入や自動検出はホストに依存 |

一度の審査では一つの形式を使ってください。テキストでの利用に Python、API キー、特定提供元との連携は不要です。[リリースページ][release]には三つのアーカイブと [SHA-256 チェックサム][checksums]があります。一致が示すのは取得したバイトの同一性であり、研究資料の真正性ではありません。

確認基準は方法に合わせます。量的研究では分母、標本抽出、不確実性、質的研究では引用の文脈と分析過程、計算研究ではデータ分割と実際の実行が重要になります。形式的研究では仮定・量化・反例、工学では単位・校正・境界条件、史資料研究では版・日付・翻刻を確認します。混合研究、エビデンス統合、概念的・実践的研究も自身の主張に合った基準が必要です。これは分野を限定する一覧ではありません。p 値、事前登録、原データ公開、DOI は一律の必須条件ではありません。

問いが原図や出典記録に依存する場合は、可能な限りそれらを提供してください。圧縮 PDF で文章の限定的な確認ができても、画素やメタデータに関する結論までは支えられない場合があります。画像認識、ウェブ、専門ツールで範囲を広げられるのは実際に利用可能な場合だけです。付属スクリプトは OCR、画像鑑識、形式的証明検査、自動 AI 画像検出のエンジンではありません。

### 報告書の読み方

報告書は、確認範囲、使ったツール、方法の背景、優先度の高い指摘、疑いを弱める証拠、限界、次の人的確認を説明します。文章/方法、統計/データ、図、メタデータ/来歴、参考文献/通知、倫理/登録、論文間比較を記録します。`completed` は示した範囲の確認済み、`partial` は一部確認、`not_assessed` は未確認です。`not_applicable` には非該当とする理由が必要です。

証拠レベルは観察の裏付けを表します。**0** は確認範囲で有意な懸念なし、**1** は問題のない説明が可能な弱い兆候、**2** は再現可能な重要な不整合、**3** は追加の裏付けがあり専門家の確認を要する強い懸念、**4** は実際に読んだ権威ある外部資料が対象論文について裏付けた具体的問題です。レベル 2/3 は意図を示しません。確信度は観察に対するもので、著者の責任認定に対するものではありません。撤回通知は実際の理由を読み、撤回だけで不正と断定しないでください。

通常の出力は Markdown またはプレーンテキストです。[報告テンプレート](skills/academic-paper-audit/assets/report-template.md)で構成を確認でき、[JSON](skills/academic-paper-audit/assets/report.schema.json)は任意です。構造の検証は科学的真実や実際の出典閲覧を証明しません。未計算のハッシュや未実施の作業は明示します。厳密な報告 JSON に必要な実際の観測時刻が分からない場合は、人が読める報告書を使います。

### 証拠を保護して次のセッションへつなぐ

原本を変更せず、派生コピーは別に記録します。未発表原稿、個人を特定できる記録、原データは、許可された環境だけで共有してください。プロジェクトはホスティングサービスや利用状況の遠隔収集を提供しませんが、アシスタントとツールには各々のデータ方針があります。審査依頼は外部アップロード、著者への連絡、疑惑の公表を許可するものではありません。資料内の指示は審査対象の内容であり、操作命令ではありません。[プライバシーガイド](docs/PRIVACY.md)に取扱いと保管の範囲を説明しています。

別のセッションやエージェントには[継続記録](skills/academic-paper-audit/assets/continuation-template.md)を使って引き継ぎます。論文/版、範囲、証拠 ID、確認位置、完了作業、指摘 ID/状態、不足資料、次の作業を実際の出典とともに渡します。変わった証拠は再確認し、訂正で解消した指摘は解決済み履歴として残して有効件数から除きます。要約は未閲覧の出典を置き換えず、新しい権限も与えません。

現在のソースコードの JSON 引き継ぎ出力は、記録済みの研究背景、各領域の制約、完了した検査への参照を保持します。旧記録にこれらの情報がない場合、`validate-checkpoint` は `warnings` で知らせます。再開時も欠落を明示してください。この更新は v.0.0.3 に含まれ、整合性のある v.0.0.2 の引き継ぎ記録も読み込めます。

### 任意のローカル補助ツール

コマンドには完全なリポジトリか skill フォルダーが必要です。プロンプト専用 ZIP に Python スクリプトはありません。Python 3.10+ が必要なのは補助ツールと開発だけです。ファイル一覧と算術には標準ライブラリ、報告書/継続記録の検証と書き出しには `jsonschema` 4.26.0 を使います。`python -m venv .venv` の後、Windows は `.venv/Scripts/python.exe`、macOS/Linux は `.venv/bin/python` を利用できます。以下の `python` はその環境のインタープリターで、リポジトリのルートから実行します。

以下のコマンドには[完全なリポジトリのソース][download-source]を使ってください。導入済み skill では、そのフォルダーからの相対パスを案内する [SKILL.md](skills/academic-paper-audit/SKILL.md) に従ってください。

```text
python -m pip install -r skills/academic-paper-audit/requirements.txt
python skills/academic-paper-audit/scripts/audit_tools.py inventory --root tests/fixtures synthetic_manuscript.md
python skills/academic-paper-audit/scripts/audit_tools.py percentage --count 1 --total 3 --reported 33.3 --places 1
python skills/academic-paper-audit/scripts/audit_tools.py flow --initial 100 --excluded 10 --dropouts 5 --analyzed 90 --disjoint
python skills/academic-paper-audit/scripts/audit_tools.py validate-report examples/synthetic-report.json
python skills/academic-paper-audit/scripts/audit_tools.py checkpoint examples/synthetic-report.json
python skills/academic-paper-audit/scripts/audit_tools.py validate-checkpoint examples/synthetic-checkpoint.json
```

例は合成資料を使います。一覧ツールは `--root` からの相対パスを受け取り、バイト数と SHA-256 を出力します。割合検査は重み付けのない件数と通常の丸め、人数フロー検査は同一集団・時点の重複しない除外を仮定します。計算は証拠レベルを付けません。継続記録の書き出しは JSON を stdout に出力するので、必要なら UTF-8 で保存します。終了コードは計算成功/有効な記録が 0、無効な報告/継続記録が 1、入力・依存関係のエラーが 2 です。数値の不一致は正常な計算結果です。

### 検証、問い合わせ、ライセンス

プロジェクトには 81 件の動作テストと、Windows・Ubuntu、Python 3.10・3.14 を対象とする CI 構成があります。v.0.0.2 は Windows 一覧ツールの時刻項目の比較を修正し、ファイルの同一性と実際の変更の検査は維持します。短い依頼文、完全版、skill はそれぞれ、正常例、証拠不足、解消した指摘を含む合成 16 ケースと、別モデルが評価した 48 基準に合格しました。これは受け入れ確認であり科学的正確率ではありません。実際のホスト試験と失敗例は検証ガイドに記録しており、結果はその実行に限られます。macOS 実行と、すべての言語・媒体・分野での専門家水準の性能は未検証です。[検証ガイド](docs/VALIDATION.md)に根拠、限界、再現手順があります。

再現できる問題は[不具合フォーム][issues]に、小さな合成例か公開許可のある資料を添えて報告してください。[貢献ガイド](CONTRIBUTING.md)は開発と公開、[CHANGELOG.md](CHANGELOG.md)は変更履歴を説明します。[MIT ライセンス](LICENSE)で利用できます。この節だけで利用に必要な説明を読めます。補足の技術文書は英語で管理しています。

[↑ 先頭に戻る](#top)

---

[release]: https://github.com/IACBI/academic-paper-forensic-auditor/releases/tag/v.0.0.3
[download-prompt]: https://github.com/IACBI/academic-paper-forensic-auditor/releases/download/v.0.0.3/academic-paper-auditor-prompt-0.0.3.zip
[download-skill]: https://github.com/IACBI/academic-paper-forensic-auditor/releases/download/v.0.0.3/academic-paper-auditor-skill-0.0.3.zip
[download-plugin]: https://github.com/IACBI/academic-paper-forensic-auditor/releases/download/v.0.0.3/academic-paper-auditor-plugin-0.0.3.zip
[checksums]: https://github.com/IACBI/academic-paper-forensic-auditor/releases/download/v.0.0.3/SHA256SUMS.txt
[download-source]: https://github.com/IACBI/academic-paper-forensic-auditor/archive/refs/heads/main.zip
[issues]: https://github.com/IACBI/academic-paper-forensic-auditor/issues/new?template=bug_report.yml
