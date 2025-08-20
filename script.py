# Create all the necessary files for the DCS Booklet
import os

# Create the HTML file
html_content = '''<!DOCTYPE html>
<html lang="hi">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>डिजिटल क्रॉप सर्वे (DCS) - मध्य प्रदेश सरकार</title>
    <link rel="stylesheet" href="style.css">
    <link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css" rel="stylesheet">
</head>
<body>
    <!-- Navigation Header -->
    <nav class="navbar">
        <div class="nav-brand">
            <i class="fas fa-seedling"></i>
            <span>DCS डिजिटल क्रॉप सर्वे</span>
        </div>
        <div class="nav-controls">
            <button class="nav-btn" id="prevBtn"><i class="fas fa-chevron-left"></i></button>
            <span class="nav-counter"><span id="currentSection">1</span> / <span id="totalSections">15</span></span>
            <button class="nav-btn" id="nextBtn"><i class="fas fa-chevron-right"></i></button>
        </div>
        <button class="menu-btn" id="menuBtn"><i class="fas fa-bars"></i></button>
    </nav>

    <!-- Progress Bar -->
    <div class="progress-bar">
        <div class="progress-fill" id="progressFill"></div>
    </div>

    <!-- Back Button (visible on all pages except home) -->
    <button class="back-btn hidden" id="backBtn">
        <i class="fas fa-arrow-left"></i>
        <span>वापस</span>
    </button>

    <!-- Table of Contents Modal -->
    <div class="modal hidden" id="tocModal">
        <div class="modal-content">
            <div class="modal-header">
                <h3>विषय सूची</h3>
                <button class="close-btn" id="closeModal"><i class="fas fa-times"></i></button>
            </div>
            <div class="modal-body">
                <div class="toc-grid">
                    <div class="toc-item" data-section="0">
                        <i class="fas fa-home"></i>
                        <span>मुख्य पृष्ठ</span>
                    </div>
                    <div class="toc-item" data-section="1">
                        <i class="fas fa-list"></i>
                        <span>विषय सूची</span>
                    </div>
                    <div class="toc-item" data-section="2">
                        <i class="fas fa-info-circle"></i>
                        <span>परिचय</span>
                    </div>
                    <div class="toc-item" data-section="3">
                        <i class="fas fa-history"></i>
                        <span>DCS से पहले</span>
                    </div>
                    <div class="toc-item" data-section="4">
                        <i class="fas fa-route"></i>
                        <span>विकास यात्रा</span>
                    </div>
                    <div class="toc-item" data-section="5">
                        <i class="fas fa-cogs"></i>
                        <span>तकनीकी आधार</span>
                    </div>
                    <div class="toc-item" data-section="6">
                        <i class="fas fa-project-diagram"></i>
                        <span>प्रक्रिया प्रवाह</span>
                    </div>
                    <div class="toc-item" data-section="7">
                        <i class="fas fa-users"></i>
                        <span>हितधारक</span>
                    </div>
                    <div class="toc-item" data-section="8">
                        <i class="fas fa-trophy"></i>
                        <span>उपलब्धियां</span>
                    </div>
                    <div class="toc-item" data-section="9">
                        <i class="fas fa-database"></i>
                        <span>डेटा संग्रह</span>
                    </div>
                    <div class="toc-item" data-section="10">
                        <i class="fas fa-rocket"></i>
                        <span>भविष्य तकनीक</span>
                    </div>
                    <div class="toc-item" data-section="11">
                        <i class="fas fa-exclamation-triangle"></i>
                        <span>चुनौतियां</span>
                    </div>
                    <div class="toc-item" data-section="12">
                        <i class="fas fa-chart-line"></i>
                        <span>आर्थिक प्रभाव</span>
                    </div>
                    <div class="toc-item" data-section="13">
                        <i class="fas fa-star"></i>
                        <span>सफलता कहानियां</span>
                    </div>
                    <div class="toc-item" data-section="14">
                        <i class="fas fa-phone"></i>
                        <span>संपर्क जानकारी</span>
                    </div>
                </div>
            </div>
        </div>
    </div>

    <!-- Main Content -->
    <main class="main-content">
        <!-- Section 0: Home Page -->
        <section class="section active front-page">
            <!-- Government Header with Logo -->
            <div class="government-header">
                <div class="gov-logo">
                    <i class="fas fa-university"></i>
                </div>
                <div class="title-section">
                    <h1 class="main-title">डिजिटल क्रॉप सर्वे</h1>
                    <p class="subtitle">मध्य प्रदेश सरकार - भू-अभिलेख एवं राजस्व विभाग</p>
                </div>
            </div>

            <!-- MP Map -->
            <div class="mp-map">
                <svg viewBox="0 0 400 300" xmlns="http://www.w3.org/2000/svg">
                    <path d="M50 150 L100 50 L200 80 L300 60 L350 100 L320 180 L250 220 L150 200 L80 180 Z" fill="rgba(255,255,255,0.3)" stroke="rgba(255,255,255,0.5)" stroke-width="2"/>
                    <text x="200" y="150" fill="white" text-anchor="middle" font-size="16" font-weight="bold">मध्य प्रदेश</text>
                </svg>
            </div>

            <!-- Vision Mission -->
            <div class="vision-mission">
                <div class="vision-box">
                    <h3><i class="fas fa-eye"></i> दृष्टि (Vision)</h3>
                    <p>मध्य प्रदेश में उन्नत डिजिटल तकनीकों का लाभ उठाकर एक पारदर्शी, सटीक और किसान-केंद्रित फसल-निगरानी पारिस्थितिकी तंत्र स्थापित करना।</p>
                </div>
                <div class="mission-box">
                    <h3><i class="fas fa-bullseye"></i> मिशन (Mission)</h3>
                    <p>सटीक मैपिंग, प्रौद्योगिकी एकीकरण, हितधारक सहभागिता, पारदर्शी शासन और क्षमता निर्माण के माध्यम से डिजिटल कृषि को बढ़ावा देना।</p>
                </div>
            </div>

            <!-- Print Button -->
            <div class="print-section">
                <button class="print-btn" id="printBtn">
                    <i class="fas fa-print"></i>
                    <span>पूरी बुकलेट प्रिंट करें</span>
                </button>
            </div>
        </section>

        <!-- Section 1: Table of Contents -->
        <section class="section toc-section">
            <div class="content-section">
                <div class="section-header">
                    <h2 class="section-title">विषय सूची</h2>
                    <p class="section-subtitle">डिजिटल क्रॉप सर्वे की संपूर्ण जानकारी</p>
                </div>
                
                <div class="toc-visual-grid">
                    <div class="toc-visual-item" data-section="0">
                        <div class="toc-visual-icon"><i class="fas fa-home"></i></div>
                        <h3>मुख्य पृष्ठ</h3>
                        <p>परिचय और विज़न-मिशन</p>
                    </div>
                    <div class="toc-visual-item" data-section="2">
                        <div class="toc-visual-icon"><i class="fas fa-info-circle"></i></div>
                        <h3>परिचय</h3>
                        <p>DCS क्या है और क्यों जरूरी</p>
                    </div>
                    <div class="toc-visual-item" data-section="3">
                        <div class="toc-visual-icon"><i class="fas fa-history"></i></div>
                        <h3>DCS से पहले</h3>
                        <p>पारंपरिक समस्याएं और चुनौतियां</p>
                    </div>
                    <div class="toc-visual-item" data-section="4">
                        <div class="toc-visual-icon"><i class="fas fa-route"></i></div>
                        <h3>विकास यात्रा</h3>
                        <p>2017 से अब तक का सफर</p>
                    </div>
                    <div class="toc-visual-item" data-section="5">
                        <div class="toc-visual-icon"><i class="fas fa-cogs"></i></div>
                        <h3>तकनीकी आधार</h3>
                        <p>SAARA, AI/ML, सैटेलाइट तकनीक</p>
                    </div>
                    <div class="toc-visual-item" data-section="6">
                        <div class="toc-visual-icon"><i class="fas fa-project-diagram"></i></div>
                        <h3>प्रक्रिया प्रवाह</h3>
                        <p>कैसे काम करता है DCS</p>
                    </div>
                    <div class="toc-visual-item" data-section="7">
                        <div class="toc-visual-icon"><i class="fas fa-users"></i></div>
                        <h3>हितधारक</h3>
                        <p>युवा, किसान, अधिकारी</p>
                    </div>
                    <div class="toc-visual-item" data-section="8">
                        <div class="toc-visual-icon"><i class="fas fa-trophy"></i></div>
                        <h3>उपलब्धियां</h3>
                        <p>88 लाख फार्मर ID, नई फसलें</p>
                    </div>
                    <div class="toc-visual-item" data-section="9">
                        <div class="toc-visual-icon"><i class="fas fa-database"></i></div>
                        <h3>डेटा संग्रह</h3>
                        <p>डेटा कैसे इकट्ठा और उपयोग</p>
                    </div>
                    <div class="toc-visual-item" data-section="10">
                        <div class="toc-visual-icon"><i class="fas fa-rocket"></i></div>
                        <h3>भविष्य तकनीक</h3>
                        <p>ड्रोन, IoT, ब्लॉकचेन, 5G</p>
                    </div>
                    <div class="toc-visual-item" data-section="11">
                        <div class="toc-visual-icon"><i class="fas fa-exclamation-triangle"></i></div>
                        <h3>चुनौतियां</h3>
                        <p>समस्याएं और समाधान</p>
                    </div>
                    <div class="toc-visual-item" data-section="12">
                        <div class="toc-visual-icon"><i class="fas fa-chart-line"></i></div>
                        <h3>आर्थिक प्रभाव</h3>
                        <p>बजट, SCA, रोजगार सृजन</p>
                    </div>
                    <div class="toc-visual-item" data-section="13">
                        <div class="toc-visual-icon"><i class="fas fa-star"></i></div>
                        <h3>सफलता कहानियां</h3>
                        <p>किसानों और युवाओं पर प्रभाव</p>
                    </div>
                    <div class="toc-visual-item" data-section="14">
                        <div class="toc-visual-icon"><i class="fas fa-phone"></i></div>
                        <h3>संपर्क जानकारी</h3>
                        <p>हेल्पलाइन, पोर्टल, सपोर्ट</p>
                    </div>
                </div>
            </div>
        </section>

        <!-- Section 2: Introduction -->
        <section class="section">
            <div class="content-section">
                <div class="section-header">
                    <h2 class="section-title">डिजिटल क्रॉप सर्वे (DCS) - परिचय</h2>
                    <p class="section-subtitle">भारत की पहली AI-आधारित फसल निगरानी प्रणाली</p>
                </div>
                
                <div class="content-grid">
                    <div class="content-card">
                        <div class="card-header">
                            <div class="card-icon"><i class="fas fa-seedling"></i></div>
                            <h3 class="card-title">DCS क्या है?</h3>
                        </div>
                        <div class="card-content">
                            <p>डिजिटल क्रॉप सर्वे (DCS) एक क्रांतिकारी पहल है जो पारंपरिक फसल सर्वेक्षण पद्धति को डिजिटल तकनीक से बदलती है। यह स्थानीय युवाओं द्वारा SAARA मोबाइल ऐप के माध्यम से, पार्सल-स्तरीय जियो-फेंसिंग और अनिवार्य फसल फोटोग्राफी के साथ सटीक फसल डेटा एकत्र करने का सिस्टम है।</p>
                        </div>
                    </div>
                    
                    <div class="content-card">
                        <div class="card-header">
                            <div class="card-icon"><i class="fas fa-bullseye"></i></div>
                            <h3 class="card-title">महत्व और आवश्यकता</h3>
                        </div>
                        <div class="card-content">
                            <ul>
                                <li><strong>पारदर्शिता:</strong> प्राकृतिक आपदा राहत या बीमा के लिए झूठे दावों को समाप्त करना</li>
                                <li><strong>सटीकता:</strong> 100% पार्सल-स्तरीय सर्वेक्षण से फसलों की सटीक पहचान</li>
                                <li><strong>तीव्रता:</strong> तत्काल बीमा भुगतान और किसान क्रेडिट कार्ड जारी करना</li>
                                <li><strong>रोजगार:</strong> ग्रामीण युवाओं को सर्वेयर के रूप में रोजगार</li>
                            </ul>
                        </div>
                    </div>
                </div>
                
                <div class="stats-grid">
                    <div class="stat-card">
                        <div class="stat-number">88 लाख</div>
                        <div class="stat-label">Farmer IDs जेनरेटेड</div>
                    </div>
                    <div class="stat-card">
                        <div class="stat-number">70,000+</div>
                        <div class="stat-label">स्थानीय युवा नियुक्त</div>
                    </div>
                    <div class="stat-card">
                        <div class="stat-number">207</div>
                        <div class="stat-label">नई फसलें पहचानी गई</div>
                    </div>
                    <div class="stat-card">
                        <div class="stat-number">82%</div>
                        <div class="stat-label">AI/ML मैचिंग सटीकता</div>
                    </div>
                </div>
            </div>
        </section>

        <!-- Section 3: Before DCS -->
        <section class="section">
            <div class="content-section">
                <div class="section-header">
                    <h2 class="section-title">DCS से पहले की स्थिति</h2>
                    <p class="section-subtitle">पारंपरिक फसल सर्वेक्षण की समस्याएं</p>
                </div>
                
                <div class="content-grid">
                    <div class="content-card">
                        <div class="card-header">
                            <div class="card-icon"><i class="fas fa-pen-alt"></i></div>
                            <h3 class="card-title">मैन्युअल प्रक्रिया</h3>
                        </div>
                        <div class="card-content">
                            <p>पटवारी द्वारा रजिस्टर में मैन्युअल एंट्री। कोई डिजिटल रिकॉर्ड नहीं, मानवीय त्रुटियों की संभावना ज्यादा।</p>
                        </div>
                    </div>
                    
                    <div class="content-card">
                        <div class="card-header">
                            <div class="card-icon"><i class="fas fa-question-circle"></i></div>
                            <h3 class="card-title">डेटा सत्यापन का अभाव</h3>
                        </div>
                        <div class="card-content">
                            <p>कोई सत्यापन विधि नहीं, फसल की वास्तविक स्थिति की पुष्टि नहीं, झूठे दावों की संभावना।</p>
                        </div>
                    </div>
                    
                    <div class="content-card">
                        <div class="card-header">
                            <div class="card-icon"><i class="fas fa-clock"></i></div>
                            <h3 class="card-title">विलंब</h3>
                        </div>
                        <div class="card-content">
                            <p>फसल बीमा और ऋण प्रक्रियाओं में देरी, किसानों को समय पर सहायता नहीं मिलना।</p>
                        </div>
                    </div>
                    
                    <div class="content-card">
                        <div class="card-header">
                            <div class="card-icon"><i class="fas fa-times-circle"></i></div>
                            <h3 class="card-title">अशुद्धता</h3>
                        </div>
                        <div class="card-content">
                            <p>गलत फसल क्षेत्र रिपोर्टिंग, नीति निर्माण में गलत आंकड़े, संसाधनों का दुरुपयोग।</p>
                        </div>
                    </div>
                </div>
                
                <div class="content-card">
                    <div class="card-header">
                        <div class="card-icon"><i class="fas fa-exclamation-triangle"></i></div>
                        <h3 class="card-title">मुख्य चुनौतियां</h3>
                    </div>
                    <div class="card-content">
                        <ul>
                            <li>फसल डेटा की अशुद्धता के कारण गलत नीति निर्माण</li>
                            <li>बीमा दावों में देरी से किसानों की आर्थिक हानि</li>
                            <li>e-उपार्जन में गलत पंजीकरण</li>
                            <li>सरकारी योजनाओं का गलत लक्ष्यीकरण</li>
                            <li>पारदर्शिता की कमी और भ्रष्टाचार की संभावना</li>
                        </ul>
                    </div>
                </div>
            </div>
        </section>

        <!-- Section 4: Development Journey -->
        <section class="section">
            <div class="content-section">
                <div class="section-header">
                    <h2 class="section-title">विकास यात्रा</h2>
                    <p class="section-subtitle">2017 से अब तक का डिजिटल रूपांतरण</p>
                </div>
                
                <div class="timeline">
                    <div class="timeline-item">
                        <div class="timeline-year">2017 से पहले</div>
                        <div class="timeline-event">पटवारियों द्वारा मैन्युअल फसल सर्वेक्षण</div>
                        <div class="timeline-description">रजिस्टर में हाथ से लिखना, कोई सत्यापन विधि नहीं, पूर्णतः मैन्युअल प्रक्रिया</div>
                    </div>
                    
                    <div class="timeline-item">
                        <div class="timeline-year">2017</div>
                        <div class="timeline-event">फसल सर्वे के लिए मोबाइल ऐप्स की शुरुआत</div>
                        <div class="timeline-description">पटवारी मोबाइल ऐप का उपयोग करके फसल सर्वे, डिजिटलाइजेशन की शुरुआत</div>
                    </div>
                    
                    <div class="timeline-item">
                        <div class="timeline-year">2018</div>
                        <div class="timeline-event">भू-अभिलेखों के साथ एकीकरण</div>
                        <div class="timeline-description">भू-अभिलेख से जुड़े मोबाइल ऐप, बेहतर डेटा मैनेजमेंट</div>
                    </div>
                    
                    <div class="timeline-item">
                        <div class="timeline-year">2020</div>
                        <div class="timeline-event">फसल एंट्री के लिए WebGIS पोर्टल</div>
                        <div class="timeline-description">वेब आधारित GIS पोर्टल में फसल डेटा एंट्री, जियो-स्पेशियल डेटा का उपयोग</div>
                    </div>
                    
                    <div class="timeline-item">
                        <div class="timeline-year">2023</div>
                        <div class="timeline-event">डिजिटल क्रॉप सर्वे पायलट प्रोजेक्ट</div>
                        <div class="timeline-description">सिवनी और नीमच जिलों में पायलट शुरुआत, AI/ML तकनीक का परीक्षण</div>
                    </div>
                    
                    <div class="timeline-item">
                        <div class="timeline-year">2024</div>
                        <div class="timeline-event">सभी जिलों में पूर्ण रोलआउट</div>
                        <div class="timeline-description">राज्य के सभी जिलों में DCS का विस्तार, 70,000+ युवाओं की नियुक्ति</div>
                    </div>
                    
                    <div class="timeline-item">
                        <div class="timeline-year">2025</div>
                        <div class="timeline-event">AI/ML एकीकरण और संवर्धन</div>
                        <div class="timeline-description">कृत्रिम बुद्धिमत्ता और मशीन लर्निंग का पूर्ण उपयोग, सैटेलाइट डेटा एकीकरण</div>
                    </div>
                    
                    <div class="timeline-item">
                        <div class="timeline-year">2026</div>
                        <div class="timeline-event">ड्रोन एनालिटिक्स एकीकरण (भविष्य)</div>
                        <div class="timeline-description">ड्रोन आधारित फसल निगरानी और विश्लेषण, रियल-टाइम मॉनिटरिंग</div>
                    </div>
                    
                    <div class="timeline-item">
                        <div class="timeline-year">2030</div>
                        <div class="timeline-event">वैश्विक मानकों की प्राप्ति (भविष्य)</div>
                        <div class="timeline-description">अंतर्राष्ट्रीय स्तर पर मान्यता प्राप्त सिस्टम, ग्लोबल बेस्ट प्रैक्टिसेज</div>
                    </div>
                </div>
            </div>
        </section>

        <!-- Continue with remaining sections... -->
        <!-- For brevity, I'll create the remaining sections in a simplified format -->
        
        <!-- Section 5: Technology Base -->
        <section class="section">
            <div class="content-section">
                <div class="section-header">
                    <h2 class="section-title">तकनीकी आधार</h2>
                    <p class="section-subtitle">SAARA, AI/ML और सैटेलाइट तकनीक</p>
                </div>
                <div class="content-grid">
                    <div class="content-card">
                        <div class="card-header">
                            <div class="card-icon"><i class="fas fa-mobile-alt"></i></div>
                            <h3 class="card-title">SAARA मोबाइल ऐप</h3>
                        </div>
                        <div class="card-content">
                            <p>ऑफलाइन मोड, जियोटैगिंग, पॉलीगॉन चेक, री-सर्वे कार्यक्षमता</p>
                        </div>
                    </div>
                    <div class="content-card">
                        <div class="card-header">
                            <div class="card-icon"><i class="fas fa-robot"></i></div>
                            <h3 class="card-title">AI/ML इंटीग्रेशन</h3>
                        </div>
                        <div class="card-content">
                            <p>फोटो विश्लेषण, सैटेलाइट इमेजरी मैचिंग, 82% सटीकता</p>
                        </div>
                    </div>
                </div>
            </div>
        </section>

        <!-- Section 6: Process Flow -->
        <section class="section">
            <div class="content-section">
                <div class="section-header">
                    <h2 class="section-title">प्रक्रिया प्रवाह</h2>
                    <p class="section-subtitle">DCS कैसे काम करता है</p>
                </div>
                <div class="content-card">
                    <div class="card-content">
                        <p>स्थानीय युवा पंजीकरण → प्रशिक्षण → फील्ड सर्वे → डेटा अपलोड → AI/ML सत्यापन → अनुमोदन</p>
                    </div>
                </div>
            </div>
        </section>

        <!-- Section 7: Stakeholders -->
        <section class="section">
            <div class="content-section">
                <div class="section-header">
                    <h2 class="section-title">हितधारक</h2>
                    <p class="section-subtitle">युवा, किसान, और सरकारी अधिकारी</p>
                </div>
                <div class="stats-grid">
                    <div class="stat-card">
                        <div class="stat-number">70,000+</div>
                        <div class="stat-label">स्थानीय युवा सर्वेयर</div>
                    </div>
                    <div class="stat-card">
                        <div class="stat-number">88 लाख</div>
                        <div class="stat-label">पंजीकृत किसान</div>
                    </div>
                </div>
            </div>
        </section>

        <!-- Section 8: Achievements -->
        <section class="section">
            <div class="content-section">
                <div class="section-header">
                    <h2 class="section-title">उपलब्धियां</h2>
                    <p class="section-subtitle">DCS की सफलताएं</p>
                </div>
                <div class="stats-grid">
                    <div class="stat-card">
                        <div class="stat-number">594.92 करोड़</div>
                        <div class="stat-label">SCA राशि</div>
                    </div>
                    <div class="stat-card">
                        <div class="stat-number">207</div>
                        <div class="stat-label">नई फसलें पहचानी</div>
                    </div>
                </div>
            </div>
        </section>

        <!-- Section 9: Data Collection -->
        <section class="section">
            <div class="content-section">
                <div class="section-header">
                    <h2 class="section-title">डेटा संग्रह और उपयोग</h2>
                    <p class="section-subtitle">27 सरकारी योजनाओं में एकीकरण</p>
                </div>
                <div class="content-card">
                    <div class="card-content">
                        <p>PM Kisan, फसल बीमा, e-उपार्जन, किसान क्रेडिट कार्ड में डेटा का उपयोग</p>
                    </div>
                </div>
            </div>
        </section>

        <!-- Section 10: Future Technology -->
        <section class="section">
            <div class="content-section">
                <div class="section-header">
                    <h2 class="section-title">भविष्य की तकनीक</h2>
                    <p class="section-subtitle">ड्रोन, IoT, ब्लॉकचेन, 5G</p>
                </div>
                <div class="content-grid">
                    <div class="content-card">
                        <div class="card-header">
                            <div class="card-icon"><i class="fas fa-drone"></i></div>
                            <h3 class="card-title">ड्रोन एनालिटिक्स</h3>
                        </div>
                        <div class="card-content">
                            <p>फसल स्वास्थ्य मॉनिटरिंग, रियल-टाइम निगरानी</p>
                        </div>
                    </div>
                    <div class="content-card">
                        <div class="card-header">
                            <div class="card-icon"><i class="fas fa-cubes"></i></div>
                            <h3 class="card-title">ब्लॉकचेन</h3>
                        </div>
                        <div class="card-content">
                            <p>सप्लाई चेन ट्रेसेबिलिटी, डेटा सिक्योरिटी</p>
                        </div>
                    </div>
                </div>
            </div>
        </section>

        <!-- Section 11: Challenges -->
        <section class="section">
            <div class="content-section">
                <div class="section-header">
                    <h2 class="section-title">चुनौतियां और समाधान</h2>
                    <p class="section-subtitle">तकनीकी और कार्यान्वयन चुनौतियां</p>
                </div>
                <div class="content-card">
                    <div class="card-content">
                        <p>कनेक्टिविटी → ऑफलाइन मोड, डिजिटल साक्षरता → व्यापक प्रशिक्षण</p>
                    </div>
                </div>
            </div>
        </section>

        <!-- Section 12: Economic Impact -->
        <section class="section">
            <div class="content-section">
                <div class="section-header">
                    <h2 class="section-title">आर्थिक प्रभाव</h2>
                    <p class="section-subtitle">बजट, SCA और रोजगार सृजन</p>
                </div>
                <div class="stats-grid">
                    <div class="stat-card">
                        <div class="stat-number">1170.73 करोड़</div>
                        <div class="stat-label">कुल SCA राशि 2024-25</div>
                    </div>
                    <div class="stat-card">
                        <div class="stat-number">129.41 करोड़</div>
                        <div class="stat-label">DCS बजट</div>
                    </div>
                </div>
            </div>
        </section>

        <!-- Section 13: Success Stories -->
        <section class="section">
            <div class="content-section">
                <div class="section-header">
                    <h2 class="section-title">सफलता की कहानियां</h2>
                    <p class="section-subtitle">किसानों और युवाओं पर वास्तविक प्रभाव</p>
                </div>
                <div class="content-card">
                    <div class="card-content">
                        <p>तीव्र बीमा भुगतान, युवाओं को रोजगार, नई फसलों की खोज</p>
                    </div>
                </div>
            </div>
        </section>

        <!-- Section 14: Contact Information -->
        <section class="section">
            <div class="content-section">
                <div class="section-header">
                    <h2 class="section-title">संपर्क जानकारी</h2>
                    <p class="section-subtitle">हेल्पलाइन, पोर्टल और सपोर्ट</p>
                </div>
                
                <div class="content-grid">
                    <div class="content-card">
                        <div class="card-header">
                            <div class="card-icon"><i class="fas fa-phone"></i></div>
                            <h3 class="card-title">हेल्पलाइन</h3>
                        </div>
                        <div class="card-content">
                            <p><strong>CM हेल्पलाइन:</strong> 181</p>
                            <p><strong>ईमेल:</strong> revenueapp.info@mp.gov.in</p>
                        </div>
                    </div>
                    
                    <div class="content-card">
                        <div class="card-header">
                            <div class="card-icon"><i class="fas fa-globe"></i></div>
                            <h3 class="card-title">पोर्टल</h3>
                        </div>
                        <div class="card-content">
                            <p><strong>SAARA Portal:</strong> saara.mp.gov.in</p>
                            <p><strong>MP Bhulekh:</strong> mpbhulekh.gov.in</p>
                            <p><strong>Farmer Registry:</strong> mpfr.agristack.gov.in</p>
                        </div>
                    </div>
                </div>
                
                <div class="content-card">
                    <div class="card-header">
                        <div class="card-icon"><i class="fas fa-video"></i></div>
                        <h3 class="card-title">ऑनलाइन सपोर्ट</h3>
                    </div>
                    <div class="card-content">
                        <p><strong>Google Meet:</strong> meet.google.com/yho-abta-gec</p>
                        <p><strong>समय:</strong> सोम-शुक्र, 10 AM-6 PM</p>
                    </div>
                </div>
                
                <div class="text-center mt-2">
                    <h3>© 2025 मध्य प्रदेश सरकार, भू-अभिलेख एवं राजस्व विभाग</h3>
                    <p><strong>डिजिटल इंडिया की दिशा में एक कदम</strong></p>
                </div>
            </div>
        </section>
    </main>

    <script src="app.js"></script>
</body>
</html>'''

# Write HTML file
with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html_content)

print("✅ index.html file created successfully!")