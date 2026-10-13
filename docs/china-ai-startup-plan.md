# Starting a Profitable AI Company in China — Business Plan

> Status: working draft, October 2026. Figures are planning estimates, not quotes.
> Regulations in China change quickly. **Check every legal and tax item with a
> PRC-qualified lawyer and accountant before acting.**

---

## 1. The one-page answer

| Question | Answer |
|---|---|
| **What should you build?** | A **vertical AI application for businesses**, not a foundation model and not a consumer chatbot. |
| **Best first problem** | Help **Chinese cross-border e-commerce sellers** (Amazon, TikTok Shop, Temu, Shein, AliExpress, Shopee) make listings, ad creative, multilingual customer service and market research for foreign buyers. Runner-up: AI document automation for small manufacturers (quotes, RFQs, BOMs, export paperwork). |
| **Why this one** | The buyer is an owner who decides fast, the return is measured in sales, they already pay for tools, and knowledge of foreign markets and languages is a real edge that big Chinese labs don't specialise in. |
| **How you make money** | A monthly or annual subscription (about ¥399–¥3,999/month), usage top-ups, and paid setup for larger accounts. Aim for 75–85% gross margin by running cheap domestic models. |
| **Where** | **Shenzhen** (the centre of cross-border e-commerce) or **Hangzhou** (Alibaba's ecosystem, DeepSeek, strong AI subsidies). Use Shanghai if you're a foreign founder who needs a foreigner-friendly setup. |
| **Money needed** | Lean path: **¥1–1.5M** (about US$140–210k) gets 2–4 people to first revenue. Funded path: **¥4–6M** gives 18 months of runway with an 8-person team. |
| **When it can be profitable** | About 450 paying customers at ¥1,200/month covers an 8-person team. A realistic target is **18–30 months**, sooner if you also sell setup and services. |
| **Biggest risks** | Big platforms copying you, price wars, regulatory filings, collecting payments, and geopolitics (chips, US investment rules). |

---

## 2. Reality check: the Chinese AI market in 2026

**What has happened:**

- **Foundation models are a commodity.** DeepSeek, Alibaba's Qwen, ByteDance's Doubao, Moonshot's Kimi, Zhipu's GLM, MiniMax, StepFun and others compete on price, and API prices have fallen close to zero. Many strong models are open-weight. **Training your own base model is not a startup business.**
- **Consumer AI is a game for the giants.** Chatbots, companion apps and AI search are dominated by ByteDance, Alibaba, Tencent and Baidu, which give their products away free and fund them with huge marketing budgets.
- **Government support is strong.** The State Council's **"AI+" action plan (人工智能+, Aug 2025)** pushes AI into manufacturing, healthcare, government services, agriculture and consumption. Cities compete with compute vouchers (算力券), rent subsidies, talent programmes and guidance funds.
- **Buyers are price-sensitive.** Chinese businesses pay less for SaaS than Western ones, and large companies and SOEs prefer on-premise deployment (私有化部署) sold as projects with long payment terms. Small businesses pay for tools only when the payback is obvious and quick.
- **Going global (出海) is a national priority.** Hundreds of thousands of Chinese sellers and brands sell abroad, and they struggle with language, culture, platform rules and creative production for foreign markets.

**What this means for you:**

1. Don't compete on the model. Compete on **workflow, data, distribution and trust** in one niche.
2. Sell to buyers who can **tie your product to revenue or cost savings** within weeks.
3. Use **domestic open-weight or API models** and keep the model layer swappable, because prices and rankings change every quarter.
4. Build a moat from **proprietary data and integrations** (your customers' catalogues, ad performance data, platform APIs) and from **channel relationships**.

---

## 3. Your first decision: who you are legally

Your nationality and residency change the company structure, cost and timeline more than anything else. Pick your path first.

### Path A — You are a PRC citizen, or have a trusted PRC co-founder who owns the company
- Register a **domestic limited liability company (有限责任公司)**. It takes about 2–4 weeks.
- Domestic ownership means no foreign-investment restrictions on internet licences.
- This is the easiest route to RMB funds, government subsidies and SOE customers.
- **If you rely on a co-founder:** put a proper shareholder agreement, vesting and IP assignment in place from day one. Hand-shake deals between foreign and local founders are a classic way to lose a company.

### Path B — You are a foreign founder
- Register a **foreign-invested enterprise (FIE, often called a WFOE)**, typically under a **Hong Kong holding company**. It takes about 1–3 months.
- **Internet licence limits:** value-added telecom services (VATS), which include commercial ICP licences, have historically been capped at 50% foreign ownership. E-commerce platform operations and a few other categories are fully open. Since 2024, **pilot zones in Beijing, Shanghai, Hainan and Shenzhen** have opened more categories, including some information services and online data processing, to 100% foreign ownership. **Confirm the current scope and your eligibility with a lawyer.**
- **Avoid VIE structures** unless a lawyer insists. They're complex, fragile and now need CSRC review for overseas listing.
- You need a **work permit and residence permit** (Z visa route). Young STEM graduates can also look at the **K visa** introduced in Oct 2025.
- **If you are a US person, or take US investors:** the **US Outbound Investment Security Program (effective Jan 2025)** prohibits or requires notification for certain US investments in Chinese AI companies, depending on the end use and the compute used. An **application-layer company that doesn't train frontier models and doesn't serve military or surveillance users** usually sits outside the prohibited zone, but **get US counsel to confirm**.
- **US model providers** (OpenAI, Anthropic, Google) don't serve mainland China or Chinese-controlled companies. Plan on **domestic models** for the China product.

### Path C — Hybrid: an offshore company serving Chinese customers
- Use a Hong Kong or Singapore company with a small mainland FIE for sales, support and invoicing (fapiao).
- This works well for the cross-border e-commerce idea, because the content you produce goes overseas. It can also let you use non-Chinese models for the **overseas-facing** parts.
- **Data flows still need care.** Chinese sellers' personal and business data leaving China falls under the cross-border data rules (see §7).

---

## 4. Which problem to solve

### 4.1 How the ideas were scored
Each idea is scored 1–5 on six factors:
- **Pain:** how badly the customer needs it
- **Pay:** willingness and speed to pay
- **Reg:** regulatory ease (5 = easy)
- **Giant:** distance from what the big platforms do (5 = far)
- **Edge:** advantage for a small or foreign team
- **Cash:** time to revenue (5 = fast)

| # | Idea | Pain | Pay | Reg | Giant | Edge | Cash | **Total** |
|---|---|---|---|---|---|---|---|---|
| 1 | **AI growth copilot for cross-border e-commerce sellers** | 5 | 4 | 4 | 3 | 5 | 5 | **26** |
| 2 | **AI document automation for SME manufacturers and exporters** (RFQs, quotes, BOMs, customs and compliance documents, multilingual emails) | 4 | 4 | 5 | 4 | 3 | 4 | **24** |
| 3 | AI visual quality inspection for factories | 5 | 4 | 5 | 4 | 2 | 2 | 22 |
| 4 | Private enterprise knowledge base and agents (on-premise open models for law firms, hospitals' admin side, SOEs) | 4 | 3 | 4 | 2 | 2 | 3 | 18 |
| 5 | AI compliance for Chinese AI and tech companies going abroad (EU AI Act, GDPR, US state laws) | 4 | 4 | 5 | 5 | 4 | 3 | 25* |
| 6 | Elder-care and "silver economy" AI (care-home operations, companion devices) | 4 | 2 | 3 | 4 | 2 | 2 | 17 |
| 7 | Consumer chatbot, companion or AI search app | 2 | 1 | 1 | 1 | 1 | 1 | 7 |
| 8 | Medical diagnosis AI | 5 | 3 | 1 | 3 | 1 | 1 | 14 |
| 9 | K-12 tutoring AI | 4 | 4 | 2 | 1 | 1 | 2 | 14 |

\*Idea 5 is mainly a services business (consulting plus tooling). It's an excellent fit **if you have a legal or compliance background**, and it pairs well with idea 1.

### 4.2 Recommended: AI growth copilot for cross-border sellers

**Customer:** small and mid-size Chinese sellers with ¥5M–¥200M in annual GMV on Amazon, TikTok Shop, Temu, Shein, AliExpress, Shopee and Lazada. They cluster in **Shenzhen, Guangzhou, Yiwu, Xiamen, Hangzhou and Ningbo**.

**Their problems:**
1. **Listings and SEO in foreign languages.** Titles, bullets, A+ content and keywords that read as native, follow each platform's rules and rank well. Most sellers rely on underpaid operators (运营) writing in poor English, German, Spanish or Japanese.
2. **Ad and social creative at volume.** Product images, lifestyle scenes, short videos with voice-over, and TikTok hooks localised for each market. Agencies are slow and expensive.
3. **Customer service in many languages around the clock**, plus handling reviews and returns.
4. **Market and competitor research.** What to sell, review mining ("what do buyers complain about?"), pricing, and spotting compliance risks (IP and trademark conflicts, banned claims, product certifications).
5. **Platform-rule compliance.** Account suspensions destroy sellers, so a pre-flight check of listings and creative for policy and IP violations is valuable.

**Product, built in stages (start narrow):**
- **MVP (months 0–4):** a **listing and creative studio**. Upload a product (photos plus a Chinese description) and get platform-ready listings in 5–10 languages, plus 20 ad images and 3 short-video scripts. Add a compliance and IP pre-check. Output is one-click export, or a direct push through platform APIs where they allow it.
- **v2:** **review and competitor intelligence.** Scrape or ingest reviews and competitor listings and produce product-improvement and positioning reports.
- **v3:** **multilingual customer-service agent** connected to marketplace messaging, Shopify and email.
- **v4:** **agentic operations.** Ad optimisation suggestions, pricing alerts and a weekly AI operator report. This is where retention and pricing power come from.

**Why you can win:**
- Native-quality foreign-market judgement is scarce in Chinese teams. If you or a co-founder have lived in target markets, that's a real moat.
- The big platforms' own tools work only on their own platform. Sellers are on 3–5 platforms and want **one cross-platform workspace**.
- The outcome is measurable ("CTR up 18%, an operator's time cut in half"), which makes case studies easy and referrals powerful in tightly networked seller communities.

**Watch out:**
- Competitors already exist, including Chinese SaaS for cross-border sellers (ERP and ad tools adding AI features) and Western tools such as Jasper and Helium 10's AI. You differentiate through **output quality in the target language, multi-platform coverage, compliance checks, and Chinese-language UX, support and payment**.
- Platform API access changes. Don't build a business that depends on one platform's goodwill.

### 4.3 Runner-up: document AI for SME manufacturers and exporters
Use this if you have manufacturing or supply-chain experience or contacts.
- **Problem:** small factories in the Pearl River Delta, Yangtze River Delta and Zhejiang spend many staff hours turning customer RFQs, drawings and emails (often in English or other languages) into quotes, BOMs, production orders, customs documents and certificates of origin.
- **Product:** an inbox-to-quote agent that reads RFQs and drawings, pulls prices from the factory's spreadsheets or ERP, drafts the quote and reply email in the buyer's language, and logs it.
- **Why:** low regulatory burden (B2B, internal use), and government "智改数转" (smart manufacturing and digital transformation) subsidies can **pay for part of the customer's purchase**.
- **Risk:** longer sales cycles, more custom integration work, and buyers who want on-premise deployment.

---

## 5. Business model and unit economics

### 5.1 Pricing (cross-border copilot)

| Plan | Price (RMB) | For | Includes |
|---|---|---|---|
| Starter | ¥399/mo (¥3,990/yr) | Solo sellers | 1 seat, 50 listings/mo, 300 images, 2 languages |
| Growth | ¥1,299/mo (¥12,990/yr) | 3–15 person teams | 5 seats, 300 listings, 2,000 images, 10 languages, compliance check |
| Pro / Brand | ¥3,999+/mo | Brands, agencies | Unlimited seats, API, customer-service agent, priority support |
| Enterprise | ¥50k–300k/yr + setup | Large sellers, agencies | Custom models trained on their catalogue, private deployment option |
| Credits | Pay as you go | Everyone | Extra video, image and translation volume |

- **Push annual prepayment.** Chinese SMEs respond well to discounts (for example "2 months free"), and prepayment fixes cash flow.
- **Every paying customer must get a fapiao.** Offer both general VAT fapiao (普票) and special VAT fapiao (专票).
- **Collect payment** by WeChat Pay and Alipay for small plans and corporate bank transfer for larger ones.

### 5.2 Unit economics (targets)

| Metric | Target | Notes |
|---|---|---|
| Blended ARPU | ~¥1,200/month | Mix of Starter, Growth and Pro |
| Model and compute cost per customer | ¥80–250/month | Domestic text APIs are very cheap. Image and video generation is the main cost, so meter it with credits. |
| Gross margin | 75–85% | Include support and cloud costs |
| Monthly logo churn | ≤4% (SMB reality is 4–7%) | Annual plans reduce it |
| LTV | ≈ ¥1,200 × 0.8 ÷ 0.04 ≈ **¥24,000** | |
| CAC (blended) | ≤ ¥6,000 | Keeps LTV:CAC ≥ 3:1 |
| CAC payback | ≤ 6 months | |
| Channel partner commission | 20–40% of first-year revenue | Agents and resellers are standard in China |

### 5.3 Early revenue to fund the company
- Sell **paid pilots and "done-for-you" creative packages** (for example ¥5k–20k per product launch) in the first 3–6 months. This brings in revenue and training examples.
- **Rule:** services must never exceed about 30% of revenue after month 12, or you become an agency.

---

## 6. Technology plan

### 6.1 Architecture
- **Model layer (swappable):** a routing layer over domestic APIs (DeepSeek, Qwen on Alibaba Cloud Bailian, Doubao on Volcano Engine, Kimi, GLM) plus **self-hosted open-weight models** (Qwen and DeepSeek families) on rented GPUs for cost control and private deployments.
- **Images and video:** domestic image and video generation APIs (Kling, Hailuo, Seedream/Seedance, Wan/Tongyi Wanxiang and similar), plus open models for product-image editing.
- **Your moat layer:**
  - platform-specific prompt and agent pipelines
  - an evaluation set per language and platform (for example "would a native German Amazon shopper trust this listing?")
  - a compliance rule engine
  - a customer catalogue and memory store (vector database plus relational database)
  - performance-feedback loops that learn from CTR and conversion data
- **Cloud:** host in mainland China (Alibaba Cloud, Tencent Cloud or Volcano Engine) for the China-facing app. ICP filing is required for any mainland-hosted website.
- **Compute:** **don't buy GPUs early.** US export controls limit high-end Nvidia chips in China. Rent from domestic clouds and apply for **city compute vouchers (算力券)**, which can cover a meaningful share of compute costs in cities such as Shanghai, Shenzhen, Beijing, Hangzhou and Chengdu.

### 6.2 Build principles
1. **Evals before features.** Score output quality per language and platform automatically, with native-speaker spot checks.
2. **Keep the model layer abstract.** Switch providers when price or quality changes.
3. **Log everything** to meet AI-content labelling and record-keeping duties (see §7).
4. **Mobile-first and WeChat-native.** Sellers live in WeChat and WeCom, so ship a **WeChat mini-program** and WeCom notifications, not only a web app.

---

## 7. Legal and regulatory checklist

### 7.1 Company setup
- [ ] Choose a structure (§3) and **register the company**. The business scope should include items such as 人工智能应用软件开发, 技术服务, 软件开发, 信息技术咨询服务 and 互联网信息服务 (if applicable).
- [ ] **Registered capital:** keep it modest. Since the **2024 Company Law**, subscribed capital must be paid in within **5 years**.
- [ ] **Registered address:** use an incubator or industrial park. They often give **free or subsidised space**, help with registration, and connect you to subsidies.
- [ ] Company seals (chops), a basic bank account, tax registration, the fapiao system and social insurance accounts.
- [ ] Hire a **local agency accountant (代理记账)**, typically ¥300–1,500/month. Monthly and quarterly filings are compulsory even with zero revenue.

### 7.2 Internet and AI rules

| Requirement | When it applies | Action |
|---|---|---|
| **ICP filing (ICP备案)** | Any mainland-hosted website or app | File through your cloud provider. It takes about 1–3 weeks. |
| **ICP commercial licence (ICP经营许可证)** | Charging for internet information services | Apply to the provincial communications administration. Foreign ownership limits apply (§3). |
| **App and mini-program filing** | Apps and mini-programs distributed in China | File through app stores or WeChat |
| **Generative AI service filing or registration (生成式人工智能服务备案/登记)** | Generative AI services offered **to the public in China** (Interim Measures, Aug 2023). Applications that **call an already-filed model through its API** generally use the lighter provincial **registration (登记)** route rather than full model filing. Purely internal or non-public enterprise use is largely outside scope. | Prepare a security assessment, content-safety mechanisms and a corpus and keyword filtering policy. Start early, as it can take months. |
| **Algorithm filing (算法备案)** | Recommendation algorithms and deep synthesis (generating or editing images, video or voice) that have public-opinion or mobilisation attributes, or are deep synthesis services | File on the CAC algorithm filing system |
| **AI-generated content labelling** | All AI-generated text, images, audio and video (**Labelling Measures and national standard GB 45438-2025, effective Sept 2025**) | Add visible labels where required, embedded metadata or watermarks, and keep logs |
| **Content safety** | All public-facing generation | Moderation filters, a complaints channel, real-name user registration (phone number) |
| **Cybersecurity Law (amended, in force Jan 2026, now includes AI provisions)** | Everyone | Assign security responsibility and keep incident-response and logging procedures |
| **MLPS 2.0 (等级保护 / 等保)** | Most information systems; often a **procurement requirement** for larger customers | Get Level 2 certification once you sell to mid-size and large companies (roughly ¥50k–150k) |

### 7.3 Data and privacy
- **PIPL (个人信息保护法):** a privacy policy, separate consent for sensitive data, data minimisation, and a personal information protection officer if you reach the volume thresholds.
- **Data Security Law:** classify your data. Customer business data such as product catalogues is usually low-risk, but **any "important data" designation changes everything**.
- **Cross-border data transfer:** the **March 2024 Provisions** relaxed the rules. Many routine business transfers, and transfers of fewer than 100k individuals' personal information per year, are exempt from a security assessment, but **standard contracts or certification may still apply**. If you use non-Chinese models for overseas-facing work, keep **personal data inside China** and send only non-personal product data out.
- **Scraping:** be careful when collecting marketplace reviews and competitor data. Respect platform terms, avoid personal data, and prefer official APIs or licensed data providers. Unfair-competition lawsuits over scraping are common in China.

### 7.4 Intellectual property
- [ ] **Register your trademark in China immediately.** China is first-to-file, and trademark squatters monitor new companies. Register in Chinese characters and Latin script, in classes 9, 35 and 42 at least.
- [ ] Register **software copyrights (软件著作权 / 软著)** for each product module. They're cheap, and they count toward high-tech enterprise status and many subsidy applications.
- [ ] Get **IP assignment and non-compete clauses** signed by every employee and contractor. Non-competes need compensation in China.

### 7.5 Tax
- **Small low-profit enterprise:** effective corporate income tax of about **5%** on taxable profit up to ¥3M under current preferential policies (check that they're still in force).
- **High and New Technology Enterprise (高新技术企业):** **15%** corporate income tax, plus subsidies (often ¥100k–500k from local governments). Apply once you have patents or software copyrights, R&D staff and R&D spending (usually in year 2).
- **R&D super-deduction:** 200% of qualifying R&D expenses.
- **VAT:** 6% on technology services for general taxpayers, with reduced rates for small-scale taxpayers. Software product sales may qualify for VAT refunds. Note the **new VAT Law in force from 2026**, and confirm the details with your accountant.
- **Social insurance and housing fund:** budget **30–40% on top of gross salary** for employer contributions (it varies by city).

---

## 8. Location

| City | Best for | Notes |
|---|---|---|
| **Shenzhen** | Cross-border e-commerce (by far the biggest seller cluster), hardware | Qianhai and Hetao zones offer Hong Kong links and are pilot zones for foreign VATS ownership. Fast-moving, commercial culture. |
| **Hangzhou** | E-commerce (Alibaba), AI (DeepSeek and the "Hangzhou six little dragons"), strong startup subsidies | Very startup-friendly local government. Close to Yiwu (small commodities) and Ningbo (exports). |
| **Shanghai** | Foreign founders, enterprise sales, finance | Lingang and Xuhui AI zones, a model "corpus" and compute support, the most foreigner-friendly administration, a pilot zone. Expensive. |
| **Beijing** | Talent (Tsinghua, Peking University), government and SOE customers, AI research | Zhongguancun and Haidian. Biggest AI talent pool, strong compute vouchers. |
| **Guangzhou / Xiamen / Yiwu** | Seller-dense locations for satellite sales offices | Add later for sales coverage |

**Recommendation:** put the HQ and engineering in **Hangzhou or Shenzhen** and the first sales base in **Shenzhen**. If you're a foreign founder unsure about setup, the **Shanghai or Shenzhen pilot zones** make foreign ownership easier.

**Apply for incubator programmes** in your chosen district. They typically offer free or subsidised office space for 1–3 years, compute vouchers, startup grants (often ¥100k–1M for qualifying teams), talent housing subsidies and introductions to government guidance funds.

---

## 9. Team and hiring

### 9.1 Founding team (ideal)
- **CEO / product:** deep customer understanding (an ex-seller or ex-operator from a cross-border e-commerce company is ideal).
- **CTO:** a full-stack and LLM-application engineer, strong on agents, evals and cost optimisation.
- **Growth / sales lead:** knows seller communities, WeChat groups, trade shows and channel agents.
- **Market expert:** native-level judgement in your main target markets (US, EU, Japan). This can be you.

### 9.2 First hires and salary ranges (tier-1 city, gross annual, 2026 estimates)

| Role | Range (RMB/yr) | When |
|---|---|---|
| Full-stack engineer (mid) | ¥250k–450k | Month 1–3 |
| LLM / AI application engineer | ¥350k–700k (top talent higher) | Month 1–3 |
| Customer success / operator (运营) with seller experience | ¥150k–300k | Month 3–6 |
| Sales / channel manager | ¥150k–300k base plus commission | Month 4–8 |
| Designer (UI and creative QA) | ¥180k–350k | Month 4–8 |
| Native-language QA (part-time or freelance, per language) | Per task | From the MVP |

- Add **30–40% on-costs** for social insurance and housing fund.
- **Equity:** use an **ESOP through a limited partnership holding platform (持股平台)**, the standard structure in China. Vest over 4 years with a 1-year cliff.
- **Hiring sources:** Boss直聘, Liepin, Maimai, university career fairs, V2EX and GitHub communities, and seller communities (for operators).

---

## 10. Go-to-market

### 10.1 Channels, in priority order
1. **Seller communities.** WeChat groups, cross-border e-commerce associations (跨境电商协会), and Amazon and TikTok Shop service-provider networks. Give **live demos inside the groups**: show a real seller's listing rewritten, with before-and-after numbers.
2. **Content marketing on Douyin, Xiaohongshu, WeChat Channels (视频号) and Zhihu.** Run "teardown" videos (rewrite a famous seller's listing live), free templates, and market-trend reports. Cross-border sellers consume a great deal of educational content.
3. **Trade shows and events.** Shenzhen and Xiamen cross-border e-commerce expos, Global Sources, and platform seller summits (Amazon Global Selling China, TikTok Shop events). Book small booths or join panels.
4. **Channel partners (代理商 / 服务商).** ERP vendors, logistics forwarders, payment providers (PingPong, LianLian, Airwallex China), incubators and training schools (培训机构) that already have thousands of sellers. Give them **20–40% revenue share**. This is often the **largest channel** in China.
5. **Free tool to paid conversion.** A free "listing score" mini-program: paste a URL and get a score and three fixes. It captures leads into WeCom, and sales follows up.
6. **Case studies.** Name customers and show their numbers. Proof spreads fast through seller networks.

### 10.2 Sales process
Free trial (7–14 days, phone-verified) → onboarding call → first win within 48 hours → convert to annual plan → referral reward (one free month for both sides).

### 10.3 Relationships matter
- Spend time in person in **Shenzhen and Yiwu**: tea, dinners, seller meetups. Trust is personal before it becomes institutional.
- Get introduced to local government contacts through your incubator. They can unlock subsidies, office space and government-backed customers.

---

## 11. Financial plan

### 11.1 Startup budget — lean path (first 9 months)

| Item | Estimate (RMB) |
|---|---|
| Company registration, legal, trademark, software copyrights | ¥30k–80k (more for a foreign-owned company) |
| Team: founders on minimal pay plus 2 engineers | ¥600k–900k |
| Cloud, APIs and compute (before vouchers) | ¥50k–120k |
| Marketing, events and travel | ¥80k–150k |
| Accounting, office and miscellaneous | ¥50k–100k |
| Buffer (15%) | ¥120k–200k |
| **Total** | **≈ ¥1.0–1.5M** |

### 11.2 Funded path: monthly burn at 8 people (from about month 9)

| Item | Monthly (RMB) |
|---|---|
| Salaries plus on-costs (8 people, about ¥34k each fully loaded) | ¥270k |
| Office (often subsidised) | ¥0–20k |
| Cloud, compute and tools | ¥30k |
| Marketing and channel | ¥80k |
| Legal, accounting and miscellaneous | ¥30k |
| **Total burn** | **≈ ¥410–430k** |

### 11.3 Break-even
- At 80% gross margin you need about **¥540k of monthly revenue**, which is **about 450 customers at ¥1,200 ARPU**, or fewer if enterprise deals land.

### 11.4 Illustrative path to break-even

| Month | Paying customers | MRR (RMB) | Notes |
|---|---|---|---|
| 3 | 10 (paid pilots) | ¥15k + services | MVP in use |
| 6 | 60 | ¥70k | Product–market fit signals |
| 12 | 200 | ¥240k | Channel partners active |
| 18 | 380 | ¥460k | Customer-service agent shipped, higher ARPU |
| 24 | 550 | ¥660k | **Profitable** at the ~8–10 person scale |

### 11.5 Funding sources (in rough order)
1. **Founder money and revenue** (bootstrap via paid pilots and services).
2. **Government grants and incubator prizes** (non-dilutive). Look at district startup grants, innovation and entrepreneurship competitions (创新创业大赛), talent programmes and compute vouchers.
3. **Angel investors**, especially ex-sellers and e-commerce entrepreneurs who will also open doors.
4. **RMB VC and government guidance funds (政府引导基金).** These are now the dominant investors in Chinese early-stage AI. They often require you to **register or relocate in their district** and may set local hiring or tax targets.
5. **USD VC:** scarce for China-only companies since 2023. It's possible for "出海"-oriented companies with an offshore holding structure, subject to the US outbound investment rules.

---

## 12. Roadmap and milestones

### Phase 0 — Validate (weeks 0–8)
- [ ] Talk to **30–50 sellers** in Shenzhen, Hangzhou and Yiwu (in person if possible). Ask what they spend time and money on, what they've tried, and what they'd pay.
- [ ] Hand-deliver the service: produce listings and creative for **5 sellers** using existing tools and your own judgement, and measure CTR and conversion before and after.
- [ ] Decide your structure (§3) and talk to a lawyer and an accountant.
- [ ] File trademarks.
- **Exit criterion:** at least 5 sellers **pay** (not just say yes) for the manual service, with measurable improvement.

### Phase 1 — Build the MVP and first revenue (months 2–6)
- [ ] Register the company, bank account and ICP filing, and join an incubator.
- [ ] Build the listing and creative studio for **one platform (Amazon US) and one or two languages**, then expand.
- [ ] Set up the evaluation framework and native-speaker QA.
- [ ] Ship the WeChat mini-program and WeCom support.
- [ ] Prepare the **generative AI registration or filing** and AI-content labelling.
- **Exit criterion:** **60 paying customers**, at least 40% weekly active, and more than 80% renewing after month 2.

### Phase 2 — Product–market fit and channels (months 6–12)
- [ ] Add platforms (TikTok Shop, Temu, Shopee) and 10 languages.
- [ ] Launch review and competitor intelligence.
- [ ] Sign 3–5 channel partners.
- [ ] Apply for software copyrights and start the high-tech enterprise application.
- [ ] Raise an angel or seed round if needed (¥3–8M).
- **Exit criterion:** **¥200k+ MRR**, LTV:CAC ≥ 3, and monthly churn ≤ 5%.

### Phase 3 — Scale and profitability (months 12–24)
- [ ] Launch the multilingual customer-service agent and agentic operations features.
- [ ] Run an enterprise tier with private deployment for large sellers and agencies.
- [ ] Get MLPS Level 2 certification.
- [ ] Consider adjacent expansion: Southeast Asian sellers, Chinese brands' DTC sites, and a compliance consulting add-on (idea 5).
- **Exit criterion:** **profitable on a monthly basis**, with an option to raise a Series A for faster growth or keep growing on profits.

### When to stop or pivot
- After 8 weeks of Phase 0, fewer than 3 sellers will pay for the result → **switch to idea 2 or 5**.
- After 6 months, more than 8% monthly churn → you have a novelty product rather than a workflow product. Go deeper into one workflow.
- A major platform ships a free equivalent → move further into **cross-platform features, compliance and agentic operations**, which a single platform won't build.

---

## 13. Risks and mitigations

| Risk | Likelihood | Mitigation |
|---|---|---|
| Big platforms (Alibaba, ByteDance, Amazon) ship free AI tools | High | Stay cross-platform, use proprietary performance data, be the compliance layer, and keep service close to customers |
| Model price or quality shifts | High (and mostly good for you) | Abstract the model layer and re-run evals monthly |
| Regulatory filing delays | Medium | Start filing early, launch B2B and invite-only first, and work with a compliance consultant |
| Payment collection and receivables | Medium | Prepayment and annual plans, avoid long-payment SOE deals early, and use channel partners who collect payment |
| Geopolitics (tariffs on Chinese exports, US outbound investment rules, chip controls) | Medium | Tariff pressure **raises** sellers' need to diversify markets (EU, Japan, Middle East, Southeast Asia, Latin America), so position as the multi-market tool. Rent compute instead of owning it. Get legal review of investors. |
| Key-person or co-founder disputes | Medium | Clear shareholder agreement, vesting and IP assignment from day one |
| Scraping or IP lawsuits | Low–Medium | Use official APIs and licensed data, and take legal advice on data collection |
| Platform-policy changes in customers' markets (Amazon AI-content rules, EU AI Act transparency duties) | Medium | Build compliance checks into the product and make them a feature |

---

## 14. Next 30 days

1. **Decide your path (§3):** citizen, foreign founder or hybrid. Book **two calls with PRC lawyers** (ask for fixed-fee company setup quotes) and one with a US or home-country lawyer if you're a US person or have foreign investors.
2. **Write down your unfair advantage.** Which markets and languages do you know natively? Which industries? Use that to choose between ideas 1, 2 and 5.
3. **Book a 1–2 week trip to Shenzhen, Hangzhou and Yiwu.** Interview 30 sellers, visit 2 incubators, and attend one cross-border e-commerce meetup.
4. **Run a manual concierge test** with 5 sellers, and charge for it.
5. **File trademarks** in China (Chinese and English name).
6. **Prototype:** build a basic listing generator on a domestic model API in a weekend and measure output quality against human-written listings.
7. **Set your financial plan:** how much of your own money you can commit, and lean versus funded path.
8. **Find a co-founder** if you're missing the seller-community or engineering profile.

---

## 15. Questions that would sharpen this plan

- Are you a PRC citizen, a foreign national, or a US person?
- Which languages and countries do you know deeply?
- What's your background: engineering, sales, e-commerce, manufacturing, legal?
- How much capital can you commit, and how long can you go without salary?
- Do you already have a network in China (sellers, factories, government, investors)?

With these answers the plan can be tightened into a specific company design, a detailed 24-month financial model and a pitch deck.
