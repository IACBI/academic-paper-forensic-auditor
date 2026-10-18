# Academic Paper Forensic & Research Integrity Auditor

**Author:** 𝓐.𝓒.𝓑  
**License:** MIT  
**Version:** v.0.0.1

[![Validate](https://github.com/IACBI/academic-paper-forensic-auditor/actions/workflows/validate.yml/badge.svg?branch=main)](https://github.com/IACBI/academic-paper-forensic-auditor/actions/workflows/validate.yml)

A provider-independent research-screening workflow for scholarly work across disciplines. Use readable evidence with your preferred AI agent; no plugin, Python or vendor integration is required for a scoped text review.

**Start:** [Quick start](QUICKSTART.md) · [Full prompt](master_prompt.md) · [Usage](docs/USAGE.md) · [Detailed project review / Ayrıntılı inceleme](docs/REVIEW_TR.md)

**Download v.0.0.1:** [Prompt package](https://github.com/IACBI/academic-paper-forensic-auditor/releases/download/v.0.0.1/academic-paper-auditor-prompt-0.0.1.zip) · [Skill](https://github.com/IACBI/academic-paper-forensic-auditor/releases/download/v.0.0.1/academic-paper-auditor-skill-0.0.1.zip) · [Optional plugin](https://github.com/IACBI/academic-paper-forensic-auditor/releases/download/v.0.0.1/academic-paper-auditor-plugin-0.0.1.zip) · [SHA-256 checksums](https://github.com/IACBI/academic-paper-forensic-auditor/releases/download/v.0.0.1/SHA256SUMS.txt)

Start with the prompt package if your agent has no native skill loader. [Release notes](https://github.com/IACBI/academic-paper-forensic-auditor/releases/tag/v.0.0.1) describe the available formats and verification boundaries.

This is AI-assisted investigative screening, not a definitive forensic or misconduct determination. Findings can be wrong and require independent human verification. No findings in the inspected scope do not establish authenticity.

## Choose your delivery format

| Format | What to provide | Requirement |
| --- | --- | --- |
| Quick textual review | Copy QUICKSTART.md's request and supply material | An agent that can inspect the text and follow instructions |
| Full protocol | Paste or attach master_prompt.md | Sufficient context or bounded passes |
| Open Agent Skills folder | Load skills/academic-paper-audit/ | A host supporting the open folder format |
| Optional plugin | Package the skill with plugin.json | A compatible plugin host; not a universal installer |

Capabilities are checked separately: text, files, vision, calculations, web and specialist tools. Missing capabilities narrow the audit; an unperformed check does not pass. JSON/schema validation and Python helpers are optional.

## Research coverage

Select checks by question, claims, methods and evidence. Routes include quantitative, qualitative, mixed, computational, formal/theoretical, engineering/measurement, archival/humanities, evidence synthesis and conceptual/practice-based work. These are open-ended examples, not restrictions on valid fields. Do not impose p-values, participant counts, ethics-board IDs, public raw data or a DOI on every study.

Separate reporting gaps, methodological limitations, scholarly disagreement and integrity concerns. Trace findings to evidence, record coverage, test benign alternatives and identify the next human verification step. Applicability across fields does not establish equal expertise or measured detection accuracy across fields or models.

For a new session or a different agent, carry the [continuation record](skills/academic-paper-audit/assets/continuation-template.md) together with the actual evidence. It preserves scope, versions, finding IDs/status and pending work; a summary does not replace the source material. Optional local helpers can export and validate a JSON checkpoint.

The [reproducible evaluation](docs/EVALUATION.md) compares quick, master and skill routes on 16 synthetic cases, including legitimate controls, insufficient evidence and a resolved finding. Reviewed baseline records retain raw responses, independent model judgements and input/protocol hashes. These local acceptance checks do not establish native installation in other hosts or real-world scientific accuracy; see the [validation record](docs/VALIDATION.md).

## Türkçe kullanım

Kullandığınız ajana [hızlı başlangıçtaki](QUICKSTART.md) isteği veya [tam promptu](master_prompt.md) verin, çıktı dilini Türkçe belirtin ve materyali ekleyin. Skill ve plugin isteğe bağlı dağıtım biçimleridir; çekirdek inceleme bir platforma bağlı değildir.

Önce alan, yöntem ve kanıt türü belirlenir. Matematiksel kanıt, nitel görüşme, arşiv belgesi, yazılım deneyi ve klinik çalışma aynı kontrol listesine zorlanmaz. Araç yoksa erişilebilir metinle sınırlı, eksikleri açık bir inceleme yapılır. Tüm ajanlarda aynı sonuç veya tüm disiplinlerde uzman doğruluğu garanti edilmez.

## Development and optional packaging

Python 3.10+ is needed only for helpers/development. In an appropriate environment:

```text
python -m pip install -r skills/academic-paper-audit/requirements.txt
python scripts/build_references.py
python scripts/check_project.py
python scripts/build_release.py
```

The default archive is the provider-independent prompt package. Use `--format skill`, `--format plugin` or `--format all` when needed. Archives are build outputs, not public submissions. No remote repository, account configuration or listing is created.

See [validation](docs/VALIDATION.md), [privacy](docs/PRIVACY.md), [contributing](CONTRIBUTING.md) and [changelog](CHANGELOG.md). The master is the canonical policy; its seven skill references are generated for selective loading. Tests and synthetic fixtures remain development resources, outside runtime packages.

## Language overviews

The 12 original language overviews are retained below. Repeated setup instructions and trees are consolidated into the shared guide. Detailed operational documentation is English; the project review is Turkish.

[English](#lang-en) · [Türkçe](#lang-tr) · [Deutsch](#lang-de) · [Français](#lang-fr) · [Español](#lang-es) · [Italiano](#lang-it) · [Português](#lang-pt) · [العربية](#lang-ar) · [简体中文](#lang-zh-cn) · [繁體中文](#lang-zh-tw) · [한국어](#lang-ko) · [日本語](#lang-ja)

<a id="lang-en"></a>

### English

This repository contains a reusable master prompt designed to turn a capable AI system into an **Academic Paper Forensic & Research Integrity Auditor**. It is intended for researchers, editors, peer reviewers, journalists, students, and research-integrity professionals who need a structured first-pass examination of scientific papers and related files.

<a id="lang-tr"></a>

### Türkçe

Bu depo, gelişmiş bir yapay zekâ sistemini **Akademik Makale Forensik ve Araştırma Bütünlüğü Denetçisi** olarak kullanmaya yönelik yeniden kullanılabilir bir ana prompt içerir. Araştırmacılar, editörler, hakemler, gazeteciler, öğrenciler ve araştırma bütünlüğü uzmanlarının bilimsel makaleleri ve ilişkili dosyaları sistematik biçimde ön incelemesine yardımcı olmak için tasarlanmıştır.

<a id="lang-de"></a>

### Deutsch

Dieses Repository enthält einen wiederverwendbaren Master-Prompt, der ein leistungsfähiges KI-System als **forensischen Prüfer für wissenschaftliche Publikationen und Forschungsintegrität** einsetzt. Er richtet sich an Forschende, Herausgebende, Peer-Reviewer, Journalistinnen und Journalisten, Studierende sowie Fachleute für Forschungsintegrität, die wissenschaftliche Arbeiten und zugehörige Dateien strukturiert vorprüfen möchten.

<a id="lang-fr"></a>

### Français

Ce dépôt contient un prompt principal réutilisable conçu pour transformer un système d'IA performant en **auditeur forensique d'articles scientifiques et d'intégrité de la recherche**. Il s'adresse aux chercheurs, éditeurs, évaluateurs, journalistes, étudiants et professionnels de l'intégrité scientifique souhaitant effectuer un premier examen structuré d'un article et de ses fichiers associés.

<a id="lang-es"></a>

### Español

Este repositorio contiene un prompt maestro reutilizable diseñado para convertir un sistema de IA avanzado en un **auditor forense de artículos académicos e integridad de la investigación**. Está pensado para investigadores, editores, revisores, periodistas, estudiantes y profesionales de integridad científica que necesiten una revisión inicial estructurada de artículos y archivos relacionados.

<a id="lang-it"></a>

### Italiano

Questo repository contiene un master prompt riutilizzabile progettato per trasformare un sistema di IA avanzato in un **auditor forense di articoli accademici e integrità della ricerca**. È pensato per ricercatori, editor, revisori, giornalisti, studenti e professionisti dell'integrità scientifica che necessitano di una prima analisi strutturata di articoli e file correlati.

<a id="lang-pt"></a>

### Português

Este repositório contém um prompt mestre reutilizável criado para transformar um sistema de IA avançado em um **auditor forense de artigos acadêmicos e integridade da pesquisa**. Ele foi pensado para pesquisadores, editores, revisores, jornalistas, estudantes e profissionais de integridade científica que precisam de uma análise inicial estruturada de artigos e arquivos relacionados.

<a id="lang-ar"></a>

### العربية

يحتوي هذا المستودع على موجّه رئيسي قابل لإعادة الاستخدام، صُمّم لتحويل نظام ذكاء اصطناعي متقدم إلى **مدقق جنائي للأوراق الأكاديمية ونزاهة البحث العلمي**. وهو موجه للباحثين والمحررين والمحكّمين والصحفيين والطلاب والمتخصصين في نزاهة البحث الذين يحتاجون إلى فحص أولي منظم للأبحاث والملفات المرتبطة بها.

<a id="lang-zh-cn"></a>

### 简体中文

本仓库包含一个可重复使用的主提示词，用于将具备较强能力的 AI 系统配置为 **学术论文取证与科研诚信审查助手**。它面向研究人员、编辑、同行评审者、记者、学生以及科研诚信专业人员，用于对论文及其相关文件进行结构化的初步审查。

<a id="lang-zh-tw"></a>

### 繁體中文

本儲存庫包含一個可重複使用的主提示詞，用於將具備較強能力的 AI 系統設定為 **學術論文鑑識與研究誠信審查助手**。它適用於研究人員、編輯、同儕審查者、記者、學生以及研究誠信專業人士，用來對論文及相關檔案進行結構化的初步檢視。

<a id="lang-ko"></a>

### 한국어

이 저장소에는 고성능 AI 시스템을 **학술 논문 포렌식 및 연구진실성 감사 도구**처럼 활용할 수 있도록 설계된 재사용 가능한 마스터 프롬프트가 들어 있습니다. 연구자, 편집자, 동료심사자, 기자, 학생, 연구진실성 담당자가 논문과 관련 파일을 구조적으로 1차 검토할 때 사용할 수 있습니다.

<a id="lang-ja"></a>

### 日本語

このリポジトリには、高性能な AI システムを **学術論文フォレンジックおよび研究公正監査アシスタント** として利用するための再利用可能なマスタープロンプトが含まれています。研究者、編集者、査読者、ジャーナリスト、学生、研究公正の専門家が、論文および関連ファイルを体系的に一次確認するために設計されています。

## License

MIT. See [LICENSE](LICENSE).
