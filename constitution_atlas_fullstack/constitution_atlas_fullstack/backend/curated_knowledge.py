"""
Curated Institutional, Administrative, Philosophical, Judicial, Historical,
and Process Nodes, Verified Directional Edges, 6 Interactive Simulations,
"Trace the Power" Chain, 8 Mandatory Exploration Journeys, and Authoritative Sources
for CONSTITUTION ATLAS.
"""

PRIMARY_CLUSTERS = [
    {
        "id": "cluster_rights",
        "node_type": "Cluster",
        "subcategory": "Constitutional Pillar",
        "title": "Fundamental Rights (Part III)",
        "code": "Cluster 1",
        "summary": "Enforceable civil and political liberties guaranteed under Articles 12–35 protecting individuals against arbitrary State action.",
        "constitutional_basis": "Part III (Articles 12 to 35)",
        "authority_type": "Constitutional Text"
    },
    {
        "id": "cluster_dpsp",
        "node_type": "Cluster",
        "subcategory": "Constitutional Pillar",
        "title": "Directive Principles of State Policy (Part IV)",
        "code": "Cluster 2",
        "summary": "Socio-economic principles fundamental in the governance of the country (Articles 36–51), guiding the State toward a welfare democracy.",
        "constitutional_basis": "Part IV (Articles 36 to 51)",
        "authority_type": "Constitutional Text"
    },
    {
        "id": "cluster_duties",
        "node_type": "Cluster",
        "subcategory": "Constitutional Pillar",
        "title": "Fundamental Duties (Part IVA)",
        "code": "Cluster 3",
        "summary": "Eleven civic and moral obligations of every citizen of India enshrined in Article 51A.",
        "constitutional_basis": "Part IVA (Article 51A)",
        "authority_type": "Constitutional Text"
    },
    {
        "id": "cluster_union_exec",
        "node_type": "Cluster",
        "subcategory": "Institutional Pillar",
        "title": "Union Executive",
        "code": "Cluster 4",
        "summary": "The President, Vice-President, Prime Minister, Council of Ministers, and Attorney-General exercising the executive power of the Union.",
        "constitutional_basis": "Part V, Chapter I (Articles 52 to 78)",
        "authority_type": "Constitutional Text"
    },
    {
        "id": "cluster_parliament",
        "node_type": "Cluster",
        "subcategory": "Institutional Pillar",
        "title": "Parliament of India",
        "code": "Cluster 5",
        "summary": "The supreme federal legislative body comprising the President, Rajya Sabha (Council of States), and Lok Sabha (House of the People).",
        "constitutional_basis": "Part V, Chapter II (Articles 79 to 122)",
        "authority_type": "Constitutional Text"
    },
    {
        "id": "cluster_judiciary",
        "node_type": "Cluster",
        "subcategory": "Institutional Pillar",
        "title": "Integrated Judiciary",
        "code": "Cluster 6",
        "summary": "A unified judicial hierarchy headed by the Supreme Court of India, High Courts in States, and Subordinate District Courts.",
        "constitutional_basis": "Part V Ch. IV (Arts. 124–147) & Part VI Ch. V–VI (Arts. 214–237)",
        "authority_type": "Constitutional Text"
    },
    {
        "id": "cluster_states",
        "node_type": "Cluster",
        "subcategory": "Institutional Pillar",
        "title": "State Governments",
        "code": "Cluster 7",
        "summary": "Constitutional machinery in the States comprising the Governor, Chief Minister, State Council of Ministers, and State Legislature.",
        "constitutional_basis": "Part VI (Articles 152 to 237)",
        "authority_type": "Constitutional Text"
    },
    {
        "id": "cluster_federalism",
        "node_type": "Cluster",
        "subcategory": "Structural Pillar",
        "title": "Federalism & Centre–State Relations",
        "code": "Cluster 8",
        "summary": "Distribution of legislative, administrative, and financial powers between the Union and the States, anchored in Parts XI–XII and the Seventh Schedule.",
        "constitutional_basis": "Parts XI & XII (Articles 245 to 293), Seventh Schedule",
        "authority_type": "Constitutional Text"
    },
    {
        "id": "cluster_local_govt",
        "node_type": "Cluster",
        "subcategory": "Institutional Pillar",
        "title": "Local Self-Government (Panchayats & Municipalities)",
        "code": "Cluster 9",
        "summary": "Constitutionalized third tier of grassroots rural (Part IX) and urban (Part IXA) democratic governance and Co-operative Societies (Part IXB).",
        "constitutional_basis": "Parts IX, IXA, IXB (Articles 243 to 243ZT), 11th & 12th Schedules",
        "authority_type": "Constitutional Text"
    },
    {
        "id": "cluster_const_bodies",
        "node_type": "Cluster",
        "subcategory": "Institutional Pillar",
        "title": "Independent Constitutional Bodies",
        "code": "Cluster 10",
        "summary": "Autonomous fourth-branch institutions safeguarding fiscal integrity, meritocracy, federalism, and social justice (CAG, UPSC, Finance Commission, GST Council, NCSC, NCST, NCBC).",
        "constitutional_basis": "Articles 148, 279A, 280, 315, 324, 338, 338A, 338B",
        "authority_type": "Constitutional Text"
    },
    {
        "id": "cluster_elections",
        "node_type": "Cluster",
        "subcategory": "Democratic Pillar",
        "title": "Elections & Democratic Representation",
        "code": "Cluster 11",
        "summary": "Universal adult suffrage, Election Commission of India, delimitation, reservations in legislatures, and electoral laws.",
        "constitutional_basis": "Part XV (Articles 324 to 329) & Part XVI (Articles 330 to 334A)",
        "authority_type": "Constitutional Text"
    },
    {
        "id": "cluster_administration",
        "node_type": "Cluster",
        "subcategory": "Administrative Pillar",
        "title": "Indian Administrative System",
        "code": "Cluster 12",
        "summary": "Union Ministries, Cabinet Secretariat, All-India & Central Civil Services, District Magistrates/Collectors, SDMs, Tehsildars, and Regulatory Authorities.",
        "constitutional_basis": "Articles 53, 73, 77, 154, 166, 309 to 312 & Rules of Business",
        "authority_type": "Administrative Practice"
    },
    {
        "id": "cluster_amendments",
        "node_type": "Cluster",
        "subcategory": "Constitutional Pillar",
        "title": "Constitutional Amendments",
        "code": "Cluster 13",
        "summary": "Constituent power under Article 368 and the evolution of the Constitution across 106 Amendment Acts (1951–2023).",
        "constitutional_basis": "Part XX (Article 368)",
        "authority_type": "Constitutional Text"
    },
    {
        "id": "cluster_history",
        "node_type": "Cluster",
        "subcategory": "Historical Pillar",
        "title": "Constitutional History & Constituent Assembly",
        "code": "Cluster 14",
        "summary": "Historical evolution from the Government of India Act 1935 through the Constituent Assembly Debates (1946–1949) to post-1950 constitutional milestones.",
        "constitutional_basis": "Article 395 & Constituent Assembly Debates",
        "authority_type": "Historical Evidence"
    },
    {
        "id": "cluster_philosophy",
        "node_type": "Cluster",
        "subcategory": "Philosophical Pillar",
        "title": "Political Philosophy & Constitutional Doctrines",
        "code": "Cluster 15",
        "summary": "Foundational values (Liberty, Equality, Justice, Fraternity, Dignity, Secularism, Constitutional Morality, Rule of Law) and judicial doctrines (Basic Structure).",
        "constitutional_basis": "Preamble, Parts III & IV, and Constitutional Jurisprudence",
        "authority_type": "Philosophical Analysis"
    },
    {
        "id": "cluster_processes",
        "node_type": "Cluster",
        "subcategory": "Process Pillar",
        "title": "Democratic & Legislative Processes",
        "code": "Cluster 16",
        "summary": "Step-by-step constitutional workflows: lawmaking, Money Bills, budget, government formation, no-confidence motions, emergencies, and judicial review.",
        "constitutional_basis": "Articles 75, 107–117, 32, 226, 352–360, 368",
        "authority_type": "Constitutional Text"
    }
]

CURATED_NODES = [
    # --- INSTITUTIONAL NODES ---
    {
        "id": "inst_parliament",
        "node_type": "Institutional",
        "subcategory": "Union Legislature",
        "title": "Parliament of India (Sansad)",
        "code": "Art. 79",
        "cluster_id": "cluster_parliament",
        "authority_type": "Constitutional Text",
        "establishment_type": "Constitutionally Established (Article 79)",
        "constitutional_basis": "Part V, Chapter II (Articles 79–122)",
        "summary": "The supreme legislative institution of the Republic of India, consisting of the President and two Houses: the Council of States (Rajya Sabha) and the House of the People (Lok Sabha).",
        "powers_and_functions": [
            "Enacting laws on Union List (97/100 items) and Concurrent List (47/52 items) under Article 246",
            "Constituent power to amend the Constitution under Article 368",
            "Financial control over the Consolidated Fund of India (Articles 110, 112–117, 266)",
            "Holding the Union Executive (Council of Ministers) accountable via questions, motions, and committees (Article 75(3))",
            "Impeachment of the President (Article 61) and removal of Supreme Court/High Court Judges (Article 124(4))"
        ],
        "checks_and_balances": "Laws passed by Parliament are subject to judicial review by the Supreme Court and High Courts under Articles 13, 32, and 226, and cannot violate the Basic Structure of the Constitution (Kesavananda Bharati, 1973).",
        "explanations": {
            "beginner": "Parliament is India's national law-making body. It has three parts: the President, the Lok Sabha (directly elected by citizens), and the Rajya Sabha (representing the States).",
            "intermediate": "Established under Article 79, Parliament exercises legislative power over the Union and Concurrent Lists, approves the Union Budget, and holds the Prime Minister and Cabinet accountable.",
            "advanced": "Unlike the British Parliament, the Indian Parliament is not sovereign; it operates within a written federal Constitution with judicial review (Article 13) and Basic Structure limitations on Article 368.",
            "research": "Parliament's bicameral design balances Westminster responsible government (Article 75(3) collective responsibility solely to Lok Sabha) with federal representation (Rajya Sabha's special powers under Articles 249 and 312)."
        }
    },
    {
        "id": "inst_lok_sabha",
        "node_type": "Institutional",
        "subcategory": "Lower House of Parliament",
        "title": "Lok Sabha (House of the People)",
        "code": "Art. 81",
        "cluster_id": "cluster_parliament",
        "authority_type": "Constitutional Text",
        "establishment_type": "Constitutionally Established (Article 81)",
        "constitutional_basis": "Articles 79, 81, 83(2), 84, 93, 75(3), 109, 110",
        "summary": "The directly elected lower house of Parliament (up to 550 members elected from territorial constituencies by universal adult suffrage under Article 326). The Council of Ministers is collectively responsible solely to the Lok Sabha.",
        "powers_and_functions": [
            "Exclusive power to introduce and pass Money Bills (Articles 109 & 110); Rajya Sabha can only make recommendations within 14 days",
            "Holds the Union Council of Ministers collectively responsible under Article 75(3); can remove the government via a No-Confidence Motion (Rule 198)",
            "Passes Demand for Grants and the Appropriation Bill authorizing expenditure from the Consolidated Fund of India (Articles 113–114)",
            "Co-equal legislative and constituent powers with Rajya Sabha on Ordinary Bills (Article 107) and Constitutional Amendment Bills (Article 368)"
        ],
        "checks_and_balances": "Subject to dissolution by the President (Article 85(2)(b)), constitutional limits on legislative competence (Article 246), and Fundamental Rights scrutiny (Article 13).",
        "explanations": {
            "beginner": "The Lok Sabha is the 'House of the People' where citizens directly elect Members of Parliament (MPs) every 5 years. Whichever party or coalition wins a majority here forms the central government.",
            "intermediate": "Composed under Article 81 with a 5-year term (Article 83(2)), the Lok Sabha controls the national purse (Money Bills under Article 110) and commands the survival of the executive under Article 75(3).",
            "advanced": "The Lok Sabha embodies popular sovereignty in India's parliamentary system. Under Article 109, its dominance in financial legislation prevents upper-house deadlocks over supply, while Article 75(3) makes executive survival contingent on its confidence.",
            "research": "Constitutional debates (CAD Vol. VII & VIII) show the framers chose direct territorial election for the House of the People alongside Article 75(3) collective responsibility to anchor daily democratic accountability while subjecting delimitation to Articles 81–82."
        }
    },
    {
        "id": "inst_rajya_sabha",
        "node_type": "Institutional",
        "subcategory": "Upper House of Parliament",
        "title": "Rajya Sabha (Council of States)",
        "code": "Art. 80",
        "cluster_id": "cluster_parliament",
        "authority_type": "Constitutional Text",
        "establishment_type": "Constitutionally Established (Article 80)",
        "constitutional_basis": "Articles 79, 80, 83(1), 89, 249, 312, Fourth Schedule",
        "summary": "The permanent upper house of Parliament (up to 250 members: 238 representing States and UTs elected by elected MLAs via proportional representation with single transferable vote, and 12 nominated by the President for expertise in literature, science, art, and social service).",
        "powers_and_functions": [
            "Permanent chamber not subject to dissolution; one-third of members retire every two years (Article 83(1))",
            "Equal footing with Lok Sabha on Ordinary Bills (Article 107) and Constitutional Amendment Bills (Article 368)",
            "Exclusive federal power under Article 249 to authorize Parliament to legislate on a State List subject in the national interest (by 2/3rds majority)",
            "Exclusive power under Article 312 to authorize creation of new All-India Services common to the Union and the States"
        ],
        "checks_and_balances": "Cannot block Money Bills beyond 14 days (Article 109) and cannot pass a No-Confidence Motion against the Council of Ministers."
    },
    {
        "id": "inst_speaker_ls",
        "node_type": "Institutional",
        "subcategory": "Parliamentary Office",
        "title": "Speaker of the Lok Sabha",
        "code": "Art. 93",
        "cluster_id": "cluster_parliament",
        "authority_type": "Constitutional Text",
        "establishment_type": "Constitutionally Established (Article 93)",
        "constitutional_basis": "Articles 93–97, 100(1), 108(4), 110(3), Tenth Schedule",
        "summary": "Presiding officer of the Lok Sabha elected by its members under Article 93. Guardian of parliamentary privileges, sole authority to certify a Money Bill under Article 110(3), presides over joint sittings (Article 108), and adjudicates disqualification under the Tenth Schedule (subject to judicial review per Kihoto Hollohon, 1992)."
    },
    {
        "id": "inst_parl_committees",
        "node_type": "Institutional",
        "subcategory": "Legislative Oversight",
        "title": "Parliamentary Committees (PAC, Estimates, DRSCs)",
        "code": "Art. 105 / 118",
        "cluster_id": "cluster_parliament",
        "authority_type": "Constitutional Conventions",
        "establishment_type": "Established under Parliamentary Rules (Article 118)",
        "constitutional_basis": "Articles 105 & 118; Rules of Procedure and Conduct of Business",
        "summary": "Standing Financial Committees (Public Accounts Committee, Estimates Committee, Committee on Public Undertakings) and 24 Departmentally Related Standing Committees (DRSCs) that scrutinize bills, ministerial budgets, and CAG audit reports in detail."
    },
    {
        "id": "inst_president",
        "node_type": "Institutional",
        "subcategory": "Head of State",
        "title": "President of India (Rashtrapati)",
        "code": "Art. 52",
        "cluster_id": "cluster_union_exec",
        "authority_type": "Constitutional Text",
        "establishment_type": "Constitutionally Established (Article 52)",
        "constitutional_basis": "Articles 52–62, 72, 74, 75, 77, 85, 111, 123, 143, 352–360",
        "summary": "Constitutional Head of State and Supreme Commander of the Defence Forces (Article 53). Elected indirectly by an Electoral College of elected MPs and MLAs (Article 54). Exercises executive power in accordance with the aid and advice of the Council of Ministers headed by the Prime Minister (Article 74(1)).",
        "powers_and_functions": [
            "Executive power of the Union vested in the President (Article 53); all executive actions taken in the President's name (Article 77)",
            "Appoints the Prime Minister and other Ministers on PM's advice (Article 75), Judges of SC/HCs (Articles 124, 217), CAG (Article 148), ECI (Article 324), Governors (Article 155)",
            "Legislative powers: summons/prorogues/dissolves Lok Sabha (Article 85), grants assent to Bills (Article 111), promulgates Ordinances when Parliament is in recess (Article 123)",
            "Judicial & Clemency power: grants pardons, reprieves, respites, or remissions under Article 72; seeks Supreme Court advisory opinion under Article 143",
            "Emergency powers under Articles 352 (National), 356 (State/President's Rule), and 360 (Financial)"
        ],
        "checks_and_balances": "Bound by the aid and advice of the Council of Ministers under Article 74(1) (with one return for reconsideration via the 44th Amendment); subject to impeachment for 'violation of the Constitution' under Article 61; pardons and emergency proclamations are subject to judicial review (S.R. Bommai, 1994)."
    },
    {
        "id": "inst_vice_president",
        "node_type": "Institutional",
        "subcategory": "Union Executive & Presiding Officer",
        "title": "Vice-President of India",
        "code": "Art. 63",
        "cluster_id": "cluster_union_exec",
        "authority_type": "Constitutional Text",
        "establishment_type": "Constitutionally Established (Article 63)",
        "constitutional_basis": "Articles 63–71, 89",
        "summary": "Second highest constitutional office in India; acts as ex-officio Chairman of the Rajya Sabha (Article 64) and discharges the functions of the President during casual vacancies (Article 65)."
    },
    {
        "id": "inst_pm",
        "node_type": "Institutional",
        "subcategory": "Head of Government",
        "title": "Prime Minister of India",
        "code": "Art. 74–75",
        "cluster_id": "cluster_union_exec",
        "authority_type": "Constitutional Text",
        "establishment_type": "Constitutionally Established (Articles 74, 75, 78)",
        "constitutional_basis": "Articles 74, 75, 78",
        "summary": "Real executive authority and Head of Government in India's Westminster parliamentary system. Appointed by the President (Article 75(1)) as leader of the majority party/coalition in the Lok Sabha; heads the Council of Ministers and serves as the constitutional channel of communication between the Cabinet and the President (Article 78).",
        "powers_and_functions": [
            "Heads the Council of Ministers to aid and advise the President (Article 74(1))",
            "Advises the President on appointment, portfolio allocation, and dismissal of Ministers (Article 75(1)–(2))",
            "Chairs Cabinet meetings and coordinates policy across all Union Ministries and the Cabinet Secretariat",
            "Constitutional duty under Article 78 to communicate all decisions of the Council of Ministers to the President"
        ],
        "checks_and_balances": "Must command the confidence of the Lok Sabha at all times (Article 75(3)); bound by constitutional limits, parliamentary oversight, and judicial review."
    },
    {
        "id": "inst_council_ministers",
        "node_type": "Institutional",
        "subcategory": "Union Executive",
        "title": "Union Council of Ministers & Cabinet",
        "code": "Art. 74–75",
        "cluster_id": "cluster_union_exec",
        "authority_type": "Constitutional Text",
        "establishment_type": "Constitutionally Established (Articles 74 & 75; 'Cabinet' explicitly named in Article 352(3))",
        "constitutional_basis": "Articles 74, 75, 77, 352(3)",
        "summary": "The real executive body directing Union governance, comprising Cabinet Ministers, Ministers of State (Independent Charge), and Ministers of State. Capped at 15% of the total strength of the Lok Sabha by the 91st Constitutional Amendment Act, 2003 (Article 75(1A)). Collectively responsible to the Lok Sabha under Article 75(3)."
    },
    {
        "id": "inst_supreme_court",
        "node_type": "Institutional",
        "subcategory": "Apex Judiciary",
        "title": "Supreme Court of India",
        "code": "Art. 124",
        "cluster_id": "cluster_judiciary",
        "authority_type": "Constitutional Text",
        "establishment_type": "Constitutionally Established (Article 124)",
        "constitutional_basis": "Part V, Chapter IV (Articles 124–147) & Article 32",
        "summary": "The apex constitutional court, final interpreter and guardian of the Constitution, and guarantor of Fundamental Rights (Article 32). Comprises the Chief Justice of India and up to 33 other Judges appointed under Article 124(2) via the Collegium system.",
        "powers_and_functions": [
            "Writ Jurisdiction under Article 32 (itself a Fundamental Right) to enforce Part III rights via Habeas Corpus, Mandamus, Prohibition, Quo Warranto, and Certiorari",
            "Exclusive Original Federal Jurisdiction under Article 131 for disputes between the Union and States or between States",
            "Appellate Jurisdiction in constitutional, civil, and criminal matters (Articles 132–134) and Special Leave to Appeal (Article 136)",
            "Power to do 'complete justice' in any cause or matter under Article 142; law declared by SC is binding on all courts in India (Article 141)",
            "Advisory Jurisdiction on questions of law/fact referred by the President (Article 143) and Judicial Review of legislative/executive actions (Articles 13, 32)"
        ]
    },
    {
        "id": "inst_high_courts",
        "node_type": "Institutional",
        "subcategory": "State Judiciary",
        "title": "High Courts",
        "code": "Art. 214 / 226",
        "cluster_id": "cluster_judiciary",
        "authority_type": "Constitutional Text",
        "establishment_type": "Constitutionally Established (Article 214)",
        "constitutional_basis": "Part VI, Chapter V (Articles 214–231)",
        "summary": "Principal constitutional courts in the States exercising broad writ jurisdiction under Article 226 (both for Fundamental Rights and 'for any other purpose') and superintendence over all subordinate courts and tribunals within their territory under Article 227."
    },
    {
        "id": "inst_subordinate_courts",
        "node_type": "Institutional",
        "subcategory": "District Judiciary",
        "title": "District & Subordinate Courts",
        "code": "Art. 233–237",
        "cluster_id": "cluster_judiciary",
        "authority_type": "Constitutional Text",
        "establishment_type": "Constitutionally Regulated (Articles 233–237)",
        "constitutional_basis": "Part VI, Chapter VI (Articles 233–237)",
        "summary": "The foundational trial judiciary in every district (District & Sessions Judges, Civil Judges, Judicial Magistrates) where citizens first access civil and criminal justice, operating under the administrative control of the respective High Court (Article 235)."
    },
    {
        "id": "inst_eci",
        "node_type": "Institutional",
        "subcategory": "Constitutional Body",
        "title": "Election Commission of India (ECI)",
        "code": "Art. 324",
        "cluster_id": "cluster_elections",
        "authority_type": "Constitutional Text",
        "establishment_type": "Constitutionally Established (Article 324)",
        "constitutional_basis": "Part XV (Articles 324–329)",
        "summary": "Permanent, independent constitutional authority vested with the superintendence, direction, and control of the preparation of electoral rolls and the conduct of elections to Parliament, State Legislatures, and the offices of President and Vice-President (Article 324). The Chief Election Commissioner is protected against arbitrary removal on the same grounds and manner as a Supreme Court Judge (proviso to Article 324(5))."
    },
    {
        "id": "inst_cag",
        "node_type": "Institutional",
        "subcategory": "Constitutional Body",
        "title": "Comptroller and Auditor-General of India (CAG)",
        "code": "Art. 148",
        "cluster_id": "cluster_const_bodies",
        "authority_type": "Constitutional Text",
        "establishment_type": "Constitutionally Established (Article 148)",
        "constitutional_basis": "Part V, Chapter V (Articles 148–151)",
        "summary": "Described by Dr. B.R. Ambedkar as perhaps the most important officer under the Constitution. Audits all receipts and expenditure from the Consolidated Fund of India and of each State/UT (Article 149). Reports are laid before Parliament and State Legislatures (Article 151) and examined by the Public Accounts Committee."
    },
    {
        "id": "inst_finance_comm",
        "node_type": "Institutional",
        "subcategory": "Constitutional Body",
        "title": "Finance Commission of India",
        "code": "Art. 280",
        "cluster_id": "cluster_federalism",
        "authority_type": "Constitutional Text",
        "establishment_type": "Constitutionally Established (Article 280)",
        "constitutional_basis": "Articles 280–281",
        "summary": "Quasi-judicial fiscal federalism institution constituted by the President every five years under Article 280 to recommend vertical devolution (share of States in net proceeds of Union taxes) and horizontal distribution among States, grants-in-aid (Article 275), and measures to augment State Consolidated Funds to support Panchayats and Municipalities."
    },
    {
        "id": "inst_gst_council",
        "node_type": "Institutional",
        "subcategory": "Constitutional Federal Body",
        "title": "Goods and Services Tax (GST) Council",
        "code": "Art. 279A",
        "cluster_id": "cluster_federalism",
        "authority_type": "Constitutional Text",
        "establishment_type": "Constitutionally Established (Article 279A via 101st Amendment, 2016)",
        "constitutional_basis": "Articles 246A, 269A, 279A",
        "summary": "Apex institution of cooperative fiscal federalism chaired by the Union Finance Minister with State Finance Ministers as members. Makes recommendations on GST rates, exemptions, thresholds, and model laws; decisions require a 3/4ths weighted majority (Union holds 1/3rd weight, States together hold 2/3rds weight under Article 279A(9))."
    },
    {
        "id": "inst_upsc",
        "node_type": "Institutional",
        "subcategory": "Constitutional Body",
        "title": "Union Public Service Commission (UPSC) & State PSCs",
        "code": "Art. 315",
        "cluster_id": "cluster_const_bodies",
        "authority_type": "Constitutional Text",
        "establishment_type": "Constitutionally Established (Article 315)",
        "constitutional_basis": "Part XIV, Chapter II (Articles 315–323)",
        "summary": "Independent constitutional recruiting agency safeguarding the merit system in India's civil services by conducting examinations for All-India Services and Central Services (Article 320) and advising on disciplinary and service matters."
    },
    {
        "id": "inst_ag",
        "node_type": "Institutional",
        "subcategory": "Constitutional Office",
        "title": "Attorney-General for India & Advocates-General",
        "code": "Art. 76 / 165",
        "cluster_id": "cluster_const_bodies",
        "authority_type": "Constitutional Text",
        "establishment_type": "Constitutionally Established (Articles 76 & 165)",
        "constitutional_basis": "Articles 76, 88, 165, 177",
        "summary": "Highest law officer of the Union (Article 76) and of each State (Article 165). Has the right of audience in all courts in India and the right to speak and take part in proceedings of both Houses of Parliament (Article 88) without the right to vote."
    },
    {
        "id": "inst_ncsc",
        "node_type": "Institutional",
        "subcategory": "Constitutional Commission",
        "title": "National Commissions for SCs, STs, and BCs",
        "code": "Art. 338–338B",
        "cluster_id": "cluster_const_bodies",
        "authority_type": "Constitutional Text",
        "establishment_type": "Constitutionally Established (Articles 338, 338A, 338B)",
        "constitutional_basis": "Articles 338, 338A (89th Amendment), 338B (102nd Amendment)",
        "summary": "Constitutional bodies vested with the powers of a civil court to investigate and monitor all matters relating to the constitutional and legal safeguards for Scheduled Castes (Article 338), Scheduled Tribes (Article 338A), and Socially and Educationally Backward Classes (Article 338B)."
    },
    {
        "id": "inst_state_govt",
        "node_type": "Institutional",
        "subcategory": "State Executive & Legislature",
        "title": "State Governments (Governor, CM, Council of Ministers, State Legislature)",
        "code": "Part VI",
        "cluster_id": "cluster_states",
        "authority_type": "Constitutional Text",
        "establishment_type": "Constitutionally Established (Articles 153–213)",
        "constitutional_basis": "Part VI (Articles 152–213)",
        "summary": "Mirroring the parliamentary architecture at the Union level, each State has a Governor (Article 153) acting on the aid and advice of a Council of Ministers headed by the Chief Minister (Articles 163–164), collectively responsible to the Legislative Assembly (Vidhan Sabha, Article 164(2))."
    },
    {
        "id": "inst_governor",
        "node_type": "Institutional",
        "subcategory": "State Head",
        "title": "Governor of a State",
        "code": "Art. 153",
        "cluster_id": "cluster_states",
        "authority_type": "Constitutional Text",
        "establishment_type": "Constitutionally Established (Article 153)",
        "constitutional_basis": "Articles 153–167, 200, 201, 213, 356",
        "summary": "Constitutional head of a State appointed by the President (Article 155) and dual link with the Union. Exercises executive power on the aid and advice of the State Council of Ministers (Article 163), grants or withholds assent or reserves State Bills for the President (Article 200), and promulgates State Ordinances (Article 213)."
    },
    {
        "id": "inst_state_legislature",
        "node_type": "Institutional",
        "subcategory": "State Legislature",
        "title": "State Legislature (Vidhan Sabha & Vidhan Parishad)",
        "code": "Art. 168",
        "cluster_id": "cluster_states",
        "authority_type": "Constitutional Text",
        "establishment_type": "Constitutionally Established (Article 168)",
        "constitutional_basis": "Part VI, Chapter III (Articles 168–212)",
        "summary": "Enacts laws on State List (61/66 subjects) and Concurrent List (52 subjects) under Article 246. Every State has a directly elected Legislative Assembly (Vidhan Sabha, Article 170), and six States also have an upper Legislative Council (Vidhan Parishad, Articles 169 & 171)."
    },
    {
        "id": "inst_panchayati_raj",
        "node_type": "Institutional",
        "subcategory": "Rural Local Self-Government",
        "title": "Panchayati Raj Institutions (Gram Sabha, Gram Panchayat, Panchayat Samiti, Zila Parishad)",
        "code": "Part IX",
        "cluster_id": "cluster_local_govt",
        "authority_type": "Constitutional Text",
        "establishment_type": "Constitutionally Established (Part IX, 73rd Amendment Act, 1992)",
        "constitutional_basis": "Part IX (Articles 243 to 243O) & Eleventh Schedule",
        "summary": "Three-tier rural local self-government anchored in the Gram Sabha (Article 243A), with village, intermediate, and district Panchayats (Article 243B), mandatory reservation for SCs, STs, and at least one-third women (Article 243D), State Finance Commission (Article 243I), State Election Commission (Article 243K), and 29 functional items in the Eleventh Schedule (Article 243G)."
    },
    {
        "id": "inst_municipalities",
        "node_type": "Institutional",
        "subcategory": "Urban Local Self-Government",
        "title": "Municipalities & Urban Local Bodies (Nagar Panchayat, Municipal Council, Municipal Corporation)",
        "code": "Part IXA",
        "cluster_id": "cluster_local_govt",
        "authority_type": "Constitutional Text",
        "establishment_type": "Constitutionally Established (Part IXA, 74th Amendment Act, 1992)",
        "constitutional_basis": "Part IXA (Articles 243P to 243ZG) & Twelfth Schedule",
        "summary": "Constitutionalized urban self-governance across transitional areas (Nagar Panchayats), smaller urban areas (Municipal Councils), and larger urban areas (Municipal Corporations), supported by Ward Committees, District & Metropolitan Planning Committees (Articles 243ZD–243ZE), and 18 urban functions in the Twelfth Schedule (Article 243W)."
    },
    {
        "id": "inst_citizens",
        "node_type": "Institutional",
        "subcategory": "Sovereign People",
        "title": "We, the People of India (Citizens & Voters)",
        "code": "Preamble / Art. 326",
        "cluster_id": "cluster_elections",
        "authority_type": "Constitutional Text",
        "establishment_type": "Ultimate Sovereign Source of Constitutional Authority",
        "constitutional_basis": "Preamble, Part II (Articles 5–11), Part III (Articles 12–35), Article 51A, Article 326",
        "summary": "The ultimate sovereign source of all political and constitutional authority in the Republic of India ('WE, THE PEOPLE OF INDIA... do HEREBY ADOPT, ENACT AND GIVE TO OURSELVES THIS CONSTITUTION'). Holders of Fundamental Rights (Part III), bearers of Fundamental Duties (Article 51A), and electors under Universal Adult Suffrage (Article 326)."
    },

    # --- ADMINISTRATIVE NODES ---
    {
        "id": "admin_ministries",
        "node_type": "Administrative",
        "subcategory": "Union Executive Machinery",
        "title": "Union Ministries & Departments (Allocation of Business Rules)",
        "code": "Art. 77(3)",
        "cluster_id": "cluster_administration",
        "authority_type": "Administrative Practice",
        "establishment_type": "Executive Arrangement under Article 77(3) (Government of India Allocation of Business Rules, 1961)",
        "constitutional_basis": "Articles 53, 73, 77(3)",
        "summary": "Under Article 77(3), the President makes rules for the more convenient transaction of the business of the Government of India and its allocation among Ministers. Policy formulation, subordinate legislation (rules/regulations), and central scheme execution take place through Union Ministries and Departments headed politically by a Minister and administratively by a Secretary to the Government of India."
    },
    {
        "id": "admin_cabinet_sec",
        "node_type": "Administrative",
        "subcategory": "Apex Executive Coordination",
        "title": "Cabinet Secretariat & Prime Minister's Office (PMO)",
        "code": "Art. 77(3)",
        "cluster_id": "cluster_administration",
        "authority_type": "Administrative Practice",
        "establishment_type": "Executive Arrangement under Article 77(3)",
        "constitutional_basis": "Article 77(3) & Transaction of Business Rules, 1961",
        "summary": "The nerve center of Union executive coordination. Headed by the Cabinet Secretary (ex-officio Chair of the Civil Services Board), the Cabinet Secretariat administers the Government of India (Transaction of Business) Rules, 1961, facilitates inter-ministerial coordination, and services Cabinet Committees."
    },
    {
        "id": "admin_civil_services",
        "node_type": "Administrative",
        "subcategory": "Permanent Executive",
        "title": "All-India Services (IAS, IPS, IFoS) & Central/State Civil Services",
        "code": "Art. 309–312",
        "cluster_id": "cluster_administration",
        "authority_type": "Constitutional Text",
        "establishment_type": "Constitutionally Recognized & Statutorily Regulated (Articles 309–312; All-India Services Act, 1951)",
        "constitutional_basis": "Part XIV, Chapter I (Articles 308–314)",
        "summary": "The permanent, politically neutral professional bureaucracy ('Steel Frame') that advises Ministers on policy and implements statutes across the Union and States. Recruited on merit by UPSC (Article 320) and protected against arbitrary dismissal or reduction in rank without a fair inquiry under Article 311(2)."
    },
    {
        "id": "admin_dm_collector",
        "node_type": "Administrative",
        "subcategory": "District Administration",
        "title": "District Magistrate / District Collector / Deputy Commissioner",
        "code": "District Admin",
        "cluster_id": "cluster_administration",
        "authority_type": "Statutory Law",
        "establishment_type": "Statutory & Executive Office (Land Revenue Codes, BNSS/CrPC, Disaster Management Act 2005)",
        "constitutional_basis": "Articles 154, 166, 243ZD, 309–312; Statutory Criminal & Revenue Codes",
        "summary": "The pivotal administrative officer connecting state and central government policies directly to citizens at the district level. Acts in three capacities: (1) District Collector (head of land revenue administration and recovery), (2) District Magistrate (maintenance of public order, executive magistracy under BNSS/CrPC), and (3) Deputy Commissioner / Chief Development Coordinator (disaster management, election conduct as District Election Officer under ECI, and welfare implementation)."
    },
    {
        "id": "admin_sdm",
        "node_type": "Administrative",
        "subcategory": "Sub-Divisional Administration",
        "title": "Sub-Divisional Magistrate (SDM) / Sub-Collector",
        "code": "Sub-Division",
        "cluster_id": "cluster_administration",
        "authority_type": "Statutory Law",
        "establishment_type": "Statutory Office (State Land Revenue Acts & BNSS/CrPC)",
        "constitutional_basis": "State Executive Power (Articles 154, 162) & Statutory Codes",
        "summary": "Heads a revenue and administrative sub-division within a district under the supervision of the District Magistrate. Exercises preventive executive magisterial powers, hears revenue appeals, serves as Returning Officer/Electoral Registration Officer during elections, and oversees public service delivery across blocks and tehsils."
    },
    {
        "id": "admin_tehsildar",
        "node_type": "Administrative",
        "subcategory": "Tehsil / Taluka Administration",
        "title": "Tehsildar / Mamlatdar & Block Development Officer (BDO)",
        "code": "Tehsil / Block",
        "cluster_id": "cluster_administration",
        "authority_type": "Statutory Law",
        "establishment_type": "Statutory & State Civil Service Office",
        "constitutional_basis": "State Land Revenue Codes & Part IX (Article 243G)",
        "summary": "Grassroots administrative interface with citizens: the Tehsildar (assisted by Naib Tehsildars, Kanungos, and Patwaris/Lekhpals) manages land records, mutations, domicile/caste/income certificates, and crop-loss relief, while the Block Development Officer (BDO) serves as executive officer to the Panchayat Samiti implementing rural development schemes."
    },
    {
        "id": "admin_regulatory_bodies",
        "node_type": "Administrative",
        "subcategory": "Statutory Regulators & Watchdogs",
        "title": "Statutory Regulatory Authorities & Accountability Bodies (RBI, SEBI, TRAI, Lokpal, CIC, NHRC)",
        "code": "Statutory Acts",
        "cluster_id": "cluster_administration",
        "authority_type": "Statutory Law",
        "establishment_type": "Created by Acts of Parliament (Article 246)",
        "constitutional_basis": "Enacted by Parliament under Article 246 & Seventh Schedule Union List",
        "summary": "Unlike constitutional bodies (ECI, CAG, UPSC), these specialized agencies are created by Parliamentary statutes to regulate complex economic sectors (RBI Act 1934, SEBI Act 1992, TRAI Act 1997, Competition Act 2002) or enforce transparency, human rights, and anti-corruption (Right to Information Act 2005 -> Central Information Commission; Protection of Human Rights Act 1993 -> NHRC; Lokpal and Lokayuktas Act 2013)."
    },

    # --- PHILOSOPHICAL NODES ---
    {
        "id": "phil_liberty",
        "node_type": "Philosophical",
        "subcategory": "Preamble Ideal & Core Value",
        "title": "Liberty (of Thought, Expression, Belief, Faith and Worship)",
        "code": "Preamble / Arts. 19–22, 25–28",
        "cluster_id": "cluster_philosophy",
        "authority_type": "Philosophical Analysis",
        "constitutional_basis": "Preamble, Articles 19, 20, 21, 22, 25–28",
        "summary": "Both negative liberty (freedom from arbitrary state restraint under Articles 19–22) and positive liberty (the conditions enabling self-realization and human dignity under Article 21 and Part IV). Dr. B.R. Ambedkar emphasized in his closing speech (25 Nov 1949) that liberty cannot be divorced from equality and fraternity.",
        "thinkers": ["Dr. B.R. Ambedkar", "Jawaharlal Nehru", "John Stuart Mill", "Isaiah Berlin", "John Locke"],
        "explanations": {
            "beginner": "Liberty means the freedom to think, speak, move freely, practice your faith, and live your life with dignity without unfair government interference.",
            "intermediate": "Proclaimed in the Preamble ('LIBERTY of thought, expression, belief, faith and worship') and made enforceable in Articles 19–22 and 25–28, Indian constitutional liberty balances individual freedom with reasonable social restrictions.",
            "advanced": "Through Maneka Gandhi (1978) and Puttaswamy (2017), the Supreme Court transformed liberty from compartmentalized textual freedoms (A.K. Gopalan, 1950) into an integrated 'Golden Triangle' (Articles 14, 19, 21) where any curtailment must satisfy legality, legitimate state aim, and proportionality.",
            "research": "Indian constitutionalism synthesizes liberal negative liberty (restraints on State power under Article 13) with republican and transformative positive liberty (enabling autonomy against both State and structural social domination)."
        }
    },
    {
        "id": "phil_equality",
        "node_type": "Philosophical",
        "subcategory": "Preamble Ideal & Core Value",
        "title": "Equality (of Status and of Opportunity)",
        "code": "Preamble / Arts. 14–18",
        "cluster_id": "cluster_philosophy",
        "authority_type": "Philosophical Analysis",
        "constitutional_basis": "Preamble, Articles 14, 15, 16, 17, 18, 38, 39",
        "summary": "Combines formal equality ('equality before the law' and 'equal protection of the laws' under Article 14) with substantive and compensatory equality (prohibition of discrimination and affirmative action under Articles 15(4)–(6) and 16(4)–(6), and abolition of untouchability under Article 17).",
        "thinkers": ["Dr. B.R. Ambedkar", "Jyotirao Phule", "Aristotle", "Ronald Dworkin", "Marc Galanter"],
        "explanations": {
            "beginner": "Equality means every person is treated equally by the law and has an equal chance to succeed, regardless of religion, race, caste, sex, or place of birth.",
            "intermediate": "Articles 14–18 guarantee formal equality before the law while explicitly empowering the State to make special provisions (reservations and welfare measures) for historically disadvantaged groups.",
            "advanced": "In E.P. Royappa (1974), Indra Sawhney (1992), and Navtej Singh Johar (2018), the Supreme Court established that equality is dynamic and antithetical to arbitrariness, and that affirmative action under Article 16(4) is not an exception to equality but an emphatic facet of substantive equality.",
            "research": "The Indian equality code rejects purely color-blind/caste-blind formal symmetry in favor of asymmetric, anti-subordination substantive equality aimed at dismantling graded social hierarchy."
        }
    },
    {
        "id": "phil_justice",
        "node_type": "Philosophical",
        "subcategory": "Preamble Ideal & Core Value",
        "title": "Justice (Social, Economic and Political)",
        "code": "Preamble / Art. 38",
        "cluster_id": "cluster_philosophy",
        "authority_type": "Philosophical Analysis",
        "constitutional_basis": "Preamble, Part III, Part IV (Articles 38, 39, 39A), Article 142",
        "summary": "Placed first among the ideals in the Preamble: Social Justice (eliminating caste/gender discrimination and untouchability), Economic Justice (preventing concentration of wealth under Article 39(b)–(c) and ensuring livelihood), and Political Justice (equal voice through universal adult franchise under Article 326).",
        "thinkers": ["Dr. B.R. Ambedkar", "Jawaharlal Nehru", "John Rawls", "Amartya Sen"]
    },
    {
        "id": "phil_fraternity",
        "node_type": "Philosophical",
        "subcategory": "Preamble Ideal & Core Value",
        "title": "Fraternity (Assuring the Dignity of the Individual and the Unity and Integrity of the Nation)",
        "code": "Preamble / Art. 51A(e)",
        "cluster_id": "cluster_philosophy",
        "authority_type": "Philosophical Analysis",
        "constitutional_basis": "Preamble, Articles 15(2), 17, 21, 51A(e)",
        "summary": "Defined by Dr. B.R. Ambedkar as 'a sense of common brotherhood of all Indians—if Indians being one people. It is the principle which gives unity and solidarity to social life.' Uniquely links individual human dignity with national unity and integrity.",
        "thinkers": ["Dr. B.R. Ambedkar", "Maitreyi / Upanishadic & Buddhist Sangha traditions", "French Republican tradition"]
    },
    {
        "id": "phil_const_morality",
        "node_type": "Philosophical",
        "subcategory": "Constitutional Philosophy",
        "title": "Constitutional Morality",
        "code": "CAD Vol. VII / Art. 14, 21",
        "cluster_id": "cluster_philosophy",
        "authority_type": "Philosophical Analysis",
        "constitutional_basis": "Constituent Assembly Debates (4 Nov 1948, Dr. B.R. Ambedkar); Preamble & Part III",
        "summary": "Introduced into Indian constitutional discourse by Dr. B.R. Ambedkar (adapting George Grote): a paramount reverence for the forms and spirit of the Constitution, self-restraint by institutions, and fidelity to pluralistic constitutional values even when they conflict with majoritarian or popular social morality (applied in Naz Foundation, Sabarimala, and Navtej Singh Johar, 2018).",
        "thinkers": ["Dr. B.R. Ambedkar", "George Grote", "Granville Austin"]
    },
    {
        "id": "phil_rule_of_law",
        "node_type": "Philosophical",
        "subcategory": "Foundational Doctrine",
        "title": "Rule of Law",
        "code": "Art. 14 / 21",
        "cluster_id": "cluster_philosophy",
        "authority_type": "Philosophical Analysis",
        "constitutional_basis": "Articles 13, 14, 21, 32, 226, 300A",
        "summary": "Supremacy of law over arbitrary power: no person or official is above the law, every executive action must have lawful authority, and independent courts enforce legal limits. Recognized as a core element of the Basic Structure of the Constitution (Indira Nehru Gandhi v. Raj Narain, 1975).",
        "thinkers": ["A.V. Dicey", "Upendra Baxi", "H.R. Khanna"]
    },
    {
        "id": "phil_dignity",
        "node_type": "Philosophical",
        "subcategory": "Core Constitutional Value",
        "title": "Human Dignity & Individual Autonomy",
        "code": "Preamble / Art. 21",
        "cluster_id": "cluster_philosophy",
        "authority_type": "Philosophical Analysis",
        "constitutional_basis": "Preamble ('dignity of the individual'), Articles 17, 21, 23",
        "summary": "The moral cornerstone of Part III and the Preamble. In Maneka Gandhi (1978), Francis Coralie Mullin (1981), and Justice K.S. Puttaswamy (2017), the Supreme Court held that the 'right to life' under Article 21 is not mere animal existence but the right to live with human dignity, encompassing bodily integrity, decisional autonomy, and informational privacy.",
        "thinkers": ["Immanuel Kant", "Dr. B.R. Ambedkar", "Martha Nussbaum"]
    },
    {
        "id": "phil_privacy",
        "node_type": "Philosophical",
        "subcategory": "Fundamental Right & Value",
        "title": "Right to Privacy",
        "code": "Art. 21 (Puttaswamy 2017)",
        "cluster_id": "cluster_rights",
        "authority_type": "Judicial Interpretation",
        "constitutional_basis": "Articles 14, 19, 21 (Part III)",
        "summary": "Unanimously affirmed by a 9-Judge Constitution Bench in Justice K.S. Puttaswamy (Retd.) v. Union of India (2017) as an intrinsic part of the right to life and personal liberty under Article 21 and across the freedoms guaranteed by Part III. Encompasses bodily integrity, spatial privacy, informational self-determination, and decisional autonomy. Any state infringement (such as surveillance or data collection) must pass the four-prong Proportionality Test: (1) legality (existence of a law), (2) legitimate state aim (e.g., national security), (3) rational nexus & necessity (least restrictive measure), and (4) procedural guarantees against abuse.",
        "thinkers": ["Justice D.Y. Chandrachud", "Justice J.S. Khehar", "Justice R.F. Nariman", "Samuel Warren & Louis Brandeis"]
    },
    {
        "id": "phil_secularism",
        "node_type": "Philosophical",
        "subcategory": "Preamble Ideal & Basic Structure",
        "title": "Indian Secularism (Principled Distance & Sarva Dharma Sambhava)",
        "code": "Preamble / Arts. 25–28",
        "cluster_id": "cluster_philosophy",
        "authority_type": "Philosophical Analysis",
        "constitutional_basis": "Preamble, Articles 14, 15, 16, 25–30, 51A(e)",
        "summary": "Unlike strict Western church-state separation, Indian constitutional secularism combines equal freedom of conscience and religion for all (Article 25) and non-establishment (no state religion or religious tax under Article 27) with 'principled distance' that allows the State to reform social evils within religion (Article 25(2)(b)). Declared part of the Basic Structure in S.R. Bommai v. Union of India (1994).",
        "thinkers": ["Dr. S. Radhakrishnan", "Jawaharlal Nehru", "Rajeev Bhargava"]
    },
    {
        "id": "phil_federalism",
        "node_type": "Philosophical",
        "subcategory": "Constitutional Principle",
        "title": "Cooperative & Asymmetric Federalism",
        "code": "Art. 1 / Part XI",
        "cluster_id": "cluster_federalism",
        "authority_type": "Philosophical Analysis",
        "constitutional_basis": "Article 1 ('Union of States'), Parts XI & XII, Seventh Schedule, Articles 263, 279A, 280, 371–371J",
        "summary": "Described by Granville Austin as 'Cooperative Federalism' and by K.C. Wheare as 'quasi-federal': a constitutional division of sovereignty between the Union and States with a strong unifying framework, intergovernmental cooperation (Finance Commission, GST Council, Inter-State Council), and asymmetric special accommodations (Fifth & Sixth Schedules, Articles 371–371J). Declared part of the Basic Structure in S.R. Bommai (1994).",
        "thinkers": ["Dr. B.R. Ambedkar", "Sardar Vallabhbhai Patel", "Granville Austin", "K.C. Wheare"]
    },
    {
        "id": "phil_sep_powers",
        "node_type": "Philosophical",
        "subcategory": "Constitutional Principle",
        "title": "Separation of Powers & Checks and Balances",
        "code": "Art. 50 / Part V",
        "cluster_id": "cluster_philosophy",
        "authority_type": "Philosophical Analysis",
        "constitutional_basis": "Articles 50, 53, 79, 121, 122, 124, 211, 212, 245, 361",
        "summary": "Functional differentiation with institutional checks and balances rather than rigid water-tight separation: the Executive is drawn from and accountable to the Legislature (Article 75(3)), the Judiciary is strictly separated from the Executive (Article 50) and insulated from parliamentary discussion of judicial conduct (Article 121), while exercising judicial review over both.",
        "thinkers": ["Montesquieu", "James Madison", "Chief Justice B.K. Mukherjea (Ram Jawaya Kapur, 1955)"]
    },

    # --- JUDICIAL NODES: LANDMARK JUDGMENTS & DOCTRINES ---
    {
        "id": "doc_basic_structure",
        "node_type": "Judicial",
        "subcategory": "Constitutional Doctrine",
        "title": "Basic Structure Doctrine",
        "code": "Art. 368 Limit",
        "cluster_id": "cluster_amendments",
        "authority_type": "Judicial Interpretation",
        "constitutional_basis": "Article 368 interpreted in Kesavananda Bharati (1973) & Minerva Mills (1980)",
        "summary": "Propounded by a 13-Judge Bench of the Supreme Court (7:6 majority) in Kesavananda Bharati v. State of Kerala (1973): while Parliament has wide power under Article 368 to amend any part of the Constitution (including Fundamental Rights), the word 'amend' does not include the power to destroy, abrogate, or alter the 'basic structure or framework' of the Constitution (such as supremacy of the Constitution, democracy, secularism, rule of law, federalism, judicial review, separation of powers, and harmony between Parts III and IV)."
    },
    {
        "id": "doc_golden_triangle",
        "node_type": "Judicial",
        "subcategory": "Constitutional Doctrine",
        "title": "Golden Triangle of the Constitution (Articles 14, 19, and 21)",
        "code": "Arts. 14, 19, 21",
        "cluster_id": "cluster_rights",
        "authority_type": "Judicial Interpretation",
        "constitutional_basis": "Articles 14, 19, and 21 (Part III)",
        "summary": "Articulated in Maneka Gandhi v. Union of India (1978) and immortalized in Minerva Mills (1980) ('Three articles of our Constitution, and only three, stand between the heaven of freedom into which Tagore wanted his country to awake and the abyss of unrestrained power'). Holds that Articles 14, 19, and 21 are not mutually exclusive islands (overruling A.K. Gopalan, 1950), and any law depriving personal liberty under Article 21 must also pass the tests of non-arbitrariness under Article 14 and reasonableness under Article 19."
    },
    {
        "id": "doc_harmonious_const",
        "node_type": "Judicial",
        "subcategory": "Constitutional Doctrine",
        "title": "Doctrine of Harmonious Construction (Fundamental Rights & DPSPs)",
        "code": "Part III & Part IV",
        "cluster_id": "cluster_dpsp",
        "authority_type": "Judicial Interpretation",
        "constitutional_basis": "Parts III & IV (Articles 14, 19, 21, 31C, 37, 38, 39)",
        "summary": "Held in Kerala Education Bill (1957), Kesavananda Bharati (1973), and Minerva Mills v. Union of India (1980): Fundamental Rights (Part III) and Directive Principles of State Policy (Part IV) are not antagonists but the 'conscience of the Constitution'—like two wheels of a chariot. Neither can destroy the other; courts must interpret them harmoniously so social-welfare goals are achieved through constitutional means."
    },
    {
        "id": "doc_proportionality",
        "node_type": "Judicial",
        "subcategory": "Legal Test",
        "title": "Proportionality Test & Non-Arbitrariness Test",
        "code": "Arts. 14, 19, 21",
        "cluster_id": "cluster_rights",
        "authority_type": "Judicial Interpretation",
        "constitutional_basis": "Articles 14, 19, 21 (Modern Dental College 2016; Puttaswamy 2017)",
        "summary": "Four-part constitutional standard for testing limitations on Fundamental Rights: (1) the measure must be designated for a proper/legitimate purpose, (2) the measures undertaken must be rationally connected to fulfilling that purpose, (3) there must be no alternative less invasive measure (necessity), and (4) there must be a proper balance between the importance of achieving the aim and the social importance of preventing the limitation on the constitutional right."
    },
    {
        "id": "doc_pith_substance",
        "node_type": "Judicial",
        "subcategory": "Federalism Doctrine",
        "title": "Doctrines of Pith and Substance, Colourable Legislation & Repugnancy",
        "code": "Arts. 245, 246, 254",
        "cluster_id": "cluster_federalism",
        "authority_type": "Judicial Interpretation",
        "constitutional_basis": "Articles 245, 246, 254 & Seventh Schedule",
        "summary": "Judicial principles governing federal legislative competence: (1) Pith and Substance (State of Bombay v. F.N. Balsara, 1951): if the true nature and character of a law falls within a legislature's allotted list, incidental encroachment on another list does not invalidate it; (2) Colourable Legislation (K.C. Gajapati Narayan Deo, 1953): 'what cannot be done directly cannot be done indirectly'; (3) Repugnancy (Article 254): on Concurrent List subjects, Union law prevails over conflicting State law unless the State law received Presidential assent under Article 254(2)."
    },
    {
        "id": "judg_kesavananda",
        "node_type": "Judicial",
        "subcategory": "Landmark Judgment (13-Judge Bench)",
        "title": "Kesavananda Bharati v. State of Kerala (1973)",
        "code": "(1973) 4 SCC 225",
        "cluster_id": "cluster_amendments",
        "authority_type": "Judicial Interpretation",
        "constitutional_basis": "Article 368, Preamble, Part III (Articles 14, 19, 25, 26, 31C)",
        "summary": "Heard by the largest bench in Supreme Court history (13 Judges) for 68 days. Background: Challenge to Kerala Land Reforms Acts and the 24th, 25th, and 29th Constitutional Amendments. Core Constitutional Question: Is Parliament's power to amend the Constitution under Article 368 unlimited? Holding (7:6 majority): Overruled Golaknath (1967) to hold that Parliament can amend any provision of the Constitution including Fundamental Rights, BUT established the Basic Structure Doctrine—Parliament cannot use Article 368 to alter or destroy the basic structure or essential features of the Constitution. Also declared the Preamble an integral part of the Constitution."
    },
    {
        "id": "judg_maneka",
        "node_type": "Judicial",
        "subcategory": "Landmark Judgment (7-Judge Bench)",
        "title": "Maneka Gandhi v. Union of India (1978)",
        "code": "(1978) 1 SCC 248",
        "cluster_id": "cluster_rights",
        "authority_type": "Judicial Interpretation",
        "constitutional_basis": "Articles 14, 19, and 21",
        "summary": "Background: Impounding of petitioner's passport under Section 10(3)(c) of the Passports Act, 1967 without giving a pre-decisional hearing or reasons. Core Constitutional Question: Does 'procedure established by law' in Article 21 mean any arbitrary statutory procedure (as held in A.K. Gopalan, 1950)? Holding: Overruled Gopalan's silo theory; established the Golden Triangle of Articles 14, 19, and 21. Held that 'procedure established by law' under Article 21 must be 'right and just and fair, and not arbitrary, fanciful or oppressive', Infusing substantive due process and natural justice into Article 21."
    },
    {
        "id": "judg_minerva",
        "node_type": "Judicial",
        "subcategory": "Landmark Judgment (5-Judge Bench)",
        "title": "Minerva Mills Ltd. v. Union of India (1980)",
        "code": "(1980) 3 SCC 625",
        "cluster_id": "cluster_dpsp",
        "authority_type": "Judicial Interpretation",
        "constitutional_basis": "Articles 14, 19, 21, 31C, 368(4)–(5)",
        "summary": "Background: Challenge to Sections 4 and 55 of the 42nd Amendment Act, 1976, which gave blanket primacy to all Directive Principles over Articles 14 and 19 and declared that no constitutional amendment could be questioned in any court. Holding: Struck down both provisions as unconstitutional violations of the Basic Structure. Held that limited amending power and judicial review are themselves essential features of the Basic Structure, and that harmony and balance between Fundamental Rights (Part III) and Directive Principles (Part IV) is a bedrock feature of the Constitution."
    },
    {
        "id": "judg_puttaswamy",
        "node_type": "Judicial",
        "subcategory": "Landmark Judgment (9-Judge Bench)",
        "title": "Justice K.S. Puttaswamy (Retd.) v. Union of India (2017)",
        "code": "(2017) 10 SCC 1",
        "cluster_id": "cluster_rights",
        "authority_type": "Judicial Interpretation",
        "constitutional_basis": "Preamble, Articles 14, 19, 21 (Part III)",
        "summary": "Background: Reference arising out of challenges to the biometric Aadhaar scheme when the Union argued (citing M.P. Sharma 1954 and Kharak Singh 1962) that the Constitution does not guarantee a fundamental right to privacy. Holding (Unanimous 9:0): Overruled M.P. Sharma and Kharak Singh; declared that the Right to Privacy is an inalienable natural right and an intrinsic part of the right to life and personal liberty under Article 21 and Part III, grounded in human dignity and individual autonomy. Established the Proportionality Test for evaluating state surveillance, biometric systems, and data protection."
    },
    {
        "id": "judg_bommai",
        "node_type": "Judicial",
        "subcategory": "Landmark Judgment (9-Judge Bench)",
        "title": "S.R. Bommai v. Union of India (1994)",
        "code": "(1994) 3 SCC 1",
        "cluster_id": "cluster_federalism",
        "authority_type": "Judicial Interpretation",
        "constitutional_basis": "Article 356, Federalism, Secularism",
        "summary": "Background: Arbitrary dismissal of elected State Governments using President's Rule under Article 356. Holding: Federalism and Secularism are integral parts of the Basic Structure. The President's proclamation under Article 356 is not immune from judicial review; courts can examine whether the proclamation was based on relevant material or mala fide. Whether a Chief Minister enjoys a majority must be tested исключительно on the floor of the Vidhan Sabha (Floor Test), not in the Governor's subjective chamber."
    },
    {
        "id": "judg_golaknath",
        "node_type": "Judicial",
        "subcategory": "Landmark Judgment (11-Judge Bench)",
        "title": "I.C. Golaknath v. State of Punjab (1967)",
        "code": "AIR 1967 SC 1643",
        "cluster_id": "cluster_amendments",
        "authority_type": "Judicial Interpretation",
        "constitutional_basis": "Articles 13(2) & 368",
        "summary": "Held by a 6:5 majority (applying prospective overruling) that a Constitutional Amendment is 'law' within the meaning of Article 13(2) and therefore Parliament could not abridge or take away Fundamental Rights—prompting the enactment of the 24th Amendment (1971) and setting the stage for Kesavananda Bharati (1973)."
    },
    {
        "id": "judg_gopalan",
        "node_type": "Judicial",
        "subcategory": "Historical Landmark Judgment (6-Judge Bench)",
        "title": "A.K. Gopalan v. State of Madras (1950)",
        "code": "AIR 1950 SC 27",
        "cluster_id": "cluster_rights",
        "authority_type": "Judicial Interpretation",
        "constitutional_basis": "Articles 19, 21, 22",
        "summary": "The Supreme Court's first major constitutional decision on preventive detention. The majority adopted a positivist, compartmentalized reading of Fundamental Rights (holding that Article 21 only required a procedure enacted by a valid statute, not natural justice or Article 19 reasonableness), while Justice Fazl Ali's famous dissent foreshadowed the integrated Golden Triangle adopted 28 years later in Maneka Gandhi (1978)."
    },
    {
        "id": "judg_indra_sawhney",
        "node_type": "Judicial",
        "subcategory": "Landmark Judgment (9-Judge Bench)",
        "title": "Indra Sawhney v. Union of India (Mandal Commission Case, 1992)",
        "code": "1992 Supp (3) SCC 217",
        "cluster_id": "cluster_rights",
        "authority_type": "Judicial Interpretation",
        "constitutional_basis": "Articles 14, 16(1), 16(4), 340",
        "summary": "Upheld 27% reservation for Socially and Educationally Backward Classes (OBCs) in central government employment under Article 16(4); established the 'Creamy Layer' exclusion rule so benefits reach the truly needy, and articulated the general 50% ceiling rule on vertical reservations to balance formal and substantive equality."
    },
    {
        "id": "judg_vishaka",
        "node_type": "Judicial",
        "subcategory": "Landmark Judgment",
        "title": "Vishaka v. State of Rajasthan (1997)",
        "code": "(1997) 6 SCC 241",
        "cluster_id": "cluster_rights",
        "authority_type": "Judicial Interpretation",
        "constitutional_basis": "Articles 14, 15, 19(1)(g), 21, 32, 51(c), 141",
        "summary": "Held that workplace sexual harassment violates a woman's fundamental rights to gender equality (Articles 14, 15), right to practice any profession (Article 19(1)(g)), and right to life with dignity (Article 21). Invoking Articles 32 and 141 alongside CEDAW and Article 51(c), laid down binding Vishaka Guidelines until Parliament enacted the POSH Act, 2013."
    },
    {
        "id": "judg_coelho",
        "node_type": "Judicial",
        "subcategory": "Landmark Judgment (9-Judge Bench)",
        "title": "I.R. Coelho v. State of Tamil Nadu (Ninth Schedule Case, 2007)",
        "code": "(2007) 2 SCC 1",
        "cluster_id": "cluster_amendments",
        "authority_type": "Judicial Interpretation",
        "constitutional_basis": "Article 31B, Ninth Schedule, Basic Structure (Articles 14, 19, 21, 32)",
        "summary": "Unanimously held that any law placed in the Ninth Schedule after 24 April 1973 (the date of the Kesavananda Bharati judgment) is not immune from judicial scrutiny if it damages or destroys the Basic Structure as reflected in the Golden Triangle of Articles 14, 19, and 21."
    },
    {
        "id": "judg_njac",
        "node_type": "Judicial",
        "subcategory": "Landmark Judgment (5-Judge Bench)",
        "title": "Supreme Court Advocates-on-Record Assn. v. Union of India (NJAC Case, 2015)",
        "code": "(2016) 5 SCC 1",
        "cluster_id": "cluster_judiciary",
        "authority_type": "Judicial Interpretation",
        "constitutional_basis": "Articles 50, 124, 124A–124C, 217, 368",
        "summary": "Struck down the 99th Constitutional Amendment Act, 2014 and the National Judicial Appointments Commission (NJAC) Act, 2014 by a 4:1 majority, holding that judicial primacy in the appointment of constitutional judges is essential to the independence of the judiciary, which is an unamendable facet of the Basic Structure."
    },
    {
        "id": "judg_kihoto",
        "node_type": "Judicial",
        "subcategory": "Landmark Judgment (5-Judge Bench)",
        "title": "Kihoto Hollohon v. Zachilhu (Anti-Defection Case, 1992)",
        "code": "1992 Supp (2) SCC 651",
        "cluster_id": "cluster_parliament",
        "authority_type": "Judicial Interpretation",
        "constitutional_basis": "Tenth Schedule (52nd Amendment), Articles 102(2), 191(2), 136, 226",
        "summary": "Upheld the constitutional validity of the Tenth Schedule (Anti-Defection Law) while striking down Paragraph 7 (which had barred judicial review), holding that the Speaker acts as a tribunal when deciding disqualification petitions and the Speaker's final decision is subject to judicial review under Articles 136, 226, and 227."
    },
    {
        "id": "judg_navtej",
        "node_type": "Judicial",
        "subcategory": "Landmark Judgment (5-Judge Bench)",
        "title": "Navtej Singh Johar v. Union of India (2018)",
        "code": "(2018) 10 SCC 1",
        "cluster_id": "cluster_rights",
        "authority_type": "Judicial Interpretation",
        "constitutional_basis": "Articles 14, 15, 19, 21 & Constitutional Morality",
        "summary": "Unanimously read down Section 377 of the Indian Penal Code to decriminalize consensual adult same-sex relations, grounding its holding in Constitutional Morality, Transformative Constitutionalism, human dignity, privacy (Puttaswamy), and non-discrimination under Articles 14, 15, 19, and 21."
    },
    {
        "id": "judg_shreya_singhal",
        "node_type": "Judicial",
        "subcategory": "Landmark Judgment",
        "title": "Shreya Singhal v. Union of India (2015)",
        "code": "(2015) 5 SCC 1",
        "cluster_id": "cluster_rights",
        "authority_type": "Judicial Interpretation",
        "constitutional_basis": "Article 19(1)(a) & Article 19(2)",
        "summary": "Struck down Section 66A of the Information Technology Act, 2000 in its entirety as an unconstitutional, vague, and overbroad restriction on the freedom of speech and expression online under Article 19(1)(a), distinguishing 'discussion' and 'advocacy' from actual 'incitement' to imminent lawless action."
    },
    {
        "id": "judg_olga_tellis",
        "node_type": "Judicial",
        "subcategory": "Landmark Judgment (5-Judge Bench)",
        "title": "Olga Tellis v. Bombay Municipal Corporation (1985)",
        "code": "(1985) 3 SCC 545",
        "cluster_id": "cluster_rights",
        "authority_type": "Judicial Interpretation",
        "constitutional_basis": "Articles 21, 39(a), 41",
        "summary": "Reading Article 21 in light of Directive Principles (Articles 39(a) and 41), held that the Right to Life includes the Right to Livelihood ('no person can live without the means of living, that is, the means of livelihood') and required fair notice and hearing before eviction of pavement and slum dwellers."
    },
    {
        "id": "judg_dk_basu",
        "node_type": "Judicial",
        "subcategory": "Landmark Judgment",
        "title": "D.K. Basu v. State of West Bengal (1997)",
        "code": "(1997) 1 SCC 416",
        "cluster_id": "cluster_rights",
        "authority_type": "Judicial Interpretation",
        "constitutional_basis": "Articles 21 & 22(1)–(2)",
        "summary": "Established mandatory nationwide procedural safeguards (arrest memo, informing family/friend, medical inspection, access to lawyer) against custodial torture and arbitrary arrest, later codified into criminal procedure statute."
    },
    {
        "id": "judg_art370",
        "node_type": "Judicial",
        "subcategory": "Landmark Judgment (5-Judge Bench)",
        "title": "In Re: Article 370 of the Constitution (2023)",
        "code": "2023 INSC 1058",
        "cluster_id": "cluster_federalism",
        "authority_type": "Judicial Interpretation",
        "constitutional_basis": "Articles 1, 3, 356, 370, Appendix II & III (C.O. 272 & C.O. 273 of 2019)",
        "summary": "Unanimously upheld the constitutional validity of Presidential Order C.O. 273 of 6 August 2019 declaring that all provisions of the Constitution of India apply to Jammu and Kashmir, holding that Article 370 was a temporary and transitional provision designed for gradual constitutional integration under Article 1."
    },

    # --- HISTORICAL NODES ---
    {
        "id": "hist_goi_1935",
        "node_type": "Historical",
        "subcategory": "Pre-1950 Constitutional Antecedent",
        "title": "Government of India Act, 1935",
        "code": "1935 Act (Repealed by Art. 395)",
        "cluster_id": "cluster_history",
        "authority_type": "Historical Evidence",
        "constitutional_basis": "Article 395 (Repeals)",
        "summary": "Provided much of the administrative and structural scaffolding adopted and democratized by the Constituent Assembly: three-fold legislative lists (Federal, Provincial, Concurrent -> Seventh Schedule), Office of the Governor, Federal Court (-> Supreme Court), Public Service Commissions, and emergency provisions—transformed from colonial control into sovereign democratic self-rule."
    },
    {
        "id": "hist_const_assembly",
        "node_type": "Historical",
        "subcategory": "Founding Institution",
        "title": "Constituent Assembly of India & Debates (1946–1949)",
        "code": "9 Dec 1946 – 26 Nov 1949",
        "cluster_id": "cluster_history",
        "authority_type": "Historical Evidence",
        "constitutional_basis": "Preamble ('IN OUR CONSTITUENT ASSEMBLY this twenty-sixth day of November, 1949')",
        "summary": "Presided over by Dr. Rajendra Prasad (after Dr. Sachchidananda Sinha as temporary Chairman), the Constituent Assembly met for 165 days across 11 sessions over 2 years, 11 months, and 18 days, debating 7,635 tabled amendments (moving and disposing of 2,473) recorded in the 12 volumes of the Constituent Assembly Debates (CAD)."
    },
    {
        "id": "hist_obj_resolution",
        "node_type": "Historical",
        "subcategory": "Foundational Charter",
        "title": "Objectives Resolution (Moved 13 Dec 1946, Adopted 22 Jan 1947)",
        "code": "13 Dec 1946",
        "cluster_id": "cluster_history",
        "authority_type": "Historical Evidence",
        "constitutional_basis": "Precursor to the Preamble",
        "summary": "Moved by Pandit Jawaharlal Nehru on 13 December 1946 and unanimously adopted on 22 January 1947. Declared India an Independent Sovereign Republic deriving all power and authority from the people, and guaranteed justice (social, economic, political), equality, freedom of thought/expression/faith, and safeguards for minorities and backward classes—forming the direct blueprint of the Preamble."
    },
    {
        "id": "hist_drafting_comm",
        "node_type": "Historical",
        "subcategory": "Founding Committee",
        "title": "Drafting Committee (Chaired by Dr. B.R. Ambedkar) & Constitutional Adviser B.N. Rau",
        "code": "29 Aug 1947",
        "cluster_id": "cluster_history",
        "authority_type": "Historical Evidence",
        "constitutional_basis": "Constituent Assembly Resolution of 29 August 1947",
        "summary": "Appointed on 29 August 1947 with Dr. B.R. Ambedkar as Chairman and Alladi Krishnaswami Ayyar, N. Gopalaswami Ayyangar, Dr. K.M. Munshi, Syed Mohammad Saadulla, N. Madhava Rau (replacing B.L. Mitter), and T.T. Krishnamachari (replacing D.P. Khaitan) as members, building upon the initial draft prepared by Constitutional Adviser Sir B.N. Rau."
    },
    {
        "id": "hist_adoption_1949",
        "node_type": "Historical",
        "subcategory": "Constitutional Milestone",
        "title": "Adoption (26 Nov 1949) & Commencement of the Constitution (26 Jan 1950)",
        "code": "Art. 394",
        "cluster_id": "cluster_history",
        "authority_type": "Constitutional Text",
        "constitutional_basis": "Preamble & Article 394",
        "summary": "Adopted and enacted on 26 November 1949 (celebrated as Samvidhan Divas / Constitution Day), when citizenship, elections, and provisional Parliament provisions took immediate effect under Article 394; the complete Constitution came into force on 26 January 1950 (commemorating the 1930 Purna Swaraj declaration), establishing the Republic of India."
    },

    # --- CONSTITUTIONAL AMENDMENT NODES ---
    {
        "id": "amend_1",
        "node_type": "Constitutional",
        "subcategory": "Constitutional Amendment",
        "title": "First Constitutional Amendment Act, 1951",
        "code": "1st Amendment (1951)",
        "cluster_id": "cluster_amendments",
        "authority_type": "Constitutional Text",
        "constitutional_basis": "Amended Arts. 15, 19, 85, 87, 174, 176, 341, 342, 372, 376; Inserted Arts. 15(4), 31A, 31B & Ninth Schedule",
        "summary": "Enacted by the Provisional Parliament to protect agrarian land reform laws (Articles 31A, 31B, Ninth Schedule), enable special provisions for socially and educationally backward classes (Article 15(4) after Champakam Dorairajan), and qualify restrictions on free speech with the word 'reasonable' in Article 19(2)."
    },
    {
        "id": "amend_42",
        "node_type": "Constitutional",
        "subcategory": "Constitutional Amendment",
        "title": "Forty-Second Constitutional Amendment Act, 1976",
        "code": "42nd Amendment (1976)",
        "cluster_id": "cluster_amendments",
        "authority_type": "Constitutional Text",
        "constitutional_basis": "Amended Preamble, Parts IV, V, VI, XI, XIV, XX; Inserted Part IVA (Art. 51A), Part XIVA (Arts. 323A–323B), Arts. 39A, 43A, 48A",
        "summary": "Enacted during the 1975–77 Internal Emergency: added 'SOCIALIST', 'SECULAR', and 'and integrity' to the Preamble; inserted Part IVA (Fundamental Duties, Article 51A) on Swaran Singh Committee recommendations; added Directive Principles on free legal aid (39A), workers' participation (43A), and environment (48A); moved Education and Forests to the Concurrent List; and sought to curtail judicial review (later struck down in Minerva Mills 1980 and undone by the 44th Amendment 1978)."
    },
    {
        "id": "amend_44",
        "node_type": "Constitutional",
        "subcategory": "Constitutional Amendment",
        "title": "Forty-Fourth Constitutional Amendment Act, 1978",
        "code": "44th Amendment (1978)",
        "cluster_id": "cluster_amendments",
        "authority_type": "Constitutional Text",
        "constitutional_basis": "Amended Arts. 19, 22, 74, 352, 356, 358, 359; Inserted Art. 300A",
        "summary": "Restored civil liberties and institutional safeguards after the Emergency: replaced 'internal disturbance' with 'armed rebellion' in Article 352; required written Cabinet communication for National Emergency (Article 352(3)); made Articles 20 and 21 non-suspendable even during an Emergency (Article 359); allowed the President to return Cabinet advice once for reconsideration (Article 74(1) proviso); and converted Right to Property from a Fundamental Right (Art. 19(1)(f)/31) into a constitutional right under Article 300A."
    },
    {
        "id": "amend_73_74",
        "node_type": "Constitutional",
        "subcategory": "Constitutional Amendment",
        "title": "73rd & 74th Constitutional Amendment Acts, 1992 (Panchayats & Municipalities)",
        "code": "73rd & 74th Amendments (1992)",
        "cluster_id": "cluster_local_govt",
        "authority_type": "Constitutional Text",
        "constitutional_basis": "Inserted Part IX (Arts. 243–243O, 11th Schedule) & Part IXA (Arts. 243P–243ZG, 12th Schedule)",
        "summary": "Constitutionalized local self-government across rural India (Part IX) and urban India (Part IXA), mandating regular 5-year elections via State Election Commissions, State Finance Commissions, and at least one-third reservation for women at the grassroots level."
    },
    {
        "id": "amend_86",
        "node_type": "Constitutional",
        "subcategory": "Constitutional Amendment",
        "title": "Eighty-Sixth Constitutional Amendment Act, 2002 (Right to Education)",
        "code": "86th Amendment (2002)",
        "cluster_id": "cluster_rights",
        "authority_type": "Constitutional Text",
        "constitutional_basis": "Inserted Art. 21A; Substituted Art. 45; Added Art. 51A(k)",
        "summary": "Elevated free and compulsory education for children aged 6 to 14 years to an enforceable Fundamental Right under Article 21A (implemented via the Right of Children to Free and Compulsory Education Act, 2009), reoriented Article 45 to early childhood care (below age 6), and added parental duty under Article 51A(k)."
    },
    {
        "id": "amend_101",
        "node_type": "Constitutional",
        "subcategory": "Constitutional Amendment",
        "title": "One Hundred and First Constitutional Amendment Act, 2016 (Goods and Services Tax)",
        "code": "101st Amendment (2016)",
        "cluster_id": "cluster_federalism",
        "authority_type": "Constitutional Text",
        "constitutional_basis": "Inserted Arts. 246A, 269A, 279A; Amended Art. 270, Sixth & Seventh Schedules",
        "summary": "Re-engineered India's fiscal federalism by introducing simultaneous Union and State legislative competence to levy Goods and Services Tax (Article 246A), integrated inter-state GST sharing (Article 269A), and the federal GST Council (Article 279A)."
    },
    {
        "id": "amend_106",
        "node_type": "Constitutional",
        "subcategory": "Constitutional Amendment",
        "title": "One Hundred and Sixth Constitutional Amendment Act, 2023 (Nari Shakti Vandan Adhiniyam)",
        "code": "106th Amendment (2023)",
        "cluster_id": "cluster_amendments",
        "authority_type": "Constitutional Text",
        "constitutional_basis": "Amended Art. 239AA; Inserted Arts. 330A, 332A, 334A",
        "summary": "The latest amendment incorporated in the 2026 edition of the Constitution: reserves one-third (33%) of all seats for women in the Lok Sabha (Article 330A), State Legislative Assemblies (Article 332A), and the Legislative Assembly of the NCT of Delhi (Article 239AA(2)(ba)), with commencement and sunset governed by Article 334A."
    },

    # --- PROCESS NODES & STATUTORY ANCHORS ---
    {
        "id": "proc_ordinary_bill",
        "node_type": "Process",
        "subcategory": "Legislative Process",
        "title": "How an Ordinary Bill Becomes an Act of Parliament",
        "code": "Arts. 107, 108, 111",
        "cluster_id": "cluster_processes",
        "authority_type": "Constitutional Text",
        "constitutional_basis": "Articles 107, 108, 111 & Parliamentary Rules",
        "summary": "May originate in either Lok Sabha or Rajya Sabha (Article 107(1)) -> First Reading (Introduction & Gazette publication) -> Reference to Departmentally Related Standing Committee -> Second Reading (General discussion & clause-by-clause voting) -> Third Reading (Passing) -> Transmission to Second House -> Joint Sitting under Article 108 in case of deadlock -> Presidential Assent under Article 111 (Assent, Withhold, or Return via Suspensive Veto) -> Gazette Notification -> Subordinate Rules & Administrative Enforcement."
    },
    {
        "id": "proc_money_bill",
        "node_type": "Process",
        "subcategory": "Financial Legislative Process",
        "title": "Money Bill Procedure & Union Budget (Annual Financial Statement)",
        "code": "Arts. 109, 110, 112–117",
        "cluster_id": "cluster_processes",
        "authority_type": "Constitutional Text",
        "constitutional_basis": "Articles 109, 110, 111, 112–117",
        "summary": "Defined strictly in Article 110(1) (taxation, Consolidated Fund borrowing/appropriation) and certified by the Speaker of the Lok Sabha under Article 110(3). Can be introduced ONLY in the Lok Sabha and ONLY on the recommendation of the President (Article 109(1), 117(1)). Rajya Sabha cannot amend or reject a Money Bill; it must return it within 14 days with or without recommendations, which Lok Sabha may accept or reject (Article 109(2)). No Joint Sitting is permissible."
    },
    {
        "id": "proc_const_amend_bill",
        "node_type": "Process",
        "subcategory": "Constituent Process",
        "title": "Constitutional Amendment Process (Article 368)",
        "code": "Art. 368",
        "cluster_id": "cluster_amendments",
        "authority_type": "Constitutional Text",
        "constitutional_basis": "Part XX (Article 368)",
        "summary": "Initiated by introducing a Bill in either House of Parliament (never in a State Legislature; does not require prior Presidential recommendation). Must be passed in EACH House separately (no Joint Sitting allowed) by a Special Majority: a majority of the total membership of that House AND a majority of not less than two-thirds of the members of that House present and voting. If the amendment seeks to change federal provisions listed in the proviso to Article 368(2) (e.g., Presidential election Art. 54–55, Union/State executive & judiciary, Seventh Schedule, representation of States, or Art. 368 itself), it must ALSO be ratified by the Legislatures of not less than one-half of the States before being presented to the President, who MUST give assent (`shall give his assent`, per 24th Amendment). Subject to Basic Structure review."
    },
    {
        "id": "proc_govt_formation",
        "node_type": "Process",
        "subcategory": "Democratic Process",
        "title": "General Elections, Formation of Government & Collective Responsibility",
        "code": "Arts. 74, 75, 81, 324, 326",
        "cluster_id": "cluster_processes",
        "authority_type": "Constitutional Text",
        "constitutional_basis": "Articles 74, 75, 81, 85, 324, 326 & Representation of the People Act, 1951",
        "summary": "Citizens aged 18+ vote under Universal Adult Suffrage (Article 326) in elections conducted by the Election Commission of India (Article 324) -> 543 MPs elected to Lok Sabha (Article 81) -> President appoints the leader commanding majority support (272+ seats) as Prime Minister (Article 75(1)) -> PM advises appointment of Council of Ministers -> Government proves majority via Vote of Confidence / Floor Test -> Council of Ministers remains in office so long as it retains the confidence of the Lok Sabha (Article 75(3); removable by No-Confidence Motion)."
    },
    {
        "id": "proc_judicial_review",
        "node_type": "Process",
        "subcategory": "Constitutional Remedy",
        "title": "Judicial Review & Writ Jurisdiction (Articles 13, 32, 226)",
        "code": "Arts. 13, 32, 226",
        "cluster_id": "cluster_processes",
        "authority_type": "Constitutional Text",
        "constitutional_basis": "Articles 13, 32, 131–136, 141–142, 226, 227, 245–246",
        "summary": "Constitutional mechanism by which the Supreme Court (Article 32) and High Courts (Article 226) examine the constitutionality of legislative enactments and executive/administrative orders against: (1) Fundamental Rights under Article 13(2), (2) Federal legislative competence under Articles 245–246, and (3) the Basic Structure Doctrine (for Constitutional Amendments). Enforced via the five prerogative writs: Habeas Corpus, Mandamus, Prohibition, Quo Warranto, and Certiorari."
    },
    {
        "id": "proc_emergency",
        "node_type": "Process",
        "subcategory": "Emergency Provisions",
        "title": "Emergency Provisions (National, State/President's Rule, Financial)",
        "code": "Part XVIII (Arts. 352–360)",
        "cluster_id": "cluster_processes",
        "authority_type": "Constitutional Text",
        "constitutional_basis": "Part XVIII (Articles 352 to 360)",
        "summary": "Three constitutional emergency regimes converting the federal system into a unitary structure during crises: (1) National Emergency (Article 352) on grounds of war, external aggression, or armed rebellion (requires written Union Cabinet decision and special majority approval by both Houses within 1 month; Articles 20 & 21 can never be suspended per Article 359); (2) Failure of Constitutional Machinery in States / President's Rule (Article 356, subject to judicial review and floor test under S.R. Bommai); and (3) Financial Emergency (Article 360, never invoked in India's history)."
    },
    {
        "id": "proc_rpa_1951",
        "node_type": "Process",
        "subcategory": "Statutory Electoral Framework",
        "title": "Representation of the People Acts, 1950 & 1951",
        "code": "Art. 327 Statutes",
        "cluster_id": "cluster_elections",
        "authority_type": "Statutory Law",
        "establishment_type": "Enacted by Parliament under Article 327",
        "constitutional_basis": "Articles 84, 102, 173, 191, 326, 327",
        "summary": "While Part XV (Articles 324–329) establishes the constitutional skeleton of elections, Parliament enacted the Representation of the People Act, 1950 (allocation of seats, delimitation, voter registration, and electoral rolls) and the Representation of the People Act, 1951 (qualifications and statutory disqualifications of MPs/MLAs, registration of political parties under Section 29A, conduct of elections, corrupt practices, and election petitions before High Courts)."
    }
]

# Explicit, directional, constitutionally grounded edges connecting Clusters, Preamble, Parts, Articles, Institutions, Administration, Philosophy, Judgments, History, and Processes
CURATED_EDGES = [
    # Root -> 16 Primary Clusters
    *[{"source": "const_india", "target": c["id"], "type": "CONTAINS", "category": "Constitutional", "ref": c["constitutional_basis"], "explanation": f"The Constitution of India structures and governs {c['title']} ({c['constitutional_basis']})."} for c in PRIMARY_CLUSTERS],

    # Cluster -> Key Constitutional & Institutional Anchors
    {"source": "cluster_rights", "target": "part_III", "type": "CONTAINS", "category": "Constitutional", "ref": "Part III (Arts. 12–35)", "explanation": "Part III of the Constitution contains the Fundamental Rights guaranteed to citizens and persons."},
    {"source": "cluster_rights", "target": "art_14", "type": "CONTAINS", "category": "Constitutional", "ref": "Article 14", "explanation": "Article 14 anchors the Right to Equality before the law and equal protection of the laws."},
    {"source": "cluster_rights", "target": "art_19", "type": "CONTAINS", "category": "Constitutional", "ref": "Article 19", "explanation": "Article 19 guarantees the six democratic freedoms of speech, assembly, association, movement, residence, and profession."},
    {"source": "cluster_rights", "target": "art_21", "type": "CONTAINS", "category": "Constitutional", "ref": "Article 21", "explanation": "Article 21 guarantees the protection of life and personal liberty."},
    {"source": "cluster_rights", "target": "art_32", "type": "CONTAINS", "category": "Constitutional", "ref": "Article 32", "explanation": "Article 32 guarantees the right to move the Supreme Court for enforcement of Fundamental Rights."},
    {"source": "cluster_dpsp", "target": "part_IV", "type": "CONTAINS", "category": "Constitutional", "ref": "Part IV (Arts. 36–51)", "explanation": "Part IV sets out the Directive Principles of State Policy."},
    {"source": "cluster_dpsp", "target": "art_38", "type": "CONTAINS", "category": "Constitutional", "ref": "Article 38", "explanation": "Article 38 directs the State to secure a social order for the promotion of welfare of the people."},
    {"source": "cluster_dpsp", "target": "art_39", "type": "CONTAINS", "category": "Constitutional", "ref": "Article 39", "explanation": "Article 39 mandates equitable distribution of material resources and prevention of concentration of wealth."},
    {"source": "cluster_duties", "target": "part_IVA", "type": "CONTAINS", "category": "Constitutional", "ref": "Part IVA (Art. 51A)", "explanation": "Part IVA enumerates the Fundamental Duties of every citizen."},
    {"source": "cluster_duties", "target": "art_51A", "type": "CONTAINS", "category": "Constitutional", "ref": "Article 51A", "explanation": "Article 51A specifies the 11 Fundamental Duties of citizens."},
    {"source": "cluster_union_exec", "target": "inst_president", "type": "CONTAINS", "category": "Institutional", "ref": "Article 52", "explanation": "The President of India is the formal head of the Union Executive under Article 52."},
    {"source": "cluster_union_exec", "target": "inst_pm", "type": "CONTAINS", "category": "Institutional", "ref": "Articles 74–75", "explanation": "The Prime Minister heads the Council of Ministers exercising real executive power."},
    {"source": "cluster_union_exec", "target": "inst_council_ministers", "type": "CONTAINS", "category": "Institutional", "ref": "Articles 74–75", "explanation": "The Union Council of Ministers aids and advises the President under Article 74."},
    {"source": "cluster_parliament", "target": "inst_parliament", "type": "CONTAINS", "category": "Institutional", "ref": "Article 79", "explanation": "Parliament is the supreme legislative organ of the Union."},
    {"source": "cluster_parliament", "target": "inst_lok_sabha", "type": "CONTAINS", "category": "Institutional", "ref": "Article 81", "explanation": "The Lok Sabha is the directly elected lower house of Parliament."},
    {"source": "cluster_parliament", "target": "inst_rajya_sabha", "type": "CONTAINS", "category": "Institutional", "ref": "Article 80", "explanation": "The Rajya Sabha is the permanent upper house representing the States."},
    {"source": "cluster_judiciary", "target": "inst_supreme_court", "type": "CONTAINS", "category": "Institutional", "ref": "Article 124", "explanation": "The Supreme Court stands at the apex of India's integrated judicial system."},
    {"source": "cluster_judiciary", "target": "inst_high_courts", "type": "CONTAINS", "category": "Institutional", "ref": "Article 214", "explanation": "High Courts head the judicial administration in each State."},
    {"source": "cluster_judiciary", "target": "inst_subordinate_courts", "type": "CONTAINS", "category": "Institutional", "ref": "Articles 233–237", "explanation": "District and Subordinate Courts form the trial backbone of the integrated judiciary."},
    {"source": "cluster_states", "target": "part_VI", "type": "CONTAINS", "category": "Constitutional", "ref": "Part VI (Arts. 152–237)", "explanation": "Part VI sets out the constitutional machinery of the States."},
    {"source": "cluster_states", "target": "inst_state_govt", "type": "CONTAINS", "category": "Institutional", "ref": "Articles 153–167", "explanation": "State Governments exercise executive and legislative authority in the States."},
    {"source": "cluster_states", "target": "inst_governor", "type": "CONTAINS", "category": "Institutional", "ref": "Article 153", "explanation": "The Governor is the constitutional head of each State."},
    {"source": "cluster_states", "target": "inst_state_legislature", "type": "CONTAINS", "category": "Institutional", "ref": "Article 168", "explanation": "State Legislatures enact laws on State and Concurrent List subjects."},
    {"source": "cluster_federalism", "target": "part_XI", "type": "CONTAINS", "category": "Constitutional", "ref": "Part XI (Arts. 245–263)", "explanation": "Part XI governs legislative and administrative relations between the Union and the States."},
    {"source": "cluster_federalism", "target": "sched_7", "type": "CONTAINS", "category": "Constitutional", "ref": "Article 246 & Seventh Schedule", "explanation": "The Seventh Schedule divides legislative subjects into the Union, State, and Concurrent Lists."},
    {"source": "cluster_federalism", "target": "inst_finance_comm", "type": "CONTAINS", "category": "Institutional", "ref": "Article 280", "explanation": "The Finance Commission adjudicates vertical and horizontal tax devolution between the Centre and States."},
    {"source": "cluster_federalism", "target": "inst_gst_council", "type": "CONTAINS", "category": "Institutional", "ref": "Article 279A", "explanation": "The GST Council is the premier cooperative federalism institution for indirect taxation."},
    {"source": "cluster_local_govt", "target": "part_IX", "type": "CONTAINS", "category": "Constitutional", "ref": "Part IX (Arts. 243–243O)", "explanation": "Part IX constitutionalizes Panchayati Raj Institutions."},
    {"source": "cluster_local_govt", "target": "part_IXA", "type": "CONTAINS", "category": "Constitutional", "ref": "Part IXA (Arts. 243P–243ZG)", "explanation": "Part IXA constitutionalizes Urban Local Bodies (Municipalities)."},
    {"source": "cluster_local_govt", "target": "inst_panchayati_raj", "type": "CONTAINS", "category": "Institutional", "ref": "Article 243B", "explanation": "Panchayati Raj Institutions form the rural third tier of democracy."},
    {"source": "cluster_local_govt", "target": "inst_municipalities", "type": "CONTAINS", "category": "Institutional", "ref": "Article 243Q", "explanation": "Municipalities form the urban third tier of democracy."},
    {"source": "cluster_const_bodies", "target": "inst_cag", "type": "CONTAINS", "category": "Institutional", "ref": "Article 148", "explanation": "The CAG is an independent constitutional authority auditing public finances."},
    {"source": "cluster_const_bodies", "target": "inst_upsc", "type": "CONTAINS", "category": "Institutional", "ref": "Article 315", "explanation": "The UPSC is an independent constitutional authority safeguarding merit recruitment."},
    {"source": "cluster_const_bodies", "target": "inst_ncsc", "type": "CONTAINS", "category": "Institutional", "ref": "Articles 338–338B", "explanation": "National Commissions for SCs, STs, and BCs monitor constitutional safeguards."},
    {"source": "cluster_elections", "target": "part_XV", "type": "CONTAINS", "category": "Constitutional", "ref": "Part XV (Arts. 324–329)", "explanation": "Part XV governs Elections in the Republic of India."},
    {"source": "cluster_elections", "target": "inst_eci", "type": "CONTAINS", "category": "Institutional", "ref": "Article 324", "explanation": "The Election Commission of India superintends and conducts free and fair elections."},
    {"source": "cluster_elections", "target": "inst_citizens", "type": "CONTAINS", "category": "Institutional", "ref": "Preamble & Article 326", "explanation": "Citizens exercise popular sovereignty as voters under Universal Adult Suffrage (Article 326)."},
    {"source": "cluster_administration", "target": "admin_ministries", "type": "CONTAINS", "category": "Administrative", "ref": "Article 77(3)", "explanation": "Union Ministries and Departments execute Union policies under the Allocation of Business Rules."},
    {"source": "cluster_administration", "target": "admin_civil_services", "type": "CONTAINS", "category": "Administrative", "ref": "Articles 309–312", "explanation": "All-India and Central/State Civil Services form the permanent administrative executive."},
    {"source": "cluster_administration", "target": "admin_dm_collector", "type": "CONTAINS", "category": "Administrative", "ref": "District Administration", "explanation": "The District Magistrate/Collector heads field administration at the district level."},
    {"source": "cluster_amendments", "target": "part_XX", "type": "CONTAINS", "category": "Constitutional", "ref": "Part XX (Article 368)", "explanation": "Part XX sets out the power and procedure to amend the Constitution."},
    {"source": "cluster_amendments", "target": "art_368", "type": "CONTAINS", "category": "Constitutional", "ref": "Article 368", "explanation": "Article 368 governs constitutional amendments."},
    {"source": "cluster_amendments", "target": "doc_basic_structure", "type": "CONTAINS", "category": "Judicial", "ref": "Kesavananda Bharati (1973)", "explanation": "The Basic Structure Doctrine defines the unamendable core of the Constitution."},
    {"source": "cluster_history", "target": "hist_const_assembly", "type": "CONTAINS", "category": "Historical", "ref": "1946–1949", "explanation": "The Constituent Assembly debated and framed the Constitution of India."},
    {"source": "cluster_history", "target": "hist_drafting_comm", "type": "CONTAINS", "category": "Historical", "ref": "29 Aug 1947", "explanation": "The Drafting Committee chaired by Dr. B.R. Ambedkar prepared the constitutional text."},
    {"source": "cluster_philosophy", "target": "preamble", "type": "CONTAINS", "category": "Constitutional", "ref": "The Preamble", "explanation": "The Preamble encapsulates the foundational political and moral philosophy of the Constitution."},
    {"source": "cluster_philosophy", "target": "phil_liberty", "type": "CONTAINS", "category": "Philosophical", "ref": "Preamble & Part III", "explanation": "Liberty is a foundational philosophical pillar of Indian constitutionalism."},
    {"source": "cluster_philosophy", "target": "phil_equality", "type": "CONTAINS", "category": "Philosophical", "ref": "Preamble & Arts. 14–18", "explanation": "Equality of status and opportunity is a core constitutional value."},
    {"source": "cluster_philosophy", "target": "phil_justice", "type": "CONTAINS", "category": "Philosophical", "ref": "Preamble & Art. 38", "explanation": "Social, economic, and political justice is the supreme objective of the Republic."},
    {"source": "cluster_philosophy", "target": "phil_fraternity", "type": "CONTAINS", "category": "Philosophical", "ref": "Preamble & Art. 51A", "explanation": "Fraternity assures the dignity of the individual and the unity and integrity of the Nation."},
    {"source": "cluster_processes", "target": "proc_ordinary_bill", "type": "CONTAINS", "category": "Process", "ref": "Articles 107–111", "explanation": "The legislative procedure transforms bills into Acts of Parliament."},
    {"source": "cluster_processes", "target": "proc_govt_formation", "type": "CONTAINS", "category": "Process", "ref": "Articles 75 & 326", "explanation": "Democratic government formation connects elections to executive authority."},
    {"source": "cluster_processes", "target": "proc_judicial_review", "type": "CONTAINS", "category": "Process", "ref": "Articles 13, 32, 226", "explanation": "Judicial review enforces constitutional supremacy across all laws and executive actions."},

    # =========================================================================
    # JOURNEY 1: Article 21 -> Right to Privacy -> Puttaswamy -> Article 14 & 19 (Golden Triangle)
    # =========================================================================
    {"source": "art_21", "target": "phil_privacy", "type": "PROTECTS", "category": "Judicial", "ref": "Article 21 & Puttaswamy (2017)", "explanation": "Article 21's guarantee of life and personal liberty encompasses the fundamental Right to Privacy as an intrinsic component of human dignity and autonomy."},
    {"source": "phil_privacy", "target": "judg_puttaswamy", "type": "ESTABLISHED_BY", "category": "Judicial", "ref": "(2017) 10 SCC 1 (9-Judge Bench)", "explanation": "In Justice K.S. Puttaswamy v. Union of India (2017), a unanimous 9-Judge Bench declared the Right to Privacy a fundamental right under Article 21 and Part III."},
    {"source": "judg_puttaswamy", "target": "doc_proportionality", "type": "DEFINES", "category": "Judicial", "ref": "(2017) 10 SCC 1", "explanation": "Puttaswamy laid down the four-prong Proportionality Test (legality, legitimate state aim, necessity, and balancing) to test any state intrusion or surveillance."},
    {"source": "judg_puttaswamy", "target": "doc_golden_triangle", "type": "INTERPRETS", "category": "Judicial", "ref": "Articles 14, 19, 21", "explanation": "Puttaswamy affirmed that privacy traverses the Golden Triangle of Articles 14, 19, and 21 rather than being confined to a single provision."},
    {"source": "art_21", "target": "judg_maneka", "type": "INTERPRETED_BY", "category": "Judicial", "ref": "(1978) 1 SCC 248", "explanation": "Maneka Gandhi v. Union of India (1978) transformed Article 21 by holding that 'procedure established by law' must be fair, just, and reasonable, not arbitrary."},
    {"source": "judg_maneka", "target": "doc_golden_triangle", "type": "ESTABLISHES", "category": "Judicial", "ref": "Articles 14, 19, 21", "explanation": "Maneka Gandhi overruled A.K. Gopalan (1950) and forged the Golden Triangle linking Articles 14, 19, and 21."},
    {"source": "doc_golden_triangle", "target": "art_14", "type": "DEPENDS_ON", "category": "Constitutional", "ref": "Article 14", "explanation": "Article 14 supplies the guarantee against arbitrariness within the Golden Triangle."},
    {"source": "doc_golden_triangle", "target": "art_19", "type": "DEPENDS_ON", "category": "Constitutional", "ref": "Article 19", "explanation": "Article 19 supplies the test of reasonable restrictions on fundamental freedoms within the Golden Triangle."},
    {"source": "doc_golden_triangle", "target": "art_21", "type": "DEPENDS_ON", "category": "Constitutional", "ref": "Article 21", "explanation": "Article 21 supplies the substantive protection of life, dignity, and personal liberty within the Golden Triangle."},
    {"source": "art_21", "target": "phil_dignity", "type": "PROTECTS", "category": "Philosophical", "ref": "Article 21 & Preamble", "explanation": "The Supreme Court has consistently held that 'life' in Article 21 means life with human dignity, not mere animal existence."},
    {"source": "art_21", "target": "judg_olga_tellis", "type": "ILLUSTRATED_BY", "category": "Judicial", "ref": "(1985) 3 SCC 545", "explanation": "Olga Tellis held that the Right to Life under Article 21 includes the Right to Livelihood."},
    {"source": "art_21", "target": "judg_dk_basu", "type": "ILLUSTRATED_BY", "category": "Judicial", "ref": "(1997) 1 SCC 416", "explanation": "D.K. Basu enforced Article 21 and 22 safeguards against custodial torture and arbitrary arrest."},
    {"source": "art_21", "target": "art_21A", "type": "RELATED_TO", "category": "Constitutional", "ref": "86th Amendment Act, 2002", "explanation": "Following Unni Krishnan (1993) reading education into Article 21, Parliament enacted Article 21A making free and compulsory education (ages 6–14) an explicit Fundamental Right."},

    # =========================================================================
    # JOURNEY 2: Parliament -> Lok Sabha -> Council of Ministers -> Prime Minister -> President
    # (Plus User Prompt Section 2 Example: Parliament & Lok Sabha expansions)
    # =========================================================================
    {"source": "inst_parliament", "target": "inst_lok_sabha", "type": "CONTAINS", "category": "Institutional", "ref": "Article 79 & Article 81", "explanation": "Under Article 79, the Lok Sabha (House of the People) is the directly elected lower chamber of Parliament."},
    {"source": "inst_parliament", "target": "inst_rajya_sabha", "type": "CONTAINS", "category": "Institutional", "ref": "Article 79 & Article 80", "explanation": "Under Article 79, the Rajya Sabha (Council of States) is the permanent upper chamber of Parliament."},
    {"source": "inst_parliament", "target": "inst_president", "type": "CONTAINS", "category": "Institutional", "ref": "Article 79", "explanation": "Under Article 79, the President of India is an integral constituent part of Parliament (summoning Houses under Art. 85 and granting assent to Bills under Art. 111)."},
    {"source": "inst_parliament", "target": "inst_parl_committees", "type": "CONTAINS", "category": "Institutional", "ref": "Articles 105 & 118", "explanation": "Parliament works through Standing Financial Committees (PAC, Estimates) and Departmentally Related Standing Committees to scrutinize legislation and budgets."},
    {"source": "inst_lok_sabha", "target": "art_81", "type": "ESTABLISHED_BY", "category": "Constitutional", "ref": "Article 81", "explanation": "Article 81 prescribes the composition of the House of the People (Lok Sabha) through direct election from territorial constituencies."},
    {"source": "inst_lok_sabha", "target": "art_83", "type": "DEFINED_BY", "category": "Constitutional", "ref": "Article 83(2)", "explanation": "Article 83(2) fixes the normal duration of the Lok Sabha at five years from the date appointed for its first meeting, unless sooner dissolved."},
    {"source": "inst_lok_sabha", "target": "art_84", "type": "DEFINED_BY", "category": "Constitutional", "ref": "Article 84", "explanation": "Article 84 sets out the constitutional qualifications for membership of Parliament (minimum age 25 years for Lok Sabha)."},
    {"source": "inst_lok_sabha", "target": "art_93", "type": "DEFINES", "category": "Constitutional", "ref": "Article 93", "explanation": "Article 93 mandates that the Lok Sabha shall choose two members of the House to be respectively Speaker and Deputy Speaker."},
    {"source": "inst_lok_sabha", "target": "inst_speaker_ls", "type": "ELECTS", "category": "Institutional", "ref": "Article 93", "explanation": "Members of the Lok Sabha elect the Speaker from among themselves under Article 93."},
    {"source": "inst_lok_sabha", "target": "art_75", "type": "EMPOWERS", "category": "Constitutional", "ref": "Article 75(3)", "explanation": "Article 75(3) makes the Union Council of Ministers collectively responsible to the House of the People (Lok Sabha)."},
    {"source": "inst_lok_sabha", "target": "proc_money_bill", "type": "EMPOWERS", "category": "Constitutional", "ref": "Articles 109 & 110", "explanation": "A Money Bill under Article 110 can only be introduced in the Lok Sabha, which holds overriding authority over financial legislation under Article 109."},
    {"source": "inst_lok_sabha", "target": "proc_rpa_1951", "type": "IMPLEMENTED_THROUGH", "category": "Legal", "ref": "Article 327 & RPA 1951", "explanation": "Direct elections to the Lok Sabha and MP qualifications/disqualifications are regulated under the Representation of the People Acts, 1950 and 1951."},
    {"source": "inst_lok_sabha", "target": "inst_council_ministers", "type": "CHECKS_AND_BALANCES", "category": "Institutional", "ref": "Article 75(3)", "explanation": "The Lok Sabha holds the Council of Ministers collectively accountable and can remove the government by passing a No-Confidence Motion."},
    {"source": "inst_council_ministers", "target": "inst_lok_sabha", "type": "ACCOUNTABLE_TO", "category": "Constitutional", "ref": "Article 75(3)", "explanation": "COLLECTIVELY_RESPONSIBLE_TO: Under Article 75(3), the Council of Ministers is collectively responsible to the House of the People (Lok Sabha). If it loses the confidence of the Lok Sabha, the entire ministry must resign."},
    {"source": "inst_council_ministers", "target": "inst_pm", "type": "HEADED_BY", "category": "Institutional", "ref": "Article 74(1)", "explanation": "Under Article 74(1), the Prime Minister sits at the head of the Council of Ministers, directing its formation, agenda, and survival."},
    {"source": "inst_pm", "target": "inst_council_ministers", "type": "EMPOWERS", "category": "Institutional", "ref": "Article 75(1)", "explanation": "Other Ministers are appointed by the President on the advice of the Prime Minister under Article 75(1)."},
    {"source": "inst_pm", "target": "inst_president", "type": "ADVISES", "category": "Constitutional", "ref": "Articles 74(1) & 78", "explanation": "The Prime Minister heads the Council of Ministers that aids and advises the President (Article 74(1)) and communicates all Cabinet decisions and legislative proposals to the President (Article 78)."},
    {"source": "inst_president", "target": "inst_pm", "type": "APPOINTS", "category": "Constitutional", "ref": "Article 75(1)", "explanation": "Under Article 75(1), the President appoints the Prime Minister (by constitutional convention, the leader who commands a majority in the Lok Sabha)."},

    # =========================================================================
    # JOURNEY 3: Fundamental Rights -> Directive Principles -> Minerva Mills -> Harmonious Construction
    # =========================================================================
    {"source": "part_III", "target": "part_IV", "type": "RELATED_TO", "category": "Constitutional", "ref": "Parts III & IV", "explanation": "Fundamental Rights (enforceable civil/political liberties in Part III) and Directive Principles (non-justiciable socio-economic goals in Part IV) together form the conscience and core charter of the Constitution."},
    {"source": "part_IV", "target": "judg_minerva", "type": "INTERPRETED_BY", "category": "Judicial", "ref": "(1980) 3 SCC 625", "explanation": "In Minerva Mills v. Union of India (1980), the Supreme Court struck down the 42nd Amendment's attempt to give all Directive Principles blanket supremacy over Fundamental Rights."},
    {"source": "part_III", "target": "judg_minerva", "type": "INTERPRETED_BY", "category": "Judicial", "ref": "(1980) 3 SCC 625", "explanation": "Minerva Mills protected Articles 14 and 19 from being subordinated to all Directive Principles under the expanded Article 31C."},
    {"source": "judg_minerva", "target": "doc_harmonious_const", "type": "ESTABLISHES", "category": "Judicial", "ref": "(1980) 3 SCC 625", "explanation": "Minerva Mills established that harmony and balance between Fundamental Rights and Directive Principles is an essential feature of the Basic Structure of the Constitution."},
    {"source": "doc_harmonious_const", "target": "part_III", "type": "INTERPRETS", "category": "Judicial", "ref": "Part III & Part IV", "explanation": "Under Harmonious Construction, Fundamental Rights are interpreted in light of Directive Principles (e.g., reading livelihood and education into Article 21)."},
    {"source": "doc_harmonious_const", "target": "part_IV", "type": "INTERPRETS", "category": "Judicial", "ref": "Part III & Part IV", "explanation": "Directive Principles guide the reasonableness of restrictions on Fundamental Rights without abrogating core Part III guarantees."},

    # =========================================================================
    # JOURNEY 4: Union Government -> State Government -> Seventh Schedule -> GST -> Finance Commission
    # =========================================================================
    {"source": "inst_council_ministers", "target": "inst_state_govt", "type": "RELATED_TO", "category": "Institutional", "ref": "Parts V, VI, XI, XII", "explanation": "The Union Government and State Governments share sovereign executive and legislative authority across India's federal architecture."},
    {"source": "inst_state_govt", "target": "sched_7", "type": "DEFINED_BY", "category": "Constitutional", "ref": "Article 246 & Seventh Schedule", "explanation": "The Seventh Schedule demarcates legislative powers between the Union and State Governments across List I (Union List), List II (State List), and List III (Concurrent List)."},
    {"source": "sched_7", "target": "art_246", "type": "IMPLEMENTED_THROUGH", "category": "Constitutional", "ref": "Article 246", "explanation": "Article 246 operationalizes the three legislative lists in the Seventh Schedule."},
    {"source": "sched_7", "target": "inst_gst_council", "type": "RELATED_TO", "category": "Constitutional", "ref": "101st Amendment (Arts. 246A & 279A)", "explanation": "The 101st Amendment modified Seventh Schedule tax entries and created Article 246A (concurrent GST power) and the GST Council (Article 279A) to coordinate Union-State indirect taxation."},
    {"source": "inst_gst_council", "target": "inst_finance_comm", "type": "RELATED_TO", "category": "Institutional", "ref": "Articles 279A & 280", "explanation": "Alongside the GST Council (which governs indirect tax rates and pooling under Art. 279A), the Finance Commission (Art. 280) governs the vertical and horizontal devolution of the divisible pool of Union taxes and grants-in-aid to the States."},
    {"source": "inst_finance_comm", "target": "art_280", "type": "ESTABLISHED_BY", "category": "Constitutional", "ref": "Article 280", "explanation": "Article 280 establishes the Finance Commission every five years to recommend tax devolution between the Union and the States."},

    # =========================================================================
    # JOURNEY 5 & "TRACE THE POWER": Voter -> Lok Sabha Election -> Majority Party ->
    # Prime Minister -> Ministry -> Department -> District Collector -> SDM -> Tehsildar -> Citizen
    # =========================================================================
    {"source": "inst_citizens", "target": "proc_govt_formation", "type": "EMPOWERS", "category": "Constitutional", "ref": "Preamble & Article 326", "explanation": "Citizens aged 18 and above exercise popular sovereignty by voting in General Elections under Universal Adult Suffrage (Article 326)."},
    {"source": "inst_citizens", "target": "inst_lok_sabha", "type": "ELECTS", "category": "Constitutional", "ref": "Articles 81 & 326", "explanation": "Voters directly elect 543 Members of Parliament to the Lok Sabha from territorial constituencies."},
    {"source": "proc_govt_formation", "target": "inst_lok_sabha", "type": "ESTABLISHES", "category": "Constitutional", "ref": "Articles 81 & 324", "explanation": "General Elections conducted by the Election Commission of India constitute the Lok Sabha and produce a majority party or coalition."},
    {"source": "inst_lok_sabha", "target": "inst_pm", "type": "EMPOWERS", "category": "Constitutional", "ref": "Article 75(1) & 75(3)", "explanation": "The leader commanding the confidence of the majority of members in the Lok Sabha is appointed Prime Minister under Article 75(1)."},
    {"source": "inst_pm", "target": "admin_ministries", "type": "EMPOWERS", "category": "Administrative", "ref": "Article 77(3) & Allocation of Business Rules", "explanation": "The Prime Minister advises the President on portfolio allocation across Union Ministries and Departments under Article 77(3)."},
    {"source": "admin_ministries", "target": "admin_civil_services", "type": "IMPLEMENTED_THROUGH", "category": "Administrative", "ref": "Articles 77 & 309–312", "explanation": "Union Ministries and Departments formulate rules, schemes, and statutory directions executed by Secretaries and officers of the All-India and Central Civil Services."},
    {"source": "admin_ministries", "target": "admin_dm_collector", "type": "IMPLEMENTED_THROUGH", "category": "Administrative", "ref": "Articles 256, 257 & Statutory Schemes", "explanation": "Central and State ministerial policies, laws, and welfare schemes flow down to the district level for field execution by the District Magistrate / Collector."},
    {"source": "admin_civil_services", "target": "admin_dm_collector", "type": "EMPOWERS", "category": "Administrative", "ref": "Article 312 & IAS Cadre Rules", "explanation": "Officers of the Indian Administrative Service (All-India Service under Article 312) and State Civil Services serve as District Magistrates / Collectors at the helm of district administration."},
    {"source": "admin_dm_collector", "target": "admin_sdm", "type": "EMPOWERS", "category": "Administrative", "ref": "State Land Revenue Codes & BNSS/CrPC", "explanation": "The District Magistrate supervises Sub-Divisional Magistrates (SDMs) managing revenue, law and order, and public service delivery across sub-divisions."},
    {"source": "admin_sdm", "target": "admin_tehsildar", "type": "EMPOWERS", "category": "Administrative", "ref": "State Land Revenue Codes", "explanation": "The SDM supervises Tehsildars and Block Development Officers (BDOs) executing land administration, certificates, and rural schemes at the tehsil/block level."},
    {"source": "admin_dm_collector", "target": "inst_citizens", "type": "ACCOUNTABLE_TO", "category": "Administrative", "ref": "Public Service Delivery, RTI Act & Art. 226", "explanation": "The District Collector delivers statutory services, land records, welfare entitlements, disaster relief, and public order directly to citizens—subject to RTI, administrative appeals, and High Court writ jurisdiction."},
    {"source": "admin_tehsildar", "target": "inst_citizens", "type": "ACCOUNTABLE_TO", "category": "Administrative", "ref": "Grassroots Governance", "explanation": "Tehsildars and BDOs are the front-line administrative officers interacting directly with citizens in villages and towns."},

    # =========================================================================
    # JOURNEY 6: Article 368 -> Constitutional Amendment -> Kesavananda Bharati ->
    # Basic Structure Doctrine -> Supreme Court
    # =========================================================================
    {"source": "art_368", "target": "proc_const_amend_bill", "type": "DEFINES", "category": "Constitutional", "ref": "Article 368", "explanation": "Article 368 defines Parliament's constituent power and special-majority procedure to amend the Constitution."},
    {"source": "proc_const_amend_bill", "target": "judg_kesavananda", "type": "INTERPRETED_BY", "category": "Judicial", "ref": "(1973) 4 SCC 225", "explanation": "In Kesavananda Bharati v. State of Kerala (1973), the 13-Judge Bench adjudicated the constitutional limits of the amending process under Article 368."},
    {"source": "art_368", "target": "judg_kesavananda", "type": "INTERPRETED_BY", "category": "Judicial", "ref": "(1973) 4 SCC 225", "explanation": "Kesavananda Bharati held that the power to 'amend' under Article 368 does not include the power to destroy the Constitution's basic structure."},
    {"source": "judg_kesavananda", "target": "doc_basic_structure", "type": "ESTABLISHES", "category": "Judicial", "ref": "(1973) 4 SCC 225", "explanation": "Kesavananda Bharati established the Basic Structure Doctrine as an implied substantive limitation on Article 368."},
    {"source": "doc_basic_structure", "target": "art_368", "type": "LIMITS", "category": "Judicial", "ref": "Kesavananda Bharati (1973) & Minerva Mills (1980)", "explanation": "The Basic Structure Doctrine limits Parliament's constituent power under Article 368, invalidating any amendment that abrogates core constitutional identity."},
    {"source": "doc_basic_structure", "target": "inst_supreme_court", "type": "IMPLEMENTED_THROUGH", "category": "Judicial", "ref": "Articles 32, 136, 141, 368", "explanation": "The Supreme Court of India exercises judicial review to test Constitutional Amendments against the Basic Structure Doctrine (as in Minerva Mills 1980, I.R. Coelho 2007, and NJAC 2015)."},
    {"source": "inst_supreme_court", "target": "doc_basic_structure", "type": "PROTECTS", "category": "Judicial", "ref": "Articles 32 & 141", "explanation": "As guardian of the Constitution, the Supreme Court enforces the Basic Structure Doctrine to preserve constitutional supremacy."},

    # =========================================================================
    # JOURNEY 7: Bill -> Parliamentary Committee -> Lok Sabha -> Rajya Sabha ->
    # President -> Act -> Rules -> Administrative Enforcement -> Judicial Review
    # =========================================================================
    {"source": "proc_ordinary_bill", "target": "inst_parl_committees", "type": "IMPLEMENTED_THROUGH", "category": "Institutional", "ref": "Article 118 & DRSC Rules", "explanation": "After introduction, Bills are referred to Departmentally Related Standing Committees for clause-by-clause scrutiny, expert testimony, and cross-party recommendations."},
    {"source": "inst_parl_committees", "target": "inst_lok_sabha", "type": "ADVISES", "category": "Institutional", "ref": "Parliamentary Procedure", "explanation": "Parliamentary Committees submit detailed reports to the Lok Sabha and Rajya Sabha to inform the Second Reading debate and amendments."},
    {"source": "proc_ordinary_bill", "target": "inst_lok_sabha", "type": "IMPLEMENTED_THROUGH", "category": "Constitutional", "ref": "Article 107", "explanation": "The Lok Sabha debates and votes on the Bill across Three Readings."},
    {"source": "inst_lok_sabha", "target": "inst_rajya_sabha", "type": "RELATED_TO", "category": "Constitutional", "ref": "Articles 107–109", "explanation": "Once passed by one House, a Bill is transmitted to the other House (Rajya Sabha) for concurrence under Article 107 (or 14-day review for Money Bills under Article 109)."},
    {"source": "inst_rajya_sabha", "target": "inst_president", "type": "RELATED_TO", "category": "Constitutional", "ref": "Article 111", "explanation": "When a Bill has been passed by both Houses of Parliament, it is presented to the President for assent under Article 111."},
    {"source": "inst_president", "target": "admin_ministries", "type": "EMPOWERS", "category": "Administrative", "ref": "Articles 53, 77 & Subordinate Legislation", "explanation": "Upon Presidential assent under Article 111, the Bill becomes an Act of Parliament and the parent Ministry frames subordinate Rules and Regulations for administrative enforcement."},
    {"source": "admin_ministries", "target": "proc_judicial_review", "type": "CHECKS_AND_BALANCES", "category": "Judicial", "ref": "Articles 13, 32, 226", "explanation": "Both the parent Act and executive rules/enforcement actions are subject to Judicial Review by the Supreme Court (Article 32) and High Courts (Article 226) for ultra vires or Fundamental Rights violations."},
    {"source": "proc_judicial_review", "target": "inst_supreme_court", "type": "IMPLEMENTED_THROUGH", "category": "Judicial", "ref": "Articles 13 & 32", "explanation": "The Supreme Court exercises judicial review to strike down unconstitutional statutes or arbitrary executive actions."},

    # =========================================================================
    # JOURNEY 8: Preamble -> Liberty/Equality/Fraternity -> Fundamental Rights ->
    # Judicial Interpretation -> Everyday Citizen Rights
    # =========================================================================
    {"source": "preamble", "target": "phil_liberty", "type": "DEFINES", "category": "Philosophical", "ref": "The Preamble", "explanation": "The Preamble resolves to secure to all citizens LIBERTY of thought, expression, belief, faith and worship."},
    {"source": "preamble", "target": "phil_equality", "type": "DEFINES", "category": "Philosophical", "ref": "The Preamble", "explanation": "The Preamble resolves to secure to all citizens EQUALITY of status and of opportunity."},
    {"source": "preamble", "target": "phil_fraternity", "type": "DEFINES", "category": "Philosophical", "ref": "The Preamble", "explanation": "The Preamble resolves to promote among all citizens FRATERNITY assuring the dignity of the individual and the unity and integrity of the Nation."},
    {"source": "preamble", "target": "phil_justice", "type": "DEFINES", "category": "Philosophical", "ref": "The Preamble", "explanation": "The Preamble resolves to secure to all citizens JUSTICE, social, economic and political."},
    {"source": "phil_liberty", "target": "part_III", "type": "IMPLEMENTED_THROUGH", "category": "Constitutional", "ref": "Articles 19–22, 25–28", "explanation": "The Preamble's ideal of Liberty is translated into enforceable Fundamental Rights in Part III (Articles 19–22 and 25–28)."},
    {"source": "phil_equality", "target": "part_III", "type": "IMPLEMENTED_THROUGH", "category": "Constitutional", "ref": "Articles 14–18", "explanation": "The Preamble's ideal of Equality is operationalized through the Equality Code in Part III (Articles 14–18)."},
    {"source": "phil_fraternity", "target": "part_III", "type": "IMPLEMENTED_THROUGH", "category": "Constitutional", "ref": "Articles 15(2), 17, 21", "explanation": "Fraternity and individual dignity animate the abolition of untouchability (Article 17), equal access to public spaces (Article 15(2)), and Article 21."},
    {"source": "part_III", "target": "proc_judicial_review", "type": "PROTECTS", "category": "Judicial", "ref": "Articles 13, 32, 226", "explanation": "Part III rights are enforced and dynamically interpreted through Judicial Review and Writ Jurisdiction under Articles 32 and 226."},
    {"source": "proc_judicial_review", "target": "inst_citizens", "type": "PROTECTS", "category": "Judicial", "ref": "Articles 32 & 226", "explanation": "Judicial interpretation of Part III directly protects everyday citizen rights—from free speech (Shreya Singhal), privacy (Puttaswamy), and workplace safety (Vishaka) to protection against arbitrary arrest (D.K. Basu)."},

    # Additional Rich Institutional, Historical & Philosophical Connections
    {"source": "hist_obj_resolution", "target": "preamble", "type": "INFLUENCED_BY", "category": "Historical", "ref": "13 Dec 1946 / 22 Jan 1947", "explanation": "Jawaharlal Nehru's Objectives Resolution formed the direct philosophical and textual foundation of the Preamble."},
    {"source": "hist_const_assembly", "target": "hist_drafting_comm", "type": "ESTABLISHES", "category": "Historical", "ref": "29 Aug 1947", "explanation": "The Constituent Assembly appointed the Drafting Committee chaired by Dr. B.R. Ambedkar on 29 August 1947."},
    {"source": "hist_drafting_comm", "target": "const_india", "type": "ESTABLISHES", "category": "Historical", "ref": "1947–1949", "explanation": "The Drafting Committee prepared and piloted the Draft Constitution through the Constituent Assembly."},
    {"source": "hist_goi_1935", "target": "sched_7", "type": "HISTORICALLY_CONNECTED_TO", "category": "Historical", "ref": "GOI Act 1935 Seventh Schedule", "explanation": "The three-list federal scheme in the Seventh Schedule evolved from the Seventh Schedule of the Government of India Act, 1935."},
    {"source": "art_32", "target": "inst_supreme_court", "type": "EMPOWERS", "category": "Constitutional", "ref": "Article 32", "explanation": "Article 32(2) empowers the Supreme Court to issue writs in the nature of habeas corpus, mandamus, prohibition, quo warranto, and certiorari."},
    {"source": "art_226", "target": "inst_high_courts", "type": "EMPOWERS", "category": "Constitutional", "ref": "Article 226", "explanation": "Article 226 empowers every High Court to issue writs for the enforcement of Fundamental Rights and for any other purpose."},
    {"source": "art_148", "target": "inst_cag", "type": "ESTABLISHES", "category": "Constitutional", "ref": "Article 148", "explanation": "Article 148 establishes the independent office of the Comptroller and Auditor-General of India."},
    {"source": "inst_cag", "target": "inst_parl_committees", "type": "ADVISES", "category": "Institutional", "ref": "Article 151 & PAC", "explanation": "The CAG's audit reports laid before Parliament under Article 151 are examined by the Public Accounts Committee (PAC) to hold ministries financially accountable."},
    {"source": "art_324", "target": "inst_eci", "type": "ESTABLISHES", "category": "Constitutional", "ref": "Article 324", "explanation": "Article 324 vests the superintendence, direction, and control of elections in the Election Commission of India."},
    {"source": "art_315", "target": "inst_upsc", "type": "ESTABLISHES", "category": "Constitutional", "ref": "Article 315", "explanation": "Article 315 establishes Public Service Commissions for the Union (UPSC) and for the States."},
    {"source": "inst_upsc", "target": "admin_civil_services", "type": "EMPOWERS", "category": "Institutional", "ref": "Article 320", "explanation": "The UPSC conducts competitive examinations for recruitment to the All-India and Central Civil Services under Article 320."},
    {"source": "art_356", "target": "judg_bommai", "type": "INTERPRETED_BY", "category": "Judicial", "ref": "(1994) 3 SCC 1", "explanation": "S.R. Bommai v. Union of India subjected proclamations of President's Rule under Article 356 to strict judicial review and mandatory floor tests."},
    {"source": "sched_10", "target": "judg_kihoto", "type": "INTERPRETED_BY", "category": "Judicial", "ref": "1992 Supp (2) SCC 651", "explanation": "Kihoto Hollohon upheld the Tenth Schedule (Anti-Defection Law) while subjecting the Speaker's disqualification orders to judicial review."},
    {"source": "sched_9", "target": "judg_coelho", "type": "INTERPRETED_BY", "category": "Judicial", "ref": "(2007) 2 SCC 1", "explanation": "I.R. Coelho held that laws placed in the Ninth Schedule after 24 April 1973 are open to challenge if they violate the Basic Structure."},
    {"source": "art_124", "target": "judg_njac", "type": "INTERPRETED_BY", "category": "Judicial", "ref": "(2016) 5 SCC 1", "explanation": "The NJAC Case struck down the 99th Amendment and preserved the Collegium system under Article 124(2) to safeguard judicial independence."},
    {"source": "art_19", "target": "judg_shreya_singhal", "type": "INTERPRETED_BY", "category": "Judicial", "ref": "(2015) 5 SCC 1", "explanation": "Shreya Singhal enforced Article 19(1)(a) free speech online by striking down Section 66A of the IT Act."},
    {"source": "art_16", "target": "judg_indra_sawhney", "type": "INTERPRETED_BY", "category": "Judicial", "ref": "1992 Supp (3) SCC 217", "explanation": "Indra Sawhney interpreted Article 16(4) to uphold 27% OBC reservations, creamy layer exclusion, and the 50% ceiling rule."},
    {"source": "art_370", "target": "judg_art370", "type": "INTERPRETED_BY", "category": "Judicial", "ref": "2023 INSC 1058", "explanation": "The 5-Judge Constitution Bench in In Re: Article 370 (2023) upheld C.O. 272 and C.O. 273 applying the entire Constitution to Jammu & Kashmir."}
]

MANDATORY_JOURNEYS = [
    {
        "id": "journey_1",
        "title": "1. Privacy & The Golden Triangle",
        "subtitle": "Article 21 → Right to Privacy → Puttaswamy → Articles 14 & 19",
        "description": "Trace how the textual protection of 'life and personal liberty' in Article 21 expanded through Maneka Gandhi (1978) and Justice K.S. Puttaswamy (2017) into a comprehensive fundamental Right to Privacy anchored in the Golden Triangle of Articles 14, 19, and 21.",
        "nodes": ["art_21", "phil_privacy", "judg_puttaswamy", "doc_golden_triangle", "art_14", "art_19"]
    },
    {
        "id": "journey_2",
        "title": "2. Parliamentary Democracy & Executive Accountability",
        "subtitle": "Parliament → Lok Sabha → Council of Ministers → Prime Minister → President",
        "description": "Explore how Westminster parliamentary accountability operates: from Parliament (Art. 79) and the directly elected Lok Sabha (Art. 81) to the collective responsibility of the Council of Ministers (Art. 75(3)), the Prime Minister's leadership (Arts. 74 & 78), and the President's constitutional role (Arts. 52, 53, 74).",
        "nodes": ["inst_parliament", "inst_lok_sabha", "inst_council_ministers", "inst_pm", "inst_president"]
    },
    {
        "id": "journey_3",
        "title": "3. Conscience of the Constitution: Rights & Directives",
        "subtitle": "Fundamental Rights → Directive Principles → Minerva Mills → Harmonious Construction",
        "description": "Follow the constitutional synthesis between enforceable civil/political Fundamental Rights (Part III) and socio-economic Directive Principles (Part IV), culminating in Minerva Mills v. Union of India (1980) and the Doctrine of Harmonious Construction.",
        "nodes": ["part_III", "part_IV", "judg_minerva", "doc_harmonious_const"]
    },
    {
        "id": "journey_4",
        "title": "4. Fiscal & Legislative Federalism",
        "subtitle": "Union Government → State Government → Seventh Schedule → GST Council → Finance Commission",
        "description": "Examine how legislative and fiscal powers are shared between New Delhi and the States through the Seventh Schedule (Art. 246), simultaneous GST taxation and the GST Council (Arts. 246A & 279A), and five-yearly tax devolution by the Finance Commission (Art. 280).",
        "nodes": ["inst_council_ministers", "inst_state_govt", "sched_7", "inst_gst_council", "inst_finance_comm"]
    },
    {
        "id": "journey_5",
        "title": "5. Democratic Chain of Governance (Voter to District)",
        "subtitle": "Voter → Election → Lok Sabha → PM → Ministry → Civil Services → District Collector → Citizen",
        "description": "Travel the complete democratic chain from a citizen casting a ballot under Article 326 through the formation of the Union Government and Ministries down to on-the-ground implementation by the District Magistrate/Collector, SDM, and Tehsildar.",
        "nodes": ["inst_citizens", "proc_govt_formation", "inst_lok_sabha", "inst_pm", "admin_ministries", "admin_civil_services", "admin_dm_collector"]
    },
    {
        "id": "journey_6",
        "title": "6. Constituent Power & Unamendable Core",
        "subtitle": "Article 368 → Amendment Process → Kesavananda Bharati → Basic Structure → Supreme Court",
        "description": "Understand how the Constitution changes while preserving its identity: Parliament's amending power under Article 368, the historic 13-Judge ruling in Kesavananda Bharati (1973), the Basic Structure Doctrine, and judicial enforcement by the Supreme Court.",
        "nodes": ["art_368", "proc_const_amend_bill", "judg_kesavananda", "doc_basic_structure", "inst_supreme_court"]
    },
    {
        "id": "journey_7",
        "title": "7. Lifecycle of a Law & Judicial Check",
        "subtitle": "Bill → Parliamentary Committee → Lok Sabha → Rajya Sabha → President → Ministry Rules → Judicial Review",
        "description": "Follow a piece of legislation from initial drafting and Standing Committee scrutiny through bicameral passage (Arts. 107–108), Presidential assent (Art. 111), subordinate rule-making, field enforcement, and constitutional testing via Judicial Review (Arts. 13, 32, 226).",
        "nodes": ["proc_ordinary_bill", "inst_parl_committees", "inst_lok_sabha", "inst_rajya_sabha", "inst_president", "admin_ministries", "proc_judicial_review"]
    },
    {
        "id": "journey_8",
        "title": "8. From Philosophical Ideals to Everyday Citizen Rights",
        "subtitle": "Preamble → Liberty, Equality & Fraternity → Part III Rights → Judicial Review → Everyday Rights",
        "description": "See how the moral promises of the Preamble (Liberty, Equality, Justice, Fraternity) are translated into enforceable Part III Fundamental Rights and interpreted by courts to protect citizens in daily life.",
        "nodes": ["preamble", "phil_liberty", "phil_equality", "phil_fraternity", "part_III", "proc_judicial_review", "inst_citizens"]
    }
]

TRACE_THE_POWER = {
    "title": "Trace the Power: Who Actually Holds Power in India?",
    "question": "How does sovereign authority flow from 'We, the People of India' through the branches of government down to district administration—and back through constitutional accountability?",
    "nodes": ["inst_citizens", "inst_eci", "inst_lok_sabha", "inst_pm", "inst_council_ministers", "inst_president", "admin_ministries", "admin_civil_services", "admin_dm_collector", "admin_sdm", "admin_tehsildar", "inst_supreme_court", "inst_cag"],
    "stages": [
        {
            "step": 1,
            "node_id": "inst_citizens",
            "role": "Ultimate Popular Sovereignty",
            "title": "We, the People of India (Citizens & Electors)",
            "constitutional_anchor": "Preamble & Article 326",
            "power_held": "Ultimate source of constituent and democratic legitimacy. Every adult citizen (18+) holds an equal vote under Article 326 and Fundamental Rights under Part III.",
            "accountability_check": "Empowers representatives every 5 years; can challenge any unconstitutional law or executive action directly in High Courts (Art. 226) or the Supreme Court (Art. 32)."
        },
        {
            "step": 2,
            "node_id": "inst_lok_sabha",
            "role": "Direct Democratic Mandate & Control of the Purse",
            "title": "Lok Sabha (House of the People)",
            "constitutional_anchor": "Articles 75(3), 81, 109, 110",
            "power_held": "543 directly elected MPs enact Union laws, hold exclusive control over Money Bills and the Union Budget (Arts. 109–114), and command the survival of the central government.",
            "accountability_check": "Can remove the Prime Minister and Council of Ministers at any time by passing a No-Confidence Motion under Article 75(3)."
        },
        {
            "step": 3,
            "node_id": "inst_pm",
            "role": "Real Executive Authority (Head of Government)",
            "title": "Prime Minister & Union Council of Ministers",
            "constitutional_anchor": "Articles 74, 75, 78",
            "power_held": "Directs national policy, legislative agenda, national security, and Union finances. Under Article 74(1), the President MUST act in accordance with the aid and advice of the Council of Ministers headed by the PM.",
            "accountability_check": "Collectively responsible to the Lok Sabha (Art. 75(3)); questioned daily during Question Hour, Zero Hour, and by Parliamentary Committees."
        },
        {
            "step": 4,
            "node_id": "inst_president",
            "role": "Constitutional Head of State",
            "title": "President of India",
            "constitutional_anchor": "Articles 52, 53, 74, 77, 111",
            "power_held": "Formal repository of Union executive power (Art. 53); all executive action is taken in the President's name (Art. 77). Appoints constitutional officers, summons Parliament, and assents to Bills (Art. 111).",
            "accountability_check": "Bound by Cabinet advice under Article 74(1) (may return advice once); removable by parliamentary impeachment for 'violation of the Constitution' under Article 61."
        },
        {
            "step": 5,
            "node_id": "admin_ministries",
            "role": "Policy Formulation & Delegated Legislation",
            "title": "Union Ministries, Departments & Permanent Civil Services",
            "constitutional_anchor": "Articles 77(3) & 309–312",
            "power_held": "Translate Cabinet decisions and Parliamentary Acts into detailed statutory Rules, Regulations, notifications, and budget allocations executed by IAS/Central Service officers.",
            "accountability_check": "Audited by the CAG (Art. 148) and scrutinized by the Public Accounts Committee, Parliamentary Standing Committees, RTI Act, and judicial review."
        },
        {
            "step": 6,
            "node_id": "admin_dm_collector",
            "role": "Field Execution at the District, Sub-Division & Tehsil",
            "title": "District Magistrate / Collector → SDM → Tehsildar",
            "constitutional_anchor": "Articles 154, 166, 243G/W, 311–312 & Statutory Codes",
            "power_held": "Where state power meets the citizen: land records, revenue, law and order (BNSS/CrPC), election conduct, disaster management, and welfare delivery.",
            "accountability_check": "Answerable to the elected State Government, State Legislature, Lokayukta, RTI Commissions, and subject to writs of Mandamus/Certiorari under Article 226."
        },
        {
            "step": 7,
            "node_id": "inst_supreme_court",
            "role": "Constitutional Guardian & Final Arbiter",
            "title": "Supreme Court & High Courts (Judicial Review)",
            "constitutional_anchor": "Articles 13, 32, 131, 141, 142, 226, 368",
            "power_held": "Strikes down parliamentary or state laws that violate Fundamental Rights (Art. 13) or federal competence (Art. 246), invalidates Constitutional Amendments that damage the Basic Structure, and issues writs against any official.",
            "accountability_check": "Bound by the text and Basic Structure of the Constitution, reasoned public judgments, larger bench review (Art. 137), and parliamentary removal process only for proved misbehaviour/incapacity (Art. 124(4))."
        }
    ]
}

SIMULATIONS = [
    {
        "id": "sim_bill_to_law",
        "title": "1. How a Bill Becomes Law",
        "category": "Legislative Process",
        "constitutional_basis": "Articles 107, 108, 109, 110, 111, 117, 368",
        "summary": "Interactive step-by-step comparison of how Ordinary Bills, Money Bills, Financial Bills, and Constitutional Amendment Bills travel through Parliament to Presidential Assent.",
        "variants": {
            "ordinary": {
                "label": "Ordinary Bill (Art. 107)",
                "house_of_origin": "Either Lok Sabha or Rajya Sabha",
                "presidential_recommendation": "Not required (except under Art. 3 for state reorganization)",
                "majority_required": "Simple Majority (majority of members present and voting)",
                "rajya_sabha_power": "Co-equal power to amend or reject (max delay 6 months before deadlock)",
                "deadlock_resolution": "Joint Sitting of both Houses summoned by President under Article 108 (presided over by Speaker of Lok Sabha)",
                "presidential_assent": "Under Article 111: (1) Grant Assent, (2) Withhold Assent, or (3) Return for reconsideration (Suspensive Veto; if passed again, President must assent)"
            },
            "money": {
                "label": "Money Bill (Arts. 109–110)",
                "house_of_origin": "ONLY in the Lok Sabha (Art. 109(1)); certified by Speaker under Art. 110(3)",
                "presidential_recommendation": "Mandatory prior recommendation of the President (Art. 117(1))",
                "majority_required": "Simple Majority in Lok Sabha",
                "rajya_sabha_power": "Cannot amend or reject; must return within 14 days with or without recommendations, which Lok Sabha may accept or reject (Art. 109(2))",
                "deadlock_resolution": "No deadlock possible; NO Joint Sitting",
                "presidential_assent": "Under Article 111: Grant Assent or Withhold Assent (cannot return a Money Bill for reconsideration)"
            },
            "financial": {
                "label": "Financial Bill Cat. I & II (Art. 117)",
                "house_of_origin": "Category I (Art. 117(1)): ONLY in Lok Sabha; Category II (Art. 117(3)): Either House",
                "presidential_recommendation": "Cat. I: Prior recommendation for introduction; Cat. II: Recommendation required before consideration",
                "majority_required": "Simple Majority in both Houses",
                "rajya_sabha_power": "Full power to amend or reject (treated like an Ordinary Bill after introduction)",
                "deadlock_resolution": "Joint Sitting under Article 108 is permissible",
                "presidential_assent": "Under Article 111: Grant Assent, Withhold Assent, or Return for reconsideration"
            },
            "amendment": {
                "label": "Constitutional Amendment Bill (Art. 368)",
                "house_of_origin": "Either Lok Sabha or Rajya Sabha (never in a State Legislature)",
                "presidential_recommendation": "Not required",
                "majority_required": "Special Majority in EACH House separately (>50% of total membership + >=2/3rds of members present and voting) + ratification by >=50% State Legislatures for federal provisions (Art. 368(2) proviso)",
                "rajya_sabha_power": "Co-equal constituent power; must pass in Rajya Sabha separately by Special Majority",
                "deadlock_resolution": "NO Joint Sitting permissible; if either House fails to pass by Special Majority, the Bill lapses",
                "presidential_assent": "Mandatory: President 'shall give his assent' under Article 368(2) (amended by 24th Amendment Act, 1971); cannot withhold or return"
            }
        },
        "steps": [
            {"step": 1, "title": "Drafting & Pre-Legislative Consultation", "node_id": "admin_ministries", "ref": "Art. 77(3)", "detail": "Concerned Ministry prepares legislative proposal, consults Law Ministry (Legislative Department), obtains Union Cabinet approval, and drafts the Bill."},
            {"step": 2, "title": "First Reading (Introduction in House)", "node_id": "inst_lok_sabha", "ref": "Art. 107 / 109", "detail": "Minister or Private Member moves for leave to introduce the Bill. Title and objectives are read and published in the Gazette of India."},
            {"step": 3, "title": "Standing Committee Scrutiny", "node_id": "inst_parl_committees", "ref": "Art. 118", "detail": "Speaker/Chairman refers the Bill to one of the 24 Departmentally Related Standing Committees (DRSCs) for detailed examination, stakeholder input, and a bipartisan report."},
            {"step": 4, "title": "Second Reading (Clause-by-Clause Consideration)", "node_id": "inst_lok_sabha", "ref": "Art. 100", "detail": "General discussion on principles followed by clause-by-clause consideration and voting on amendments."},
            {"step": 5, "title": "Third Reading & Passage in First House", "node_id": "inst_lok_sabha", "ref": "Art. 100 / 368", "detail": "Final debate confined to acceptance or rejection of the Bill as a whole; passed by Simple Majority (or Special Majority for Art. 368)."},
            {"step": 6, "title": "Consideration by the Second House", "node_id": "inst_rajya_sabha", "ref": "Arts. 107–109", "detail": "Transmitted to the other House. Ordinary Bills require concurrence (or Art. 108 Joint Sitting); Money Bills must be returned by Rajya Sabha within 14 days."},
            {"step": 7, "title": "Presidential Assent & Gazette Notification", "node_id": "inst_president", "ref": "Art. 111 / 368(2)", "detail": "Presented to the President under Article 111. Upon assent, the Bill becomes an Act of Parliament and is notified in the Official Gazette."}
        ]
    },
    {
        "id": "sim_govt_formation",
        "title": "2. Formation of Government & Parliamentary Confidence",
        "category": "Democratic Process",
        "constitutional_basis": "Articles 74, 75, 81, 85, 324, 326",
        "summary": "From General Election notification by the Election Commission to the swearing-in of the Prime Minister, Floor Test, and No-Confidence Motion mechanics.",
        "steps": [
            {"step": 1, "title": "General Election Notification & Polling", "node_id": "inst_eci", "ref": "Arts. 324 & 326", "detail": "Election Commission of India conducts elections across 543 Lok Sabha constituencies under Universal Adult Suffrage."},
            {"step": 2, "title": "Constitution of New Lok Sabha & Majority Claim", "node_id": "inst_lok_sabha", "ref": "Art. 81 & RPA 1951 s. 73", "detail": "ECI notifies elected MPs. The party or pre/post-poll coalition commanding 272+ seats elects its parliamentary leader."},
            {"step": 3, "title": "Invitation & Appointment of Prime Minister", "node_id": "inst_president", "ref": "Art. 75(1)", "detail": "President appoints the majority leader as Prime Minister (or in a hung House, invites the leader most likely to command a majority subject to an immediate Floor Test)."},
            {"step": 4, "title": "Oath of Office & Portfolio Allocation", "node_id": "inst_pm", "ref": "Art. 75(1)–(4), Third Schedule", "detail": "On PM's advice, President appoints Cabinet Ministers and Ministers of State (capped at 15% of Lok Sabha strength under Art. 75(1A)) and allocates Ministries under Art. 77(3)."},
            {"step": 5, "title": "Floor Test / Motion of Confidence", "node_id": "inst_council_ministers", "ref": "Art. 75(3)", "detail": "The Council of Ministers proves majority support on the floor of the Lok Sabha."},
            {"step": 6, "title": "Continuous Collective Responsibility & No-Confidence Motion", "node_id": "inst_lok_sabha", "ref": "Art. 75(3) & LS Rule 198", "detail": "Any MP supported by 50 members may move a Motion of No-Confidence in the Lok Sabha. If passed by simple majority, the Prime Minister and entire Council of Ministers must resign."}
        ]
    },
    {
        "id": "sim_judicial_review",
        "title": "3. Judicial Review & Constitutional Remedies in Action",
        "category": "Judicial Process",
        "constitutional_basis": "Articles 13, 32, 136, 141, 142, 226, 246",
        "summary": "Trace how an executive order or statute is challenged by a citizen before a High Court (Art. 226) or the Supreme Court (Art. 32) and tested against the Constitution.",
        "steps": [
            {"step": 1, "title": "Impugned State Action (Statute or Executive Order)", "node_id": "admin_ministries", "ref": "Art. 12 & Art. 13(3)", "detail": "Parliament/State Legislature enacts a statute or a Ministry/District Collector issues an executive order affecting citizen rights."},
            {"step": 2, "title": "Invocation of Writ Jurisdiction (Art. 32 or Art. 226)", "node_id": "inst_citizens", "ref": "Arts. 32 & 226", "detail": "Aggrieved citizen or Public Interest Litigant (PIL) files a Writ Petition before the High Court (Art. 226) or directly before the Supreme Court (Art. 32 for Fundamental Rights)."},
            {"step": 3, "title": "Threshold Test: Federal Competence (Arts. 245–246)", "node_id": "sched_7", "ref": "Arts. 245, 246 & 7th Schedule", "detail": "Court first examines whether the legislature had competence under the Union, State, or Concurrent List using the Doctrine of Pith and Substance."},
            {"step": 4, "title": "Substantive Test: Golden Triangle & Proportionality", "node_id": "doc_golden_triangle", "ref": "Arts. 13(2), 14, 19, 21", "detail": "Court tests whether the law or order is arbitrary (Art. 14), imposes disproportionate restrictions on freedoms (Art. 19), or violates fair procedure/dignity/privacy (Art. 21)."},
            {"step": 5, "title": "Constitutional Remedy: Severability, Reading Down, or Striking Down", "node_id": "inst_supreme_court", "ref": "Arts. 13(2), 32(2), 141, 142", "detail": "Court issues appropriate Writ (Certiorari/Mandamus/Habeas Corpus), reads down or strikes down the unconstitutional provision as void under Article 13(2), binding all authorities nationwide under Article 141."}
        ]
    },
    {
        "id": "sim_amendment_368",
        "title": "4. Amending the Constitution (Article 368 & Basic Structure)",
        "category": "Constituent Process",
        "constitutional_basis": "Article 368 & Kesavananda Bharati (1973)",
        "summary": "Explore the three tiers of constitutional change in India and how the Supreme Court tests amendments against the Basic Structure Doctrine.",
        "steps": [
            {"step": 1, "title": "Classify the Constitutional Provision", "node_id": "art_368", "ref": "Arts. 4, 169, 239A, 368(2)", "detail": "(A) Simple Majority outside Art. 368 (e.g., new States under Arts. 2–4); (B) Special Majority under Art. 368(2) (e.g., Fundamental Rights, DPSPs); or (C) Special Majority + Ratification by >=1/2 State Legislatures under Art. 368(2) Proviso (e.g., Seventh Schedule, GST, Art. 368)."},
            {"step": 2, "title": "Introduction in Either House of Parliament", "node_id": "inst_parliament", "ref": "Art. 368(2)", "detail": "Bill introduced in Lok Sabha or Rajya Sabha (no prior Presidential recommendation needed; cannot be introduced in a State Legislature)."},
            {"step": 3, "title": "Separate Passage by Special Majority in Both Houses", "node_id": "inst_lok_sabha", "ref": "Art. 368(2)", "detail": "Each House must independently pass the Bill by >50% of total membership AND >=2/3rds of members present and voting. No Joint Sitting is allowed."},
            {"step": 4, "title": "Federal Ratification by State Legislatures (If Applicable)", "node_id": "inst_state_legislature", "ref": "Proviso to Art. 368(2)", "detail": "If entrenched federal articles are amended, at least half of the State Legislatures must pass resolutions ratifying the amendment by simple majority."},
            {"step": 5, "title": "Mandatory Presidential Assent", "node_id": "inst_president", "ref": "Art. 368(2) (24th Amendment)", "detail": "Upon presentation, the President 'shall give his assent to the Bill' and the Constitution stands amended."},
            {"step": 6, "title": "Basic Structure Review by Supreme Court", "node_id": "doc_basic_structure", "ref": "Kesavananda Bharati (1973)", "detail": "If challenged under Article 32, a Constitution Bench examines whether the amendment damages or destroys any basic feature of the Constitution (e.g., judicial independence in the NJAC Case, 2015)."}
        ]
    },
    {
        "id": "sim_centre_state",
        "title": "5. Centre–State Relations & Federal Dispute Resolution",
        "category": "Federal Process",
        "constitutional_basis": "Articles 131, 245–263, 279A, 280, 355–356 & Seventh Schedule",
        "summary": "Simulate how legislative conflicts, fiscal transfers, and emergency interventions work between the Union and the States.",
        "steps": [
            {"step": 1, "title": "Allocation of Subject Matter (Seventh Schedule)", "node_id": "sched_7", "ref": "Art. 246 & 7th Schedule", "detail": "Union legislates exclusively on List I (Defence, Foreign Affairs, Currency, Banking); States on List II (Public Order, Police, Public Health, Agriculture, Land); both on List III (Criminal Law, Education, Forests, Marriage)."},
            {"step": 2, "title": "Resolving Concurrent List Conflicts (Repugnancy)", "node_id": "doc_pith_substance", "ref": "Art. 254", "detail": "If a State law on a Concurrent List item conflicts with a Parliamentary law, the Parliamentary law prevails (Art. 254(1)), UNLESS the State law was reserved for and received the President's assent (Art. 254(2))."},
            {"step": 3, "title": "Fiscal Federalism: Finance Commission & GST Council", "node_id": "inst_finance_comm", "ref": "Arts. 246A, 270, 279A, 280", "detail": "Union taxes are shared with States per Finance Commission recommendations (Art. 280), while GST rates and revenue-sharing are decided jointly in the GST Council (Art. 279A)."},
            {"step": 4, "title": "Inter-State Water & Federal Disputes", "node_id": "inst_supreme_court", "ref": "Arts. 131, 262, 263", "explanation": "Legal disputes between the Union and States are adjudicated exclusively by the Supreme Court under Article 131; Inter-State river water disputes are referred to tribunals under Article 262."},
            {"step": 5, "title": "Constitutional Breakdown & Floor Test Safeguard", "node_id": "judg_bommai", "ref": "Art. 356 & S.R. Bommai (1994)", "detail": "Article 356 allows President's Rule only upon genuine breakdown of constitutional machinery, subject to Parliamentary approval within 2 months and judicial review."}
        ]
    },
    {
        "id": "sim_rights_scenarios",
        "title": "6. Constitutional Rights in Everyday Scenarios",
        "category": "Citizen Rights",
        "constitutional_basis": "Part III (Articles 14, 15, 19, 20, 21, 21A, 22, 25, 32) & Article 226",
        "summary": "Interactive real-world citizen scenarios showing which Constitutional Articles, Landmark Judgments, and Remedies apply when rights are tested.",
        "steps": [
            {"step": 1, "title": "Scenario A: Unlawful Detention or Custodial Abuse", "node_id": "art_22", "ref": "Arts. 21, 22(1)–(2), 32, 226 & D.K. Basu (1997)", "detail": "Right to be informed of grounds of arrest, consult a lawyer of choice (Art. 22(1)), and be produced before the nearest Magistrate within 24 hours (Art. 22(2)). Immediate remedy: Writ of Habeas Corpus under Art. 226 or Art. 32."},
            {"step": 2, "title": "Scenario B: Censorship of Peaceful Online Speech or Protest", "node_id": "art_19", "ref": "Art. 19(1)(a)–(b), 19(2) & Shreya Singhal (2015)", "detail": "Protected under Freedom of Speech and Expression (Art. 19(1)(a)) and Peaceful Assembly (Art. 19(1)(b)). State restriction is valid only if backed by a law narrowly tailored to grounds in Art. 19(2) (public order, sovereignty, incitement)."},
            {"step": 3, "title": "Scenario C: Intrusive State Surveillance or Data Breach", "node_id": "phil_privacy", "ref": "Art. 21 & Puttaswamy (2017)", "detail": "Protected by the Fundamental Right to Privacy (informational self-determination and bodily/spatial privacy). Must satisfy the 4-step Proportionality Test."},
            {"step": 4, "title": "Scenario D: Denial of School Admission to a Child (Age 6–14)", "node_id": "art_21A", "ref": "Art. 21A (86th Amendment) & RTE Act 2009", "detail": "Direct violation of the Fundamental Right to Free and Compulsory Education under Article 21A; enforceable via local authority grievance redressal and Writ of Mandamus under Art. 226."},
            {"step": 5, "title": "Scenario E: Caste or Gender Discrimination in Public Access or Employment", "node_id": "art_15", "ref": "Arts. 14, 15, 16, 17 & Vishaka (1997)", "detail": "Prohibited by Articles 14, 15(1)–(2), 16(1)–(2), and 17. Enforceable via constitutional courts, National Commissions (Arts. 338–338B), and statutory protection acts."}
        ]
    }
]

HISTORICAL_TIMELINE = [
    {"year": "1935", "date": "2 Aug 1935", "category": "Pre-1950 Antecedent", "title": "Government of India Act, 1935", "node_id": "hist_goi_1935", "ref": "Repealed by Art. 395", "summary": "Established federal legislative lists, provincial autonomy, and a Federal Court, later adapted and democratized by the Constituent Assembly."},
    {"year": "1946", "date": "9 Dec 1946", "category": "Constituent Assembly", "title": "First Sitting of the Constituent Assembly", "node_id": "hist_const_assembly", "ref": "CAD Vol. I", "summary": "Constituent Assembly convenes in the Constitution Hall (Central Hall of Parliament); Dr. Rajendra Prasad elected permanent President on 11 Dec 1946."},
    {"year": "1946", "date": "13 Dec 1946", "category": "Constituent Assembly", "title": "Objectives Resolution Moved by Jawaharlal Nehru", "node_id": "hist_obj_resolution", "ref": "CAD Vol. I (Adopted 22 Jan 1947)", "summary": "Proclaimed India an Independent Sovereign Republic guaranteeing social, economic, and political justice, liberty, and equality."},
    {"year": "1947", "date": "29 Aug 1947", "category": "Constituent Assembly", "title": "Appointment of the Drafting Committee (Chaired by Dr. B.R. Ambedkar)", "node_id": "hist_drafting_comm", "ref": "CAD Vol. V", "summary": "Seven-member Drafting Committee appointed under Dr. B.R. Ambedkar to scrutinized B.N. Rau's initial draft and author the Draft Constitution."},
    {"year": "1949", "date": "26 Nov 1949", "category": "Founding Milestone", "title": "Adoption & Enactment of the Constitution of India", "node_id": "hist_adoption_1949", "ref": "Preamble & Art. 394", "summary": "After 165 sitting days over 2 years, 11 months, and 18 days, the Constituent Assembly adopts the Constitution (395 Articles, 8 Schedules)."},
    {"year": "1950", "date": "26 Jan 1950", "category": "Founding Milestone", "title": "Commencement of the Constitution (Republic Day)", "node_id": "const_india", "ref": "Article 394", "summary": "The Constitution enters into full force; India becomes a Sovereign Democratic Republic and the Supreme Court of India is inaugurated on 28 Jan 1950."},
    {"year": "1950", "date": "19 May 1950", "category": "Landmark Judgment", "title": "A.K. Gopalan v. State of Madras", "node_id": "judg_gopalan", "ref": "AIR 1950 SC 27", "summary": "Early positivist reading of Article 21 ('procedure established by law'), with Justice Fazl Ali's historic dissent laying the seed for Maneka Gandhi (1978)."},
    {"year": "1951", "date": "18 Jun 1951", "category": "Constitutional Amendment", "title": "1st Constitutional Amendment Act, 1951", "node_id": "amend_1", "ref": "Arts. 15(4), 19(2), 31A, 31B, 9th Schedule", "summary": "Protected agrarian land reforms from judicial invalidation, enabled substantive equality provisions (Art. 15(4)), and added Ninth Schedule."},
    {"year": "1956", "date": "1 Nov 1956", "category": "Constitutional Amendment", "title": "7th Amendment & States Reorganisation Act, 1956", "node_id": "part_I", "ref": "Art. 1, 3 & First Schedule", "summary": "Abolished Part A, B, C, D classification of States and reorganized Indian States predominantly along linguistic and administrative lines."},
    {"year": "1967", "date": "27 Feb 1967", "category": "Landmark Judgment", "title": "I.C. Golaknath v. State of Punjab (11-Judge Bench)", "node_id": "judg_golaknath", "ref": "AIR 1967 SC 1643", "summary": "Ruled 6:5 that Parliament could not abridge Fundamental Rights under Article 368, triggering a major institutional debate over constituent power."},
    {"year": "1973", "date": "24 Apr 1973", "category": "Landmark Judgment", "title": "Kesavananda Bharati v. State of Kerala (13-Judge Bench)", "node_id": "judg_kesavananda", "ref": "(1973) 4 SCC 225", "summary": "Established the Basic Structure Doctrine: Parliament can amend any part of the Constitution under Art. 368 provided it does not alter or destroy its basic structure."},
    {"year": "1976", "date": "18 Dec 1976", "category": "Constitutional Amendment", "title": "42nd Constitutional Amendment Act, 1976", "node_id": "amend_42", "ref": "Preamble, Part IVA (Art. 51A), Arts. 39A, 43A, 48A", "summary": "Added 'Socialist', 'Secular', and 'Integrity' to the Preamble and Fundamental Duties (Part IVA) during the Internal Emergency."},
    {"year": "1978", "date": "25 Jan 1978", "category": "Landmark Judgment", "title": "Maneka Gandhi v. Union of India (7-Judge Bench)", "node_id": "judg_maneka", "ref": "(1978) 1 SCC 248", "summary": "Overruled Gopalan; forged the Golden Triangle (Arts. 14, 19, 21) and required that any procedure depriving liberty under Art. 21 must be fair, just, and reasonable."},
    {"year": "1978", "date": "30 Apr 1979", "category": "Constitutional Amendment", "title": "44th Constitutional Amendment Act, 1978", "node_id": "amend_44", "ref": "Arts. 20, 21, 74, 300A, 352, 359", "summary": "Restored post-Emergency democratic safeguards, made Articles 20 and 21 non-suspendable during Emergency, and moved Property to Article 300A."},
    {"year": "1980", "date": "31 Jul 1980", "category": "Landmark Judgment", "title": "Minerva Mills v. Union of India", "node_id": "judg_minerva", "ref": "(1980) 3 SCC 625", "summary": "Struck down Art. 368(4)–(5) and affirmed that judicial review and harmony between Part III and Part IV are part of the Basic Structure."},
    {"year": "1985", "date": "1 Mar 1985", "category": "Constitutional Amendment", "title": "52nd Amendment (Tenth Schedule Anti-Defection) & 61st Amendment (1989 Voting Age 18)", "node_id": "sched_10", "ref": "Tenth Schedule & Art. 326", "summary": "Curbed political defections via the Tenth Schedule (1985) and lowered the voting age from 21 to 18 years under Article 326 (61st Amendment, 1989)."},
    {"year": "1992", "date": "16 Nov 1992", "category": "Landmark Judgment", "title": "Indra Sawhney (Mandal Case) & 73rd/74th Amendments (Local Self-Govt)", "node_id": "judg_indra_sawhney", "ref": "1992 Supp (3) SCC 217; Parts IX & IXA", "summary": "Upheld 27% OBC reservation under Art. 16(4) with creamy layer exclusion; Parliament enacted Parts IX and IXA constitutionalizing Panchayats and Municipalities."},
    {"year": "1994", "date": "11 Mar 1994", "category": "Landmark Judgment", "title": "S.R. Bommai v. Union of India (9-Judge Bench)", "node_id": "judg_bommai", "ref": "(1994) 3 SCC 1", "summary": "Declared Federalism and Secularism part of the Basic Structure and curbed arbitrary misuse of Article 356 via judicial review and mandatory floor tests."},
    {"year": "2002", "date": "12 Dec 2002", "category": "Constitutional Amendment", "title": "86th Amendment Act, 2002 (Right to Education - Art. 21A)", "node_id": "amend_86", "ref": "Articles 21A, 45, 51A(k)", "summary": "Made free and compulsory education for children aged 6 to 14 years an enforceable Fundamental Right under Article 21A."},
    {"year": "2016", "date": "8 Sep 2016", "category": "Constitutional Amendment", "title": "101st Amendment Act, 2016 (Goods and Services Tax)", "node_id": "amend_101", "ref": "Articles 246A, 269A, 279A", "summary": "Introduced cooperative fiscal federalism for indirect taxation via GST and established the constitutional GST Council."},
    {"year": "2017", "date": "24 Aug 2017", "category": "Landmark Judgment", "title": "Justice K.S. Puttaswamy v. Union of India (9-Judge Bench)", "node_id": "judg_puttaswamy", "ref": "(2017) 10 SCC 1", "summary": "Unanimously affirmed the Fundamental Right to Privacy under Article 21 and Part III and established the four-part Proportionality Test."},
    {"year": "2023", "date": "28 Sep 2023", "category": "Constitutional Amendment", "title": "106th Amendment Act, 2023 & In Re: Article 370 Judgment", "node_id": "amend_106", "ref": "Arts. 239AA, 330A, 332A, 334A; 2023 INSC 1058", "summary": "Enacted 33% reservation for women in Lok Sabha and State Assemblies (106th Amendment) and upheld constitutional integration under Article 370."}
]

AUTHORITATIVE_SOURCES = [
    {
        "id": "src_const_2026_leg",
        "title": "The Constitution of India (As on 1st May, 2026 — Incorporating up to the 106th Constitutional Amendment Act, 2023)",
        "category": "Constitutional Text",
        "authority": "Ministry of Law and Justice, Legislative Department, Government of India",
        "publication_date": "2026-05-01",
        "url": "https://www.legislative.gov.in/static/uploads/2025/07/88cca69e868e50b217f855be2fb8bdba.pdf",
        "verification_status": "Official Primary Source (Ingested 402-page PDF)",
        "pages": 402
    },
    {
        "id": "src_const_2026_indiacode",
        "title": "The Constitution of India — Official Digital Repository Edition (10 September 2026 Edition)",
        "category": "Constitutional Text",
        "authority": "India Code, Legislative Department, Ministry of Law and Justice",
        "publication_date": "2026-09-10",
        "url": "https://indiacode.gov.in/server/api/core/bitstreams/2bd776ff-891e-444c-9344-f63df7b299fc/content",
        "verification_status": "Official Primary Source",
        "pages": 402
    },
    {
        "id": "src_sci_constitution",
        "title": "Supreme Court of India — Constitutional Jurisprudence & Landmark Judgments Portal",
        "category": "Judicial Interpretation",
        "authority": "Supreme Court of India (e-SCR / Official Reports)",
        "publication_date": "2026",
        "url": "https://www.sci.gov.in/constitution/",
        "verification_status": "Official Judicial Repository",
        "pages": None
    },
    {
        "id": "src_cad_volumes",
        "title": "Constituent Assembly Debates (Official Report, Volumes I to XII, 9 Dec 1946 – 24 Jan 1950)",
        "category": "Historical Evidence",
        "authority": "Lok Sabha Secretariat, Parliament of India",
        "publication_date": "1950",
        "url": "https://eparlib.nic.in/handle/123456789/760448",
        "verification_status": "Official Parliamentary Archive",
        "pages": 5500
    },
    {
        "id": "src_rpa_1950_1951",
        "title": "Representation of the People Act, 1950 (Act 43 of 1950) & Representation of the People Act, 1951 (Act 43 of 1951)",
        "category": "Statutory Law",
        "authority": "Parliament of India / Election Commission of India",
        "publication_date": "1951",
        "url": "https://www.eci.gov.in/electoral-laws",
        "verification_status": "Official Statutory Enactment",
        "pages": None
    },
    {
        "id": "src_aob_rules_1961",
        "title": "Government of India (Allocation of Business) Rules, 1961 & (Transaction of Business) Rules, 1961 (Under Article 77(3))",
        "category": "Administrative Practice",
        "authority": "Cabinet Secretariat, Government of India",
        "publication_date": "1961",
        "url": "https://cabsec.gov.in/allocationofbusinessrules/",
        "verification_status": "Official Executive Rules",
        "pages": None
    }
]
