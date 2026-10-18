# Evrensellik, araştırma kapsamı ve bakım incelemesi

Sürüm: **v.0.0.1**. İnceleme tarihi: **18 Ekim 2026**. Başlangıç noktası: `9e15cd5` yerel commit'indeki kaynaklar. Bu rapor projenin tasarımını, talimatlarını, şemasını, yardımcı araçlarını, paketlemesini ve testlerini inceler; gerçek bir makalenin bilimsel doğruluk raporu değildir.

## 1. Sonuç ve evrenselliğin sınırı

Projenin çekirdeği, kullanıcının tercih ettiği ve verilen materyali okuyabilen bir yapay zekâda **düz metinle uygulanabilen bir inceleme protokolü** olmalıdır. Native skill veya plugin desteği, Python, web erişimi ve görsel araçlar bunun ön koşulu değildir. Bunlar incelemenin kapsamını genişleten isteğe bağlı yeteneklerdir.

Araştırma alanından bağımsızlık, her makaleye aynı kontrol listesini uygulamak anlamına gelmez. Alan, soru, iddia, yöntem, kanıt türü ve bağlam belirlendikten sonra uygun kontroller seçilmelidir. Bu yaklaşım yeni ve disiplinler arası yöntemlere de açık kalmalıdır.

Başlangıç sürümünde bu iki hedefe ulaşmayı zorlaştıran gerçek eksikler vardı. Aşağıdaki değişiklikler uygulandı. Bununla birlikte, hiçbir prompt her ajanda aynı davranışı, tüm alanlarda uzmanlık veya ölçülmüş tespit başarısını garanti edemez. Dosya biçiminin taşınabilirliği, ajanın yetenekleri ve bilimsel inceleme yeterliliği ayrı değerlendirilir.

## 2. İnceleme yöntemi

- Ana prompt, skill giriş dosyası, üretilen referanslar, rapor şeması, yardımcı kod, paketleyici, kontroller ve testler okundu.
- İddialar ile gerçekten uygulanan fonksiyonlar ayrıldı. Yardımcı kodun PDF/OCR/görsel adli inceleme veya ispat doğrulama motoru olmadığı doğrulandı.
- Ajan bağımsızlığı açık Agent Skills biçimiyle; alan kapsamı disiplinler arası araştırma bütünlüğü ilkeleriyle karşılaştırıldı. Bu kaynaklar bir sertifika veya otomatik uygunluk denetimi olarak kullanılmadı.
- Yapısal testlere ek olarak iki bağımsız değerlendiriciye, beklenen cevaplar verilmeden altı sentetik yöntem örneği sunuldu. Biri araçsız metin yolunu, diğeri dosya/hesaplama ve JSON yolunu kullandı.
- Sonraki kabul seti 16 vakaya genişletildi: altı tutarsızlık, yedi meşru/sorunsuz kontrol, iki yetersiz kanıt durumu ve bir düzeltmeyle çözülen bulgu. Kısa istek, tam prompt ve skill ayrı kör paketlerle, cevapları bilmeyen değerlendiricilere verildi; ayrı model yargıcı gerçek yanıtları ortak ölçütlerle inceledi.
- Gerçek makale, katılımcı verisi, dış hizmet yüklemesi, yayıncı teması veya kamuya yayın yapılmadı.

## 3. Öncelikli bulgular ve uygulanan düzeltmeler

| Öncelik | Başlangıçtaki eksik | Etkisi | Uygulanan düzeltme |
| --- | --- | --- | --- |
| Yüksek | Kullanım belgesi Codex dizini/komutunu öne çıkarıyordu; skill içinde OpenAI arayüz metadata'sı vardı | Native desteği olmayan kullanıcılarda kurulum zorunluymuş izlenimi | Düz metin ana giriş oldu; sağlayıcı metadata'sı kaldırıldı; hosta özgü kurulum isteğe bağlı olarak ayrıldı |
| Yüksek | Kontroller ve örnekler deneysel/biyomedikal çalışmalara ağırlık veriyordu | Formal, nitel ve arşiv araştırmaları uygunsuz kriterlerle değerlendirilebilirdi | Açık uçlu yöntem seçimi ve dokuz örnek yöntem ailesi eklendi; listeye uymayan yöntemler için uzmanlık sınırı belirtildi |
| Yüksek | Yöntemsel sınırlılık, raporlama eksiği ve bütünlük kaygısı açıkça ayrılmıyordu | Normal akademik eleştiri suçlama benzeri bir bulguya dönüşebilirdi | Ayrım ana protokole ve şablona işlendi; JSON'a isteğe bağlı issue_kind eklendi |
| Yüksek | Kaynak şeması HTTP(S) URL istiyordu | Kitap, arşiv, sözlü tarih veya çevrimdışı kaynağın kaydı için sahte URL üretme baskısı | URL null olduğunda gerçek ve boş olmayan identifier desteği eklendi; eski URL kayıtları geçerli kaldı |
| Orta | Araçsız/small-context kullanım için belirgin bir yol yoktu | Yapılamayan kontrol tüm görevi engelleyebilir veya yapılmış gibi gösterilebilirdi | Yetenek matrisi, okunabilir alıntı yolu, devam kaydı ve isteğe bağlı JSON/hesaplama kuralları eklendi |
| Orta | Kesin zaman damgası bilinmeyen ajan strict JSON'u doldurmaya zorlanabilirdi | Uydurulmuş işlem tarihi | Bilinmeyen zamanı açıkça belirtip insan-okunur rapora dönme kuralı eklendi; strict kayıt gereksinimi sessizce gevşetilmedi |
| Orta | Level 3'teki matematiksel imkânsızlık örneği, basit yanlış ispatı otomatik yükseltebilirdi | Alanlar arası kanıt düzeyi tutarsızlığı | Tekrar üretilebilir basit karşıörnek/argüman hatası için Level 2 varsayılanı, Level 3 için ek kanıt gerekçesi tanımlandı |
| Orta | Kısa rapor ile uzun zorunlu şablon arasında gerilim vardı | Basit incelemeler gereksiz uzuyordu | Kısa eşdeğer uyarı ve ortak statü/gerekçelerin gruplanması mümkün kılındı; önemli kapsam sınırları korundu |
| Orta | Yedi sabit alanın isimleri biyomedikal kontrol listesi gibi okunabilirdi | İlgisiz kontroller veya yanlış not_applicable kullanımı | Alanların genel anlamı açıklandı; görülmeyen figür ile gerçekten uygulanamaz figür alanı ayrıldı |
| Orta | Tek katılımcı-akışı örneği disiplinler arası davranışa kanıt oluşturmuyordu | Kapsam iddiası testlerden daha genişti | Formal, nitel, arşivsel, hesaplamalı, mühendislik ve sentez örnekleriyle bağımsız ileri test eklendi |
| Orta | Yalnız sorun içeren örnekler yanlış alarm davranışını göstermiyordu | Meşru uygulamalar gereksiz şüpheye dönüşebilirdi | Yedi sorunsuz kontrol ve iki yetersiz kanıt vakası eklendi; yapılmayan kontroller başarılı sayılmıyor |
| Orta | Denemelerin yanıtları ve puanlaması tekrar incelenebilir bir kayıtta tutulmuyordu | Sonuçlar yalnız anlatı düzeyinde kalıyordu | Gerçek yanıtlar, ayrı yargıcın alıntı/gerekçeleri ve kaynak hash'leriyle yerel değerlendirme kayıtları eklendi |
| Orta | Oturum/ajan değiştirirken aktarılacak asgari kayıt biçimi belirsizdi | Bulgu kimlikleri, çözüm durumu ve geçmiş kontroller kaybolabilirdi | İnsan-okunur devam şablonu, isteğe bağlı JSON şeması, rapordan aktarım ve doğrulama komutları eklendi |
| Orta | Bazı kısa yanıtlarda bağımsız insan incelemesi açıkça söylenmiyordu | Doğru ama sınırlı ön inceleme gereğinden güçlü algılanabilirdi | İki gerçek başarısız yanıt/gerekçe korundu; kısa ve bulgusuz raporlarda da açık insan incelemesi şartı netleştirildi; yeni kör paketlerle üç yol tekrar değerlendirildi |
| Düşük | Değerlendirme aracı yalnız manifesti kontrol ediyordu | Sonradan değiştirilmiş paket içeriği aynı kayıtla kabul edilebilirdi | Gerçek protokol, vaka ve talimat baytları yanıtlar okunmadan karşılaştırılıyor; değişiklik reddi test edildi |
| Düşük | Dışa aktarılan devam kaydı bazı referans listelerini raporla paylaşıyordu | Kaydı bellekte düzenlemek önceki raporu da değiştirebilirdi | Listeler ayrıldı; önceki raporun değişmediği davranış testiyle doğrulandı |
| Orta | Referans üreticisinde aynı numaralı bölüm sözlükte sessizce ezilebilirdi | Politika kaybı güncel görünerek geçebilirdi | Yinelenen bölüm ve çift/eksik yönlendirme artık hata; her bölüm tam bir kez aktarılıyor |
| Düşük | Geçersiz JSON için bulgu sayıları sıfır görünüyordu | Hatalı rapor, sorunsuz rapor gibi yorumlanabilirdi | Geçersiz raporda sayılar null oldu; davranış testi eklendi |
| Düşük | Envanterde dosya yollarının köke göre olduğu yeterince açık değildi | İlk kullanımda gereksiz yol hatası | Root-relative ve mutlak yol örnekleri açıklandı |
| Düşük | Runtime plugin ZIP'i test, örnek ve geliştirici belgelerini de taşıyordu | Gereksiz büyük ve amaca göre belirsiz paket | Prompt/skill/plugin paketleri ayrıldı; varsayılan prompt oldu; runtime paketlerinden geliştirme materyali çıkarıldı |
| Düşük | README'de 12 kez aynı kurulum/dizin bilgisi, ayrı yayın/sonuç belgeleri ve kökte bağımlılık yönlendirme dosyası vardı | Bakım yükü ve çelişki riski | 12 dilin özgün tanıtımı korundu; tekrarlar tek kullanım belgesine indirildi; yinelenen dosyalar birleştirildi |

## 4. Araştırma alanlarına uygulanabilirlik

Protokol bir alan listesine kilitlenmez. Yöntem aileleri kontrol seçimini kolaylaştıran örneklerdir:

- **Nicel deneysel/gözlemsel araştırma:** tasarım, ölçüm, örnekleme, deney birimi, belirsizlik, nedensel çıkarım varsayımları ve paydalar.
- **Nitel/yorumlayıcı/katılımcı araştırma:** araştırma sorusu–analiz yaklaşımı uyumu, seçilen materyal, alıntı izi, konumlanma ve refleksivite gerektiğinde, karşı örnekler ve mahremiyet. Her yaklaşım için p-değeri veya kodlayıcı uyumu zorunlu değildir.
- **Karma/disiplinler arası araştırma:** bileşenlere uygun ölçütler, birleştirme gerekçesi ve çelişen kanıtların ele alınışı. Bir bileşenin gücü diğerindeki açığı otomatik kapatmaz.
- **Hesaplamalı/yazılım/simülasyon/ML:** veri ve bölünme kökeni, sızıntı, ön işleme, değerlendirme bağımsızlığı, temel karşılaştırmalar, kod/ortam ve çalıştırmanın gerçekten yapılıp yapılmadığı.
- **Matematiksel/formal/kuramsal çalışma:** tanımlar, varsayımlar, niceleyiciler, ispat bağımlılıkları, sınır durumları ve gerçek karşıörnekler. Çalıştırılmamış bir ispat denetleyicisi kullanılmış gibi raporlanmaz.
- **Mühendislik/fiziksel/ölçüm çalışması:** boyutlar ve birimler, kalibrasyon, belirsizlik, sınır koşulları, sayısal yakınsama ve ölçüm ile simülasyon ayrımı.
- **Tarih/arşiv/metin/beşerî bilimler:** baskı, varak/sayfa, tarih, çeviri/transkripsiyon, kaynak bağımsızlığı, bağlam ve gerekçeli alternatif yorumlar. DOI veya açık arşiv yokluğu tek başına sorun değildir.
- **Derleme/kanıt sentezi:** derleme türü, seçme/dışlama, çıkarım izi, örtüşen birincil örneklemler ve sentezin iddiaları. Her derleme meta-analiz değildir.
- **Kavramsal/normatif/felsefî/hukuk-kuramsal/tasarım veya uygulama temelli çalışma:** öncüller, ölçütler, argüman tutarlılığı, bağlam ve normatif yargı ile ampirik iddianın ayrımı.

Yeni veya tanınmayan bir yöntem çıkarsa makalenin kendi tanımıyla ele alınır; uygun uzmanlık veya doğrulanmış rehber yoksa sınır belirtilir. Hassas alanlarda uzman incelemesi gereksinimi, genel bir promptla ortadan kalkmaz.

## 5. Evrensel kullanım tasarımı

1. **En geniş erişim:** QUICKSTART.md içindeki isteği veya tam master_prompt.md'yi metin olarak verme. Dosya okuma bile zorunlu değildir; ilgili bölümler yapıştırılabilir.
2. **Standart destekleyen ajan:** Agent Skills klasörünü yükleme. Native komut, kurulum dizini ve otomatik keşif hosta bağlıdır.
3. **İsteğe bağlı paket:** Uyumlu plugin hostu için plugin.json. Bu manifest tüm ajanlar için ortak bir kurucu değildir.
4. **İsteğe bağlı otomasyon:** Python yardımcıları veya gerçekten doğrulanmış host eşdeğerleri. Bunlar bilimsel muhakemenin yerine geçmez.

Bu ayrım, sağlayıcı sayısını artırmak için çok sayıda aynı içeriğin kopyası olan adaptör dosyası üretmeyi gerektirmez. Tek politika ve açık fallback, gereksiz platform bakımından daha sürdürülebilirdir.

## 6. Doğrulama ve bağımsız denemeler

Yapısal testler; eski raporların kabulünü, çevrimdışı kaynak kimliğini, açık uçlu yöntem bağlamını, yanlış JSON sayımlarını, bölüm kaybını, paket sınırlarını ve mevcut hesaplama/dosya güvenilirliği kontrollerini kapsar. Ayrıntılı çalıştırma kaydı [VALIDATION.md](VALIDATION.md) içindedir.

**Araçsız deneme:** Formal karşıörnek, nitel alıntı çelişkisi ve arşiv tarihinin yanlış aktarımı bulundu. Eksik p-değeri, transkript kısıtı ve DOI/URL yokluğu anomali sayılmadı. Kod, saat, hash, web veya şema doğrulaması yapıldığı iddia edilmedi.

**Araçlı skill denemesi:** Test verisinin değerlendirmeye sızması, joule–watt-hour eşdeğerliği hatası ve aynı kohortun iki kez bağımsız sayılması bulundu. JSON doğrulandı. Deneme kodu/veri yeniden çalıştırılmış gibi sunmadı.

Bu denemeler bağımsız yerel değerlendiricilerle sentetik veri üzerinde yapıldı. Ayrı ticari sağlayıcıların canlı ürünlerini test etmez; örneklerin basitliği nedeniyle gerçek literatürde doğruluk oranı, duyarlılık veya özgüllük hesaplanamaz.

Tekrarlanabilir süreç [EVALUATION.md](EVALUATION.md) içinde tanımlı. Her yol için 16 gerçek yanıt ve 48 ölçüt değerlendirmesi kaydedilir. Eksik/yinelenen vaka, yapılmamış ölçüt, eski kaynak hash'i veya yanıtta bulunmayan alıntı geçerli başarı kaydı oluşturamaz. Önceki iki sunum hatasının gerçek çıktıları `evaluations/reviewed-regressions.json` içinde korunur; doğru sonuç sınıflandırması, eksik insan incelemesi ifadesini başarıya çevirmedi.

Güncel yerel sonuç: **70 yazılım testi geçti**. Kısa istek, tam prompt ve skill'in her biri **16/16 vaka ve 48/48 ölçütü** geçti; üç yolun toplamı 48 yanıt ve 144 ölçüt kararıdır. Bunlar ayrı model yargıcının sentetik kabul sonuçlarıdır; tüm alanlarda bilimsel doğruluk oranı veya farklı ticari ürünlerin uyumluluk testi değildir.

Devam kaydı için rapor kimliği, kapsam, sürüm, kanıt kimlikleri ve bulgu geçmişi korunur; dönüşüm yeni inceleme, kaynak okuma veya saat gözlemi üretmez. Önceki F001 bulgusunun sürüm-2 düzeltmesiyle çözülmesi, kör devam vakasında ayrıca değerlendirilir. Yapısal doğrulayıcı bilimsel doğruluğu veya önceki ajanın dürüstlüğünü kanıtlamaz.

## 7. Hâlâ doğrulanması gerekenler

- Farklı gerçek hostlarda kurulum, dosya okuma, otomatik keşif ve bağlam davranışı. Hosta ait test yapılmadan o ürüne uyumluluk rozeti verilmemeli.
- Farklı disiplinlerden yetkili, uzmanlarca değerlendirilmiş örneklerle yanlış alarm ve kaçırma oranları. Şu anda sayı verilemez.
- Gerçek PDF/OCR, mikroskopi, harita, ses, video, 3B/model dosyası ve diğer modaliteler. Protokol bu materyallere açıktır; yardımcı kod bunların analiz motorunu sağlamaz.
- Gerçek formal ispat, uzman yöntem ve hukuki/etik yükümlülük değerlendirmesi. Ajanın öz güveni uzman doğrulaması yerine geçmez.
- Kaynak yetkisinin, gerçekten okunmasının ve kaydın gerçeğe uygunluğunun doğrulanması. JSON validator metnin doğruluğunu kanıtlamaz.
- Çeviri ve uzman terminolojisinin alan/dil bazında değerlendirilmesi. Orijinal yazı sistemi ve baskı/çeviri izi korunmalı; 12 dil tanıtımı 12 dilde uzman doğruluğu iddiası değildir.

Bu sınırlar bilinen yazılım hatası olarak gizlenmedi veya genel bir "evrensel çalışır" sözüyle kapatılmadı; hangi iddiaların henüz desteklenmediğini gösterir.

## 8. Temizlik kararı

Kaldırılan izlenen dosyalar: sağlayıcıya özgü agents/openai.yaml, yinelenen requirements-validation.txt, ayrı PUBLICATION.md ve VALIDATION_RESULTS.md. Gerekli kullanım/yayın bilgisi USAGE.md'ye, güncel doğrulama bilgisi VALIDATION.md'ye alındı. README'nin yinelenen tam rehberleri sadeleştirildi; 12 özgün dil tanıtımı korundu.

Geçici deneme raporları, eski açılmış paket kopyaları, tekrar üretilebilir ZIP'ler, proje içindeki sanal ortam ve Python önbellekleri son doğrulamadan sonra temizlenir. Git geçmişi, kaynak kod, testler, sentetik veri, tek bağımlılık listesi, lisans, gerekli üretilen skill referansları ve sonuçları destekleyen asgari değerlendirme kayıtları korunur. Geçici paket kopyalarıyla, sonuçların dayanağı olan özgün yanıt kayıtları aynı şey değildir. Proje dışındaki kullanıcı klasörlerine veya sistem/genel önbelleklerine dokunulmaz.

## 9. Birincil kaynaklar ve kullanım sınırları

- [Agent Skills specification](https://agentskills.io/specification): klasör, frontmatter, göreli kaynaklar ve aşamalı yükleme. Biçim uygunluğu her hostta çalışma garantisi değildir.
- [Agent Skills overview](https://agentskills.io/home): ortak biçim, skills-compatible ajanlar arasında yeniden kullanım.
- [ALLEA araştırma bütünlüğü kodu](https://allea.org/code-of-conduct/): farklı bilimsel ve akademik disiplinleri kapsayan ortak çerçeve. Yerel yükümlülüklerin yerine otomatik olarak konulmadı.
- [COPE retraction guidelines](https://doi.org/10.24318/cope.2019.1.4): geri çekme gerekçesini okumak ve dürüst hata ile suistimali eşitlememek.
- [ACM SIGSIM artifact evaluation](https://sigsim.acm.org/conf/pads/2024/blog/artifact-evaluation/): hesaplamalı artifact incelemesinde belgelenmiş, tutarlı ve çalıştırılabilir materyal ile sonuç doğrulamasını ayıran uygulama örneği. Bağlantıdaki konferans ölçütleri tüm disiplinlere zorunlu tutulmadı.

Erişim tarihi: 18 Ekim 2026. Kaynaklar tasarım kararlarını destekler; onay, sertifika veya projenin bu kuruluşlarca değerlendirilmesi anlamına gelmez. Context7 aracı bu oturumda sunulmadığından mevcut birincil belgeler doğrudan okundu.

Güncel test, paket ve değerlendirme sonuçları için [VALIDATION.md](VALIDATION.md) esas alınır. İlk yerel inceleme tamamlandığında uzak depo veya yayın oluşturulmamıştı. Sahibinin sonraki yayın izniyle oluşturulan [GitHub deposu](https://github.com/IACBI/academic-paper-forensic-auditor) ve [sürüm sayfası](https://github.com/IACBI/academic-paper-forensic-auditor/releases/tag/v.0.0.1) güncel dağıtım noktalarıdır.
